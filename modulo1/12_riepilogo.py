"""Esercizio 12 (Modulo 1) - Registro voti: programma di fine modulo.

Teoria: tutto il Modulo 1 (teoria/01 e teoria/02), in particolare
liste, dizionari, funzioni, file/JSON e try/except.

OBIETTIVO
Un registro voti da terminale che combina tutto quello che hai imparato.
I dati sono un dizionario: la chiave e' la materia, il valore e' la lista
dei voti.
    registro = {"matematica": [7, 8.5], "storia": [6]}

MENU
    === Registro voti ===
    1) Aggiungi un voto
    2) Mostra tutti i voti
    3) Media di una materia
    4) Media generale
    5) Materia con la media piu' alta
    6) Salva su file
    7) Carica da file
    0) Esci

COSA DEVE FARE OGNI VOCE
1. Aggiungi un voto: chiede materia e voto (voto tra 0 e 30 o tra 0 e 10,
   scegli tu e scrivilo in una costante in alto, VOTO_MAX). Se la materia
   non esiste la crea con una lista vuota, poi aggiunge il voto.
2. Mostra tutti i voti: una riga per materia, ad esempio
       matematica: [7, 8.5]
3. Media di una materia: chiede il nome; se non esiste lo dice (niente
   KeyError!); altrimenti stampa la media con 2 decimali.
4. Media generale: media di TUTTI i voti di tutte le materie insieme.
   (Attenzione: non e' la media delle medie.)
5. Materia con la media piu' alta: stampa nome e media.
6. Salva su file: scrive il registro in "registro.json".
7. Carica da file: legge "registro.json" e sostituisce il registro; se il
   file non esiste lo comunica, senza andare in errore.

REQUISITI DI QUALITA'
- Una FUNZIONE per ogni voce del menu (aggiungi_voto, mostra_voti,
  media_materia, media_generale, materia_migliore, salva, carica).
  Le funzioni ricevono il registro come parametro.
- Le funzioni di calcolo (medie) RESTITUISCONO il valore, non stampano.
- Lettura dei numeri con una funzione protetta da try/except (esercizio 10).
- Una funzione main() e il blocco  if __name__ == "__main__": main()
- Percorso del file con Path(__file__).parent (esercizio 9).
- Costanti in maiuscolo in alto (VOTO_MAX, NOME_FILE).

JSON IN BREVE (teoria/02, sezione 8)
    import json
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(registro, f, indent=2, ensure_ascii=False)
    with open(percorso, "r", encoding="utf-8") as f:
        registro = json.load(f)

PASSI CONSIGLIATI
Non scrivere tutto insieme. Procedi a strati e prova ogni strato:
1. Registro vuoto + aggiungi_voto + mostra_voti (senza menu, con chiamate
   dirette e print).
2. Le funzioni di calcolo, verificate con assert (vedi sotto).
3. Il menu in un ciclo.
4. Salvataggio e caricamento.
5. Gestione degli errori e dei casi limite.

COME VERIFICARE DA SOLO
Con questo registro:
    r = {"matematica": [7, 8, 9], "storia": [6, 10]}
    assert media_materia(r, "matematica") == 8
    assert media_materia(r, "storia") == 8
    assert media_generale(r) == 8            # (7+8+9+6+10)/5 = 8
    assert materia_migliore(r)[0] in ("matematica", "storia")   # pari merito
Poi:
    r["storia"].append(10)
    assert abs(media_materia(r, "storia") - 26 / 3) < 1e-9
    assert materia_migliore(r)[0] == "storia"
E per il salvataggio: salva, svuota il registro, ricarica, e controlla che
sia uguale a prima:  assert registro_caricato == r

CASI LIMITE DA PROVARE
- Media di una materia senza voti (lista vuota): sum/len darebbe
  ZeroDivisionError. Cosa vuoi stampare?
- Media generale con registro vuoto.
- Voto fuori range (-3, 45), testo al posto di un numero.
- Materia scritta con maiuscole diverse ("Storia" e "storia"): trattale
  come la stessa con lower() e strip().
- Carica da file inesistente o file con contenuto non valido.

BONUS (facoltativo)
- Voce "Elimina un voto" o "Elimina una materia".
- Ordina l'elenco delle materie per media decrescente.
- Salva automaticamente all'uscita e carica automaticamente all'avvio.
- Aggiungi per ogni voto anche la data (stringa "2026-11-17").

Scrivi il tuo codice qui sotto.
"""

