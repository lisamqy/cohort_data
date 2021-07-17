"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    file = open(filename)

    houses = set()
    for line in file:
      line = line.rstrip() #remove all the white spaces to the right
      student_record = line.split("|") #split into a list
      if student_record[2]:
        houses.add(student_record[2])

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []
    file = open(filename)

    for line in file:
      line = line.rstrip() #remove all the white spaces to the right
      student_record = line.split("|") #split into a list
      
      if cohort == student_record[4]:
        student_name = student_record[0]+ " " + student_record[1]
        students.append(student_name)
      elif cohort == "All":
        if len(student_record[4]) > 1:
          student_name = student_record[0]+ " " + student_record[1]
          students.append(student_name)
      
    
    return sorted(students)
    


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    # roster= []

    file = open(filename)

    for line in file:
      line = line.rstrip() #remove all the white spaces to the right
      student_record = line.split("|") #split into a list
      
      if student_record[2] == "Dumbledore's Army":
        name = student_record[0]+ " " + student_record[1]
        dumbledores_army.append(name)
        dumbledores_army.sort()
      elif student_record[2] == "Gryffindor":
        name = student_record[0]+ " " + student_record[1]
        gryffindor.append(name)
        gryffindor.sort()
      elif student_record[2] == "Hufflepuff":
        name = student_record[0]+ " " + student_record[1]
        hufflepuff.append(name)
        hufflepuff.sort()
      elif student_record[2] == "Ravenclaw":
        name = student_record[0]+ " " + student_record[1]
        ravenclaw.append(name)
        ravenclaw.sort()
      elif student_record[2] == "Slytherin":
        name = student_record[0]+ " " + student_record[1]
        slytherin.append(name)
        slytherin.sort()
      elif student_record[4] == "G":
        name = student_record[0]+ " " + student_record[1]
        ghosts.append(name)
        ghosts.sort()
      elif student_record[4] == "I":
        name = student_record[0]+ " " + student_record[1]
        instructors.append(name)
        instructors.sort()
      
    return [dumbledores_army, gryffindor, hufflepuff, ravenclaw, slytherin, ghosts, instructors]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    file = open(filename)

    for line in file:
      line = line.rstrip() #remove all the white spaces to the right
      student_record = line.split("|") #split into a list

      # if student_record[3] != "":
      name = student_record[0]+ " " + student_record[1]
      house = student_record[2]
      advisor = student_record[3]
      cohort = student_record[4]
      all_data.extend([(name, house, advisor, cohort)])

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    file = open(filename)

    for line in file:
      line = line.rstrip() #remove all the white spaces to the right
      student_record = line.split("|") #split into a list

      student_name = student_record[0]+ " " + student_record[1]
      if student_name == name:
        return student_record[4]
      



def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    
    dupe = set()


    last_names = []

    file = open(filename)

    for line in file:
      line = line.rstrip() #remove all the white spaces to the right
      student_record = line.split("|") #split into a list

      last_names.append(student_record[1]) #put all last names in the list

      for lname in last_names: 
        if last_names.count(lname)>1:
          dupe.add(lname)

    return dupe




def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    house = ""
    cohort= ""
    housemate = []

    file = open(filename)

    for line in file:
      line = line.rstrip() #remove all the white spaces to the right
      student_record = line.split("|") #split into a list

      student_name = student_record[0]+ " " + student_record[1]

      if name == student_name:
        house = student_record[2]
        cohort = student_record[4]

    file.seek(0)

    for line in file:
      line = line.rstrip() #remove all the white spaces to the right
      student_record_two = line.split("|") #split into a list

      student_name = student_record_two[0]+ " " + student_record_two[1]
      if (house == student_record_two[2]) and (cohort == student_record_two[4]) and (name != student_name):
        

        housemate.append(student_name)

    housemate = set(housemate)
    return housemate




##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
