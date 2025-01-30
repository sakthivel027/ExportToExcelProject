#models.py file
Matplotlib
import matplotlib.pyplot as plt
year=[1950,1970,1990,2010]
pop=[2.4,4.5,6.5,7.2]
plt.plot(year,pop)
plt.show()

import matplotlib.pyplot as plt
year=[1950,1970,1990,2010]
pop=[2.4,4.5,6.5,7.2]
plt.scatter(year,pop,alpha=0.8) 
#s also agrument for size which is by default none
#alpha can vary from 0 to 1 for opacity
plt.show()

Histogram
import matplotlib.pyplot as plt
values=[2.4,4.5,6.5,7.2,3.4,5.6,6.7,2.3]
#by default bins=10
plt.hist(values,bins=3)
plt.show()


