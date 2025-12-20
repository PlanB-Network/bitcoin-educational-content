---
name: LN Markets
description: Bitcoin handelsplatform op Lightning Network
---

![cover](assets/cover.webp)



LN Markets is het eerste echte Lightning-native Bitcoin handelsplatform, waarmee u direct vanuit uw wallet Lightning Bitcoin derivaten met hefboomwerking kunt verhandelen, zonder KYC, onmiddellijke vereffening en minimale bewaring. Gelanceerd in 2020, elimineert het de fricties van traditionele beurzen: geen identiteitsverificatie, geen geblokkeerde stortingen, niet wachten op blockchainbevestigingen. Uw wallet Lightning wordt uw handelsrekening.



## Wat is LN Markets?



LN Markets biedt **Futures** (eeuwigdurende contracten met een hefboom tot 100×) en **Opties** (Call/Put met risico beperkt tot de betaalde premie). Het platform fungeert als een liquiditeitsaggregatielaag die meerdere handelsplatformen consolideert voor een optimale zero-slippage uitvoering. Uw fondsen worden alleen vastgezet voor de exacte duur van uw actieve posities, geen dagen of weken zoals bij een traditionele effectenrekening.



### Handelsproducten beschikbaar



**Futures (eeuwigdurende contracten)**



Perpetuele contracten zijn futures zonder vervaldatum, waardoor je met een hefboom kunt speculeren op de Bitcoin prijstrend. LN Markets biedt twee modi voor margebeheer:



**Gesoldeerde modus**: Elke positie heeft zijn eigen specifieke marge. Alleen het geld dat aan deze specifieke positie is toegewezen loopt risico. Als de positie de liquidatieprijs bereikt, wordt **alleen deze positie geliquideerd**, uw andere posities en resterende saldo worden niet beïnvloed. Ideaal om het risico per transactie strikt te beperken.



**Kruismodus (Cross Margin)** : Margin wordt gedeeld tussen al uw open posities. Uw totale rekeningsaldo dient als onderpand voor al uw posities. Als een positie slecht gaat, trekt het systeem uw volledige beschikbare saldo aan om liquidatie te voorkomen. **Risico**: als uw totale saldo opraakt, kunnen al uw posities tegelijkertijd worden geliquideerd. Alleen aanbevolen voor ervaren handelaren die hun kapitaalefficiëntie willen maximaliseren.



**Positiemanagement** :





- Long positie**: je wedt op de stijging van BTC/USD. Als de prijs stijgt, win je; als hij daalt, verlies je. **Voorbeeld**: Bitcoin op $100.000, u opent een Long met 10.000 sats en 10× hefboomwerking. Als Bitcoin stijgt naar $105.000 (+5%), wint uw positie 50% (5% × 10), d.w.z. ~5.000 sats winst. Als Bitcoin daalt tot $95.000 (-5%), verlies je 50%, d.w.z. een verlies van ~5.000 sats.





- Short positie**: je zet in op een daling van BTC/USD. Als de prijs daalt, win je; als hij stijgt, verlies je. **Voorbeeld: Bitcoin op $100.000, u opent een short met 10.000 sats en 10× leverage. Als Bitcoin daalt tot $95.000 (-5%), win je 50%, d.w.z. ~5.000 sats. Als Bitcoin stijgt naar $105.000 (+5%), verliest u 50%.



Hefboomwerking (tot 100×) versterkt winsten en verliezen proportioneel. Een **funding rate** mechanisme (periodieke kosten om de 8 uur) brengt lange en korte posities in evenwicht. Je kunt tot 100 futuresposities tegelijk beheren.



**Opties**



Een optie is als een **loterijbriefje met vervaldatum**. Je betaalt een premie om te wedden op de richting van de Bitcoin prijs. **Groot voordeel**: je kunt nooit meer verliezen dan de betaalde premie, geen liquidatie mogelijk.





- Calloptie (stijgende inzet)**: Je wedt dat Bitcoin boven de uitoefenprijs zal stijgen voor de expiratie. Je wint als de prijs stijgt, het verlies is beperkt tot de premie als de prijs daalt.





