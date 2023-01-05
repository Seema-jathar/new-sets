frist_name =input("Please enter the frist name\n")
last_name=input("Please enter the last name\n")
frist_name = frist_name.capitalize()
last_name = last_name.capitalize()
full_name = frist_name + last_name
len_full_name = len(full_name)
print(full_name[-len_full_name:-len(last_name)],full_name[-len(last_name):])

