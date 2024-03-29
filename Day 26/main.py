
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

my_dict = {row.letter: row.code for (index, row) in df.iterrows()}

word = input("Enter a word: ").upper()
code_list = [my_dict[char] for char in word]
#
print(code_list)



