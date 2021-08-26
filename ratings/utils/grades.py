import requests
from bs4 import BeautifulSoup
import re

def get_valid_courses(courses):
    matches = re.findall(r"([A-Za-z]+) ?([0-9]{4})", courses)
    return [match[0].upper() + " " + match[1] for match in matches]

def findInfo(courses):
    ret = []
    for course in get_valid_courses(courses):
        url = "https://c4citk6s9k.execute-api.us-east-1.amazonaws.com/test/data/course?courseID=" + course.replace(" ", "%20")
        r = requests.get(url)
        j = r.json()
        if (j["header"][0]["full_name"]):
            if (j["header"][0]["avg_a"] < 30):
                ret.append("%s is a difficult class." % course)
            elif (j["header"][0]["avg_a"] < 50):
                ret.append("%s is a moderate class." % course)
            else:
                ret.append("%s is an easy class." % course)
        else:
            ret.append("Error: No data available for %s" % course)
    return ret
