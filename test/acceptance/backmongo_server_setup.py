#! /usr/bin/env python

import os
import subprocess

pidfile = '/tmp/backmongo-test-server.pid'

if not os.path.isfile(pidfile):
    pid = subprocess.Popen('./bin/backmongo',
        stdout=open(os.devnull, 'w'),
        stderr=open(os.devnull, 'w')).pid
    open(pidfile, 'w').write(str(pid))
