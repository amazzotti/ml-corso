# Teoria 1 — Python base

Appunti dei concetti incontrati negli esercizi dei Moduli 0 e 1, da rileggere quando serve.
Ogni sezione dice **cos'è**, **come si usa**, e **gli errori più comuni**.
Gli esempi si possono copiare in un file `.py` ed eseguire.

Indice: [1. Programma e interprete](#1-programma-e-interprete) ·
[2. print e stringhe](#2-print-e-stringhe) · [3. Variabili e tipi](#3-variabili-e-tipi) ·
[4. input e conversioni](#4-input-e-conversioni) · [5. f-string](#5-f-string) ·
[6. Operatori](#6-operatori) · [7. Confronti e condizioni](#7-confronti-e-condizioni) ·
[8. Cicli](#8-cicli) · [9. Liste](#9-liste) · [10. Dizionari](#10-dizionari) ·
[11. Leggere gli errori](#11-leggere-gli-errori)

---

## 1. Programma e interprete

Un programma è un elenco di istruzioni scritte in un file di testo (`.py`). L'**interprete**
Python legge il file **dall'alto verso il basso, una riga alla volta**, ed esegue ogni istruzione.

Conseguenza importante: se una riga dà errore, il programma si ferma lì. Le righe prima sono
già state eseguite, quelle dopo no.

**Ambiente virtuale (`.venv`):** una cartella con una copia isolata di Python e delle librerie
del progetto. Serve perché ogni progetto abbia le sue versioni, senza interferire con gli altri.
Le librerie elencate in `requirements.txt` si installano con `pip install -r requirements.txt`.

## 2. print e stringhe

`print` è una **funzione**: prende ciò che metti tra le parentesi e lo mostra a schermo.

```python
print("Ciao, mondo!")
print("Somma:", 2 + 3)     # più valori separati da virgola: uno spazio in mezzo
```

Il testo tra virgolette (`"..."` oppure `'...'`) è una **stringa** (`str`).
Una riga che inizia con `#` è un **commento**: Python la ignora, serve a spiegare il codice.

## 3. Variabili e tipi

Una **variabile** è un nome a cui si assegna un valore. Il simbolo `=` significa
"assegna", non "è uguale a".

```python
nome = "Marco"
eta = 30
altezza = 1.78
maggiorenne = True
```

Tipi principali:

| Tipo | Nome Python | Esempio |
|---|---|---|
| testo | `str` | `"ciao"` |
| intero | `int` | `42` |
| decimale | `float` | `3.14` |
| vero/falso | `bool` | `True`, `False` |

Con `type(x)` si vede il tipo. Il tipo conta: `"5" + "5"` dà `"55"` (testo incollato),
`5 + 5` dà `10`.

I nomi delle variabili: lettere, numeri e `_`, senza spazi, non iniziano con un numero.
Meglio nomi che dicono cosa contengono (`eta`, non `x`).

## 4. input e conversioni

`input("domanda")` mostra la domanda, aspetta che l'utente scriva e premi Invio, e restituisce
**sempre testo**, anche se si scrive `30`.

Per fare calcoli bisogna **convertire**:

```python
eta = int(input("Quanti anni hai? "))        # testo -> intero
numero = float(input("Numero: "))            # testo -> decimale
```

- `int("30")` → `30`; `float("2.5")` → `2.5`.
- Se il testo non è un numero (`int("ciao")`), Python dà `ValueError`. Si gestisce con
  `try/except` (vedi esercizi futuri).
- Trucco visto negli esercizi: `int(input("...") or 10)` usa 10 se l'utente preme solo Invio,
  perché una stringa vuota conta come "falso" e `or` passa al valore successivo.

## 5. f-string

La **f** sta per *formatted*. Si scrive una `f` prima delle virgolette; tutto ciò che sta tra
**graffe `{ }`** viene calcolato e sostituito con il suo valore.

```python
nome = "Marco"
eta = 30
print(f"{nome}, tra 10 anni avrai {eta + 10} anni")
# Marco, tra 10 anni avrai 40 anni
```

Senza la `f` le graffe sarebbero testo normale. Dentro le graffe va qualsiasi espressione:
`{eta * 2}`, `{nome.upper()}`, `{len(voti)}`.

Con la virgola in `print(a, b)` Python inserisce uno spazio tra i pezzi; con la f-string
decidi tu esattamente il testo.

## 6. Operatori

| Operatore | Significato | Esempio | Risultato |
|---|---|---|---|
| `+` | somma | `7 + 2` | `9` |
| `-` | differenza | `7 - 2` | `5` |
| `*` | prodotto | `7 * 2` | `14` |
| `/` | divisione (sempre decimale) | `7 / 2` | `3.5` |
| `//` | divisione intera | `7 // 2` | `3` |
| `%` | resto | `7 % 2` | `1` |
| `**` | potenza | `7 ** 2` | `49` |

- `x % 2 == 0` controlla se `x` è pari; `x % 3 == 0` se è multiplo di 3.
- `/` con numeri interi dà comunque un `float` (`4 / 2` → `2.0`).
- Dividere per zero dà `ZeroDivisionError`.
- Ordine delle operazioni come in matematica; le parentesi servono per forzarlo.

## 7. Confronti e condizioni

Un **confronto** dà `True` o `False`:

| Simbolo | Significato |
|---|---|
| `>` `<` | maggiore, minore |
| `>=` `<=` | maggiore o uguale, minore o uguale |
| `==` | uguale |
| `!=` | diverso |

**Attenzione:** `=` assegna, `==` confronta. Scrivere `if x = 5:` è un errore.

`if / elif / else` sceglie quale blocco eseguire:

```python
if numero > 0:
    print("positivo")
elif numero < 0:
    print("negativo")
else:
    print("zero")
```

Regole:
- i **due punti** `:` alla fine di `if`, `elif`, `else` sono obbligatori;
- le righe del blocco vanno **rientrate di 4 spazi** (tasto Tab in VS Code): l'indentazione fa
  parte del codice, senza il programma non parte;
- Python controlla dall'alto e **si ferma al primo ramo vero**: l'ordine conta;
- attenzione ai casi limite (es. 18 anni: `eta >= 18` e `eta > 18` danno risultati diversi).

Si possono combinare condizioni con `and`, `or`, `not`:
`if eta >= 18 and eta < 65:`.

## 8. Cicli

Un **ciclo** ripete un blocco di codice.

### for e range

```python
for i in range(1, 11):
    print(i)          # 1, 2, ..., 10
```

- `range(fine)` → da 0 a fine-1. `range(5)` → 0, 1, 2, 3, 4 (**5 valori**, non 6).
- `range(inizio, fine)` → da inizio a fine-1. Il valore `fine` è **escluso**.
- Per fare `N` giri si scrive `range(N)`; per andare da 1 a N compreso, `range(1, N + 1)`.
- Il blocco ripetuto è la parte **rientrata**.

### Accumulatore

Una variabile creata **prima** del ciclo e aggiornata a ogni giro:

```python
totale = 0
for i in range(1, 101):
    totale = totale + i      # si legge: nuovo totale = vecchio totale + i
print(totale)                # 5050, fuori dal ciclo
```

Se il `print` è rientrato, viene eseguito a ogni giro (100 stampe). Questa idea
("una variabile che migliora giro dopo giro") tornerà nell'addestramento di un modello.

### while

Ripete finché una condizione è vera:

```python
n = 0
while n < 3:
    print(n)
    n = n + 1
```

Se la condizione non diventa mai falsa il ciclo non finisce (ciclo infinito, si ferma con
Ctrl+C). `break` esce subito dal ciclo.

## 9. Liste

Una **lista** contiene più valori in ordine, tra parentesi quadre.

```python
voti = []                 # lista vuota
voti.append(7)            # aggiunge in fondo
voti.append(9)
print(voti)               # [7, 9]
print(voti[0])            # 7: le posizioni partono da 0
print(voti[-1])           # 9: l'ultimo
print(len(voti))          # 2: quanti elementi
```

Funzioni utili con liste di numeri: `sum(voti)`, `max(voti)`, `min(voti)`,
`sorted(voti)` (copia ordinata). **Media** = `sum(voti) / len(voti)`.

Scorrere una lista:

```python
for v in voti:
    print(v)
```

Errori comuni: indice fuori dalla lista (`voti[5]` con 2 elementi → `IndexError`);
dimenticare che il primo indice è 0.

Le liste sono la base di ciò che arriverà con NumPy e pandas: una colonna di dati è una
sequenza di valori su cui si fanno calcoli.

## 10. Dizionari

Un **dizionario** associa una **chiave** a un **valore**, tra parentesi graffe.

```python
rubrica = {"Anna": "333111222", "Marco": "347000111"}
print(rubrica["Anna"])            # 333111222
rubrica["Luca"] = "340555666"     # aggiunge (o modifica)
print("Anna" in rubrica)          # True: controlla se la chiave esiste
for nome, numero in rubrica.items():
    print(nome, numero)
print(rubrica.get("Zoe", "non trovato"))   # valore di riserva, niente errore
```

- Lista: si legge per **posizione** (`voti[0]`). Dizionario: per **chiave** (`rubrica["Anna"]`).
- Leggere una chiave che non esiste dà `KeyError`: si controlla prima con `in` o si usa `.get`.
- Le chiavi sono uniche. Il numero di telefono si tiene come **testo**: come numero intero
  perderebbe lo zero iniziale e non serve fare calcoli.
- Un dizionario è comodo anche come **contatore** (es. quante volte compare ogni parola).

## 11. Leggere gli errori

Quando Python va in errore stampa un **traceback**. Si legge **dal basso**:

1. L'ultima riga dice il **tipo di errore** e il motivo (`ZeroDivisionError: float division by zero`).
2. Subito sopra c'è il **file e il numero di riga** dove è successo, con la riga di codice.

Errori incontrati finora:

| Errore | Significato | Causa tipica |
|---|---|---|
| `ZeroDivisionError` | divisione per zero | secondo numero uguale a 0 |
| `ValueError` | valore non convertibile | `int("ciao")` |
| `KeyError` | chiave non presente | leggere `rubrica["Zoe"]` senza controllare |
| `IndexError` | posizione inesistente | `voti[5]` in una lista corta |
| `EOFError` | l'input è finito | più `input()` di quanti dati forniti (es. ciclo che gira una volta di troppo) |
| `IndentationError` | rientro sbagliato | righe del blocco non rientrate |
| `SyntaxError` | sintassi non valida | manca `:` o una parentesi |

Abitudine utile: prima di cercare altrove, leggere con calma l'ultima riga e il numero di riga.
