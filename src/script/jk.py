def top_score(top_list):
    max_number = 0
    for i in top_list:
        if i == 1:
            return 14
        else:
            if max_number < i:
                max_number = i
    return max_number

class check:
    def __init__(self, card):  # 점수 체크할 때 객체 생성, card는 패 7장
        self.score = 0
        self.straight_flush_count = list(range(4))
        self.straight_flush_last = list(range(4))
        self.straight_flush_first = list(range(4))
        self.count_number = [0, 0, 0, 0, 0]
        self.number_count = [0]
        self.pattern_count = [0, 0, 0, 0]  # 순서대로 스다하클
        self.card_number = [[0 for _ in range(14)] for _ in range(4)]  # 패턴 별로 숫자 입력
        self.is_straight_flush = False
        self.is_royal_straight_flush = False

        self.straight_number = []
        self.straight_flush_number = [[], [], [], []]
        self.card = card

        self.check()
        #print("self.card_number : " + format(self.card_number), sep=' ')

        self.pattern_check()
        self.number_check()
        self.straight_check()
        self.straight_flush_check()
        self.check_score()

    def check(self):
        for i in range(len(self.card)):
            if self.card[i][0] == "S":
                self.card_number[0][int(self.card[i][1:])] += 1
            elif self.card[i][0] == "D":
                self.card_number[1][int(self.card[i][1:])] += 1
            elif self.card[i][0] == "H":
                self.card_number[2][int(self.card[i][1:])] += 1
            elif self.card[i][0] == "C":
                self.card_number[3][int(self.card[i][1:])] += 1

    def pattern_check(self):  # 각 패턴이 몇 개인지 확인
        self.pattern_count = [0, 0, 0, 0]  # 순서대로 스다하클
        for i in range(4):
            for j in range(14):
                if self.card_number[i][j] >= 1:
                    self.pattern_count[i] += 1

    def number_check(self):  # 각 숫자가 몇 개인지 확인
        for i in range(13):
            self.number_count.append(0)
        for i in range(4):
            for j in range(14):
                if self.card_number[i][j] >= 1:
                    self.number_count[j] += 1
        self.number_count[0] = 0
        #print("self.number_count : " + format(self.number_count), sep=' ')

        for i in self.number_count:
            self.count_number[i] += 1

        self.number_max = 0
        for i in range(14):  # 제일 많은 수와 그 개수
            if self.number_max <= self.number_count[i]:
                self.number_max = self.number_count[i]
                self.number_max_count = i

            #        print(self.number_count[i])  # 각 숫자의 개수가 잘 들어갔나 테스트

    def straight_check(self):
        for i in range(14):
            if self.number_count[i] >= 1:
                self.straight_number.append(i)

        #print("self.straight_number : " + format(self.straight_number), sep=' ')

        self.straight_first = self.straight_number[0]
        #print("1 self.straight_first : " + format(self.straight_first), sep=' ')

        self.straight_count = 1
        for i in range(len(self.straight_number) - 1):
            if self.straight_number[i] + 1 == self.straight_number[i + 1]:
                self.straight_count += 1
                self.straight_last = self.straight_number[i + 1]
                if self.straight_count == 5:
                    break
            else:
                self.straight_count = 1
                self.straight_first = self.straight_number[i + 1]

        #print("2 self.straight_first : " + format(self.straight_first), sep=' ')
        #print("self.straight_last : " + format(self.straight_last), sep=' ')
        #print("self.straight_count : " + format(self.straight_count), sep=' ')

    def straight_flush_check(self):
        for i in range(4):
            for j in range(14):
                if self.card_number[i][j] >= 1:
                    self.straight_flush_number[i].append(j)
            if len(self.straight_flush_number[i]) >= 1:
                #print("self.straight_flush_number : " + format(self.straight_flush_number), sep=' ')

                self.straight_flush_first[i] = self.straight_flush_number[i][0]
                self.straight_flush_last[i] = self.straight_flush_number[i][len(self.straight_flush_number[i]) - 1]
                #print("1 self.straight_flush_first[" + format(i) + "] : " + format(self.straight_flush_first[i]), sep=' ')

                self.straight_flush_count[i] = 1
                for j in range(len(self.straight_flush_number[i]) - 1):
                    if self.straight_flush_number[i][j] + 1 == self.straight_flush_number[i][j + 1]:
                        self.straight_flush_count[i] += 1
                        self.straight_flush_last[i] = self.straight_flush_number[i][j + 1]
                        if self.straight_flush_count[i] == 5:
                            break
                    else:
                        self.straight_flush_count[i] = 1
                        self.straight_flush_first[i] = self.straight_flush_number[i][j + 1]

                #print("2 self.straight_flush_first[" + format(i) + "] : : " + format(self.straight_flush_first[i]), sep=' ')
                #print("self.straight_flush_last[" + format(i) + "] : : " + format(self.straight_flush_last[i]), sep=' ')
                #print("self.straight_flush_count[" + format(i) + "] : " + format(self.straight_flush_count[i]), sep=' ')

        for i in range(4):
            if self.straight_flush_count[i] == 5:
                self.is_straight_flush = True
                self.what_pattern = i

        for i in range(4):
            if len(self.straight_flush_number[i]) >= 1:
                if self.straight_flush_number[i][0] == 1 and self.straight_flush_count[i] == 4 and self.straight_flush_first[i] == 10 and self.straight_flush_last[i] == 13:
                    self.is_royal_straight_flush = True
                    self.what_pattern = i

    def mountain_check(self):
        if self.straight_number[0] == 1 and self.straight_count == 4 and self.straight_first == 10 and self.straight_last == 13:
            return True

    def flush_score(self):
        for i in range(4):
            if self.pattern_count[i] == 5:
                return i

    def fair_win(self):
        for i in range(4):
            if (self.card_number[i][self.number_max_count]):
                return 4 - i

    def check_score(self):  # 족보 별 점수 계산

        # royal straight flush
        if self.is_royal_straight_flush:
            self.score += 12000 + (4 - self.what_pattern)

        # back straight flush
        elif self.is_straight_flush and self.straight_flush_first[self.what_pattern] == 1:
            self.score += 11000 + (4 - self.what_pattern)

        # straight flush
        elif self.is_straight_flush:
            self.score += 10000 + self.straight_flush_last[self.what_pattern] * 10 + (4 - self.what_pattern)

        # four card
        elif self.count_number[4] == 1:
            self.score += 9000 + top_score([self.number_max_count]) * 10

        # full house
        elif self.count_number[3] == 1 and self.count_number[2] >= 1:
            self.score += 8000 + top_score([self.number_max_count]) * 10

        # flush
        elif max(self.pattern_count) == 5:
            self.score += 7000 + (4 - self.flush_score())

        # mountain
        elif self.mountain_check():
            self.score += 6000 + top_score([max(self.straight_number[1:3])]) * 10

        # back straight
        elif self.straight_count == 5 and self.straight_first == 1:
            self.score += 5000 + top_score([max(self.straight_number[5:])]) * 10

        # straight
        elif self.straight_count == 5:
            self.score += 4000 + self.straight_last * 10

        # triple
        elif self.count_number[3] >= 1:
            self.score += 3000 + top_score([self.number_max_count]) * 10

        # two pair
        elif self.count_number[2] >= 2:
            self.score += 2000 + top_score([self.number_max_count]) * 10 + self.fair_win()

        # one pair
        elif self.count_number[2] == 1:
            self.score += 1000 + top_score([self.number_max_count]) * 10 + self.fair_win()

        # top
        else:
            self.score += top_score(self.straight_number) * 10 + self.fair_win()

    def getscore(self):
        return self.score

# 테스트
#test_card = ["D07", "D06", "D05", "S05", "H05", "D10", "D11"]  # 테스트 패 7장
#test = check(test_card)  # 객체 생성
#score = test.getscore()  # 테스트 패의 점수 계산
#print(score)