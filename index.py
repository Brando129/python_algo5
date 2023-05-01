# Create a function that takes a users list and set value and pushes the greater
# list values into a new list, as well as keeping count of how many items in
# the users list are greater than the set value

def greater_than(list, value):
    new_list = []
    count = 0

    for i in range(0,len(list)):
        if (list[i] > value):
            new_list.append(list[i])
            count += 1
    print(f"The count is {count}")
    return new_list

print(greater_than([2, 5, 7, 9, 10], 5))
