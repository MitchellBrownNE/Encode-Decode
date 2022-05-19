import string

### Main function ###
def main():
   
    ### Greeting ###
    print ("Hello, this program will allow you to translate english to morse code and vise versa!")

    ### Menu with choice ###
    print("Please enter one of the options below.\n")
    Menu()
    Choice = int(input("Please enter an option: "))
    
    ### While loop for encode, decode, and exit ###
    while Choice:
        if Choice == 1:
            EnglishText = (input("\nPlease enter english text below:\n"))
            print(Encode(EnglishText))

        elif Choice == 2:
            MorseText = (input("\nPlease enter morse code with spaces between each code and | between each word below:\n"))
            print(Decode(MorseText))
    
        elif Choice == 3:
            print ("\nProgram terminated!")
            break

        ### After function choice ###
        Menu()
        Choice = int(input("Please enter an option: "))



### Encode dictionary fucntion ###
def EncodeDict():
    EncodeDict = {}
    EncodeTxt = open("Encode.txt", "r")

    for line in EncodeTxt:
        line = line.split()
        EncodeDict[line[0]] = line[1]
    
    return (EncodeDict)
### Decode dictionary function ###
def DecodeDict():
    DecodeDict = {}
    DecodeTxt = open("Decode.txt", "r")

    for line in DecodeTxt:
        line = line.split()
        DecodeDict[line[0]] = line[1]
    
    return (DecodeDict)



### Menu function for choice ###
def Menu():
    print ("\nEnter 1 to encode your text.")
    print ("Enter 2 to decode your text.")
    print ("Enter 3 exit program.")



### Function to encode English to morse code ###
def Encode(Message):
    MorseCode = []
    EDict = EncodeDict()
    EDict[" "] = "|"

    for char in Message.upper():
        if char in EDict:
           MorseCode.append(EDict[char]) 

    Morse = " ".join(MorseCode)

    return Morse
### Function to decode morse code into English ###
def Decode(Message):
    Message = Message.split()
    EnglishText = []
    DDict = DecodeDict()
    DDict["|"] = " "

    for char in Message:
        if char in DDict:
            EnglishText.append(DDict[char])

    English = "".join(EnglishText)

    return English



### Calling main() function ###
main()