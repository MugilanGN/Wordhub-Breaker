import time
from selenium import webdriver
from itertools import permutations
from itertools import combinations
import enchant
import time
import pyautogui
       
english = enchant.Dict("en_US")
liperm=[]
licombfinal=[]
final=[]
count=0
driver = webdriver.Chrome()
driver.get("https://wordhub.com")


def allPermutations(str): 
       
     # Get all permutations of string str 
     permList = permutations(str) 
  
     # insert all permutations into a list 
     for perm in list(permList):
         liperm.append(''.join(perm))

def allCombinations(string,integer): 
       
     # Get all combinations of string 
     combList = combinations(string,integer) 
  
     # insert all combinations into a list 
     for comb in list(combList):
         licombfinal.append(''.join(comb))

def word_finder(letters):
    string = "".join(letters)
    i=(len(string))
    while(i>2):
        allCombinations(string,i)
        for j in licombfinal:
            allPermutations(j)
        i=i-1

        
    for k in liperm:
        checked=english.check(k)
        if(checked==True):
            final.append(k)
            if((final.count(k)>1)):
                final.pop(-1)


    return final

def letter_identifier():
    while True:
        try:
            letters = []
            count = 0
            spans = driver.find_elements_by_tag_name('span')
            for span in spans:
                text = span.get_attribute('innerHTML')
                if len(text) == 1 and text.isalpha() and count >75 and count < 116:
                    letters.append(text)
                count+=1
            print(letters)
            if (len(letters) > 3):
                 break
        except:
            pass
    
    return letters

def typing_output(words):
    words.sort(key=len)
    for word in words:
        word_array = [word[i:i+1] for i in range(0, len(word), 1)]
        for letter in word_array:
            pyautogui.press(letter)
            time.sleep(0.1)
        for letter in word_array:
            pyautogui.press('backspace')
        time.sleep(0.5)
        print(word)
    
def main():
    time.sleep(15)
    print("started")
    letters = letter_identifier()
    word = word_finder(letters)
    print(word)
    typing_output(word)

main()

