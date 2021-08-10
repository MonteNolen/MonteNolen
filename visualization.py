import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
fig, ax = plt.subplots()
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
ax.scatter(x_values, y_values, c='red', s=10,) #cmap=plt.cm.Blues
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
#ax.axis([0, 110, 0, 1100000])
plt.show()
#print(plt.style.available)
#plt.savefig('squares_plot.png', bbox_inches='tight')