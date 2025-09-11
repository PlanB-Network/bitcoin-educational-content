---
name: BitcoinVoucherBot
description: Een Telegram-bot om vertrouwelijk Bitcoin te kopen
---
![image](assets/cover.webp)


_Deze handleiding is geschreven door_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Inleiding


De BitcoinVoucherBot is een tool waarmee Bitcoins in Exchange voor euro's kunnen worden gekocht.


### KYC Licht


De actie om euro's om te wisselen voor Bitcoin is de eerste en meest fundamentele stap om te beginnen met het bestuderen van dit onderwerp, maar het is blijkbaar ook de moeilijkste en meest complexe. Er zijn vele opties: Bitcoin aanbieden via gecentraliseerde Exchanges, Bitcoin-thema meetups, vrienden, kennissen, en meer. Wij sluiten ons aan bij de Bitcoinergemeenschap en **wij raden het gebruik van gecentraliseerde uitwisselingen** absoluut aan om meer aandacht voor iemands privacy te waarborgen.


Hoewel deze keuze misschien minder handig is, is het belangrijk om te begrijpen dat exchanges de Know Your Cutomer (KYC)-regelgeving handhaven en dus een identiteit en fysieke locatie toekennen aan elke Satoshi die bij hen wordt gekocht. "Gemak heeft een aantal opvallende neveneffecten.


### Hoe doe je dat?


