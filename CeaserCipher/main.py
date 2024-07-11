from alphabet import alphabet
def cesar(direction, text, shift_number):
  end_text = ""
  if direction == "decode":
      shift_number *= -1
  for char in text:
      if char in alphabet:
          position = alphabet.index(char)
          new_position = position+shift_number
          end_text+=alphabet[new_position]
      else:
          end_text+=char
  print(f"The {direction}d message is: {end_text}")

again = True
while again:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    cesar(choice, message, shift)
    resume=  input("Do you want to continue 'yes' or 'no':\n")
    if resume=="no":
        again=False
        print("GoodBye")