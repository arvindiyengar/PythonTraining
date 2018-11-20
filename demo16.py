'''

Looping in Python : While

'''

print("Script Starting...")

x = 1

print("\n\nLooping from 1..9\n\n")
while(x < 10):
    print("X counter : ", x)
    x += 1  # learnt about this in the shortcut assignment


print("\n\nContinue Usage : Will skip the print invocation for 3\n\n")

# Used when we want to jump a certain interation

x = 1
while(x < 10):
    if(x == 3):
        x += 1
        continue
    print("X counter : ", x)
    x += 1  # learnt about this in the shortcut assignment

print("\n\nBreak Usage : Will stop the print Invocation post 2\n\n")

# Used when we want to jump a certain interation

x = 1
while(x < 10):
    if(x == 3):
        break
    print("X counter : ", x)
    x += 1  # learnt about this in the shortcut assignment

print("\n\nScript Executed")
