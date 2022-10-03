# Script to scrape dictionary.com for all 5 letter words
import requests 
import string

all_letters = list(string.ascii_uppercase)

print(all_letters)

all_words = []

for letter in all_letters:
    page = 0
    response = requests.get("https://www.dictionary.com/e/crb-ajax/cached.php?page=" + str(page) + "&wordLength=5&letter=" + str(letter) + "&action=get_wf_widget_page&pageType=4&nonce=fd9e8921b8")
    print(response.json()['success'])

    suc = response.json()['success']    
    while suc: 
    #add to list 
        response = requests.get("https://www.dictionary.com/e/crb-ajax/cached.php?page=" + str(page) + "&wordLength=5&letter=" + str(letter) + "&action=get_wf_widget_page&pageType=4&nonce=fd9e8921b8")
        suc = response.json()['success']
        if suc:
            print(response.json()['data']['words'])
            all_words.append(response.json()['data']['words'])
        page += 1



f = open("All_words.txt", "a")

f.write(str(all_words))
f.close()

