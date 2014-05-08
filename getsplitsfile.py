#! /usr/bin/python
# _*_coding:utf-8 _*_
import os
import re
import time
import sys
reload(sys)

def splitfile(inputfile,npieces,outputpath):
    '''
    input:input a file you want to split 
    npieces:how many pieces you want
    output:where you want to store
    notion:all the same session will be splited in one file,and will be promised
    '''
    filehandler = open(inputfile,'r')
    for line in filehandler:
        pass



if __name__ == "__main__":
    if(len(sys.argv)<4):
        print "used: %s,which need three arguments!"%sys.argv[0]
    else:
        splitfile(sys.argv[1],sys.argv[2],sys.argv[3])
