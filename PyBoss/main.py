
import pandas as pd
df = pd.read_csv('employee_data1.csv')

us_state_abbrev = {
'Alabama': 'AL',
'Alaska': 'AK',
'Arizona': 'AZ',
'Arkansas': 'AR',
'California': 'CA',
'Colorado': 'CO',
'Connecticut': 'CT',
'Delaware': 'DE',
'Florida': 'FL',
'Georgia': 'GA',
'Hawaii': 'HI',
'Idaho': 'ID',
'Illinois': 'IL',
'Indiana': 'IN',
'Iowa': 'IA',
'Kansas': 'KS',
'Kentucky': 'KY',
'Louisiana': 'LA',
'Maine': 'ME',
'Maryland': 'MD',
'Massachusetts': 'MA',
'Michigan': 'MI',
'Minnesota': 'MN',
'Mississippi': 'MS',
'Missouri': 'MO',
'Montana': 'MT',
'Nebraska': 'NE',
'Nevada': 'NV',
'New Hampshire': 'NH',
'New Jersey': 'NJ',
'New Mexico': 'NM',
'New York': 'NY',
'North Carolina': 'NC',
'North Dakota': 'ND',
'Ohio': 'OH',
'Oklahoma': 'OK',
'Oregon': 'OR',
'Pennsylvania': 'PA',
'Rhode Island': 'RI',
'South Carolina': 'SC',
'South Dakota': 'SD',
'Tennessee': 'TN',
'Texas': 'TX',
'Utah': 'UT',
'Vermont': 'VT',
'Virginia': 'VA',
'Washington': 'WA',
'West Virginia': 'WV',
'Wisconsin': 'WI',
'Wyoming': 'WY',
}

df['First'] = df['Name'].map(lambda x: x.split(" ")[0])
df['Last'] = df['Name'].map(lambda x: x.split(" ")[1])
df['DOB'] = df['DOB'].map(lambda x: x.split("-"))
df['SSN'] = df['SSN'].map(lambda x: x[::-3])
df['SSN'] = '***-**-' + df['SSN']
df['day'] = df['DOB'].map(lambda x: x[2])
df['month'] = df['DOB'].map(lambda x: x[1])
df['year'] = df['DOB'].map(lambda x: x[0])
df['DOB'] = df['month'] + '/' + df['day'] + "/" + df['year']

df["State"] = df["State"].map(us_state_abbrev)
df = df[['Emp ID', 'First', 'Last', 'DOB', 'SSN', 'State']]

print(df)

with open('text_file.txt', 'w') as text_file:
    text_file.write(str(df))
text_file.close()
