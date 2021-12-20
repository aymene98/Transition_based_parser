import matplotlib.pyplot as plt
import numpy as np
# Values for the graphs
# Preffixes (100):
mean_las = [42.183,46.805,45.965] 
std_las = [5.182,6.103,6.432]
#yerr = std_las
mean_uas = [51.793,55.848,53.295] 
std_uas = [2.677,5.140,5.323]
# Preffixes (150):
"""
mean_las = [41.368,48.12,47.538] 
std_las = [5.160,5.972,7.218]
#yerr = std_las
mean_uas = [50.623,56.813,55.753] 
std_uas = [3.447,5.377,	5.506]

"""
# Suffixes (100):
"""
mean_las = [44.73,	45.673	,46.743] 
std_las = [6.103,5.157,	7.160]
#yerr = std_las
mean_uas = [54.358,	54.153,	53.93] 
std_uas = [3.514,	3.713,	6.502]

"""
# Suffixes (150):
"""
mean_las = [44.458,	48.232,	48.59] 
std_las = [5.045,4.805,5.938]
#yerr = std_las
mean_uas = [54.323,56.558,56.693] 
std_uas = [4.901,2.803,5.401]

"""
fig = plt.figure()
x = [2,3,4]

plt.errorbar(x, mean_las, yerr=std_las, capsize = 5, fmt='bo',label = "LAS")
plt.errorbar(x, mean_uas, yerr=std_uas, capsize = 5, fmt='ro',label = "UAS")
#plt.ylabel('LAS')
plt.xlabel('Taille des Preffixes')
plt.title('A')
my_xticks = [2,3,4]#['2',"","","","3","","", "","4"]
plt.xticks(x, my_xticks)
plt.ylim([0, 100])
plt.legend()
plt.show()
"""
# Create lists for the plot
mean = [42.183,46.805,45.965]
std = [5.182,6.103,6.432]
materials = ['Aluminum', 'Copper', 'Steel']
x_pos = np.arange(len(materials))
CTEs = [mean]
error = [std]

# Build the plot
fig, ax = plt.subplots()
ax.bar(x_pos, CTEs, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
ax.set_ylabel('Coefficient of Thermal Expansion ($\degree C^{-1}$)')
ax.set_xticks(x_pos)
ax.set_xticklabels(materials)
ax.set_title('Coefficent of Thermal Expansion (CTE) of Three Metals')
ax.yaxis.grid(True)

# Save the figure and show
plt.tight_layout()
plt.savefig('bar_plot_with_error_bars.png')
plt.show()
"""
"""
# example data
x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)

# example variable error bar values
yerr = 0.1 + 0.2*np.sqrt(x)
xerr = 0.1 + yerr

# First illustrate basic pyplot interface, using defaults where possible.
plt.figure()
plt.errorbar(x, y, xerr=0.2, yerr=0.4)
plt.title("Simplest errorbars, 0.2 in x, 0.4 in y")
plt.show()
"""
"""
# Mean
x2 = [2,3,4]
y2 = [42.183,46.805,45.965]
plt.plot(x2,y2,"blue", label = "Mean")
plt.scatter(x2,y2,s=300,color='blue')

# STD
x1 = [2,3,4]
y1 = [5.182,6.103,6.432]
plt.plot(x1,y1,"red",label = "SD")
plt.scatter(x1,y1,s=300,color='red')

plt.xlabel('Taille des Preffixes')
# Set the y axis label of the current axis.
plt.ylabel('LAS')
# Set a title of the current axes.
plt.title('LAS Moyanne et SD x Taille des Preffixes')
#plt.xticks(range(len([0,2,3,4])), [0,2,3,4])
#plt.grid()
#plt.xticks(range(len([0,2,3,4])), [0,2,3,4])
plt.legend()

#plt.savefig("scatter_points_order_01.png", bbox_inches='tight')
plt.show()
plt.close()
"""