# !/usr/bin/python

import sys
import os

binfilepath=["//usr//local//sbin","//usr//local//bin","//usr//sbin","//usr//bin","//sbin","//bin"]
manfilepath=["//usr//share//man","//var//cache//man"]

binpath=""
manpath=""

try:
 binfile=sys.argv[1]
except IndexError:
 print "Usage Eg: python find_bin_man.py <bin>"
 exit()

for path in binfilepath:
 for root,dirs,files in os.walk(path):
  for file in files:
   if file == binfile:
    binpath=os.path.join(root,file)

for path in manfilepath:
 for root,dirs,files in os.walk(path):
  for file in files:
   if file.split(".")[0] == binfile:
    manpath=os.path.join(root,file)


if binpath != "":
 print "\nBinary: "+binpath+"\n"
else:
 print "Unable to locate binary"

if manpath != "":
 print "Man page: "+manpath+"\n"
else:
 print "Unable to locate man page path"
