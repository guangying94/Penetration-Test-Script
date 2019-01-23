import psycopg2
import random
import string
import numpy as np
import time

def generate_cred(sets,idLength,pwLength):
    ## first input is numbers of credentials needed
    ## second input is the length of id string
    ## third input is the length of password string
    cred = []
    for i in range(0,sets):
        letters = string.ascii_letters
        id = ''.join(random.choice(letters) for j in range(idLength))
        pw_characters = string.ascii_letters + string.digits + string.punctuation
        pw = ''.join(random.choice(pw_characters) for k in range(pwLength))
        cred.append([id,pw])   
    return cred


def connect(dbname,host,id,pw):
    try:
        userhost = host
        ## this is for Azure Postgresql, but can be done in PostgreSQL server as well, just need to replace the host
        conn_string = "dbname='%s' user='%s@%s' host='%s.postgres.database.azure.com' password='%s' port='5432'" % (dbname,id,userhost,host,pw)
        conn = psycopg2.connect(conn_string)

        cur = conn.cursor()
        print('Connected!')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()

    except (Exception, psycopg2.DatabaseError):
        print('Failed.')

if __name__ == '__main__':

    test = generate_cred(500,8,8)
    ## Should try the right credential first, to ensure the connectivity is reachable
    array_len = len(test)
    for i in range(array_len):
        test_id = test[i][0]
        test_pw = test[i][1]
        print('test ' + str(i) + ' Cred: (%s)(%s)') % (test_id,test_pw)
        ## replace your database name, and the host name for your own
        connect('postgres',test_id,'asc-demo',test_pw)
        time.sleep(1)
