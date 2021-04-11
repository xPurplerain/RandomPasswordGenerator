import random

# Hier stehen alle Zeichen die zufällig zusammen gefügt werden
zeichen = "abcdefghijklmonopqrstuvwxyzABCDEFGHIJKLMONOPQRSTUVWXYZ1234567890!§$%&/()=?'#-_.;,:-"

while 1:
    passwd_len = int(input("Wie lang soll dein Passwort sein? "))
    passwd_anzahl = int(input("Wieviele Passwörter sollen generiert werden? "))
    for x in range(0, passwd_anzahl):
        password = ""
        for x in range(0, passwd_len):
            password_zeichen = random.choice(zeichen)
            password = password + password_zeichen
        print("Fertig -- Hier ist dein zufälliges Passwort: ", password)
