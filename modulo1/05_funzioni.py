"""Esercizio 5 (Modulo 1) - Le funzioni.

Teoria: teoria/02_python_avanzato.md, sezioni 1 e 11.

OBIETTIVO
Scrivere quattro funzioni, verificarle con degli assert e riscrivere
l'esercizio dei voti (03_liste.py) usando le funzioni.

LE QUATTRO FUNZIONI
1. media(numeri)
   Riceve una lista di numeri e RESTITUISCE la loro media.
2. e_pari(n)
   Riceve un intero e restituisce True se e' pari, False altrimenti.
   (Suggerimento: l'operatore % da' il resto della divisione.)
3. massimo_di_tre(a, b, c)
   Restituisce il piu' grande dei tre numeri SENZA usare max().
   (Usa if/elif/else e i confronti.)
4. saluta(nome, saluto="Ciao")
   Restituisce la stringa "Ciao, Anna!". Se si passa un secondo
   argomento lo usa al posto di "Ciao". Prova: saluta("Anna", "Buongiorno").

CONCETTI NUOVI
- def nome(parametri):  e il corpo rientrato di 4 spazi.
- return: restituisce un valore e termina la funzione.
- Differenza tra print e return: se la funzione fa solo print, il valore
  e' perso e non puo' essere usato in altri calcoli.
- Parametro con valore predefinito: def saluta(nome, saluto="Ciao").
- Variabili locali: quelle create dentro la funzione non esistono fuori.

PASSI SUGGERITI
1. Scrivi la funzione, poi SUBITO provala con una chiamata e un print.
2. Quando tutte e quattro funzionano, aggiungi in fondo gli assert qui sotto.
3. Infine riscrivi la parte "chiedi 5 voti" in modo che usi media().

COME VERIFICARE DA SOLO (copia in fondo al file, dopo le funzioni)
    assert media([6, 8, 7]) == 7
    assert media([10]) == 10
    assert e_pari(4) is True
    assert e_pari(7) is False
    assert e_pari(0) is True
    assert massimo_di_tre(3, 9, 5) == 9
    assert massimo_di_tre(9, 3, 5) == 9
    assert massimo_di_tre(5, 3, 9) == 9
    assert massimo_di_tre(4, 4, 4) == 4
    assert saluta("Anna") == "Ciao, Anna!"
    assert saluta("Anna", "Buongiorno") == "Buongiorno, Anna!"
    print("Tutti i controlli superati")
Se un assert fallisce leggi la riga indicata: ti dice quale caso non torna.

ERRORI TIPICI
- Dimenticare return (la funzione restituisce None).
- Mettere return dentro un ciclo for senza volerlo: la funzione esce
  al primo giro.
- Chiamare la funzione senza le parentesi: e_pari invece di e_pari(4).

BONUS (facoltativo)
- minimo_massimo(numeri) che restituisce DUE valori: return min(...), max(...)
  e usala con: piccolo, grande = minimo_massimo([4, 9, 2]).
- e_primo(n): True se n e' un numero primo (prova i divisori da 2 a n-1).
- Una funzione leggi_voti(quanti) che chiede i voti e restituisce la lista.

Scrivi il tuo codice qui sotto.
"""
def media(numeri):
    return sum(numeri) / len(numeri)

def e_pari(n):
    return n % 2 == 0

def massimo_di_tre(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def saluta(nome, saluto="Ciao"):
    return f"{saluto}, {nome}!"

assert media([6, 8, 7]) == 7
assert media([10]) == 10
assert e_pari(4) is True
assert e_pari(7) is False
assert e_pari(0) is True
assert massimo_di_tre(3, 9, 5) == 9
assert massimo_di_tre(9, 3, 5) == 9
assert massimo_di_tre(5, 3, 9) == 9
assert massimo_di_tre(4, 4, 4) == 4
assert saluta("Anna") == "Ciao, Anna!"
assert saluta("Anna", "Buongiorno") == "Buongiorno, Anna!"
print("Tutti i controlli superati")

voti = []

def stampa_risultati(voti):
    print(f"Voti: {voti}")
    print(f"Massimo: {max(voti)}")
    print(f"Minimo: {min(voti)}")
    print(f"Media: {media(voti)}")

for i in range(5):
    voto = float(input(f"Inserisci il voto {i + 1}: "))
    voti.append(voto)

stampa_risultati(voti)
