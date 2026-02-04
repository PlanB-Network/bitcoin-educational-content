---
term: BIP0035
definition: Förslag som gör det möjligt för noder att dela sin mempool-information (väntande transaktioner) med andra deltagare i nätverket.
---

Förslag som tillåter en Bitcoin-nod att öppna upp information om sin Mempool, det vill säga de transaktioner som väntar på bekräftelse. Tack vare detta kan andra deltagare få realtidsdata om obekräftade transaktioner genom att skicka ett specifikt meddelande till en nod. Innan BIP35 infördes kunde noderna endast få tillgång till information om redan bekräftade transaktioner. Denna förbättring ger SPV-plånböcker möjlighet att ta emot information om obekräftade transaktioner, gör det möjligt för en Miner att undvika att missa transaktioner med höga avgifter under en omstart och underlättar analysen av Mempool-information av externa tjänster.