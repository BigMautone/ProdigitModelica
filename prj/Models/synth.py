import os
import sys
import math
import numpy as np
import time
import os.path

from OMPython import OMCSessionZMQ


os.system("rm -f ./System")      # .... to be on the safe side

omc = OMCSessionZMQ()
omc.sendExpression("getVersion()")
omc.sendExpression("cd()")

omc.sendExpression("loadModel(Modelica)")
omc.sendExpression("getErrorString()")

omc.sendExpression("loadFile(\"randomGenerator.mo\")")
omc.sendExpression("getErrorString()")

omc.sendExpression("loadFile(\"connectors.mo\")")
omc.sendExpression("getErrorString()")

omc.sendExpression("loadFile(\"aule.mo\")")
omc.sendExpression("getErrorString()")

omc.sendExpression("loadFile(\"studenti.mo\")")
omc.sendExpression("getErrorString()")

omc.sendExpression("loadFile(\"gomp.mo\")")
omc.sendExpression("getErrorString()")

omc.sendExpression("loadFile(\"prodigit.mo\")")
omc.sendExpression("getErrorString()")

omc.sendExpression("loadFile(\"MonitorSafety.mo\")")
omc.sendExpression("getErrorString()")

omc.sendExpression("loadFile(\"MonitorLiveness.mo\")")
omc.sendExpression("getErrorString()")

omc.sendExpression("loadFile(\"MonitorDown.mo\")")
omc.sendExpression("getErrorString()")

omc.sendExpression("loadFile(\"system.mo\")")
omc.sendExpression("getErrorString()")

omc.sendExpression("buildModel(System, stopTime = 300)")
omc.sendExpression("getErrorString()")

startTime = time.time()
num_pass = 0
num_fail = 0
down = False

with open ("logMonitorNonFunz", 'wt') as f:
        f.write("Begin log"+"\n")
        f.flush()
        os.fsync(f)
        
with open ("outputMonitorNotFunz.txt", 'wt') as f:
        f.write("Outcomes"+"\n\n")
        f.flush()
        os.fsync(f)
        
for i in range(1000):
	
	
	with open("newValues.txt", 'wt') as f:
		rand1 = np.random.rand()
		f.write("gomp.probDown="+str(rand1)+"\n")
		f.flush()
		os.fsync(f)
		
		
	with open ("logMonitorNonFunz", 'a') as f:
		f.write("\nTest "+str(i)+" : ")
		f.write("Probabilita' che gomp sia down = " + str(rand1) + "\n")
		f.flush()
		os.fsync(f)
	
	os.system("./System -overrideFile=newValues.txt >> logMonitorNonFunz")
	#time.sleep(1.0) # Delay to avoid races on file re-writings. Can be dropped for non-toy examples.
	os.system("rm -f newValues.txt") # .... to be on the safe side
	
	down = omc.sendExpression("val(down.downReq, 150.0, \"System_res.mat\")")
	prodDown = omc.sendExpression("val(down.numProd, 150.0, \"System_res.mat\")")
	gompDown = omc.sendExpression("val(down.numGomp, 150.0, \"System_res.mat\")")
	
	#print(str(omc.sendExpression("val(gomp.probDown, 150.0, \"System_res.mat\")")))
	
	os.system("rm -f System_res.mat")      # .... to be on the safe side
        
	print("Monitor value at iteration", i, ": ", str(down),"- with gomp down probability = ", rand1)
	
	with open ("outputMonitorNotFunz.txt", 'a') as g:
		if (not down):
			num_pass = num_pass + 1.0
			g.write("Down["+str(i)+"] = "+str(down)+": test passato con probabilita' che il gomp vada down = "+str(rand1)+
			" (Gomp down "+str(gompDown)+ "volte); Prodigit down "+str(prodDown)+ " volte);\n")
		else:
			num_fail = num_fail + 1.0
			g.write("Down["+str(i)+"] = "+str(down)+": testo non passato con probabilita' che il gomp vada down = "+str(rand1)+
			" (Gomp down "+str(gompDown)+ "volte); Prodigit down "+str(prodDown)+ " volte);\n")
		g.flush()
		os.fsync(g)
	
with open ("outputMonitorNotFunz.txt", 'a') as g:
	g.write("CPU time = "+str(time.time()-startTime)+"\n")
	g.flush()
	os.fsync(g)
	
print("Execution time = ", (time.time()-startTime))
print ("num pass = ", num_pass)
print ("num fail = ", num_fail)
print ("total tests = ",  num_pass + num_fail)
print ("pass prob = ", num_pass/(num_pass + num_fail))
print ("fail prob = ", num_fail/(num_pass + num_fail))

