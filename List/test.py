import copy

mix_list=['animal', 'bird', 13, 'human', 55.65]
print("Old List :", mix_list)

new_list2=copy.copy(mix_list)
print("New List 2:", new_list2)

new_list2.append("helo")
print("New List 2:", new_list2)
print("Old List :", mix_list)
