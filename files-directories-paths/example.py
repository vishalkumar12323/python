# with open('./text.txt', "r", buffering=-1, encoding="utf-8") as file:
#     content = file.read()
#     print(content)


# with open("./text.txt", mode='rb') as file:
#     content = file.read()
#     print(content)
#     pass

class ReadFile:
    def __init__(self, mode):
        self.score = 0
        self.fileHandler = open("./score.txt", mode=mode)

    def getScore(self):
        return int(self.fileHandler.read())

    def updateScore(self, score):
        return int(self.fileHandler.write(score))
    
read_file = ReadFile('r')
print(read_file.getScore())

write_file = ReadFile('w')
print(write_file.updateScore(1))