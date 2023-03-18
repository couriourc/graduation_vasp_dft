# !/usr/bin/bash
# vasprun.xml
# <imag> a ; b ; c; d ; e ; f; g; </imag>
# <real> a ; b ; c; d ; e ; f; g; </real>
# get img partials
awk 'BEGIN{i=1} /<imag>/,\
                /<\/imag>/ \
                 {a[i]=$2 ; b[i]=$3 ; c[i]=$4; d[i]=$5 ; e[i]=$6 ; f[i]=$7; g[i]=$8; i=i+1} \
     END{for (j=12;j<i-3;j++) print a[j],b[j],c[j],d[j],e[j],f[j],g[j]}' vasprun.xml > IMAG.in;

# get real partials
awk 'BEGIN{i=1} /<real>/,\
                /<\/real>/ \
                 {a[i]=$2 ; b[i]=$3 ; c[i]=$4; d[i]=$5 ; e[i]=$6 ; f[i]=$7; g[i]=$8; i=i+1} \
     END{for (j=12;j<i-3;j++) print a[j],b[j],c[j],d[j],e[j],f[j],g[j]}' vasprun.xml > REAL.in;