
# to open the list of words and condense it into a usable list. 
# in the future I'd like to clean this up. 
f = open("All_words.txt", "r")
words = f.readlines()
list_of_lists = words[0].split("], [")
clean_list = []
for l in list_of_lists: 
    clean_list.append(l.split("','")[0].replace("'", '').replace("]", "").replace("[", "").replace(" ", "").split(","))

flat_list = [item for sublist in clean_list for item in sublist]



green_letters = [] # put your letters in here e
yellow_letters = []
grey_letters = []

sample_green = [['e', 0]] # example of how the list might look
sample_yellow = [['s', 2], ['s', 2], ['i', 1], ['i', 2]] # example of how the list might look
sample_grey = ['c', 'l', 'n', 'k', 
'g', 'h', 'o', 't', 'd', 'r', 'e', 'a', 'm', 'w', 'p', 'y' ] # example of how the list might look



def listPossibleAnswers(green_let, yellow_let, grey_let, big_list): 
    # will give a list of possible answers based on placed letters
    green_words = []
    for word in big_list:
        containsAllLetters = True
        for g in green_let: 
            if not(g[0] in word):
                containsAllLetters = False  
            if g[0] != word[g[1]]:
                containsAllLetters = False  

        if containsAllLetters:
            green_words.append(word)
            
    yellow_words = []
    for gw in green_words: 
        containsAllLetters = True 
        for y in yellow_let:
            if not(y[0] in gw):
                containsAllLetters = False
            if y[0] == gw[y[1]]:
                containsAllLetters = False

        if containsAllLetters:
            yellow_words.append(gw)

    final_words = []
    for yw in yellow_words:
        containsGreyLetter = False
        for g in grey_let:
            if g in yw:
                containsGreyLetter = True
        if not containsGreyLetter:
            final_words.append(yw)


    print("List of possible words: ")
    print(final_words)
   

listPossibleAnswers(green_letters, yellow_letters, grey_letters, flat_list)

