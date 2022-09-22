# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Description:  General mathematical operations
# Author:       benedikt.strahm@ilek.uni-stuttgart.de
# Created:      19.09.2022
# Execution:    Import functions / collections (from pyLek.helpers import util)
# Status:       Finished
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------------
import numpy as np
# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------


def sphereToCartesian(r: int, phi: int, theta: int):
    """
    Transform from spherical coordinates to Cartesian coordinates, 
    :param r: radius r
    :param phi: inclination φ
    :param theta: azimuth θ
    :return: cartesian coordinate
    :rtype: tuple
    """
    x = r * np.cos(phi) * np.cos(theta)
    y = r * np.cos(phi) * np.sin(theta)
    z = r * np.sin(phi)
    return (x, y, z)