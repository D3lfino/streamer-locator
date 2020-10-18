# python-wireshark-geolocate

A script to geolocate people on streaming media using **Wireshark/tshark** and the **[maxminddb-geolite2](https://pypi.python.org/pypi/maxminddb-geolite2/2015.0303)** python module. Tested on Omegle and Chatroulette.

I created this script as an experiment after learning about wireshark in my computer communications class. It's for educational/harmless purposes only. Please don't try to use it to stalk or scare people.

[![Video](https://img.youtube.com/vi/nPpW3xTKhbE/0.jpg)](https://www.youtube.com/watch?v=nPpW3xTKhbE "YouTube Video")


## Steps to download wireshark/tshark in Linux:
* ```sudo apt-get update -y```
* ```sudo apt-get install -y tshark```


## Removal
* ```sudo apt-get remove --purge wireshark```

Then remove all dependencies that are no longer needed:
* ```sudo apt-get autoremove```
* ```sudo rm -rf /etc/wireshark```
