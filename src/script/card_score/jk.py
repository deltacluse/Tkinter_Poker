class check :
    def __init__(self, card) :  # pattern-카드 무늬 배열, number-카드 숫자 배열
        self.card = card
        self.check()
        print(self.cardNumber)
        
        self.patternCheck()
        self.numberCheck()
        self.straightCheck()
        self.checkScore()

    def check(self) :
        self.cardNumber = [[0 for col in range(14)] for row in range(4)]  # 패턴 별로 숫자 입
        for i in range(7) :
            if(self.card[i][0] == "S") :
                self.cardNumber[0][int(self.card[i][1:])] += 1
            elif(self.card[i][0] == "D") :
                self.cardNumber[1][int(self.card[i][1:])] += 1
            elif(self.card[i][0] == "H") :
                self.cardNumber[2][int(self.card[i][1:])] += 1
            elif(self.card[i][0] == "C") :
                self.cardNumber[3][int(self.card[i][1:])] += 1

    def patternCheck(self) :  # 각 패턴이 몇 개인지 확인
        self.patternCount = [0, 0, 0, 0]  # 순서대로 스다하클
        for i in range(4) :
            self.patternCount[i] = len(self.card[i])

        self.patternMax = 0
        for i in range(4) :  # 각 패턴의 개수
            if(self.patternMax < self.patternCount[i]) :
                self.patternMax = self.patternCount[i]
#            print(self.patternCount[i])  # 각 패턴의 개수가 잘 들어갔나 테스트

    def numberCheck(self) :  # 각 숫자가 몇 개인지 확인

        self.numberCount = [0]
        for i in range(13) :
            self.numberCount.append(0)
        for i in range(4) :
            for j in range(14) :
                if(self.cardNumber[i][j] >= 1) :
                    self.numberCount[j] += 1
        self.numberCount[0] = 0
        print(self.numberCount)

        self.countNumber = [0, 0, 0, 0, 0]
        for i in self.numberCount :
            self.countNumber[i] += 1

        self.numberMax = 0
        for i in range(14) :  # 제일 많은 수와 그 개수
            if(self.numberMax <= self.numberCount[i]) :
                self.numberMax = self.numberCount[i]
                self.numberMaxCount = i

#        print(self.numberCount[i])  # 각 숫자의 개수가 잘 들어갔나 테스트

    def straightCheck(self) :
        self.straightNumber	= []
        for i in range(14) :
            if(self.numberCount[i] >= 1) :
                self.straightNumber.append(i)

        print(self.straightNumber)
        
        self.straightCount = 1
        for i in range(len(self.straightNumber) - 1) :
            if(self.straightNumber[i] + 1 == self.straightNumber[i+1]) :
                self.straightCount += 1
                if(self.straightCount == 5) :
                    break
            else :
                self.straightCount = 1
        print(self.straightCount)

    def checkScore(self):  # 족보 별 점수 계산

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
            score += 800 + self.topCheck([self.numberMaxCount])

        elif (self.patternMax == 5):  # flush
            score += 700

        elif (self.straightCount == 5):  # mountain
            score += 600

        elif (self.straightCount == 5):  # back straight
            score += 500

        elif (self.straightCount == 5):  # straight
            score += 400

        elif (self.countNumber[3] >= 1):  # triple
            score += 300 + self.topCheck([self.numberMaxCount])

        elif (self.countNumber[2] >= 2):  # two pair
            score += 200 + self.topCheck([self.numberMaxCount])

        elif (self.countNumber[2] == 1):  # one pair
            score += 100 + self.topCheck([self.numberMaxCount])


        else :  # top
            # don't plus score
            score += self.topCheck(self.straightNumber)

        print(score)

    def topCheck(self, topList) :
        maxNumber = 0
        for i in topList :
            if(i == 1) :
                return 14
            else :
                if(maxNumber < i) :
                    maxNumber = i
        return maxNumber


# 테스트
testCard = ["S01", "D01", "S01", "H11", "C05", "H05", "S07"]
test = check(testCard)