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

from vmguestlib import VMGuestLib

gl = VMGuestLib()
gl.UpdateInfo()

print 'CPU'
print '  Stolen: %dms' % gl.GetCpuStolenMs()
print '  Used: %dms' % gl.GetCpuUsedMs()
print '  Elapsed: %dms' % gl.GetElapsedMs()
print

print 'Memory'
print '  Active: %d MB' % gl.GetMemActiveMB()
print '  Ballooned: %d MB' % gl.GetMemBalloonedMB()
print '  Mapped: %d MB' % gl.GetMemMappedMB()
print '  Overhead: %d MB' % gl.GetMemOverheadMB()
print '  Shared: %d MB' % gl.GetMemSharedMB()
print '  Shared saved: %d MB' % gl.GetMemSharedSavedMB()
print '  Swapped: %d MB' % gl.GetMemSwappedMB()
print '  Used: %d MB' % gl.GetMemUsedMB()
print

gl.CloseHandle()
```


vmguest-stats tool
------------------
The vmguestlib package includes a basic vmguest-stats tool to get all
vmguestlib counters. It outputs this:
```
[user@system ~]$ vmguest-stats
VM Processor
    Processor Time: 4.64 %
    CPU stolen time: 0.15 %
    Effective VM Speed: 136 MHz
    Host processor speed: 2932 MHz

    Limit: unlimited
    Reservation: 0 MHz
    Shares: 4000

VM Memory
    Active: 1105 MB
    Ballooned: 0 MB
    Mapped: 12288 MB
    Overhead: 110 MB
    Shared: 69 MB
    Shared Saved: 68 MB
    Swapped: 0 MB
    Target Size: 12219 MB
    Used: 12219 MB

    Limit: unlimited
    Reservation: 0 MB
    Shares: 122880
```


Tools
-----
Tools known to be using vmguestlib:

 * vmguest-stats - *Ships with this library*  
   http://github.com/dagwieers/vmguestlib/blob/master/vmguest-stats

 * Dstat - *Tool to correlate many system resource statistics* (see options *--vm-cpu*, *--vm-mem* and *--vm-mem-adv*)  
   http://github.com/dagwieers/dstat


Documentation
-------------
 * Guest and HA Application Monitoring SDK for vSphere 5.5  
   http://pubs.vmware.com/vsphere-55/topic/com.vmware.ICbase/PDF/vs550_guest_HAappmon_sdk.pdf

 * Understanding Memory Resource Management in VMware ESX Server  
   http://www.vmware.com/files/pdf/perf-vsphere-memory_management.pdf

 * vSphere Resource Management - ESXi 5.0  
   http://pubs.vmware.com/vsphere-50/topic/com.vmware.ICbase/PDF/vsphere-esxi-vcenter-server-50-resource-management-guide.pdf


Development
-----------
Please report bugs, improvements and feedback on GitHub at:

http://github.com/dagwieers/vmguestlib


Packaging guidelines
--------------------
Please package this software using the name "python-vmguestlib" on all platforms,
and include the vmguest-stats utility as-is.


Author and license
------------------
This software is (c) 2013-2014 Dag Wieers <dag@wieers.com>

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 2 of the License, or (at your option) any later
version.
