import copy

my_list = ["joomla", "Android", "Python", "joomala"]
print("The List  is", my_list)
print("The count of a variable 'joomla is", my_list.count("joomla"))
my_list.sort()
print("After sort my list is", my_list)
my_list.reverse()
print("after reverse my list is", my_list)
my_list.append("ERP")
print("After append my list is", my_list)
list2 = ["MIS", "JaVA"]
my_list.extend(list2)
print("Print list two time", (list2) * 2)
print("after insert new element", my_list)
my_list.pop(2)
print("after popped my list is", my_list)
list2.insert(3, "PHP")
print("after inserting in second list", list2)
a = len(my_list)
print("Length of my list", a)
a = max(my_list)
print("Maximum of list", a)
a = min(my_list)
print("Minimum of list", a)
print("index of a list", my_list.index("joomla"))
print("List by range", my_list[::-1])
print("print sorted", sorted(my_list))
my_list.sort(reverse=0)
print("list sort by true A-Z", my_list)
print("print sorted", sorted(my_list))
print("print list", list(my_list))
list2 = ["MIS", "JaVA"]
# print ("compare list",cmp(my_list,list2))
shop = [1, 2]
shop1 = copy.copy(shop)
print("after copying", shop1)
shop1.append(4)
print("after append", shop1)
print("after append", shop)
mylist1 = copy.deepcopy(my_list)
print("deep copy", mylist1)
print("soft copy", my_list)
mylist1.append("core")
print(mylist1)
print(my_list)
list4 = [2, 4, 2, 2]
print("total sum is", sum(list4))


# del list2
