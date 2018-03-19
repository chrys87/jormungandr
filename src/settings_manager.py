#!/usr/bin/env/python3

import imp, os, sys


""" Access settings for the screen reader using settings.parameter e.g. settings.speechRate"""

# Read settings file

def read_settings(settingsFile):
    global settings
    s = open(settingsFile)
    settings = imp.load_source('settings', '', s)
    s.close()


#check for settings file
if os.path.isfile("/etc/jormungandr/settings/settings.conf"):
    settingsFile = "/etc/jormungandr/settings/settings.conf"
# This should load the settings file in the git repo's settings directory, but not sure how to make it do it yet.
elif os.path.isfile("../settings/settings.conf"):
    pass
# There is no settings file, so error out
else:
    sys.exit('no settings file found, exiting.')

read_settings(settingsFile)
