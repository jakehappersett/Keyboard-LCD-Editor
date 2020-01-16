class ByteCode:

    def __init__(self):
        pass


class FileParser:
    
    def __init__(self, filePath):
        self.filePath = filePath
    
    def ParseFile(self):
        wordList = self.ReadFile(self.filePath)
        return self.filterHex(wordList)
    
    def ReadFile(self, filePath):
        lineList = [line.split() for line in open(filePath, 'r')]
        wordList = [item for sublist in lineList for item in sublist]
        return(wordList)
    
    def isHex(self, word):
        return(word.startswith('0x'))
    
    def filterHex(self, wordList):
        return([x.rstrip(', ').replace('0x', '') for x in wordList if self.isHex(x)])


def main():
    x = FileParser('glcdfont.c')
    hex = x.ParseFile()
    print(hex)

main()

