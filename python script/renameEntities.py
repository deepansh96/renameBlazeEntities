import os
cwd = os.getcwd()
nameStartInd = -1
dispName = 'xxxnameNOTfoundxxx'

for (root, dirs, files) in os.walk(cwd, topdown=True):
    for filename in os.listdir(root):
        #print(filename)
        if filename.endswith('.innovator_attbs'):
            with open(os.path.join(root, filename), 'rt') as myfile:
                for line in myfile:
                    nameStartInd = line.find('innovatorDisplayName=')
                    dispName = 'xxxnameNOTfoundxxx'
                    if nameStartInd != -1:
                        dispName = line[21:-1]
                        break

            if nameStartInd == -1 or dispName == 'xxxnameNOTfoundxxx': break
            else: print(dispName)

            #print(dispName)
            oldFileName = os.path.join(root, filename[:-16])
            newFileName = os.path.join(root, dispName)
            os.rename(oldFileName, newFileName)

            oldFileName = os.path.join(root, filename)
            newFileName = os.path.join(root, dispName+'.innovator_attbs')
            os.rename(oldFileName, newFileName)