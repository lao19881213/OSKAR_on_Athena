# -*- coding: utf-8 -*-
"""Simulate a Measurement Set."""

import os
from os.path import join
from collections import OrderedDict
import subprocess
import argparse
import json
from shutil import copyfile
import numpy
import math
import time



def run_interferometer(ini, verbose=True):
    """Run the OSKAR interferometer simulator."""
    if verbose:
        subprocess.call(["oskar_sim_interferometer", ini])
    else:
        subprocess.call(["oskar_sim_interferometer", "-q", ini])

def run(settings, verbose=True):
    """Run the OSKAR simulation."""
    sim_dir = settings['path']
    sim = settings['sim']
    obs = sim['observation']
    sky_file = join(sim_dir, 'gleam_mod.10k.mod')
    if not os.path.isdir(os.path.dirname(sky_file)):
        os.makedirs(os.path.dirname(sky_file))
    os.system('cp gleam_mod.10k.mod %s' % sky_file)
    #create_sky_model(sky_file, [obs['ra_deg']], [obs['dec_deg']+0.9], [1.0])

    for n in obs['num_times']:
        # ===== Without analytical smearing =====
        ms_out = join(sim_dir, 'n%04i.ms' % n)
        if not os.path.isdir(ms_out):
            clock_start = time.time()
            run_interferometer('/group/pawsey0245/blao/gleam_data_test/n0100.ini', verbose)
            clock_end = time.time()
        
    log_string = '%.2f' % \
            ((clock_end - clock_start))
    with open("dingo_log.txt", "a") as log_file:
        log_file.write(log_string + '\n')

