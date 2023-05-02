# Pi Pico W - Setup files
Raspberry Pi Pico W script to setup a wifi connection and launch the installation of the 'phew' package on the pico W.  

## Installation
clone this repository on your local drive  
Use [Thonny](https://thonny.org/) (or your prefered IDE) to upload secrets.py and setup_phew.py to your micro-controller (Raspberry Pi Pico W)  
  
## Execution  
From Thorny update the secrets.py parameters with your specific Wifi credentials  
Open the setup_phew.py file and run it  
  
This will connect to the Web, and install the phew library on the lib folder of your 'pico W' storage  

## Backwards compatibility
From verion 1.20 of micropython for Raspberry Pi Pico W the package manager is mip.install().  
For version before 1.20 (1.19 or lower) the package manager was upip (a lightweight version pip usually used in python environmenets)  
This script will try to detect the version installed and use the proper package installer.  

## Micropython version
[Micropython Latest Version](https://micropython.org/download/rp2-pico-w/)  
An older v1.19 micropython is available in thie repository for testing purposes.  

## How to reset you micropyhton  (windows version())
- Unplugthe Pico W from computer  
- Hold the BOOTSEL button on the micro-controller  
- Plug the USB cable in the micro-controller, this should open the - windows file explorer  
- Drag the desired *.uf2 file to the micro-controller, that's it  
- Open Thonny to connect to the Pico W  
- Go to the Thonny console  
- import os
- os.uname() should display an object that contains the version - identification

