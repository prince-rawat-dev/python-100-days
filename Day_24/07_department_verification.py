company_employees = {"prince","sagar","alok","kishan","angad","bajrangi","ram","keshav","rohit","divyanshu"}
IT_department = {"alok","prince","sagar","kishan"}

print(f"\nCompany Employees: {company_employees}\nIT department Employees: {IT_department}")
print(f"\n(Company Employees) is a superset of (IT department employees): {company_employees.issuperset(IT_department)}\n")