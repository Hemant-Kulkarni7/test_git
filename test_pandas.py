import pandas as pd 
dict1 ={'a':1, 'b':2, 'c':3, 'd':4}        # Define Dictionary 1 
dict2 ={'a':5, 'b':6, 'c':7, 'd':8, 'e':9} # Define Dictionary 2 
Data = {'first':dict1, 'second':dict2}  # Define Data with dict1 and dict2 
df = pd.DataFrame(Data)
#print(df)
#print(df['first'].max())
#print(df.size)
df1 = pd.read_csv('dataset.csv')
#print(df1.head(10)) 
#print(df1.info(null_counts=True))
#print(df1.describe())

#df1.rename(columns = {'User ID':'ID'})

df1.Purchased.fillna(1, inplace = True)     #filling null values

df2 = df1[['EstimatedSalary','Purchased']].corr()     #correlation

df1.Purchased = df1.Purchased.astype(int)       #change data type 

#print(df1.loc[:,['Gender','Purchased']])        #select by row and column

df1 = df1.sort_values(by= 'EstimatedSalary' )       #sorting

filter = df1.Purchased == 1           #selction by condition
df1 = df1[filter]
print(df1)