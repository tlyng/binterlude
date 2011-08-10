from setuptools import setup, find_packages
import sys, os

version = '1.0b1'

setup(name='binterlude',
      version=version,
      description="Provides an interactive shell aka console inside your doctest case.",
      long_description="""\
Shamelessly stolen from ``interlude`` package. This one just uses bpython as a default shell
if its available.
""",
      classifiers=[
          'Development Status :: 6 - Mature',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
          'Topic :: Software Development :: Libraries :: Python Modules'      
      ],
      keywords='',
      author='Torkel Lyng',
      author_email='torkel.lyng@gmail.com',
      url='http://github.com/tlyng/binterlude/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
