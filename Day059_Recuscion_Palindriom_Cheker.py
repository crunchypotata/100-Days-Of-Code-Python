print("🌟Palindrome Checker🌟")
print()

word = input("Input a word: ").strip().lower()

def palindrome(word):
  if len(word) <= 1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1])
  
print(palindrome(word))    

