'''Here the function welcome() use to print the message which is wriiten inside the function.'''
'''the backslash(\) which is an escape character and n represent a newline.'''
'''#Simply, \n used to start the text on a new line.'''

def welcome():
    print("Welcome to the Caeser Cipher\nThis program encrypts and decrypts text with the Caeser Cipher")

'''The function which i named choose_mode is used to select the choices wheater users wants to encrypt(e) or decrypts(d)'''
'''here user enters their choice 'e' for encryption and 'd' for decryption.'''
'''when user enters another alphapets except 'e' and 'd' else statement will be execute.'''
'''.lower() used to ensure that both upper and lower case inputs are accepted.'''
'''while True ensures that user can repedeatly enters the values until they provide a valid input'''
def choose_mode():
    while True:
        choose_choice=input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if choose_choice=='e':
            return 'e'
        elif choose_choice=='d':
            return 'd'
        else:
            print("Invalid Mode")
            
'''The enter_message function is used to take input from user and check the condition according to their choice wheather they want to encrypt or decrypt.'''
'''select_mode is a variable which stores user's choice encrypt or decrypt'''
'''user's choice determine by calling the function choose_mode.'''
'''here input(message) is conveted to uppercase to avoid mixing of upper and lowercase letters)'''
def enter_message():
    select_mode=choose_mode()
    message = input("What message would you like to encrypt or decrypt: ")
    return message.upper(),select_mode

'''The shift_value function used to take input from users to get the shift numbers(how many positions they want to shift)for the encrypt and decrypt process.'''
'''.isnumeric function check wheather the user enter numeric(digit)or not.'''
'''if the input is numeric,the function convert input to an integer using int(shift_choice)'''
def shift_value():
    while True:
        shift_choice=input("What is the shift number ?: ")
        if shift_choice.isnumeric():
            return int(shift_choice)
        else:
            print("Invalid Shift")

''' this is the repeat function to ask if the user wants to continue with another message or not'''
'''if user choose y than the program will be continue and they can encrypt or decrypt contineously'''
'''if user choose n than program will stop and display thans for using the program goodbye'''

def repeat():
    while True:
        continue_choice = input("Would you like to encrypt or decrypt another message ? (y/n): ").lower()
        if continue_choice == 'y':
            return True
        elif continue_choice == 'n':
            return False
        else:
            print("please enter 'y' for yes or 'n' for no.")

'''the encrypt function uses for encrypting a message using the ceasar cipher.'''
'''shift_choice use to shift the each character that user enters(which is stores in message variable)'''
'''initializing ceaser_text an empty string to store encrypted message.'''
'''for loop (for char in choose_choice)iterates over each character of the variable message.'''
'''asc =ord(char.upper()) converts the character to ASCII value (in uppercase).'''
'''ord() gives the ASCII value of the given character from user.'''
'''if 64 < asc <91 ensure that only alphabetic characters(A-Z) are encrypted.'''
'''a_asc =asc + shift_choice shifts the ASCII value of the character by shift_choice.'''
''' a_asc -= 26 means if the shifted value is Z it start from the beginning of the alphabet.'''
'''ceaser_text=ceaser_text + chr(a_asc) appends the newly shifted character.'''
'''(x+n)%26'''
def encrypt(message,shift_choice):
    ceaser_text=""
    for char in message:
        asc=ord(char.upper())
        if 64 < asc < 91:
            a_asc = asc + shift_choice
            if a_asc > 90:
                a_asc -= 26
        else:
            a_asc = asc
        ceaser_text = ceaser_text + chr(a_asc)
    return ceaser_text
'''the decrypt function is decrypt a message that was encrypted using the ceaser cipher.it has text and shift value to store the encryption.'''
'''same as encrypt(condition) it will works to decrypt the ceaser cipher text.'''
'''(ceaser_txt-n)%26'''
'''ord(char.upper()) converts the character to its ASCII value (in uppercase).'''
'''64 < asc < 91 (condition check if the character ASCII value is between 65 and 90 which are'A' to 'Z'.'''
'''asc-shift (shift the character backwards by the given shift)'''
def decrypt(text,shift):
     ceaser_text = ""
     for char in text:
         asc= ord(char.upper())
         if 64 < asc < 91:
            a_asc = asc - shift
            if a_asc < 65:
                a_asc += 26
         else:
            a_asc = asc
         ceaser_text = ceaser_text + chr(a_asc)
     return ceaser_text

