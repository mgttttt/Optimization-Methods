from matplotlib import pyplot as plt
import numpy as np
# Let's redefine the function f(y(t)) according to the new conditions provided.
def f(y):
    if y <= h:
        return 1
    else:
        return -1

# Let's set up the simulation parameters again.
delta_t = 1  # Time step, Δt
total_time = 50  # Total time for simulation
h = 10  # Desired height (threshold)

# Initial conditions for the three scenarios
initial_conditions = [h+10, h-10, h]  # y0 > h, y0 < h, y0 = h

# Set up the plot
plt.figure(figsize=(12, 6))

# Simulation for each initial condition
for y_0 in initial_conditions:
    # Time points
    t = np.arange(0, total_time, delta_t)
    # Initialize the height array
    y = np.zeros(len(t))
    y[0] = y_0

    # Simulation loop
    for i in range(1, len(t)):
        y[i] = y[i-1] + delta_t * f(y[i-1])

    # Plotting the results
    plt.plot(t, y, label=f'y0 = {y_0}')

# Plot the desired height line
plt.axhline(y=h, color='r', linestyle='--', label='Desired height h')
plt.title('Automatic Altitude Control System Simulation for Different Initial Conditions')
plt.xlabel('Time (t)')
plt.ylabel('Height (y(t))')
plt.legend()
plt.grid(True)
plt.show()
