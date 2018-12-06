#!/usr/bin/env python2
import sys
import re
import datetime

line_re = re.compile(r"^(\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d\.\d+) (\S+) (\S+) (\S+)$")
event_log = sys.stdin
last_ts = None
for line in event_log:
    match = line_re.match(line.strip())
    ts, etype, ecode, data = match.groups()
    ts = datetime.datetime.strptime(ts, "%Y-%m-%d %H:%M:%S.%f")
    etype, ecode, data = int(etype, 16), int(ecode, 16), int(data, 16)
    if last_ts:
        delta = ts - last_ts
        sleeptime = '%.3f' % (delta.total_seconds())
        if float(sleeptime):
            print "sleep %s" % sleeptime
    last_ts = ts
    print "adb shell sendevent /dev/input/event1 %s %s %s" % (etype, ecode, data)