class Employee:
    def __init__(self):
        self.emp_id=input('Employee id=')
        self.emp_name=input('Employee name=')
        self.emp_salary=float(input('Employee salary='))
        self.emp_dept=input('Employee department=')
    def calculate_emp_salary(self):
        hours_worked=int(input('Enter no. of hours worked:'))
        if hours_worked>50:
            overtime=hours_worked-50
            over_amount=(overtime*(self.emp_salary/50))
            self.emp_salary+=over_amount
            print('salary=',self.emp_salary)
        else:
            print('salary=',self.emp_salary)
    '''def emp_assign_dept:
        if emp_dept!='Accounting':'''
    def emp_details(self):
        print(self.emp_name,self.emp_id,self.emp_salary,self.emp_dept)

emp=Employee()
emp.calculate_emp_salary()
emp.emp_details()
