import os
import sys

print("\n\n Generic Try Catch\n\n")
try:
    print(x)
except:
    print("There was an exception caught")

print("\n\n Generic Try Finally\n\n")

try:
    print(0/0)
except ValueError:
    print("There was an ValueError caught")
except NameError:
    print("There was an NameError caught")
except Exception as e:
    print(e)
finally:
    print("All done")
