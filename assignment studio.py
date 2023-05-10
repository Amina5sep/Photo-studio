# -------------------------------------------------CODE HUNTERS -------------------------------------------------------
# -----------------AMINA HABIB
# ------------------SAMREEN FATIMA
# -------------------------LINTA ASHFAQ
# -------------------------------NOOR ZAHRA
# ----------------------------------NADIA NOOR
# ----------------------------------TAQADUS FATIMA

print("WELCOME TO")
print("BRYANT ROTHMOORE STUDIO")


class Studio:
    def __init__(self, school, weddingevents, casual):
        self.school = school
        self.weddingevents = weddingevents
        self.casual = casual
while True:
    b = input("Press any key to visit our site")
    print("press 1 if you want school function photography   ")
    print(" press 2 if you want wedding photography")
    print(" press 3 if you want formal function photography")
    print("press 4 to get online tutorials of our experts")
    print("press 5 if you want to get physical classes ")
    print("press 6 to exit")
    a = int(input("Enter your choice "))

    obj1 = Studio("*****************photoshoot for schools and colleges*************888", "***********photoshoot for wedding cerimonys and engagments***********88",
                 "**************888photoshoot for formal functions***************")
    if a == 1:
        print(obj1.school)
        print("We are here to provide our services  ")
        print("           We charge 20k/- per hour")
        print("                           If you heir us for consecutive two day we will offer you discount of 20 %")
    if a == 2:
        print(obj1.weddingevents)
        print("3 days event coverage + on location photoshoot (limited)  ")
        print("3 printed books of events ")
        print("100 pics/ each book per days package 35000/- which include one digital album and ")
        print("3 photographs (1 portrait ,1 canted, 1 wide angled ) ")

    if a == 3:
        print(obj1.casual)
        print(" Photography with drones , DSLR ,video graphy jib,ronin and smd screen")
        print("We are here to save your beautiful memories forever")
        print("We charge 5000/- per hour for casual functions  ")


    class Course(Studio): #child class of studio
        def __init__(self, online, physical):
            self.online = online
            self.physical = physical


    obj2 = Course("*********online tutorial**************", "*********physical course*****************")
    if a == 4:
        print(obj2.online)
        print("To learn skill about photography click on the link given below")
        print("www.photographystudio/photographyskills/equipments.com")
    if a == 5:
        print(obj2.physical)
        print("For physical classes ")
        print("        our team is available from monday to thursday ")
        print("                 from 9am to 1 pm ")
        print("                           |location : MNSUAM JESMINE COURTS| ")

    if a == 6:
        break