Hier komt de [BitcoinVoucherBot:](https://t.me/BitcoinVoucherBot) service, een Telegram bot die fungeert als doorgeefluik tussen onze SEPA overboekingen en Sats aankopen.


### Vereiste voorkennis


Om te beginnen met het gebruik van BitcoinVoucherBot is het niet nodig om gevoelige persoonlijke informatie vrij te geven aan het personeel van de Bot. **Geen autorisatie nodig**.


Het enige dat nodig is, is een reeds actieve Telegram-account en een bankrekening. **Noot**: Een rekening geopend bij Poste Italiane (voor Italiaanse klanten) of, meer in het algemeen, verwijzend naar een oplaadbare kaart is niet geschikt.


In de Telegram-chat bereiden we een bestelling voor, met een bankoverschrijving betalen we, en uiteindelijk krijgen we via de bot een voucher die wordt uitgegeven door een derde partij die het object van de aankoop niet kent.


### Bot activering en menu


Activering is een eenvoudige eenmalige handeling. Zoek vanuit Telegram naar _@BitcoinVoucherBot_ en zodra je in de chat van de Bot komt, valt onderaan een grote _Start/Start_ knop op. De handeling zorgt ervoor dat de Bot reageert, die een menu presenteert met de belangrijkste commando's die beschikbaar zijn. Ook verschijnen de eerste welkomstboodschappen, die we aandachtig moeten lezen.


**Let op**: er zijn meerdere oplichters die zich voordoen als de originele VoucherBot. Als je niet zeker bent van de zoekopdracht via Telegram, gebruik de BitcoinVoucherBot-link vanaf de [officiële site](https://www.bitcoinvoucherbot.com/)


![image](assets/it/01.webp)


Opties verschijnen door te klikken op de _Menu_ knop in de linker benedenhoek: je kunt klikken op het woord dat overeenkomt met de opdracht, of in de berichtenbox de schuine streep `/` typen gevolgd door de getypte opdracht.


![image](assets/it/02.webp)


De belangrijkste activiteiten zijn:




- _/purchase_: is de eigenlijke aankoopprocedure. Wanneer de transactie is voltooid, wordt de QR Code automatisch gegenereerd door de bot, klaar voor inwisseling.
- _/refill_: beschikbaar ten tijde van het schrijven van deze tutorial, maar we zullen het niet behandelen omdat deze optie om technische redenen later verwijderd kan worden.
- _/swap_: opent de ruilprocedure, beschikbaar met een handige Telegram-bot of via het web.
- _/ap_: accumulatieplan, waarmee je een **Constant Accumulation Plan (CAP)** kunt instellen.
- _/lnaddress_: waarmee we gevraagd worden een eigen LN Address te koppelen, voor een bepaalde procedure die we later zullen zien.
- _/credits_: om te controleren hoeveel krediet er over is voor generate vouchers.
- _/mijnbestellingen_: toont geplaatste bestellingen met de bot (**waarschuwing** het systeem houdt alleen de laatste 10 geplaatste bestellingen bij en niet de hele geschiedenis).
- _/fees_: een commando om netwerkkosten te controleren. Om ze te evalueren is het altijd het beste om Mempool.space te gebruiken.
- _/support_: als het nodig is, verschijnen er contacten om problemen aan het ondersteuningsteam te melden.


## Procedure voor het kopen van Bitcoin


### Voorbereiding van de bestelling


Klik op _/aankopen_ in het opdrachtmenu


![image](assets/it/03.webp)


Er verschijnen een aantal mogelijkheden, maar wij kiezen voor _BTC Vouchers_


![image](assets/it/04.webp)


Met BitcoinVoucherBot kunt u Bitcoin onchain, Lightning en Liquid kopen.


Kies in dit stadium _Onchain & Lightning 🔗⚡️_


![image](assets/it/05.webp)


Het scherm verandert snel en VoucherBot stelt aankoopwaarden voor. Ze beginnen bij een minimum van €100,00 tot €900,00.


Bij een eerste aankoop worden alleen de coupures 100,00 €, Onchain en Lightning aangeboden. Om de privacy te verhogen, raden we aan om _Lightning ⚡️_ te kiezen


![image](assets/it/06.webp)


De VoucherBot waarschuwt ons dat er een eerste keuze is gemaakt en dat we, om deze te bevestigen, _Proceed_ moeten kiezen


![image](assets/it/07.webp)


Het is nu een kwestie van het kiezen van de betaalmethode. De overschrijving wordt gedaan door middel van een bankoverschrijving **(alleen SEPA geaccepteerd)**. VoucherBot stelt als ontvanger een bedrijf voor dat twee bankrekeningen heeft, een in Groot-Brittannië en de andere in Zwitserland. De Zwitserse bank is gekozen om deze tutorial uit te voeren


![image](assets/it/08.webp)


Op dit punt worden we gevraagd om onze IBAN in te voeren, de IBAN van waaruit de overschrijving naar de gekozen bank zal starten. Deze informatie vormt een puzzel waarmee de bot, een machine, informatie kan samenvoegen om het aankoopproces zonder menselijke tussenkomst te laten verlopen.


Het IBAN moet in de berichtenbalk worden geschreven, gecontroleerd en naar de bot worden gestuurd.


![image](assets/it/09.webp)


Er verschijnt nu een controlebericht in de chat met VoucherBot.


Als alles correct is, ga dan verder door op _Proceed_ te klikken.


![image](assets/it/10.webp)


### Betaling


Na enkele ogenblikken, die nodig zijn om de gegevens te verwerken, antwoordt VoucherBot met een bericht met alle gegevens die nodig zijn om de bestelling af te ronden. Afhankelijk van wat uw bank vereist, is de relevante informatie:




- `IBAN`, wat essentieel is voor de storting, evenals de Address van de ontvanger;
- `het gekozen bedrag` eerder door de cutoff, waaraan moet worden voldaan om VoucherBot de bestelling te laten herkennen wanneer de betaling is ontvangen;
- `Betalingsreden`, dat is de reden voor de betaling. **Moet worden gekopieerd en geplakt zonder iets te verwijderen of toe te voegen in het daarvoor bestemde veld van uw overschrijving. Elke "." of "-" in de betalingsreden kan worden vervangen door `witruimte` **.
- een unieke `OrderID` om naar te verwijzen bij het aanvragen van assistentie.


Je kunt dan doorgaan met de betaling, via je app of bank. Wanneer de betaling is geaccepteerd door de bank, is het belangrijk om te onthouden om op _Betaling melden_ te drukken in de chat met VoucherBot. Deze eenvoudige handeling waarschuwt u dat er een betaling onderweg is.


![image](assets/it/11.webp)


VoucherBot antwoordt met een bericht dat een zeer belangrijke waarschuwing bevat: **verwijder de chat** niet, tenminste totdat de tegoedbon is ontvangen, want dat is de enige manier om de bestelling te reconstrueren en door te laten gaan.


![image](assets/it/12.webp)


---
Let op:




- alleen SEPA-overschrijvingen worden geaccepteerd;
- wachttijden hebben uitsluitend te maken met hoe de banken (die niet 24/7/365 werken zoals Bitcoin) de voucher verwerken. Het kan een paar uur tot 3 werkdagen duren voordat je de voucher ontvangt;
- gW-15 VoucherBot heeft een uitstekende [support](https://t.me/BitcoinVoucherGroup) service op Telegram voor al je behoeften.


---
### Inlossing


Zodra de betaling succesvol is, stuurt Bitcoin VoucherBot de voucher direct naar de chat. De bliksemvoucher heeft de vorm van een QR-code, afgedrukt op een oranje achtergrond.


![image](assets/it/31.webp)


Daar staan alle gegevens die nodig zijn om het te verzilveren:




- het bedrag in Sats, gelijk aan het bedrag dat per bankoverschrijving is verzonden, exclusief servicekosten en netwerkkosten;
- een referentie-ID van de voucher;
- de datum waarop de voucher moet zijn ingewisseld, anders gaat het geld verloren, d.w.z. 25 dagen na uitgifte.


Je kunt de voucher verzilveren door de QR-code in te kaderen met de scanfunctie van een compatibele Wallet Lightning Network, of via LNURL, ook te zien onder de QR-code.


Voor deze tutorial gebruikten we Wallet Of Satoshi, met de scanfunctie die wordt geactiveerd door de knop _Send_.


![image](assets/it/32.webp)


Omlijst de QR-code in de chat met de camera van de mobiele telefoon geactiveerd en open Telegram vanaf de PC


![image](assets/it/34.webp)


Voordat u verdergaat, toont Wallet Of Satoshi een verificatiescherm dat het bedrag bevat, dat exact overeenkomt met het bedrag dat op de voucher staat vermeld, en als beschrijving, BitcoinVoucherBot. Om de voucher te innen, hoeft u alleen op _Receive_ te klikken.


![image](assets/it/35.webp)


Wallet Of Satoshi verwerkt enkele ogenblikken.


![image](assets/it/36.webp)


en ten slotte wordt de inning gerapporteerd en onmiddellijk beschikbaar in de Wallet balans.


**Wallet of Satoshi is een bewaar-app: direct na het inwisselen van de voucher is het aan te raden de sats naar een non-custodial wallet te verplaatsen.**


![image](assets/it/37.webp)


### Hoe verzilver je een onchain voucher


Zoals we zagen bij het voorbereiden van de bestelling, maakt VoucherBot het mogelijk om Sats direct onchain te kopen, met de keuze van de gelijknamige voucher.


**Opmerking**: Ordervoorbereiding en betaling veranderen niet, ze zijn altijd hetzelfde. Wat wel verandert, is hoe een onchain voucher wordt verzilverd.


Na het afronden van de bestelling, het doen van de betaling, het drukken op _Betaling bevestigen_ en het wachten op de technische tijd van de banken om de overschrijving te doen, zal VoucherBot reageren door de voucher direct in de chat te sturen.


Deze voucher is ook in de vorm van een QR-code, maar de hoofdkleur is kanariegeel en - het belangrijkste - in de beschrijving wordt goed uitgelegd dat het een onchain voucher is, die je direct verzilvert op je Wallet onchain en, om de uitbetalingsprocedure te starten, moet je klikken op _Redeem on Telegram_. De onchainvoucher bevat ook de informatie die je al bij de lightningvoucher hebt gezien:




- het bedrag in Sats, gelijk aan het bedrag dat per bankoverschrijving is verzonden, exclusief servicekosten en netwerkkosten;
- een vouchercode;
- een referentie-ID van de voucher;
- de datum waarop de voucher moet zijn ingewisseld, anders gaat het geld verloren, d.w.z. 25 dagen na uitgifte.


![image](assets/it/22.webp)


**WARNING ⚠️:** geklikt zoals uitgelegd, pop-up van een andere bot wordt geopend: **Voucher inwisselenbot.**


Voucher inwisselbot is de tool die hiervoor beschikbaar is. Of dit nu het eerste gebruik is of dat er eerdere bestellingen zijn, bij elke nieuwe inwisselactie moet er altijd op _START_ worden geklikt.


![image](assets/it/23.webp)


Op dit punt laadt RedeemBot de onchain voucher, gemakkelijk te herkennen aan de Voucher Code en referentie ID. Het ontgrendelt ook de bar om berichten te schrijven en te beginnen chatten met de bot, die ons in feite uitnodigt om het een onchain Address van onze Wallet te vertellen.


**Noot**: Deze Address moet van het type SegWit zijn.


![image](assets/it/24.webp)


We openen onze Wallet op dit punt en generate een SegWit Address


![image](assets/it/25.webp)


we kopiëren het


![image](assets/it/26.webp)


en plak het in de chat met RedeemBot


![image](assets/it/27.webp)


We hebben nu een controlescherm om te controleren of de vouchercode correct is, evenals de Address die we hebben doorgegeven aan RedeemBot. Laten we het goed controleren, want door op _Proceed_ te klikken, start de transactie en is er geen manier om het terug te vinden als we bijvoorbeeld de verkeerde Address hebben doorgegeven.


![image](assets/it/28.webp)


De transactie is gestart en de Redeem procedure van de onchain voucher eindigt daarmee.


![image](assets/it/29.webp)


terwijl het bedrag te zien is in de geschiedenis van onze Wallet.


![image](assets/it/30.webp)