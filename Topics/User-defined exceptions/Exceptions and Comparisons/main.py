try:
    word = input("Enter a word: ")
    message = "'cat' is a wrong word!"
    assert word != "cat", message
    print("Your word is", word)
except AssertionError as err:
    print(err)  # if the word is 'cat', "'cat' is a wrong word!" is printed