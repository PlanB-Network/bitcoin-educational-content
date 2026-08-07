---
term: BTCPay Server

definition: Processore di pagamento open-source che consente di accettare pagamenti in bitcoin senza intermediari.
---

⚠️ **Allarme di sicurezza critico (7 agosto 2026):** una vulnerabilità critica che riguarda BTCPay Server è attivamente sfruttata e può causare la perdita dei fondi. Aggiorna immediatamente la tua istanza alla **versione 2.4.2** tramite `Admin Dashboard > Server > Maintenance > Update`, quindi verifica che il footer mostri `2.4.2`. Se non puoi aggiornare subito, spegni il tuo BTCPay Server. Una volta aggiornato, devi anche rigenerare completamente i tuoi macaroons e il tuo `macaroons.db`, rigenerare completamente le stringhe di autenticazione di qualsiasi altro backend Lightning e, se hai generato un wallet on-chain di tipo hot all'interno di BTCPay Server, spostare quei fondi e ricreare il wallet. Gli integratori dovrebbero inoltre aggiornare NBXplorer alla versione 2.6.10. Fonte: [note di rilascio di BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b
BTCPay Server è un processore di pagamento open-source che consente a commercianti e utenti di accettare pagamenti in Bitcoin senza affidarsi a terzi per l'elaborazione delle transazioni. Lanciato nel 2017, BTCPay Server fornisce una soluzione di integrazione dei pagamenti in Bitcoin per i siti di e-commerce, con funzionalità avanzate come il supporto per i portafogli hardware, strumenti di fatturazione e contabilità, nonché la compatibilità con la rete Lightning. Il suo sviluppo è stato avviato da Nicolas Dorier, in risposta alle azioni di Bitpay che, a suo dire, aveva ingannato i suoi utenti spingendoli verso l'adozione di SegWit2x, che l'azienda considerava erroneamente come il "vero" Bitcoin. Questa opposizione è stata racchiusa in un famoso tweet di Nicolas Dorier dell'agosto 2017:

> "_Questa è una menzogna, la mia fiducia in te è venuta meno, ti renderò obsoleto_".
