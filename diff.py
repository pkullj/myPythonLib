#! /usr/bin/python 
import os
import difflib
import sys

def getdiff():
    print sys.argv[1]
    new = open(sys.argv[1],'r')
    old = open(sys.argv[2],'r')
    newcontent = new.readlines()
    oldcontent = old.readlines()
    print newcontent[1],oldcontent[1]
    d = difflib.Differ()
    for line in difflib.context_diff(newcontent,oldcontent,fromfile="one",tofile="two"):
        sys.stdout.write(line)
#    diff = d.compare(newcontent,oldcontent)
#    print " ".join(list(diff))
#    cmd = "diff %s %s"%(str(newcontent[1]),str(oldcontent[1]))
#    print cmd
#    result = os.popen("diff %s %s"%(newcontent[1],oldcontent[1])).read()
#    print result

if __name__ == "__main__":
    getdiff()
