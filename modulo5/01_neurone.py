"""Esercizio 1 (Modulo 5) - Un neurone scritto a mano.

Teoria: teoria/06_reti_neurali.md, sezioni 1 e 2.

OBIETTIVO
Scrivere con NumPy il calcolo di un neurone artificiale: somma pesata degli
ingressi, piu' bias, piu' funzione di attivazione.

LA FORMULA
       z = w . x + b          (prodotto scalare tra pesi e ingressi, piu' il bias)
       a = f(z)               (attivazione)

PASSI
1. Scrivi le attivazioni (con NumPy, valgono anche per interi array):
       def sigmoide(z): return 1 / (1 + np.exp(-z))
       def relu(z):     return np.maximum(0, z)
       tanh: usa np.tanh
2. Scrivi:
       def neurone(x, w, b, attivazione):
           z = np.dot(w, x) + b
           return attivazione(z)
3. Calcola a mano e poi con il codice:
   Esempio A:  x = [2, 3]   w = [0.4, -0.2]   b = 0.5
       z = 0.4*2 + (-0.2)*3 + 0.5 = 0.8 - 0.6 + 0.5 = 0.7
       sigmoide -> 0.6682     relu -> 0.7     tanh -> 0.6044
   Esempio B:  x = [1, 2]   w = [0.5, -0.9]   b = 0.1
       z = 0.5 - 1.8 + 0.1 = -1.2
       sigmoide -> 0.2315     relu -> 0.0     tanh -> -0.8337
   Osserva: la ReLU "spegne" il neurone (uscita 0) quando z e' negativo.
4. Un neurone che calcola una media pesata:
   x = [10, 20, 30], w = [0.5, 0.3, 0.2], b = 0, nessuna attivazione (identita'):
       z = 5 + 6 + 6 = 17.0
5. Interpreta in un commento: cosa succede se un peso e' zero? (l'ingresso
   corrispondente viene ignorato.) Se un peso e' molto grande? (quell'ingresso
   domina.) A cosa serve il bias? (sposta la soglia: a x = 0 il neurone puo'
   comunque dare un valore diverso da 0.)

PARTE B - TANTI CAMPIONI CON LE MATRICI
Con una matrice X di forma (N, d) (una riga per campione) lo stesso neurone si
calcola per tutti i campioni in una volta:
       Z = X @ w + b
Prova con:
       X = np.array([[2, 3], [1, 2], [0, 0]])
       w = np.array([0.4, -0.2]);  b = 0.5
       Z = X @ w + b           ->  [0.7, 0.1, 0.5]  (sigmoide: [0.668, 0.525, 0.622])
Controlla le forme: (3, 2) @ (2,) -> (3,).

CONCETTI NUOVI
- Neurone = modello lineare + attivazione non lineare.
- Pesi, bias, attivazione, uscita.
- Prodotto scalare np.dot e prodotto matrice-vettore X @ w.
- Tre attivazioni: sigmoide (0..1), tanh (-1..1), ReLU (0..infinito).

COME VERIFICARE DA SOLO
    assert abs(neurone(np.array([2, 3]), np.array([0.4, -0.2]), 0.5, sigmoide) - 0.6682) < 1e-3
    assert abs(neurone(np.array([2, 3]), np.array([0.4, -0.2]), 0.5, relu) - 0.7) < 1e-9
    assert abs(neurone(np.array([2, 3]), np.array([0.4, -0.2]), 0.5, np.tanh) - 0.6044) < 1e-3
    assert abs(neurone(np.array([1, 2]), np.array([0.5, -0.9]), 0.1, sigmoide) - 0.2315) < 1e-3
    assert neurone(np.array([1, 2]), np.array([0.5, -0.9]), 0.1, relu) == 0
    assert abs(np.dot([0.5, 0.3, 0.2], [10, 20, 30]) - 17) < 1e-9
    assert np.allclose(X @ w + b, [0.7, 0.1, 0.5])

ERRORI TIPICI
- Usare * invece di np.dot tra pesi e ingressi: ottieni un vettore, non un numero.
- Scrivere np.exp(z) invece di np.exp(-z) nella sigmoide: risultato rovesciato.
- Dimenticare il bias.
- Confondere z (prima dell'attivazione) con a (dopo).

BONUS (facoltativo)
- Calcola l'uscita di un neurone con attivazione a gradino (step: 1 se z > 0, altrimenti 0).
  Questo e' il neurone del perceptron (prossimo esercizio ma uno).
- Disegna come cambia l'uscita sigmoide del neurone A al variare del primo ingresso
  da -5 a 5 (gli altri parametri fissi).
- Cerca a mano pesi e bias per far comportare un neurone con ingressi 0/1 e gradino
  come una porta AND (suggerimento: w = [1, 1], b = -1.5).

Scrivi il tuo codice qui sotto.
"""

