import csv
from statistics import median 

with open("a.csv",newline='')as f:
    reader =csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
#Sorting data to get the height of the people
new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))
#Getting the mean
n=len(new_data)
total=0
for x in new_data:
    total+=x
mean=total/n
print("Mean/Average Is :"+str(mean))

# median

n=len(new_data)
new_data.sort()
if(n%2==0):
  median1=new_data[n//2]
  median2=new_data[n//2-1]
  median=(median1+median2)/2
  print('even')
else:
  median=new_data[n//2]
  print('odd')
print("median is ----> ",str(median))

# mode
from collections import Counter

data=Counter(new_data)

mode_range={"50-60":0,"60-70":0,"70-80":0}
for height,occ in data.items():
  if 50<height<60:
    mode_range["50-60"]=mode_range["50-60"]+occ
  elif 60<height<70:
    mode_range["60-70"]=mode_range["60-70"]+occ
  elif 70<height<80:
    mode_range["70-80"]=mode_range["70-80"]+occ

print("Mode is ----->",mode_range)
