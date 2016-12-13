import sys
sys.path.insert(0, '../hp_spells/hp_spells')
import pytest
from hp_spells import *


if __name__ == '__main__':

	#Test 1 checks whether the string contains a character
	assert contains("james", "_") == False

	#Test 2  
	input1 = [
			["type 1", "lang 1", 2], 
			["type 1", "lang 2", 2], 
			["type 2", "lang 1", 2], 
			["type 2", "lang 2", 2], 
	]

	output = [
			["type 1", "lang 1", 2, 0.25], 
			["type 1", "lang 2", 2, 0.25], 
			["type 2", "lang 1", 2, 0.25], 
			["type 2", "lang 2", 2, 0.25],
	]

	#assert calcProb(input1) == output
	
