"""Esercizio 7 (Modulo 2) - Tre grafici con matplotlib.

Teoria: teoria/03_numpy_pandas.md, sezioni 8 e 9.

OBIETTIVO
Disegnare tre grafici di tipo diverso, ciascuno con titolo, etichette degli
assi e griglia, e salvarli come immagini nella cartella "grafici".

GRAFICO 1 - LINEA: y = x al quadrato
    x = np.linspace(-5, 5, 100)
    y = x ** 2
Disegna con ax.plot(x, y, label="y = x^2"). Aggiungi una linea
orizzontale tratteggiata a y = 10 con ax.axhline(10, linestyle="--").
Titolo, etichette "x" e "y", legenda, griglia.
Controlla visivamente: una parabola con il minimo in (0, 0).

GRAFICO 2 - ISTOGRAMMA: altezze
    rng = np.random.default_rng(0)
    altezze = rng.normal(170, 10, 1000)
Disegna ax.hist(altezze, bins=30). Aggiungi una linea verticale tratteggiata
sulla media con ax.axvline(altezze.mean(), linestyle="--").
Etichette "altezza (cm)" e "numero di persone".
Controlla: forma a campana centrata intorno a 170; circa il 68% dei valori
tra 160 e 180 (verificalo: np.mean((altezze > 160) & (altezze < 180))).

GRAFICO 3 - SCATTER: una retta con rumore
    rng = np.random.default_rng(1)
    x = rng.uniform(0, 10, 80)
    y = 2 * x + 1 + rng.normal(0, 1.5, 80)
Disegna ax.scatter(x, y). Sovrapponi la retta vera y = 2x + 1 con
ax.plot(...). Etichette e legenda ("dati", "retta vera").
Controlla: nuvola di punti lungo una retta crescente. Questi sono i dati
che userai nel Modulo 3 per la regressione lineare!

SALVATAGGIO
    from pathlib import Path
    cartella = Path(__file__).parent / "grafici"
    cartella.mkdir(exist_ok=True)
    fig.savefig(cartella / "01_parabola.png", dpi=150, bbox_inches="tight")
Salva i tre grafici come 01_parabola.png, 02_altezze.png, 03_scatter.png.
La cartella "grafici" e' ignorata da git (sono file generati).

BONUS - TRE GRAFICI IN UNA FIGURA
    fig, assi = plt.subplots(1, 3, figsize=(15, 4))
    assi[0].plot(...);  assi[1].hist(...);  assi[2].scatter(...)
    fig.tight_layout()
Usa questa modalita' per salvare anche "tutti_insieme.png".

CONCETTI NUOVI
- Figura (fig) e assi (ax): fig, ax = plt.subplots(figsize=(6, 4)).
- plot (linea), hist (istogramma), scatter (punti).
- set_title, set_xlabel, set_ylabel, legend, grid.
- axhline / axvline: linee di riferimento.
- savefig e Path.mkdir per salvare i risultati.
- Quale grafico per quale dato: vedi la sezione 9 della teoria.

COME VERIFICARE DA SOLO
- Apri i tre PNG in VS Code. Ogni grafico deve avere: titolo, entrambi gli assi
  etichettati, griglia, legenda dove ci sono piu' elementi.
- Istogramma: la linea della media cade al centro della campana.
- Scatter: la retta vera passa "in mezzo" ai punti.
    assert (cartella / "01_parabola.png").exists()
    assert (cartella / "02_altezze.png").exists()
    assert (cartella / "03_scatter.png").exists()

ERRORI TIPICI
- Dimenticare plt.show(): non compare nessuna finestra (se serve vederla).
  Chiudi la finestra per far proseguire il programma.
- Disegnare tutto sullo stesso asse senza creare una nuova figura: i grafici
  si sovrappongono. Crea una figura per grafico.
- Dimenticare le etichette: un grafico senza etichette non comunica.
- Chiamare savefig DOPO plt.show(): il file risulta vuoto. Salva prima.

BONUS (facoltativo)
- Grafico a barre del voto medio per citta' usando i dati di studenti.csv.
- Cambia i colori, lo stile delle linee, la dimensione dei punti (s=...).
- Aggiungi un secondo istogramma con altezze di un altro gruppo (media 160)
  sovrapposto con trasparenza (alpha=0.5).

Scrivi il tuo codice qui sotto.
"""

