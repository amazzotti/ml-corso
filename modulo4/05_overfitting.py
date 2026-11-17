"""Esercizio 5 (Modulo 4) - Overfitting: la curva di complessita'.

Teoria: teoria/05_ml_classico.md, sezione 6.

OBIETTIVO
Vedere con un grafico l'overfitting: al crescere della complessita' del modello
l'accuratezza sul training sale sempre, quella sul test sale e poi SCENDE.

DATI: due "mezzelune" rumorose
    from sklearn.datasets import make_moons
    X, y = make_moons(n_samples=300, noise=0.3, random_state=0)
Sono 300 punti in 2 dimensioni, di 2 classi a forma di mezzaluna, con tanto
rumore: le classi si sovrappongono, quindi nessun modello puo' fare 100% sul
test (ed e' proprio per questo che l'overfitting si vede bene).
Dividi:  train_test_split(X, y, test_size=0.3, random_state=0)   -> 210 train, 90 test.

PASSI
1. Disegna i dati con uno scatter colorato per classe.
2. Per max_depth da 1 a 15 addestra un albero (random_state=0) e registra
   accuratezza di training e di test. Attesi (train / test), tra gli altri:
       depth  1:  0.838 / 0.733
       depth  2:  0.900 / 0.856
       depth  3:  0.905 / 0.844
       depth  5:  0.976 / 0.900     <- il test e' al massimo
       depth  7:  0.990 / 0.878
       depth  9:  1.000 / 0.844     <- training perfetto, test peggiorato
       depth 15:  1.000 / 0.844
3. Disegna le due curve (profondita' sull'asse x, accuratezza sull'asse y), con
   legenda "training" e "test". Aggiungi una linea verticale alla profondita' con
   il test migliore (np.argmax) e scrivi nel titolo il suo valore.
4. Disegna il CONFINE DI DECISIONE di tre alberi (profondita' 1, 5, 15) in un'unica
   figura con tre grafici affiancati:
       from sklearn.inspection import DecisionBoundaryDisplay
       DecisionBoundaryDisplay.from_estimator(albero, X, ax=ax, alpha=0.3)
       ax.scatter(X[:, 0], X[:, 1], c=y)
   Profondita' 1: una sola retta (UNDERFITTING). Profondita' 5: confine ragionevole.
   Profondita' 15: un confine frastagliato con "isole" attorno ai singoli punti
   (OVERFITTING: ha imparato il rumore).
5. In un commento scrivi quale profondita' sceglieresti e perche'.
   (Attenzione: scegliere guardando il test non e' corretto in un progetto vero.
   Qui e' solo un esperimento didattico; il metodo giusto e' la validazione o
   la cross-validation, esercizio 8.)

CONCETTI NUOVI
- Underfitting, overfitting, buon equilibrio.
- Divario tra training e test come diagnosi.
- Curva di complessita'.
- Confine di decisione.
- Con pochi campioni di test (90) ogni errore pesa l'1,1%: i numeri sono rumorosi.

COME VERIFICARE DA SOLO
    assert acc_train[0] < acc_train[-1] and acc_train[-1] == 1.0
    assert max(acc_test) > acc_test[-1]            # il test a profondita' massima non e' il migliore
    assert 3 <= int(np.argmax(acc_test)) + 1 <= 6  # il picco del test e' a profondita' intermedia
    assert abs(max(acc_test) - 0.900) < 0.012

ERRORI TIPICI
- Dimenticare random_state in make_moons o in train_test_split: numeri diversi.
- Calcolare entrambe le accuratezze sul test (la curva di training deve usare X_train).
- Dimenticare di ordinare le curve per profondita' crescente.
- Concludere "l'albero piu' profondo e' peggiore": dipende dai dati; qui c'e' molto rumore.

BONUS (facoltativo)
- Ripeti con noise=0.1 (rumore basso): l'overfitting e' meno marcato?
- Ripeti con n_samples=3000: piu' dati riducono l'overfitting? (Si'.)
- Prova a limitare con min_samples_leaf=10 invece di max_depth (altro modo di
  frenare la complessita').
- Fai la stessa curva con KNeighborsClassifier variando n_neighbors da 1 a 50:
  qui la complessita' e' il contrario (1 vicino = overfitting).

Scrivi il tuo codice qui sotto.
"""

