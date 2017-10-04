#Thomas Christie (6012)
#Traditional Application (Submission 2017)
#A Population Model

#First I import the libraries which will be used in the program.
import os
import sys
import random

#The function CheckFloat is used to validate the floats the user enters when setting Generation 0 Values.
#It takes the value "Statement", which is the statement which will be outputted to the user when setting each Generation 0 Value.
def CheckFloat(Statement):
  while True: #An infinite loop is set up.
    Float = input(Statement) #The user inputs their reply to the statement outputted.
    try: #A try-except block is used to check if the input is actually a float.
      float(Float) 
      Float = float(Float) #If the input is a float then the variable Float is assigned their float.
      Float = round(Float,3) #Their float is then rounded to 3 decimal places as the number of greenfly is measured in thousands, so 3 decimal places is the maximum accuracy available whilst keeping the populations whole numbers.
      if Float >= 0: #Checks if their float is positive.
        break 
      else:
        Float = 0 #If their number is negative then the while loop starts again.
    except:
      Float = 0 #If the original value entered wasn't a float then the variable Float remains 0 and the while loop starts again.
  return Float #The user's float is returned at the end once they have entered a valid input.

#The function CheckInt is used to validate the integers the user enters when setting generation 0 values (Number of Generations).
#It takes the value "Statement", which is the statement which will be outputted to the user when setting each Generation 0 Value.
def CheckInt(Statement):
  while True: 
    Num = input(Statement) #The user inputs their reply to the statement outputted.
    try: 
      int(Num) 
      Integer = int(Num) #If the input is an integer then the variable Integer is assigned their integer.
      if Integer >= 0: #Checks if their integer is positive.
        break 
      else:
        Integer = 0 #If their number was negative then the while loop starts again.
    except:
      Integer = 0 #If the original value entered wasn't an integer then the variable Integer is assigned 0 and the while loop starts agin until they input an appropriate number.
  return Integer #The user's integer is returned once they've entered a valid input.


#The function CheckYesNo is used to check if the user has entered yes or no to the question concerning overwriting data if thee file they wish to export to already exists.
#It takes the value "Statement", which is the statement which will be outputted to the user when setting each Generation 0 Value.
def CheckYesNo(Statement):
  while True: 
    String = input(Statement)  
    String = String.lower() #Their input is put into LowerCase so that the program isn't case-sensitive.
    if String != "yes": #The program then checks if their input wasn't yes.
      if String != "no":
        String = "0" #If their input also was't "no" then their input wasn't a valid input, and the loop starts again until they input a valid choice.
      else:
        break #If their input was "no" then the while loop is stopped.
    else:
      break #If their input was "yes" then the while loop is stopped.
  return String #The user's string is returned at the end of the function.

#The function NotData is used to tell the user that they haven't inputted data yet.
#For example, if they haven't set Generation 0 Values but are trying to see them then this will be run.
#It would also be run if they tried to export data without running the model, as they wouldn't have data to export.
#It takes the value "Message", which is the error message which will be outputted to the user.
def NotData(Message):
  print(Message) 
  input("Press enter to return to the menu...") #It waits for the user to press enter before returning to the menu.
  os.system("clear") #It clears the screen.

