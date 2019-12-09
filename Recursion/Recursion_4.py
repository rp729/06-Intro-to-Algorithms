'''
4. Largest List Item
    Design a function that accepts a list as an argument, and returns the largest value in the list.
    The function should use recursion to find the largest item.
'''

'''Main Function'''
def main():
    num_list = [1025,290,673,317,574,5024,599,274,999,785,430,5024]
    largest_num(num_list)

'''Where the magic happens'''
def largest_num(num_list):
    if len(num_list) == 1:
        print(num_list[0])
    else:
        num_find = lambda x,y,num_list : num_list.remove(x) if x <= y else num_list.remove(y)
        num_find(num_list[0],num_list[1],num_list)
        largest_num(num_list)

main()