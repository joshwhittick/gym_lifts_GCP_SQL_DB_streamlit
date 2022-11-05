# https://towardsdatascience.com/sql-on-the-cloud-with-python-c08a30807661
# https://console.cloud.google.com/welcome?project=light-return-366609

# https://www.plus2net.com/python/cloud-google.php
# https://dev.to/gabrielosluz/get-data-from-cloud-sql-with-python-51jm

#user = "batman"
#password = "robin"
#ip = "35.246.101.125"
#db = "lifting-db"
#ip_type=IPTypes.PUBLIC


import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'JW',
    'password': 'test',
    'host': '35.246.101.125',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'server-ca.pem',
    'ssl_cert': 'client-cert.pem',
    'ssl_key': 'client-key.pem',
    'database': 'lifting-db'
}


# now we establish our connection
cnxn = mysql.connector.connect(**config)

cursor = cnxn.cursor()  # initialize connection cursor
#cursor.execute("CREATE TABLE Lifts (Exercise_ID serial NOT NULL, Date_of_exercise date NOT NULL, Exercise varchar(20) NOT NULL, Sets smallint NOT NULL, Reps smallint NOT NULL, Weight float NOT NULL, Total_Reps smallint NOT NULL, Total_Load float NOT NULL, PRIMARY KEY (Exercise_ID))")
#cnxn.commit()

results = cursor.execute("SHOW COLUMNS FROM Lifts")

print(results)

cnxn.close()

