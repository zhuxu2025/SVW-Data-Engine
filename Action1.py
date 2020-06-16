#Action1：求2+4+6+8+...+100的求和，用Python该如何写

import numpy as np
 
a = []
a.append(range(2, 101, 2))
b = np.array(a)
print(b.sum())  #利用numpy的求和函数