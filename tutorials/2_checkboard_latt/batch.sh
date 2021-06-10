#!/bin/bash

mkdir -p work && cd work
python3.7 ../scan_checkboard.py --skipshow
python3.7 ../scan_checkboard.py -sp --skipshow
python3.7 ../scan_checkboard.py -uhf --skipshow
python3.7 ../scan_checkboard.py -rhf --skipshow

# 329.65user 1633.46system 37:40.60elapsed 86%CPU (0avgtext+0avgdata 153788maxresident)k
# 65384inputs+342472outputs (83major+117692484minor)pagefaults 0swaps