#This function covers Task 2 of the program, where the user sets the Generation 0 values.
#At the end of the function it returns their Inputs in the form of an array, UserInputs.
def UserInput():
  JuvenileGeneration0 = CheckFloat("Juvenile Generation 0 Population (Thousands): " ) #Juvenile, Adult and Senile Generation 0 Populations are set, using the "CheckFloat" function to validate the inputs.
  AdultGeneration0 = CheckFloat("Adult Generation 0 Population (Thousands): ")
  SenileGeneration0 = CheckFloat("Senile Generation 0 Population (Thousands): ")
  JuvenileSurvival = CheckFloat("Juvenile Survival Rate (0 - 1): ") #Juvenile Survival Rate is set, using the "CheckFloat" function to validate the input.
  while JuvenileSurvival < 0 or JuvenileSurvival > 1: #As survival rate has to be between 0-1, if the Juvenile Survival Rate is outside these boundaries then the user will be asked to input the survival rate again until they enter a number between 0-1.
    JuvenileSurvival = CheckFloat("Juvenile Survival Rate (0 - 1): ")
  AdultSurvival = CheckFloat("Adult Survival Rate (0 - 1): ") #Adult Survival Rate is set, using the "CheckFloat" function to validate the input.
  while AdultSurvival < 0 or AdultSurvival > 1: #As survival rate has to be between 0-1, if the Adult Survival Rate is outside these boundaries then the user will be asked to input the survival rate again until they enter a number between 0-1.
    AdultSurvival = CheckFloat("Adult Survival Rate (0 - 1): ")
  SenileSurvival = CheckFloat("Senile Survival Rate (0 - 1): ") #Seniles Survival Rate is set, using the "CheckFloat" function to validate the input.
  while SenileSurvival < 0 or SenileSurvival > 1: #As survival rate has to be between 0-1, if the Senile Survival Rate is outside these boundaries then the user will be asked to input the survival rate again until they enter a number between 0-1.
    SenileSurvival = CheckFloat("Senile Survival Rate (0 - 1): ")
  BirthRate = CheckFloat("Birth Rate: ")  #Birth Rate is set, using the "CheckFloat" function to validate the input.
  NewGenerations = CheckInt("Number of New Generations (5 - 25): ") #Number of Generations is set, using the "CheckInt" function to validate the input.
  while NewGenerations < 5 or NewGenerations > 25: #As the number of new generations has to be between 0-1, if the Number of Generations is outside these boundaries then the user will be asked to input the Number of Generations again until they enter a number between 5-25.
    NewGenerations = CheckInt("Number of New Generations (5 - 25): ")
  DiseaseTriggerPoint = CheckFloat("Total Population Disease Trigger Point (Thousands): ") #The Disease Trigger Point is set, using the "CheckFloat" function to validate the input.
  UserInputs = [JuvenileGeneration0, AdultGeneration0, SenileGeneration0, JuvenileSurvival, AdultSurvival, SenileSurvival, BirthRate, NewGenerations, DiseaseTriggerPoint] #The array "UserInputs" is used to store all the data set by the user throughout this function (the Generation 0 Values).
  input("Press enter to return to the menu...") 
  os.system("clear") 
  return UserInputs #The data in UserInputs is returned for use later on in the program.

#This procedure covers Task 3 of the program, taking the values that generation 0 Values set by the users and then outputting each one to the user.
def DisplayChoice(Generation0Values):
  print("Juvenile Generation 0 Population (Thousands): " + str(Generation0Values[0]))
  print("Adult Generation 0 Population (Thousands): " + str(Generation0Values[1]))
  print("Senile Generation 0 Population (Thousands): " + str(Generation0Values[2]))
  print("Juvenile Survival Rate: " + str(Generation0Values[3]))
  print("Adult Survival Rate: " + str(Generation0Values[4]))
  print("Senile Survival Rate: " + str(Generation0Values[5]))
  print("Birth Rate: " + str(Generation0Values[6]))
  print("Number of New Generations: " + str(Generation0Values[7]))
  print("Total Population Disease Trigger Point (Thousands): " + str(Generation0Values[8]))
  input("Press enter to return to the menu...") 
  os.system("clear") 
 
