#First we need to import csv module of pythan
import csv
# give file name of csv file
filename ='D:\\Machine Learing\\iris-species\\Iris.csv'

#Open that csv file
# try:
with open(filename,'r') as csvfile:
        lines=csv.reader(csvfile)
        for row in lines:
         print (', '.join(row) ) 



