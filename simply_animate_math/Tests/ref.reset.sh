#!/bin/sh
echo 'Copies from /tmp/whatever.bmp to ref.whatever.bmp'
ls ref*png | perl -lane '$r = $F[0]; $t = $r; $t =~ s/ref.//; $t = qq(/tmp/$t); print qq(cp $t $r)' | /bin/sh
