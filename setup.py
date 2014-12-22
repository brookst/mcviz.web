"""Setuptools config"""
from setuptools import setup, find_packages
from textwrap import dedent

VERSION = "2014.12.22"

setup(name='mcviz.web',
      version=VERSION,
      description="mcwebviz",
      long_description=dedent("""
          `MCWebViz` is a visualizer for HEP Monte Carlo events. Users can
          upload event files and select view options then the server will
          render the event. The browser based interface means no set-up for
          users and allows for fast iteration.
      """).strip(),
      classifiers=['License :: OSI Approved :: GNU Affero General Public'
                   ' License v3',
                   'Development Status :: 2 - Pre-Alpha',
                   'Programming Language :: Python',
                   'Framework :: Flask',
                   'Topic :: Scientific/Engineering :: Physics',
                   'Environment :: Web Environment',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Physicists :: Developers',
                   'Natural Language :: English',
                   'Operating System :: POSIX',
                  ],
      keywords='mcviz web hep montecarlo hepmc lhe pythia graphviz svg'
               ' visualization',
      author='Tim Brooks',
      author_email='dev@mcviz.net',
      url='http://mcviz.net',
      license='GNU Affero GPLv3',
      platforms='any',
      packages=find_packages(),
      install_requires=['mcviz',
                        'flask',
                        'werkzeug',
                       ],
      data_files=[('log', []),
                  ('uploads', []),
                  ('renders', []),
                  ('templates', ['templates/base.html',
                                 'templates/main.html',
                                 'templates/render.html',
                                ]),
                 ],
     )
