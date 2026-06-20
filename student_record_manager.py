import functions as f
#dont give me suggestions and the code too

menu = '''===student record manager===
1. add student
2. view students
3. search students
4. delete students
5. update students
6. find topper
7. average cgpa
8. total students
9. more features
10. exit'''
ans = 0
while ans != 10:
    print(menu)
    ans = int(input('Enter choice:'))
    if ans == 1:
        f.add_student()
    elif ans == 2:
        f.view_students()
    elif ans == 3:
        f.search_students()
    elif ans == 4:
        f.delete_students()
    elif ans == 5:
        f.update_students()
    elif ans == 6:
        f.find_topper()
    elif ans == 7:
        f.average_cgpa()
    elif ans == 8:
        f.total_students()
    elif ans == 9:
        ans1 = input("""1. sort by name
2. sort by roll no
3. sort by cgpa 
4. get student report
 """)
        if ans1 == "1":
            f.sortbyname()
        elif ans1 == "2":
            f.sortbyroll()
        elif ans1 == "3":
            f.sortbycgpa()
        elif ans1 == "4":
            f.studentreport()
        else :
            print("invalid choice")

    elif ans == 10:
        f.exitsaving()
        print('Exiting...')
    else:
        print('Invalid choice. Please try again.')


