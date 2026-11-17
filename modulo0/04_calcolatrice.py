"""Esercizio 4 - Mini calcolatrice (fine Modulo 0).

Obiettivo: il programma chiede due numeri e stampa somma, differenza,
prodotto e divisione, ciascuno su una riga.

Esempio con 7 e 2:
    7 + 2 = 9
    7 - 2 = 5
    7 * 2 = 14
    7 / 2 = 3.5

Concetti nuovi:
- float() converte il testo in numero con la virgola (decimale).
  Usalo al posto di int() cosi' accetti anche numeri come 2.5.
- Operatori: + (somma), - (differenza), * (prodotto), / (divisione).
- Operatori in piu' da conoscere: // (divisione intera, scarta i decimali),
  % (resto della divisione), ** (potenza).

Suggerimento: dentro una f-string puoi mettere un calcolo tra graffe:
    print(f"{a} + {b} = {a + b}")

Bonus (facoltativo): stampa anche divisione intera, resto e potenza.
Prova a inserire 0 come secondo numero: cosa succede con la divisione?
Leggi l'errore, ci torneremo nel Modulo 1.

Scrivi il tuo codice qui sotto.
"""
val1 = float(input("Inserisci il primo numero: "))
val2 = float(input("Inserisci il secondo numero: "))

print(f"{val1} + {val2} = {val1 + val2}")
print(f"{val1} - {val2} = {val1 - val2}")
print(f"{val1} * {val2} = {val1 * val2}")
print(f"{val1} / {val2} = {val1 / val2}")
print(f"{val1} // {val2} = {val1 // val2}")
print(f"{val1} % {val2} = {val1 % val2}")
print(f"{val1} ** {val2} = {val1 ** val2}")
