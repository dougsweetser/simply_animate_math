==========
Docs Usage
==========

The package sphinx is being used to maintain the documetation.  The html output is stored in the _build/html directory.  Point your browser to::

    _build/html/index.html

to see the results.

To alter content, edit the index.rst file.  The markup language is known as reST
see: http://docutils.sourceforge.net/docs/user/rst/quickref.html

A few clues.  Files must have the extension: .rst

Indents matter.  To set off a block of code, end in a double colon::

    This will appear in a yellow box
    Unaltered
    Great for code

To include an image, use

`image <file.jpg>`_  (I think)
.. image:: file.jpg

`Link text <http://whatever.xxx>`_
.. _Link text: http://whatever.xxx

To generate the docs, type "make html".
