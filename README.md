# README #

## Welcome to my **RoomManager** project.
This is a small Raspberry device handler, running an all round CLIENT device, placed into a Room
of an apartment.
Its tasks - as of now - are as follows:

#### Communication:
  - sending Data to the Apartment server
  - receiving and executing global commands from the Apartment server

#### Measurement:
  - temperature
  - moisture
  - pressure
  - optical movement detection

#### Local LED display:
  - measurements
  - entertainment
  - small directional light

#### Peripherials:
  - switching local devices.

### How do I get set up? ###

* go to the install folder and run the PackInst-roommanager.sh bash file.
To do so, enter:

```
sudo bash PackInst-roommanager.sh
```

* Configuration: ...
* Dependencies are installed automatically or install everithing in the _lib_ folder, by entering:

```
pip3 install <packagename>
```

for each package found there. Most of them should be offline installable.

* Once all your packages are installed, go to root, open up a terminal, and enter:

```
pytest
```

* Small projects of mine such as this one; can be run four ways:
  * from terminal: `python3 App_RoomManager.py`
  * from IDLE: App_RoomManager()
  * from editor: the way the editor ever executes a Python code
  * Desktop icon, fund in /DesktopLauncher

### Stuck? ###
* contact: szillerke@gmail.com
