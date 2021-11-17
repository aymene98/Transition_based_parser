import numpy as np

class FeatModel:
    def __init__(self, featModFilename, dicos):
        self.featArray = self.readFeatModelFile(featModFilename)
        self.inputVectorSize = self.computeInputSize(dicos)


    def readFeatModelFile(self, featModFilename):
        try:
            featModFile = open(featModFilename, encoding='utf-8')
        except IOError:
            print(featModFilename, " : ce fichier n'existe pas")
            exit(1)
        featArray = []
        for ligne in featModFile:
            if ligne.split()[0] == "W":
                # We are in a word feature
                (featType, container, position, wordFeature) = ligne.split()
                #print("type =", featType, "container = ", container, "position = ", position, "wordFeature = ", wordFeature)
                if(container != "B" and container != "S"):
                    print("error while reading featMod file : ", featModFilename, "container :", container, "undefined")
                    exit(1)
                if not wordFeature in set(['POS', 'LEMMA', 'FORM', 'SUFFIXE', 'PREFIXE']):
                    print("error while reading featMod file : ", featModFilename, "wordFeature :", wordFeature, "undefined")
                    exit(1)
                featArray.append((featType, container, int(position), wordFeature))
            elif ligne.split()[0] == "C":
                # We are in a configuration feature
                featArray.append(tuple(ligne.split()))
                pass
        featModFile.close()
        return featArray
            
    def computeInputSize(self, dicos):
        #print("dicos=",dicos.content['POS'])
        #print("FeatArray=",self.getFeatArray())
        inputVectorSize = 0
        for featTuple in self.getFeatArray():
            if featTuple[0]=="W":
                feat = featTuple[3]
                inputVectorSize += dicos.getDico(feat).getSize()
            else:
                inputVectorSize += 1
        #return 0
        return inputVectorSize

    def getInputSize(self):
        return self.inputVectorSize
        
    def getNbFeat(self):
        return len(self.featArray)
        
    def getFeatArray(self):
        return self.featArray

    def getFeatType(self, featIndex):
        return self.featArray[featIndex][0]

    def getFeatContainer(self, featIndex):
        return self.featArray[featIndex][1]

    def getFeatPosition(self, featIndex):
        return self.featArray[featIndex][2]

    def getFeatLabel(self, featIndex):
        return self.featArray[featIndex][3]

    def buildInputVector(self, featVec, dicos):
        inputVector = np.zeros(self.inputVectorSize, dtype="float32")
        origin = 0
        for i in range(self.getNbFeat()):
            if self.getFeatType(i)=="W" and self.getFeatLabel(i)!='FORM':
                label = self.getFeatLabel(i)
                size = dicos.getDico(label).getSize()
                position = dicos.getCode(label, featVec[i])
                #print('featureName = ', featureName, 'value =', featVec[i], 'size =', size, 'position =', position, 'origin =', origin)
                inputVector[origin + position] = 1
                origin += size
            if self.getFeatType(i)=="W" and self.getFeatLabel(i)=='FORM':
                em = dicos.getCode(self.getFeatLabel(i), featVec[i])
                for i in range(len(em)):
                    inputVector[origin] = em[i]
                    origin+=1
                
        #return None
        return inputVector, origin
