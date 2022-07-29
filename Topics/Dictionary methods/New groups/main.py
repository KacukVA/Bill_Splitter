# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
# your code here
input_groups = int(input())
groups_dict = dict().fromkeys(groups)
i = 0
for group in groups_dict:
    if i < input_groups:
        groups_dict[group] = int(input())
        i += 1
    else:
        break
print(groups_dict)
