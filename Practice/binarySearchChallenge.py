'''
2(challenge). The method that’s usually used to look up an entry in a phone book is not
exactly the same as a binary search because, when using a phone book, you don’t always go
to the midpoint of the sublist being searched. Instead, you estimate the position of the
target based on the alphabetical position of the first letter of the person’s last name.
For example, when you are looking up a number for “Smith,” you look toward the middle of
the second half of the phone book first, instead of in the middle of the entire book.
Suggest a modification of the binary search algorithm that emulates this strategy for a
list of names. Is its computational complexity any better than that of the standard
binary search?
'''

import string

def dict_generator():
    alpha = {}
    num = 0
    for i in list(string.ascii_lowercase):
        alpha[i] = num
        num += 1
    return alpha

def phone_book_lookup(dict,phone_book):
    name = input("Enter the name of the user you would like to search: ")
    first_letter = dict[name[0].lower()]
    if first_letter < 9:
        for key in phone_book.keys():
            key_num = dict[key[0]]
            if first_letter <= key_num:
                for key in phone_book.keys():
                    if name.lower() == key.lower():
                        return f'{name}:{phone_book[key]}'
    elif first_letter > 18 and first_letter < 26:
        for key in list(reversed(phone_book.keys())):
            key_num = dict[key[0]]
            if first_letter <= key_num:
                for key in phone_book.keys():
                    if name.lower() == key.lower():
                        return f'{name}:{phone_book[key]}'
    else:
        phone_keys = list(phone_book.keys())
        print(phone_keys)
        right = len(list(phone_keys))
        left = 0
        while left <= right:
            midpoint = (left + right) // 2
            if name == phone_keys[midpoint]:
                return f'{name}:{phone_book[name.lower()]}'
            elif first_letter < dict[phone_keys[midpoint][0]]:
                right = midpoint - 1
            else:
                left = midpoint + 1


phone_book = {
    'aaron':'555-0001',
    'carson':'555-0002',
    'frank':'555-0003',
    'juliet':'555-0004',
    'pratt':'555-0005',
    'perry':'555-0010',
    'reuben':'555-0006',
    'tim':'555-0007',
    'victor':'555-0008'
}

print(phone_book_lookup(dict_generator(),phone_book))