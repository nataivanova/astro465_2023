import os
import mesa_read as ms
import matplotlib.pyplot as plt
import numpy as np

# this files extracts data in a simple profile the way you would want it
# change "./" to the actual directory where your file is located
# the file is to start with profile

p1 = ms.mesa_profile("./", num="_last")

# you can add here any variable which you previosly stored using profile_columns.list 
x1=np.array(p1.get('mass'))
x2=np.array(p1.get('logR'))
x3=np.array(p1.get('energy'))


# you can do any data work you need within python


# here are a couple of lines to output data if you want to work with it outside of python

zipped = [ *zip(x1,x2,x3) ]
#if you use python eralier than 3, use instead the next line
#zipped = zip(x1,x2,x3) 

np.savetxt('data_profile.txt',zipped, newline='\n')
