# Teoria 2 — Python: funzioni, file, errori, moduli

Completa la base del Modulo 1. Serve per gli esercizi `modulo1/05` … `modulo1/12`.
Si assume di aver letto `01_python_base.md`.

Indice: [1. Funzioni](#1-funzioni) · [2. Stringhe](#2-stringhe) · [3. while, break, continue](#3-while-break-continue) ·
[4. Moduli e import](#4-moduli-e-import) · [5. Ordinare](#5-ordinare) · [6. Tuple e insiemi](#6-tuple-e-insiemi) ·
[7. File](#7-file) · [8. JSON](#8-json) · [9. Errori e try/except](#9-errori-e-tryexcept) ·
[10. Organizzare il codice](#10-organizzare-il-codice) · [11. Verificare con assert](#11-verificare-con-assert)

---

## 1. Funzioni

Una **funzione** è un blocco di codice con un nome, che si può richiamare quante volte si vuole.
Evita di ripetere lo stesso codice e rende il programma leggibile.

```python
def media(numeri):
    totale = sum(numeri)
    return totale / len(numeri)

risultato = media([6, 8, 7])     # chiamata: risultato vale 7.0
print(risultato)
```

Pezzi della definizione:
- `def` introduce la funzione; segue il **nome**, le **parentesi** con i **parametri**, i `:`.
- Il corpo è **rientrato** di 4 spazi.
- `return` **restituisce** un valore a chi ha chiamato la funzione e **termina** la funzione.
- Una funzione senza `return` restituisce `None` (nessun valore).

**`print` contro `return`** (errore frequentissimo): `print` mostra qualcosa a schermo ma il valore
è perso; `return` consegna il valore al programma, che può usarlo in altri calcoli.

```python
def somma_print(a, b):
    print(a + b)        # stampa, ma restituisce None

def somma_return(a, b):
    return a + b        # restituisce il valore

x = somma_return(2, 3) * 10    # 50: funziona
y = somma_print(2, 3) * 10     # TypeError: None * 10
```

**Parametri e argomenti.** I parametri sono i nomi nella definizione (`a`, `b`); gli argomenti
sono i valori passati nella chiamata (`2`, `3`). Si possono passare per posizione o per nome:
`saluta(nome="Anna", saluto="Buongiorno")`.

**Valori predefiniti:**

```python
def saluta(nome, saluto="Ciao"):
    return f"{saluto}, {nome}!"

saluta("Anna")                  # "Ciao, Anna!"
saluta("Anna", "Buongiorno")    # "Buongiorno, Anna!"
```

I parametri con valore predefinito vanno **dopo** quelli senza.

**Più valori restituiti** (in realtà una tupla):

```python
def minimo_massimo(lista):
    return min(lista), max(lista)

piccolo, grande = minimo_massimo([4, 9, 2])
```

**Variabili locali.** Le variabili create dentro una funzione esistono solo lì dentro.
Fuori dalla funzione il nome non esiste (`NameError`). La funzione comunica con l'esterno
tramite parametri (in ingresso) e `return` (in uscita).

**Buona pratica:** una funzione fa **una cosa sola** e ha un nome che dice quale
(`calcola_media`, `e_pari`, `leggi_numero`). Se serve un commento lungo per spiegarla, forse
va divisa in due.

## 2. Stringhe

Una stringa è una **sequenza di caratteri**: si può indicizzare come una lista.

```python
s = "Python"
s[0]        # "P"
s[-1]       # "n"
s[0:3]      # "Pyt"  (slicing: dal 0 al 3 escluso)
len(s)      # 6
"th" in s   # True
```

Le stringhe sono **immutabili**: i metodi non le modificano, ne restituiscono una nuova.

| Metodo | Cosa fa | Esempio |
|---|---|---|
| `lower()` / `upper()` | minuscolo / maiuscolo | `"Ciao".lower()` → `"ciao"` |
| `strip()` | toglie spazi e a-capo ai bordi | `"  hi\n".strip()` → `"hi"` |
| `split()` | divide in una lista di parole | `"a b  c".split()` → `["a","b","c"]` |
| `split(",")` | divide con un separatore | `"1,2,3".split(",")` → `["1","2","3"]` |
| `join(lista)` | unisce con un separatore | `", ".join(["a","b"])` → `"a, b"` |
| `replace(a, b)` | sostituisce | `"a.b".replace(".", "")` → `"ab"` |
| `startswith(x)` | inizia con? | `"ciao".startswith("ci")` → `True` |
| `find(x)` | posizione, `-1` se manca | `"ciao".find("a")` → `2` |
| `count(x)` | quante volte compare | `"banana".count("a")` → `3` |

**Formattare i numeri nelle f-string:**

```python
x = 3.14159
f"{x:.2f}"       # "3.14"   (2 decimali)
f"{1234567:,}"   # "1,234,567" (separatore migliaia)
f"{0.256:.1%}"   # "25.6%"
f"{7:>5}"        # "    7"  (allineato a destra, larghezza 5)
```

## 3. while, break, continue

`while` ripete finché la condizione è vera. Si usa quando **non si sa in anticipo quante volte**
(per esempio "finché l'utente non indovina").

```python
tentativi = 0
while True:                      # ciclo che continua finché non c'è un break
    risposta = input("Password? ")
    tentativi += 1
    if risposta == "segreto":
        break                    # esce dal ciclo
    print("Sbagliata")
print(f"Ci sei riuscito in {tentativi} tentativi")
```

- `break` esce subito dal ciclo.
- `continue` salta al giro successivo senza eseguire il resto del blocco.
- `x += 1` è la forma breve di `x = x + 1` (esistono anche `-=`, `*=`, `/=`).
- Rischio: **ciclo infinito**. Se una finestra non risponde, `Ctrl+C` nel terminale lo ferma.

**for o while?** `for` quando si scorre una sequenza o si conosce il numero di giri;
`while` quando si ripete finché succede qualcosa.

## 4. Moduli e import

Python ha una **libreria standard** di moduli già pronti. Si importano con `import`.

```python
import random
numero = random.randint(1, 100)       # intero casuale tra 1 e 100 (estremi inclusi)
scelta = random.choice(["a", "b"])    # un elemento a caso da una lista

import math
math.sqrt(16)      # 4.0
math.pi            # 3.14159...

from random import randint            # importa solo una funzione
import numpy as np                    # alias: da qui in poi si scrive np.
```

Per ottenere sempre gli stessi numeri casuali (utile per verificare un programma):
`random.seed(42)` prima di usare `random`.

Le librerie **non** standard (NumPy, pandas, …) si installano con `pip` nell'ambiente virtuale.

## 5. Ordinare

```python
numeri = [5, 2, 9]
sorted(numeri)                    # [2, 5, 9], nuova lista
sorted(numeri, reverse=True)      # [9, 5, 2]
numeri.sort()                     # ordina la lista originale (restituisce None)
```

Ordinare secondo un criterio: parametro `key`, che è una funzione applicata a ogni elemento.

```python
parole = ["pera", "kiwi", "banana"]
sorted(parole, key=len)           # ['pera', 'kiwi', 'banana']  per lunghezza

conteggi = {"gatto": 1, "il": 3, "e": 2}
# ordinare le coppie (chiave, valore) per VALORE decrescente:
sorted(conteggi.items(), key=lambda coppia: coppia[1], reverse=True)
# [('il', 3), ('e', 2), ('gatto', 1)]
```

Una **lambda** è una funzione senza nome scritta su una riga: `lambda coppia: coppia[1]`
equivale a `def f(coppia): return coppia[1]`. `coppia[1]` è il secondo elemento (il valore).

Prendere i primi N elementi: `lista[:5]`.

## 6. Tuple e insiemi

**Tupla:** come una lista ma **immutabile**, tra parentesi tonde. Serve per gruppi di valori
che non cambiano (coordinate, coppie chiave-valore).

```python
punto = (3, 4)
x, y = punto           # "spacchettamento"
```

**Insieme (`set`):** raccolta **senza duplicati** e senza ordine.

```python
parole_uniche = set(["a", "b", "a"])    # {'a', 'b'}
len(parole_uniche)                       # 2
```

Utile per contare quanti valori diversi ci sono.

## 7. File

Per salvare dati tra una esecuzione e l'altra si usano i **file**.

```python
with open("voti.txt", "w", encoding="utf-8") as f:    # "w" = scrittura (azzera il file)
    f.write("7\n")
    f.write("9\n")

with open("voti.txt", "r", encoding="utf-8") as f:    # "r" = lettura
    righe = f.readlines()          # ['7\n', '9\n']
voti = [float(r.strip()) for r in righe]
```

- Modalità: `"r"` leggere, `"w"` scrivere (cancella il contenuto), `"a"` aggiungere in fondo.
- `with` chiude il file da solo anche in caso di errore: usalo sempre.
- `"\n"` è il carattere di a-capo; `write` non lo aggiunge da sé. `strip()` lo toglie in lettura.
- `encoding="utf-8"` evita problemi con le lettere accentate.
- Leggere un file che non esiste dà `FileNotFoundError`.
- `for riga in f:` scorre le righe una alla volta.

**Percorsi.** Un percorso relativo (`"voti.txt"`) è relativo alla cartella da cui si lancia
il programma, che può cambiare. Per essere sicuri di usare la cartella del file `.py`:

```python
from pathlib import Path
cartella = Path(__file__).parent
percorso = cartella / "voti.txt"          # l'operatore / unisce i pezzi
with open(percorso, "w", encoding="utf-8") as f:
    f.write("ciao")
```

Nel codice **non** si scrivono percorsi assoluti (`C:\Users\...`): non funzionerebbero su un
altro computer.

**Comprehension** (forma breve per costruire liste):
`[float(r.strip()) for r in righe]` equivale a un ciclo `for` che fa `append` per ogni riga.

## 8. JSON

Per salvare strutture (liste, dizionari) senza inventare un formato, si usa **JSON**.

```python
import json

registro = {"matematica": [7, 8], "storia": [6]}

with open("registro.json", "w", encoding="utf-8") as f:
    json.dump(registro, f, indent=2, ensure_ascii=False)

with open("registro.json", "r", encoding="utf-8") as f:
    registro = json.load(f)
```

`json.dump` scrive, `json.load` legge. Le chiavi JSON sono sempre testo; liste, numeri,
`True/False` si conservano.

## 9. Errori e try/except

Un errore (eccezione) ferma il programma. Con `try/except` si **intercetta** e si decide
cosa fare.

```python
try:
    eta = int(input("Età: "))
except ValueError:
    print("Non è un numero")
```

Struttura completa:

```python
try:
    ...                      # codice che potrebbe fallire
except ValueError:
    ...                      # eseguito se c'è un ValueError
except ZeroDivisionError:
    ...                      # un altro tipo di errore
else:
    ...                      # eseguito solo se NON ci sono stati errori
finally:
    ...                      # eseguito sempre (es. chiusure)
```

- Intercetta **il tipo specifico** di errore, non tutto indiscriminatamente: `except:` nudo
  nasconde anche i tuoi errori di programmazione.
- Il blocco `try` deve contenere **solo** il codice che può fallire.

**Schema per chiedere un valore valido, finché è valido:**

```python
def leggi_intero(messaggio):
    while True:
        testo = input(messaggio)
        try:
            return int(testo)          # return esce dalla funzione e dal ciclo
        except ValueError:
            print("Inserisci un numero intero.")
```

**Sollevare un errore da soli:**

```python
def radice(x):
    if x < 0:
        raise ValueError("x non può essere negativo")
    return x ** 0.5
```

## 10. Organizzare il codice

Per programmi più lunghi di poche righe:

1. **Funzioni piccole**, una per compito (`leggi_numero`, `mostra_menu`, `salva`, `carica`).
2. **Costanti** in alto, in maiuscolo: `LIMITE_TENTATIVI = 7`.
3. Una funzione `main()` che coordina il programma, chiamata solo se il file è eseguito
   direttamente:

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

4. **Menu** in un ciclo:

```python
while True:
    print("1) Aggiungi   2) Mostra   0) Esci")
    scelta = input("Scelta: ")
    if scelta == "1":
        ...
    elif scelta == "2":
        ...
    elif scelta == "0":
        break
    else:
        print("Scelta non valida")
```

5. Nomi chiari, commenti sul **perché** (non sul cosa), niente codice copiato e incollato:
se lo scrivi due volte, fanne una funzione.

## 11. Verificare con assert

`assert condizione` non fa nulla se la condizione è vera e dà errore (`AssertionError`) se è falsa.
È un modo veloce per **controllare da soli** che una funzione sia corretta.

```python
def e_pari(n):
    return n % 2 == 0

assert e_pari(4) is True
assert e_pari(7) is False
assert media([6, 8, 7]) == 7
print("Tutti i controlli superati")
```

Per confrontare decimali usa una tolleranza: `assert abs(risultato - 0.3) < 1e-9`
(perché `0.1 + 0.2` non è esattamente `0.3` nei calcolatori).

Negli esercizi, gli `assert` indicati nella descrizione servono a verificare il tuo lavoro
senza bisogno di nessuno che lo controlli.
