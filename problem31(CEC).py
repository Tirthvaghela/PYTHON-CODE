while True:
    print("==============================")
    print("Enter 1 for Employee Details ")
    print("Enter 2 for Pyramid ")
    print("Enter 3 for Dictionary ")
    print("Enter -1 to exit")
    print("==============================")

    choice = int(input('Enter a choice between (1-3) or -1 to exit: '))

    if choice == -1:
        
        break

    if choice == 1:
        Employee_det = []
        Employee_id = input('Enter an ID: ')
        Employee_name = input('Enter a name: ')
        Employee_salary = float(input('Enter a salary: '))
        Employee_Des = input('Enter a Designation: ')
        emp_hra = 0
        emp_Mediclaim = 0

        if Employee_salary > 80000:
            emp_hra = Employee_salary * 1.1
            emp_Mediclaim = Employee_salary * 1.15
        elif Employee_salary > 50000:
            emp_hra = Employee_salary * 0.7
            emp_Mediclaim = Employee_salary * 1.12
        elif Employee_salary > 30000:
            emp_hra = Employee_salary * 1.05
            emp_Mediclaim = Employee_salary * 1.1

        Employee_det = [Employee_id, Employee_name, Employee_salary, Employee_Des]
        print("==============================")
        print(f'Name is: {Employee_det[1]}')
        print(f'Designation is: {Employee_det[3]}')
        


    elif choice == 2:
        n = int(input('Enter starting range: '))
        b = int(input('Enter ending range: '))

        for i in range(n, b + 1):
            for j in range(b + 1):
                if j < i:
                    print("*", end=" ")
            print(" ")

        print("Complete")
        


    elif choice == 3:
        student_det = {'name': 'Tirth', 'Roll_no': 113, 'contact': 123456788, 'Email': 'tirth@gmail.com'}
        print('Roll_no' in student_det)
        print(student_det)
        

    else:
        print("Invalid choice. Please enter a choice between 1-3 or -1 to exit.")
