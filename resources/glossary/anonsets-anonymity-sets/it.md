---
termine: ANONSETS (INSIEMI DI ANONIMATO)
---

Gli Anonsets fungono da indicatori per valutare il livello di privacy di un particolare UTXO. Più specificamente, misurano il numero di UTXO indistinguibili all'interno dell'insieme che include la moneta in esame. Poiché è richiesto un gruppo di UTXO identici, gli anonsets sono generalmente calcolati all'interno di un ciclo di coinjoin. Consentono, ove appropriato, di giudicare la qualità dei coinjoin. Un grande anonset significa un livello aumentato di anonimato, poiché diventa difficile distinguere un UTXO specifico all'interno dell'insieme. Esistono due tipi di anonsets:
* L'insieme di anonimato prospettico;
* L'insieme di anonimato retrospettivo.

Il primo indica la dimensione del gruppo tra cui l'UTXO studiato è nascosto, conoscendo l'UTXO all'input. Questo indicatore permette di misurare la resistenza della privacy della moneta contro un'analisi dal passato al presente (input a output). In inglese, il nome di questo indicatore è “*forward anonset*,” o “*forward-looking metrics*.”

![](../../dictionnaire/assets/39.png)

Il secondo indica il numero di possibili fonti per una data moneta, conoscendo l'UTXO all'output. Questo indicatore permette di misurare la resistenza della privacy della moneta contro un'analisi dal presente al passato (output a input). In inglese, il nome di questo indicatore è “*backward anonset*,” o “*backward-looking metrics*.”

![](../../dictionnaire/assets/40.png)

> ► *In francese, è generalmente accettato usare il termine “anonset.” Tuttavia, potrebbe essere tradotto come “ensemble d'anonymat” o “potentiel d'anonymat.” Sia in inglese che in francese, il termine “score” è talvolta usato anche per riferirsi agli anonsets (prospective score e retrospective score).*