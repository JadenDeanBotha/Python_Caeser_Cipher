# This is a program which encodes text
# This cypher will shift the letters of the alphabet by a certain amount of places
# eg.  if you input "hello" and set the key to 3, it would output "khoor"
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 
            'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caeser(start_text, shift_amount, cipher_direction):
        # create an empty string which will hold the encoded or decoded message
        end_text = ""
        # if the user chose to decode a message we then change the shift amount to a negative
        if cipher_direction == "decode":
            shift_amount *= -1
        # created a for loop which loops over the user inputed text
        for char in start_text:
            if char in alphabet:
                # We then find where each letter's index is in the alphabet list
                position = alphabet.index(char)
                # We then add the shift amount to the index of the original letter
                new_position = position + shift_amount
                # We then add the new index's value to our string end_text which will form the new word
                end_text += alphabet[new_position]
            else:
                # If the character isn't a letter just copy the character to the new word
                end_text += char
        # We then print the result back to the user
        print(f"The {cipher_direction}d text is {end_text}")

    # We use the modulus function to get the rainder of the shift so that if a user enters a shift
    # that is greater than the largest index in our alphabet, it will still work
    shift = shift % 26
    caeser(start_text=text, cipher_direction=direction, shift_amount=shift)
    
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")

