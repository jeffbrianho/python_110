# Write a function to decode a dubstep string to its original form.The string
# may begin and end with one or more "WUB"s and there will be at least one (and
# possibly more) "WUB"s between each word.
# The input consists of a single non-empty string, consisting only of uppercase
# English letters.

"""
split word by WUB. 
final string if word in list is not wub, append
join word

"""
def song_decoder(sentence):
    
    word_list = sentence.split('WUB')
    final_list = [word for word in word_list
                  if word]
    
    return ' '.join(final_list)

# Examples:
print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")  == "WE ARE THE CHAMPIONS MY FRIEND")
