from mpmath import *


def function(y, z):
    return 108 - (815 - 1500 / mpf(y)) / mpf(z)    #funkcja dla podanych wartości zbiega do 5 dopóki precyzja zmiennych na to pozwala


iteracje = []                                       #tablica dla wygody wyświetlania ile iteracji zajęło odbiegnięcie od 5

def calculate(dps):
    x = [4, 4.25]
    i = 0
    tmp = 0
    mp.dps = dps                                    #ustawianie liczby miejsc po przecinku

    abs_list = []

    while tmp < 5:
        tmp = mpf(function(x[i], x[i+1]))           #mpf - float o wybranej ilości miejsc po przecinku
        x.append(tmp)
        i += 1
        print(i, tmp)

        minimum = abs(tmp - 5)                          #wyznaczanie wartości najbliższej 5
        abs_list.append(minimum)


    iteracje.append(abs_list.index(min(abs_list))+1)

calculate(15)                                           #domyślna precyzja
calculate(16)
calculate(17)
calculate(20)
calculate(50)
#calculate(250)
#calculate(1000)            #tymczasowo zakomentowane dla czytelności przy sprawdzaniu

print(iteracje)                                     #wyświetlanie przy której operacji wartość była najbliższa 5
