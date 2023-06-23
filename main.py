from scripts.color import c_r,c_g,c_b,c_y
from scripts.Banner import banner,clear,_quit
from scripts.cprint import cprint
import os,platform,sys,time
from conf._pass import admin ,guest,repo
from assets.analysis_model import analysis_model
import pandas as pd


class app:
    user = oprn = year = continent = None
    def __init__(self):
        clear()
        banner()
        print(c_g+'Loading application please wait...')
        time.sleep(2)
        clear()


    def login(self):
       
        cprint(c_b+'...')
        time.sleep(.3)
        clear()
        cprint(c_b+'...')
        time.sleep(.3)
        clear()
        cprint(c_b+'...')
        time.sleep(.5)
        while True:
            clear()
            print(c_b)
            print('''
                \t\t\t\t\t\t\t\t\t\t\t\t\tpress CTRL+C to quit
                ---------------------------------------
                ---------------------------------------
                ||   Hi                              ||
                ||   Login as a Guest or Admin       ||
                ||   Select either of the following: ||
                ||    [0] Guest                      ||
                ||    [1] Admin                      ||
                ||    [2] Quit                       ||
                ---------------------------------------
                ---------------------------------------
            ''')
            c = input()
            if c == str(0):
                while True:
                    cprint(c_g+"Input Guest password (check it in the readme file): ")
                    pkk = input()
                    if pkk == guest:
                        self.user = "Guest"
                        break
                    elif pkk == str(0):
                        _quit()
                    else:
                        print(c_r+"Invalid password \t\t\t\t\t\t\t\t\t\t\t\t\t input 0 to quit\n"+c_g+"try again")
                break
            elif c == str(1):
                cnt = 4
                while cnt >0:
                    cnt-=1
                    cprint(c_r+"Input Admin password : ")
                    pkk = input()
                    if pkk == admin:
                        self.user = "Admin"
                        return None
                        break
                        
                    else:
                        print(c_r+"invalid you have {} trials left".format(cnt))
                    if(cnt>0):
                        continue
                    else:
                        _quit()
                    print("success")
                    time.sleep(1)
                    break    
            elif c == str(2):
                cprint(c_y+"GoodBye and do have a nice day")
                time.sleep(1)
                _quit()
            else:
                cprint(c_r+"Invalid user operation")
                continue

    def modal_g(self):
        while True:
            clear()
            print(c_b)
            print('''
                \t\t\t\t\t\t\t\t\t\t\t\t\tpress CTRL+C to quit
                ----------------------------------------
                ----------------------------------------
                ||   SELECT OPTIONS :                  ||
                ||What operation do you want to perform||
                ||   Select either of the following:   ||
                ||    [0] Run Analysis                 ||
                ||    [1] Read about the Application   ||
                ||    [2] View Credits                 ||
                ||    [3] Get Source Codes             ||
                ----------------------------------------
                ----------------------------------------
            ''')
            cprint(c_y+"Your selection: ")
            x=input()
            if x=='0':
                self.oprn="an"
                break
            elif x=='1':
                self.oprn="ab"
                break
            elif x=='2':
                self.oprn="cr"
                break
            elif x=='3':
                self.oprn="gs"
            else:
                cprint(c_r+"Invalid Operation ")
    

    def modal_a(self):
        while True:
            print('''
                \t\t\t\t\t\t\t\t\t\t\t\t\tpress CTRL+C to quit
                ----------------------------------------
                ----------------------------------------
                ||   SELECT OPTIONS :                  ||
                ||What operation do you want to perform||
                ||   Select either of the following:   ||
                ||    [0] Get Source Codes             ||
                ||    [1] Add Person to Credits        ||
                ||    [2] View Credits                 ||
                ----------------------------------------
                ----------------------------------------
            ''')
            cprint(c_y+"Your selection: ")
            x=input()
            if x=='0':
                self.oprn="gs"
                break
            elif x=='1':
                self.oprn="ap"
                break
            elif x=='2':
                self.oprn="cr"
                break
            else:
                cprint(c_r+"Invalid Operation ")


    def modal1(self):
        #clear()
        cprint(c_g+"\tThis application was built by mechatronics students of Uniport for\nthe analysis of the crude oil exports according to an analysis model used for a group project work.\nThe model takes raw data given in a csv file format and gets the mean, median and number of coontries in a continent that falls in the range\nof one standard deviation from the mean.")
        time.sleep(1)
        cprint("Steps we took in the analysis process :")
        time.sleep(.5)
        cprint('''
                1. The raw data was cleaned and striped of other unwanted continents data.
                2. An object of the analysis model class is created with the cleaned data.
                3. The necesary results are obtained through the model class methods.
                4. Results are outputed and plotted in suitable graphs. 

        ''')
        time.sleep(2)
        cprint(c_y+"The contributors of this project are mechatronics group 2 students whose names are listed in the credits file")
        cprint("This application is an open source project you can get the source codes by the 'get source codes' option")
        cprint("This application is still in its beta mode as some features are not fully implemented and bugs cannot be guaranteed.\n Whereas your contributions are important You can raise an issue at the github repo and suggestions are welcome.\nThanks for your support --From the developers--")

    def modal2(self):
        while True:
            clear()
            print(c_b)
            banner()
            cprint(c_b+"What year of data do you want to analyze")
            time.sleep(.5)
            print('''
                    \t\t\t\t\t\t\t\t\t\t\t\t\tpress CTRL+C to quit
                    ----------------------------------------
                    ----------------------------------------
                    ||   Select year to analyze:           ||
                    ||    [0] 1996 Petroleum export        ||
                    ||    [1] 2011 Petroleum export        ||
                    ||    [2] 2016 Petroleum export        ||
                    ||    [3] 2020 Petroleum export        ||
                    ----------------------------------------
                    ----------------------------------------
                ''')
            y = input()
            if y == '0':
                self.year = "1996 Petroleum Exports"
                df = pd.read_csv("assets/e1996-.csv")
                y = "1996"
            elif y == '1':
                self.year = "2011 Petroleum Exports"
                df = pd.read_csv("assets/e2011-.csv")
                y = "2011"
            elif y == '2':
                self.year = "2016 Petroleum Exports"
                df = pd.read_csv("assets/e2016-.csv")
                y="2016"
            elif y == '3':
                self.year = "2020 Petroleum Exports"
                df = pd.read_csv("assets/e2020-.csv")
                y="2020"
            else:
                cprint(c_r+"Invalid Request")
                continue
        
            time.sleep(1)
            clear()
            banner()
            cprint(c_b+"What continent data do you want to analyze")
            time.sleep(.5)
            print('''
                    \t\t\t\t\t\t\t\t\t\t\t\t\tpress CTRL+C to quit
                    ----------------------------------------
                    ----------------------------------------
                    ||   Select continent to analyze:      ||
                    ||    [0] Africa                       ||
                    ||    [1] Asia                         ||
                    ||    [2] Europe                       ||
                    ||    [3] North America                ||
                    ||    [4] Oceania                      ||
                    ||    [5] South America                ||
                    ----------------------------------------
                    ----------------------------------------
                ''')
            x = input()
            if x == '0':
                self.year = "Africa"
                x = "Africa"
            elif x == '1':
                self.year = "Asia"
                x = "Asia"
            elif x == '2':
                self.year = "Europe"
                x = "Europe"
            elif x == '3':
                self.year = "North America"
                x = "North America"
            elif x == '4':
                self.year = "Oceania"
                x = "Oceania"
            elif x == '5':
                self.year = "South America"
                x = "South America"
            else:
                cprint(c_r+"Invalid Request")
                continue

            xm=df.loc[df["Continent"]==self.year]
            xm= xm.reset_index(drop=True)

            print(xm)
            s_model = analysis_model(xm,y,x)

            time.sleep(1)
            break
        print(c_b+"Parsing csv file...")
        time.sleep(.3)
        print("Screening...")
        time.sleep(.5)
        print("Analyzing...")
        time.sleep(1)
        print("Checking results...")
        time.sleep(1.5)
        cprint(c_g+'Analysis success...')
        time.sleep(.3)
        cprint("...")
        clear()
        cprint(c_y+"This is the result of the analysis \nplease wait...")
        time.sleep(1)
        cprint("The mean of the trade value of exports for countries in Asia in 2016 : {}".format(s_model._m))
        cprint("The median the trade value of exports for countries in Asia in 2016 : {}".format(s_model._me))
        cprint("{} countries fall between the range of one standard deviation from the mean".format(s_model._r))
        time.sleep(2)
        cprint("The pictorial representation of the data is ready and available with the results")

        while True:
            cprint(c_b+'Would you want to view?')
            print('''
                        \t\t\t\t\t\t\t\t\t\t\t\t\tpress CTRL+C to quit
                        ----------------------------------------
                        ----------------------------------------
                        ||   Select Option                     ||
                        ||    [y] Yes                          ||
                        ||    [n] No                           ||
                        ----------------------------------------
                        ----------------------------------------
                    ''')
            opt = input()
            if opt=="Y"or opt=="y":
                showimg = True
                break
            elif opt=="N"or opt=="n":
                showimg = False
                break
            else:
                cprint(c_r+'Invalid response')
                continue
        if showimg :
             s_model.gen_chart_b(0)
             s_model.gen_chart_b(1)
             s_model.gen_chart_b(2)
             cprint(c_g+"Analysis plots have been saved successfully at C:\Group2MTEanalysisModel")
        else:
            input("Press Enter to continue")


    def modal3(self):
        try:
            with open('credits.txt') as f:
                cont=f.read()
            f.close()
            cprint(c_b+cont)
        except:
            cprint(c_r+'Unfortunately an error ocurred. Consider downloading the source codes')
        
        input("Press Enter to continue")

    def modal4(self):
        cprint("This source codes are available  at {}".format(repo))
        input("Press Enter to continue")



    def run(self):
        cprint("application start")
        self.login()
        time.sleep(1)
        clear()
        cprint(c_g+self.user+" login success")
        time.sleep(.5)
        cprint('Please Wait...')
        
        while True:
            time.sleep(2)
            clear()
            banner()
            if self.user=="Admin":
                self.modal_a()
            elif self.user=="Guest":
                self.modal_g()
            else:
                pass
            
            if(self.oprn=="ab"):
                self.modal1()
            elif(self.oprn=="an"):
                self.modal2()
            elif(self.oprn=="cr"):
                self.modal3()
            elif(self.oprn=="gs"):
                self.modal4()
            else:
                cprint(c_y+'Feature not available yet. Check out for updates')
                time.sleep(.8)



    

