def checkStoredWords(kwords, word):
    """
	
	This function updates a list of known words with a new word. If the spell type and
    language exists in the list the value is append by 1 otherwise, it is appended to 
    the end of the list with a value of 1. 

    :param kwords: List of spell types and language with associated frequencies.  
    :param word: One being the spell type and the other being the origin language.
    :type kwords: [[[str, str], int]...] 
    :type word: str  
    :return: the updated list of known words. 
    """ 

    found = False
    for kword in kwords:
        if kword[0] == word:
            kword[1] += 1
            found = True
    if found == False:
        kwords.append([word, int(1)])
    return kwords




def count_instances(fname):
    """
	
	Reads supplied file, where it splits it up. Then it appends each word to the data
    set building a list of words and frequencies using checkStoredWords(kwords, word). 

    :param fname: This is the name of the CSV file in which the spell data is stored.
    :type fname: str
    :return: returns a list of languages and the probabilities for each one.
    """

    file = open(fname, 'r')
    data = []

    for line in file:
        temp = line.rstrip()
        temp = temp.split(",")
        data = checkStoredWords(data, temp)
    file.close()
    data = calcProb(data)
    print(data)
    return data



def totalSpells(data):
    """
	
	Counts the number of spells in the dataset.

    :param data: List of spell types and origin language with frequency. 
    :type data: [[[str,str], int]...] 
    :return: an integer value of total number of spells.
    """

    total = 0
    for d in data:
        total += d[1]
    return total


def calcProb(data):
    """

	Calculates the probabilities for spells of each type. 

    :param data: List of spell types and origin language with frequency. 
    :type data: [[[str, str], int]...] 
    :return: A list of type of spells and their associated probabilities.
    """

    total = totalSpells(data)
    prob = 0.0
    for d in data:
	    prob = d[1] / total
	    d.append(prob)
    return data

count_instances("test.csv") 
