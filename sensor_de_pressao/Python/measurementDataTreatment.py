import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm
import statistics
import statsmodels.api as sm

"""
*Sea level standard atmospheric pressure: 101325 Pa = 1013.25 mbar
*Acceleration due to gravity at sea level: 9.80665 m/s^2
*Water Density: 
https://www.usgs.gov/special-topics/water-science-school/science/water-density
@26.7°C: 0.99669 g/cm^3
https://www.omnicalculator.com/physics/water-density
@25°C, 0% salinity, 1atm: 997.17 kg/m^3
"""

data = np.loadtxt("characterizationData_negative.csv", dtype='float', delimiter=',')
marks = data[9,2:]

fig, axis = plt.subplots(figsize=(10,5))

axis.hist(marks, bins = np.linspace(min(marks), max(marks), num=5))
x_axis = np.arange(min(marks), max(marks), 0.001)
mean = statistics.mean(marks)
sd = statistics.stdev(marks)
plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
plt.show()
print(marks)

y = range(len(marks))
plt.scatter(y,marks)
plt.show()
'''
sm.qqplot(marks, line='45', fit='false')
plt.show()


print(marks)
gas_pressure = 997.17*9.80665*((data[9,0]-data[9,1])/100)
print("Calculation: ", gas_pressure)
mean = statistics.mean(marks)
sd = statistics.stdev(marks)
#sensor_gasPressure = 100*np.mean(data[0,94:])
#std = 100*np.std(data[0,2:])
sensor_gasPressure = 100*mean
std = 100*sd
print("Sensor: ", sensor_gasPressure, "+/-", std)
print("Mean numpy: ", np.mean(marks))
print("Mean statistics: ", statistics.mean(marks))
print("SD numpy: ", np.std(marks))
print("SD statistics: ", statistics.stdev(marks))
'''
