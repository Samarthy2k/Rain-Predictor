import pandas as pd
import glob
import csv

path = r"C:\Users\Pratheek S B\Desktop\Logs\*.csv"
for fname in glob.glob(path):
	df=pd.read_csv(fname,usecols=[0,5,6])
	df.to_csv(fname, index=False)
	count_row = df.shape[0]
	if(count_row<480):
		count=480-count_row-1
		while(count!=0):
			row=df.iloc[count_row-1]
			df=df.append(row)
			count=count-1
	df.to_csv(fname, index=False)
	