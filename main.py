from time import sleep

print("Witaj!")
print("1 - Zarejestruj sie\n2 - Zaloguj sie")
wybor = int(input("Co wybierasz: "))
if wybor == 1:
    nick = open("nick.txt", "w")
    haslo = open("haslo.txt", "w")

    if nick.writable():
        nick.write(input("Podaj nick: "))
    else:
        print("ERROR")

    if haslo.writable():
        haslo.write(input("Podaj haslo: "))
    else:
        print("ERROR")

    nick.close()
    haslo.close()
    
    print("Zamknij okno i sprawdz czy możesz sie zalogować")

elif wybor == 2:
    nick = open("nick.txt", "r")
    haslo = open("haslo.txt" , "r")

    if nick.readable():
        nickg = str(input("Podaj login: "))
    if haslo.readable():
        haslog = str(input("Podaj haslo: "))
    if nickg == nick.read():
        print("Login pomyslny")
    else:
        print("Login zły")
    if haslog == haslo.read():
        print("Haslo pomyslne")
    else:
        print("Haslo złe")

else:
    print("BLAD")


#Od tego miejsa możesz pisać co chcesz np. aplikacje, gre!

##########################
# \/ To możesz usunąć \/ #
                         #
while True:              #
    sleep(1)             #
                         #
# /\ To możesz usunąć /\ #
##########################