import sys
sys.path.insert(0, '../hp_spells/')
import pytest
import hp_spells


if __name__ == '__main__':
	assert hp_spells.contains("james", "_") == False 
