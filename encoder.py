# Joe Goodman
# 02/28/23
# encode passwords and then decode them

# all you have to do is write this function's body.
# Just make sure you return a string and it
# will work with the main funciton.
# password is a string
#
# rn, it just returns a bunch of 1's
# so that the program runs without errors
def decode(password):
    return "11111111"

# crash the program with a custom error message
# msg is a string
# this function returns nothing and will crash the program
def error(msg):
    raise Exception(msg)

# prints the menu plus whitespace, nothing returned
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")

# get input after displaying the menu to the user
# the input should only ever be "1", "2", or "3"
#
# this function returns the input as a number 
# UNLESS
# the input is invalid, in which case the program crashes
def menu_input():
    user_input = int(input("Please enter an option: "))

    # if input is invalid, crash
    if user_input < 1 or user_input > 3:
        error("invalid input!!!")

    return user_input

def main():
    # var to store the encoded password in once the user inputs it
    # it starts as None and then becomes a string
    encoded_password = None

    # main loop
    while True:
        # print the menu
        print_menu()
        
        # get the user input
        user_choice = menu_input()

        # encode
        if user_choice == 1:
            # get the password from the user
            raw_password = input("Please enter your password to encode: ")

            # encode the password and store it
            encoded_password = encode_password(raw_password)

            # print message
            print("Your password has been encoded and stored!")
            print("") # here for formatting

        # decode
        elif user_choice == 2:
            # i am assuming that this will never be called before a password is passed in
            # if that happens, the program crashes
            if encoded_password == None:
                error("cannot decode password: there is no password!")

            # decode the password
            decoded_password = decode(encoded_password)
            
            # print the message
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

        # quit
        elif user_choice == 3:
            return # break would work here too

        else:
            # the program would have crashed if
            # the input were not 1, 2, or 3
            error("unreachable!")

# encode a password by shifting each number up by three.
# 9 wraps back around to 0
#
# password is a string containing ONLY numbers. Ex: "123123" or "57857439"
# This function returns a string.
#
# this function assumes the input is valid and will crash if it's not
def encode_password(password):
    encoded_password = ""

    # loop over every character
    for char in password:
        # convert char to number
        char = int(char)

        # if the char is 7 or greater, adding 3 to it would cause an overflow,
        # (i.e 8's encoding is not 8 + 3)
        # so I hard code the encodings for 7, 8, and 9

        if char == 9:
            encoded_password += "2"

        elif char == 8:
            encoded_password += "1"

        elif char == 7:
            encoded_password += "0"

        # in every other case, I can just add 3 to
        # the char to get its encoding
        # (i.e 3's encoding is 3 + 3)

        else:
            encoded_password += str(char + 3)

    return encoded_password

if __name__ == "__main__":
    main()

