"""Esercizio 3 (Modulo 2) - Matrici con NumPy.

Teoria: teoria/03_numpy_pandas.md, sezioni 1 e 4.

OBIETTIVO
Creare matrici, leggerne sezioni, fare somme per riga/colonna, trasposta e
prodotto matriciale. E' la base di cio' che farai nelle reti neurali.

PARTE A - FORMA E INDICI
    M = np.arange(12).reshape(3, 4)
Stampa M e controlla:
    M.shape      ->  (3, 4)
    M[1, 2]      ->  6            (riga 1, colonna 2)
    M[0]         ->  [0 1 2 3]    (prima riga)
    M[:, 0]      ->  [0 4 8]      (prima colonna)
    M[1:, :2]    ->  [[4 5] [8 9]] (dalla riga 1 in poi, prime due colonne)
    M.T.shape    ->  (4, 3)       (trasposta)
    M.reshape(2, 6).shape -> (2, 6)

PARTE B - SOMME E MEDIE LUNGO UN ASSE
    M.sum(axis=0)   ->  [12 15 18 21]   (una somma per COLONNA)
    M.sum(axis=1)   ->  [ 6 22 38]      (una somma per RIGA)
    M.mean(axis=0)  ->  [4. 5. 6. 7.]
Spiega a parole (in un commento) che cosa significa axis=0 e axis=1.

PARTE C - PRODOTTO MATRICIALE
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[0, 1], [1, 0]])
1. Calcola A @ B  ->  [[2 1] [4 3]]
   Verificalo A MANO riga per colonna e scrivi i passaggi in un commento.
2. Calcola A * B  ->  [[0 2] [3 0]]   (elemento per elemento).
   Perche' i due risultati sono diversi?
3. Prodotto non commutativo: confronta A @ B con B @ A.
   B @ A  ->  [[3 4] [1 2]]

PARTE D - UN LIVELLO DI RETE (anticipazione)
Una rete prende 3 caratteristiche in ingresso e produce 2 numeri in uscita.
Dati:
    X = np.array([[1, 2, 3],
                  [4, 5, 6]])         # 2 campioni, 3 caratteristiche  -> shape (2, 3)
    W = np.array([[1, 0],
                  [0, 1],
                  [1, 1]])            # pesi: 3 ingressi, 2 uscite    -> shape (3, 2)
    b = np.array([10, 20])            # un "bias" per ciascuna uscita
Calcola   Y = X @ W + b
    Y  ->  [[14 25] [20 31]]
Controlla le forme: (2, 3) @ (3, 2) = (2, 2). Il bias di forma (2,) viene
sommato a ogni riga (broadcasting).
Verifica a mano il primo elemento: 1*1 + 2*0 + 3*1 + 10 = 14.

CONCETTI NUOVI
- Matrice = array a 2 dimensioni, shape (righe, colonne).
- Indicizzazione a due indici M[riga, colonna], slicing per righe e colonne.
- reshape, trasposta (.T).
- axis=0 (lungo le righe, risultato per colonna), axis=1 (per riga).
- @ (prodotto matriciale) contro * (elemento per elemento).
- Regola delle forme: (a, b) @ (b, c) -> (a, c).
- Broadcasting del bias.

COME VERIFICARE DA SOLO
    assert M[1, 2] == 6
    assert list(M[:, 0]) == [0, 4, 8]
    assert M.T.shape == (4, 3)
    assert list(M.sum(axis=0)) == [12, 15, 18, 21]
    assert list(M.sum(axis=1)) == [6, 22, 38]
    assert (A @ B).tolist() == [[2, 1], [4, 3]]
    assert (A * B).tolist() == [[0, 2], [3, 0]]
    assert (B @ A).tolist() == [[3, 4], [1, 2]]
    assert (X @ W + b).tolist() == [[14, 25], [20, 31]]

ERRORI TIPICI
- Usare * invece di @ e ottenere un risultato diverso (senza errore!).
- ValueError "shapes (a,b) and (c,d) not aligned": le dimensioni interne
  non coincidono. Stampa .shape di entrambi.
- Confondere righe e colonne negli indici: M[1, 2] e' riga 1, colonna 2.
- Dimenticare che reshape richiede lo stesso numero totale di elementi.

BONUS (facoltativo)
- Matrice identita' con np.eye(3): verifica che M[:, :3] @ np.eye(3) lasci
  invariata la parte di matrice.
- Calcola la matrice dei quadrati e la sua somma totale.
- Prova np.linalg.inv(A) e controlla che A @ inversa dia (circa) l'identita'.
- Cosa succede con A @ np.array([1, 2])? Che forma ha il risultato?

Scrivi il tuo codice qui sotto.
"""

