---
term: MINISCRITTURA

---
Framework progettato per fornire un quadro di riferimento per la programmazione di script in modo sicuro su Bitcoin. Il linguaggio nativo di Bitcoin è chiamato script. È piuttosto complesso da usare nella pratica, soprattutto per applicazioni sofisticate e personalizzate. Soprattutto, è molto difficile verificare i limiti di uno script. Miniscript utilizza un sottoinsieme di script Bitcoin per semplificarne la creazione, l'analisi e la verifica. Ogni miniscript è equivalente 1 a 1 a uno script nativo. Viene utilizzato un linguaggio di policy facile da usare, che viene poi compilato in miniscript, per corrispondere infine a uno script nativo.

![](../../dictionnaire/assets/30.webp)

Miniscript permette quindi agli sviluppatori di costruire script sofisticati in modo più sicuro e affidabile. Le proprietà essenziali di Miniscript sono le seguenti:


- Consente l'analisi statica dello script, comprese le condizioni di spesa consentite e il suo costo in termini di risorse;
- Consente la creazione di script che aderiscono al consenso;
- Permette di analizzare se i diversi percorsi di spesa sono conformi o meno alle regole standard dei nodi;
- Stabilisce uno standard generale, comprensibile e componibile, per tutto il software e l'hardware dei portafogli.

Il progetto Miniscript è stato lanciato nel 2018 da Peter Wuille, Andrew Poelstra e Sanket Kanjalkar, attraverso la società Blockstream. Miniscript è stato aggiunto al portafoglio Bitcoin Core in modalità watch-only nel dicembre 2022 con la versione 24.0, e poi completamente nel maggio 2023 con la versione 25.0.