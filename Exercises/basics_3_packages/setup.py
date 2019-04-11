#!/usr/bin/env python

from setuptools import setup, find_packages


# Edit these variables
package_name = 'DiceRoller' 
version = '1.0'
description='Rolls different types of dices',
author = '<Your Name Here>'
author_email = '<Your e-mail here>'


# This is the function that will actually perform the installation
setup(name=package_name,
      version=version,
      description=description,
      author=author,
      author_email=author_email,
      packages=find_packages(exclude=["answer",]),
      scripts=[],
     )
