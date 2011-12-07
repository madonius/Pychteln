#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import random

def comparelistlines(list1, list2):
    same = 0
    for i in range(0,len(list1)):
        if(list1[i]==list2[i] or same == 1):
            same=1

    if(same==0):
        return True
    else:
        return False

parser = argparse.ArgumentParser( description="Definiere wer mit wem wichteln soll", add_help=True, usage="%(prog)s -f NAMENSLISTE -o WICHTELLISTE [-v]")
parser.add_argument("-f", "--file", dest="filename", type=str, help="Gebe die NAMENSLISTE mit der Liste der Teilnehmer an. Diese sollte pro Zeile nur einen Teilnehmer enthalten", metavar="NAMENSLISTE")
parser.add_argument("-o", "--output", dest="output", type=str, help="Gebe die Liste in die WICHTELLISTE aus", metavar="WICHTELLISTE")
parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=False, help="Gebe die Liste auf dem Bildschirm aus")
args = parser.parse_args()

if not args.filename:
    print("Bitte gebe eine Namensliste an. Siehe Hilfe mit pychteln.py -h")
    exit

Namelist = open(args.filename,'r').readlines()
Namelist_copy = list(Namelist)

tautologies = 1

while(tautologies==1):
    random.shuffle(Namelist_copy)

    if(comparelistlines(Namelist,Namelist_copy)):
        tautologies=0

if args.output:
    outfile = open(args.output,'w')
    for i in range(0,len(Namelist)):
        outfile.write(Namelist[i].rstrip() + '   \t' + Namelist_copy[i])
    outfile.close()

if(args.verbose==True):
     for i in range(0,len(Namelist)):
        print(Namelist[i].rstrip() + '   \t' + Namelist_copy[i].rstrip())
