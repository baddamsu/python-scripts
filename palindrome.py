def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example usage
user_input = input("Enter a word or phrase: ")
if is_palindrome(user_input):
    print("✅ It's a palindrome!")
else:
    print("❌ Not a palindrome.")