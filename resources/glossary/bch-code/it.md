---
term: CODICE BCH
---

Una classe di codici di correzione degli errori utilizzati per rilevare e correggere gli errori in una sequenza di dati. In altre parole, i codici di correzione degli errori BCH sono utilizzati per individuare e correggere gli errori casuali nelle informazioni trasmesse, per garantire che arrivino intatte a destinazione. L'acronimo "BCH" sta per le iniziali dei nomi degli inventori di questi codici: Bose, Ray-Chaudhuri e Hocquenghem.


Questo strumento è utilizzato in molti settori dell'informatica, tra cui SSD, DVD e codici QR. Ad esempio, grazie a questi codici a correzione di errore, anche se un codice QR è parzialmente coperto, è ancora possibile recuperare le informazioni che codifica.


Come parte del Bitcoin, i codici BCH sono utilizzati per la somma di controllo nei formati Bech32 e Bech32m (post-SegWit) Address. Essi rappresentano un compromesso migliore tra dimensione del checksum e capacità di rilevamento degli errori rispetto alle semplici funzioni Hash utilizzate in precedenza sugli indirizzi Legacy. Nel contesto del Bitcoin, i codici BCH sono utilizzati solo per il rilevamento degli errori, non per la correzione degli errori. Pertanto, il software del portafoglio Bitcoin identificherà e segnalerà all'utente eventuali errori in un Address ricevente, ma non cambierà automaticamente il Address errato. Questa scelta è motivata dal fatto che l'integrazione della correzione degli errori influisce inevitabilmente sulle capacità di rilevamento degli errori dell'algoritmo.