Naming Rules
============
* The directory names define a dictionary.
* A number in a plane (2, 1) is written in a file as N2n1
* Two numbers are separted by a dash: N2n1_3n1

Bulk Transparency
=================
Here is a perl one-liner using imagemagick convert on jpg images in a directory:

ls *jpg | perl -lane '$j = $F[0]; $p = $j; $p =~ s/.jpg/.png; print qq(/opt/local/bin/convert $j -fuzz 38% -transparent white $p)'

Try this out to see if the fuss % is what is needed.  If so, then pipe this into the shell command to "make it so".
