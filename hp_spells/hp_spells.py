from __future__ import division
from __future__ import print_function
import random
import gensim
from random import randint
from translate import Translator
import numpy as np
from transliterate import translit
import argparse, sys 
import matplotlib.pyplot  as plt 
from scipy.spatial import distance 
import seaborn as sns 
import pandas as pd 

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


def generateScale(data):
    """
	
	This stacks the probabilities of spells so that each spell has a boundary in which
    it a spell can be selected over another.

    :param data: list of spell names and their associated frequencies and probabilities. 
    :type data: [[[str,str],int,float]...]
    :return: a list of spells and the value between 0-1 in which that name will be selected.
    """

    value = 0
    index = -1
    scale = []
    for d in data:
        value += d[2]
        index += 1
        scale.append((value, d[0]))
    return scale


def getSpellType(scale, rndNum):
    """

	Selects a spell according to the random number passed. 

    :param scale: A list of tuples which contains the probability associated with each spell and type.  
    :param rndNum: The random number used to select a spell type.
    :type scale: [(str,str,float)..]
    :type rndNum: float
    :return: A string which is the spell type.
    """

    for i in range(-1, len(scale) - 1):
        if i == -1:
            temp2 = scale[i + 1]
            if rndNum >= 0:
                if rndNum < temp2[0]:
                    return temp2[1]
        else:
            temp = scale[i]
            temp2 = scale[i + 1]
            if rndNum >= temp[0]:
                if rndNum < temp2[0]:
                    return temp2[1]

    #add in extra code
    temp2 = scale[0]
    return temp2[1]


def is_valid(string):
    """
    check to see whether a word consists of alpha characters. 
    
    :param string: The string to be checked.  
    :type string: str 
    :return: Boolean value.
    """
    if string.isalpha():  
        return False
    return True 
   
    


def langCode(language): #this now works with python 2.7 i believe.  
    """
    
    Converts a language name into a language code for the translator. 

    :param language: Full name of the language, for example latin. 
    :type language: tr
    :return: The string code for the language.   
    """
    return {
        'Latin': 'la',
        'Greek': 'el',
        'Portuguese': 'pt',
        'West African Sidiki': 'it',  # CANT BE TRANSLATED. - Returns italian
        'Aramaic': 'el',  # CANT BE TRANSLATED - RETURNS GREEK
        'Pig Latin': 'PL',  # implement a seperate function to convert to pig latin.
        'English': 'en',
        'French': 'fr',
        'Spanish': 'es',
        'Italian': 'it',
    }.get(language, 'la')  # returns latin as default - if language is not found.


def translate2(word, lang):
    """
	Translates a word to a target language. 

    :param word: The word you want to convert. 
    :param lang: the lang code of the language you want to convert to.
    :type word: str
    :type lang: str 
    :return: a string containing the translated word in the latin alphabet. 
    """

    translator = Translator(to_lang=lang)
    try:
        out = translator.translate(word)
        if lang == 'el':
            return translit(word, lang, reversed=True)
        return out
    except:
        log("Error Cannot translate: " + word)

def log(text): 
    logfile = open("log.txt", "a") 
    logfile.write(text.encode("utf-8") + "\n")
    logfile.close() 

def sentenceToWord(sentence, model):
    """

    Takes a string and converts it into a vector. Then from that it picks a similar word that doesn't contain an underscore. 

    :param sentence: A string which contains a sentence to be converted into one word. 
    :type sentence: str
    :return: A string containing a similar word. 
    """

    sentence = sentence.split()
    output = []
    top_val = 10
    selected = []
    for word in sentence:
        try:
            output.append(model[word])
        except KeyError:
            log("key error in vector file" + word)

    output = np.array(output)
    vector_sum = output.sum(axis=0)
    output = model.most_similar(positive=[vector_sum], topn=top_val)
    final_output = output[randint(0, (top_val - 1))]
    
    while is_valid(final_output[0]):
        num = randint(0, top_val - 1)
        final_output = output[num]
        if num in selected:
            if len(selected) == top_val:
                top_val = top_val * 2
                output = model.most_similar(positive=[vector_sum], topn=top_val)
        else:
            selected.append(num)
#    print final_output[0]
    return final_output


def pigLatin(source):
    """
	 
	Takes a source string and converts it from english to pig latin. 

    :param source: Takes string of english words and changes it into pig latin.
    :type source: str
    :return: a string containing pig latin words.
    
    """

    letters = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
    source = source.split()
    for k in range(len(source)):
        i = source[k]
        if i[0] in ['a', 'e', 'i', 'o', 'u']:
            source[k] = i + 'ay'
        elif f(i) in letters:
            source[k] = i[2:] + i[:2] + 'ay'
        elif i.isalpha() == False:
            source[k] = i
        else:
            source[k] = i[1:] + i[0] + 'ay'
    return ' '.join(source)


