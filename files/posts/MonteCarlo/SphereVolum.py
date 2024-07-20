import numpy as np
import matplotlib.pyplot as plt
# timing
import time
import itertools

def grid_volume(n, d):

    # set range to be from -1 to 1
    ran = np.linspace(-1, 1, n)

    # run through all possible points in unit cube
    count = 0
    for i in itertools.product(ran, repeat=d):
        # check if point is inside the sphere
        if sum([x**2 for x in i]) <= 1:
            count += 1        

    # Compute the volume of the sphere
    return 2**d * count / n**d

def monte_carlo_volume(n, d):
    
        count = 0
    
        # Generate n random points in the unit cube
        for _ in range(n):
            point = np.random.rand(d)
            # Check if the point is inside the sphere
            if sum([x**2 for x in point]) <= 1:
                count += 1
    
        # Compute the volume of the sphere
        return 2**d * count / n

def monte_carlo_volume_comparison(n, d, d_sphere_volume, Griderror):
    
    count = 0
    npoints = 0
    error = 1000

    # we run the method until the error is less than the Griderror
    while error > Griderror:
        npoints += 1

        # Generate a random point in the unit cube
        point = np.random.rand(d)
        # Check if the point is inside the sphere
        if sum([x**2 for x in point]) <= 1:
            count += 1

        # Compute the volume of the sphere and the error
        aux_volume = 2**d * count / npoints
        error = abs(d_sphere_volume - aux_volume)
    
    # Return the volume of the sphere and the number of points used
    return 2**d * count / npoints, npoints


volumes_grid = []
volumes_monte = []
monte_npoints = []

timings_grid = []
timings_monte = []

dims = [1, 2, 3, 4]
quantities = [10, 20, 30, 40, 50, 100]


######################## comparison #############################
# for d in dims:

#     print(f'Running for {d} dimensions')

#     grid_aux = []
#     monte_aux = []

#     timings_grid_aux = []
#     timings_monte_aux = []
#     monte_npoints_aux = []

#     for n in quantities:

#         print(f'Running for {n} side-points')

#         time_start = time.time()
#         v_grid = grid_volume(n, d)
#         time_end = time.time()
#         print(f'Grid volume with {n**d} points: {v_grid}' + 'with time: ' + str(time_end - time_start))
#         timings_grid_aux.append(time_end - time_start)

#         d_sphere_volume = np.pi**(d/2) / np.math.gamma(d/2 + 1)
#         print(f'Volume of a {d}D sphere: {d_sphere_volume}')
#         Griderror = abs(d_sphere_volume - v_grid)

#         time_start = time.time()
#         v_monte, mc_np = monte_carlo_volume_comparison(n, d, d_sphere_volume, Griderror)
#         time_end = time.time()
#         print(f'Monte Carlo volume with {n**d} points: {v_monte}' + 'with time: ' + str(time_end - time_start))
#         timings_monte_aux.append(time_end - time_start)
#         monte_npoints_aux.append(mc_np/n**d)

#         grid_aux.append(v_grid)
#         monte_aux.append(v_monte)

#     volumes_grid.append(grid_aux)
#     volumes_monte.append(monte_aux)
#     monte_npoints.append(monte_npoints_aux)

#     timings_grid.append(timings_grid_aux)
#     timings_monte.append(timings_monte_aux)

# # plot grid results with two plots, one is timing and the other is volume
# fig, ax = plt.subplots(2, 2)

# ax[0, 0].plot(quantities, volumes_grid[1], label='Grid')
# ax[0, 0].grid()
# ax[0, 0].set_xticks(quantities)
# ax[0, 0].set_xlabel('Number of points')
# ax[0, 0].set_ylabel('Volume')
# ax[0, 0].set_title('Volume of a 2D sphere by grid method')
# ax[0, 0].legend()

# ax[0, 1].plot(quantities, timings_grid[0], label='Grid')
# ax[0, 1].grid()
# ax[0, 1].set_xticks(quantities)
# ax[0, 1].set_xlabel('Number of points')
# ax[0, 1].set_ylabel('Time')
# ax[0, 1].set_title('Time of a 2D sphere by grid method')
# ax[0, 1].legend()

# # for 50 points
# ax[1, 0].plot(dims, [volumes_grid[i][-1] for i in range(len(dims))], label='Grid')
# ax[1, 0].grid()
# ax[1, 0].set_xticks(dims)
# ax[1, 0].set_xlabel('Number of dimensions')
# ax[1, 0].set_ylabel('Volume')
# ax[1, 0].set_title('Volume of a sphere by grid method with 100 points')
# ax[1, 0].legend()

# ax[1, 1].plot(dims, [timings_grid[i][-1] for i in range(len(dims))], label='Grid')
# ax[1, 1].grid()
# ax[1, 1].set_xticks(dims)
# ax[1, 1].set_xlabel('Number of dimensions')
# ax[1, 1].set_ylabel('Time')
# ax[1, 1].set_title('Time of a sphere by grid method with 100 points')
# ax[1, 1].legend()

# plt.tight_layout()
# plt.show()

# plot monte_npoints for the fourth dimension
# fig, ax = plt.subplots(1, 1)

# ax.plot(quantities, monte_npoints[0], label='1D')
# ax.plot(quantities, monte_npoints[1],label='2D')
# ax.plot(quantities, monte_npoints[2],  label='3D')
# ax.plot(quantities, monte_npoints[3],  label='4D')
# ax.grid()
# ax.set_xticks(quantities)
# ax.set_xlabel('Number of points in Grid side')
# ax.set_ylabel('Ratio of points Monte Carlo/Grid')
# ax.set_title('Comparison of points used by Monte Carlo and Grid methods')
# ax.legend()

# plt.tight_layout()
# plt.show()


######################################################
###############      Monte Carlo     #################

# dims = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# for d in dims:

#     print(f'Running for {d} dimensions')

#     n = int(100**(np.math.log(d, 3)+0.8))

#     print(f'Running for {n} points')

#     v_monte = monte_carlo_volume(n, d)
#     print(f'Monte Carlo volume with {100**d} points: {v_monte}')

#     volumes_monte.append(v_monte)


# # plot monte results

# fig, ax = plt.subplots(1, 1)

# ax.plot(dims, volumes_monte, label='Monte Carlo')
# ax.grid()
# ax.set_xticks(dims)
# ax.set_xlabel('Number of dimensions')
# ax.set_ylabel('Volume')
# ax.set_title('Volume of a sphere by Monte Carlo method')
# ax.legend()

# plt.tight_layout()
# plt.show()

####################################################
###################### Explicit curve ##############

dims = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
volumes = []

for d in dims:

    print(f'Running for {d} dimensions')

    v = np.pi**(d/2) / np.math.gamma(d/2 + 1)
    print(f'Volume of a {d}D sphere: {v}')

    volumes.append(v)

# plot results

fig, ax = plt.subplots(1, 1)

ax.plot(dims, volumes, label='Explicit')
ax.grid()
ax.set_xticks(dims)
ax.set_xlabel('Number of dimensions')
ax.set_ylabel('Volume')
ax.set_title('Volume of a sphere by explicit formula')
ax.legend()

plt.tight_layout()
plt.show()

