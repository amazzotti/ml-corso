"""Progetto (Modulo 6) - Passo 1: i dati MNIST.

PROGETTO COMPLETO: riconoscere cifre scritte a mano (0-9) con una rete neurale in PyTorch.
Sei passi (file 01 ... 06). Ogni passo usa quello che hai imparato nei moduli precedenti.
Teoria: teoria/06_reti_neurali.md e teoria/05_ml_classico.md.

Prima di iniziare:  pip install torch torchvision matplotlib scikit-learn

OBIETTIVO DI QUESTO PASSO
Scaricare il dataset, guardare i dati con i tuoi occhi, capirne forma e valori, e preparare i
DataLoader con la normalizzazione corretta.

IL DATASET
MNIST: 70.000 immagini in bianco e nero di cifre scritte a mano, 28 x 28 pixel.
- 60.000 per l'addestramento (train), 10.000 per il test.
- Ogni immagine ha un'etichetta (la cifra, da 0 a 9).
Cartella dei dati: modulo6/data (ignorata da git: e' scaricabile di nuovo).

PASSI
1. Percorso dei dati accanto al file (nessun percorso assoluto):
       from pathlib import Path
       cartella_dati = Path(__file__).parent / "data"
2. Carica con torchvision:
       from torchvision import datasets, transforms
       trasformazione = transforms.ToTensor()
       train = datasets.MNIST(cartella_dati, train=True, download=True, transform=trasformazione)
       test  = datasets.MNIST(cartella_dati, train=False, download=True, transform=trasformazione)
   (La prima volta serve Internet: circa 12 MB.)
3. Stampa:
       len(train) -> 60000      len(test) -> 10000
       immagine, etichetta = train[0]
       immagine.shape -> torch.Size([1, 28, 28])    (canali, righe, colonne: 1 canale = grigi)
       immagine.min(), immagine.max()  ->  0.0 e 1.0 (ToTensor porta i pixel in [0, 1])
       etichetta -> 5  (il primo esempio e' un "5")
4. Quanti campioni per cifra nel training set?  np.bincount(train.targets.numpy())
       [5923, 6742, 5958, 6131, 5842, 5421, 5918, 6265, 5851, 5949]
   Dataset quasi bilanciato (la cifra 5 e' la meno frequente, la 1 la piu' frequente).
   Domanda: qual e' l'accuratezza di un modello che risponde sempre "1"?
   6742 / 60000 = circa 11,2%: il riferimento da battere e' molto basso.
5. Disegna una griglia 2 x 5 con la prima immagine di ciascuna cifra, con l'etichetta come titolo
   (ax.imshow(img.squeeze(), cmap="gray"); ax.axis("off")). Salva in modulo6/grafici/01_cifre.png.
   Guarda: la stessa cifra e' scritta in modi molto diversi. Questo e' il problema.
6. Disegna anche 20 esempi della stessa cifra (per esempio i "7") per vedere la variabilita'.
7. NORMALIZZAZIONE. Le reti addestrano meglio con ingressi centrati (teoria 04 e 06).
   MNIST ha media 0.1307 e deviazione standard 0.3081 sui pixel. Costruisci:
       trasformazione = transforms.Compose([
           transforms.ToTensor(),
           transforms.Normalize((0.1307,), (0.3081,)),
       ])
   e ricarica i dataset. Verifica su un campione di 5000 immagini che la media dei pixel sia
   vicina a 0 e la deviazione standard vicina a 1:
       lotto = torch.stack([train[i][0] for i in range(5000)])
       lotto.mean() -> circa 0     lotto.std() -> circa 1
   Il valore minimo ora e' circa -0.424 (il nero) e il massimo circa 2.82 (il bianco).
8. DataLoader per i mini-batch:
       from torch.utils.data import DataLoader
       dati_train = DataLoader(train, batch_size=64, shuffle=True)
       dati_test  = DataLoader(test, batch_size=1000)
   Prendi il primo batch:  X, y = next(iter(dati_train))
       X.shape -> torch.Size([64, 1, 28, 28])     y.shape -> torch.Size([64])
   Quanti passi per epoca? len(dati_train) -> 938   (60000 / 64 = 937,5 -> 938)
   Perche' shuffle=True solo per il train? (Mescolare i campioni a ogni epoca evita che la
   rete impari l'ordine; per il test non serve.)
9. Scrivi in un commento le risposte: quanti campioni, quante classi, che forma ha un'immagine,
   perche' normalizziamo, quanti batch per epoca.

CONCETTI NUOVI
- Dataset di immagini, canali, forma (canali, altezza, larghezza).
- transforms: ToTensor (pixel in [0, 1]) e Normalize (media 0, deviazione 1).
- DataLoader: mini-batch, shuffle.
- Il riferimento banale (classe piu' frequente) e' ~11%.

COME VERIFICARE DA SOLO
    assert len(train) == 60000 and len(test) == 10000
    assert tuple(immagine.shape) == (1, 28, 28)
    assert np.bincount(train.targets.numpy()).tolist() == [5923, 6742, 5958, 6131, 5842, 5421, 5918, 6265, 5851, 5949]
    assert abs(lotto.mean().item()) < 0.05 and abs(lotto.std().item() - 1) < 0.05
    assert tuple(X.shape) == (64, 1, 28, 28) and len(dati_train) == 938

ERRORI TIPICI
- Dimenticare download=True la prima volta (FileNotFoundError).
- Scrivere un percorso assoluto invece di Path(__file__).parent.
- Scaricare in una cartella che poi finisce nel repository: i dati NON vanno pubblicati
  (la cartella data/ e' gia' nel .gitignore).
- Applicare Normalize prima di ToTensor: l'ordine nel Compose conta.
- Dimenticare che le etichette in train.targets sono un tensore: usa .numpy() per np.bincount.

BONUS (facoltativo)
- Calcola tu media e deviazione standard su TUTTO il training set (train.data.float() / 255)
  e verifica 0.1307 e 0.3081.
- Disegna la media di tutte le immagini di ciascuna cifra (un'immagine "tipica" per cifra).
- Disegna l'istogramma dei valori dei pixel: quasi tutti sono 0 (sfondo).

Scrivi il tuo codice qui sotto.
"""

