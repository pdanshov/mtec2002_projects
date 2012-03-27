import random
import sqlite3
import os
import sys
import time

anima="""
----O  Rock
-------------[]  Paper
-----------------------8<  Scissors
"""
idx = 0
for x in range(72):
    print anima[idx%len(anima)],;
    sys.stdout.softspace=False;
    #sys.stdout.write((idx%len(anima))+"\b"),
    idx += 1
    time.sleep(0.05)

if not os.path.exists('./save_data'):
    os.makedirs('./save_data')

conn = sqlite3.connect('./save_data/scores.db')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='scores'")
data = c.fetchall()
if len(data)==0:
    c.execute('CREATE TABLE IF NOT EXISTS scores(Player TEXT, Round INT, Score INT, Computer INT)')
    conn.commit()
    c.execute('INSERT INTO scores (Player, Round, Score, Computer) VALUES ("Peter", 1, 99999, 0)')
    conn.commit()
    c.execute('INSERT INTO scores (Player, Round, Score, Computer) VALUES ("Jon", 62, 48, 14)')
    conn.commit()
    c.execute('INSERT INTO scores (Player, Round, Score, Computer) VALUES ("Joseph", 16, 12, 5)')
    conn.commit()
    c.execute('INSERT INTO scores (Player, Round, Score, Computer) VALUES ("Paul", 23, 5, 18)')
    conn.commit()
    c.execute('INSERT INTO scores (Player, Round, Score, Computer) VALUES ("Zombie", 52, 6, 46)')
    conn.commit()
    c.execute('INSERT INTO scores (Player, Round, Score, Computer) VALUES ("Gaia", 12, 3, 9)')
    conn.commit()

print "Hi, what's your name?"
player_name = raw_input("> ").capitalize()
if len(player_name) > 6:
    player_name = player_name[0:3]+"..."

c.execute("SELECT Player FROM scores WHERE Player=?",[player_name])
data = c.fetchall()
if len(data)==0:
    c.execute("INSERT INTO scores (Player, Round, Score, Computer) VALUES (?, ?, ?, ?)", (player_name, 0, 0, 0))
    conn.commit()
c.execute('SELECT Round FROM Scores WHERE Player=?',[player_name])
round = c.fetchone()[0]
c.execute('SELECT Score FROM scores WHERE Player=?',[player_name])
player_score = c.fetchone()[0]
c.execute('SELECT Computer FROM scores WHERE Player=?',[player_name])
computer_score = c.fetchone()[0]

help = """
"r" - Play rock
"p" - Play paper
"s" - Play scissors
"quit" - Leave the game
"scores" - High-score list
"help" - Return to this menu\n"""
print """\nHi %s, let's play a game of Rock, Paper, Scissors... \n%s""" % (player_name, help)
choices = ['r', 'p', 's']

while True:
    print "Round %d" % round
    print "="*29
    print "%s: %d, Computer: %d\n\n(r)ock, (p)aper, (s)cissors, or (help)" % (player_name, player_score, computer_score)
    choice = raw_input("> ").lower()
    computer_choice = choices[random.randint(0, 2)]
    if choice == 'quit':
        break
    elif choice == 'help':
        print "\n%s" % help
    elif choice == 'scores':
        print "\n        ~~~~~~~~Current~~~~~~~~"
        print "   Player    Round    Score    Computer"
        print "   %-6s    %-5s    %-5s    %-3s" % (player_name, round, player_score, computer_score)
        with conn:
            c.execute('SELECT * FROM scores ORDER BY Score DESC')
            col_names = [cn[0] for cn in c.description]
            rows = c.fetchall()
            print "\n        ~~~~~~~Hi Scores~~~~~~~"
            print "   ____________________________________"
            print "   %-6s    %s    %s    %s" % (col_names[0], col_names[1], col_names[2], col_names[3])
            for row in rows:
                print "   %-6s    %-5s    %-5s    %-3s" % row
            print ""
    elif choice not in choices:
        print '\nInvalid input\n'
    else:
        print '%s played %s, Computer played %s' % (player_name, choice, computer_choice)
        if choice == 'r':
            if computer_choice == 'r':
                print 'Tie!\n'
            elif computer_choice == 'p':
                print 'Computer wins\n'
                computer_score += 1
            elif computer_choice == 's':
                print '%s wins\n' % player_name
                player_score += 1
        elif choice == 'p':
            if computer_choice == 'p':
                print 'Tie!\n'
            elif computer_choice == 's':
                print 'Computer wins\n'
                computer_score += 1
            elif computer_choice == 'r':
                print '%s wins\n' % player_name
                player_score += 1
        elif choice == 's':
            if computer_choice == 's':
                print 'Tie!\n'
            elif computer_choice == 'r':
                print 'Computer wins\n'
                computer_score += 1
            elif computer_choice == 'p':
                print '%s wins\n' % player_name
                player_score += 1
        round += 1
c.execute("UPDATE scores SET Round=?,Score=?,Computer=? WHERE Player=?", (round, player_score, computer_score, player_name))
conn.commit()
c.close()