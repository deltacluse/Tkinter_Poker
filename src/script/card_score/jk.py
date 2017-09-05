class check :
    def __init__(self, pattern, number) :  # pattern-카드 무늬 배열, number-카드 숫자 배열
        self.pattern = pattern
        self.number = number
        self.patternCheck()
        self.numberCheck()

    def patternCheck(self) :
        self.patternCount = [0, 0, 0, 0]
        for i in self.pattern :
            if(i=="S") : self.patternCount[0] += 1
            elif(i=="D") : self.patternCount[1] += 1
            elif(i=="H") : self.patternCount[2] += 1
            elif(i=="C") : self.patternCount[3] += 1

        self.patternMax = 0
        for i in range(4) :
            if(self.patternMax<self.patternCount[i]) :
                self.patternMax = self.patternCount[i]
#            print(self.patternCount[i])

    def numberCheck(self) :

        self.numberCount = [0]
        for i in range(13) :
            self.numberCount.append(0)
        for i in self.number :
            self.numberCount[i] += 1

        self.countNumber = [0, 0, 0, 0, 0]
        for i in self.numberCount :
            self.countNumber[i] += 1

        self.numberMax = 0
        for i in range(14) :
            if(self.numberMax<self.numberCount[i]) :
                self.numberMax = self.numberCount[i]
                self.numberMaxCount = i

#        print(self.numberCount[i])


    def checkScore(self):

        score = 0

        if ():  # royal straight flush
            score += 1200

        elif ():  # back straight flush
            score += 1100

        elif ():  # straight flush
            score += 1000

        elif (self.countNumber[4] == 1):  # four card
            score += 900

        elif (self.countNumber[3] == 1 and self.countNumber[2] >= 1):  # full house
            score += 800

        elif (self.patternMax == 5):  # flush
            score += 700

        elif ():  # mountain
            score += 600

        elif ():  # back straight
            score += 500

        elif ():  # straight
            score += 400

        elif (self.countNumber[3] >= 1):  # triple
            score += 300

        elif (self.countNumber[2] >= 2):  # two pair
            score += 200

        elif (self.countNumber[2] == 1):  # one pair
            score += 100

        else :  # top
            # don't plus score
            pass

        print(score)


testPattern = ["S", "D", "D", "S", "H", "C", "C"]
testNumber = [1, 3, 7, 3, 7, 9, 10]
test = check(testPattern, testNumber)
test.checkScore()