#This function covers Task 4 and 6 of the program, running the model with disease once the Trigger Point has been reached (if the user chooses to run the model with disease) and outputting the various values to the user in the form of a table as the program is run.
#It takes the Generation 0 Values set by the user as an input and a value called "Disease", which is set at either 0, if the model is to be run without disease, or 1, if the model is to be run with disease.
def RunModel(Generation0Values,Disease):
  Juveniles = float(Generation0Values[0]) #First it extracts the data from the array Generation0Values and assigns the numbers to appropriately named variables.
  Adults = float(Generation0Values[1])
  Seniles = float(Generation0Values[2])
  JuvenileSurvival = float(Generation0Values[3])
  AdultSurvival = float(Generation0Values[4])
  SenileSurvival = float(Generation0Values[5])
  BirthRate = float(Generation0Values[6])
  NewGenerations = int(Generation0Values[7])
  DiseaseTriggerPoint = float(Generation0Values[8])
  if  Disease == 1 and DiseaseTriggerPoint == 0: #If the user is running the model with disease and has entered the Disease trigger Point as 0 then the program asks them to enter their choice again, to make sure they wanted disease taking effecting all the time.
    print("Your Total Population Disease Trigger Point is currently set at 0, if you wish to change this then you may now.")
    DiseaseTriggerPoint = CheckFloat("Total Population Disease Trigger Point (Thousands): ")
  Generation = 0
  TotPop = float(Juveniles + Adults + Seniles)
  FinishedValues = [[Generation],[Juveniles],[Adults],[Seniles],[TotPop]] #A multidimensional array called "FinishedValues" is made to store the values that the program generates as it runs.
  print("{0:20} {1:20} {2:20} {3:20} {4:20}".format("Generation", "Juveniles (Thousands)", "Adults (Thousands)", "Seniles (Thousands)", "Total Population (Thousands)")) #The program prints the table headers.
  while Generation <= NewGenerations: #A while loop is set to keep calculating the new numbers of species until the desired number of generations has been run.
    print("{0:20} {1:20} {2:20} {3:20} {4:20}".format(FinishedValues[0][Generation], FinishedValues[1][Generation], FinishedValues[2][Generation], FinishedValues[3][Generation], FinishedValues[4][Generation])) #At the start of each while loop the values from the last generation are added to the table in the appropriate columns
    PrevAdults = float(Adults) #PrevAdults is assigned then number of adults from the previous generation so that when the new number of adults is calculated this number is still available for calculating the number of Juveniles with.
    if Disease  == 0 or TotPop < DiseaseTriggerPoint: #If the Total Population is below the Disease Trigger Point or they are running the model without disease then the new values will be calculated using the appropriate formulae, the values calculated are then appended to the the suitable locations in "FinishedValues".
      FinishedValues[0].append(Generation + 1)
      Seniles = round(float((Seniles*SenileSurvival) + (PrevAdults*AdultSurvival)),3)
      FinishedValues[3].append(Seniles)
      Adults = round(float(Juveniles*JuvenileSurvival),3)
      FinishedValues[2].append(Adults)
      Juveniles = round(float(PrevAdults*BirthRate),3)
      FinishedValues[1].append(Juveniles)
      TotPop = round(float(Juveniles + Adults + Seniles),3)
      FinishedValues[4].append(TotPop)
      Generation += 1
    else: #If the Total Population is above the Disease Trigger Point, and the user is running the model with disease, then the new senile and juvenile values will be calculated using a Disease Factor (adults aren't affected by disease) and the values will then be appended to the suitable locations in "FinishedValues"
      FinishedValues[0].append(Generation + 1)
      DiseaseFactor = random.uniform(0.2,0.5) #The Disease Factor is assigned a random float between 0.2 and 0.5 inclusive.
      Seniles = round(float((Seniles*SenileSurvival*DiseaseFactor) + (PrevAdults*AdultSurvival)),3)
      FinishedValues[3].append(Seniles)
      Adults = round(float(Juveniles*JuvenileSurvival*DiseaseFactor),3)
      FinishedValues[2].append(Adults)
      Juveniles = round(float(PrevAdults*BirthRate),3)
      FinishedValues[1].append(Juveniles)
      TotPop = round(float(Juveniles + Adults + Seniles),3)
      FinishedValues[4].append(TotPop)
      Generation += 1
  input("Press enter to return to the menu...") 
  os.system("clear") 
  return FinishedValues #The numbers from each generation are returned so that they can be exported later in the program.

