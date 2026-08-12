# text = input("enter a statement: ")
# banned_word = input("Enter the banned word: ")

# def censor_words(text, banned_word):
#     arr = text.split(" ")
    
#     for i, ar in enumerate(arr):
#         if ar == banned_word:
#             arr[i] = "***"
#     return " ".join(arr)


# print(censor_words(text, banned_word))


# # Get inputs from the user
# text = input("Enter a statement: ")
# banned_word = input("Enter the word to ban: ")

# def censor_words(text, banned_word):
#     # Split the statement into a list of words
#     arr = text.split(" ")
    
#     # Loop through the words and check for matches
#     for i, ar in enumerate(arr):
#         if ar.lower() == banned_word.lower(): # Case-insensitive check
#             arr[i] = "***"
            
#     # Rejoin the words back into a sentence
#     return " ".join(arr)

# print(censor_words(text, banned_word))
def censor_words(text, banned_word):
    rep = text.replace(banned_word, "***")
    return rep