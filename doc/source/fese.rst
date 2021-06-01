LQSGW+GRISB calculation of FeSe
-------------------------------
In this example, we illustrate how to perform LQSGW+GRISB calculation of FeSe.

LQSGW calculation of FeSe
=========================
For convenience, we prepared the input file *ini* for LQSGW calculation 
in the folder *lqsgw*. 
Starting with folder *4_FeSe*, 
One could calculate by typing the following command 
or prepare your job file accordingly and submit::

    $ cd lqsgw && mpirun -np 128 ${COMRISB_BIN}/rspflapw.exe && cd ..

Change the number of cores for parallelization as available.
The calculation is nevertheless time-consuming 
and the resulting data file is several GB. 
For convenience, the results have been precalculated 
and can be downloaded `here <https://www.dropbox.com/s/x9oz9kd6m3bh6e2/lqsgw_fese.tar.gz?dl=0>`_. 
If you choose to download the precalculated results, 
please move the downloaded file *lqsgw_fese.tar.gz* 
to the current folder *4_FeSe* and type::

    $ tar -xzf lqsgw_fese.tar.gz

This should create the file *lqsgw* with calculation results inside. 

LQSGW+GRISB calculation of FeSe
===============================


