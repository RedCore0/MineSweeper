#============================================================
#
#   Binary search
#       by Michal Redzko
#
#   Final build
#
#   WARNING:
#       it seems like this code runs only in VScode
#       I doubt it's because of the code itself but rather directory of my python app
#       might work normally on different computers
#
#   Make sure words.txt file is in the same directory as the python file
#
#=============================================================


#This part of code gets all the words from the text file and puts them in a list
WordList = []
with open("words.txt") as words:
    for line in words:
        WordList.append(line.strip())

SearchFor = input("Find: ") #Allows user to search for a word

#This function Searches for the word using binary search
def FindWord(Search, start, end):
    #Prints not found if word was not found
    if start > end: 
        print("Not Found")
        exit() 
    middle = (start + end)//2 #finds middle of the list
    center = WordList[middle]
    #prints words location if it has been found
    if center == Search:
        print("Word location: Line ", middle+1)
    
    #splits searching area
    if center > Search:
        FindWord(SearchFor, start, middle-1)
    if center < Search:
        FindWord(SearchFor, middle+1, end)

FindWord(SearchFor,0,len(WordList))