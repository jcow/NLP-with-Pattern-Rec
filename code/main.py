from __future__ import division
import nltk
from nltk.corpus import brown
from tags import *

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
def get_tagged_words_from_file(fileid):
    return current_corpus.tagged_words(fileids=fileid);


## 
# Helper function to return a list of lists of sentences for a given file
##
def get_sentences_from_file(fileid):
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
    return round((len(words) / len(set(words))), 6)

##
# Returns the number distinct tokens used in a text
# example: the list ['I', 'am', 'am', 'a', 'duck'] would return 4
#
# @param words: The list of words from a text 
##
def get_vocabulary_count(words):
    return len(set(words))

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
def get_total_character_count(words):
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
# Get the sentence count 
##
def get_sentence_count(sents):
    return len(sents)

##
# Get the average characters per sentence count 
##
def get_chars_per_sentence_avg(words, sents):
    return round((get_total_character_count(words) / get_sentence_count(sents)), 6)

##
# Tags include anything in the list ['me', 'we', 'us', 'our', 'my', 'us']
##
def get_first_person_pronouns(words):
    ret = []
    for word in words:
        for fppn in ['me', 'we', 'us', 'our', 'my', 'us']:
            if word.lower() == fppn:
                ret.append(word)
                break;
    return len(ret)

##
# Get the 'me' count
##
def get_me_count(words):
    ret = []
    for word in words:
        if word.lower() == 'me':
            ret.append(word)
    return len(ret)

##
# Get the 'present partciple' count. Tags: BEG, FW-VBG, HVG, VBG, VBG+TO
##
def get_present_participle_count(tagged_words):
    ret = []
    for (word, tag) in tagged_words:
        for pp in ['BEG', 'FW-VBG', 'HVG', 'VBG', 'VBG+TO']:
            if tag == pp:
                ret.append(tag)
                break;
    return len(ret)

##
# Get the 'I' count
##
def get_I_count(words):
    ret = []
    for word in words:
        if word == 'I':
            ret.append(word)
    return len(ret)

##
# Get the average characters per word count 
##
#def get_chars_per_word_avg(words):
    #return round((get_character_count(words) / len(words)), 6)

##
# Get the 'it' count
##
def get_it_count(words):
    ret = []
    for word in words:
        if word.lower() == 'it':
            ret.append(word)
    return len(ret)

##
# Get the 'noun' count. Tags: FW-AT+NN, FW-AT+NP, FW-IN+NN, FW-IN+NP, FW-NN, FW-NN$, FW-NNS, FW-NP, FW-NPS, FW-NR, NN, NN$, NN+BEZ, NN+HVD,
##
def get_noun_count(tagged_words):
    ret = []
    for (word, tag) in tagged_words:
        if 'NN' in tag:
            ret.append(tag)
    return len(ret)

##
# Get the 'present verb' count.
# Tags:  BEM, BEM*, BER, BER*, BEZ, BEZ*, DO, DO*, DO+PPSS, DOZ, DOZ*, DT+BEZ, DTS+BEZ, EX+BEZ, EX+HVZ, FW-BEZ, FW-DT+BEZ, FW-HV, FW-PPL+VBZ, FW-PPSS+HV, FW-VB, FW-VBZ, HV, HV*, HV+TO,
#        HVZ, HVZ*, VB, VB+AT, VB+IN, VB+JJ, VB+PPO, VB+TO, VB+VB, VBZ, WDT+BER, WDT+BER+PP, WDT+BEZ, WDT+DO+PPS, WDT+DOD, WDT+HVZ, WPS+BEZ, WPS+HVZ
##
def get_present_verb_count(tagged_words):
    ret = []
    for (word, tag) in tagged_words:
        for pp in ['BEM', 'BEM*', 'BER', 'BER*', 'BEZ', 'BEZ*', 'DO', 'DO*', 'DO+PPSS', 'DOZ', 'DOZ*', 'DT+BEZ', 'DTS+BEZ', 'EX+BEZ', 'EX+HVZ',
                   'FW-BEZ', 'FW-DT+BEZ', 'FW-HV', 'FW-PPL+VBZ', 'FW-PPSS+HV', 'FW-VB', 'FW-VBZ', 'HV', 'HV*', 'HV+TO', 'HVZ', 'HVZ*', 'VB',
                   'VB+AT', 'VB+IN', 'VB+JJ', 'VB+PPO', 'VB+TO', 'VB+VB', 'VBZ', 'WDT+BER', 'WDT+BER+PP', 'WDT+BEZ', 'WDT+DO+PPS', 'WDT+DOD', 'WDT+HVZ', 'WPS+BEZ', 'WPS+HVZ']:
            if tag == pp:
                ret.append(tag)
                break;
    return len(ret)

##
# Get the 'that' count
##
def get_that_count(words):
    ret = []
    for word in words:
        if word.lower() == 'that':
            ret.append(word)
    return len(ret)

