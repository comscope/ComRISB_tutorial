import h5py
import matplotlib.pyplot as plt


with h5py.File("/home/ykent/GWIEN/example/MnO/results.h5", "r") as f:
    elist1 = f["/lapw/e_list"][()]
    vlist1 = f["/lapw/v_list"][()]

with h5py.File("./results.h5", "r") as f:
    elist2 = f["/dft/e_list"][()]
    vlist2 = f["/dft/v_list"][()]

# shift
elist2 += elist1[-1] - elist2[-1]

plt.plot(vlist1, elist1)
plt.plot(vlist2, elist2, "o")
plt.show()
