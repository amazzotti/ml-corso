"""Esercizio 2 (Modulo 5) - Le funzioni di attivazione.

Teoria: teoria/06_reti_neurali.md, sezione 2.

OBIETTIVO
Scrivere le funzioni di attivazione e le loro derivate, disegnarle e capire
perche' servono (non linearita') e perche' la ReLU ha sostituito la sigmoide
negli strati nascosti (gradienti che svaniscono).

PARTE A - LE FUNZIONI
Scrivile con NumPy:
       sigmoide(z) = 1 / (1 + e^-z)
       tanh(z)     = np.tanh(z)
       relu(z)     = max(0, z)
       softmax(v)  = e^vi / somma(e^vj)  (per un vettore)
Valori di controllo:
       sigmoide([-2, 0, 2])  ->  [0.1192, 0.5, 0.8808]
       tanh([-2, 0, 2])      ->  [-0.9640, 0, 0.9640]
       relu([-2, 0, 2])      ->  [0, 0, 2]
       softmax([1, 2, 3])    ->  [0.0900, 0.2447, 0.6652]   (somma 1)

SOFTMAX STABILE
Prova softmax([1000, 1001, 1002]) con la formula ingenua: nan (e^1000 e' infinito).
Correggi sottraendo il massimo prima di calcolare gli esponenziali:
       def softmax(v):
           e = np.exp(v - np.max(v))
           return e / e.sum()
Il risultato e' lo stesso di softmax([0, 1, 2]) = [0.0900, 0.2447, 0.6652]:
la softmax non cambia se si sommano costanti a tutti gli elementi.

PARTE B - DERIVATE
       sigmoide'(z) = s(z) * (1 - s(z))
       tanh'(z)     = 1 - tanh(z)^2
       relu'(z)     = 1 se z > 0, altrimenti 0
Controlla ogni derivata con la derivata numerica (differenze finite, come nell'esercizio 4
del Modulo 3) in z = -1.5, 0.3, 2.0 con tolleranza 1e-6.
Valori: sigmoide'(0) = 0.25 (il massimo); relu'(-3) = 0; relu'(3) = 1.

PARTE C - GRAFICI (salva in modulo5/grafici/02_attivazioni.png)
Con z = np.linspace(-6, 6, 300) disegna in una figura con 2 righe x 3 colonne:
   riga 1: sigmoide, tanh, ReLU;   riga 2: le loro derivate.
Osserva e scrivi in un commento:
- la sigmoide schiaccia tutto in (0, 1); la sua derivata e' una campana alta al massimo
  0.25 e quasi zero per |z| > 5;
- la ReLU ha derivata 1 per tutti i valori positivi.

PARTE D - GRADIENTI CHE SVANISCONO
1. Calcola sigmoide'(10): circa 4.5e-5. Praticamente zero!
2. Immagina una rete con 10 strati sigmoide: nel caso migliore (derivata 0.25 a ogni
   strato) il gradiente viene moltiplicato per 0.25^10 = circa 9.5e-7. I primi strati
   non imparano. Calcolalo: 0.25 ** 10.
3. Con la ReLU in zona positiva la derivata e' 1: 1 ** 10 = 1. Il gradiente non si
   smorza. Scrivi la conclusione in un commento.

PARTE E - SENZA NON LINEARITA' (ragionamento)
Prova con NumPy: due strati lineari in fila (W1 e W2 casuali, senza attivazione):
       y1 = (x @ W1) @ W2
Verifica che e' identico a un unico strato con la matrice W = W1 @ W2:
       y2 = x @ (W1 @ W2)        np.allclose(y1, y2) -> True
Conclusione: senza attivazione non lineare, 100 strati equivalgono a UNO.

CONCETTI NUOVI
- Sigmoide, tanh, ReLU, softmax e le loro proprieta'.
- Derivate delle attivazioni (servono per la backpropagation).
- Gradienti che svaniscono (vanishing gradient).
- Stabilita' numerica: sottrarre il massimo nella softmax.
- La non linearita' e' essenziale: composizione di lineari = lineare.

COME VERIFICARE DA SOLO
    assert np.allclose(sigmoide(np.array([-2, 0, 2.0])), [0.1192, 0.5, 0.8808], atol=1e-3)
    assert np.allclose(np.tanh(np.array([-2, 0, 2.0])), [-0.9640, 0, 0.9640], atol=1e-3)
    assert list(relu(np.array([-2, 0, 2]))) == [0, 0, 2]
    assert np.allclose(softmax(np.array([1.0, 2.0, 3.0])), [0.0900, 0.2447, 0.6652], atol=1e-3)
    assert abs(softmax(np.array([1000.0, 1001.0, 1002.0])).sum() - 1) < 1e-9
    assert abs(derivata_sigmoide(0.0) - 0.25) < 1e-12
    assert derivata_relu(-3.0) == 0 and derivata_relu(3.0) == 1
    assert abs(derivata_sigmoide(10.0) - 4.54e-5) < 1e-6

ERRORI TIPICI
- Usare math.exp con array (funziona solo con numeri singoli): usa np.exp.
- Softmax calcolata senza sottrarre il massimo: nan per numeri grandi.
- np.max(0, z) invece di np.maximum(0, z): np.max fa un'altra cosa.
- Applicare la softmax per riga o per colonna in modo sbagliato quando si lavora
  con matrici (axis!).

BONUS (facoltativo)
- Scrivi la "leaky ReLU": z se z > 0, altrimenti 0.01 * z. Perche' puo' essere utile?
  (La ReLU puo' "morire": con z sempre negativo il gradiente e' sempre 0.)
- Estendi softmax a matrici (una riga per campione) con axis=1 e keepdims=True.
- Disegna la sigmoide con la sua tangente in z = 0 (pendenza 0.25).

Scrivi il tuo codice qui sotto.
"""

