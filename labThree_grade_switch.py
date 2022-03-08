class Switch:

    def __init__(self, mark):
        print("This program will determine your grade based on your %.")
        self.mark = mark

    def score(self):
        print(self.mark)


    def markB(self):
        if self.mark > 80:
            print("B")

    def markC(self):
        if self.mark > 70:
            print("C")

    def markD(self):
        if self.mark >60:
            print("D")

    def markF(self):
        if self.mark < 60:
            print("You fucking suck cunt")


myMark = Switch(int(input("Score:")))
myMark.score()
