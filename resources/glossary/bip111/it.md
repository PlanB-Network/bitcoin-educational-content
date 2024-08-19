---
term: BIP111
---

Propone l'aggiunta di un bit di servizio denominato `NODE_BLOOM` per permettere ai nodi di segnalare esplicitamente il loro supporto per i Filtri Bloom come descritto nel BIP37. L'introduzione di `NODE_BLOOM` consente agli operatori dei nodi di disabilitare questo servizio al fine di ridurre i rischi di DoS. L'opzione BIP37 è disabilitata per impostazione predefinita in Bitcoin Core. Per abilitarla, è necessario inserire il parametro `peerbloomfilters=1` nel file di configurazione.