---
term: ANONSETS (INSIEMI DI ANONIMI)

---
Gli insiemi servono come indicatori per valutare il livello di privacy di un particolare UTXO. Più precisamente, misurano il numero di UTXO indistinguibili all'interno dell'insieme che comprende la moneta in esame. Poiché è necessario un gruppo di UTXO identici, gli anonset sono generalmente calcolati all'interno di un ciclo di coinjoin. Essi consentono, se del caso, di giudicare la qualità delle coinjoin. Un anonset grande significa un maggiore livello di anonimato, poiché diventa difficile distinguere un UTXO specifico all'interno dell'insieme. Esistono due tipi di anonset:


- L'insieme dell'anonimato prospettico;
- L'insieme dell'anonimato retrospettivo.

Il primo indica la dimensione del gruppo tra cui si nasconde l'UTXO studiato, conoscendo l'UTXO in ingresso. Questo indicatore permette di misurare la resistenza della privacy della moneta nei confronti di un'analisi dal passato al presente (dall'ingresso all'uscita). In inglese, il nome di questo indicatore è "*forward anonset*", o "*forward-looking metrics*"

![](../../dictionnaire/assets/39.webp)

Il secondo indica il numero di possibili fonti per una data moneta, conoscendo l'UTXO in uscita. Questo indicatore permette di misurare la resistenza della privacy della moneta rispetto a un'analisi dal presente al passato (dall'uscita all'ingresso). In inglese, il nome di questo indicatore è "*backward anonset*", o "*backward-looking metrics*"

![](../../dictionnaire/assets/40.webp)

> *In francese è generalmente accettato l'uso del termine "anonset" Tuttavia, potrebbe essere tradotto come "ensemble d'anonymat" o "potentiel d'anonymat" Sia in inglese che in francese, il termine "score" viene talvolta utilizzato anche per riferirsi agli anonset (prospective score e retrospective score)*