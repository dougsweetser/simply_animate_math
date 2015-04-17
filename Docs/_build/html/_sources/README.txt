Notes
=====
To make the original version:

> sphinx-api -F -o Docs simply_animate_math ::

The conf.py needed a modification to fix finding the code:
::
    sys.path.insert(0, os.path.abspath('.'))
    parent = os.path.abspath(os.path.join(os.path.dirname('conf.py'), ".."))
    sys.path.insert(0, parent)
    sys.path.insert(0, parent + "/simply_animate_math")

Then *make html* in the Docs directory does the trick.

If any further programs are added, rerun the command with a *-f* for *-F*

