# Put Your Back Into It by Omar Aziz (u7205952@anu.edu.au)

# Using Whitney Houston's Greatest Love of All, either replaces the word 'love' with 'butt'
# or reverses the spelling of each line in the lyric.
# Partially inspired by Cloud to Butt extension for Chrome

# opening .txt with read mode because we don't want to edit the original
block_of_text = open('Greatest Love of All.txt','r')

# creates a loop so that user has to choose between the two given choices
while True:
    choice = input('Pick your poison: Back or Butt? ').lower()
    if choice == 'back' or choice == 'butt':
        print("Enjoy!")
        break
    else:
        print('Please choose between Back or Butt.')
        continue

# replaces every instance of the word 'love' with 'butt'
if choice == 'butt':
    butt = block_of_text.read().replace('love', 'butt').replace('Love', 'Butt')
    new_file = open('Greatest Butt of All.txt', 'w')
    new_file.write(butt)
    new_file.close()

# reverses the spelling for each line in the lyric, while maintaining line order
else:
    back = block_of_text.read().split('\n')
    back_sentence = []
    for line in back:
    # assuming slice statement is acceptable as is a built in method
        back_sentence.append(line [::-1])
    back_sentence = '\n'.join(back_sentence)
    new_file = open('Greatest Back(wards) of All.txt', 'w')
    new_file.write(back_sentence)
    new_file.close()

block_of_text.close()