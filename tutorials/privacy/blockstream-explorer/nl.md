---
name: Blokstroomverkenner
description: Verken de hoofdlaag van Bitcoin en Liquid Network
---

![cover](assets/cover.webp)



De Blockstream Explorer is een project dat het verkennen van transacties en de globale toestand van het Bitcoin protocol mogelijk maakt, evenals de [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) Liquid ontwikkeld door het bedrijf Blockstream.



De [blockstream.info](https://blockstream.info) verkenner werd in 2014 opgestart door Blockstream, een bedrijf opgericht door Adam Back, en heeft als doel een robuuste infrastructuur te bieden voor Bitcoin, waarbij interoperabiliteit en het traceren van transacties tussen lagen (on-chain en Liquid) worden gegarandeerd, terwijl de veiligheid en privacy van gebruikers wordt verbeterd.



In deze tutorial kijken we naar wat het onderscheidt, de diensten en hoe het naadloze bewaking biedt van de activiteiten en status van Bitcoin's on-chain en Liquid lagen.



## Aan de slag met de Blockstream-verkenner



### Navigeren door het hoofdkanaal



Wanneer je naar de Blockstream.info verkenner gaat, is op het "**Dashboard**" standaard de hoofdketen van het Bitcoin protocol geselecteerd. Vanuit deze interface heeft u een overzicht van :





- Hoofdketen grootte: Recent gedolven blokken.



![blocks](assets/fr/01.webp)



Dit gedeelte geeft informatie over recente blokken die zijn gedolven, de tijdstempel, het aantal transacties in elk blok, de grootte in kilobytes (kB) en de meting van elk blok in gewichtseenheden (**WU** = *Weight Units*). Deze laatste meting is interessant omdat het ons in staat stelt de optimalisatie van het blok te evalueren, aangezien elk blok van de hoofdketen beperkt is tot `4.000.000 WU`, of `4.000 kWU`.





- Recente transacties.



![transactions](assets/fr/02.webp)



De transactiesectie geeft informatie over de unieke identificatiecode van de transactie, de betrokken bitcoinwaarde, de grootte in virtuele bytes (vB) - die de som van alle gegevens (invoer en uitvoer) vertegenwoordigt - en het bijbehorende tarief. Bijvoorbeeld, een transactie met een grootte van `153 vB` tegen een tarief van `2 sat/vB` zal een tarief van `306 satoshis` met zich meebrengen.



### Vloeistofverkenning



Vanuit het "**Blocks**" menu kun je de geschiedenis van de hele hoofdketen terugvolgen tot het laatst gedolven blok.



![blocs](assets/fr/03.webp)



Door op een specifiek blok te klikken, kun je meer details krijgen over de informatie en transacties die erin staan. Bijvoorbeeld voor blok 919330: je ziet de hash van het blok. Je kunt ook naar het vorige blok navigeren, want elk gemijnd blok (behalve Genesis) is gelinkt aan het vorige, met behoud van de hash van zijn voorganger.



![metadata](assets/fr/04.webp)



Door op de knop **"Details"** te klikken, kun je meer informatie over dit blok krijgen, zoals de status, die bevestigt dat het is toegevoegd aan de bewaarde en vermeerderde hoofdketen. Je hebt ook de moeilijkheid waarmee dit blok wordt gemined: deze moeilijkheid vertegenwoordigt de rekenkracht die nodig is om het cryptografische probleem van mining op te lossen en wordt elke 2016 blokken (ongeveer 2 weken) aangepast.



![details](assets/fr/05.webp)



Onder dit detailgedeelte vinden we alle transacties die in dit blok zijn opgenomen.



De allereerste transactie in het blok wordt de **transaction coinbase** genoemd. Deze wordt gebruikt om de mining beloning van de miner toe te kennen (alle kosten die verbonden zijn aan de transacties in het blok en de toekenning van het blok). De bitcoins die door deze transactie zijn gecreëerd, kunnen pas worden uitgegeven als er nog eens 100 opeenvolgende blokken zijn gemined. Met andere woorden, om ze te kunnen gebruiken moet de miner wachten op de productie van blok **919430**. Dit staat bekend als de [*"maturity period"*](https://planb.academy/fr/resources/glossary/maturity-period).



De coinbase is een speciale transactie: het is de enige transactie zonder echte input, omdat er geen bitcoins van een vorige transactie worden uitgegeven.




![coinbase](assets/fr/06.webp)



Alle andere transacties zijn verdeeld in twee secties: inputs en outputs.



Om bitcoins te kunnen gebruiken als input in een nieuwe transactie, moet de initiatiefnemer van de transactie zijn of haar bezit bewijzen door een handtekening te leveren die overeenkomt met een specifiek script. Elk stuk bitcoins (UTXO) bevat een script dat over het algemeen een specifieke handtekening vereist die alleen de private sleutel van de houder kan leveren. Deze scripts zijn ***scriptSig*** (in ASM), geschreven in Bitcoin Script, en kunnen van verschillende types zijn. In dit voorbeeld kunnen we zien dat de gebruikte UTXO's van het type P2SH waren naar een uitvoer van het type P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Je kunt de geschiedenis van een specifieke UTXO traceren met behulp van heuristieken. Wij nodigen u uit om de verschillende Bitcoin heuristieken te ontdekken en manieren om de vertrouwelijkheid van uw transacties op Bitcoin te versterken:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Laten we het voorbeeld nemen van de uitgaande kosten van deze transactie. Door op de transactie-ID te klikken, worden we doorgestuurd naar het gedeelte **Transacties** op de pagina met transactiegegevens.



![transaction](assets/fr/08.webp)



Op deze pagina kun je zien in welk blok de transactie is opgenomen. Afhankelijk van het gebruikte adrestype kan de transactie haar gegevens optimaliseren (*virtuele bytes*) en daardoor minder transactiekosten betalen. Deze transactie bespaarde bijvoorbeeld 53% aan kosten door een native SegWit Bech32 adresformaat te gebruiken dat begint met `bc1q`.



![trx_details](assets/fr/09.webp)



## Liquid laag



Liquid Network is een [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) en een open source level 2-oplossing voor het Bitcoin protocol. Het maakt met name snellere en meer vertrouwelijke bitcointransacties mogelijk.



Klik in de Blockstream.info verkenner op de **"Liquid"** knop om over te schakelen naar het Liquid netwerk.



![liquid](assets/fr/10.webp)



Als we klikken op één van de transacties die we willen volgen, zien we dat de bitcoin chunk bedragen zijn vervangen door de woorden "**Confidential**". Op dit netwerk kunnen transacties vertrouwelijk zijn, dus we kunnen de bedragen van elke UTXO niet zien, zowel in als uit de transactie.



![liquid_trx](assets/fr/11.webp)



We merken echter op dat de principes en mechanismen op de hoofdlaag van het Bitcoin protocol hetzelfde zijn: bitcoin vergrendelingsscripts en UTXO traceerbaarheid.



![liquid_details](assets/fr/12.webp)



De Liquid Network biedt ook niet-depository digitale activa die gebruikt kunnen worden door organisaties. In het **"Assets"** menu vind je een lijst van geregistreerde assets, hun totaal en het domein waarop ze betrekking hebben.



![assets](assets/fr/13.webp)



Voor elk activum kun je de geschiedenis van uitgifte- en verbrandingstransacties traceren (waarbij het totaal in omloop wordt verwijderd).



![assets_trxs](assets/fr/14.webp)




## Meer opties



De Blockstream.info verkenner bevat ook visualisaties en het bijhouden van transacties op Testnet, Bitcoin, on-chain en Liquid Network.



![testnet](assets/fr/15.webp)



Als je naar het Testnet netwerk gaat, gebruik je geen echte bitcoins, maar heb je wel alle functies die hierboven beschreven staan.



![liquid_testnet](assets/fr/16.webp)



Dit netwerk heeft een andere kettinglengte, waarop je de werking van de Bitcoin en Liquid mechanismen kunt aansluiten en testen.





- Het API gedeelte is bedoeld voor iedereen die bepaalde Explorer functies in zijn eigen applicatie wil integreren. Via deze API kun je bijvoorbeeld de hoofdketen van de verschillende lagen (on-chain en Liquid) opvragen, transacties traceren en de gemiddelde kosten voor transacties in een blok achterhalen.



![api](assets/fr/17.webp)



Je bent nu klaar om het volledige potentieel van Blockstream Explorer te benutten voor het bevragen van blockchains op de on-chain en Liquid lagen. We hopen dat je deze tutorial informatief vond, en raden je onze tutorial over een andere Bitcoin explorer aan:



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f