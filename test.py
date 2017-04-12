import sys
sys.path.insert(0, 'hp_spells/')
import pytest
from hp_spells import *


def test1():
	assert is_valid("james") == False
	assert is_valid("test_1") == True

def test2(): 
	input1 = [
	    [["type 1", 2, "lang 1"], 2], 
	    [["type 1", 2, "lang 2"], 2], 
	    [["type 2", 2, "lang 1"], 2],  
	    [["type 2", 2, "lang 2"], 2],
	]
	output = [
	    [["type 1", 2, "lang 1"], 2, 0.25], 
	    [["type 1", 2, "lang 2"], 2, 0.25], 
	    [["type 2", 2, "lang 1"], 2, 0.25], 
	    [["type 2", 2, "lang 2"], 2, 0.25],
	]

	assert calcProb(input1) == output


def test3():
	assert langCode("latin") == "la"


def test4():
	assert pigLatin("this is a test") == "histay isay aay esttay"

def test5(): 
    assert translate2("hello", "la") == "salve"

def test6(): 
	assert f("james") == "ja" 

def test7(): 
	input1 = [
		["type 1", 2, "lang 1"], 
		["type 1", 2, "lang 2"], 
		["type 2", 2, "lang 1"], 
		["type 2", 2, "lang 2"], 
	]	
	assert totalSpells(input1) == 8

def test8():
	assert checkStoredWords([], ["spell 1", "type 1"]) == [[["spell 1", "type 1"], 1]]


def test9(): 
	input1 = [
		[["L1", "t1"], 3, 0.2], 
		[["L2", "t2"], 2, 0.3], 
		[["L3", "t1"], 3, 0.5]
	]

	output = [
		( 0.2, ["L1", "t1"]), 
		(0.5, ["L2", "t2"]), 
		(1.0, ["L3", "t1"])
	]

	assert generateScale(input1) == output 


def test10():
	correct = [[['name1', ' def1', ' lang1', ' desc1'], 1, 0.5], [['name2', ' def2', ' lang1', ' desc2'], 1, 0.5]]
	assert count_instances("test.csv") == correct 

	
if __name__ == '__main__':
	test1()
	test2()
	test3()
	test4()
	test5()
	test6()
	test7()
	test8()
	test9() 
	test10()
