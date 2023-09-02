Newword=''

def Caeser_Cyfer(input_line,input_number):
    global Newword
    for letter in input_line:
        if letter.isalpha():
            letter=(ord(letter)+input_number)
            while letter>122:
                letter=letter-26
            letter=chr(letter)
        if letter.isdigit():
            letter=int(letter)
            letter=letter+int(input_number)
            while letter>9:
                letter=letter-9
        Newword=Newword+str(letter) #16
    return Newword

def Relitive_Cipher(input_var):
    global Newword
    count = 1
    for input_letter in input_var:
        Cyfer = int(count)
        Caeser_Cyfer(input_letter,Cyfer)
        count = count+1
    print(str(Newword))
    return

Relitive_Cipher("abc")
