'''
1) if-else - single condition - yes/no, even/odd, paas/fail  no need to else sometimes
2) if -else(ladder) - more than one condithion  -  grade,discount,electricity,  only one body execute
3) if -else (nesting) - level wise - authentication, otp , entrance exam
'''
'''#space - indent & it is mendatory
age = int(input("enter age :")) 
if age>=18:
    print("you are eligible")
else:
    print("you are not eligible")
'''

'''
print("main script")   #simple
if True:    #complex
    print("if body")
print("if body")


print("twinkle")
if False: 
    print("yes")
    print("no")
else:
    print("else 1")
    print("else 2")
    '''

    # WAP to determine whether a character is vowel or not
 
''' in c++
ch = input("enter any character")
if ch == 'a' or ch == 'e' or ch== 'i' or ch == 'o' or ch=='u':
    print("it is vowel")
else:
    print("it is not a vowel")'''

'''ch = input("enter any character")
v = "AEIOUaeiou"
if ch in v :
    print("vowel")
else :
    print("it is not vowel")
'''
    #or

ch = input("enter any character")
v = "AEIOUaeiou"
if ch[0] in v :
    print("vowel")
else :
    print("it is not vowel")
