word = 'what-a-b.e.a.utiful day!'

cleaned_word = [char for char in word
                if char.isalpha()]

crazy_letters = [char.lower() if indx % 2 == 0 else char.upper() for indx, char in enumerate(cleaned_word)
                 ]


print(crazy_letters  == ['w', 'H', 'a', 'T', 'a', 'B', 'e', 'A', 'u', 'T', 'i', 'F', 'u', 'L', 'd', 'A', 'y'])