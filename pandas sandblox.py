# import pandas as pd
# list_teams =['49ers','KC','Cowboys','Steelers']

# print (type(list_teams))

# print(list_teams)

# series_teams = pandas.series(list_teams)

# print(series_teams)

# print(type(series_teams))

students = {'Hawai':'Isabella','Ohio':'Davir','Iowa':'Robert'}
print(type(students))
print(students)

student_series = pd.series(index=students.keys(),data=students.values())

print(type(student_series))
print(student_series)
