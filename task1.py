def chop(lst):
    if len(lst) >= 2:
        del lst[0]
        del lst[-1]
        return None
    else:
        lst.clear()

def middle(lst):
    if len(lst) >= 2:
        return lst[1:-1]
    else:
        return []

my_list = [1, 2, 3, 4]
print("My list before call chop function:", my_list)

chop(my_list)
print("My list after call chop function:", my_list)  

my_list = [1, 2, 3, 4]  
print("\nMy list before call middle function:", my_list)

new_list = middle(my_list)
print("My list after call middle funtion:",my_list)
print("New list after call middle function:", new_list)  
