print ('Hello World! This is branch1!')

import numpy as np
from scipy import linalg as la

A = np.eye(3)
A[0,2] = 3
A[2,0] = 3
print (A)
e, v = la.eig(A)
print(e)
