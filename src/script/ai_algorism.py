class Ai:
    def __init__(self, parent):  # 부모로 main.py의 Poker 클래스 객체 a를 받아옴
        self.parent = parent

    def ai_turn(self):  # 버튼 클릭하면 user 차례 끝나고 실행되는 ai 진행
        self.ai_betting(1)
        self.ai_betting(2)
        self.ai_betting(3)

    def ai_betting(self, index):  # 각 ai가 실행하는 코드
        self.parent.betting.call(index)
        self.parent.ui_update(index)
