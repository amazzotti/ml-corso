"""Esercizio 6 (Modulo 5) - Autograd: i gradienti li calcola PyTorch.

Teoria: teoria/06_reti_neurali.md, sezioni 5 e 9; teoria/04 (gradiente della regressione).

OBIETTIVO
Vedere PyTorch calcolare da solo, con la regola della catena, i gradienti che nel
Modulo 3 hai scritto a mano, e riscrivere il training loop della regressione lineare
senza nessuna formula di derivata.

PARTE A - UNA FUNZIONE SEMPLICE
       w = torch.tensor(2.0, requires_grad=True)
       y = w ** 2 + 3 * w
       y.backward()
       w.grad            ->  tensor(7.)
Controllo a mano: dy/dw = 2w + 3 = 7. PyTorch ha costruito il "grafo" delle operazioni
e ha applicato la regola della catena all'indietro (backpropagation!).
1. Prova con y = (3*w + 1) ** 2 in w = 1: gradiente 2*(3w+1)*3 = 24.
2. Prova con y = torch.sigmoid(w) in w = 0: gradiente s(1-s) = 0.25.
3. Piu' variabili: a = tensor(3.0, requires_grad), b = tensor(4.0, requires_grad);
   f = a * b + a ** 2  ->  df/da = b + 2a = 10,  df/db = a = 3.

PARTE B - ATTENZIONE: I GRADIENTI SI ACCUMULANO
1. Ripeti  y = w**2; y.backward()  due volte di fila (ricreando y ogni volta): w.grad passa da
   4 a 8! Ogni backward() SOMMA al valore precedente.
2. Per azzerare:  w.grad.zero_()   (in una rete: optimizer.zero_grad()).
3. Scrivi in un commento perche' serve azzerare a ogni passo (altrimenti si somma il gradiente
   di tutti i passi precedenti).

PARTE C - IL GRADIENTE DEL MODULO 3, SENZA FORMULE
Dati del Modulo 3 (seed 42, 50 punti) convertiti in tensori float64:
       xt = torch.tensor(x, dtype=torch.float64);  yt = torch.tensor(y, dtype=torch.float64)
       W = torch.tensor(0.0, dtype=torch.float64, requires_grad=True)
       B = torch.tensor(0.0, dtype=torch.float64, requires_grad=True)
       L = ((W * xt + B - yt) ** 2).mean()
       L.backward()
       W.grad.item(), B.grad.item()   ->  -153.77, -22.91
       L.item()                       ->  163.94
Sono ESATTAMENTE i numeri che hai calcolato a mano nell'esercizio 5 del Modulo 3: PyTorch
ha derivato da solo la perdita. Scrivi un assert che lo verifica con tolleranza 1e-6.

PARTE D - TRAINING LOOP CON AUTOGRAD
Riscrivi l'addestramento (lr = 0.01, 1000 epoche) usando autograd:
       for epoca in range(1000):
           L = ((W * xt + B - yt) ** 2).mean()
           L.backward()
           with torch.no_grad():          # l'aggiornamento non va tracciato
               W -= 0.01 * W.grad
               B -= 0.01 * B.grad
           W.grad.zero_();  B.grad.zero_()
Risultato atteso (identico al Modulo 3):  W = 2.0189,  B = 0.6476,  perdita 1.2903.
Nessuna formula di derivata: la backpropagation e' automatica.

PARTE E - NO_GRAD E DETACH
1. Dentro  with torch.no_grad():  le operazioni non vengono tracciate:
       with torch.no_grad(): z = W * 2     ->  z.requires_grad e' False
   Si usa in valutazione e negli aggiornamenti manuali.
2. t.detach() restituisce un tensore "staccato" dal grafo; .item() un numero Python.
3. Prova a fare un aggiornamento SENZA no_grad:  W -= 0.01 * W.grad
   Errore ("a leaf Variable that requires grad is being used in an in-place operation").
   Leggilo e spiegalo in un commento.

CONCETTI NUOVI
- requires_grad, backward(), .grad: differenziazione automatica.
- Il grafo computazionale: PyTorch ricorda le operazioni e le deriva all'indietro.
- Accumulo dei gradienti e necessita' di azzerarli.
- torch.no_grad() e detach().
- La backpropagation e' lo stesso meccanismo che hai scritto a mano nell'esercizio 4.

COME VERIFICARE DA SOLO
    assert w.grad.item() == 7.0                       # parte A
    assert abs(W.grad.item() + 153.7748) < 1e-3 and abs(B.grad.item() + 22.9092) < 1e-3   # parte C
    assert abs(L.item() - 163.9376) < 1e-3
    assert abs(W_finale - 2.0189) < 1e-3 and abs(B_finale - 0.6476) < 1e-3     # parte D

ERRORI TIPICI
- Dimenticare di azzerare i gradienti: l'addestramento "impazzisce".
- Chiamare backward() su un tensore non scalare: errore (la perdita deve essere un numero).
- Aggiornare i pesi fuori da no_grad.
- Mescolare float32 e float64.
- Dimenticare requires_grad=True: W.grad resta None.

BONUS (facoltativo)
- Verifica con la derivata numerica (esercizio 4 del Modulo 3) i gradienti trovati da autograd
  per la funzione  y = sin(w) * w**2  in w = 1.5.
- Calcola con autograd il gradiente della perdita rispetto a W1[0, 0] della rete XOR
  dell'esercizio 4 e confrontalo con quello della tua backpropagation a mano (0.009076
  con l'inizializzazione seed 0, float64).
- Prova torch.autograd.grad(y, w) invece di backward().

Scrivi il tuo codice qui sotto.
"""

