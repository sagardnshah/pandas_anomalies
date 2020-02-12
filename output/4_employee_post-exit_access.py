import pandas as pd
from datetime import timedelta
details = pd.read_csv('employee_details.csv')
df = pd.DataFrame(details, columns = ['EmployeeID','Department','End Date'])
df['End Date'] = pd.to_datetime(df['End Date'])

data =pd.read_csv('datalog.csv')
logdata =pd.DataFrame(data, columns = ['EmployeeID','Action','ResourceID','Datetime','Result'])
logdata['Datetime'] = pd.to_datetime(logdata['Datetime'])

activityafterenddate=pd.DataFrame(columns = ['EmployeeID','Action','ResourceID','Resource Access Date','Emp End Date'])

for index,row in df.iterrows():

    eid=(int(row['EmployeeID']))
    enddate=row['End Date']+ timedelta(hours=24)
    tdate=row['End Date']
    x=logdata.loc[(logdata['EmployeeID']==(eid))]
    if not(x.empty):
        for index,emp in x.iterrows():

            accessdatedate = emp['Datetime']
            if(accessdatedate>enddate):
                msg=emp['EmployeeID'],"Accessed ",emp['ResourceID'],"after end date"

                activityafterenddate=activityafterenddate.append({'EmployeeID':emp.EmployeeID,'Action':emp.Action,'ResourceID':emp.ResourceID,'Resource Access Date':accessdatedate,'Emp End Date':tdate},ignore_index=True)
                print(activityafterenddate)

activityafterenddate.to_csv('question-4-report.csv', encoding='utf-8', index=False)
