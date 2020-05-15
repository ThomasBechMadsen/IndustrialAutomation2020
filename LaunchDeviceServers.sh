#!/bin/bash
#Launches all device servers in parallel

#Tanks
python TankDeviceServer/TankDeviceServer.py Tank1 &
python TankDeviceServer/TankDeviceServer.py Tank2 &

#Distribution
python DistributionDeviceServer/DistributionDeviceServer.py Distribution &

#PreMix
python PreMixDeviceServer/PreMixDeviceServer.py PreMix &

wait
