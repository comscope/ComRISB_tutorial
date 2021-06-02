Installation of ComRISB
=======================

Prerequisites
-------------

ComRISB consists of programs, executables, and scripts, 
written in Fortran90, c (c++) and Python3.
Before you start the installation, 
please make sure that the following packages 
are installed in your system.

* Linux
* GNU make >= 3.82
* Intel Fortran, C and C++ compiler >= 19.0.0.117 20180804
* Intel MKL
* Intel MPI
* parallel hdf5 >= 1.10.3 (configured with CC=mpiicc FC=mpiifort
  CXX=mpiicpc --enable-fortran --enable-fortran2003 
  --enable-parallel --enable-shared)
* Anaconda with python >=3.7

Install
-------
From the folder *comrisb*, type::

    $ make

Hopefully it will finish the compiling and installation without incidents. 
Important settings are located in *arch.mk* file::

 compfl = -O2 -mp1 -w -prec_div -pc80 -pad -ip -DINTEL_VML -traceback
 
 PF90 = h5pfc  # located in bin directory of the parallel hdf5 package.
 F90 = h5pfc
 
 FPPFLAGS += -DUSE_HDF5
 LAPACK_LIB = -mkl
 
 FIX_FORM = -fixed
 FREE_FORM = -free
 
 # C/C++ compiler
 CC = icc
 C++ = icpc
 
 # C compiler options.
 CFLAGS = -O2

Please report problems to `cygutz@gmail.com`.
