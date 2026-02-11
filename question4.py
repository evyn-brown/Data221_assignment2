import pandas as pd

#read file into pandas dataframe
df=pd.read_csv('student.csv')

#create new datafram using rows with studytime>3, internet=1, absence<5
newDf=df[
    (df['studytime']>=3)&
    (df['internet']==1) &
    (df['absences']<=5)
]

#add new dataframe to high-engagement csv
newDf.to_csv('high_engagement.csv', index=False)

#make new variable by calculating mean of 'grade' column in new dataframe
averageGrade=newDf['grade'].mean()
#count number of students who meet the required stats
numStudents=len(newDf.columns)
#print to user
print(f"Number of students: {numStudents}\nAverage grade: {averageGrade}")