#This function covers Task 5 of the programme, taking the values calculated from the model and exporting them to an external file.
def ExportData(Generation0Values, FinishedData):
  NewGenerations = Generation0Values[7] 
  cont = False
  while cont == False:
    FileName = str(input("Please Enter a File Name to Export your Data to: ")) #The user enters a name for the file and if it doesn't have ".txt" extension then this is added.
    FinalFour = (len(FileName)) - 4
    FinalLetters = FileName[FinalFour:]
    if FinalLetters == ".txt":
      FileName = FileName
    else:
      FileName = FileName + ".txt"
    if os.path.isfile(FileName): #The programme checks if a file with the same name as that given exists, and if it does, asks them if they wish to overwrite the file.
      print("WARNING! File already exists under given name.") 
      overwrite = CheckYesNo("Do you wish to overwrite the current contents of the file (Yes / No)? ")
      if overwrite == "no":
        cont = False #If they don't want to overwrite the file then the while loop starts again.
      elif overwrite == "yes":
        break
    else:
      break
  f = open(FileName, "w")
  LoopUntil = NewGenerations + 1
  Loop = 0
  while Loop < LoopUntil: #A loop is set up to export the Population Values for each Generation until the number of Generations has been reached and all data is exported.
    f.write("Generation; " + str(FinishedData[0][Loop]) + "\n") #A semi-colon is used to split the strings from the numbers, so that a spreadsheet package such as excel can separate the values from the words.
    f.write("Juveniles (Thousands); " + str(FinishedData[1][Loop]) + "\n")
    f.write("Adults (Thousands); " + str(FinishedData[2][Loop]) + "\n")
    f.write("Seniles (Thousands); " + str(FinishedData[3][Loop]) + "\n")
    f.write("Total Population (Thousands); " + str(FinishedData[4][Loop]) + "\n")
    f.write("\n")
    Loop += 1
  print("Data exported to file.")
  input("Press enter to return to the menu...")
  os.system("clear")

#This procedure is used to terminate the program if the user wishes to "Quit".
def Quit():
  print("Program Terminated...")
  sys.exit()

#This function covers Task 1, the Main Menu, and is the function from which all others are run.
def Main():
  os.system("clear") #The screen is cleared and two empty arrays are set up to store the Generation 0 Values and the Data once the model has been run.
  Generation0Values = []
  FinishedData = []
  while True:
    print("Welcome to the Population Model Menu, please enter the number assigned to you choice below:") #The choices are outputted and the user inputs their choice.
    choices = {1 : "[1] Set Generation 0 Values", 2 : "[2] Display Generation 0 Values", 3 : "[3] Run Model Without Disease", 4 : "[4] Run Model With Disease", 5 : "[5] Export Data", 6 : "[6] Quit"}
    functions = {1 : UserInput, 2 : DisplayChoice, 3 : RunModel, 4 : RunModel, 5 : ExportData, 6 : Quit}
    for i in range (1,(len(choices)) + 1):
      print(choices[i])
    UserChoice = CheckInt("Choice: ")
    while UserChoice < 1 or UserChoice > 6: #They're asked to input their choice until it is between 1-6, the desired range.
      UserChoice = CheckInt("Choice: ")
    else:
      os.system("clear") #The program then runs the function in the dictionary "function" which has a key of the number they entered, with each function getting supplied with the relevant data and its "returned" data getting stored in the blank array declared outside the while loop.
      if UserChoice == 1:
        Generation0Values = functions[UserChoice]()
      elif UserChoice == 2 and not Generation0Values: #The program checks to make sure they have inputted data before running the functions where inputted data is necessary.
        NotData("No Generation 0 Values Set to Display, Set Generation 0 Values by Choosing [1] at the Menu.")
      elif UserChoice == 2:
        functions[UserChoice](Generation0Values)
      elif UserChoice == 3 and not Generation0Values or UserChoice == 4 and not Generation0Values:
        NotData("No Generation 0 Values Set to Run the Program with, Set Generation 0 Values by Choosing [1] at the Menu. ")
      elif UserChoice == 3:
        FinishedData = functions[UserChoice](Generation0Values, 0) #The number "0" tells the function "RunModel" that they are running the model without disease.
      elif UserChoice == 4:
        FinishedData = functions[UserChoice](Generation0Values, 1) #The number "1" tells the function "RunModel" that they are running the model with disease.
      elif UserChoice == 5 and not FinishedData:
        NotData("No Data to Export, Obtain Data by Running the Model by Choosing either Option 3 or Option 4 at the Menu.")
      elif UserChoice == 5:
        functions[UserChoice](Generation0Values, FinishedData)
      elif UserChoice == 6:
        functions[UserChoice]() #Once each function has been run, the program clears the screen and returns to the menu until they choose to quit.
  
#Entry Point
Main()
