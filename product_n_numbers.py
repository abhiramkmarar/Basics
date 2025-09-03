char=input("Enter the letter: ")
if char.isalpha():
  if char in 'aeiouAEIOU':
    print(f'{char} is a vowel')
  else:
    print(f'{char} is not a vowel')
else:
 print(f'{char} is not a letter')
  
