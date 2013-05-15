#Natural Language Processing with Pattern Recognition

This code base is used to classify texts based on genre.  The python scripts utilize the NLTK to get parts-of-speech tags from the Brown Corpus which is then written to a CSV file.  The R scripts take the CSV data and perform
PCA, MDS, LDA, and feature selection to the data to classify the texts.

## Results Folder
### tagged_words.csv
This CSV lives at results/tagged_words.csv and shows the results for the latest Brown Corpus iteration.

## Code Folder
### nlpr.R
This R script is the main R script that uses the results/tagged_words.csv to run the algorithms for pattern recognition

### nlpr-lib.R
This script is designed to hold functions to be used by the main R script

### main.py
This script runs though the brown corpus to analyze and write the found data to tagged_words.csv


### tags.py 
This script is used to get the parts-of-speech tags that the NLTK provides

