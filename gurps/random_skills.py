from random import sample, choice
from library_parser import *

SKILLS = list()

for s in library['skills']:
    SKILLS.append(
        (s.find("name").text,
        s.find("difficulty").text,
        s.find("reference").text ))
        #[_.text for _ in s.find("categories").findall("category")]
        #))

if __name__ == "__main__":
    for skill in sample(SKILLS, 5):
        print ("%-20s %5s %5s" % skill)
    
