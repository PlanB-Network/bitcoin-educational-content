---
term: Coinbase-transaktion
definition: Den första transaktionen i ett block, skapad av brytaren för att ta emot blockbelöning och subsidie.
---

Coinbase Transaction är en speciell och unik transaktion som ingår i varje block av Bitcoin Blockchain. Den representerar den första transaktionen i ett block och skapas av Miner som framgångsrikt har hittat en header som validerar Proof of Work (*Proof-of-Work*), det vill säga mindre än eller lika med målet.


Coinbase Transaction tjänar främst två syften: att tilldela Block reward till Miner och att lägga till nya enheter av bitcoins till de cirkulerande pengarna Supply. Block reward, som är det ekonomiska incitamentet för miners att engagera sig i Proof of Work, inkluderar de ackumulerade avgifterna för de transaktioner som ingår i blocket och ett bestämt belopp av nyskapade bitcoins ex-nihilo (blocksubvention). Detta belopp, som ursprungligen fastställdes till 50 bitcoins per block 2009, halveras vart 210.000:e block (ungefär vart fjärde år) under en händelse som kallas "Halving"


Coinbase Transaction skiljer sig från vanliga transaktioner på flera sätt. För det första har den ingen ingång, vilket innebär att ingen befintlig transaktionsutgång (UTXO) konsumeras av den. Därefter innehåller signaturskriptet (`scriptSig`) för Coinbase Transaction vanligtvis ett godtyckligt fält som gör det möjligt att införliva ytterligare data, till exempel anpassade meddelanden eller information om Mining-programvaruversion. Slutligen är de bitcoins som genereras av Coinbase Transaction föremål för en mognadsperiod på 100 block (101 bekräftelser) innan de kan spenderas, för att förhindra att icke-existerande bitcoins spenderas i händelse av en omorganisation av kedjan.


