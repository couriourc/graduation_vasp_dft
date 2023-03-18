#!/bin/sh

a=`awk '{if(NR==6)print $3}' DOSCAR`
b=`echo "${a}+6"|bc`

f=`awk '{ if (NR==6) print $4}' DOSCAR`

echo $a, $b, $f
awk '{if(NR>=7&&NR<='$b') print $0}' DOSCAR > DOS.dat

