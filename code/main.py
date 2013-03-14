from __future__ import division
import nltk


##
# returns the read in file as a string
##
def read_text(text, file_extension = "txt"):
    return open("../files/"+text+"."+file_extension, "rU").read()

##
# returns the lexical richness of a set of tokens which is
#   The number of tokens / the number if distinct tokens
##
def get_lexical_richness(tokens):
    return len(tokens)/get_distinct_word_count(tokens)

##
# returns the number distinct words used in a set of tokens
# example: the list ['I', 'am', 'am', 'a', 'duck'] would return 4
##
def get_distinct_word_count(tokens):
    return len(set(tokens))


test_file = read_text("test")
tokens = nltk.word_tokenize(test_file)

print get_distinct_word_count(tokens)
print get_lexical_richness(tokens)
print len(tokens)
print len(set(tokens))