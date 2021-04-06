import h5py, itertools, numpy
import matplotlib.pyplot as plt


e_skn = []
k_dist = []
k_tick_label = []
k_tick_pos = []
file_list = ["../dftg/u0j0_1iter/lowh/bands_plot.h5",
        "../dftg/u5j0.8_1iter/lowh/bands_plot.h5",
        "../lqsgw_risb/u0j0/lowh/bands_plot.h5",
        "../lqsgw_risb/u5j0.8/lowh/bands_plot.h5",
        ]

# expt
gamma1 = numpy.loadtxt("gamma.dat")
gamma2 = numpy.loadtxt("gamma2.dat")
m1 = numpy.loadtxt("m.dat")
m2 = numpy.loadtxt("m2.dat")

for fname in file_list:
    with h5py.File(fname, "r") as f:
        e_skn.append(f["/e_skn"][()])
        k_dist.append(f["/k_dist"][()])
        k_tick_label.append([s.decode("utf-8")  \
                for s in f["/k_tick_label"][()]])
        k_tick_pos.append(f["/k_tick_pos"][()])


fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(8, 6))
for ij, ij2 in enumerate(itertools.product(range(2), repeat=2)):
    i, j = ij2
    for n in range(e_skn[ij].shape[2]):
        axs[i, j].plot(k_dist[ij], e_skn[ij][0, :, n], 'k-')
    axs[i, j].plot(-gamma1[:, 0]/(2*numpy.pi), gamma1[:, 1], "+", color='k')
    axs[i, j].plot(-gamma2[:, 0]/(2*numpy.pi), gamma2[:, 1], "+", color='k')
    axs[i, j].plot(m1[:, 0]/(2*numpy.pi)+k_dist[ij][-1],
            m1[:, 1]/1000, "+", color='k')
    axs[i, j].plot(m2[:, 0]/(2*numpy.pi)+k_dist[ij][-1],
            m2[:, 1]/1000, "+", color='k')
    axs[i, j].axhline(y = 0, ls = ':', lw = 2)
    # High-symmetry lines and labels
    for x1 in k_tick_pos[ij][1:-1]:
        axs[i, j].axvline(x = x1, ls = '--')
    axs[i, j].set_xticks(k_tick_pos[ij])
    ktick_label = [r"${}$".format(s) for s in k_tick_label[ij]]
    axs[i, j].set_xticklabels(ktick_label)
    axs[i, j].set_xlim(k_dist[ij][0], k_dist[ij][-1])
    axs[i, j].set_ylim(-0.2, 0.2)

axs[0, 0].set_ylabel("E (eV)")
axs[1, 0].set_ylabel("E (eV)")

fig.tight_layout()
plt.show()
fig.savefig("FeSeBands.pdf")

