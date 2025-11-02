---
name: BLOCKSTREAM Verkenner
description: Verken de belangrijkste Layer van Bitcoin en Liquid Network
---

![cover](assets/cover.webp)



De BLOCKSTREAM Verkenner is een project dat het verkennen van transacties en de Global State van het Bitcoin protocol mogelijk maakt, evenals de [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) Liquid ontwikkeld door het BLOCKSTREAM bedrijf.



De [BLOCKSTREAM.info](https://BLOCKSTREAM.info) verkenner werd in 2014 geïnitieerd door BLOCKSTREAM, een bedrijf opgericht door Adam Back. Het doel is om een robuuste infrastructuur te bieden voor Bitcoin, om interoperabiliteit en het volgen van transacties tussen lagen (On-Chain en Liquid) te garanderen en tegelijkertijd de veiligheid en privacy van gebruikers te verbeteren.



In deze tutorial laten we zien wat het verschil maakt, wat de diensten zijn en hoe het naadloze bewaking biedt van de activiteiten en status van Bitcoin's On-Chain en Liquid lagen.



## Aan de slag met BLOCKSTREAM



### Navigeren door het hoofdkanaal



Wanneer je naar de BLOCKSTREAM.info verkenner gaat, op het "**Dashboard**", is het hoofdkanaal van het Bitcoin protocol standaard geselecteerd. Vanuit deze Interface heb je een overzicht van :





- Hoofdketen grootte: Recent gedolven blokken.



![blocks](assets/fr/01.webp)



Dit gedeelte geeft informatie over recent gedolven blokken, de Timestamp, het aantal transacties in elke BLOCK, de grootte in kilobytes (kB) en de meting van elke BLOCK in gewichtseenheden (**WU** = *Weight Units*). Deze laatste meting is interessant, omdat het ons in staat stelt de optimalisatie van de BLOCK te evalueren, aangezien elke BLOCK van de hoofdketen beperkt is tot `4.000.000 WU`, of `4.000 kWU`.





- Recente transacties.



![transactions](assets/fr/02.webp)



De transactiesectie geeft informatie over de unieke identificatiecode van de transactie, de Bitcoin waarde in kwestie, de grootte in virtuele bytes (vB) - die de som van alle gegevens (invoer en uitvoer) vertegenwoordigt - en het bijbehorende tarief. Bijvoorbeeld, een transactie met een grootte van `153 vB` tegen een tarief van `2 sat/vB` brengt `306 satoshis` in rekening.



### Vloeistofverkenning



In het menu "**Blokken**" kun je de geschiedenis van de hele hoofdketen terugvolgen tot de laatste BLOCK die gedolven werd.



![blocs](assets/fr/03.webp)



Door op een specifieke BLOCK te klikken, krijg je meer details over de informatie en transacties die erin staan. Bijvoorbeeld voor BLOCK 919330: je hebt de Hash van de BLOCK. Je kunt ook naar de vorige BLOCK navigeren, want elke gedolven BLOCK (behalve Genesis) is gekoppeld aan de vorige, met behoud van de Hash van zijn voorganger.



![metadata](assets/fr/04.webp)



Door op de **"Details"** knop te klikken, krijg je meer informatie over deze BLOCK, zoals zijn status, die bevestigt dat hij is toegevoegd aan de bewaarde en vermeerderde hoofdketen. Je hebt ook de moeilijkheid waarmee deze BLOCK wordt gedolven: deze moeilijkheid vertegenwoordigt de rekenkracht die nodig is om het cryptografische probleem van Mining op te lossen en wordt elke 2016 blokken (ongeveer 2 weken) aangepast.



![details](assets/fr/05.webp)



Onder dit detailgedeelte vinden we alle transacties die zijn opgenomen in deze BLOCK.



De allereerste transactie in de BLOCK wordt de **transactie coinbase** genoemd. Deze wordt gebruikt om de Mining beloning van de Miner toe te wijzen (alle kosten die verbonden zijn aan de transacties in de BLOCK en de BLOCK toelage). De bitcoins die door deze transactie zijn gecreëerd, kunnen pas worden uitgegeven als er nog eens 100 opeenvolgende blokken zijn gemined. Met andere woorden, om ze te kunnen gebruiken, zal de Miner moeten wachten op de productie van BLOCK **919430**. Dit staat bekend als de [*"maturity period"*](https://planb.network/fr/resources/glossary/maturity-period).



De coinbase is een speciale transactie: het is de enige transactie zonder echte input, omdat er geen bitcoins van een vorige transactie worden uitgegeven.




![coinbase](assets/fr/06.webp)



Alle andere transacties zijn verdeeld in twee secties: inputs en outputs.



Om bitcoins te kunnen gebruiken als input in een nieuwe transactie, moet de initiatiefnemer van de transactie zijn of haar bezit bewijzen door een handtekening te leveren die overeenkomt met een specifiek script. Elk stuk bitcoins (UTXO) bevat een script dat over het algemeen een specifieke handtekening vereist die alleen de private sleutel van de houder kan leveren. Deze scripts zijn ***scriptSig*** (in ASM), geschreven in Bitcoin Script, en kunnen van verschillende types zijn. In dit voorbeeld zien we dat de gebruikte UTXO's van het type P2SH zijn naar een uitvoer van het type P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Je kunt de geschiedenis van een specifieke UTXO traceren met behulp van heuristieken. We nodigen u uit om de verschillende Bitcoin heuristieken te ontdekken en hoe u de vertrouwelijkheid van uw Bitcoin transacties kunt versterken:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Laten we het voorbeeld nemen van de uitgaande kosten van deze transactie. Door op de transactie-ID te klikken, worden we doorgestuurd naar het gedeelte **Transacties** op de pagina met transactiegegevens.



![transaction](assets/fr/08.webp)



Op deze pagina kun je zien in welke BLOCK de transactie was opgenomen. Afhankelijk van het gebruikte Address type, kan de transactie haar data (*virtuele bytes*) optimaliseren en daardoor minder transactiekosten betalen. Deze transactie bespaarde bijvoorbeeld 53% aan kosten door een native SegWit BECH32 Address formaat te gebruiken dat begint met `bc1q`.



![trx_details](assets/fr/09.webp)



## Liquid coating



Liquid Network is een [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) en een niveau 2 open source oplossing voor het Bitcoin protocol. Het maakt met name snellere en meer vertrouwelijke Bitcoin transacties mogelijk.



Klik in de BLOCKSTREAM.info verkenner op de **"Liquid"** knop om over te schakelen naar de Liquid Network.



![liquid](assets/fr/10.webp)



Als we klikken op een van de transacties die we willen volgen, zien we dat de bedragen van de Bitcoin stukken zijn vervangen door de woorden "**Confidential**". Op dit netwerk kunnen transacties vertrouwelijk zijn, dus we kunnen de bedragen van elke UTXO niet zien, noch in, noch uit de transactie.



![liquid_trx](assets/fr/11.webp)



We merken echter op dat de principes en mechanismen die aanwezig zijn op de hoofd Layer van het Bitcoin protocol hetzelfde zijn: Bitcoin vergrendelingsscripts en UTXO traceerbaarheid.



![liquid_details](assets/fr/12.webp)



De Liquid Network biedt ook niet-depository digitale activa die gebruikt kunnen worden door organisaties. In het **"Assets"** menu vind je een lijst van geregistreerde assets, hun totaal en het domein waarop ze betrekking hebben.



![assets](assets/fr/13.webp)



Voor elk activum kun je de geschiedenis van uitgifte- en verbrandingstransacties traceren (waarbij het totaal in omloop wordt verwijderd).



![assets_trxs](assets/fr/14.webp)




## Meer opties



De BLOCKSTREAM.info verkenner bevat ook visualisaties en het bijhouden van transacties op Testnet, Bitcoin, On-Chain en Liquid Network.



![testnet](assets/fr/15.webp)



Als je naar het Testnet netwerk gaat, gebruik je geen echte bitcoins, maar heb je wel alle functies die hierboven beschreven staan.



![liquid_testnet](assets/fr/16.webp)



Dit netwerk heeft een andere kettinglengte, waarop je kunt aansluiten en de werking van de Bitcoin en Liquid mechanismen kunt testen.





- De API-sectie is bedoeld voor iedereen die bepaalde Explorer-functies in zijn eigen applicatie wil integreren. Via deze API kun je de hoofdketen van de verschillende lagen (On-Chain en Liquid) opvragen, transacties bijhouden en bijvoorbeeld de gemiddelde kosten voor transacties in een BLOCK te weten komen.



![api](assets/fr/17.webp)



Je bent nu klaar om het volledige potentieel van BLOCKSTREAM Explorer te benutten om blockchains op de On-Chain en Liquid lagen te bevragen. We hopen dat je deze tutorial informatief vond, en raden je onze tutorial over een andere Bitcoin Explorer aan:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f