def f(str):
    """
    Returns the first two chacters from the string.      

    :param str: A word that is passed.  
    :type str: str
    :return: a string that only contains the first two letters.  
    
    """
    if len(str) ==1:
        return str[0]
    return str[0] + str[1]


def generateSpell(sentence, model):
    """
    Generates a Spell from a sentence. 

    :param sentence: string which is the definition of the spell you want to create.
    :type sentence: str   
    :return: list containing the spell and the spell type.   
    :param model: loaded vector orepresentation of words.
	:type model: data file loaded.
    """

    spell = []
    vector = sentenceToWord(sentence, model)
    vector = vector[0]
    scale = generateScale(count_instances('spell_prob.csv'))
    selection = random.random()
    spell_meta = getSpellType(scale, selection)
    
    try:
        target_lang = langCode(spell_meta[1])
    except:
        log("langCode function didn't work. Using default latin.")
        target_lang = "la"
     
    if target_lang == "PL":
        spell.append(pigLatin(vector))
    else:
        spell.append(translate2(vector, target_lang))
    spell.append(spell_meta[0])
    spell.append(vector) #The original word before translation is also added onto the end for evaluation purposes.
    return spell 

def load_vectors(path, is_binary): 
    print("Loading: ", path) 
    model = gensim.models.Word2Vec.load_word2vec_format(path, binary=is_binary)
    model.init_sims(replace=True) 
    print("Loaded: ", path)
    return model 

# ==================================================================================
# Main part of the program. 
# ==================================================================================
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            'Use Word2Vec or GloVe datasets to generate Harry Potter Spells')
    parser.add_argument('--glove', action='store_const', const = 'glove',
            help='Use the GloVe dataset instead of the default Word2Vec.')    
    parser.add_argument('--exp',
    help="Specifies the number of experiments on this run. Default is 20.",
            action='store', type=int)
    args = parser.parse_args()
   
    logFile = open("log.txt", 'w' ) #the log file is blank at start of each execution 
    logFile.close() #closes the log file 
    num_experiments = 20 
    if args.exp != None: 
        num_experiments = args.exp 

    if args.glove:
        print("Vectors used: GloVe")
        log("---------------" +  "Vectors used: GloVe"+ "---------------")
        model = load_vectors("../../vectors/glove.txt.vw", False) 
        
    else:
        print("Vectors used: Word2Vec")
        log("---------------"+ "Vectors used: Word2Vec"+ "---------------")
        model = load_vectors("../../vectors/GoogleNews-vectors-negative300.bin", True) 
    average = 0.0 
    iterationCount = 0
    scores = [] 
    cos_dists = [] 
    avg_cos_dists = [] 

    for i in range(0, num_experiments): 
        print("---------------", i, "---------------")
        log("---------------"+str(i) +  "---------------")
        spellFile = open("spells.csv") 
        entry = [] 
        score = 0
        count = 0 
        for line in spellFile:
            count+=1
            line = line.strip("\n")
            entry = line.split(",")
             
            spell = generateSpell(entry[1], model)
             
            # spells is reduced to lower case to make sure "Bat" is same as "bat". 
            # definitin is split into words. 
            if spell[2].lower() in entry[1].split():  
                score +=1
            #calculate the cosine simalarity. 
           
            og_wd = model[entry[-1].strip()] 
            nw_wd = model[spell[-1]]
            cos_dists.append(distance.cosine(og_wd, nw_wd))   
             
        print("Num of spells that feature in definition: ", score)       
        print("Percentage: ", ((float(score)/count) * 100),"%") 
        print("Average Cosine-simalarity:", float(sum(cos_dists) / len(cos_dists)))  
        scores.append(score)  
        spellFile.close()
        iterationCount +=1 
        average += (float(score)/count)*100
        avg_cos_dists.append(float(sum(cos_dists) / len(cos_dists))) 

    print("----------------Experiment Results------------------")
    print("The mean average percentage over ", iterationCount , "tests: ",
            (average/iterationCount), "%")
    print("The mean cosine simalarity over ", iterationCount, "tests: ", 
            float(sum(avg_cos_dists)/ len(avg_cos_dists)))
    results = pd.DataFrame({'scores': scores, 'simalarity': avg_cos_dists}) 
    ax2 = sns.violinplot(x=results["simalarity"]) 
    sns.plt.show() 
    ax = sns.violinplot(x="scores", y="simalarity", data=results) 
    sns.plt.show()  

