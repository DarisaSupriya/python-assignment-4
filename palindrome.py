def isPalindrome(word):
    if len(word)<1:
        return True
    else:
        if word[0]==word[-1]:
            return isPalindrome(word[i:-1])
        else:
            return False

def fileInput(filename):
    palindromes=False
    fh=open(filename,"r")
    length=input("enter length of palindromes:")
    d=int(length)
    try:
        for line in fh:
            for s in str(len(line)):
                if ispalindrome(line.strip()):
                    palindromes=true
                    if(len(line.strip())==d):
                        print(line.strip())
    except:
        print("no palindromes found for length eneterd.")
    finally:
            fh.close()
