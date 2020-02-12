import pandas as pd
import numpy as np


details = pd.read_csv('employee_details.csv')
df = pd.DataFrame(details, columns = ['EmployeeID'])

data =pd.read_csv('datalog.csv')
logdata =pd.DataFrame(data, columns = ['EmployeeID','Action','ResourceID','Datetime','Result','Latitude','Longitude'])
logdata['Datetime'] = pd.to_datetime(logdata['Datetime'])

activityfromdifferentlocation=pd.DataFrame(columns = ['EmployeeID','Action','ResourceID','Datetime','Result','Latitude','Longitude'])

#x=logdata.loc[(logdata['Result'] == 'failed')]

for index,row in df.iterrows():
    eid=row['EmployeeID']
    r=logdata.loc[(logdata['EmployeeID'] == (eid))]
    p=[]

    for ind,user in r.iterrows():
        t=user['Datetime']

        if (t not in p):
            l=r.loc[(r['Datetime'] == (t))]
            count=l['Datetime'].count()
            if(count>1):
                lat1=np.unique(l[['Latitude', 'Longitude']], axis=0)
                ct=len(lat1)
                if(ct>1):
                    data=l.drop_duplicates(subset=['Latitude','Longitude'],keep='first')
                    print(data)
                    for inde,d in data.iterrows():
                        activityfromdifferentlocation=activityfromdifferentlocation.append({'EmployeeID':d['EmployeeID'],\
                        'Action':d['Action'], 'ResourceID':d['ResourceID'],
                        'Datetime':d['Datetime'],'Result':d['Result'],'Latitude':d['Latitude'],'Longitude':d['Longitude']},ignore_index=True)
                p.append(t)

activityfromdifferentlocation.to_csv('question-6-report.csv', encoding='utf-8', index=False)