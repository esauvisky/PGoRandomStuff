#!/bin/bash

adb shell getevent /dev/input/event2 | ts "%Y-%m-%d %H:%M:%.S"