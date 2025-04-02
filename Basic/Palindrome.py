name = "madam"

# enumerate is return the index , char and reversed its used for reverse the string
for index, char in enumerate(name):
    print(char)

print()
for index, char in enumerate(reversed(name)):
    print(char)

print()
ss = "ajith"
for i in range(len(ss) - 1, 0, -1):
    print(ss[i])
