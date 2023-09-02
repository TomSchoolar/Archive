import random
import time

NumbersOfPets=''
Pet=''
PetList=['Cow','Pig','Sheep','Chicken']
OwnedPetsList=[]
Barn=[]
YesOrNo=''
MilkOrBaconOrEggOrWool=''
WhatYouDo=''
Level=1
Limit=2
WhatToMake=''
Money=10
WhatToGrow=''
LevelUp=0
FishCount={'Cod':0,'Salmon':0,'Haddock':0,'Trout':0}
FishList=['Cod','Salmon']

def Market():
    global Money
    if Money>4:
        print('Welcome To The Market')
        print('Your Balence is \xA3'+str(Money))
        q=True
        while len(OwnedPetsList) < Limit and Money>4.5 and q==True:
            NumbersOfPets=len(PetList)
            Pet=PetList[random.randint(0,NumbersOfPets-1)]
            answar=Input("Shopkepper: "+Pet+" For Sale "+Pet+' For Sale'+'\n'+'Buy the '+Pet+'?\n It costs \xA35').lower()
            if answar.lower()=='buy':
                Money=Money-5
                OwnedPetsList.append(Pet)
                print('Your Animals '+str(OwnedPetsList))
                print('Your Balence is \xA3'+str(Money))
            if answar.lower()=='quit':
                q=False
        if len(OwnedPetsList)==Limit or Money<4.5 or q==False:
            print('The Shopkepper has no other animals to sell today!')
            print('Come again soon')
        return

def Collect(Animal):
    if len(OwnedPetsList)>0:
        if OwnedPetsList[Animal]=='Cow':
            MilkOrBaconOrEggOrWool='Milk'
        if OwnedPetsList[Animal]=='Pig':
            MilkOrBaconOrEggOrWool='Bacon'
        if OwnedPetsList[Animal]=='Chicken':
            MilkOrBaconOrEggOrWool='Eggs'
        if OwnedPetsList[Animal]=='Sheep':
            MilkOrBaconOrEggOrWool='Wool'
        if OwnedPetsList[Animal]=='Goat':
            MilkOrBaconOrEggOrWool="Goat's Milk"
        WhatYouDo=Input('Do you want to collect Your '+MilkOrBaconOrEggOrWool+" \nYes\nNo").lower()
        if WhatYouDo=='yes':
            if OwnedPetsList[Animal]=='Pig':
                OwnedPetsList.pop(Animal)
            print('You Got it',True)
            Barn.append(MilkOrBaconOrEggOrWool)
            print('Your Barn Contains '+str(Barn))
            print('Your Animals '+str(OwnedPetsList))
    return

def Produce():
    global LevelUp
    global Money
    WhatToMake=Input("What do you want to make? \nBacon and Eggs\nWooly hat\nYoghurt\nFeta\nBread\nPopcorn\nFish and Chips\nSushi").lower()
    if WhatToMake=='bacon and eggs':
        if Barn.count('Bacon')>0:
            if Barn.count('Eggs')>0:
                print('Bacon and Eggs ready in 5 seconds')
                Barn.pop(Barn.index('Bacon'))
                Barn.pop(Barn.index('Eggs'))
                Barn.append('Bacon and Eggs')
                time.sleep(5)
                print('Bacon and Eggs ready!')
                print('Your Barn Contains '+str(Barn))
            else:
                print('You need Eggs')
        else:
            print('You need Bacon')
    if WhatToMake=='wooly hat':
        if Barn.count('Wool')>0:
            print('Wooly hat ready in 7 seconds')
            Barn.pop(Barn.index('Wool'))
            Barn.append('Wooly hat')
            time.sleep(7)
            print('Wooly hat ready!')
            print('Your Barn Contains '+str(Barn))
        else:
            print('You need Wool') #_______________________________________
    if WhatToMake=='yoghurt':
        if Barn.count('Milk')>0:
            print('Yoghurt ready in 2 seconds')
            Barn.pop(Barn.index('Milk'))
            Barn.append('Yoghurt')
            time.sleep(2)
            print('Yoghurt ready!')
            print('Your Barn Contains '+str(Barn))
        else:
            print('You need Milk')
    if WhatToMake=='feta':
        if Barn.count("Goat's Milk")>0:
            print('Feta ready in 4 seconds')
            Barn.pop(Barn.index("Goat's Milk"))
            Barn.append('Feta')
            time.sleep(4)
            print('Feta ready!')
            print('Your Barn Contains '+str(Barn))
        else:
            print("You need Goat's Milk")
    if WhatToMake=='bread':
        if Barn.count('Wheat')>0:
            print('Bread ready in 5 seconds')
            Barn.pop(Barn.index('Wheat'))
            Barn.append('Bread')
            time.sleep(5)
            print('Bread ready!')
            print('Your Barn Contains '+str(Barn))
            if Level==3:
                LevelUp=1
        else:
            if Level<3:
                print('Crop Products open at Level 3')
            else:
                print('You need Wheat')
    if WhatToMake=='popcorn':
        if Barn.count('Corn')>0:
            print('Popcorn ready in 6 seconds')
            Barn.pop(Barn.index('Corn'))
            Barn.append('Popcorn')
            time.sleep(6)
            print('Popcorn ready!')
            print('Your Barn Contains '+str(Barn))
            if Level==3:
                LevelUp=1
        else:
            if Level<3:
                print('Crop Products open at Level 3')
            else:
                print('You need Corn')
    if WhatToMake=='fish and chips':
        if Level>3:
            if Barn.count('Cod')>0:
                if Barn.count('Potato')>0:
                    print('Fish n Chips ready in 4 seconds')
                    Barn.pop(Barn.index('Potato'))
                    Barn.pop(Barn.index('Cod'))
                    Barn.append('Fish n Chips')
                    time.sleep(4)
                    print('Fish n Chips ready!')
                    print('Your Barn Contains '+str(Barn))
                    LevelUp=2
                else:
                    print('You need Potato')
            else:
                print('You need Cod')
        else:
            print('Fish n Chips unlocks at Level 4')
    if WhatToMake=='sushi':
        if Level>3:
            if Barn.count('Salmon')>0:
                if Barn.count('Rice')>0:
                    print('Sushi ready in 5 seconds')
                    Barn.pop(Barn.index('Salmon'))
                    Barn.pop(Barn.index('Rice'))
                    Barn.append('Sushi')
                    time.sleep(5)
                    print('Sushi ready!')
                    print('Your Barn Contains '+str(Barn))
                    LevelUp=2
                else:
                    print('You need Rice')
            else:
                print('You need Salmon')
        else:
            print('Sushi unlocks at Level 4')
        return

