import pandas as pd

#read data set into dataframe
df=pd.read_csv('student.csv')

#if grade<10, assign to gradeband=low
df.loc[df['grade']<10, 'grade_band']='Low'
#if 10<=grade<15, assign gradeband=medium
df.loc[(df['grade']>=10) & (df['grade']<15), 'grade_band']='Medium'
#if grade>=15, assign gradeband=high
df.loc[df['grade']>=15, 'grade_band']='High'

#group data by grade_banf
summaryTable=df.groupby('grade_band').agg(
    #include columns for num_students, avg_absence, internet_access
    num_students=('grade_band', 'count'),
    avg_absence=('absences', 'mean'),
    internet_access=('internet', 'mean')
)

#multilpy interned access by 100 to get percentage
summaryTable['internet_access']= summaryTable['internet_access']*100
#print summary table
print(summaryTable)
#add summary table to csv file
summaryTable.to_csv('student_bands.csv', index=False)