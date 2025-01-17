---
term: CONSOLIDAMENTO

---
Una transazione specifica in cui più UTXO di piccole dimensioni vengono uniti in un unico input per formare un singolo UTXO più grande come output. Questa operazione è una transazione effettuata sul proprio portafoglio. L'obiettivo del consolidamento è quello di sfruttare i periodi in cui le commissioni sulla rete Bitcoin sono basse per unire più UTXO di piccole dimensioni in uno di valore maggiore. In questo modo, si anticipano le spese obbligatorie in caso di aumento delle commissioni, consentendo di risparmiare sulle future commissioni di transazione.

Infatti, le transazioni con molti input sono più pesanti e, di conseguenza, più costose. Oltre ai risparmi ottenibili sulle commissioni di transazione, il consolidamento è anche una forma di pianificazione a lungo termine. Se il vostro portafoglio contiene UTXO molto piccoli, questi possono diventare inutilizzabili se la rete Bitcoin entra in un periodo prolungato di commissioni elevate. Ad esempio, se è necessario spendere un UTXO di 10.000 sats ma le commissioni mining minime ammontano a 15.000 sats, la spesa supererebbe il valore dell'UTXO stesso. Questi piccoli UTXO diventano quindi economicamente irrazionali da usare e rimangono inutilizzabili finché le tariffe non diminuiscono. Questi UTXO sono comunemente chiamati "polvere" Consolidando regolarmente le piccole UTXO, si riduce il rischio di aumento delle commissioni.

Tuttavia, è importante notare che le transazioni di consolidamento sono riconoscibili durante l'analisi della catena. Una transazione di questo tipo indica una Common Input Ownership Heuristic (CIOH), ovvero che gli input della transazione di consolidamento sono di proprietà di un'unica entità. Ciò può avere implicazioni in termini di privacy per l'utente.

![](../../dictionnaire/assets/7.webp)