# Q: Print the string in the normal order.
# s = "Hello"
# for i in range(len(s)):
#     print(s[i])



#Q: Print a string with the sign ‘-’ in between the characters.
# s = str(input("Enter a string: "))
# for i in range(len(s)):
#     print(s[i], end = "-")



#Q: Print the string in reverse order.
# s = str(input("Enter a string: "))
# for i in range(len(s)-1,-1,-1):
#     print(s[i])




#Q: Check whether a string is palindrome or not
# s = str(input("Enter a string: "))
# r = ""
# for i in range(len(s)-1,-1,-1):
#     r += s[i]
# if s == r:
#     print("Yes, the string is Palindrome")
# else:
#     print("No, the string is not plaindrome")


#Q: Take a string as input and print the numbers of uppercase, lowercase characters, digits and alphabets in it.
# Also print the number of spaces and special characters in it.
# s = str(input("Enter a string: "))
# upper_count = 0
# lower_count = 0
# digit_count = 0
# alpha_count = 0
# space_count = 0
# spl_char_count = 0
# for i in s:
#     if i.isupper():
#         upper_count += 1
#     elif i.islower():
#         lower_count += 1
#     elif i.isdigit():
#         digit_count += 1
#     elif i == " ":
#         space_count += 1
#     else:
#         spl_char_count += 1
#     if i.isalpha():
#         alpha_count += 1
# print("Number of uppercase characters: ",upper_count) 
# print("Number of lowercase characters: ",lower_count)
# print("Number of digit: ",digit_count)
# print("Number of alphabet: ",alpha_count)
# print("Number of spaces: ",space_count)
# print("Number of special characters: ",spl_char_count)


#Q:  Display the length of the longest substring having only consonants
# s = input()
# count = 0
# for i in range(len(s)):
#     if s[i] in "aeiou":
#         m = 0
#         m = max(m,count)
#         count = 0
#     else:
#         count += 1
#         m= max(m,count)
# print(m)



#Q: Display the number of the substrings having only consonants.
# s = input()
# count = 0
# for i in range(len(s)):
#     if s[i] in "aeiou":
#         count = 0
#     else:
#         count += 1
# print(count) 