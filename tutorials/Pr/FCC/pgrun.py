#!/usr/bin/env python
import os, subprocess, multiprocessing

def spawn():
    print(f"cwd: {os.getcwd()}")
    cmd = ["mpirun", "-np", "1",
            "/home/ykent/GitLab/comrisb/bin/rspflapw.exe"]
    subprocess.run(cmd)


def pgwrun():
    for i in range(3):
        path = f"V{i}"
        print(f"working at {path}")
        os.chdir(f"{path}/dft")
        p = multiprocessing.Process(target=spawn)
        p.start()
        os.chdir("../../")


if __name__ == "__main__":
    pgwrun()
