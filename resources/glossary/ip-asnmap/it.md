---
term: IP_ASN.MAP

---
File utilizzato in Bitcoin Core per memorizzare l'ASMAP, che migliora il bucketing (cioè il raggruppamento) degli indirizzi IP basandosi sui numeri di sistema autonomo (ASN). Invece di raggruppare le connessioni in uscita in base ai prefissi di rete IP (/16), questo file consente di diversificare le connessioni stabilendo una mappa degli indirizzi IP in base agli ASN, che sono identificatori unici per ogni rete su Internet. L'idea è di migliorare la sicurezza e la topologia della rete Bitcoin diversificando le connessioni per proteggersi da alcuni attacchi (in particolare l'attacco Erebus).