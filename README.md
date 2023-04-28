# Pi Pico W - Setup files
Raspberry Pi Pico W project to setup a wifi connection and launch the installation of the 'phew' package on the pico W.  

## Installation
clone this repository on your local drive  
Use [Thorny](https://thonny.org/) to upload secrets.py and setup_phew.py to your micro-controller (Raspberry Pi Pico W)  
  
## Execution  
From Thorny update the secrets.py parameters with your specific Wifi credentials  
Open the setup_phew.py file and run it  
  
This will connect to the Web, and install the phew library on the lib folder of your 'pico W' storage  
Note: the script imports and uses the upip package (might be depracted in futur release of micro-python)  
