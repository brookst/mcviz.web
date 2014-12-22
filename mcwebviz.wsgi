activate_this = 'env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from mcviz.web.app import APP as application
