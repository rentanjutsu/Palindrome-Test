forbidden = ('!', '?', '.', '...', '"')
running = True
final_str = []


while running:
    # Program to check if a string is palindrome or not

    my_str = input('Enter Text: ')

    # make it suitable for caseless comparison
    my_str = my_str.casefold()

    # make it suitable for comparison without the contents of forbidden
    f = forbidden
    for f in my_str:
        if f != forbidden:
            final_str.append(f)

    # reverse the string
    rev_str = reversed(final_str)

    # check if the string is equal to its reverse
    if list(final_str) == list(rev_str):
        print("Yes, this is a palindrome.")
    else:
        print("No, this is not a palindrome.")
