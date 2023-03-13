import math, time

def szuk_inter(tab, szukana):
    lewa , prawa, poz, a = 0, len(tab) - 1 ,0, 0

    try:                                                                #element do obsługi wyjątków - sytuacje z błędnymi danymi
        if tab[prawa] == tab[lewa]:                                     #dla jednej wartości dzielono by przez 0 przy obliczanniu wsp. interpolacji
            if tab[prawa] == szukana:
                return prawa
            else:
                return -1

        while tab[poz] != szukana and a >= 0 and a <= 1:                #dopóki wartość z tablicy nie będzie równa szukanej,
                                                                        # lub wsp. interpolacji nie będzie sensowny - czyli [0, 1]
            try:
                a = (szukana - tab[lewa]) / (tab[prawa] - tab[lewa])    #try except to wydajny sposób na ominięcie dzielenia przez 0,
                                                                        # które następuje kiedy prawa == lewa
            except ZeroDivisionError:
                if tab[lewa] == szukana:
                    return lewa
                else:
                    return -1

            if a >=0 and a <= 1:
                poz = math.floor(lewa + a * (prawa - 1))                    #wyznaczanie indeksu sprawdzanej wartości
                if szukana > tab[poz]:
                    lewa = poz + 1
                elif szukana < tab[poz]:
                    prawa = poz - 1

        if tab[poz] == szukana:
            return poz
        else:
            return -1

    except (NameError, TypeError) as errors:                             #element do obsługi wyjątków - sytuacje z błędnymi danymi
        return "Błędne dane wejściowe"




def weryfikator(tab, szukana):
    for each in tab:
        if each == szukana:
            return tab.index(szukana)


def czy_niemalejaca(tab):                                     #raczej będzie tu zbędne, dane wejściowe będą niemalejące
    for i in range(0, len(tab) - 1):
        if tab[i] > tab[i+1]:
            return 'Tablica nie jest niemalejąca'
        else:
            return 'Tablica jest niemalejąca'


def gen_rowno(n):
    lista_rownomierna = []
    x, i = 0, 0

    while i < n:
        i += 1
        x += 10
        lista_rownomierna.append(x)
    return lista_rownomierna

def gen_nierowno(n):
    lista_nierownomierna = []
    x, i = 0, 0
    czesc1 = math.ceil(n/4)
    czesc2 = math.ceil(n/2)

    while i < czesc1:
        i += 1
        x += 10
        lista_nierownomierna.append(x)
    while i < czesc2:
        i += 1
        x += 200
        lista_nierownomierna.append(x)
    while i < n:
        i += 1
        x += 10
        lista_nierownomierna.append(x)
    return lista_nierownomierna

def gen_exp(n):
    lista_exp = []
    x, i = 2, 0

    while i < n:
        i += 1
        x = 2 ** i

        lista_exp.append(x)
    return lista_exp

#### listy do N #####################################

lista_rownomierna_10 = gen_rowno(10)
#lista_nierownomierna_10 = gen_nierowno(10)
#lista_exp_10 = gen_exp(10)

#### listy N = 100
lista_rownomierna_100 = gen_rowno(100)
#lista_nierownomierna_100 = gen_nierowno(100)
#lista_exp_100 = gen_exp(100)

#### listy N = 300
lista_rownomierna_300 = gen_rowno(300)
#lista_nierownomierna_300 = gen_nierowno(300)
#lista_exp_300 = gen_exp(300)

#### listy N = 750
lista_rownomierna_750 = gen_rowno(750)
#lista_nierownomierna_750 = gen_nierowno(750)
#lista_exp_750 = gen_exp(750)

#### listy N = 1500
lista_rownomierna_1500 = gen_rowno(1500)
#lista_nierownomierna_1500 = gen_nierowno(1500)
#lista_exp_1500 = gen_exp(1500)

#### listy N = 5000
lista_rownomierna_5000 = gen_rowno(5000)
#lista_nierownomierna_5000 = gen_nierowno(5000)
#lista_exp_5000 = gen_exp(5000)

#### listy N = 10000
lista_rownomierna_10000 = gen_rowno(10000)
#lista_nierownomierna_10000 = gen_nierowno(10000)
#lista_exp_10000 = gen_exp(10000)

#### listy N = 20000
lista_rownomierna_20000 = gen_rowno(20000)
#lista_nierownomierna_20000 = gen_nierowno(20000)
#lista_exp_20000 = gen_exp(20000)

#### listy N = 30000
lista_rownomierna_30000 = gen_rowno(30000)
#lista_nierownomierna_30000 = gen_nierowno(30000)
#lista_exp_30000 = gen_exp(30000)

#### listy N = 50000
lista_rownomierna_50000 = gen_rowno(50000)
#lista_nierownomierna_50000 = gen_nierowno(50000)
#lista_exp_50000 = gen_exp(50000)

### listy N = 75000
lista_rownomierna_75000 = gen_rowno(75000)
#lista_nierownomierna_75000 = gen_nierowno(75000)
#lista_exp_75000 = gen_exp(75000)

#### listy N = 100000
lista_rownomierna_100000 = gen_rowno(100000)
#lista_nierownomierna_100000 = gen_nierowno(100000)
#lista_exp_100000 = gen_exp(100000)


####################################################################### wywołania
#print(lista_rownomierna_100)

print(lista_rownomierna_30000[math.floor(len(lista_rownomierna_30000) * (7/10))])

start = time.perf_counter_ns()
print(szuk_inter(lista_rownomierna_30000, 210010))
end = time.perf_counter_ns()

c1 = time.perf_counter_ns()
print('weryfikator', weryfikator(lista_rownomierna_30000, 210010))
c2 = time.perf_counter_ns()

czas_inter = str(end - start)
czas_linia = str(c2 - c1)

print('Czas szukania interpolacyjnego:', czas_inter)
print('Czas szukania liniowego:', czas_linia)

with open('rownowazone_10.txt', 'a') as f:
    f.writelines(czas_inter + '\n')
with open('liniowe.txt', 'a') as f:
    f.writelines(czas_linia + '\n')


#wersja z rekursją, niewykorzystana
''' wersja z rekursją ma limity pamięci; daje RecursionError dla dużych tablic
def interpolationSearch(tab, lewa, prawa, x):

    if lewa <= prawa and x >= tab[lewa] and x <= tab[prawa]:

        if lewa == prawa:                                       #
            return lewa

        poz = lewa + ((prawa - lewa) // (tab[prawa] - tab[lewa]) * (x - tab[lewa]))        #interpolacja liniowa - wzór wręcz z wikipedii

        if tab[poz] == x:
            return poz

        if tab[poz] < x:
            return interpolationSearch(tab, poz + 1, prawa, x)

        if tab[poz] > x:
            return interpolationSearch(tab, lewa, poz - 1, x)
    return 'Nie znaleziono'
'''