##
# Get the 'which' count
##
def get_which_count(words):
    ret = []
    for word in words:
        if word.lower() == 'which':
            ret.append(word)
    return len(ret)

##
# Get punctuation count for a specific punctuation character
# @param words:
#    A list of words from the corpus
# @param punc:
#    The punctuation character you wish to count
##
def get_punctuation_count(words, punc):
    count = 0
    for word in words:
        if word == punc:
            count += 1
    return count
    


# TEST CRAP

'''
words = get_words_from_file('cg22')
tagged_words = get_tagged_words_from_file('cg22')
sents = get_sentences_from_file('cg22')


print "Sentence count: " + str(get_sentence_count(sents))
print "Char Avg Per Sentence: " + str(get_chars_per_sentence_avg(words, sents))
print "FPPN count: " + str(get_first_person_pronouns(words))
print "'Me' count: " + str(get_me_count(words))
print "PP count: " + str(get_present_participle_count(tagged_words))
print "'I' count: " + str(get_I_count(words))
print "'it' count: " + str(get_it_count(words))
print "Noun count: " + str(get_noun_count(tagged_words))
print "Verb count: " + str(get_present_verb_count(tagged_words))
print "'that' count: " + str(get_that_count(words))
print "'which' count: " + str(get_which_count(words))

print get_punctuation_count(['cats', 'are', 'really', 'no', 'fun', '?'], '?')
print get_punctuation_count(words, '.')

print get_tagged_words_from_file('cg22')


t = Tags()
print t.get_tag_counts(get_tagged_words_from_file('cg22'))
'''


# make the csv file
final_dump = []

final_dump_header = ["FileID", "Category", "Exclamation Count", "Quote Count", "Dollar Sign Count", "Percent Sign Count", "Ampersand Count", "Apostrophe Count", "Open Parenthesis Count", "Close Parenthesis Count", "Star Symbol Count", "Comma Count", "Period Count", "Colon Count", "Semicolon Count", "Question Mark Count","'Therefore' Count","Long Characters", "Total Chars", "Second Person Pronouns","Vocabulary Count", "Lexical Diversity", "Sentence Count", "Char Avg Per Sentence", "FPPN Count", "'Me' count", "PP count","'I' count", "'it' count", "Noun count", "Verb count", "'that' count", "'which' count"]
tag = Tags()
for t in tag.get_tags():
    final_dump_header.append(t)
final_dump.append(final_dump_header)


count = 1
for fileid in current_corpus.fileids():
    words = get_words_from_file(fileid)
    tagged_words = get_tagged_words_from_file(fileid)
    sents = get_sentences_from_file(fileid)
    
    row = []
    row.append(str(fileid))
    row.append(str(current_corpus.categories(fileids=fileid)[0]))
    row.append(str(get_punctuation_count(words, "!")))
    row.append(str(get_punctuation_count(words, "\"")))
    row.append(str(get_punctuation_count(words, "$")))
    row.append(str(get_punctuation_count(words, "%")))
    row.append(str(get_punctuation_count(words, "&")))
    row.append(str(get_punctuation_count(words, "'")))
    row.append(str(get_punctuation_count(words, "(")))
    row.append(str(get_punctuation_count(words, ")")))
    row.append(str(get_punctuation_count(words, "*")))
    row.append(str(get_punctuation_count(words, ",")))
    row.append(str(get_punctuation_count(words, ".")))
    row.append(str(get_punctuation_count(words, ":")))
    row.append(str(get_punctuation_count(words, ";")))
    row.append(str(get_punctuation_count(words, "?")))
    row.append(str(get_therefore_count(words)))
    row.append(str(get_long_word_count(words)))
    row.append(str(get_total_character_count(words)))
    row.append(str(len(get_second_person_pronouns(words))))
    row.append(str(get_vocabulary_count(words)))
    row.append(str(get_lexical_diversity(words)))
    row.append(str(get_sentence_count(sents)))
    row.append(str(get_chars_per_sentence_avg(words, sents)))
    row.append(str(get_first_person_pronouns(words)))
    row.append(str(get_me_count(words)))
    row.append(str(get_present_participle_count(tagged_words)))
    row.append(str(get_I_count(words)))
    row.append(str(get_it_count(words)))
    row.append(str(get_noun_count(tagged_words)))
    row.append(str(get_present_verb_count(tagged_words)))
    row.append(str(get_that_count(words)))
    row.append(str(get_which_count(words)) )

    tag = Tags()
    for t in tag.get_tag_counts(tagged_words):
        row.append(t[1])
    
    print str(count)+" row length: "+str(len(row))
    
    final_dump.append(row)
    
    count += 1
    
final_string = ""

last_line = len(final_dump[0])-1
counter = 0
for row in final_dump:
    final_string = str(final_string+(','.join( map( str, row) )))
    if counter != last_line:
        final_string = str(final_string + "\n")

print "-----------------"
#print final_string
print len(final_dump[0])
print len(final_dump[1])

f = open("../results/tagged_words.csv", "r+")
f.writelines(final_string)
f.close()

print("Done")
