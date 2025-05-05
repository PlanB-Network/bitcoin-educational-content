---
name: PayJoin
description: Vad är en PayJoin på Bitcoin?
---
![Payjoin thumbnail - steganography](assets/cover.webp)


***Efter gripandet av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april fungerar Payjoins Stowaway på Samourai Wallet endast genom att manuellt utbyta PSBT mellan de berörda parterna, förutsatt att båda användarna är anslutna till sin egen Dojo. När det gäller Sparrow fungerar Payjoins via BIP78 fortfarande. Det är dock möjligt att dessa verktyg kommer att återlanseras under de kommande veckorna. Under tiden kan du fortfarande läsa den här artikeln för att förstå den teoretiska funktionen av payjoins.*


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg i kriminella syften. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


---
## Förståelse av PayJoin Transaktioner på Bitcoin


PayJoin är en specifik struktur av Bitcoin-transaktionen som förbättrar användarens integritet under en betalning genom att samarbeta med betalningsmottagaren.


År 2015 nämnde [LaurentMT](https://twitter.com/LaurentMT) för första gången denna metod som "steganografiska transaktioner" i ett dokument som finns tillgängligt [här](https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt). Denna teknik antogs senare av Samourai Wallet, som blev den första kunden att implementera den med Stowaway-verktyget 2018. Konceptet med PayJoin finns också i [BIP79](https://github.com/Bitcoin/bips/blob/master/bip-0079.mediawiki) och [BIP78](https://github.com/Bitcoin/bips/blob/master/bip-0078.mediawiki). Flera termer används för att referera till PayJoin:


- PayJoin
- Stowaway
- P2EP (betalning till slutpunkt)
- Steganografisk transaktion


Det unika med PayJoin ligger i dess förmåga att generate skapa en transaktion som vid första anblicken verkar vanlig men som i själva verket är en mini CoinJoin mellan två parter. För att uppnå detta involverar transaktionsstrukturen betalningsmottagaren vid sidan av den faktiska avsändaren i ingångarna. Mottagaren inkluderar en betalning till sig själv i mitten av transaktionen, vilket gör det möjligt för dem att få betalt.


Låt oss ta ett konkret exempel: om du köper en baguette för 4000 Sats med ett UTXO på 10 000 Sats och väljer ett PayJoin, kommer din bagare att lägga till ett UTXO på 15 000 Sats som tillhör dem som en insatsvara, som de kommer att få i sin helhet som en produktion, utöver dina 4000 Sats:

![Payjoin transaction diagram](assets/en/1.webp)


I det här exemplet lägger bagaren in 15 000 Sats` som input och får ut 19 000 Sats`, med en skillnad på exakt 4000 Sats`, vilket är priset på baguetten. På din sida går du in med 10 000 Sats` och får ut 6 000 Sats`, vilket motsvarar ett saldo på 4 000 Sats`, vilket är priset på baguetten. För att förenkla exemplet har jag avsiktligt utelämnat Mining-avgifter i denna transaktion.


## Vad är syftet med en PayJoin-transaktion?


En PayJoin-transaktion tjänar två syften som gör det möjligt för användare att förbättra integriteten för sin betalning.

Först och främst syftar PayJoin till att vilseleda en extern observatör genom att skapa ett lockbete i kedjeanalysen. Detta görs möjligt genom Common Input Ownership Heuristic (CIOH). Vanligtvis, när en transaktion på Blockchain har flera ingångar, antas det att alla dessa ingångar sannolikt tillhör samma enhet eller användare. När en analytiker undersöker en PayJoin-transaktion förleds de således att tro att alla inmatningar kommer från samma person. Denna uppfattning är dock felaktig eftersom betalningsmottagaren också bidrar med input vid sidan av den faktiska betalaren. Därför avleds kedjeanalysen mot en tolkning som visar sig vara falsk.


PayJoin gör det också möjligt att vilseleda en extern observatör om det faktiska beloppet för den betalning som har gjorts. Genom att granska transaktionsstrukturen kan analytikern tro att betalningen motsvarar beloppet för ett av utfallen. I själva verket motsvarar dock inte betalningsbeloppet någon av prestationerna. Det är i själva verket skillnaden mellan mottagarens output UTXO och mottagarens input UTXO. I detta avseende faller PayJoin-transaktionen inom steganografins domän. Den gör det möjligt att dölja det faktiska beloppet för en transaktion i en falsk transaktion som fungerar som ett lockbete.


Vänligen notera vår definition av **Stenografi**:

> Steganografi är en teknik för att dölja information i andra data eller objekt på ett sådant sätt att den dolda informationen inte är märkbar. Ett hemligt meddelande kan t.ex. döljas i en punkt i en text som inte har något med meddelandet att göra, så att det inte kan upptäckas med blotta ögat (detta är mikropunktstekniken). Till skillnad från kryptering, som gör information obegriplig utan dekrypteringsnyckeln, ändrar steganografi inte informationen. Den förblir synlig i öppen dager. Dess syfte är snarare att dölja förekomsten av det hemliga meddelandet, medan kryptering tydligt avslöjar förekomsten av dold information, även om den är otillgänglig utan nyckeln.

Låt oss gå tillbaka till vårt exempel med en PayJoin-transaktion för betalning av en baguette.

![Payjoin transaction schema from the outside](assets/en/2.webp)

Genom att se denna transaktion på Blockchain skulle en extern observatör som följer den vanliga heuristiken för kedjeanalys tolka den på följande sätt: "*Alice slog samman 2 UTXO som input i transaktionen för att betala 19 000 Sats` till Bob*."

![Incorrect interpretation of Payjoin transaction from the outside](assets/en/3.webp)

Denna tolkning är uppenbarligen felaktig eftersom, som ni redan vet, de två ingående UTXO:erna inte tillhör samma person. Dessutom är det faktiska värdet av betalningen inte 19 000 Sats` utan snarare 4 000 Sats`. Den externa observatörens analys riktas således mot en felaktig slutsats, vilket säkerställer att intressenternas konfidentialitet bevaras![PayJoin transaktionsdiagram](assets/en/1.webp)

Om du vill analysera en riktig PayJoin-transaktion, här är en som jag utförde på Testnet: [8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c](https://Mempool.space/fr/Testnet/tx/8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c)


[**-> Upptäck vår handledning om hur man gör en PayJoin med Samourai Wallet**](https://planb.network/tutorials/privacy/On-Chain/PayJoin-samourai-Wallet-48a5c711-ee3d-44db-b812-c55913080eab)


[**-> Upptäck vår handledning om hur man gör en PayJoin med Sparrow Wallet**](https://planb.network/tutorials/privacy/On-Chain/PayJoin-sparrow-Wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62)



**Externa resurser:**


- https://docs.samourai.io/en/spend-tools#stowaway;
- https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt;
- https://github.com/Bitcoin/bips/blob/master/bip-0078.mediawiki.