import pandas
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key, value)
#
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(row)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
#  {"A": "Alfa", "B": "Bravo"}
nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
#nato_alphabet_dict = { for ()}
nato_dict = {row.letter: row.code for (index, row) in nato_dataframe.iterrows()}
print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please say a word: ").upper()
user_code = [nato_dict[char] for char in user_input]
print(user_code)
