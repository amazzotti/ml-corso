"""Esercizio 4 (Modulo 3) - La pendenza, calcolata numericamente.

Teoria: teoria/04_regressione_gradient_descent.md, sezione 5.

OBIETTIVO
Capire la derivata come "pendenza" e calcolarla senza formule, spostando un
parametro di pochissimo e guardando di quanto cambia il risultato. Poi usarla
sulla perdita dell'esercizio 3 per capire in quale direzione muoversi.

PARTE A - DERIVATA DI UNA FUNZIONE SEMPLICE
1. Scrivi:
       def derivata(f, x, eps=1e-5):
           return (f(x + eps) - f(x - eps)) / (2 * eps)
   (differenza "centrata": si guarda un pelo a destra e un pelo a sinistra.)
2. Prova con  f(t) = t**2  (cioe' f = lambda t: t ** 2):
       derivata(f, 3)   ->  circa 6        (la formula e' 2t = 6)
       derivata(f, 0)   ->  circa 0        (fondo della parabola: piatto)
       derivata(f, -2)  ->  circa -4       (la funzione scende)
3. Prova con f(t) = 3*t + 1:  derivata -> 3 ovunque (una retta ha pendenza costante).
4. Prova con f(t) = (3*t + 1)**2 in t = 1: la regola della catena da'
   2 * (3t+1) * 3 = 24. Verifica con la derivata numerica.

PARTE B - DERIVATA PARZIALE DELLA PERDITA
Usa i dati dell'esercizio 1 (seed 42) e le funzioni predici e mse.
1. Definisci la perdita come funzione dei due parametri:
       def L(w, b):
           return mse(predici(x, w, b), y)
2. Calcola nel punto (w, b) = (0, 0):
       dL_dw = (L(0 + eps, 0) - L(0 - eps, 0)) / (2 * eps)
       dL_db = (L(0, 0 + eps) - L(0, 0 - eps)) / (2 * eps)
   Cambia SOLO un parametro alla volta (derivate parziali).
   Risultati attesi:
       dL/dw  ->  -153.77
       dL/db  ->   -22.91
3. Interpretazione, da scrivere in un commento:
   - Il segno e' NEGATIVO: aumentando w la perdita SCENDE. Quindi, per ridurla,
     bisogna spostare w verso destra (aumentarlo).
   - Il valore e' grande: la perdita e' molto "ripida" rispetto a w in (0, 0).
4. Calcola le derivate numeriche nel punto (2, 1), vicino al minimo:
       dL/dw -> circa 2.40      dL/db -> circa 0.50
   Piccole: vicino al fondo la valle e' quasi piatta. Spiegalo in un commento.

CONCETTI NUOVI
- Derivata = pendenza = di quanto cambia f se sposto un po' l'ingresso.
- Derivata positiva: f sale; negativa: scende; zero: punto piatto.
- Derivata numerica (differenze finite) con eps piccolo.
- Derivate PARZIALI: si muove un parametro solo, tenendo fermo l'altro.
- Il vettore delle derivate parziali e' il GRADIENTE: indica la direzione di
  massima salita. Per scendere si va nella direzione OPPOSTA.

COME VERIFICARE DA SOLO
    assert abs(derivata(lambda t: t ** 2, 3) - 6) < 1e-4
    assert abs(derivata(lambda t: t ** 2, -2) + 4) < 1e-4
    assert abs(derivata(lambda t: 3 * t + 1, 10) - 3) < 1e-4
    assert abs(derivata(lambda t: (3 * t + 1) ** 2, 1) - 24) < 1e-3
    assert abs(dL_dw_0_0 + 153.77) < 0.05 and abs(dL_db_0_0 + 22.91) < 0.05
    assert abs(dL_dw_2_1 - 2.40) < 0.05 and abs(dL_db_2_1 - 0.50) < 0.05

ERRORI TIPICI
- eps troppo piccolo (1e-12): errori di arrotondamento dei decimali, il
  risultato diventa rumoroso. 1e-5 va bene.
- eps troppo grande (0.5): non e' piu' una "pendenza locale".
- Cambiare w e b contemporaneamente nelle differenze: non e' una derivata parziale.
- Dimenticare di dividere per 2 * eps.

BONUS (facoltativo)
- Confronta la differenza "in avanti" (f(x+eps) - f(x)) / eps con quella
  centrata sulla funzione t**3 in t = 2 (vero: 12): quale e' piu' precisa
  con eps = 1e-3?
- Disegna la tangente alla parabola in t = 3: y = 9 + 6*(t - 3).
- Prova a "scendere" a mano: parti da w = 0 e, usando la derivata numerica,
  sposta w di 0.001 volte la derivata (con il segno giusto, cioe' meno).
  Ripeti 10 volte e osserva che la perdita cala. Hai appena fatto, con le
  tue mani, il gradient descent: nei prossimi esercizi lo scriviamo bene.

Scrivi il tuo codice qui sotto.
"""

