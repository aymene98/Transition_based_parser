import string
from WordBuffer import WordBuffer

def getPrefixe(word, n = 3):
    if len(word) < n:
        while len(word) < n: word = word + 'µ'
        return word.lower()
    return word[:n].lower()
    #for i in range(len(last_chars)):
    #    if (last_chars[i] in string.ascii_letters) == False:
    #        last_chars[i] = '@'

def getCode(letter):
    characters = "µ" + "@" + string.ascii_lowercase
    return characters.index(letter)

class Prefixe:

    def __init__(self, lang, n = 100):
        self.content = {}
        for dataset in ['train_', 'dev_', 'test_']:
            self.readFromConllu('../data/'+dataset+lang+'.conllu')
        self.keepFrequentPrefixes(n)
        #self.listToString()

    def readFromConllu(self, conlluFilename):
        try:
            conlluFile = open(conlluFilename, encoding='utf-8')
        except IOError:
            print(conlluFilename, " : ce fichier n'existe pas")
            exit(1)
        
        tokens = []
        wordBuffer = WordBuffer()
        for ligne in conlluFile:
            if ligne[0] == '\n' :
                next
            elif ligne[0] == '#' :
                #print("commentaire")
                next
            else :
                ligne = ligne.rstrip()
                #                                1  Je  il  PRON    _   Number=Sing|Person=1|PronType=Prs   2   nsubj   _   _
                tokens = ligne.split("\t")
            if '-' not in tokens[0]:
                prefixe = getPrefixe(tokens[1])
                if (prefixe in self.content) == True:
                    self.content[prefixe] += 1
                else:
                    self.content[prefixe] = 1
        return self.content

    def keepFrequentPrefixes(self, n):
        sortedValues = dict(sorted(self.content.items(), key=lambda item: item[1], reverse = True))
        self.content = list(sortedValues.keys())[:n]
        return self.content

    #def listToString(self):
    #    for i in range(len(self.content)):
    #        self.content[i] = self.content[i][0] + self.content[i][1]
    #    return self.content