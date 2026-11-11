my_list = [1,2,4,4,1,4,4,2,6,2,9]
#I use a new list to keep the numbers without repats
new_list =[]
for number in my_list:
    if number not in new_list:
        new_list.append(number)

my_list = new_list

print("The list with unique elements only:")
print(my_list)
        
