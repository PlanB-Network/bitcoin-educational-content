---
termine: MINISCRIPT
---

Framework progettato per fornire un framework per la programmazione di script in modo sicuro su Bitcoin. Il linguaggio nativo di Bitcoin si chiama script. È piuttosto complesso da utilizzare nella pratica, specialmente per applicazioni sofisticate e personalizzate. Soprattutto, è molto difficile verificare le limitazioni di uno script. Miniscript utilizza un sottoinsieme degli script di Bitcoin per semplificarne la creazione, l'analisi e la verifica. Ogni miniscript è equivalente 1 a 1 con uno script nativo. Viene utilizzato un linguaggio di policy user-friendly, che viene poi compilato in miniscript, per corrispondere infine a uno script nativo.

![](../../dictionnaire/assets/30.png)

Miniscript consente quindi agli sviluppatori di costruire script sofisticati in modo più sicuro e affidabile. Le proprietà essenziali di Miniscript sono le seguenti:
* Permette l'analisi statica dello script, inclusi le condizioni di spesa che permette e il suo costo in termini di risorse;
* Consente la creazione di script che aderiscono al consenso;
* Permette l'analisi di se i diversi percorsi di spesa rispettano o meno le regole standard dei nodi;
* Stabilisce uno standard generale, comprensibile e componibile, per tutto il software e l'hardware dei portafogli.

Il progetto Miniscript è stato lanciato nel 2018 da Peter Wuille, Andrew Poelstra e Sanket Kanjalkar, attraverso l'azienda Blockstream. Miniscript è stato aggiunto al portafoglio Bitcoin Core in modalità solo visualizzazione nel dicembre 2022 con la versione 24.0, e poi completamente nel maggio 2023 con la versione 25.0.