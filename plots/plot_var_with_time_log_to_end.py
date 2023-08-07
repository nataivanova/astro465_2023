import os
import mesa_read as ms
import matplotlib.pyplot as plt
import numpy as np

# change the directory below to a directory where your history file is located
# if run is not finished, or recalculated, delete LOGS/history.datasa file

f1 = ms.history_data("./LOGS/")

# browse your history file for more variables that you may want to plot. Only a few examples are listed below
mass = f1.get('star_mass')
age = f1.get('star_age')
radius = f1.get('log_R')
fe_core_mass=f1.get('fe_core_mass')
si_core_mass=f1.get('si_core_mass')
o_core_mass=f1.get('o_core_mass')
c_core_mass=f1.get('c_core_mass')
he_core_mass=f1.get('he_core_mass')
pp=f1.get('pp')
cno=f1.get('cno')
tri_alfa=f1.get('tri_alfa')

# this is if you need to plot with "reversed" time axis
#age_final=2.0543e8
#time=np.array(np.log10(age_final-age))

plt.figure(1)
plt.plot(age,pp,color='red')
plt.plot(age,cno,color='blue')
plt.plot(age,tri_alfa,color='black')
plt.ticklabel_format(axys='x',style='sci',scilimits=(0,0))

# asjust the limits if needed
#plt.xlim(-2., 0.)
#plt.ylim(0., 20.)

# do change the label to reflect what are you plotting!!!!
plt.xlabel('Star Age, years in units')
plt.ylabel('Nuclear reactions')
plt.savefig('nuclear')
