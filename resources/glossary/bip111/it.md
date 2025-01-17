---
term: BIP111

---
Propone l'aggiunta di un bit di servizio denominato `NODE_BLOOM` per consentire ai nodi di segnalare esplicitamente il loro supporto per i filtri Bloom, come descritto in BIP37. L'introduzione di `NODE_BLOOM` consente agli operatori dei nodi di disabilitare questo servizio per ridurre i rischi di DoS. L'opzione BIP37 è disabilitata per impostazione predefinita in Bitcoin Core. Per attivarla, è necessario inserire il parametro `peerbloomfilters=1` nel file di configurazione.