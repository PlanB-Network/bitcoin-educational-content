---
termine: ADDRV2
---

Evoluzione proposta con BIP155 del messaggio `addr` sulla rete Bitcoin. Il messaggio `addr` veniva utilizzato per trasmettere gli indirizzi dei nodi che accettano connessioni in entrata, ma era limitato a indirizzi di 128 bit. Questa dimensione era adeguata per indirizzi IPv6, IPv4 e Tor V2, ma insufficiente per altri protocolli. La versione aggiornata `addrv2` è progettata per supportare indirizzi più lunghi, inclusi i servizi nascosti Tor v3 da 256 bit, così come altri protocolli di rete come I2P o protocolli futuri.