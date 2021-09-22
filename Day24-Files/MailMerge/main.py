#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt", "r") as inv_names:
    names = [name[:-1] for name in inv_names.readlines()]

with open("Input/Letters/starting_letter.txt", "r") as letter:
    lines = [line for line in letter.readlines()]

for name in names:
    new_letter = [line.replace("[name]", name) for line in lines]
    with open(f"Output/letter_for_{name}", "w") as out_letter:
        out_letter.writelines(new_letter)
