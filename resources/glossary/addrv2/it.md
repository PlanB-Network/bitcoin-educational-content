---
term: ADDRV2

---
Evoluzione proposta con BIP155 del messaggio `addr` sulla rete Bitcoin. Il messaggio `addr` è stato utilizzato per trasmettere gli indirizzi dei nodi che accettano le connessioni in entrata, ma era limitato a indirizzi di 128 bit. Questa dimensione era adeguata per gli indirizzi IPv6, IPv4 e Tor V2, ma insufficiente per altri protocolli. La versione aggiornata `addrv2` è stata progettata per supportare indirizzi più lunghi, compresi i servizi nascosti Tor v3 a 256 bit, nonché altri protocolli di rete come I2P o protocolli futuri.