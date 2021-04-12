# Word Wrangler
# Author - Noel Pereira
# Submission - http://www.codeskulptor.org/#user47_Ou6YdYG426hWDso.py

####################################################################

"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    list2=[]
    length=len(list1)
    for count in range(length):
        if list1[count] not in list2:
            list2.append(list1[count])
    return list2

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    list3 = []
    length1 = len(list1)
    
    for count1 in range(length1):
        if list1[count1] in list2:
            list3.append(list1[count1])
    return list3

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """  
    list3=[]
    while len(list1)>0 or len(list2)>0:
        if len(list1)>0 and len(list2)>0:
            if list1[0]>=list2[0]:
                list3.append(list2[0])
                list2=list2[1:]
                
            else:
                list3.append(list1[0])
                list1=list1[1:]
                
        elif len(list1)==0:
            while len(list2)>0:
                list3.append(list2[0])
                list2=list2[1:]
        else:
            while len(list1)>0:
                list3.append(list1[0])
                list1=list1[1:]
                
    return list3
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1)<= 1:
        return list1
    mid = len(list1)/2
    
    
    left = []
    right = []
    left = list1[:mid]
    
    right = list1[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    #print left,right
    list4 = merge(left,right)
    return list4

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    rest_strings = []
    reststring = []
    lastitem = []
    if len(word) == 0:
        return [""]
    else:
        first = word[0]
        rest = word[1:]
        #print rest,1
        reststring = gen_all_strings(rest)
        
        for items in reststring:
            
            rest_strings.append(items)
            #print rest_strings
            
        for item in reststring:
            #print item
            #print item
            last=first+str(item)
            lastitem=[]
            lastitem.append(last)
            #print lastitem
            
            
            #print lastitem
            rest_strings.append(lastitem[0])
            #lastitem=rest_strings[-1]
            #print lastitem
            length=len(lastitem[0])
            for count in range(0,length-1):
                #print lastitem,2
                listitem=list(lastitem[0])
                temp=listitem[count]
               # print temp,1
               # print listitem
                listitem[count]=listitem[count+1]
                #print listitem
                listitem[count+1]=temp
                #print listitem
                #print "".join(listitem),count
                rest_strings.append("".join(listitem))
                lastitem=[]
                #joined="".join(listitem)
                lastitem.append(listitem)
        
        return rest_strings

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()


