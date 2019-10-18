import pandas as pd 

dict1 ={'a':1, 'b':2, 'c':3, 'd':4}        # Define Dictionary 1 
dict2 ={'a':5, 'b':6, 'c':7, 'd':8, 'e':9} # Define Dictionary 2 
Data = {'first':dict1, 'second':dict2}  # Define Data with dict1 and dict2 
df = pd.DataFrame(Data)
#print(df.shape)
#print(df['first'].max())
#print(df.size)

df1 = pd.read_csv('dataset.csv')
#print(df1.head(10)) 
#print(df1.info(null_counts=True))
#print(df1.describe())

#df1.rename(columns = {'ID':'User_ID'}, inplace = True)      #rename columns

#df1.Purchased.fillna(1, inplace = True)     #filling null values

#df2 = df1[['EstimatedSalary','Purchased']].corr()     #correlation

#df1.Purchased = df1.Purchased.astype(int)       #change data type 

#print(df1.loc[:,['Gender','Purchased']])        #select by row and column

#df1 = df1.sort_values(by= 'EstimatedSalary' )       #sorting

#filter = df1.Purchased == 1           #selction by condition
#df1 = df1[filter]
#print(df1)

#df1.drop(columns = ['Age'], inplace = True)    #drop column
#print(df1)

#print(df1.at[4,'Age'])                 #selection by row/column pair

#num = [1,2,3,4,5,6,7,8,9]                 #insert column
#df1.insert(5, 'number', num,)



df1.Age = df1.Age.astype(int)
df1.EstimatedSalary = df1.EstimatedSalary.astype(int)
print(df1)
df2 = df1[['EstimatedSalary','Age']].corr() 
print(df2)