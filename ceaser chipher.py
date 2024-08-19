alphab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def display_menu():
    print("\nCaesar Cipher Menu:")
    print("1. Encode a message")
    print("2. Decode a message")
    print("3. Exit")

def encode(txt, sft):
    chiper_text = ""
    for i in txt:
        if i in alphab:
            position = alphab.index(i)
            new_position = position + sft
            new_letter = alphab[new_position]
            chiper_text += new_letter
        else:
            chiper_text += i
    return chiper_text

def decode(tex, st):
    dec_text = ""
    for i in tex:
        if i in alphab:
            position = alphab.index(i)
            org_position = position - st
            org_letter = alphab[org_position]
            dec_text += org_letter
        else:
            dec_text += i
    return dec_text

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").lower()

        if choice == '1':
            text = input("Enter the text you want to encode: ").lower()
            shift = int(input("Enter the shift number: "))
            encoded_message = encode(text, shift)
            print(f"\nThe encoded text is: {encoded_message}")

        elif choice == '2':
            text = input("Enter the text you want to decode: ").lower()
            shift = int(input("Enter the shift number: "))
            decoded_message = decode(text, shift)
            print(f"\nThe decoded text is: {decoded_message}")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
