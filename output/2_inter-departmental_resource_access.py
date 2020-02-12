import pandas as pd

details = pd.read_csv('employee_details.csv')
df = pd.DataFrame(details, columns = ['EmployeeID','Department'])

resource = pd.read_csv('dept_resources.csv')
res = pd.DataFrame(resource, columns = ['ResourceID','Department'])


data =pd.read_csv('datalog.csv')
logdata =pd.DataFrame(data, columns = ['EmployeeID','Datetime','Action','ResourceID','Result'])

resourceoutsidedept=pd.DataFrame(columns = ['EmployeeID','Datetime','Action','ResourceID','Result'])
for index,row in df.iterrows():

    eid=(int(row['EmployeeID']))
    deptid=row['Department']
    x=logdata.loc[(logdata['EmployeeID']==(eid))\
      &((logdata['Action'] == 'access') | (logdata['Action'] == 'print'))]
    if not(x.empty):
        for ind,a in x.iterrows():
            r=res.loc[(res['Department']==(deptid))]
            if not(a['ResourceID'] in r.ResourceID.values):
                resourceoutsidedept =resourceoutsidedept.append({'EmployeeID':a.EmployeeID,'Datetime':a.Datetime,'Action':a.Action,'ResourceID':a.ResourceID,'Result':a.Result},ignore_index=True)
                print(a)

resourceoutsidedept.to_csv('question-2-report.csv', encoding='utf-8', index=False)



