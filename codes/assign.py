import numpy as np
import numpy.random as nr

names = np.array(["Clement Bonnerot", "Maria Charisi", "Shea Garrison-Kimmel", \
         "Davide Gerosa", "François Hébert", "Cameron Hummels", \
         "Suoqing Ji", "Eve Lee", "Wenbin Lu", \
         "Yiqiu Ma", "Jordan Moxon", "Stephen Taylor", \
         "Coral Wheeler", "Jess Mclver", "Andrew Wade", "Johannes Eichholz", \
         "Brittany Kamai", "Christine Corbett Moran", "Quanzhi Ye", \
         "Michael Coughlin", "Susanna Kohler", "Joseph Simon", \
         ])

dates = np.array(["Oct 25 18", \
                  "Nov 01 18", "Nov 08 18","Nov 15 18", "Nov 29 18", \
                  "Dec 06 18", "Dec 13 18", \
                  "Jan 10 19", "Jan 17 19", "Jan 24 19", "Jan 31 19", \
                  "Feb 07 19", "Feb 14 19", "Feb 21 19", "Feb 28 19", \
                  "Mar 07 19", "Mar 14 19", "Mar 21 19", \
                  "Apr 04 19", "Apr 11 19", "Apr 18 19", "Apr 25 19",])

speaker = np.copy(names)
food = np.copy(names)

nr.shuffle(speaker)
nr.shuffle(food)

f = open("assignment.txt", 'w')
for d, s, o in zip(dates, speaker, food):
    f.write("<tr> <td> %s </td> <td> %s </td> <td> %s </td> </tr>\n"%(d, s, o))
f.close()