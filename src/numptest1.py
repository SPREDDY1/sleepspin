import numpy as np
import matplotlib.pyplot as plt

a=np.arange(100).reshape(10, 10)
print(a.ndim)
print(a.size)

b=np.array([[1,2,3,4,5],[9,99,999,999,9999]],dtype=complex)
print(b)

c=np.zeros((2,2))
print(c)

d=np.ones((2,2),dtype=np.int16)
print(d@c)

e=np.empty((2,2),dtype=np.int16)
print(e@d)

x=np.arange( 10, 20, 3 )
print(x)

y=np.linspace( 1, 2, 10,dtype=np.float16 )
print(y)

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
#plt.plot(x, x**2, label='quadratic')
#plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()