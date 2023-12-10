"""
Counting Organizations
This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)
When you have run the program on mbox.txt upload the resulting database file above for grading.
If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.
"""

import sqlite3
conn = sqlite3.connect("orgdb.sqlite")
cur = conn.cursor()

cur.execute(''' DROP TABLE IF EXISTS Counts''')
cur.execute(''' CREATE TABLE Counts (org TEXT, count INTEGER)''' )

fname = input("Enter file name:")
if (len(fname) < 1): fname = "mbox.txt"
fh = open(fname)
for line in fh:
    if not line.startswith("From: "): continue
    pieces = line.split('@') # split every piece of text left and right from the @ sign.
    org = pieces[1]
    #print (org)
    cur.execute ('SELECT count FROM Counts WHERE org = ?', (org,)) # the "?" is a placeholder for the email domain which being added as a tuple. This line does not read the data.
    row = cur.fetchone() #Grab the first row
    if row is None:
        cur.execute (''' INSERT INTO Counts (org, count) VALUES (?, 1)''' , (org,)) # If the mail domain does not yet exist in the column: create it and add a value of 1 to it.
    else:
        cur.execute('UPDATE Counts SET count = count +1 WHERE org = ?', (org,)) # if the mail domain exists, update the count of the mail domain in the table "Counts"
        #conn.commit() #Data is being written from memory to database every time new data is found because it is in the "for loop". This process takes a lot of memory
conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr): #When executing the sqlstring, print the information (count and mail domain) of every row of both columns of the table COUNTS in decending order.
    print(str(row[0]), row[1])

cur.close
