import requests
from bs4 import BeautifulSoup
import re

def findInfo(courses):
    ret = []
    for course in courses.split(","):
        code = course.replace(" ", "").upper()
        if (not code.strip()):
            ret.append("Error: Invalid code %s" % code)
            continue
        url = 'https://critique.gatech.edu/course.php?id=' + code

        r = requests.get(url)

        soup = BeautifulSoup(r.text, 'html.parser')

        try:
            mainTable = soup.findAll("table")[0].find("tbody").find("tr")
            avgGpa = float(mainTable.findAll("td")[1].get_text())
            percents = [int(mainTable.findAll("td")[i+2].get_text())
                        for i in range(5)] # A B C D F
        except:
            ret.append("Error: No data available for %s" % code)
            continue

        if (percents[0] < 30):
            ret.append("%s is a difficult class." % code)
        elif (percents[0] < 50):
            ret.append("%s is a moderate class." % code)
        else:
            ret.append("%s is an easy class." % code)
    return ret
