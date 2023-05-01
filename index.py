# Create a function that takes a users array and set value and pushes the greater
# values into a new array, as well as keeps count of how many items in
# the array are greater than the set value

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