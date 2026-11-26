"""Esercizio 11 (Modulo 1) - Convertitore di unita' con menu.

Teoria: teoria/02_python_avanzato.md, sezioni 1, 9 e 10.

OBIETTIVO
Un programma con un menu che permette di convertire valori tra unita'
diverse, finche' l'utente non sceglie di uscire.

MENU
    === Convertitore ===
    1) Chilometri -> miglia
    2) Miglia -> chilometri
    3) Celsius -> Fahrenheit
    4) Fahrenheit -> Celsius
    5) Chilogrammi -> libbre
    6) Libbre -> chilogrammi
    0) Esci
    Scelta:

FORMULE
    km -> miglia        miglia = km * 0.621371
    miglia -> km        km = miglia * 1.609344
    C -> F              F = C * 9 / 5 + 32
    F -> C              C = (F - 32) * 5 / 9
    kg -> libbre        lb = kg * 2.204623
    libbre -> kg        kg = lb * 0.453592

REQUISITI
- Una FUNZIONE per ogni conversione, che riceve il valore e RESTITUISCE
  il risultato (nessun print o input dentro le funzioni di calcolo):
      def km_a_miglia(km): ...
- Il menu in un ciclo while True; "0" esce con break.
- Una scelta non valida stampa un messaggio e mostra di nuovo il menu.
- Il valore da convertire viene letto con una funzione che accetta solo
  numeri (riusa il lavoro dell'esercizio 10: leggi_float con try/except).
- Risultati con 2 decimali, con la f-string: f"{risultato:.2f}".

IDEA PER ORGANIZZARE IL CODICE (facoltativa ma istruttiva)
Invece di una lunga catena if/elif, usa un DIZIONARIO che associa la
scelta a una coppia (descrizione, funzione):
    conversioni = {
        "1": ("km -> miglia", km_a_miglia),
        "2": ("miglia -> km", miglia_a_km),
        ...
    }
Poi scorri conversioni.items() per costruire il menu e chiama
conversioni[scelta][1](valore) per convertire. Le funzioni sono valori
come gli altri: si possono mettere in un dizionario e richiamare dopo.

CONCETTI
- Funzioni di calcolo "pure": solo ingresso -> uscita.
- Menu a ciclo con break.
- Dizionario di funzioni (opzionale).
- Formattazione dei decimali nelle f-string.

COME VERIFICARE DA SOLO (assert sulle funzioni, fuori dal menu)
    assert abs(km_a_miglia(100) - 62.1371) < 1e-4
    assert abs(miglia_a_km(1) - 1.609344) < 1e-6
    assert celsius_a_fahrenheit(0) == 32
    assert celsius_a_fahrenheit(100) == 212
    assert fahrenheit_a_celsius(32) == 0
    assert abs(fahrenheit_a_celsius(212) - 100) < 1e-9
    assert abs(kg_a_libbre(10) - 22.04623) < 1e-4
    assert abs(libbre_a_kg(10) - 4.53592) < 1e-4
Controllo di coerenza: convertire un valore e poi riconvertire il
risultato deve riportare (quasi) al valore di partenza:
    assert abs(miglia_a_km(km_a_miglia(42)) - 42) < 0.01

ERRORI TIPICI
- Mettere input/print dentro le funzioni di calcolo: non si possono
  piu' testare con assert.
- Usare / al posto di * per i fattori (o viceversa): controlla con i
  valori noti (0 C = 32 F).
- Dimenticare le parentesi in (F - 32) * 5 / 9.
- Il menu non si ripete: manca il while True.

BONUS (facoltativo)
- Aggiungi altre conversioni (metri/piedi, litri/galloni, ...).
- Salva in un file di testo uno storico delle conversioni fatte.
- Mostra, dopo ogni conversione, la formula usata.

Scrivi il tuo codice qui sotto.
"""

def km_a_miglia(km):
    return km * 0.621371

def miglia_a_km(miglia):
    return miglia * 1.609344

def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def kg_a_libbre(kg):
    return kg * 2.204623

def libbre_a_kg(libbre):
    return libbre * 0.453592

conversioni = {
    "1": ("km -> miglia", km_a_miglia),
    "2": ("miglia -> km", miglia_a_km),
    "3": ("celsius -> fahrenheit", celsius_a_fahrenheit),
    "4": ("fahrenheit -> celsius", fahrenheit_a_celsius),
    "5": ("kg -> libbre", kg_a_libbre),
    "6": ("libbre -> kg", libbre_a_kg)
}

def leggi_float(messaggio):
    while True:
        try:
            return float(input(messaggio))
        except ValueError:
            print("Input non valido. Inserisci un numero.")

while True:  # "0" esce con break
    print("\n=== Convertitore ===")
    for key, (desc, _) in conversioni.items():
        print(f"{key}) {desc}")
    print("0) Esci")
    scelta = input("Scelta: ")

    if scelta == "0":
        break

    if scelta not in conversioni:
        print("Scelta non valida.")
        continue

    valore = leggi_float("Valore da convertire: ")
    _, funzione = conversioni[scelta]
    risultato = funzione(valore)
    print(f"Risultato: {risultato:.2f}")


assert abs(km_a_miglia(100) - 62.1371) < 1e-4
assert abs(miglia_a_km(1) - 1.609344) < 1e-6
assert celsius_a_fahrenheit(0) == 32
assert celsius_a_fahrenheit(100) == 212
assert fahrenheit_a_celsius(32) == 0
assert abs(fahrenheit_a_celsius(212) - 100) < 1e-9
assert abs(kg_a_libbre(10) - 22.04623) < 1e-4
assert abs(libbre_a_kg(10) - 4.53592) < 1e-4    
assert abs(miglia_a_km(km_a_miglia(42)) - 42) < 0.01