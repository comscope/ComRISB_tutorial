#!/usr/bin/env python
import numpy, os, subprocess


def create_dft_list():
    with open("vrange.inp", "r") as f:
        vmin, vmax, vstep = map(float, f.readlines()[0].split())
    vlist = numpy.arange(vmin, vmax + vstep/2, vstep)
    for i, v in enumerate(vlist):
        vdir = f"V{i}/dft"
        os.makedirs(vdir, exist_ok=True)
        os.chdir(vdir)
        print(f"working at {vdir}")
        cmd = ["/home/ykent/GitLab/comrisb/ComBin/cif2matdelab.py",
                "--rmt", "{25: 1.84, 8:1.58}", "-k", "4.5",
                "../../MnO.cif", "--vv0", f"{v}"]
        subprocess.run(cmd)
        os.chdir("../..")


if __name__ == "__main__":
    create_dft_list()
