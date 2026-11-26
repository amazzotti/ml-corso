"""Esercizio 10 (Modulo 1) - Gestire gli errori con try/except.

Teoria: teoria/02_python_avanzato.md, sezione 9.

OBIETTIVO
Rendere i programmi "a prova di utente": se qualcuno scrive "ciao" dove
serve un numero, il programma NON si blocca con un errore, ma rifa' la
domanda.

PARTE A - leggi_intero(messaggio)
Scrivi una funzione che chiede un intero con input(messaggio) e, se
l'utente scrive qualcosa che non e' un intero, stampa "Inserisci un numero
intero." e richiede, finche' il valore e' valido. Alla fine RESTITUISCE
l'intero.
    eta = leggi_intero("Quanti anni hai? ")

PARTE B - leggi_intero_positivo(messaggio)
Come la A, ma accetta solo numeri maggiori di zero. Riusa leggi_intero!
Se il numero e' <= 0 stampa "Il numero deve essere positivo." e richiede.

PARTE C - dividi(a, b)
Restituisce a / b. Se b e' zero NON deve andare in errore: stampa
"Divisione per zero non possibile" e restituisce None.

PARTE D - leggi_file(nome)
Legge e restituisce tutto il testo del file indicato (con Path e with,
come nell'esercizio 9). Se il file non esiste (FileNotFoundError) stampa
"File non trovato" e restituisce una stringa vuota.

SCHEMA DA CONOSCERE
    def leggi_intero(messaggio):
        while True:
            testo = input(messaggio)
            try:
                return int(testo)       # return esce da funzione e ciclo
            except ValueError:
                print("Inserisci un numero intero.")

CONCETTI NUOVI
- try / except TipoDiErrore: il codice nel try viene eseguito; se si
  verifica QUELL'errore, si salta al blocco except invece di fermarsi.
- Tipi di errore da intercettare: ValueError (int("ciao")),
  ZeroDivisionError (1/0), FileNotFoundError (file inesistente).
- Si intercetta il tipo SPECIFICO: un "except:" nudo nasconde anche i
  tuoi errori di programmazione.
- Nel try si mette SOLO il codice che puo' fallire.
- raise ValueError("messaggio"): sollevare un errore da soli.

COME VERIFICARE DA SOLO
Per le parti C e D si puo' usare assert (le A e B richiedono di scrivere
nel terminale, provale a mano scrivendo "ciao", "3.5", "", "-4", "7"):
    assert dividi(10, 2) == 5
    assert dividi(1, 0) is None
    assert leggi_file("file_che_non_esiste.txt") == ""
Per le parti A e B prova questi input in sequenza e controlla che il
programma restituisca 7 senza mai andare in errore:
    ciao  ->  "Inserisci un numero intero."
    3.5   ->  "Inserisci un numero intero."   (int("3.5") fallisce!)
    (invio vuoto) -> "Inserisci un numero intero."
    7     ->  restituisce 7

ERRORI TIPICI
- Mettere tutto il programma dentro il try: nasconde i problemi.
- Dimenticare il ciclo while True: la domanda non viene ripetuta.
- except ValueError scritto senza il tipo (except:) .
- Pensare che int("3.5") funzioni: serve int(float("3.5")) o accettare
  solo interi.

BONUS (facoltativo)
- leggi_float(messaggio) per i decimali, che accetti anche la virgola
  come separatore ("3,5" -> 3.5) usando replace.
- Scrivi una funzione leggi_scelta(messaggio, valide) che accetta solo
  una scelta tra quelle in una lista, ad esempio ["s", "n"].
- Torna agli esercizi 06 (indovina) e 04 (calcolatrice) e proteggili con
  queste funzioni.
- Usa finally per stampare "Operazione terminata" qualunque cosa accada.

Scrivi il tuo codice qui sotto.
"""

def leggi_intero(messaggio):
    while True:
        testo = input(messaggio)
        try:
            return int(testo)       # return esce da funzione e ciclo
        except ValueError:
            print("Inserisci un numero intero.")


def leggi_intero_positivo(messaggio):
    while True:
        n = leggi_intero(messaggio)
        if n > 0:
            return n
        print("Il numero deve essere positivo.")


def dividi(a, b):
    if b == 0:
        print("Divisione per zero non possibile")
        return None
    return a / b


def leggi_file(nome):
    try:
        with open(nome, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("File non trovato")
        return ""


assert dividi(10, 2) == 5
assert dividi(1, 0) is None
assert leggi_file("file_che_non_esiste.txt") == ""
