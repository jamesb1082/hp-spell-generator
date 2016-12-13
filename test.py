import sys
sys.path.insert(0, 'hp_spells/')
import pytest
from hp_spells import *


def failedtest(num, name):
	str1 = "test " + str(num) +  ": " + str(name) 
	str2 = "result = failed" 
	
	print("{0:<50} {1:<50}".format(str1, str2)) 
	
if __name__ == '__main__':
	
	#Test 1 checks whether the string contains a character
	try:
		assert contains("james", "_") == False
	except: 
		failedtest(1, "contains()") 
	#Test 2  
	input1 = [
			["type 1", 2, "lang 1"], 
			["type 1", 2, "lang 2"], 
			["type 2", 2, "lang 1"], 
			["type 2", 2, "lang 2"], 
	]

	output = [
			["type 1", 2, "lang 1", 0.25], 
			["type 1", 2, "lang 2", 2, 0.25], 
			["type 2", 2, "lang 1", 0.25], 
			["type 2", 2, "lang 2", 0.25],
	]

	try: 
		assert calcProb(input1) == output
	except: 
		failedtest(2, "calcProb()")


	#test 3 language code
	try:
		assert langCode("latin") == "la" 	
	except: 
		failedtest(3, "langCode()") 

	
	#test 4 pig latin function 
	try: 
		assert pigLatin("this is a test") == "histay isay aay esttay"
	except: 
		failedtest(3, "pigLatin()") 
