def dic():
    DobStudents = {"ADAM": "27 Dec, 2001",
                   "ABRAHAM": "18 Aug, 2004",
                   "DANIEL": "15 Jun, 2002",
                   "JACK": "12 Jul, 2004",
                   "VERONIKA": "29 Sep, 2006",
                   "CASSANDRA": "23 Nov, 2002"}

    name = input("Input persons name: ")
    if name.upper() in DobStudents:
        print("Dob of "+name+" is "+DobStudents[name.upper()])
    else:
        print("no")
        new_person = input("Would you like to create a new entry? (y or n)")
        if new_person =="y":

            new_person_dob = input("Enter new DoB:")
            newDob = {name.upper(): new_person_dob}
            DobStudents.update(newDob)
            print(newDob)
            print(DobStudents)


dic()