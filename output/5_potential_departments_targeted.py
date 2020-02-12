import pandas as pd
details = pd.read_csv('employee_details.csv')
df = pd.DataFrame(details, columns = ['EmployeeID','Department'])

data =pd.read_csv('datalog.csv')
logdata =pd.DataFrame(data, columns = ['EmployeeID','Action','ResourceID','Datetime','Result'])
logdata['Datetime'] = pd.to_datetime(logdata['Datetime'])

repeatedfailuers=pd.DataFrame(columns = ['EmployeeID','Department','Action','ResourceID','Datetime','Result'])

x=logdata.loc[(logdata['Result'] == 'failed')]

for index,row in df.iterrows():
    eid=row['EmployeeID']
    r=x.loc[(x['EmployeeID'] == (eid))]
    dept=str(row['Department'])
    p=[]

    for ind,user in r.iterrows():
        t=user['Datetime']

        if (t not in p):
            l=r.loc[(r['Datetime'] == (t))]
            if(len(l)>3):
                msg=str(user.EmployeeID)+" has " + str(len(l))+ " Failed attempts at "+str(t)
                for inde, line in l.iterrows():
                    repeatedfailuers=repeatedfailuers.append({'EmployeeID':line['EmployeeID'],'Department':dept, 'Action':line['Action'], 'ResourceID':line['ResourceID'],'Datetime':line['Datetime'],'Result':line['Result']},ignore_index=True)
                    print(l)
            p.append(t)
group = repeatedfailuers.groupby('Department')
group['Result'].count().head()
result = repeatedfailuers.sort_values(['Department'], ascending=[1])
result.to_csv('question-5-report.csv', encoding='utf-8', index=False)


