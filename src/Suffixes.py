import string
from WordBuffer import WordBuffer

def getSuffixe(word, n = 3):
    last_chars = word[-n:]
    last_chars = list(last_chars)
    #for i in range(len(last_chars)):
    #    if (last_chars[i] in string.ascii_letters) == False:
    #        last_chars[i] = '@'
    while len(last_chars) < n: last_chars = ["µ"] + last_chars
    last_chars = last_chars[0] + last_chars[1] + last_chars[2]
    return last_chars.lower()

def getCode(letter):
    characters = "µ" + "@" + string.ascii_lowercase
    return characters.index(letter)

class Suffixe:

    def __init__(self, lang, n = 100):
        self.content = {}
        for dataset in ['train_', 'dev_', 'test_']:
            self.readFromConllu('../data/'+dataset+lang+'.conllu')
        self.keepFrequentSuffixes(n)
        self.listToString()

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
                suffixe = getSuffixe(tokens[1])
                if (suffixe in self.content) == True:
                    self.content[suffixe] += 1
                else:
                    self.content[suffixe] = 1
        return self.content

    def keepFrequentSuffixes(self, n):
        sortedValues = dict(sorted(self.content.items(), key=lambda item: item[1], reverse = True))
        self.content = list(sortedValues.keys())[:n]
        return self.content

    def listToString(self):
        for i in range(len(self.content)):
            self.content[i] = self.content[i][0] + self.content[i][1] + self.content[i][2]
        return self.content