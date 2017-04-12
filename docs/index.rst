.. Matching Harry Potter Spells To Their Definitions documentation master file, created by
   sphinx-quickstart on Thu Dec  8 11:44:40 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Match HP spells with their definition's documentation!
==================================================================

About
-----
This is a research project which aims to explore computational creativity using recent advancements in natural language processing and machine learning. In order to execute this research, this program will be created and used to match harry potter spells to their definitions. The research will focus on how good two different types of vector representation of words (GloVe and Word2Vec) are at modelling semantic simalarity.  


Current Features
----------------
* Can use either Word2Vec or GloVe to generate Harry Potter spell names. 

* Provides evaluation against four different metrics: 
    
  1. Originality
  2. Cosine Similarity
  3. Synoynms
  4. Gibberish Words




Usage Notes 
-----------
* This program uses various python packages such as gensim and translate. To install all the relevant python packages go to the base directory of the project and run the command "pip install -r requirements.txt". 

* This program is designed to run through a command line interface and does not have a GUI. 



.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   code



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
