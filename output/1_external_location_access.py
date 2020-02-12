import pandas as pd

details = pd.read_csv('employee_details.csv')
df = pd.DataFrame(details, columns = ['EmployeeID','Department', 'Home Latitude','Home Longitude'])
df['Home Latitude']=df['Home Latitude'].apply(str)
df['Home Longitude']=df['Home Longitude'].apply(str)
df['location'] = df['Home Latitude'].str.cat(df['Home Longitude'],sep="_")

location = pd.read_csv('office_locations.csv')
loc = pd.DataFrame(location, columns = ['Location','Latitude','Longitude'])
loc['Latitude']=loc.Latitude.apply(str)
loc['Longitude']=loc.Longitude.apply(str)
loc['location'] = loc['Latitude'].str.cat(loc['Longitude'],sep="_")

data =pd.read_csv('datalog.csv')
logdata =pd.DataFrame(data, columns = ['EmployeeID','Datetime','Action','Latitude','Longitude','Result','location'])
logdata['Latitude']=logdata.Latitude.apply(str)
logdata['Longitude']=logdata.Longitude.apply(str)
logdata['location'] = logdata['Latitude'].str.cat(logdata['Longitude'],sep="_")
unauthorizedaccess=[]

for index,row in df.iterrows():

    eid=(int(row['EmployeeID']))
    homelocation=row['location']
    x=logdata.loc[(logdata['EmployeeID']==(eid))\
      &((logdata['Action'] == 'access')\
      |(logdata['Action'] == 'login'))]
    filter=     x[((x['location'] !=loc['location'].values[0] )\
             & (x['location'] != loc['location'].values[1])\
             & (x['location'] != loc['location'].values[2])\
             & (x['location'] != loc['location'].values[3])\
             & (x['location'] != homelocation))]

    unauthorizedaccess.append(filter)

newdf = pd.concat(unauthorizedaccess)

newdf.to_csv('question-1-report.csv', encoding='utf-8', index=False)
















