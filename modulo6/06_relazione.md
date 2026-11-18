# Relazione finale: riconoscimento di cifre scritte a mano (MNIST)

Passo 6 del progetto. Scrivi qui, con parole tue, il resoconto del lavoro. Una buona relazione
si legge da sola, senza il codice. Lunghezza indicativa: 1-2 pagine. Sostituisci le istruzioni
in corsivo con il tuo testo e inserisci i grafici salvati in `modulo6/grafici/`.

## 1. Obiettivo

*In 2-3 frasi: qual è il problema (classificare cifre 0-9 da immagini 28×28), perché è
interessante, cosa volevi imparare. Cos'è un problema di classificazione multiclasse.*

## 2. Dati

*Dataset MNIST: quante immagini di training e di test, forma delle immagini, numero di classi,
distribuzione delle classi (quasi bilanciata), normalizzazione scelta (media 0.1307, deviazione
standard 0.3081) e perché. Inserisci `grafici/01_cifre.png`.*

## 3. Modello

*Architettura della rete di base (784 → 128 → 10, ReLU), numero di parametri (101 770), perdita
(cross-entropy), ottimizzatore (Adam, learning rate 0.001), dimensione del batch (64), numero di epoche.
Spiega in due righe cosa fa ciascuno strato.*

## 4. Addestramento

*Descrivi l'andamento: come scende la perdita, come sale l'accuratezza sul test. Inserisci
`grafici/02_curve.png`. C'è overfitting? Quanto è il divario tra training e test?*

## 5. Risultati

*Accuratezza sul test set (con un numero sensato di cifre). Confronto con il riferimento banale
(~11%) e con un classificatore lineare (~92%). Matrice di confusione (`grafici/03_confusione.png`),
cifre meglio e peggio riconosciute, coppie più confuse e una spiegazione plausibile.*

## 6. Analisi degli errori

*Cosa hai visto guardando le cifre sbagliate (`grafici/04_errori.png`): errori scusabili o veri?
Fiducia della rete quando sbaglia contro quando ha ragione. Cosa succede se la rete "si astiene" sotto
una soglia di fiducia (copertura contro accuratezza)?*

## 7. Esperimenti di miglioramento

*Tabella degli esperimenti del passo 5 (nome, parametri, epoche, accuratezza, tempo). Cosa ha
migliorato davvero i risultati, cosa no, cosa ti ha sorpreso. Variabilità tra seed: media ± deviazione
standard.*

## 8. Limiti

*Cosa non sai o non hai verificato: il modello è stato provato solo su MNIST (cifre pulite, centrate,
bianco su nero); come reagirebbe a cifre scritte diversamente, ruotate, rumorose? Quanto sono stabili
le stime con un solo addestramento? Cosa non hai provato (convoluzioni, data augmentation…)?*

## 9. Cosa ho imparato

*8-10 righe con parole tue: cosa è un modello, la perdita, il gradiente, la backpropagation, i dati di
training e di test, l'overfitting, le metriche. Qual è stato il passaggio più difficile e come l'hai
superato. Cosa vorresti imparare dopo.*

## 10. Come riprodurre

*Comandi per rifare tutto da capo: installazione delle librerie, ordine di esecuzione dei file
`01` … `05`, tempi indicativi (qualche minuto su CPU), seed usati.*
