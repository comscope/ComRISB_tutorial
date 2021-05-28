import h5py


with h5py.File("../../u7j0.8/lowh/wannier_den_matrix.dat", "r") as f:
    data = f["/n_matrix_new"][()]


res = 0
for mat in data:
    res += mat.trace()


print(res)
