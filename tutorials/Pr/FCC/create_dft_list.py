#!/usr/bin/env python
import numpy, os


def create_dft_list():
    with open("vrange.inp", "r") as f:
        vmin, vmax, vstep = map(float, f.readlines()[0].split())
    vlist = numpy.arange(vmin, vmax + vstep/2, vstep)
    for i, v in enumerate(vlist):
        vdir = f"V{i}/dft"
        os.makedirs(vdir, exist_ok=True)
        with open(f"{vdir}/ini", "w") as f:
            with open("dft/ini", "r") as fsrc:
                for line in fsrc:
                    if "MULTI_SCF" in line:
                        line = f"MULTI_SCF vv0=  {v:.2f}\n"
                    f.write(line)


if __name__ == "__main__":
    create_dft_list()
