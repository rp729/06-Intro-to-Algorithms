'''
3. At what point does an n^4 algorithm begin to perform better than a 2^n algorithm?

As n gets larger, n^4 will perform far better than 2^n due to complexity. When n > 17 is when 2^n becomes more complex
'''

n = 2

while n**4 >= 2**n:
    print(f'num:{n}: {n**4},{2**n}')
    n += 1