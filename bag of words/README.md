# Bag of Words Implementation using Python

This repository contains a custom implementation of the binary bag of words (BoW) model using Python. The binary bag of words model is a simple and commonly used technique in natural language processing (NLP) for text representation. It represents text data as a set of binary features, indicating the presence or absence of words in a given corpus.

## Binary BOW

The binary bag of words model is a text representation method that transforms text data into a binary format. Each word in the text is represented by a binary value (0 or 1), where 1 indicates the presence of the word and 0 indicates its absence. This implementation provides a basic approach to fitting a vocabulary and transforming text data into a binary bag of words representation.

## Count BOW
The count bag of words model is a text representation method that transforms text data into a numerical format by counting the frequency of each word in the corpus. Unlike the binary bag of words model, which represents words as binary values (0 or 1), the count bag of words model captures the frequency of each word occurrence.



## Usage

To use the binary bag of words implementation in your project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies (NumPy).
3. Use the provided functions to fit the vocabulary and transform your text data.

### Example



Below is an example of how to use the  bag of words implementation:

```python
# Importing required libraries
import numpy as np
from binary_bow import fit,transform
from count_bow import fit,transform

# Example usage
dataset = ["this is a sample", "this is another example example"]

# pass the dataset to fit function to get the vocabulary
vocabulary = fit(dataset)

# pass the dataset and vocabulary to the transform function
binary_bow_matrix = transform(dataset, vocabulary)

print("Binary/Count Bag of Words Matrix:\n", binary_bow_matrix) 


