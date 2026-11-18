"""Esercizio 5 (Modulo 5) - Tensori in PyTorch.

Prima di iniziare:  pip install torch torchvision     (ambiente .venv attivo; ~200 MB, CPU)
Teoria: teoria/06_reti_neurali.md, sezione 9.

OBIETTIVO
Prendere confidenza con i tensori, l'equivalente PyTorch degli array NumPy: stesse
operazioni, ma capaci di calcolare gradienti (esercizio successivo).

PARTE A - CREARE E OSSERVARE
    import torch
1. a = torch.tensor([1.0, 2.0, 3.0])
   Stampa a.shape -> torch.Size([3]);  a.dtype -> torch.float32 (il tipo di default dei decimali).
2. b = torch.tensor([1, 2, 3]) -> dtype torch.int64 (interi).
   Prova b.mean(): errore! Le medie richiedono decimali. Soluzione: b.float().mean() -> 2.0.
3. torch.zeros(2, 3) (forma (2, 3)),  torch.ones(3),  torch.arange(0, 10, 2) -> [0, 2, 4, 6, 8],
   torch.linspace(0, 1, 5) -> [0.0, 0.25, 0.5, 0.75, 1.0].
4. Numeri casuali ripetibili:
       torch.manual_seed(0)
       r = torch.rand(3)          # uniformi in [0, 1)
   (Il seed serve per esperimenti riproducibili, come default_rng(42) in NumPy.)

PARTE B - OPERAZIONI (uguali a NumPy)
1. a * 2 -> [2., 4., 6.];  a + a -> [2., 4., 6.];  a ** 2 -> [1., 4., 9.].
2. a @ a  (prodotto scalare) -> tensor(14.)  (1 + 4 + 9);  a.sum() -> 6;  a.mean() -> 2;  a.max() -> 3.
3. Matrici:
       M = torch.tensor([[1., 2.], [3., 4.]])
       N = torch.tensor([[0., 1.], [1., 0.]])
       M @ N -> [[2., 1.], [4., 3.]]       M * N -> [[0., 2.], [3., 0.]]
       M.T -> [[1., 3.], [2., 4.]]          M.sum(dim=0) -> [4., 6.]   M.sum(dim=1) -> [3., 7.]
   (In PyTorch l'asse si chiama dim; in NumPy axis.)
4. Slicing come in NumPy: M[0] -> [1., 2.];  M[:, 1] -> [2., 4.];  M[1, 0] -> tensor(3.)
5. Per ottenere un numero Python da un tensore scalare:  M[1, 0].item() -> 3.0.

PARTE C - DA E VERSO NUMPY
    import numpy as np
    n = np.array([1.0, 2.0, 3.0])
    t = torch.from_numpy(n)        # tensore (float64!)
    t32 = t.float()                # float32: il tipo che si usa in rete
    ritorno = t32.numpy()          # di nuovo array NumPy
Attenzione: from_numpy e numpy() CONDIVIDONO la memoria: se modifichi n[0] = 100, cambia anche t.
Verificalo. Per una copia indipendente usa torch.tensor(n) o t.clone().

PARTE D - FORME E VISTE (servono per le immagini)
1. x = torch.arange(12) -> forma (12,).
2. x.reshape(3, 4)  e  x.view(3, 4)  -> matrice 3 x 4.
3. Un'immagine MNIST ha forma (1, 28, 28): un canale, 28 righe, 28 colonne. Un batch di 64 immagini
   (64, 1, 28, 28). Crea un tensore finto: img = torch.rand(64, 1, 28, 28) e appiattiscilo
   per una rete densa:
       img.view(64, -1).shape  ->  torch.Size([64, 784])      (-1 = "calcolalo tu": 1*28*28)
4. img.shape[0] -> 64 (numero di campioni);  img.numel() -> 64*784 = 50176.

PARTE E - UN NEURONE CON I TENSORI (ripasso dell'esercizio 1)
       x = torch.tensor([2.0, 3.0]);  w = torch.tensor([0.4, -0.2]);  b = torch.tensor(0.5)
       z = w @ x + b                      ->  tensor(0.7000)
       torch.sigmoid(z)                   ->  tensor(0.6682)
       torch.relu(z) -> 0.7;  torch.tanh(z) -> 0.6044
Stessi numeri dell'esercizio 1: sono la stessa matematica, in un'altra libreria.

CONCETTI NUOVI
- Tensore: array multidimensionale con dtype (float32 di default) e capacita' di tracciare gradienti.
- Convenzioni PyTorch: dim al posto di axis; .item() per i numeri; .float(), .long() per cambiare tipo.
- Condivisione della memoria con NumPy.
- reshape/view, -1, forme di immagini e batch.

COME VERIFICARE DA SOLO
    assert a.dtype == torch.float32 and tuple(a.shape) == (3,)
    assert (a @ a).item() == 14.0
    assert (M @ N).tolist() == [[2., 1.], [4., 3.]]
    assert M.sum(dim=1).tolist() == [3., 7.]
    assert img.view(64, -1).shape == (64, 784)
    assert abs(torch.sigmoid(z).item() - 0.6682) < 1e-3

ERRORI TIPICI
- Mescolare float32 e float64 (da from_numpy): "expected scalar type Float but found Double".
  Soluzione: .float().
- b.mean() su interi: errore. Converti a float.
- Dimenticare .item() e stampare "tensor(3.)" invece di 3.0 dove serve un numero Python.
- view() su un tensore non contiguo: usa reshape().
- Modificare t e stupirsi che n cambi (memoria condivisa).

BONUS (facoltativo)
- Se hai una GPU NVIDIA: torch.cuda.is_available() e t.to("cuda"). (Il corso funziona
  anche solo con la CPU.)
- Misura il tempo di un prodotto tra due matrici 1000 x 1000 in NumPy e in PyTorch.
- Prova torch.stack, torch.cat e torch.where.

Scrivi il tuo codice qui sotto.
"""

