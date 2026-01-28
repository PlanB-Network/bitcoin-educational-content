---
term: Output
definition: Transaktionsutgång som skapar en ny UTXO avsedd för en adress.
---

I samband med Bitcoin hänvisar en output inom en transaktion till _Unspent Transaction Outputs_ (UTXOs) som skapas som destinationsmedel för betalning. Mer exakt är det en mekanism genom vilken en transaktion distribuerar medel. En transaktion tar UTXO:er, dvs. bitar av bitcoins, som "input" och skapar nya UTXO:er som "output". Dessa outputs stipulerar en viss mängd bitcoins, ofta allokerade till en specifik Address, samt villkoren under vilka dessa medel kan spenderas vid ett senare tillfälle.


Bitcoin-transaktionens roll är därför att konsumera UTXO:er som input och att skapa nya UTXO:er som output. Skillnaden mellan de två motsvarar de transaktionsavgifter som kan återvinnas av den vinnande Miner i blocket. En UTXO är i själva verket resultatet av en tidigare transaktion som ännu inte har använts. Transaktionsutgångar är därför skapandet av nya UTXO:er som i sin tur potentiellt kommer att användas som ingångar i framtida transaktioner.


Ur ett bredare perspektiv, inom datavetenskap, avser termen "output" i allmänhet de data som är resultatet av en funktion, algoritm eller ett system. När t.ex. data skickas genom en kryptografisk Hash-funktion kallas denna information "input" och resultatet kallas "output".