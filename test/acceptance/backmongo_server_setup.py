#! /usr/bin/env python

import os
import subprocess

pidfile = '/tmp/backmongo-test-server.pid'

if not os.path.isfile(pidfile):
    pid = subprocess.Popen('./bin/backmongo').pid
    open(pidfile, 'w').write(str(pid))
    print "1>", pid
