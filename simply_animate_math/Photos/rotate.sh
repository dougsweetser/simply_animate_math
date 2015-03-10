#/bin/sh
ls *jpg | perl -lane 'print qq(/opt/local/bin/convert $F[0] -rotate 90 $F[0])'
