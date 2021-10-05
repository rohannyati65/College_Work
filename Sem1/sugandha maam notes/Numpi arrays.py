# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:53:47 2019

@author: sugandha.sharma
"""



import numpy as np
a=np.array([1,2,3])
print(a)


import numpy as np
b=np.array([(1,2,3),(4,5,6)])
print(b)

import numpy as np
my_mat = [[1,2,3], [4,5,6], [7,8,9]] 
np.array(my_mat)

"""***finding dimension of an array """
import numpy as np
b=np.array([(1,2,3),(4,5,6),(7,8,9)])
print(b.ndim)


"""Finding size of each element/item of numpy array """
import numpy as np
b=np.array([(1,2,3),(4,5,6)])
print(b.itemsize)




"""Finding datatype of the array elements """
import numpy as np
b=np.array([(1,2,3),(4,5,6)])
print(b.dtype)

"""Finding size of an array (total number of elements
 in an array) """
import numpy as np
b=np.array([(1,2,3),(4,5,6)])
print(b.size)



"""Finding shape of an array  (rows,columns)"""
import numpy as np
b=np.array([(1,2,3),(4,5,6)])
print(b.shape)



"""Reshaping of  array """
import numpy as np
b=np.array([(1,2,3,4),(4,5,6,7)])#2 rows and 4 columns
print(b)

b=b.reshape(4,2)#4 rows and 2 columns
print(b)


"""linspace   creates a 1 D array of equally 
spaced elements"""
import numpy as np
b=np.linspace(1,10,5)
print(b)


"""Maximum value in an array """
import numpy as np
b=np.array([(1,2,3,4),(4,5,6,7)])#2 rows and 4 columns
print(b.max())


"""Minimum value in an array """
import numpy as np
b=np.array([(1,2,3,4),(4,5,6,7)])#2 rows and 4 columns
print(b.min())


"""Sum of all elements in an array """
import numpy as np
b=np.array([(1,2,3,4),(4,5,6,7)])#2 rows and 4 columns
print(b.sum())


"""sum of elements in each column  axis=0"""
import numpy as np
b=np.array([(1,2,3,4),(4,5,6,7)])#2 rows and 4 columns
print(b.sum(axis=0))


"""sum of elements in each row  axis=1"""
import numpy as np
b=np.array([(1,2,3,4),(4,5,6,7)])#2 rows and 4 columns
print(b.sum(axis=1))


"""square-root of each element of an array """
import numpy as np
b=np.array([(1,2,3,4),(4,5,6,7)])
print(np.sqrt(b))


"""standard deviation """
import numpy as np
b=np.array([(1,2,3,4),(4,5,6,7)])
print(np.std(b))


"""Addition of two arrays """
import numpy as np
b=np.array([(1,2,3,4),(4,5,6,7)])#2 rows and 4 columns
c=np.array([(1,2,3,4),(4,5,6,7)])
print(b+c)




"""subtraction of two arrays """
import numpy as np
b=np.array([(1,2,3,4),(4,5,6,7)])#2 rows and 4 columns
c=np.array([(1,2,3,4),(4,5,6,9)])
print(c-b)




"""Multiplication  of two arrays """
import numpy as np
b=np.array([(1,2,3,4),(4,5,6,7)])#2 rows and 4 columns
c=np.array([(1,2,3,4),(4,5,6,7)])
print(b*c)




"""Division of two arrays """
import numpy as np
b=np.array([(1,2,3,4),(4,5,6,7)])#2 rows and 4 columns
c=np.array([(1,2,3,4),(4,5,6,7)])
print(b/c)





"""Vertical stacking of two arrays """
import numpy as np
b=np.array([(1,2,3,4),(4,5,6,7)])#2 rows and 4 columns
c=np.array([(8,9,10,11),(4,5,6,7)])
print(np.vstack((c,b)))


"""horizontal stacking of two arrays """
import numpy as np
b=np.array([(1,2,3,4),(4,5,6,7)])#2 rows and 4 columns
c=np.array([(8,9,10,11),(4,5,6,7)])
print(np.hstack((c,b)))




"""convert a multi D array into 1 D array """
import numpy as np
b=np.array([(1,2,3,4),(4,5,6,7)])

print(np.ravel(b))





"""
The syntax of numpy.arange function is the following.

numpy.arange(start, stop, step, dtype)

The parameters are the following.

start: number, optional. Start of an interval. 
The interval includes this value. The default start 
value is 0.

stop: number. End of the interval. 
The interval does not include stop value, 
except in some cases where a step is not an integer
 and floating-point round-off affects the length of out. 

step: number, optional. step can’t be zero. 
Otherwise, you’ll get a ZeroDivisionError. 
You can’t move away anywhere from the start if the 
increment or decrement is 0.

dtype: The type of an output array.
 If the dtype is not given,
 infer the data type from the other input arguments. 
 If dtype is omitted, arange() will try to deduce the
 type of the array elements from the types of start, 
 stop, and step.






"""




"""Plotting a graph sin(),cos() and tan()"""


import numpy as np
import matplotlib.pyplot  as plt#2 rows and 4 columns
#c=np.array([(1,2,3,4),(4,5,6,7)])
x=np.arange(0,np.pi,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.show()


import numpy as np
import matplotlib.pyplot  as plt#2 rows and 4 columns
#c=np.array([(1,2,3,4),(4,5,6,7)])
x=np.arange(0,np.pi,0.1)
y=np.cos(x)
plt.plot(x,y)
plt.show()


import numpy as np
import matplotlib.pyplot  as plt#2 rows and 4 columns
#c=np.array([(1,2,3,4),(4,5,6,7)])
x=np.arange(0,np.pi,0.1)
y=np.tan(x)
plt.plot(x,y)
plt.show()
