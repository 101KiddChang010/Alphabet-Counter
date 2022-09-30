import string

#returns all lowercase letters
def lowerAlphabet(): 
    return string.ascii_lowercase

#returning the list
def arrayAlphabet(a): 
    return list(a)

#algorithm to read letters
def readLetters(d):
    lengDict = len(d)
    lower = lowerAlphabet()

    inc = {}

    for letter in lower:
        inc[letter] = 0

    for x in range(lengDict):
        for letter in d[x]:
            for low in lower:
                if letter == low:
                    inc[letter] += 1 
                else:
                    pass

    return inc

#prints alphabet counter
def histogram(d):
    print("letter    count")
    
    letter = arrayAlphabet(lowerAlphabet())
    value = readLetters(d)

    for x in range(26): 
        print("{:10}{}".format(letter[x], value[letter[x]]))

#main function
def main():
    file = input("Enter file name: ")
    f = open(file, "r")

    s = {}
    x = int(0)

    #   splits every word in file into a dictionary
    for line in f:
        L = line.split()
        for key in L:
            s[x] = key.lower()
            x += 1

    histogram(s)

    f.close()

main()    
