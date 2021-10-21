# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
import re
p= input("Input your string")
x = True
while x:  
    if (len(p)<8):
        break
    elif not re.search("[a-z]-[abc]&[qwerty]",p):
        break
    elif not re.search("[0-9]-[123]",p):
        break
    elif not re.search("[A-Z]-[ABC]&[QWERTY]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("TRUE")
        x=False
        break
if x:
    print("FALSE")

