import os
import mesa_read as ms
import matplotlib.pyplot as plt
import numpy as np

# change the directory below to a directory where your history file is located

m1 = ms.history_data("./LOGS")

# browse your history file for more variables that you may want to plot. Only a few examples are listed below

mass = m1.get('star_mass')
age = m1.get('star_age')
radius = m1.get('log_R')

#make sure that you have stored the quantity that you want to plot, by listing it before your code ran in the 'history_columns.list'
#fe_core_mass=m1.get('fe_core_mass')
#si_core_mass=m1.get('si_core_mass')
#o_core_mass=m1.get('o_core_mass')
#c_core_mass=m1.get('c_core_mass')
#he_core_mass=m1.get('he_core_mass')


# this is if you need to plot with "reversed" time axis
#age_final=2.0543e8
#time=np.array(np.log10(age_final-age))

# you can also plot evolution of any variable against another. Plotting Teff vs L (do not forget the direction for Teff!) will make HR diagram 

plt.plot(age,radius)
plt.ticklabel_format(axis='x',style='sci',scilimits=(0,0)) 

# asjust the limits if needed
#plt.xlim(-2., 0.)
#plt.ylim(0., 20.)

# do change the label to reflect what are you plotting!!!!
plt.xlabel('Star Age, years')
plt.ylabel('log_{10} (Radius, $R_\odot)$')
plt.savefig('radius')
