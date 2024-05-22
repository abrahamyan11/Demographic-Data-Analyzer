import pandas as pd

df = pd.read_csv('demographic_data.csv')

race_counts = df['race'].value_counts()

average_age_men = df[df['sex'] == 'Male']['age'].mean()

bachelors_percentage = (df['education'] == 'Bachelors').mean() * 100

higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
higher_education_rich = (higher_education['salary'] == '>50K').mean() * 100

lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
lower_education_rich = (lower_education['salary'] == '>50K').mean() * 100

min_hours_per_week = df['hours-per-week'].min()

num_min_workers = df[df['hours-per-week'] == min_hours_per_week]
rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100

country_counts = df['native-country'].value_counts()
rich_countries = df[df['salary'] == '>50K']['native-country'].value_counts() / country_counts * 100
highest_earning_country = rich_countries.idxmax()
highest_earning_country_percentage = round(rich_countries.max(), 1)

top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()
