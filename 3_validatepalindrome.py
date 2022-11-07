# validate palindrome words in python
# ex: mom, dad
# a man, a plan, a canal, panama

def ispalindrome(x):
    x=x.lower()
    text = ""
    for i in range(len(x)):
        if x[i].isalnum():
            text=text + x[i]
    return text == text[::-1]
print(ispalindrome("a man, a plan, a canal: panama")) 