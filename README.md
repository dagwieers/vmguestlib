VMGuestLib python wrapper
=========================
Python API for interacting with VMware's VMGuestLib SDK.


Installation
------------
The software is easy to install from github:

    $ git clone git://github.com/dagwieers/vmguestlib
    $ cd vmguestlib
    $ python setup.py install


Quick Example
-------------
```python
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
```


Documentation
-------------

 * Guest and HA Application Monitoring SDK for vSphere 5.5  
   http://pubs.vmware.com/vsphere-55/topic/com.vmware.ICbase/PDF/vs550_guest_HAappmon_sdk.pdf

 * Understanding Memory Resource Management in VMware ESX Server  
   http://www.vmware.com/files/pdf/perf-vsphere-memory_management.pdf

 * vSphere Resource Management - ESXi 5.0  
   http://pubs.vmware.com/vsphere-50/topic/com.vmware.ICbase/PDF/vsphere-esxi-vcenter-server-50-resource-management-guide.pdf


Author and license
------------------
This software is (c) 2013-2014 Dag Wieers <dag@wieers.com>

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 2 of the License, or (at your option) any later
version.
