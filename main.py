file_name = "student.txt"
file1 = open(file_name, "a")
file1.close


def show_main_menu():
    print("\n   *** student Menu ***\n"+
          "Enter 1,2,3 or 4:\n"+
          "Enter 1 To Display Your Students Records\n" +
          "Enter 2 To Add a New Student Record\n"+
          "Enter 3 To search your students\n"+
          "Enter 4 To Quit\n**********************")
    choice = input("Enter your choice: ")
    if choice == "1":
        file1 = open(file_name, "r")
        file_students = file1.read()
        if len(file_students) == 0:
            print("students menu is empty")
        else:
            print (file_students)
        file1.close
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "2":
        enter_student_record()
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "3":
        search_student_record()
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice== "4":
        print("Thanks for using student menu's ")
              
    else:
        print("Wrong choice, Please Enter [1 to 4]\n")
        ent = input("Press Enter to continue ...")
        show_main_menu()
        
def search_student_record():
    search_name = input("Enter First name for Searching student record: ")
    rem_name = search_name[1:]
    first_char = search_name[0]
    search_name = first_char.upper() + rem_name
    file1 = open(file_name, "r")
    file_students = file1.readlines()
     
    found = False   
    for line in file_students:
        if search_name in line:
            print("Your Required Student Record is:", end=" ")
            print (line)
            found=True
            break
    if  found == False:
        print("There's no student Record in menu with name = " + search_name )
        

def input_fname():
    fname = input("Enter First name ")
    rem_fname = fname[1:]
    first_char = fname[0]
    return first_char.upper() + rem_fname

def input_lname():
    lname = input("Enter Last name ")
    rem_lname = lname[1:]
    first_char = lname[0]
    return first_char.upper() + rem_lname


def enter_student_record():
    first = input_fname()
    last = input_lname()
    score = input('Enter score ')
    student= ("[" + first + " " + last + ", " + score + "]\n")
    file1 = open(file_name, "a")
    file1.write(student)
    print( "This student\n " + student + "has been added successfully!")
    


show_main_menu()


#Elahe Eslami (project) 
