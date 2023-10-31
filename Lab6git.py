def main():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    global user_input
    user_input = 1
    user_inuput = int(input("Please enter an option: "))

    return user_inuput

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
    print(encoded_password)

    return encoded_password


if __name__ == "__main__":
    main()
    if user_input == 1:
        encode()
    elif user_input == 2:
        print()