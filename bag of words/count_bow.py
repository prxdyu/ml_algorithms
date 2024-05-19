# importing the required libraries
import numpy as np
from collections import Counter


# function to fit the given corpus
def fit(dataset):
    """ 
    dataset : dataset : list of sentences
    finds unique words in the given corpus and returns a vocabulary of unique words of dictionary type, 
    data must be in the form of a list, this function returns a vocabulary (dictionary) 
    
    """
    unique_words=set()
    vocabulary=dict()
    if type(dataset)==type(list()):
        # our dataset should be a list of lists
        for row in dataset:
                words=row.split(" ")
                for word in words:
                    if len(word)>0:
                        unique_words.add(word)
    for i,j in enumerate(unique_words):
        vocabulary[j]=i
        
    return vocabulary


# function to transform the given text corpus to array of count vectors
def transform(corpus,vocab):
    """
    vocab : vocab returned by fit function
    
    returns a CountVectorized version of numpy array of (nxm) where n is the number of sentences in your corpus and m is the total number of unique words in your corpus, 
    here data is your whole corpus and vocabulary is the unique words in your corpusreturns a matrix of size (n_texts,max_len) 
    """
    # creating a numpy array which we will return in the end
    n=len(corpus)
    m=len(vocab.values())
    matrix=np.zeros([n,m],int)
    for text in corpus:
            word_count_text=dict(Counter(text.split()))
            index_text=corpus.index(text)
            for word in text.split():
                index_of_word=text.split().index(word)
                for i in range(m):
                    i_word=list(vocab.keys())[i]
                    if word==i_word:
                        matrix[index_text][i]=word_count_text[word]
                        
                   
    return matrix

