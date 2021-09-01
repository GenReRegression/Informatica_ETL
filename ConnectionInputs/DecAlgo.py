import os
from binhex import openrsrc
from pathlib import Path


def decrypt(text):
    result = ""
    s = 9  #string length of config.txt file
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):  #returns True if all characters in the string are uppercase,
            # otherwise, returns “False”
            result += chr((ord(char) + (26-s) - 65) % 26 + 65)  # encrypt the plain text
        elif char.isdigit():  #isdigit() method returns “True” if all characters in the string are digits,
            # Otherwise, It returns “False”
            c_new = (int(char) - s) % 10
            result += str(c_new)
        elif (char.islower()):  ##returns True if all characters in the string are lowercase,
            # otherwise, returns “False”
            result += chr((ord(char) + (26-s) - 97) % 26 + 97)  # encrypt the plain text
        else:
            result += char
    return result

def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.isdigit():
            c_new = (int(char) + s) % 10
            result += str(c_new)
        elif (char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    #print(result)
    return result

def generateencfile(filepath):
    inputfile = open(filepath,'r')
    data = inputfile.readlines()
    if not os.path.exists(str(Path(__file__).parent.parent) + "\\TestData\\config.txt"):  # is used to check whether the specified path exists or not
        outputfile = os.mkdir(str(Path(__file__).parent.parent) + "\\TestData\\config.txt")
    otfile = open(outputfile,'w')
    for i in range(data.__len__()):
        datatoenc = data[i].split('-')
        servername = datatoenc[0]
        username = datatoenc[1]
        password = datatoenc[2]
        finaluser = encrypt(username, 9)
        finalpassword = encrypt(password, 9)
        datawriteinfile = servername+'-'+finaluser+'-'+finalpassword
        otfile.write(datawriteinfile)
        otfile.close()
        print(datawriteinfile)
    inputfile.close()
    #os.rmdir(filepath)

def main():
    #encrypt("kNOCKout#46",9)
    generateencfile("C:\\Users\\kpawar\\PycharmProjects\\ETLValidationInformatica\\TestData\\tt.txt")

if __name__ == "__main__":
    main()