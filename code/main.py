from __future__ import division
import nltk
from nltk.corpus import brown


#-----------------------------------------------------------------------------
#  Configurations
#-----------------------------------------------------------------------------

# which corpus do we want to use
current_corpus = brown



#-----------------------------------------------------------------------------
#  Helper functions to assist the Dimension-finding fucntions
#-----------------------------------------------------------------------------

def get_words_from_file(fileid):
    return current_corpus.words(fileids = fileid)

##
# Helper function to get the tagged words of the brown corpus
##
def get_tagged_words(fileid):
    return current_corpus.tagged_words(fileids=fileid);


## 
# Helper function to return a list of lists of sentences for a given file
##
def get_sentences(fileid):
    return current_corpus.sents(fileids=fileid)



#-----------------------------------------------------------------------------
#  Dimension-finding fucntions
#      These functions are used to get a specific dimension's value
#-----------------------------------------------------------------------------

##
# Gets the Lexical Diversity
# @param words: The list of words from a text
##
def get_lexical_diversity(words):
    return len(words) / len(set(words))

##
# Returns the number distinct tokens used in a text
# example: the list ['I', 'am', 'am', 'a', 'duck'] would return 4
#
# @param words: The list of words from a text 
##
def get_vocabulary_count(words):
    return len(set(words))


##
# Gets the adverbs, tag of RB
#     Tags are defined here: http://www.comp.leeds.ac.uk/ccalas/tagsets/brown.html
##
def get_adverbs(fileid):
    ret = []
    for i in get_tagged_words(fileid):
        if i[1] == 'RB':
            ret.append(i[0])
    return ret
            
##
# Gets the adverbs, tag of IN
#    Tags are defined here: http://www.comp.leeds.ac.uk/ccalas/tagsets/brown.html
##
def get_prepositions(fileid):
    ret = []
    for i in get_tagged_words(fileid):
        if i[1] == 'IN':
            ret.append(i[0])
    return ret
            
            
##
# Tags include anything in the list ['you', 'yous', 'your', 'yours']
##
def get_second_person_pronouns(words):
    ret = []
    for word in words:
        for sppn in ['you', 'yous', 'your', 'yours']:
            if word.lower() == sppn:
                ret.append(word)
                break;
    return ret

##
# Get the total character count for a set of words
#     The idea for this dimension comes from http://arxiv.org/pdf/cmp-lg/9410008.pdf
##
def get_character_count(words):
    count = 0
    for word in words:
        count += len(word)
    return count


## 
# Get the long word count
#     The idea for this dimension comes from http://arxiv.org/pdf/cmp-lg/9410008.pdf
##
def get_long_word_count(words):
    count = 0
    for word in words:
        if len(word) > 6:
            count += 1
    return count


##
# Get the "therefore" count 
##
def get_therefore_count(words):
    count = 0
    for word in words:
        if word.lower() == "therefore":
            count += 1
    return count

##
# Get punctuation count for a specific puncuation character
# @param words:
#    A list of words from the corpus
# @param punc:
#    The puncuation character you wish to count
##
def get_puncuation_count(words, punc):
    count = 0
    for word in words:
        if word == punc:
            count += 1
    return count
    


# TEST CRAP

words = get_words_from_file('cg22')

print get_tagged_words('cg22')

print get_second_person_pronouns(brown.words(fileids='cg22'))

print get_adverbs('cg22')

print get_puncuation_count(['cats', 'are', 'really', 'no', 'fun', '?'], '?')
print get_puncuation_count(words, '.')