'''is_file is the function to check if a given file exist or not'''
'''the function has take a signle argument called filename'''
'''the open function open the file (which we created in notpad) in read mood'''
''' if the file open successfully then we know if exist and return true'''
'''if file not exist it return false (file not found)'''

def is_file(filename):
    try:
        with open(filename,'r'):
            return True
    except FileNotFoundError:
        return False

'''process_file () is simply used to process the file to read users encrypt or decrypt'''
'''file name is the name to process the file'''
'''mode simply use to select either user want encrypt or decrypt'''
'''shift use to adjust the shifthing number for encryption and decryption'''
'''here empty list messages created to store our further imformation after encryption and decryption'''
'''try use to open the file in read mood'''
'''if file not found it will raised file not found error and handled  in except'''
'''line.strip removes all spaces from the line'''
'''encrypt and decrypt calls the respective function that we created '''
'''here i pass shift as an argument to specify the transfer imformation'''
'''and all processed line is appended to the empty list messages'''

def process_file(filename,mode,shift):
    messages=[]
    try:
        with open(filename,'r')as file:
            for line in file:
                if mode=='e':
                    messages.append(encrypt(line.strip().upper(),shift))
                elif mode=='d':
                    messages.append(decrypt(line.strip().upper(),shift))
    except FileNotFoundError:
        print("Invalid Filename")
    return messages

'''function to write the results from the input file (messages.txt)'''
'''opens a file named results.txt in write mode 'w'''
'''/n helps to write each each message on a new line in results.txt which is our output file'''


def write_messages(messages):
    with open('results.txt','w')as file:
        for message in messages:
            file.write(message+'\n')

'''this is the choice function wheather user choose to print in console or in file'''
'''source determine wheather the input is provided through file or directly from the console'''
'''message or filename depending upon chosen sources either reads from console(c) or specifies a file to read'''

def message_or_file():
    shift=None
    message =None
    while True:
        mode=input("Would you like to encrypt (e) or decrypt(d):").lower()
        if mode=='e' or mode == 'd':
            break
        else:
            print("Invalid Mode")
    while True:
        source=input("Would you like to read from a file(f) or the console(c)?").lower()
        if source=='f' or source =='c':
            break
        else:
            print("Invalid Input")
            
    filename=None
    if source=="f":
        while True:
            filename=input("Enter filename:")
            if is_file(filename):
                break
            else:
                print("Invalid Filename")
        while True:
            shift_input=input("What is the shift number:")
            if shift_input.isnumeric():
                shift=int(shift_input)
                break
            else:
                print("Invalid Shift")
                
    elif source=='c':
            message=input(f"What message would you like to {mode}:").upper()
            while True:
                shift_input =input("What is the shift number:")
                if shift_input.isnumeric():
                    shift=int(shift_input)
                    break
                else:
                    print("Invalid Shift")
                    
    return mode,message,filename,shift
'''this is the main function to execute our whole ceaser cipher program'''
'''displaying a welcome message by calling welcome function'''
'''while true can proccess multiple messages or files without restartinf the program'''
'''the proccess_file function proccess the file with encrypt or decrypt to each line'''
''' the output result saved to a file through write_messages and with print function message will print to the console'''
'''shift() function to ask the user in which number of position they want to shift the letters in the message.'''

def main():
    welcome()
    while True:
        mode,message,filename,shift=message_or_file()
        if filename:
            messages=process_file(filename,mode,shift)
            write_messages(messages)
            print(messages)
        else:
            if mode=='e':
                result=encrypt(message,shift)
            else:
                result=decrypt(message,shift)
            print(result)
        another_message=input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if another_message=='n':
            print("Thanks for using the program,goodbye!")
            break
main()

    
    

            
            
        
        
    

    
    
