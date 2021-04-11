import random

# Hier stehen alle Buchstaben die zufällig zusammen gefügt werden
chars = "abcdefghijklmonopqrstuvwxyzABCDEFGHIJKLMONOPQRSTUVWXYZ1234567890!§$%&/()=?'#-_.;,:-"

while 1:
    passwd_len = int(input("Wie lang soll dein Passwort sein? "))
    passwd_count = int(input("Wieviele Passwörter sollen generiert werden? "))
    for x in range(0, passwd_count):
        password = ""
        for x in range(0, passwd_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Fertig -- Hier ist dein zufälliges Passwort: ", password)
