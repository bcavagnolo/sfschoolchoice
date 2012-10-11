import csv, urllib2, urllib, sys
from HTMLParser import HTMLParser
import tidy
from lxml import etree
from StringIO import StringIO

# check input file to ensure API data is available from CA dept of education.
def appendCADeptEdIds(schools):
    urlFormat = 'http://dq.cde.ca.gov/dataquest/API/APISearchName.asp?TheYear=&cTopic=API&cLevel=School&cName=%s&cCounty=&cTimeFrame=S'
    for row in schools:
        name = row[0].split(' ')[0]
        if name == 'name':
            # skip header row
            continue

        # Handle a bunch of special cases
        if row[0] == 'S. F. Community':
            name = row[0].split(' ')[2]
        elif row[0] == 'S. F. Public Montessori Elementary School':
            name = 'public'
        elif row[0] == 'E. R. Taylor Elementary School':
            name = row[0].split(' ')[2]
        elif row[0] == 'John Yehall Chin Elementary School':
            name = 'Yehall'
        elif row[0] == 'Dr. William L. Cobb Elementary School':
            name = 'Cobb'
        elif row[0] == 'Dr. George Washington Carver Elementary School':
            name = 'Carver'
        elif row[0] == 'Chinese Immersion School at DeAvila':
            name = 'Immersion'
        elif row[0] == 'Frank McCoppin Elementary School':
            name = 'McCoppin'
        elif row[0] == 'George Moscone Elementary School':
            name = 'Moscone'
        elif name == 'Dr.':
            name = row[0].split(' ')[1]
        elif row[0] == 'El Dorado Elementary School':
            name = 'Dorado'
        url = urlFormat % urllib.quote(name)
        try:
            html = urllib2.urlopen(url)
        except urllib2.HTTPError:
            # something is wrong with the name.  Try again with just the first word
            # of the name
            url = urlFormat % urllib.quote(name.split(' ')[0])
            html = urllib2.urlopen(url)
        parsedPage = etree.HTML(html.read())
        options = parsedPage.xpath('/html/body//select/option')
        finalParts = []
        for o in options:
            parts = map(lambda x: x.replace(u'\xa0',''), o.text.split('--'))
            district = parts[1]
            if district == "SAN FRANCISCO U" and not finalParts:
                finalParts.append(parts)

        if finalParts == []:
            print 'Failed to find ' + row[0] + ' in results for ' + name
            continue
        elif len(finalParts) != 1:
            print 'WARNING: Found multiple matches for ' + row[0] + ':'
            map(lambda p : sys.stdout.write("\t" + p[0]), finalParts)
        else:
            print 'Found ' + row[0] + ' (a.k.a. ' + finalParts[0][0] + ')'

csvfile = open('schools.csv', 'rb')
schools = csv.reader(csvfile, delimiter=',')
schools = appendCADeptEdIds(schools)

