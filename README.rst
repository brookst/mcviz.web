========
MCWebViz
========

`MCViz`_ as a Service! Written with `python`_-`flask`_. Take a look at an `example`_ and try for yourself at `mcviz.skoorb.net`_.

.. _MCViz: http://mcviz.net
.. _python: http://www.python.org
.. _flask: http://flask.pocoo.org
.. _example: http://mcviz.skoorb.net/render/15g9x8wy7?--layout=Feynman&--transform=NoKinks&--transform=Chainmail&--transform=Cut&--style=FancyLines&--style=SimpleColors&--annotation=index#render

Setup
=====
Check out from github and bootstrap an enviroment::

    git clone git://gihub.com/brookst/mcviz.web
    ./bootstrap.py


Standalone running
------------------
Run the ``dev_serve`` script as::

    ./dev_serve

Messages will be printed to the console and the application will be available on http://localhost:5000/

Apache mod_wsgi running
-----------------------
Install `mod_wsgi`_ using the `installation instructions`_. Add the following rule to your Apache config::

    <VirtualHost *:80>
        ServerName mcviz.example.com

        WSGIDaemonProcess mcwebviz user=flask group=www-data threads=5 home=/path/to/mcviz.web
        WSGIScriptAlias / /path/to/mcviz.web/mcwebviz.wsgi

        <Directory /path/to/mcviz.web>
            WSGIProcessGroup mcwebviz
            WSGIApplicationGroup %{GLOBAL}
            WSGIScriptReloading On
            Order deny,allow
            Allow from all
        </Directory>
    </VirtualHost>

Make sure to change ``example.com`` to your domain, create the user ``flask`` and the group ``www-data`` (if needed), and replace (3) instances of ``/path/to/mcviz.web``.

You can then test your configuration and reload apache with::

    # apache2ctl configtest && apache2ctl restart

.. _mod_wsgi: http://www.modwsgi.org
.. _installation instructions: http://code.google.com/p/modwsgi/wiki/QuickInstallationGuide

VirtualEnv
----------
`VirtualEnv`_ makes setting up python package dependencies much easier. The ``bootstrap.py`` script creates a standalone environment in the ``env`` directory. To work with the environment, you can ``source env/bin/activate`` in bash. To deactivate the `VirtualEnv`_, call ``deactivate``.

.. _Virtual env docs: http://virtualenv.readthedocs.org/en/latest/virtualenv.html#installation

Active sites
============
* MCWebViz is hosted by the author at `mcviz.skoorb.net`_.

Let us know if you would like to host a site at `dev@mcviz.net`_.

.. _dev@mcviz.net: mailto:dev@mcviz.net
.. _mcviz.skoorb.net: http://mcviz.skoorb.net

Attribution
===========
MCWebViz by `Tim Brooks`_. Based upon `MCViz`_ by Johannes Ebke, Peter Waller and `Tim Brooks`_. Both projects are licensed under the `GNU Affero GPLv3`_.

.. _GNU Affero GPLv3: http://www.gnu.org/licenses/agpl-3.0.html
.. _Tim Brooks: mailto:brooks@skoorb.net
