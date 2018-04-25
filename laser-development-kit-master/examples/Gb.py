#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import numpy as np
import matplotlib.pyplot as plt

from koheron import connect
from drivers import Laser

# Connect to the board
host = '192.168.1.99'
client = connect(host, instrument='oscillo')
#export host=192.168.1.101 # Red Pitaya IP address
