forbidden = ('!', '?', '.', '...', '"', ' ')
f = forbidden[::]

running = True

letter = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z')
L = letter

while running:
    # Program to check if a string is palindrome or not
    my_str = input('Enter Text: ')

    # make it suitable for case-less comparison
    my_str = my_str.casefold()

    final_str = []

    # take the letters in my_str and add them to final_str
    for L in my_str[::1]:
        if L != f:
            final_str.append(L)
    else:
        pass
    print(final_str)

    
    # reverse the string
    rev_str = reversed(final_str)

    # check if the string is equal to its reverse
    if list(final_str) == list(rev_str):
        print("Yes, this is a palindrome.")
    else:
        print("No, this is not a palindrome.")

    del final_str
