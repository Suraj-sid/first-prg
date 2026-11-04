import time
lst=[1,2,4,5,6,7,9]
start=time.time()
print(23 in lst)
end=time.time()
print(end-start)


import sys
tup=(1,2,23,55)
p=sys.getsizeof(tup)
print(p)

import sys 
lst=[1,2,23,55]
p=sys.getsizeof(lst)
print(p)