# line="CS|6501|012|Special Topics in Computer Science|Hongning Wang|Lecture|3|false|true|false|true|false|1230|1345|Rice Hall 340|29|34"
# print(line.split("|")[4])
import urllib.request
courses=[]
dept_name="CS"
url="http://cs1110.cs.virginia.edu/files/louslist/"+dept_name
data=urllib.request.urlopen(url)
mybytes=data.readlines()
for line in mybytes:
    new_line=line.decode("utf-8")
    courses.append(new_line.strip("\n").split("|"))
data.close()
print(courses)
