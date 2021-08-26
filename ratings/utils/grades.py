import requests
from bs4 import BeautifulSoup

def findInfo(courses):
    ret = []
    for course in courses.split(","):
        if (not course.strip()):
            ret.append("Error: Invalid code %s" % course)
            continue
        code = course.strip().upper()
        url = "https://c4citk6s9k.execute-api.us-east-1.amazonaws.com/test/data/course?courseID=" + code.replace(" ", "%20")

        r = requests.get(url)

        j = r.json()
        if (j["header"][0]["full_name"]):
            if (j["header"][0]["avg_a"] < 30):
                ret.append("%s is a difficult class." % code)
            elif (j["header"][0]["avg_a"] < 50):
                ret.append("%s is a moderate class." % code)
            else:
                ret.append("%s is an easy class." % code)
        else:
            ret.append("Error: No data available for %s" % code)
    return ret
