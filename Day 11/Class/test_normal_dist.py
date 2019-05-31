
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib.mlab as mlab


#opening csv file
with open("data/human_body_temperature.csv",mode = "rt") as file:
    data = file.readlines()
    
#deleting column name from etracted data
del(data[0])

#creating list of temperature
list1 = []
for i in data:
    a = i.split(",")
    list1.append(float(a[0]))
    
#creating array of data
arr = np.array(list1, dtype = float)


#plt.hist(arr,7)
#plt.show


#plt.figure(1)a

arr.min()

arr.max()


plt.hist(arr,normed=True,color='black',bins=7)
plt.xlim((min(arr), max(arr)))
    
x = np.linspace(min(arr), max(arr), 100)
plt.plot(x, mlab.normpdf(x, np.mean(arr), np.sqrt(np.var(arr))),color="red")
plt.show()
    


# Normal distribution Test

print("mean is:",np.mean(arr))
print("median is",np.median(arr))
print("mode is",stats.mode(arr))


stats, pvalue = stats.normaltest(list1)
if pvalue > 0.05:
    print("Data is normally distributed")
else:
    print("Data is not normally distributed")
        
        
        

    