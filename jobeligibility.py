degree=input("enter the degree:")
skills=input("enter the skills:")
age=float(input("enter the age:"))
experience=float(input("enter the experience:"))
if(skills=="ai stack" and experience>=5):
    enter_salary_expectations=float(input("enter the amount:"))
    estimated_salary=enter_salary_expectations*1.5
    print("the base salary package is:",estimated_salary)
elif(skills=="devops and cloud computing" and experience>=8 ):
    print("you are eligible for the devops manager role")
    input_salary=float(input("enter the salary expectations:"))
    net_estimated_salary=input_salary*3.5
    print("the net package offered for your role is:",net_estimated_salary)
elif(skills=="java web developer" and experience==0):
    print("you are eligible for trainee role")
    cgpa=float(input("enter the cgpa:"))
    salary=cgpa*1500
    print("the salary amount is :",salary)
elif(skills=="cybersecurity and cloud computing" and experience>=7):
    rating=float(input("enter the rating:"))
    if(rating>=7):
        print("you are eligible for cybersecurity role")
    else:
        print("you are not elegible for this role")
elif(degree=="bca" or degree=="bba"):
    print("you are cooked")
else:
    print("you are not eligible")
    
    
    
    
    