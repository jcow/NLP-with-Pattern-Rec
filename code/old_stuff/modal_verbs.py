from nltk.corpus import brown
import nltk

'''
cfd = nltk.ConditionalFreqDist(
                               (genre, word)    
                               for genre in brown.categories()
                               for word in brown.words(categories=genre))
genres = ['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
'''
print brown.fileids()

modals = ['can', 'could', 'may', 'might', 'must', 'will']

fin = []
for category in brown.categories():
    print category
    for fileid in brown.fileids(categories=category):
        sudo_fin = []
        sudo_fin.append(category)
        print fileid
        freqdist = nltk.FreqDist([w.lower() for w in brown.words(fileid)])
        for m in modals:
            sudo_fin.append(freqdist[m])
        print sudo_fin
        fin.append(sudo_fin)
    print '-----------------------'

print 'Writing to file'

print fin


f = open('../results/brown_modal_verbs.csv', 'w')
f.write('can,could,may,might,must,will\n')
for line in fin:
    
    counter = 1
    for item in line:
        item = str(item)
        f.write(item)
        if counter != len(line):
            f.write(',')
        else:
            f.write('\n')
        counter += 1
f.close()

#print brown.words('ca01')

#cfd.tabulate(conditions=genres, samples=modals)