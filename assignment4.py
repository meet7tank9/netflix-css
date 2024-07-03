# 1. Consider the sample number of observations:
# 4,20,50,100,30,50,900,500,700,48,90
# Write the Python Program and perform following operations:
# a) Find the mean for the data using the mathematical formula.
# b) Find the median for the data using the mathematical formula.
# c) Find the mode for the data using the mathematical formula.
# d) Find the mean for the data using numpy function.
# e) Find the median for the data using numpy function.
# f) Find the mode for the data using numpy function.

import numpy as np
from scipy import stats

data = [4, 20, 50, 100, 30, 50, 900, 500, 700, 48, 90]

sum=0
for i in data:
    sum+= i

m = sum / len(data)
print("Mean using the mathematical formula :", m)


# b) Find the median using the mathematical formula
data = [4, 20, 50, 100, 30, 50, 900, 500, 700, 48, 90]

for i in range(0,len(data)):
    for j in range(i+1, len(data)):
        if data[i] > data[j]:
            temp=data[i]
            data[i]=data[j]
            data[j]=temp
print(data)
n = len(data)

if n % 2 == 0:
    median = (data[n // 2] + data[n // 2-1]) / 2
else:
    median = data[n // 2]

print("b) Median using the mathematical formula:", median)


# c) Find the mode for the data using the mathematical formula.
data = [4, 20, 50, 100, 30, 50, 900, 500, 700, 48, 90]
mode_formula = max(set(data), key=data.count)
print("c) Mode using the mathematical formula:", mode_formula)


# d) Find the mean using numpy function
mean = np.mean(data)
print("d) Mean using numpy function:", mean)

# e) Find the median using numpy function
median = np.median(data)
print("e) Median using numpy function:", median)

# f) Find the mode using numpy function
# mode = stats.mode(data).mode[0]
# print("f) Mode using numpy function:", mode)




# Consider the following data:
# Purchase Cost Per Pound No of pounds
# 1 3.00 1200
# 2 3.40 500
# 3 2.80 2750
# 4 2.90 1000
# 5 3.25 800
# Write the Python Program and perform following operations:
# a) Find the weighted mean for the data by using the mathematical formula.

data1=[3.00, 3.40, 2.80, 2.90, 3.25]
data2=[1200,500,2750,1000,800]
wixi=0
wi=0
data3=[]
for i in range(len(data1)):
    data3.insert(i,data1[i]*data2[i])
    wixi+=data3[i]
    wi+=data2[i]

print(wixi/wi)




# 3. Consider the following data:
# 5700,5750,5850,5900,6000,6200,6500,6800,7000
# Write the Python Program and perform following operations:

data=[5700,5750,5850,5900,6000,6200,6500,6800,7000]

def percentile(n,data):
    LP=n/100*(len(data)+1)
    print(LP)
    temp=LP
    temp=int(temp)
    decimal=LP-temp
    n1=data[temp-1]
    n2=data[temp-1+1]

    ans=n1+decimal*(n2-n1)
    print(f"{n} percentile of data is : ", ans)


# a) Calculate the 30 percentile of the data using the mathematical formula.
percentile(30,data)

# b) Calculate the 70 percentile of the data using the mathematical formula.
percentile(70,data)
# c) Calculate the First Quartile of the data using the mathematical formula.
percentile(25,data)
# d) Calculate the Third Quartile of the data using the mathematical formula.
percentile(75,data)
# e) Calculate the Inter Quartile Range of the data using the mathematical formula.
print("inter quartile : ", data[len(data)-1] - data[0])




# 4. Consider the following data of number of students in class:
# 46,54,42,46,32,50.
# Write the Python Program and perform following operations:

data=[46,54,42,46,32,50]

# a) Calculate the Variance of the data using the mathematical formula.
sum=0
n=len(data)
for i in data:
    sum+=i

mean=sum/n
print("Mean : ", mean)

data2=[]
data3=[]
sum2=0
for i in range(len(data)):
    data2.insert(i, data[i]-mean)
    data3.insert(i,data2[i]*data2[i])
    sum2+=data3[i]

ans=sum2/(n-1)
print("Variance : ", ans)


# b) Calculate the Standard Deviation of the data using the mathematical formula.
SD=np.sqrt(ans)
print("Standard Daviation : ", SD)

# c) Calculate the Coefficient of Variation of the data using the mathematical formula.
CE=(SD*100)/mean
print("coefficient is : ", CE, "%")

# d) Calculate the Variance of the data using the numpy function.
print(np.var(data))

# e) Calculate the Standard Deviation of the data using the numpy function.
print(np.std(data))