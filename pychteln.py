#!/usr/bin/python
# -*- coding: utf-8 -*-

##################################################################################
# Pychteln is a Software written to assign the Hidden Santa partners to eachother
# Copyright (C) 2011  Emmanouil Kampitakis
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
##################################################################################

import argparse
import random

#check if the lists have assigned an individual to itself
def comparelistlines(list1, list2):
    same = 0
    for i in range(0,len(list1)):
        if(list1[i]==list2[i] or same == 1):
            same=1

    if(same==0):
        return True
    else:
        return False

#read the commandline arguments
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

#print the list into a given file
if args.output:
    outfile = open(args.output,'w')
    for i in range(0,len(Namelist)):
        outfile.write(Namelist[i].rstrip() + '   \t' + Namelist_copy[i])
    outfile.close()

#print the List on screen
if(args.verbose==True):
     for i in range(0,len(Namelist)):
        print(Namelist[i].rstrip() + '   \t' + Namelist_copy[i].rstrip())

