forbidden = ('!', '?', '.', '...', '"', ' ')
running = True
letter = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z')

while running:
    # Program to check if a string is palindrome or not
    my_str = input('Enter Text: ')

    # make it suitable for case-less comparison
    my_str = my_str.casefold()

    final_str = []

    # make it suitable for comparison without the contents of forbidden
    for letter in my_str:
        final_str.append(letter)

    # reverse the string
    rev_str = reversed(final_str)

    # check if the string is equal to its reverse
    if list(final_str) == list(rev_str):
        print("Yes, this is a palindrome.")
    else:
        print("No, this is not a palindrome.")

    del final_str
