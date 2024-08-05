import copy

mix_list=['animal', 'bird', 13, 'human', 55.65]
print("Old List :", mix_list)

new_list = copy.deepcopy(mix_list)
print("New List :", new_list)

new_list.append('alien')
print("Old List :", mix_list)
print("New List :", new_list)