import sys
sys.path.insert(0, 'hp_spells/')
import pytest
from hp_spells import *


def test1():
	assert contains("james", "_") == False

def test2(): 
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
	assert calcProb(input1) == output


def test3():
	assert langCode("latin") == "la"


def test4():
	assert pigLatin("this is a test") == "histay isay aay esttay"

def test5(): 
	assert translate2("hello", "la")

if __name__ == '__main__':


	test1()
	test2()
	test3()
	test4()
	test5()

	
	print("All tests have passed.") 
	

