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
safety = False

with open ("logMonitorFunz", 'wt') as f:
        f.write("Begin log"+"\n")
        f.flush()
        os.fsync(f)
        
with open ("outputMonitorFunz.txt", 'wt') as f:
        f.write("Outcomes"+"\n\n")
        f.flush()
        os.fsync(f)
        
for i in range(10000):
	
	with open("newValues.txt", 'wt') as f:
		rand1 = np.random.rand()
		f.write("stud.probPren="+str(rand1)+"\n")
		f.flush()
		os.fsync(f)
		
		
	with open ("logMonitorFunz", 'a') as f:
		f.write("\nTest "+str(i)+" : ")
		f.write("Probabilita' di prenotazione = " + str(rand1) + "\n")
		f.flush()
		os.fsync(f)
	
	os.system("./System -overrideFile=newValues.txt >> logMonitorFunz")
	#time.sleep(1.0) # Delay to avoid races on file re-writings. Can be dropped for non-toy examples.
	os.system("rm -f newValues.txt") # .... to be on the safe side
	
	safety = omc.sendExpression("val(saf.safety, 150.0, \"System_res.mat\")")
	posti = omc.sendExpression("val(saf.postiAula, 150.0, \"System_res.mat\")")
	prenotati = omc.sendExpression("val(saf.prenotazioni, 150.0, \"System_res.mat\")")
	
	#print(str(omc.sendExpression("val(stud.probPren, 150.0, \"System_res.mat\")")))

	os.system("rm -f System_res.mat")      # .... to be on the safe side
        
	print("Monitor value at iteration", i, ": ", safety, "- with prenotation probability = ", rand1)
	
	with open ("outputMonitorFunz.txt", 'a') as g:
		if (not safety):
			num_pass = num_pass + 1.0
			g.write("Safety["+str(i)+"] = "+str(safety)+": test passato con probabilita' di prenotazione = "+str(rand1)+
			" (Numero posti disponibili nell'aula = "+str(posti)+ "; Studenti prenotati =  "+str(prenotati)+")\n")
		else:
			num_fail = num_fail + 1.0
			g.write("Safety["+str(i)+"] = "+str(safety)+": testo non passato con probabilita' di prenotazione = "+str(rand1)+
		" (Numero posti disponibili nell'aula = "+str(posti)+ "; Studenti prenotati =  "+str(prenotati)+")\n")
		g.flush()
		os.fsync(g)
		
with open ("outputMonitorFunz.txt", 'a') as g:
	g.write("CPU time = "+str(time.time()-startTime)+"\n")
	g.flush()
	os.fsync(g)
	
print("Execution time = ", (time.time()-startTime))
print ("num pass = ", num_pass)
print ("num fail = ", num_fail)
print ("total tests = ",  num_pass + num_fail)
print ("pass prob = ", num_pass/(num_pass + num_fail))
print ("fail prob = ", num_fail/(num_pass + num_fail))
