from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z' ]

def caesar(text, shift, direction):
    end_text=""
    # if direction=="decode":
    #     shift*=-1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == "encode":
                new_position = position + shift
            elif direction == "decode":
                new_position = position - shift

            # new_position = position + shift
            new_letter = alphabet[new_position]
            end_text += new_letter
        else:
            end_text+=char #numbers, symbols and letters will be left out and will be added as it is

    print(f"The {direction}ed text is {end_text}")

should_continue=True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift=shift%26

    caesar(text,shift,direction)

    res= input("Do you want to continue? Type 'yes' or 'no.\n")

    if res=="no":
        should_continue=False
        print("Goodbye")




