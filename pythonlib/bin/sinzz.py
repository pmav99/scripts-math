#!/usr/bin/python

# ================================================================
# Copyright (c) John Kerl 2007
# kerl.john.r@gmail.com
# ================================================================

from __future__ import division # 1/2 = 0.5, not 0.
# Import the cmath module rather than the math module so that exp et al. may
# take complex arguments.
from  math import *
from cmath import *
import sys
from kerlutil import *

# ----------------------------------------------------------------
def f(z):
	#return sin(z)/z
	return exp(1j*z)/z

# ----------------------------------------------------------------
def pathz(R,t):
	return R * exp(1j*t)

# ----------------------------------------------------------------
tlo =  0.0
thi =  2*pi
nt  = 1000
dt = (thi-tlo)/nt

#[R1,R2,R3,R4] = [1.0, 0.1, 0.01, 0.001]
#[R1,R2,R3,R4] = [1.0, 0.9, 0.8, 0.7]
#[R1,R2,R3,R4] = [0.1, 0.01, 0.001, 0.0001]
#[R1,R2,R3,R4] = [2., 3., 4., 5.]
#[R1,R2,R3,R4] = [1, 2, 3, 4]
#[R1,R2,R3,R4] = [1, 10, 100, 1000]
#[R1,R2,R3,R4] = [.8, .6, .4, .2]
#[R1,R2,R3,R4] = [1, .1, .01, .001]
[R1,R2,R3,R4] = [.1, .01, .001, .0001]

for t in mfrange(tlo, dt, thi):
	z1 = pathz(R1,t)
	z2 = pathz(R2,t)
	z3 = pathz(R3,t)
	z4 = pathz(R4,t)

	w1 = f(z1)
	w2 = f(z2)
	w3 = f(z3)
	w4 = f(z4)

	#printf_row([t, w1.real, w1.imag], "%.7e")
	#printf_row([t, z1.real, z1.imag, w1.real, w1.imag], "%.7e")

	#printf_row([t, z1.real, z1.imag, z2.real, z2.imag, z3.real, z3.imag, z4.real, z4.imag], "%.7e")
	#printf_row([t, w1.real, w1.imag, w2.real, w2.imag, w3.real, w3.imag, w4.real, w4.imag], "%.7e")

	a1 = abs(w1)
	a2 = abs(w2)
	a3 = abs(w3)
	a4 = abs(w4)
	printf_row([t, a1, a2, a3, a4], "%.7e")
