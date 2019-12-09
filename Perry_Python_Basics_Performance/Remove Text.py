"""
25/25 points. Great job on this one. 
"""


'''    (Remove text) Write a program that removes all the occurrences of a specified
    string from a text file named pointsOfAuthority.txt. Your program should prompt the user to enter
    a filename and a string to be removed.'''

#This is the main function
def main():
    open_file()

#This function does the magic. It finds the file, removes strings and writes it to a new file
def open_file():
    #This first list is used to enter all the lines from the original file for easy list comprehension later
    new_file_lines = []
    #This next list holds the new lines with the removed string to write to the new file
    new_file = []
    user_file = input("Enter the name of the file you wish to find:")
    user_string = input("Enter the string you wish to remove from the file:")
    file = open(user_file)
    lines = file.readlines()
    #This for loop is just getting all of the lines from the original file
    for i,line in enumerate(lines):
        new_file_lines.append(lines[i])
    #This nested for loop is designed to remove the strings from each line
    for i in new_file_lines:
        i = i.split()
        for j in i:
            if j == user_string:
                i.remove(j)
                #i = ' '.join(i)
        new_file.append(i)
    #This is the new file
    with open('pointsOfAuthorityNew.txt','w') as f:
        for item in new_file:
            f.write(f"{' '.join(item)}\n")
        f.close()
    file = open('pointsOfAuthorityNew.txt')
    print(file.read())




main()