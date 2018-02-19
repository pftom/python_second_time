message = input('Tell me something, and I will repeat it back to you：')
print(message)

cnt = 0
for cnt in range(1, 5):
    value = input("Input it: ")
    if int(value) == 3:
        break
    print(value)
