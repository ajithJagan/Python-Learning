from traceback import print_tb

name = "madam"

# enumerate is return the index , char and reversed It's used for reverse the string
for index, char in enumerate(name):
    print(char)

print()
for index, char in enumerate(reversed(name)):
    print(char)

print()
ss = "maam"
for i in range(len(ss) - 1, 0, -1):
    print(ss[i])

new_string=[]

for i in range(len(ss)-1,0,-1):
    new_string.append(ss[i])

# ''.join means its join the list or any collection if we used that
final_string=''.join(new_string)
print(final_string)

if ss == final_string:
    print("It is palindrome")
else :
    print("It is not a palindrome")

# word[0:-1] first index to last index


word="akildz"

# word[::-1] last index to first index
reverse_name=word[::-1]
print()

if word == reverse_name:
    print("It is palindrome")
else :
    print("It is not a palindrome")

# word[1:-2] second index to last second index
last=word[1:-1]
print(last)