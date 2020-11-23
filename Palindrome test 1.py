forbidden = ('!', '?', '.', '...', '"')
running = True
wordList = []
num = int(input())

while running:
        def reverse(num):
            for letter in something:
                if letter != forbidden:
                    add = True
                    # add is used to put the input into a list without the forbidden characters
                if add:
                    add = wordList.append(letter)
                    continue
                elif letter == forbidden:
                    add = False
                return wordList[::-1]
        def is_palindrome(something):
            return wordList == reverse(num)

        something = input("Enter text: ")
        if is_palindrome(something):
            print("Yes, this is a palindrome")
        else:
            print("No, it is not a palindrome")