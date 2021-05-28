import h5py, numpy
import matplotlib.pyplot as plt


# spin resolved arpes data
updata = numpy.loadtxt("uparpes.dat", delimiter=",").T
dndata = numpy.loadtxt("dnarpes.dat", delimiter=",").T

e_skn = []
k_dist = []
k_tick_label = []
k_tick_pos = []
file_list = ["../u5j0.8_fm/lowh/bands_plot.h5",
        "../u5j0.8_fm/lowh_kpath/bands_plot.h5"]

for fname in file_list:
    with h5py.File(fname, "r") as f:
        e_skn.append(f["/e_skn"][()])
        k_dist.append(f["/k_dist"][()])
        k_tick_label.append([s.decode("utf-8")  \
                for s in f["/k_tick_label"][()]])
        k_tick_pos.append(f["/k_tick_pos"][()])


fig, ax = plt.subplots(1, 2,
        gridspec_kw={'width_ratios': [k_dist[0][-1], k_dist[1][-1]]},
        figsize=(6, 4))

for i, ax1 in enumerate(ax):
    for n in range(e_skn[0].shape[2]):
        ax1.plot(k_dist[i], e_skn[i][0, :, n], 'k-')
        ax1.plot(k_dist[i], e_skn[i][1, :, n], 'r--')
    ax1.axhline(y = 0, ls = ':', lw = 2)
    # High-symmetry lines and labels
    for x1 in k_tick_pos[i][1:-1]:
        ax1.axvline(x = x1, ls = '--')
    ax1.set_xticks(k_tick_pos[i])
    ktick_label = [r"${}$".format(s) for s in k_tick_label[i]]
    ax1.set_xticklabels(ktick_label)
    ax1.set_xlim(k_dist[i][0], k_dist[i][-1])
    ax1.set_ylim(-4, 4)

ax[0].set_ylabel("E (eV)")
ax[1].get_yaxis().set_ticklabels([])
ax[1].scatter(updata[0], updata[1], marker='o', c='k')
ax[1].scatter(dndata[0], dndata[1], marker='d', c='r')
fig.tight_layout()
plt.show()
fig.savefig("FeFMBands.pdf")

