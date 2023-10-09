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


NAME = "RaspiRoommanager"

PROJECT_PATH = "/home/sziller/Projects/"
GEN_PACKAGES_PATH = PROJECT_PATH + "001_GeneralAssistance/GeneralCoding/Python/general_package_development"
HAT_PACKAGES_PATH = PROJECT_PATH + "900_Raspberry/_general_packages/SenseHat"

INSTALL_REQUIRES = [
    "pytest",
    "sqlalchemy",
    "sensehat_led_clock @ file://localhost/{}/sensehat_led_clock/dist/sensehat_led_clock-0.0.0-py3-none-any.whl"
    .format(HAT_PACKAGES_PATH),
    "sensehat_led_display @ file://localhost/{}/sensehat_led_display/dist/sensehat_led_display-0.0.0-py3-none-any.whl"
    .format(HAT_PACKAGES_PATH),
    "sensehat_sensors @ file://localhost/{}/sensehat_sensors/dist/sensehat_sensors-0.0.0-py3-none-any.whl"
    .format(HAT_PACKAGES_PATH)]

# 'ExampleRepo @ git+ssh://git@github.com/example_org/ExampleRepo.git'

print("--" + "-"*30 + "--",)
print("- {:^30} -".format(NAME))
print("--" + "-"*30 + "--",)
print("- {:^30} -".format("INSTALL_REQUIRES"))
print("--" + "-"*30 + "--",)
for _ in INSTALL_REQUIRES:
    print(_)
print("--" + "-"*30 + "--")


setup(
    name=NAME,  # package name, used at pip or tar.
    version='0.0.0',  # version Nr.... whatever
    packages=["RoomManager"],  # string list of packages to be translated
    include_package_data=True,
    url='',  # if url is used at all
    license='',  # ...
    author='sziller',  # well obvious
    author_email='sziller@gmail.com',  # well obvious
    description='RasPi based room manager module',  # well obvious
    install_requires=INSTALL_REQUIRES,
    dependency_links=[],  # if dependent on external projects
)
