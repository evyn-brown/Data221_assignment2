import pandas as pd

#open crime file as dataframe
df=pd.read_csv('crime.csv')

#if violentCrimes>=0.5 assign risk=highcrime
df.loc[df['ViolentCrimesPerPop']>=0.5, 'Risk']='HighCrime'
#if violentCrimes<0.5, assign risk=lowcrime
df.loc[df['ViolentCrimesPerPop']<0.5, 'Risk']='LowCrime'

#group datafram by risk, compute percent unemployed for each risk category
groupByRisk=(df.groupby('Risk')['PctUnemployed'].mean())*100

#get value for avg unemployement for high risk category
highCrimeUnemployed=groupByRisk.loc['HighCrime']
#get value for avg unemployment for low risk category
lowCrimeUnemployed=groupByRisk.loc['LowCrime']

#print results to user
print(f"Average unemployment rate for HighCrime: {highCrimeUnemployed}\nAverage unemployment rate for LowCrime: {lowCrimeUnemployed}")