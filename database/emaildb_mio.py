import sqlite3

conn = sqlite3.connect('C:/users/ma_gi/desktop/python_scripts/database/emaildb_mio.sqlite') # una specie di file handle più complicato
cur = conn.cursor() # noi comunichiamo direttamente col cursore, che è una specie di lazy evaluator (poi il commit funge da flush, tipo)

cur.execute('DROP TABLE IF EXISTS Counts') # cancella i dati nel database se esiste una colonna counts, cioè se ci sono già dei dati

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)') # crea una table chiamata Counts con due colonne: org (testo) e count (interi)

fname = 'C:/users/ma_gi/desktop/python_scripts/mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue # non mi interessa il testo delle mail, solo gli headers
    pieces = line.split()
    email = pieces[1] # così scarto 'From: ' e leggo l'indirizzo email, che è il secondo elemento della lista pieces
    org = email.split('@')[1] # in realtà non mi serve tutta la mail, solo ciò che c'è dopo @

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,)) # si usa il gergo SQL (in particolare il placeholder ?) e non f-strings per evitare SQL injections, dice dr Chuck
    # selezioniamo la colonna count dalla table Counts nelle righe dove org (attributo SQL) == org (variabile python)
    row = cur.fetchone() # prendiamo il primo output restituito dal comando precedente

    if row is None: # se questa org non esiste ancora creiamo una riga per essa con count = 1
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else: # se esiste già incrementiamo count di 1
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))

conn.commit() # dalla spiegazione di questo esercizio (che fa il confronto con quello già pronto):
# Because the sample code is using an UPDATE statement and committing the results to the database as each record is read in the loop, 
# it might take as long as a few minutes to process all the data. The commit insists on completely writing all the data to disk every time it is called.
# The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program, 
# there is a balance between the number of operations you execute between commits and the importance of not losing the results of operations that have not yet been committed.

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1]) # Hint: The top organizational count is 536.

cur.close()