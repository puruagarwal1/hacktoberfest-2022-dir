import big_o
#Generating random test strings of length 100
sample_strings = lambda n: big_o.datagen.strings(100)
#my logic to find the first non-repetitive character in the string
def non_repetitive(sample_string):
    string_list = list(sample_string)
    non_repetitive_char = next((ele for ele in string_list if string_list.count(ele)==1),None)
    return non_repetitive_char
#Calculating the Time complexity
best, others = big_o.big_o(non_repetitive, sample_strings,n_measures=20)
print(best)