def Grow():
    print('Wheat = 3 seconds')
    print('Corn = 4 seconds')
    if Level>3:
        print('Potato = 2 seconds')
        print('Rice = 4 seconds')
    WhatToGrow=Input('What do you want to Grow?').lower()
    if WhatToGrow=='wheat':
        print(str(Barn))
        print('Wheat will be ready in 3 seconds')
        time.sleep(3)
        Barn.append('Wheat')
        print('Your Barn Contains '+str(Barn))
    if WhatToGrow=='corn':
        print(str(Barn))
        print('Corn will be ready in 4 seconds')
        time.sleep(4)
        Barn.append('Corn')
        print('Your Barn Contains '+str(Barn))
    if WhatToGrow=='potato':
        if Level>3:
            print(str(Barn))
            print('Potato will be ready in 2 seconds')
            time.sleep(2)
            Barn.append('Potato')
            print('Your Barn Contains '+str(Barn))
        else:
            print('Potatos unlocks at Level 4')
    if WhatToGrow=='rice':
        if Level>3:
            print(str(Barn))
            print('Rice will be ready in 4 seconds')
            time.sleep(4)
            Barn.append('Rice')
            print('Your Barn Contains '+str(Barn))
        else:
            print('Rice unlocks at Level 4')
    return

def Fishing():
    global FishList
    global FishCount
    NumberOfFish=len(FishList)
    print('You Could catch a '+str(FishList))
    print('Fishing...')
    time.sleep(2)
    if random.randint(1,10)<5:
        print("You didn't catch anything today!")
    else:
        Fish=FishList[random.randint(0,NumberOfFish-1)]
        print('You caught a '+Fish+'!')
        Barn.append(Fish)
        print('Your Barn Contains '+str(Barn))
        if Fish=='Cod':
            FishCount['Cod']=FishCount['Cod']+1
            print(str(FishCount))
        if Fish=='Salmon':
            FishCount['Salmon']=FishCount['Salmon']+1
            print(str(FishCount))
        if Fish=='Haddock':
            FishCount['Haddock']=FishCount['Haddock']+1
            print(str(FishCount))
        if Fish=='Trout':
            FishCount['Trout']=FishCount['Trout']+1
            print(str(FishCount))
    return

def Sell():
    global Barn
    global Money

    while True:
        print("Your Barn Contains "+str(Barn))
        WhatToSell = Input("What would you like to sell?")
        counter = 0
        boolean = False
        for item in Barn:
            if item.lower() == WhatToSell.lower():
                boolean = True
                break
            else:
                counter = counter + 1
        if boolean:
            Barn.pop(counter)
            Money = Money + 25
            print('Your Balence is \xA3' +str(Money))
            break
        else:
            print("Item not in Barn")
    return

