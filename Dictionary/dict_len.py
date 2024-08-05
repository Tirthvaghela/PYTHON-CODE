import copy

sales2 = {"carrot": 5}
emp = {"empid": 1, "empname": "Rahul", "desi": "Manager", "dept": "sales"}
print("Length of emp dict :", len(emp))
newemp = emp.copy()
print("New emp dict", newemp)
newemp.clear()
print("Original emp dict", emp)
print("New emp dict", newemp)
