Introduction
============

The purpose of this project is just to have a place to collect the random
one-off scripts I'm using to gather data on SF elementary schools.  You may (or
may not) find the schools.csv file interesting, which contains the collected
data.  You probably will not find any of the python code interesting.

Data Sources
============

1. I copied the initial list of elementary schools manually from:

   http://www.sfusd.edu/en/schools/elementary-schools.html

   This only has name, grades served, neighborhood, address, and phone of the
   school.

2. The original school list included many "early education programs".  We
   eliminate these because we are only interested public schools with
   kindergartens.  See departmentOfEd.py for details.  Note that this script
   also captures some sort of D of Ed ID numbers that can be used for fetching
   SARC webpages.  S

3. Both SFUSD and Ca D of Ed publish SARC data.  And we're probably going to
   have to scrape it somehow.  Not sure what the best source will be.  Perhaps
   somebody else has done this work for us already?  SFUSD also makes SARC data
   available, here:

   http://www.sfusd.edu/en/assets/sfusd-staff/rpa/schdata/sarctran.htm

   I'm not quite sure which one will be easier to scrape.
