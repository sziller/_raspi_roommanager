#!/usr/bin/python3.10

from setuptools import setup

'''
setup function to be run when creating packages for Organica
command to be typed in:
python setup.py sdist
'''
# ATTENTION! Wheel file needed, depending on environment

setup(
    name='RaspiRoommanager',  # package name, used at pip or tar.
    version='0.0.0',  # version Nr.... whatever
    packages=["RoomManagerEngine"],  # string list of packages to be translated
    url='',  # if url is used at all
    license='',  # ...
    author='sziller',  # well obvious
    author_email='sziller@gmail.com',  # well obvious
    description='RasPi based room manager module',  # well obvious
    install_requires=["sensehat_assist", "sensehat_led_clock", "sensehat_led_display", "sensehat_sensors"],
    dependency_links=[],  # if dependent on external projects
)
