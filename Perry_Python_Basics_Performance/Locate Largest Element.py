
"""
25/25 points. Well Done
"""

'''
    (Locate the largest element) Write the following function that returns the location
    of the largest element in a two-dimensional list:


    def locateLargest(a):
        The return value is a one-dimensional list that contains two elements. These
        two elements indicate the row and column indexes of the largest element in the
        two-dimensional list. Write a test program that prompts the user to enter a
        two-dimensional list and displays the location of the largest element in the list.


    Here is a sample run(You don't have to mimic this, this is just a guide):

        Enter the number of rows in the list: 3
        Enter a row: 23.5  35  2    10
        Enter a row: 4.5   3   45   3.5
        Enter a row: 35    44  5.5  11.6
        The location of the largest element is at (1,2)
'''

'''Main Function'''
def main():
    num_find()

#This function is the main engine of the program. Prompts user input and finds location of largest number
def num_find():
    #This list will hold the numbers entered for each row
    main_row_list = []
    #Dictionary to hold all of the data
    max_num = {
        'largest':0,
        'row':0,
        'column':0
    }
    #Enter the number of rows you would like to enter
    rows = input('Enter the number of rows in the list:')
    rows = input_validation(rows)
    #Creates a list for each row held in main_row_list
    for i in range(rows):
        main_row_list.append([])
    #Get user input for each row
    for i in main_row_list:
        row_input = input(f'Enter a row ({main_row_list.index(i)+1} of {rows}): ')
        row_input = row_input.split()
        for num in row_input:
            num = row_validation(num)
            i.append(num)
    #This for loop will find the location of the largest number
    for row in main_row_list:
        if max(row) > max_num['largest']:
            max_num['largest'] = max(row)
            max_num['row'] = row.index(max(row))
            max_num['column'] = main_row_list.index(row)
    print(f'The location of the largest element is at ({max_num["column"]},{max_num["row"]})')

#Simple integer validation for input
def input_validation(num):
    while str.isdigit(num) == False:
        num = input("INVALID INPUT! Must be a number : ")
    num = int(num)
    return num

#Simple float validation for input
def row_validation(num):
    is_float = False
    while is_float == False:
        try:
            float(num)
            is_float = True
        except:
            num = input(f'{num} is not a number. Please enter a number in place of {num}: ')
            is_float = False
    return float(num)

#Run the main function
main()
