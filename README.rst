========
MCWebViz
========

`MCViz`_ as a Service! Written with `python`_-`flask`_.

.. _MCViz: http://mcviz.net
.. _python: http://www.python.org
.. _flask: http://flask.pocoo.org

Setup
=====
Check out from github::

    git clone git://gihub.com/brookst/mcviz.web

VirtualEnv
----------
`VirtualEnv`_ makes setting up python package dependencies much easier. To install; see the `Virtual env docs`_. `VirtualEnv`_ is packaged as `python-virtualenv`_ on `Ubuntu`_ systems.
Set up a virtual environment using the following::

    mkvirtualenv -a `pwd` -r requirements.txt mcviz.web
    workon mcviz.web

To deactivate the `VirtualEnv`_, run ``deactivate``. To work on the environment again; run ``workon mcviz.web`` again.

.. _Virtual env docs: http://virtualenv.readthedocs.org/en/latest/virtualenv.html#installation
.. _python-virtualenv: http://packages.ubuntu.com/utopic/python/python-virtualenv
.. _Ubuntu: http://www.ubuntu.com

Standalone running
------------------
Run the ``mcwebviz.py`` script as::

    python mcwebviz.py

Messages will be printed to the console and the application will be available on http://localhost:5000/

Attribution
===========

`MCViz`_ by Johannes Ebke, Peter Waller and Tim Brooks. Licensed under AGPLv3.

