a = input('Enter your surname here: ')
name = upper(a)

Surnames = {
    'ADEBOR': 0,
    'ADUEYE':1,
    'AKUSU':2,
    'AMUAMUZIA':3,
    'BALOGUN':4,
    'BENYEGOR': 5
}

First_name =['john','Peter','mary','paul','agnes','Listel']

matric_no = [
    'FOS/17/18/248957',
    'FOS/16/17/243815',
    'FOS/16/17/242888',
    'FOS/16/17/241138',
    'FOS/16/17/240620',
    'FOS/16/17/239310'
]

Courses= ['CSC 201', 'CSC 202', 'CSC 203', 'CSC 204' ]
Units = [ 2,2, 3, 1]
Scores=[
    [75, 50, 66, 44],
    [40, 76, 49, 64],
    [55, 60, 70, 58],
    [88, 70, 79, 70],
    [62, 60, 51, 46],
    [90, 76, 80, 61]
]



def student_info(name):
    for surname, no in Surnames.items():
        if name in surname:
            w = no
    print(f"\nFull name of student is {name} {First_name[w]}.")
    print(f"Your matric number is {matric_no[w]}.")
    scores = Scores[w] 
    x = [0, 1, 2 ,3]
    print(f"\nYour score in {Courses[x[0]]}, a {Units[x[0]]}-units course is {scores[0]}")
    print(f"Your score in {Courses[x[1]]}, a {Units[x[1]]}-units course is {scores[1]}")
    print(f"Your score in {Courses[x[2]]}, a {Units[x[2]]}-units course is {scores[2]}")
    print(f"Your score in {Courses[x[3]]}, a {Units[x[3]]}-units course is {scores[3]}")
    gpa = []
    for score in scores:
        if score > 70:
            gpa.append(5)
        elif score >60:
            gpa.append(4)
        elif score >50:
            gpa.append(3)
        elif score >40:
            gpa.append(2)
        else:
            gpa.append(1)

    
    gpa_ = []
    y = -1
    while y<3:
        y+= 1
        my_gpa= (gpa[y] *Units[x[y]])
        gpa_.append(my_gpa)
    a = sum(gpa_)/ sum(Units)
    print(f'\nYour gpa is {a}')

    


student_info(name)