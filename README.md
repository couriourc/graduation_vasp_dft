# 不同浓度 Mo 掺杂的 Vo2 密度泛函理论

> 毕业设计：不同浓度 Mo 掺杂的 Vo2 密度泛函理论研究(DFT),基于 Python 对 Vasp 模拟信息 Vaspy 实现可视化。

## 辅助脚本

### [获取介电函数的实部和虚部](./shell/optics.sh)
```shell
# extract image and real parts of dielectric function from vasprun.xml
awk 'BEGIN{i=1} /<imag>/,\
                /<\/imag>/ \
                 {a[i]=$2 ; b[i]=$3 ; c[i]=$4; d[i]=$5 ; e[i]=$6 ; f[i]=$7; g[i]=$8; i=i+1} \
     END{for (j=12;j<i-3;j++) print a[j],b[j],c[j],d[j],e[j],f[j],g[j]}' vasprun.xml > IMAG.in
#awk 'BEGIN{i=1} /imag/,\
#                /\/imag/ \
#                 {a[i]=$2 ; b[i]=$3 ; c[i]=$4; d[i]=$5 ; e[i]=$6 ; f[i]=$7; g[i]=$8; i=i+1} \
#     END{for (j=12;j<i-3;j++) print a[j],b[j],c[j],d[j],e[j],f[j],g[j]}' vasprun.xml > IMAG.in
awk 'BEGIN{i=1} /<real>/,\
                /<\/real>/ \
                 {a[i]=$2 ; b[i]=$3 ; c[i]=$4; d[i]=$5 ; e[i]=$6 ; f[i]=$7; g[i]=$8; i=i+1} \
     END{for (j=12;j<i-3;j++) print a[j],b[j],c[j],d[j],e[j],f[j],g[j]}' vasprun.xml > REAL.in
```

### [获取态密度(DOS)信息](./shell/get_dos.sh)
```shell
#!/bin/sh
a=`awk '{ if(NR==6) print $3}' DOSCAR`
b=`echo "${a}+6"|bc`
f=`awk '{ if(NR==6) print $4}' DOSCAR`

echo $a, $b, $f
awk '{ if (NR>=7&&NR<='$b') print $0}' DOSCAR > DOS.dat
```