---
name: Blue Wallet

description: Een radicaal eenvoudige en krachtige Bitcoin-wallet
---
![cover](assets/cover.webp)



Voor mensen die sceptisch zijn over het gebruik van Bitcoin, lijkt het beginnen een grote uitdaging. Het vinden van de juiste hulpmiddelen om deze eenvoud te garanderen, is dan ook van het grootste belang voor een betere adoptie van Bitcoin als een betaalmiddel en niet alleen als een waardeopslag.



In deze tutorial kijken we naar Blue Wallet, een eenvoudige maar zeer effectieve Bitcoin-wallet waarmee je je bitcoins persoonlijk kunt beheren en waarmee je ook beheercoöperaties kunt opzetten op basis van [multisig](https://planb.academy/resources/glossary/multisig) (maak je geen zorgen, hier komen we later nog op terug).






## Aan de slag met Blue Wallet



Blue Wallet is een open source, self-custodial Bitcoin-wallet waarmee je controle krijgt over je bitcoins. Het is beschikbaar als mobiele app op zowel Android- als iOS-platforms. In deze tutorial baseren we ons op de Android-versie, maar alle processen die worden beschreven, zijn ook geldig op iOS.



![download](assets/fr/01.webp)



⚠️ Zorg ervoor dat je de Blue Wallet Bitcoin-wallet app downloadt op een officieel platform om de echtheid ervan te garanderen en je bitcoins te beschermen tegen mogelijke lekken en hacks.



Eenmaal geïnstalleerd, kun je een nieuwe wallet aanmaken en de 12 herstelwoorden opslaan, of een bestaande Bitcoin-wallet importeren. Ontdek hoe je een efficiënte back-up van je sleutelwoorden kunt maken, zodat je de toegang tot je bitcoins niet verliest.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Met Blue Wallet kun je aparte, speciale Bitcoin-wallets aanmaken. Je kunt bijvoorbeeld een wallet hebben voor je spaargeld en een andere voor je dagelijkse uitgaven, allemaal binnen dezelfde applicatie.



![home](assets/fr/02.webp)



## Soorten wallets



In Blue Wallet vind je twee native Bitcoin-wallettypes.



### Bitcoin wallet



Als je gewend bent aan andere bitcoin wallets zoals Phoenix of Aqua, zul je de interface van de Blue Wallet bitcoin wallet meteen herkennen.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf


https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Blue Wallet's Bitcoin-wallet vertegenwoordigt de standaard-wallet in het Bitcoin-ecosysteem. Je kunt bitcoins uitgeven zolang je in het bezit bent van de herstelwoorden die zorgen voor een geldige handtekening op het netwerk om te verifiëren dat je de bitcoins bezit.



Om een Bitcoin-wallet aan te maken, klik je op de knop **Add now**, voer je de naam van je wallet in en kies je het Bitcoin-type.



![bitcoin-wallet](assets/fr/03.webp)



Als je op de voorbeeldweergave van je Bitcoin-wallet klikt, kun je je transactiegeschiedenis bekijken en bitcoins versturen en ontvangen.



⚠️ Alle transacties in je Bitcoin-wallet vinden plaats op de hoofdketen van het Bitcoin-protocol (Mainnet).





- Bitcoins ontvangen met de Blue Wallet Bitcoin-wallet is intuïtief. Klik onderaan op de knop **Receive**. Deel de QR-code of je Bitcoin-adres met je afzender, zodat hij je de bitcoins kan sturen.



Je kunt ook een vooraf gedefinieerd bedrag instellen om het bitcoinbedrag te specificeren dat je wilt ontvangen.



![receive-bitcoin](assets/fr/04.webp)





- Tik op de **Send** knop om bitcoins naar een Bitcoin-adres te sturen, stel het gewenste bedrag in en valideer de transactie.



![send-bitcoin](assets/fr/05.webp)



Met Blue Wallet kun je de parameters van je Bitcoin-transactie naar wens configureren.



Je kan dus de verhouding van de transactiekosten (fee ratio) kiezen die bij je past als je wilt dat je transactie snel wordt gevalideerd in een mempool en door miners in een blok wordt opgenomen. Afhankelijk van de verhouding die je kiest, zullen de miners jouw transactie meer of minder prioriteit geven. Ontdek meer in onze Mempool Space tutorial.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

![feerate](assets/fr/06.webp)





- In het kader van gegroepeerde betalingen laat Blue Wallet je toe om meerdere ontvangers aan één transactie toe te voegen.



Wanneer je het Bitcoin-adres van je eerste ontvanger toevoegt, klik dan in de opties op **Add Recipient**, voeg het Bitcoin-adres toe en stel vervolgens het bedrag in dat naar deze ontvanger moet worden verzonden, enzovoort. Blue Wallet verzendt de bitcoins voor de meerdere transacties op basis van jouw enige actie.



![add-recipients](assets/fr/07.webp)



Je kunt één of alle ontvangers verwijderen door respectievelijk op **Remove Recipient** en **Remove All Recipients** te klikken.



![remove-recipient](assets/fr/08.webp)





- **Kosten opdrijven**: Heb je een transactie gedaan waarvan de bevestiging lang op zich laat wachten? Door RBF (Replace-By-Fee) (Allow Fee Bump) in te schakelen kun je extra transactiekosten toevoegen aan je lopende transactie om de bevestiging ervan te versnellen.



![bumping](assets/fr/09.webp)



### Multisig-wallet



De Multisig (multi-handtekening) wallet vertegenwoordigt een wallet die is gecreëerd uit de groepering van een bepaald aantal (minimaal 2) Bitcoin-wallets. Bij dit type wallet wordt, afhankelijk van de gekozen configuratie en methode, het uitgeven van bitcoins een collectieve en coöperatieve actie.



In Blue Wallet kun je multisig-wallets maken voor je vereniging, je familie, je bedrijf. In dit hoofdstuk zullen we elk aspect van dit speciale type wallet verkennen.



Voeg een nieuwe wallet toe en selecteer het type **Multisig Vault** om een multisig-wallet aan te maken.



![multisig-vault](assets/fr/10.webp)



Definieer de m-van-n configuratie voor je multisig-organisatie door te klikken op **Vault Settings**.



⚠️ In een m-van-n configuratie staat **m** voor het minimum aantal handtekeningen dat nodig is om een transactie goed te keuren en **n** voor het aantal wallets in je organisatie.



Zorg ervoor dat je een minimum aantal handtekeningen (m) definieert voor de meerderheid van je organisatie. Bijvoorbeeld, een 2-van-3 multisig-configuratie vereist dat twee wallets in je organisatie de transactie ondertekenen voordat deze kan worden uitgevoerd.



Het definiëren van een m-van-n configuratie waarbij n gelijk is aan m is een groot risico. Wanneer een lid de toegang tot zijn wallet verliest, verlies je de autorisatie om bitcoins uit de wallet uit te geven.



Hier zijn enkele voorbeelden van optimale configuraties om de veiligheid en toegankelijkheid van je bitcoins te garanderen:





- 2-de-3 multisig.





- 5-de-7 multisig.



![vault-settings](assets/fr/11.webp)



Houd je aan de best practice door het P2WSH-formaat te kiezen.



❗ **[P2WSH](https://planb.academy/resources/glossary/p2wsh) of Pay to Witness Script Hash** is een vergrendelingsmethode die de uitgaande bitcoins (outputs) van je transactie vergrendelt naar de hash van een aangepast script dat Blue Wallet instelt. Het belangrijkste voordeel van dit type vergrendeling is dat het de grootte van transactiegegevens vermindert en je impliciet lagere transactiekosten kan betalen.



Maak of importeer elk van de **n** wallets in je configuratie. In onze tutorial gebruiken we een 2-van-3 configuratie met meerdere handtekeningen. Zorg ervoor dat je de herstelwoorden voor elke wallet afzonderlijk opslaat.



![vault-keys](assets/fr/12.webp)





- **Bitcoins ontvangen**



Op je Multisig-wallet pagina vind je je transactiegeschiedenis en de knoppen Receive en Send.



Bitcoins ontvangen in een mulitsig-wallet is hetzelfde proces als in een standaard Bitcoin-wallet.





- **Bitcoins verzenden**:



Door een multisig-wallet te beheren, wordt het uitgeven van bitcoins een samengestelde actie, of het nu met andere mensen is of met een tweede wallet van jezelf. De enkele handtekening van je wallet is niet langer voldoende. Dit voegt een beveiligingslaag toe aan je bitcoins, omdat een kwaadwillende persoon die bitcoins niet zal kunnen uitgeven wanneer hij slechts één van je privésleutels bezit.



Net als bij de standaard Blue Wallet Bitcoin-wallet, kun je meerdere ontvangers definiëren met de **Add Recipients** optie.



Bij het valideren van je transactie heb je een tweede handtekening nodig om het uitgeven van de bitcoins goed te keuren. Onthoud dat we in een 2-van-3 multisig-configuratie zitten.



De tweede wallet-ondertekenaar kan, als hij of zij ook een gebruiker is, de transactie ondertekenen, zelfs zonder internetverbinding (geen Wi-Fi, geen mobiele data), door de QR-code te scannen van de [gedeeltelijk ondertekende transactie](https://planb.academy/resources/glossary/psbt) die je zojuist hebt aangemaakt.



![mutisig-send](assets/fr/13.webp)





- Ga verder met de **Multisig**-wallet:



Klik in de interface van je multisig-wallet op de knop **Manage keys**.



Door één van de herstelwoorden van één van de ondertekenende wallets te vergeten (**Forget this seed...**), laat je Blue Wallet weten dat het de back-up van deze woorden uit zijn geheugen moet wissen. Je hebt dus een externe back-up gemaakt.



![revoke-key](assets/fr/14.webp)



Door deze actie uit te voeren, behoudt je alleen de openbare sleutel (XPUB) die aan deze herstelwoorden is gekoppeld.



⚠️ Door alleen openbare sleutels te bewaren (XPUB) kun je een extra beveiligingsniveau toevoegen aan je 2-van-3 multisig-configuratie. Het kan inderdaad nadelig zijn om alle herstelwoorden op één plaats te bewaren als je telefoon wordt aangevallen. Aanvallers met toegang tot slechts één **VAULT** (sleutelwoord) die je gebruikt om je transacties te ondertekenen, zullen niet in staat zijn om je bitcoins te stelen (minimaal 2 handtekeningen vereist) omdat publieke sleutels niet kunnen worden gebruikt om transacties te ondertekenen.



## Meer opties met Blue Wallet



### Toegangsbeveiliging voor wallets verbeteren



In Settings kun je met de optie **Security** het gebruik van een vingerafdruk definiëren om een transactie uit te voeren, je wallet te exporteren of te verwijderen. Dit authenticeert de persoon die je smartphone gebruikt.



![biometry](assets/fr/15.webp)



## Lightning Network activeren



Lightning Network wordt niet langer ondersteund in de Blue Wallet-applicatie.



In Instellingen > **Lightning Settings**, kun je je Lightning-wallet handmatig koppelen wanneer je een Lightning Network Daemon (LND) node gebruikt. Installeer de LND Hub en koppel vervolgens je wallet door de link in te voeren die door de hub wordt gegenereerd.



![ln](assets/fr/16.webp)



https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Je hebt nu de Blue Wallet rondleiding voltooid en bent klaar om Bitcoin in al zijn eenvoud en kracht te gebruiken. Wij raden je aan de volgende stap te nemen en te ontdekken hoe je Bitcoin betalingen kunt accepteren in je winkel, dankzij de kracht van Lightning.



https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06
