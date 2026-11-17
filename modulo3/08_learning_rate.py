"""Esercizio 8 (Modulo 3) - L'effetto del learning rate.

Teoria: teoria/04_regressione_gradient_descent.md, sezioni 8 e 12.

OBIETTIVO
Scoprire sperimentalmente che il learning rate e' un iperparametro critico:
troppo piccolo e' lentissimo, troppo grande fa DIVERGERE l'addestramento.

PASSI
1. Riscrivi il ciclo di addestramento come funzione:
       def addestra(x, y, lr, epoche):
           w, b = 0.0, 0.0
           storia = []
           for _ in range(epoche):
               dw, db = gradiente(x, y, w, b)
               w -= lr * dw
               b -= lr * db
               storia.append(mse(predici(x, w, b), y))
           return w, b, storia
2. Esegui con 200 epoche per questi learning rate e stampa, per ciascuno,
   la perdita finale:
       lr = 0.0001   perdita finale  9.54      (troppo lento: non ha finito)
       lr = 0.001    perdita finale  1.312     (lento ma arriva)
       lr = 0.01     perdita finale  1.295     (buono)
       lr = 0.02     perdita finale  1.291     (converge, con qualche oscillazione iniziale)
       lr = 0.03     perdita finale  enorme (circa 1e38): DIVERGE
       lr = 0.05     perdita finale  astronomica (1e175): DIVERGE
   Con lr >= 0.03 il processo esplode: ogni passo "salta" oltre il fondo della
   valle e finisce piu' in alto di prima, sempre peggio.
3. Disegna le curve della perdita sullo stesso grafico, in scala logaritmica
   sull'asse y (ax.set_yscale("log")). Per le curve divergenti puoi ridurre i
   valori con np.clip(storia, None, 1e6) (per non rovinare la scala).
4. Per ciascun lr stampa dopo quante epoche la perdita scende sotto 1.35
   (se mai). Valori attesi: lr 0.001 -> epoca 55; lr 0.01 -> epoca 4;
   lr 0.02 -> epoca 6. Sorpresa: 0.02 e' PIU' LENTO di 0.01 a raggiungere
   quella soglia! Perche'? (Il passo e' cosi' grande che la retta "rimbalza"
   da un lato all'altro della valle prima di assestarsi: guarda la curva.)
5. Per rendere il confronto leggibile fai un grafico della perdita finale contro
   il learning rate (asse x logaritmico).

QUANDO SI DIVERGE?
Il limite dipende dalla "ripidezza" della valle: con x tra 0 e 10, circa
2 / (2 * media(x**2) + 2) ~ 0.027. Sotto questo valore l'addestramento converge,
sopra diverge. Se le feature hanno valori grandi, il limite si abbassa.

PARTE B - STANDARDIZZARE LA FEATURE (facoltativa ma consigliata)
    xn = (x - x.mean()) / x.std()
Ripeti l'esperimento usando xn al posto di x. Ora la valle e' piu' "rotonda":
puoi usare learning rate molto piu' grandi. Verifica che con lr = 0.1 e 100
epoche converge (con x invece diverge).
Attenzione: dopo la standardizzazione i parametri imparati hanno un significato
diverso (w = pendenza per unita' di deviazione standard). Per confrontarli con
2 e 1 va riconvertito:  w_orig = w_n / x.std()   b_orig = b_n - w_n * x.mean() / x.std()

CONCETTI NUOVI
- Iperparametro: valore scelto da noi che non viene imparato (lr, epoche, ...).
- Divergenza: la perdita cresce fino a inf / nan.
- Scala logaritmica per confrontare numeri di ordini di grandezza diversi.
- Standardizzazione delle feature: (x - media) / dev. standard.

COME VERIFICARE DA SOLO
    w, b, s = addestra(x, y, 0.01, 200)
    assert abs(s[-1] - 1.295) < 0.01
    w, b, s = addestra(x, y, 0.03, 200)
    assert s[-1] > 1e6 or not np.isfinite(s[-1])      # diverge
    w, b, s = addestra(x, y, 0.0001, 200)
    assert 5 < s[-1] < 15                              # lentissimo

ERRORI TIPICI
- Interpretare "nan" come un bug sulla perdita: e' il sintomo della divergenza,
  la causa e' il learning rate.
- Concludere che "lr piu' grande e' sempre meglio": e' vero solo fino alla soglia.
- Dimenticare la scala logaritmica: le curve divergenti schiacciano tutto il resto.
- Dimenticare di riconvertire i parametri dopo la standardizzazione.

BONUS (facoltativo)
- Cerca con una ricerca a tentativi (bisezione) il lr piu' grande che ancora
  converge. Confrontalo con il valore teorico ~0.027.
- Aggiungi il "decay": lr che si dimezza ogni 200 epoche. Cambia qualcosa?
- Disegna il percorso (w, b) sulla mappa a curve di livello (bonus
  dell'esercizio 3) per lr = 0.01 e lr = 0.025: vedrai il secondo "zigzagare".

Scrivi il tuo codice qui sotto.
"""

