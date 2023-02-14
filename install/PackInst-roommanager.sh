#!/bin/bash

# Enter necessary paths here:
# default         - for installation related packages
# project-public  - for packages needed for local project in public domain
# project-own     - for packages needed for local project developed locally

dmn="room"
path="/home/pi/python_projects/_raspi_roommanager/lib/"

def="default/"
pub="project-public/"
own="project-own/"



echo '[$dmn]: START - Initializing DEFAULT installation:'
# variable name 'file' bears importance! Keep it!
for file in $path$def*
do
	echo ' >>> now installing: $file'
        pip3 install $file
	echo ' >>> finished'
done
echo '[$dmn]: FINISHED local package installation!'

echo '[$dmn]: START - Initializing PUBLIC project related installation:'
# variable name 'file' bears importance! Keep it!
for file in $path$pub*
do
	echo ' >>> now installing: $file'
        pip3 install $file
	echo ' >>> finished'
done
echo '[$dmn]: FINISHED local package installation!'

echo '[$dmn]: START - Initializing LOCAL project related installation:'
# variable name 'file' bears importance! Keep it!
for file in $path$own*
do
	echo ' >>> now installing: echo $file'
        pip3 install $file
	echo ' >>> finished'
done
echo '[$dmn]: FINISHED local package installation!'
