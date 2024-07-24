
print("Enter 1 for Employee Details ")
print("Enter 2 for pyramid ")
print("Enter 3 for Dictionary ")
choice=int(input('Enter a choice between (1-3) : '))

if choice == 1:
	Employee_det=[];
	Employee_id=input('Enter a id :  ');
	Employee_name=(input('Enter a name :  '));
	Employee_salay=float(input('Enter a salay :  '));
	Employee_Des=input('Enter a Designation : ');
	emp_hra=0;
	emp_Medicliam=0;

	if Employee_salay > 80000:
		emp_hra=Employee_salay*1.1;
		emp_Medicliam=Employee_salay*1.15;

	elif Employee_salay >  50000:
		emp_hra=Employee_salay*0.7;
		emp_Medicliam=Employee_salay*1.12;

	elif Employee_salay >  30000:
		emp_hra=Employee_salay*1.05;
		emp_Medicliam=Employee_salay*1.1;

	Employee_det=[Employee_id,Employee_name,Employee_salay,Employee_Des];
	print(f'name is :',{Employee_det[1]})
	print(f'Designation is :',{Employee_det[3]})


elif choice== 2:

	n=int(input('Enter starting range : '))
	b=int(input('Enter starting range : '))
	for i in range(n,b+1):
		for j in range(b+1):
			if j < i :
				print("*",end=" ")
		print(" ")
				
	print("Complate")

elif choice== 3:
	student_det={'name':'Tirth','Roll_no':113,'contact':123456788,'Email':'tirth@gmail.com'}
	print('Roll_no' in student_det)
	print(student_det)






