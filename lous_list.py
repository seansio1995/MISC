import urllib.request
def instructors(department):
    instructor_names=[]
    url="http://cs1110.cs.virginia.edu/files/louslist/"+department
    data=urllib.request.urlopen(url)
    mybytes=data.readlines()
    for line in mybytes:
        new_line=line.decode("utf-8")
        instructor_names.append(new_line.strip("\n").split("|")[4])
    data.close()
    names_set=set(instructor_names)
    instructor_names=list(names_set)
    instructor_names=[name for name in instructor_names if "+" not in name]
    instructor_names=sorted(instructor_names)
    return instructor_names

def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    courses=[]
    url="http://cs1110.cs.virginia.edu/files/louslist/"+dept_name
    data=urllib.request.urlopen(url)
    mybytes=data.readlines()
    for line in mybytes:
        new_line=line.decode("utf-8")
        courses.append(new_line.strip("\n").split("|"))
    data.close()
    if has_seats_available:
        courses=[course for course in courses if int(course[15])<int(course[16])]
    if level is not None:
        courses=[course for course in courses if course[1][0]==str(level)[0]]
    if not_before is not None:
        courses=[course for course in courses if int(course[12])>=not_before]
    if not_after is not None:
        courses=[course for course in courses if int(course[12])<=not_after]
    return courses



# print(instructors("CS"))
# print("\n")
# print(instructors("MATH"))
