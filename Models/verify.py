import os
import sys
import math
import numpy as np
import time
import os.path

#from OMPython import OMCSessionZMQ
import OMPython

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

random.seed(1)

numPass = 0
numFail = 0
y = False

with open ("log", 'wt') as f:
        f.write("Begin log"+"\n")
        f.flush()
        os.fsync(f)
        
with open ("output.txt", 'wt') as f:
        f.write("Outcomes"+"\n\n")
        f.flush()
        os.fsync(f)
        
for i in range(100):
	
	with open("parametri.txt", "wt") as f:
		rand1 = random.random()
		f.write("stud.prob.pren = "+str(rand1)+"\n")
		f.flush()
		os.fsync(f)
		
		
	with open ("log", 'a') as f:
		f.write("\nTest "+str(i)+" :\n")
		f.flush()
		os.fsync(f)
	
	os.system("./System -overrideFile=parametri.txt >> log")
	time.sleep(1.0) # Delay to avoid races on file re-writings. Can be dropped for non-toy examples.
	#os.system("rm -f parametri.txt") # .... to be on the safe side
	
	y = omc.sendExpression("val(saf.safety, 150.0, \"System_res.mat\")")
	os.system("rm -f System_res.mat")      # .... to be on the safe side
        
	print("Monitor value at iteration", i, ": ", y)
	
	with open ("output.txt", 'a') as g:
		if (not y):
			num_pass = num_pass + 1.0
			g.write("y["+str(i)+"] = "+str(y)+": test passato con probabilita' di prenotazione = "+str(rand1)+"\n")
		else:
			num_fail = num_fail + 1.0
			g.write("y["+str(i)+"] = "+str(y)+": testo non passato con probabilita' di prenotazione = "+str(rand1)+"\n")
		g.flush()
		os.fsync(g)
	

print ("num pass = ", num_pass)
print ("num fail = ", num_fail)
print ("total tests = ",  num_pass + num_fail)
print ("pass prob = ", num_pass/(num_pass + num_fail))
print ("fail prob = ", num_fail/(num_pass + num_fail))
