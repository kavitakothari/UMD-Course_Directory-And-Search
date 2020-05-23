# Team members: Kavita Kothari, Rachel Kim, Isaac Macarthy
# Project: Searching through courses offered at the University of Maryland

import requests


def get_course_names(course):
    """
    Returns the list of courses from the specified department

    Args:
        course(String): The link constructed with the department ID

    """
    response = requests.get(course)
    response_json = response.json()
    for courses in response_json:
        for keys, vals in courses.items():
            if keys == 'course_id':
                print(vals)
    return


def get_prereqs(course):
    """
    Returns the prerequisites needed to take a specific course

    Args:
        course(String): The link constructed with the course name
    """
    response = requests.get(course)
    response_json = response.json()
    for keys, vals in response_json.items():
        if keys == 'relationships':
            for items, values in vals.items():
                if items == 'prereqs':
                    print(values)
    return


def get_video_page_urls(course):
    """
    Returns all information about all courses from a specified department

    Args:
        course(String): The link constructed with the department ID
    """
    response = requests.get(course)
    response_json =  response.json()
    for courses in response_json:
        print("-------------------------------------------------")
        for keys, vals in courses.items():
            print(keys + ":", vals)
    return


def get_geneds(course):
    """
    Returns whether a course satisfies any GenEd requirements

    Args:
        course(String): The link constructed with the course name
    """
    response = requests.get(course)
    response_json = response.json()
    for keys, vals in response_json.items():
        if keys == 'gen_ed':
            if len(vals) == 0:
                print('None')
            else:
                for items in vals:
                    print(items)
    return


def get_dept_list(index):
    """
    Returns the entire list of departments at UMD

    Args:
        index(String): The link from which the data is being pulled
    """
    response = requests.get(index)
    response_json = response.json()
    for items in response_json:
        for keys, vals in items.items():
            if keys == 'department':
                print(vals)

def get_section(section):
    """
        Returns information about specific sections for courses at UMD

        Args:
            section(String): The link associated with data from the courses,
            with the section information
        """
    response = requests.get(section)
    response_json = response.json()

    for sections in response_json:
        for keys, vals in sections.items():
            print(keys, vals)


def get_user_input():
    """
    Displays a menu of options and calls various functions based on the users
    input
    """
    flag = 1
    print("Welcome! What would you like to do? ")
    while flag != 0:
        print("1. List the names of all courses from a specific department")
        print("2. List prerequisites for a specific course")
        print("3. Print all the information available for all courses in a "
              "specific department")
        print("4. List which GenEds the course satisfies, if any")
        print('5. Get a list of all the departments at UMD')
        print('6. Get the section information of any specified course at UMD')
        print("Press 0 to exit the program.")
        num = int(input("Enter the index number of the action you want to "
                        "perform: "))

        if num == 0:
            flag = 0

        if num == 1:
            dept = input("Enter department ID: ")
            root_url = 'https://api.umd.io'
            index_url = root_url + '/v0/courses?dept_id=' + dept
            print("The courses in the %s department are: " % dept)
            get_course_names(index_url)

        if num == 2:
            course_name = input("Enter course name: ")
            root_url = 'https://api.umd.io'
            index_url = root_url + '/v0/courses/'+course_name
            print("The prerequisites for %s are: "%course_name)
            get_prereqs(index_url)

        if num == 3:
            dept = input("Enter department ID: ")
            root_url = 'https://api.umd.io'
            index_url = root_url + '/v0/courses?dept_id=' + dept
            get_video_page_urls(index_url)

        if num == 4:
            course_name = input("Enter course name: ")
            root_url = 'https://api.umd.io'
            index_url = root_url + '/v0/courses/'+course_name
            print("The GenEds %s satisfies are: "%course_name)
            get_geneds(index_url)

        if num == 5:
            index_url = "https://api.umd.io/v0/courses/departments"
            print('The list of departments at UMD is: ')
            get_dept_list(index_url)

        if num == 6:
            sect = input("Enter course name with section number ")
            index_url = "https://api.umd.io/v0/courses/sections?section_id=" +sect
            print('The section ID of a specified course at UMD: ')
            get_section(index_url)


if __name__ == '__main__':
    get_user_input()