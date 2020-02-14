# generate random integer values
from random import seed
from random import randint
# seed random number generator
# generate some integers
def randomString():
    string = ''
    for _ in range(10):
        value = randint(97, 122)
        string = string+chr(value)
    return string

def randomInt():
    value = randint(1, 42)
    return value

def createFile(string):
    string = string+'\n'
    f= open(files,"w+")
    f.write(string)
    f.close()

if __name__ == "__main__": 
    fileNames = ["myFile1", "myFile2", "myFile3"]
    for files in fileNames:
        string = randomString()
        createFile(string)
        print(string)
    num1 = randomInt()
    num2 = randomInt()
    print(num1)
    print(num2)
    print(num1*num2)