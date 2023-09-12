#! /usr/bin/python

TEMP_PATH="/sys/class/thermal/thermal_zone0/"

def readTemp():
    fo = open(TEMP_PATH + "temp","r")
    temp = fo.read()
    return int(temp)

def averageTemp(n):
    sum=0
    for i in range(n):
        sum=sum+readTemp()
    average = sum/n
    return average
