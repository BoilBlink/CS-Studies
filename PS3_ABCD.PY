import re

#target strings
target = 'atgacatgcacaagtatgcat'
target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'
targetList = [target1, target2]

#key strings
key1 = 'at'
key2 = 'c'
key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'
keyList = [key10, key11, key12, key13]

#recursive

def countSubStringMatchRecursive(target,key):
    str_count = (target).count(key)
    print (str_count)

#makes it so you can snipe the key placements in string
    
def subStringMatchExact(target,key):
    result = [_.start() for _ in re.finditer(key,target)]
    print("The start indices of the substrings are : " + str(result))

#derive predefined substrings straight from target
    
starts1 = [_.start() for _ in re.finditer(key1,target1)]
starts2 = [_.start() for _ in re.finditer(key2,target1)]

#makes it so you can compare two strings and empty space of 1char match
#length is the number of chars in firstMatch

def subStringMatchOnePair(firstMatch,secondMatch,length):
    n = [_.start() for _ in re.finditer(firstMatch,target)]
    k = [_.start() for _ in re.finditer(secondMatch,target)]
    m = (str(length))
    print (n)
    print (k)
    print (m)
    
#makes it so you can see if the subStrings are a close match with
#the long String, allowing for misplacement of 1 char

####import re
####target = ('hellohelloheyheyhello')
####
####def subStringMatchOneSub(firstMatch,secondMatch,length):
####    n = [_.start() for _ in re.finditer(firstMatch,target)]
####    k = [_.start() for _ in re.finditer(secondMatch,target)]
####    m = length
####
####    print (n)
####    print (k)
####    print (m)
##
##
##listOne = [0, 5, 15, 19, 1]
##listTwo = [4, 8, 10, 18, 1]
##m = 2
##
###adds values to list content
##new_list = [x+m+1 for x in listOne]
##print (new_list)
##
###returns EXACT matching list values
##print1 = set(listOne) & set(listTwo)
##
### returns -1 accuracy to listTwo values
##newer_list = [x-1 for x in listTwo]
##
###returns comparison of formula and listTwo values expected to match with
### -1 char accuracy
##print2 = set(new_list) & set(newer_list)
##
##
##firstTest = ('four')
##ok = (len(firstTest))
##print (ok)


