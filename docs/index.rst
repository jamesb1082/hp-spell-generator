.. Matching Harry Potter Spells To Their Definitions documentation master file, created by
   sphinx-quickstart on Thu Dec  8 11:44:40 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Match HP spells with their definition's documentation!
==================================================================

About
-----
This Python package has been made as a tool which provides the user with the ability to perform an analysis on two popular vector space models: Google's Word2Vec and Stanford's GloVe. It can either be imported so that other developers can adapt the implemented functions for their own projects, or alternatively, they can run the file hp_spells.py, see the usage notes for more details. 

This documentation briefly describes the main features of the program, as well as notes on how to use the program, from installing the necessary dependencies to the parameters that can be passed. 

Current Features
----------------
* Can use either Word2Vec or GloVe to generate Harry Potter spell names. 

* A different list of spells can easily be used by replacing the contents of the file "spells.csv" with different contents provided the new content is in the same format. 

* Provides evaluation against four different metrics: 
    
  1. Originality
  2. Cosine Similarity
  3. Synoynms
  4. Gibberish Words

* Displays the metrics graphically using violin plots and time series plots. 

Usage Notes 
-----------
* To install the dependencies, navigate to the base level of the directory and use the command "pip install -r requirements.txt". 

* To execute the program navigate to the "hp_spells" directory, and use the command "Python hp_spells.py" to execute the program with default settings. 

* There are five different parameters that can be passed to the program. 
  
  1. --help : This displays the help screen which lists what parameters are available. 
  2. --glove : When this parameter is passed, the GloVe vector set is loaded instead of Word2Vec. 
  3. --exp EXP : An integer supplied to the program which determines how many times the experiment is repeated. 
  4. --comp : This flag is used to run the program in comparison mode. 
  5. --verbose : When this parameter is passed, the new spell name is printed out on the screen. 

* When passing a parameter to the parameter, ensure to use two hyphens.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   code



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
