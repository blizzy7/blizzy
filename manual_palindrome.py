# Implement manual_palindrome(text). 
# Ignore spaces and letter case. 
# Return true if the cleaned text reads the same forward and backward, otherwise return false. 
# Do not use slicing shorthand or reversed. Students may need to research manual string reversal.



def manual_palindrome(text):
    # Clean the text by removing spaces and converting to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Initialize pointers for the start and end of the cleaned text
    left = 0
    right = len(cleaned_text) - 1
    
    # Compare characters from both ends moving towards the center
    while left < right:
        if cleaned_text[left] != cleaned_text[right]:
            return False
        left += 1
        right -= 1
    
    return True





    def manual_palindrome(text):
        text = text.lower().replace(" ", "")
        clean = ""
        for char in text:
            if char.isalnum():
                clean += char
        reversed_clean = ""
        for char in clean:
            reversed_clean = char + reversed_clean
        return clean == reversed_clean


        def manual_palindrome(text):
    # Step 1: Remove all spaces and convert to lowercase
    text = text.replace(" ", "").lower()

    # Step 2: Create an empty string to store the reversed text
    reversed_text = ""

    # Step 3: Find the last index of the string
    last_index = len(text) - 1

    # Step 4: Loop backwards through the string
    for i in range(last_index, -1, -1):
        reversed_text = reversed_text + text[i]

    # Step 5: Compare the original cleaned text with the reversed text
    if text == reversed_text:
        return True
    else:
        return False