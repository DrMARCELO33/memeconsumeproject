import numpy as np
import matplotlib.pyplot as plt

# Parameters
k = 0.01  # Growth rate constant
I = 0.8   # Intrinsic ability of MEMEcoin (0 to 1)
Q_max = 100  # Maximum quality
V_0 = 10    # Initial memecoin value
r = 0.05    # Memecoin growth rate
t_max = 100 # Time horizon
dt = 0.1    # Time step

# Time array
t = np.arange(0, t_max, dt)

# Memecoin value function
V_t = V_0 * np.exp(r * t)

# Numerical solution for Q(t) using Euler method
Q = np.zeros(len(t))
Q[0] = 0  # Initial quality
for i in range(1, len(t)):
    dQ_dt = k * V_t[i] * I * (Q_max - Q[i-1])
    Q[i] = Q[i-1] + dQ_dt * dt

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, Q, label='AI Quality (Q)')
plt.plot(t, V_t, label='MEMEcoin Value (V)')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('AI Quality vs MEMEcoin Value Over Time')
plt.legend()
plt.grid()
plt.show()