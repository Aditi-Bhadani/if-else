'''
vow=input("Enter a letter ")
if vow=="a" or vow=="e" or vow=="i" or vow=="o" or vow=="u" or vow=="A" or vow=="E" or vow=="I" or vow=="O" or vow=="U":
 print(vow, "is vowel")
else :
    print(vow, "is not vowel")

'''

vow=input("Enter a letter ")
collection="aeiouAEIOU"
if vow in collection:
 print(vow, "is vowel")
else :
    print(vow, "is not vowel")
