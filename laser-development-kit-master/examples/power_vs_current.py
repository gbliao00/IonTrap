#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import numpy as np
import matplotlib.pyplot as plt

from koheron import connect
from drivers import Laser

host = os.getenv('HOST','192.168.0.101')
client = connect(host, name='oscillo')

laser = Laser(client)

laser.start()
laser.set_current(0)
time.sleep(0.1)

current_max = 40
currents = np.linspace(0,current_max, num=100)

laser_powers = 0 * currents
measured_currents = 0 * currents

for i, current in enumerate(currents):
    laser.set_current(current)
    time.sleep(0.02)
    laser_powers[i] = laser.get_measured_power()
    measured_currents[i] = (0.0001/21)*(laser.get_measured_current())
    print('laser power = ' + str(laser_powers[i]) + ' arb. units')

# Plot
fig1 = plt.figure('Power vs current')
plt.plot(currents, laser_powers)
plt.xlabel('Control current (mA)')
plt.ylabel('Laser power (arb. units)')

np.savetxt('power_vs_current.csv',
           np.transpose([currents, laser_powers]),
           delimiter=',',
           fmt='%1.4e')

laser.stop()
plt.show()
