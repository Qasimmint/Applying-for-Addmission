import time

class Subjects:
    def __init__(self,sub_list):
        def greet(visitor):
            print(f"Hi ! Mr.{visitor.capitalize()}\nWelcom to our University")

        greet(input("Enter your name: "))
        time.sleep(1)

        self.sub_list = sub_list
        sub_list = ["Math","Geometry","Calculus","Trignometry","Linear Algebra","Statistics","Algorithms"]
        print("The list of availibale subjecta are as follow:\n")
        for sub in sub_list:
            print("-->",sub)
            time.sleep(2)
    
    def mathData(self):
        math_crit = {
            'merit':1060,
            'required_marks':1020,
            'program': 'BS_4-year',
            'total_seats': 50
            }
        print(math_crit)
        
    def geoData(self):
            geo_crit ={
                'merit':900,
            'required_marks': '750',
            'program': 'BS_4-year',
            'total_seats': 50
            }
            print(geo_crit)

    def calData(self):
            cal_crit = {
                'merit':1090,
                'required_marks':1050,
                'program': 'BS_4-year',
                'total_seats': 50
                }
            print(cal_crit)

    def aglbData(self):
            lin_algb_crit = {
                'merit':1000,
                'required_marks':950,
                'program': 'BS_4-year',
                'total_seats': 50
                }
            print(lin_algb_crit)

    def trigData(self):
            trig_crit = {
                'merit':1100,
                'required_marks':1070,
                'program': 'BS_4-year',
                'total_seats': 50
                }
            print(trig_crit)

    def statData(self):
            stat_crit = {
                'merit':900,
                'required_marks':820,
                'program': 'BS_4-year',
                'total_seats': 50
                }
            print(stat_crit)
        
    def algoData(self):
            algo_crit = {
                'merit':1010,
                'required_marks':920,
                'program': 'BS_4-year',
                'total_seats': 50
                }
            print(algo_crit)

    def query(self):
        su_dict = {
            'Math':'m',
            'Linear Algebra':'l',
            'Calculus':'c',
            'Trignometry':'t',
            'Statistics':'s',
            'Geometry':'g',
            'Algorithms':'a'
        }
        time.sleep(1.5)
        print("press the respective keys to get the info and criteria about subject\n",su_dict)
        sub_dict = input("Enter the key: ")
        time.sleep(1.1)
        if sub_dict==('m' or 'M'):
            print(self.mathData())
        elif sub_dict=='l' or 'L':
            print(self.algoData())
        elif sub_dict=='c' or 'C':
            print(self.calData())
        elif sub_dict=='t' or 'T':
            print(self.trigData())
        elif sub_dict=='s' or 'S':
            print(self.statData())
        elif sub_dict=='g' or 'G':
            print(self.geoData())
        elif sub_dict=='a' or 'A':
            print(self.algoData())
        else:
            print("Sir...! please enter the valid key")
            
class StudentMarks:
    mat_marks = int(input('Enter your matric marks: '))
    inter_marks = int(input('Enter your Intermediate marks: '))
    time.sleep(2)
    total_marks = mat_marks+inter_marks
    prcnt_marks = (total_marks/1100)*100
    time.sleep(2)
    print(f"You got {prcnt_marks} marks in percentage ")

    def marksCriteria(self):
        if self.inter_marks in range(900,1000):
            print("you are only eligible for Geography and Statistics")
        elif self.inter_marks in range(1000,1050):
            print("you are only eligbile for Algorithms, Algebra,Geography,Statistics and Math")
        elif self.inter_marks in range(1050,1100):
            print("you are eligible for any discipline which you wish")
        else:
            print("Sorry, you never meet to our criteria, try somewhere else.")
    
    def alterMarks(self,crisis):
        print(f"Due to {crisis} 3% are incremented in each students final marks.")
        alter_marks = self.inter_marks + 12
        print("So marks are estimated as: \t",alter_marks)

S = StudentMarks()
S.marksCriteria()
s = Subjects(sub_list=Subjects)
s.query()
S.alterMarks("Corona Virus")
