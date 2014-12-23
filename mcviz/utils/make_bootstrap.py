#!/usr/bin/env python
"""Make bootstrap script"""

import virtualenv, textwrap
OUTPUT = virtualenv.create_bootstrap_script(textwrap.dedent("""
import os, subprocess
def after_install(options, home_dir):
    dirs = ['log', 'uploads', 'renders']
    for folder in dirs:
        if not os.path.exists(folder):
            os.makedirs(folder)

    os.system("git submodule update --init mcviz.standalone")

    ret = subprocess.call([join(home_dir, 'bin', 'pip'), 'install', '-e',
                           'mcviz.standalone'])
    if ret:
        print("Error installing mcviz")
        return

    ret = subprocess.call([join(home_dir, 'bin', 'pip'), 'install', '-e', '.'])
    if ret:
        print("Error installing mcviz.web")
        return

    try:
        os.symlink("env/bin/mcwebviz", "dev_serve")
    except OSError:
        pass

    print("")
    print("Check the user running apache can access these folders")
    print("e.g. > chown ${USER}:www-data log uploads renders")
    print("     > chmod 775 .")

def adjust_options(options, args):
    args[:] = ["env"]
"""))
open('bootstrap.py', 'w').write(OUTPUT)
