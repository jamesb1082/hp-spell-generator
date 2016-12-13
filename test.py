import sys
sys.path.insert(0, '../hp_spells/')
import pytest
from hp_spells import contains


if __name__ == '__main__':
	assert contains("james", "_") == False 