def Input(text):
    print("---")
    return input(text)

def Save():
    savefile=open('animals.txt','w')
    SaveLine = ''
    for animals in OwnedPetsList:
        SaveLine = SaveLine + animals + ','
    savefile.writelines(SaveLine)
    savefile.write('\n')
    SaveLine = ''
    for animals in Barn:
        SaveLine = SaveLine + animals + ','
    savefile.writelines(SaveLine)
    savefile.write('\n')
    savefile.write(str(Level))
    savefile.write('\n')
    savefile.write(str(Money))
    savefile.write('\n')
    savefile.write(str(FishCount['Cod']))
    savefile.write(',')
    savefile.write(str(FishCount['Salmon']))
    savefile.write(',')
    savefile.write(str(FishCount['Haddock']))
    savefile.write(',')
    savefile.write(str(FishCount['Trout']))
    savefile.write(',')
    savefile.close()
    return

print('Welcome to Hay Day In Python')
var=Input('Would you like to open a save?\n').lower()
if var =="yes":
    print('Loading...')
    try:
        line=''
        savefile=open('animals.txt','r')
        line=savefile.readline()
        line = line[:-2]
        OwnedPetsList=line.split(',')
        line=savefile.readline()
        line = line[:-2]
        Barn=line.split(',')
        line=savefile.readline()
        line = line[:-1]
        Level=int(line)
        line=savefile.readline()
        Money=int(line)
        line=savefile.readline()
        line = line[:-1]
        FishCount['Cod']=int(line[0])
        FishCount['Salmon']=int(line[2])
        FishCount['Haddock']=int(line[4])
        FishCount['Trout']=int(line[6])
        savefile.close()
        if Level>1:
            Limit=4
            PetList.append('Goat')
        if Level>4:
            FishList.append('Haddock')
            FishList.append('Trout')
        print('Loading Sucsessfull!')
        print('Your Animals '+str(OwnedPetsList))
        print('Your Barn contains '+str(Barn))
        print('Level '+str(Level))
        print('Your Balence is \xA3'+str(Money))
        print(str(FishCount))
    except IOError:
        print('No save Found')

while True:
    if Level==1:
        print('To Get to level 2 Collect Products from your animals')
    YesOrNo=Input("What Would you like to do? \n\nMarket (Level 1)\nCollect (Level 1)\nProduce (Level 2)\nSell (Level 2)\nGrow (Level 3)\nFish (Level 4)\n")
    YesOrNo=YesOrNo.lower()
    if YesOrNo=='collect':
        if len(OwnedPetsList)>0:
            for x in range (len(OwnedPetsList),0,-1):
                Collect(x-1)
        else:
            print("You don't own any animals Yet Go to the market to get animals")
    if YesOrNo=='market':
        Market()
    if YesOrNo=='produce':
        if Level==1:
            print('Producing Unlockes at Level 2')
        else:
            Produce()
    if YesOrNo=='sell':
        if Level == 1:
            print('Selling Unlockes at Level 2')
        else:
            Sell()
    if YesOrNo=='grow':
        if Level>2:
            Grow()
        else:
            print('Growing Unlockes at Level 3')
    if YesOrNo=='fish':
        if Level>3:
            Fishing()
        else:
            print('Fishing Unlockes at Level 4')
    if YesOrNo=='quit':
        if Input('Would you like to save?').lower()=='yes':
            Save()
        break
    if len(Barn)>0 and Level==1:
        Level=2
        print('Level '+str(Level))
        PetList.append('Goat')
        print('You Have unlocked the Goat')
        print('You Have unlocked Producing ')
        Limit=Limit+2
        print('You Can store 2 more Animals')
        print('To Get to level 3 Produce an item')
    if Money>0 and Level==2:
        Level=3
        print('Level '+str(Level))
        print('You can Grow Wheat')
        print('You can make Bread')
        print('You can Grow Corn')
        print('You can make Popcorn')
        print('To Get to level 4 Make a product from a growable item')
    if LevelUp==1:
        Level=4
        LevelUp=0
        print('Level '+str(Level))
        print('You Have unlocked the Fishing')
        print('You can Grow Potatos')
        print('You can make Fish n Chips')
        print('You can Grow Rice')
        print('You can make Sushi')
        print('To Get to level 5 produce something using fish')
    if LevelUp==2:
        Level=5
        LevelUp=0
        print('Level '+str(Level))
        print('Try to get all the fish')
        FishList.append('Haddock')
        FishList.append('Trout')
    if Level==5:
        if FishCount['Cod']>0:
            if FishCount['Salmon']>0:
                if FishCount['Haddock']>0:
                    if FishCount['Trout']>0:
                        Level=6
                        FishList.append('Carp')
                        Save()
                        break
