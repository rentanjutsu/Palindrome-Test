forbidden = ('!', '?', '.', '...', '"')
running = True
final_str = []

while running:
    # Program to check if a string is palindrome or not
    my_str = input('Enter Text: ')

    # make it suitable for case-less comparison
    my_str = my_str.casefold()

    # make it suitable for comparison without the contents of forbidden
    for int in my_str:
        if int != forbidden:
            final_str.append(int)

    # reverse the string
    rev_str = reversed(final_str)

    # check if the string is equal to its reverse
    if list(final_str) == list(rev_str):
        print("Yes, this is a palindrome.")
    else:
        print("No, this is not a palindrome.")
