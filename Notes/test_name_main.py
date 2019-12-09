'''
1 before python runs any code it sets special variables,
1 directly it sets __name__ to main.
print(f'Original file: {__name__}')
'''

if __name__ == "__main__":
    print(f'Original file:{__name__}')
else:
    print(f'not in main')