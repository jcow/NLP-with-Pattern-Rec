##########################################################################################################
# Evin Ozer
# Jason Cowan
# CSCI 548-01
# Spring Semester
# 4/16/13
#
# Graduate Project - Natural Language Pattern Recognition
# ~ Performs Exploratory Data Analysis on a collection of
# ~ 500 texts from the Brown Corpus.
##########################################################################################################
# LIBRARIES
#
library(MASS)
library(gplots)
source("nlpr-lib.R");
#
# REQUIREMENTS
#
#require(graphics)
#

# Read in the NLP features.
nl_samples = read.csv("..//results//tagged_words.csv", header=TRUE)

# Create a vector of categories.
types = nl_samples$Type
sub_types = nl_samples$SubType
categories = nl_samples$Category

# set the data to be used
features = nl_samples[,5:ncol(nl_samples)]
non_constant_features = normalize(as.matrix(removeConstants(features)))
s_features = normalize(as.matrix(nl_samples[, c("Question.Mark.Count", "Long.Characters", "Total.Chars", "Second.Person.Pronouns", "Vocabulary.Count", "Lexical.Diversity", "Char.Avg.Per.Sentence", "Noun.count", "BEZ", "CD", "HVZ", "NP", "NPS", "NR", "PP.", "PPO", "PPS", "PPS.BEZ", "RB", "UH", "VBD", "VBG", "WQL")]))

# set the classes to be classified
classes = list()
classes[[1]] = types
classes[[2]] = sub_types
classes[[3]] = categories

# explore all non-constant features
cat("\nAll Non-Constant Features\n")
explore(non_constant_features,classes,F,F)

# explore all feature-selected features
cat("\nFeature-selected Features\n")
explore(s_features,classes,F,F)

# stop("Bam!")

