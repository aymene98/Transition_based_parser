def configuration_features(inputVector, config, featModel, index):
    for feature in featModel.featArray:
        if feature[0]=='C':
            if feature[1]=="SH":
                inputVector[index] = config.getStack().getLength()
            if feature[1]=="DIST":
                if config.getStack().isEmpty():
                    inputVector[index] = -1
                else:
                    #print(config.getStack().top())
                    b = feature[3] if feature[2] == "B" else feature[5]
                    s = feature[3] if feature[2] == "S" else feature[5]
                    inputVector[index] = config.getBuffer().distance(b, config.getStack().top()-s)
            index+=1
    return inputVector