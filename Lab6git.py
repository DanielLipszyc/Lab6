def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    global user_input
    user_input = 1
    user_input = int(input("Please enter an option: "))

    return user_input

def encode():
    password = input("Please enter your password to encode: ")
    encoded_password = ""
    list = []
    for i in range(0, 8):
        list.append(int(password[i]))
    for i in range(0, len(list)):
        list[i] = str(list[i] + 3)
    for i in range(0, len(list)):
        encoded_password = encoded_password + list[i]
    print("Your password has been encoded and stored!")

    return encoded_password

def decode_password(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password
def main():
    while True:
        user_input = menu()
        if user_input == 1:
            encoded_password = encode()
            continue
        elif user_input == 2:
            decoded_password = decode_password(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif user_input == 3:
            break


if __name__ == "__main__":
    main()