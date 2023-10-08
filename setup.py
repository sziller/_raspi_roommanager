#!/usr/bin/python3.10
import os
from setuptools import setup

'''
setup function to be run when creating packages for Organica
command to be typed in:
python setup.py sdist
python setup.py bdist_wheel
'''
# ATTENTION! Wheel file needed, depending on environment

setup(
    name='RaspiRoommanager',  # package name, used at pip or tar.
    version='0.0.0',  # version Nr.... whatever
    packages=["RoomManager"],  # string list of packages to be translated
    include_package_data=True,
    url='',  # if url is used at all
    license='',  # ...
    author='sziller',  # well obvious
    author_email='sziller@gmail.com',  # well obvious
    description='RasPi based room manager module',  # well obvious
    install_requires=[
        "pytest",
        "sqlalchemy",
        "sensehat_assist @ file://localhost/{}/lib/project-own/sensehat_assist-0.0.0-py3-none-any.whl"
        .format(os.getcwd()),
        "sensehat_led_clock @ file://localhost/{}/lib/project-own/sensehat_led_clock-0.0.0-py3-none-any.whl"
        .format(os.getcwd()),
        "sensehat_led_display @ file://localhost/{}/lib/project-own/sensehat_led_display-0.0.0-py3-none-any.whl"
        .format(os.getcwd()),
        "sensehat_sensors @ file://localhost/{}/lib/project-own/sensehat_sensors-0.0.0-py3-none-any.whl"
        .format(os.getcwd())
      ],
    dependency_links=[],  # if dependent on external projects
)
