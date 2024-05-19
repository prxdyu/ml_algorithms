import numpy as np


# function to fit the given vocabulary 
def fit(dataset):
    """
    dataset : list of sentences

    finds unique words in the given corpus and returns a vocabulary of unique words of  dictionary type, data must be in the form of a list

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
        vocabulary[i]=j
        
    return vocabulary

# funciton to transform the given vocabulary to binary vectors
def transform(corpus,vocab):
    """ 
    vocab : vocabulary returned by the fit function
    
    returns a numpy bianry array of (nxm) where n is the number of sentences in your corpus and m is the total number of unique  words in your corpus, here data is your whole corpus and vocabulary is the unique words in your corpus 
    """
    # creating a numpy array which we will return in the end
    n=len(corpus)
    m=len(vocab.values())
    matrix=np.zeros([n,m],int)
    for text in corpus:
            index_text=corpus.index(text)
            for word in text.split():
                index_of_word=text.split().index(word)
                for i in range(m):
                    i_word=vocab[i]
                    if word==i_word:
                        matrix[index_text][i]=1
                        
                   
    return matrix