#!/usr/bin/python

from vmguestlib import *

gl = VMGuestLib()

gl.UpdateInfo()
print 'Active memory:', gl.GetMemActiveMB()
print 'Ballooned memory:', gl.GetMemBalloonedMB()
print 'Mapped memory:', gl.GetMemMappedMB()
print 'Overhead memory:', gl.GetMemOverheadMB()
print 'Shared memory:', gl.GetMemSharedMB()
print 'Shared saved memory:', gl.GetMemSharedSavedMB()
print 'Swapped memory:', gl.GetMemSwappedMB()
print 'Used memory:', gl.GetMemUsedMB()
print

print 'Stolen:', gl.GetCpuStolenMs()
print 'Used:', gl.GetCpuUsedMs()
print 'Elapsed:', gl.GetElapsedMs()
print