- Putoptie (dalende weddenschap)**: Je wedt dat Bitcoin onder de uitoefenprijs zal zakken. Je wint als de prijs daalt, het verlies is beperkt tot de premie als de prijs stijgt.





- Straddle (volatiliteitsweddenschap)**: Je koopt tegelijkertijd een Call EN een Put. Je wint als Bitcoin een grote beweging maakt in welke richting dan ook, je verliest beide premies als de prijs stabiel blijft.



Limiet: 50 gelijktijdige posities. Ideaal voor beginnende handel met een hefboom zonder angst voor liquidatie.



**sats ↔ sUSD**: Zet onmiddellijk uw satoshis om in synthetische dollars (sUSD) om uzelf te beschermen tegen volatiliteit, of vice versa om weer Bitcoin blootstelling te krijgen.



## Platformtoegang en account aanmaken



### Ga naar LN Markets



Ga naar [lnmarkets.com](https://lnmarkets.com) en klik op "Open App".



![Page d'accueil LN Markets](assets/fr/01.webp)



### Maak je account aan



Het welkomstscherm biedt verschillende verbindingsmethoden:



![Méthodes de connexion](assets/fr/02.webp)



**Opties beschikbaar** :


1. **Registreren met een Lightning wallet** (aanbevolen) : LNURL-auth met Phoenix, Breez, Zeus of BlueWallet


2. **Registreer met e-mail**: klassieke account (beperkt Lightning-ervaring)


3. **Alby** of **Ledger**: browserextensies



### Verbinding via Lightning (LNURL-auth)



Klik op "Registreer met een Lightning wallet". Scan de QR-code met je wallet Lightning:



![QR code LNURL-auth](assets/fr/03.webp)



Je wallet ondertekent automatisch een cryptografische aanvraag en je account wordt direct aangemaakt, zonder e-mail of wachtwoord. Sterke beveiliging en totale anonimiteit.



### Eerste configuratie



![Configuration post-connexion](assets/fr/04.webp)



**Beschikbare parameters** :




- Gebruikersnaam**: personaliseer je gebruikersnaam
- Automatische opnames**: activeer automatische opnames naar uw wallet na sluiting van de transactie
- Authenticatie met twee factoren**: verbeterde beveiliging met 2FA
- Documentatie**: toegang tot officiële bronnen



## Interface tour



De interface van LN Markets is onderverdeeld in verschillende secties die toegankelijk zijn via het menu aan de zijkant:



### Dashboard



![Dashboard](assets/fr/06.webp)



Toont uw prestaties per producttype (Futures Cross, Futures Isolated, Opties) met P&L, verhandelde volumes en uw persoonlijke Address Lightning (bijv. `pivi@lnmarkets.com`).



### Profiel



![Profil trader](assets/fr/07.webp)



Gedetailleerde statistieken: aantal transacties, handelaarstype (SCALPER, etc.), mediane positieduur, uitsplitsing Long/Short, winstpercentage, gemiddelden (hoeveelheid, marge, hefboom) en progressieve kostenstructuur op basis van volume.



### Handelingen



![Historique des trades](assets/fr/08.webp)



Het tabblad Trades toont een volledige geschiedenis van uw posities, met alle belangrijke gegevens: aanmaakdatum, richting (Long/Short), positiegrootte (hoeveelheid), vastgelegde marge, instap- en uitstapprijs, gerealiseerde winst/verlies (P&L) en handelskosten. U kunt filteren op producttype (futures/opties) en uw gegevens exporteren voor externe analyse of boekhouding.



### Instellingen



![Paramètres de la plateforme](assets/fr/05.webp)



Het tabblad Instellingen biedt twee tabbladen: **Account** en **Interface**.



*tabblad *Account**:



Accountbeheer met bewerkbare velden :




- Gebruikersnaam**: wijzig je gebruikersnaam (bijv. "pivi") met de knop "Bijwerken
- E-mail**: je e-mailadres toevoegen/wijzigen
- Bitcoin-stortingsadres**: het bitcoin-adres dat u kunt gebruiken om on-chain-fondsen te storten.



**Drie configuratieknoppen** :




- Verschijnen in leaderboards**: kies of je wel of niet wilt verschijnen in publieke leaderboards
- Gebruik Taproot adressen**: gebruik Bitcoin adressen Taproot voor on-chain stortingen/opnames
- Automatische geldopnames**: activeer automatische geldopnames naar uw wallet Lightning na het sluiten van de transactie



**Accountmigratie**: Sectie waarmee u uw Lightning-account kunt migreren naar klassieke e-mail/wachtwoordverificatie.



**Session beheer**: knop "Clear session and local data" (sessie en lokale gegevens wissen) om de verbinding te verbreken en lokale browsergegevens op te schonen.



*tabblad *Interface**:



Pas de gebruikerservaring aan met zeven toggles:




- Orderbevestiging overslaan**: deactiveer bevestigingsmodal vóór de uitvoering van de transactie (snel handelen)
- Toon tooltips**: toon tooltips wanneer u met de muis over elementen beweegt
- Privémodus (maskeert gevoelige gegevens)**: maskeert hoeveelheden en gevoelige gegevens in de interface (privacymodus)
- Toon netto PL in profiel**: toon nettowinst/-verlies in je openbare profiel
- Eenheidspictogrammen gebruiken**: pictogrammen voor valuta-eenheden weergeven (sats, $)
- Geluidsmeldingen inschakelen**: activeer geluidsmeldingen voor handelsgebeurtenissen
- Bureaubladmeldingen inschakelen**: bureaubladmeldingen van het besturingssysteem activeren



### Wallet



![Wallet](assets/fr/09.webp)



Bitcoin en synthetische USD-saldi met geschiedenis van stortingen, opnames, overboekingen, swaps, financiering en on chain adresbeheer.



### API



![API V3](assets/fr/10.webp)



LN Markets biedt een complete API REST (V2 en V3) om uw handel volledig te automatiseren via scripts of bots. U kunt API sleutels aanmaken met aanpasbare rechten (alleen-lezen, handel, opnames) direct vanuit de interface. Officiële TypeScript en Python SDK's zijn beschikbaar voor eenvoudige integratie. De volledige API V3 documentatie is beschikbaar op [api.lnmarkets.com/v3](https://api.lnmarkets.com/v3).



## Eerste storting van fondsen



Klik op "Storten". Er zijn drie methoden beschikbaar:



![Modal de dépôt](assets/fr/11.webp)



1. **LNURL**: scan de QR-code met uw wallet Lightning


2. **Invoice**: voer een bedrag in en scan vervolgens de Lightning-factuur


3. **On-Chain**: depot Bitcoin on chain



## Handel in de praktijk



### Trade Futures Long: inzetten op de opwaartse trend



Klik in het dashboard op "Futures" en vervolgens op "Geïsoleerd". Klik op **"Buy"** om een Long positie te openen.



![Interface Futures Long](assets/fr/12.webp)



Klik op het pictogram **calculator** naast de knop "Kopen" om de positiecalculator weer te geven:



![Calculateur de position Long](assets/fr/13.webp)



**Concreet voorbeeld** :




- Hoeveelheid**: $100 (positiegrootte)
- Handelsmarge**: 12.336 sats (vastgelegde marge)
- Hefboom**: 7.73× (elke 1% BTC variatie = 7,73% op uw kapitaal)
- Ingangsprijs** : $104,863.5
- Liquidatie**: $92.852 (kritische automatische liquidatieprijs)
- Exitprijs**: $110.000 (voor winstberekening)
- PL** : 4.492 sats (winst bij exit op $110.000)



**Scenario's** :




- Stijging +4,9%** ($110.000) : +4.492 sats winst (+36,4%)
- Neutraal** ($104.863) : -185 sats (alleen vergoedingen)
- Afname -11,5%** ($92.852): totale liquidatie (-100%)



Klik op de knop "Kopen" om de transactie te bevestigen. **Twee mogelijke gevallen** :





- Als je genoeg liquiditeit** in je account hebt: er wordt direct een bevestigingsmodal weergegeven (afbeelding hieronder). Klik op "Ja" om de transactie direct uit te voeren.



![Confirmation trade Long](assets/fr/14.webp)





- Als je niet genoeg geld hebt**: in plaats daarvan wordt een Lightning QR-code weergegeven. Scan deze met uw wallet Lightning om de vereiste marge te betalen. De transactie wordt automatisch geopend na ontvangst van de betaling



### Futures short verhandelen: inzetten op de neerwaartse trend



Klik op **"Sell"** om een Short-positie te openen (je wint als de prijs daalt). Open de rekenmachine met het rekenmachinepictogram om je positie in te stellen:



![Calculateur de position Short](assets/fr/15.webp)



Klik op "Verkopen" om te bevestigen. Wat betreft de Long, **twee mogelijke gevallen**:





- Als je genoeg geld hebt**: directe bevestigingsmodus, klik op "Ja"
- Als je niet genoeg geld hebt**: er wordt een Lightning QR-code weergegeven (afbeelding hieronder). Scan deze met je wallet Lightning om de vereiste marge te betalen:



![Paiement Lightning pour Short](assets/fr/16.webp)



Zodra de Lightning-betaling is ontvangen, wordt uw Short-positie automatisch geopend. Je kunt deze dan beheren vanuit de handelsinterface.



#### Een positie sluiten



Om uw positie te sluiten (Long of Short), klikt u op het **kleine kruisje in de rechterbenedenhoek** van de beheerinterface:



![Interface de clôture](assets/fr/17.webp)



Er wordt een bevestigingsdialoog weergegeven om de sluiting van de transactie te bevestigen:



![Confirmation clôture](assets/fr/18.webp)



Het venster toont je huidige winst- en verliesrekening. Klik op "Ja" om te sluiten. Het saldo wordt onmiddellijk toegevoegd (winst) of afgetrokken (verlies) van je Wallet via Lightning.



### Handel in opties Call: voorwaardelijk recht om te kopen



Opties bieden **risico beperkt** tot de betaalde premie, zonder mogelijkheid tot liquidatie. Een Call geeft je het recht (niet de plicht) om Bitcoin te kopen tegen de uitoefenprijs voor de expiratie. In tegenstelling tot futures kunt u nooit meer verliezen dan de geïnvesteerde premie.



Klik in het Dashboard op "Opties" en selecteer vervolgens de tab "Gesprek".



![Interface Options Call](assets/fr/19.webp)



Configureer je transactie met de volgende parameters:




- Hoeveelheid**: $100 (grootte van je contract)
- Vervaldatum** : 2025-11-15 (vervaldatum)
- Staking**: $96.000 (richtprijs)



De andere velden worden automatisch berekend:




- Marge**: 1.045 sats (te betalen premie, jouw investering)
- Breakeven**: $96.923 (prijs om je inzet terug te verdienen)
- Delta**: 40 (prijsgevoeligheid Bitcoin)



**Hoe bereken je je winst?



Je winst hangt af van de Bitcoin prijs op de expiratiedatum. Formule: **(BTC prijs - Strike) × Contract grootte - Premie betaald**.



**Concrete voorbeelden** :





- Bitcoin tegen $96.000** (huidige prijs) : Intrinsieke waarde = $0. **Verlies: -1,045 sats** (je verliest de premie)





- Bitcoin op $97.000**: Intrinsieke waarde = (97.000 - 96.000) × 0,00105 BTC = $1,05. Omgerekend naar sats ≈ 2.175 sats. **Winst: 2,175 - 1,045 = +1,130 sats** (+108% winst)





- Bitcoin op $98.000**: intrinsieke waarde = $2.000 ≈ 3.224 sats. **Winst: +2.179 sats** (+208% winst)





- Bitcoin op $100.000**: intrinsieke waarde = $4.000 ≈ 5.263 sats. **Winst: +4.218 sats** (+403% winst)





- Bitcoin onder $96.000**: Optie loopt waardeloos af. **Beperkt verlies: -1.045 sats**, geen liquidatie mogelijk



Klik op "Call kopen". Er verschijnt een bevestigingsdialoogvenster:



![Confirmation Call option](assets/fr/20.webp)



Klik nogmaals op "Call kopen" om te bevestigen. De optie verschijnt in "Lopende Opties". Op de vervaldatum berekent LN Markets automatisch de intrinsieke waarde en past je winst/verlies aan.



**Opmerking over putopties** : De werking is identiek aan die van een call, maar dan omgekeerd. Met een put wedt u erop dat de Bitcoin prijs **daalt**. Als Bitcoin onder uw uitoefenprijs daalt, wint u; als het erboven blijft, verliest u alleen de betaalde premie. De berekening van de winst volgt dezelfde logica: **(Strike - BTC prijs) × Contract grootte - Betaalde premie**.



### Opname bliksemfonds



Klik op "Intrekken":



![Modal de retrait](assets/fr/21.webp)



**Methodes** : LNURL, Invoice, Lightning Address, On-Chain.



**Invoice procedure** :


1. Een Lightning-factuur genereren vanaf uw wallet


2. Kopieer de factuur (begint met `lnbc...`)


3. Plak het in het LN Markets veld


4. Terugtrekking bevestigen


5. Je wallet wordt binnen 1-3 seconden gecrediteerd



Geen Lightning-opnamekosten, slechts minimale routingkosten (<0,1% in de praktijk).



## Risico's en best practices



**Hoofdrisico's** :




- Totale liquidatie**: hoge hefboomwerking kan 100% van de marge in enkele minuten wegvagen
- Experimentele dienst**: alfa-fase, technologische onzekerheden
- Tegenpartijrisico**: platform blijft één tegenpartij



**Best practices** :



1. **Kapitaalbeheer**: hanteer een risicobeheerstrategie die is afgestemd op jouw profiel. Bijvoorbeeld: wijs 5% van je totale vermogen toe aan handel met een hefboom en riskeer maximaal 1% van dit kapitaal per transactie (bijv.: 1 BTC activum → 5M sats om te verhandelen → 50k sats max risico per positie)



2. **Systematische stop-loss**: configureer stop-losses om je verliezen per transactie te beperken. Met een 1%-risicoregel, bijvoorbeeld, vertegenwoordigen zelfs 10 opeenvolgende verliezende transacties slechts 10% van uw handelskapitaal



3. **Start small**: test eerst met een paar duizend satss om de mechanismen te begrijpen voordat u uw kapitaalbeheerstrategie toepast



4. **Neem uw winsten regelmatig op**: stel uw winsten veilig op uw wallet en laat alleen actief handelskapitaal achter op het platform



5. **Pas op voor hefboomwerking**: vermijd een hefboomwerking >20× tenzij u zich volledig bewust bent van liquidatierisico's



**Kosten**: geen Lightning stortings/opnamekosten, spread ~0,1% per transactie (dalend tot 0,06% afhankelijk van volume).



## Voordelen en beperkingen



**Voordelen** :




- Niet-custodiaal (totale controle exclusief handelsperioden)
- KYC-vrij (anonimiteit via Lightning/Nostr)
- Directe vereffeningen (stortingen/opnames in seconden)
- Nul-slippage uitvoering met liquiditeitsaggregatie
- API publiek en Nostr ondersteuning



**Beperkingen** :




- Service alfa (mogelijke evoluties)
- Lagere liquiditeit dan Binance/Deribit
- Verboden voor inwoners van de VS



## Conclusie



LN Markets belichaamt een belangrijke evolutie van Bitcoin handel door Lightning Network te integreren om de controle terug te geven aan gebruikers. Voor slimme bitcoiners die willen speculeren zonder hun soevereiniteit in gevaar te brengen, is het een uniek alternatief voor traditionele gecentraliseerde beurzen.



Het platform blijft zich ontwikkelen met USDT lineaire futures en niet-custodiale handel via Discreet Log Contracts (DLC) in ontwikkeling. Door goede risicobeheerpraktijken toe te passen (kleine bedragen, stop-loss, regelmatige opnames), wordt LN Markets een krachtig hulpmiddel om de hefboomwerking van Bitcoin op verantwoorde wijze te verkennen.



Begin klein, test met een paar duizend satss en verken geleidelijk deze nieuwe Lightning Network grens. Fijne soevereine handel ⚡️!



## Bronnen





- [LN Markets officiële website](https://lnmarkets.com)
- [Documentatie](https://docs.lnmarkets.com)