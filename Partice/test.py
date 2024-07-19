def vowels_in_string(alphabets):
    vowels = 'aeiouAEIOU'
    found_vowels = [char for char in input_string if char in vowels]

    return found_vowels

input_string = 'hihow, are, you'
vow = vowels_in_string(input_string)
print(f'{vow}')
