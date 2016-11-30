# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.

def double_element(element_list):
    try:
        for i in range(len(element_list)):
            element_list[i] *= 2
        return element_list
    except TypeError:
        return 'It isn\'t a list!'

print(double_element([1,2,3,4]))
print(double_element('x'))
