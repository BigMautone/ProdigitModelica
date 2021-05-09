import os
import sys
import math
import numpy as np
import time
import os.path_exists

from OMPython import OMCSessionZMQ

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
