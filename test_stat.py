#!/usr/bin/python

import time
from vmguestlib import *

gl = VMGuestLib()

while True:
    time.sleep(1)
    gl.UpdateInfo()
    try:
        print {
        'cpuReservationMHz': gl.GetCpuReservationMHz(),
        'cpuLimitMHz': gl.GetCpuLimitMHz(),
        'cpuShares': gl.GetCpuShares(),
        'cpuStolenMs': gl.GetCpuStolenMs(),
        'cpuUsedMs': gl.GetCpuUsedMs(),
        'elapsedMs': gl.GetElapsedMs(),
        'hostProcessorSpeed': gl.GetHostProcessorSpeed(),
        'memActiveMB': gl.GetMemActiveMB(),
        'memBalloonedMB': gl.GetMemBalloonedMB(),
        'memLimitMB': gl.GetMemLimitMB(),
        'memMappedMB': gl.GetMemMappedMB(),
        'memOverheadMB': gl.GetMemOverheadMB(),
        'memReservationMB': gl.GetMemReservationMB(),
        'memSharedMB': gl.GetMemSharedMB(),
        'memSharedSavedMB': gl.GetMemSharedSavedMB(),
        'memShares': gl.GetMemShares(),
        'memSwappedMB': gl.GetMemSwappedMB(),
        'memTargetSizeMB': gl.GetMemTargetSizeMB(),
        'memUsedMB': gl.GetMemUsedMB(),
        }
    except Exception, e:
        print dir(e)