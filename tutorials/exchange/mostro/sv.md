---
name: Mostro
description: KYC-fri Bitcoin P2P-växlingsplattform via Lightning och Nostr
---

![cover](assets/cover.webp)



Hur förvärvar eller säljer du bitcoins utan att äventyra din ekonomiska suveränitet? Centraliserade plattformar inför invasiva KYC-förfaranden som exponerar dina personuppgifter, med möjlighet till godtycklig kontofrysning eller statlig övervakning.



**Mostro P2P** erbjuder ett decentraliserat alternativ som kombinerar Lightning Network, Nostr-protokollet och hold-fakturor. Dess främsta innovation: ett automatiserat spärrsystem där dina bitcoins förblir under din kontroll under hela börsen, vilket eliminerar risken för stöld, börskonkurs eller godtycklig konfiskering.



## Vad är Mostro P2P?



Mostro P2P är ett Bitcoin-utbytesprotokoll med öppen källkod skapat av **grunch**, utvecklare av den populära Telegram-boten **lnp2pbot** som lanserades 2021. Medan lnp2pbot redan möjliggjorde KYC-fria P2P-utbyten via Lightning, presenterade det en stor sårbarhet: **Telegram utgör en centraliserad punkt av misslyckande** som är mottaglig för censur av regeringar.



Mostro representerar den **decentraliserade utvecklingen** av detta koncept: genom att ersätta Telegram med **Nostr**-protokollet (ett oöverskådligt nätverk av distribuerade reläer) eliminerar Mostro denna systemrisk. Protokollet kombinerar Lightning Network för omedelbara transaktioner, Nostr för censurresistent kommunikation och **håll fakturor** för att skapa en verkligt icke-frihetsberövande automatiserad spärr.



### Teknisk arkitektur



Mostro arbetar genom tre komponenter:




- Daemon Mostrod**: samordnar utbyten mellan användare och Lightning Network
- Lightning**-nod: skapar innehavsfakturor (~24h kryptografisk spärr)
- Mostro** kunder: användargränssnitt (CLI, mobil, webb)



Order publiceras på Nostr som publika händelser (typ 38383), medan privata affärer överförs via krypterade meddelanden från början till slut (NIP-59, NIP-44). Varje Mostro-instans definierar sina egna avgifter (i allmänhet mellan 0,3% och 1%) och transaktionsgränser (från några tusen till flera hundra tusen sats, beroende på instans).



### Avgörande fördelar



**Censurresistent**: Ingen regering kan stänga av Mostro så länge Nostr-reläer finns någonstans i världen. Till skillnad från den sårbara lnp2pbot via Telegram tillåter Mostro utbyten som är **censurskyddade **.



**Escrow icke-frihetsberövande**: Blixthållningsfakturor låser dina bitcoins utan att överföra dem permanent. Dina medel förblir under din kontroll och returneras automatiskt till dig i händelse av ett problem (~ 24 timmar).



**Konfidentialitet genom design**: Två lägen tillgängliga för att passa dina behov. Reputation Mode** kopplar ditt rykte till din Nostr-nyckel för att bygga upp ett varaktigt förtroende. Full Private Mode** ger absolut anonymitet med efemära nycklar för engångsbruk.



## Huvudsakliga egenskaper



**Decentraliserad kommunikation**: Alla order publiceras på Nostr via kryptografiskt signerade events. Privata förhandlingar överförs via krypterade meddelanden från början till slut, vilket garanterar absolut sekretess.



**Reputationssystem**: 5-stjärnigt betyg med iterativ beräkning som lagras permanent på Nostr. Gör att du gradvis kan bygga upp ett rykte som en pålitlig handlare.



**Decentraliserat skiljeförfarande**: I händelse av en tvist granskar en opartisk skiljedomare bevisen och fattar ett beslut baserat på transparenta kriterier. Varje tvist genererar en unik token för spårbarhet.



** Betalningsflexibilitet**: Stöd för många fiat-valutor via yadio.io:s växelkurstjänst. Accepterar SEPA-överföringar, PayPal, Revolut, kontanter och alla metoder som överenskommits mellan parterna.



## Mostro kunder tillgängliga



Mostro erbjuder två huvudsakliga operativa klienter för dina P2P-växlar.



### Mostro CLI - Klient för kommandoraden



**Mostro CLI** är den mest mogna och funktionella klienten. Den är skriven i Rust och erbjuder hela Mostros utbud av funktioner via ett kommandoradsgränssnitt. Kompatibel med macOS, Linux och Windows.



**Huvudreglage** :




- `listororder`: Visa alla tillgängliga order
- `neworder` : Skapa en ny köp- eller säljorder
- `takesell` / `takebuy`: Ta en köp- eller säljorder
- `fiatsent`: Bekräfta sändning av fiat-betalning
- "frigöra": Frigör spärren och slutför bytet
- `getdm`: Visa direktmeddelanden
- `rate` : Utvärdera din motpart efter ett byte



Idealisk för tekniska användare, automation och miljöer som kräver maximal säkerhet.



### Mostro Mobile - Applikation för smartphone



Den **mobila appen** i alpha-version möjliggör P2P-handel direkt från din smartphone. Intuitiv grafisk Interface med navigering i flikar, ordervisning, avancerade filter och integrerad chatt för att kommunicera med dina motparter.



Tillgänglig för ** Android ** (via APK på GitHub), det är det optimala valet för användare som föredrar enkelhet och tillfällig mobilhandel.



### Mostro-web - Interface-webb (under utveckling)



Interface avancerad JavaScript-webbapplikation under aktiv utveckling. Utformad för att erbjuda en komplett användarupplevelse med omfattande funktioner för handel och portföljhantering. Åtkomst via webbläsare utan krav på installation.



## Installation och konfiguration



Denna handledning guidar dig genom installation och användning av de två viktigaste Mostro-klienterna: CLI och mobilapplikationen.



### Viktiga förutsättningar



Innan du börjar behöver du :





- En fungerande Lightning Network** wallet med tillräcklig likviditet (eller Lightning-kompatibel)
 - Rekommenderas: Phoenix, Breez, Wallet eller Satoshi...
 - Minst 1000 satoshis i likviditet för att testa



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- En privat nyckel från Nostr** (format `nsec1...`)
 - Skapa en dedikerad handelsnyckel på [nostrkeygen.com](https://nostrkeygen.com/)
 - Viktigt**: Använd aldrig din huvudsakliga personliga Nostr-nyckel
 - Förvara din privata nyckel på en säker plats (lösenordshanterare)





- Valfritt men rekommenderas**: VPN- eller Tor-anslutning för att maskera din IP-adress



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Mostro CLI installation



#### På macOS



**Steg 1: Rust-kontroll**



Kontrollera att Rust är installerat (version 1.64+ krävs):



```bash
rustc --version
```



Om Rust inte är installerad :



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**Steg 2: Kloning av förvaret**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**Steg 3: Konfiguration**



Kopiera och redigera :



```bash
cp .env-sample .env
```



Öppna `.env` och konfigurera dina inställningar:



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**Viktigt för synkronisering av CLI/Mobile**: För att få tillgång till samma order på CLI och i mobilappen måste du använda **samma Mostro Pubkey** och **samma Nostr reläer** i båda klienterna. Kontrollera dessa inställningar i Inställningar i mobilappen.



![Configuration .env](assets/fr/02.webp)



**Steg 4: Installation**



Kompilera och installera CLI :



```bash
cargo install --path .
```



Kompileringen tar 1-2 minuter. Den körbara filen `mostro-cli` kommer att installeras i `~/.cargo/bin/`.



![Installation du CLI](assets/fr/03.webp)



**Steg 5: Kontrollera**



Kontrollera att allt fungerar:



```bash
mostro-cli --help
```



Du bör se den fullständiga listan över beställningar.



![Vérification avec --help](assets/fr/04.webp)



#### På Linux (Ubuntu/Debian)



Installation identisk med macOS, med tillägg av :



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Följ sedan steg 3 och 4 i avsnittet om macOS.



#### På Windows



Installera först Rust via [rustup.rs](https://rustup.rs/), använd sedan PowerShell :



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Identisk konfiguration: kopiera `.env-sample` till `.env` och fyll i dina parametrar.



### Installation av Mostro Mobile



#### På Android



**Steg 1**: Gå till [GitHub releases page](https://github.com/MostroP2P/mobile/releases) och ladda ner filen **app-release.apk** (ca 65 MB).



![Page GitHub Releases](assets/fr/10.webp)



**Steg 2: När du har laddat ner öppnar du APK-filen från dina nedladdningar. Android kommer att be dig att godkänna installationen från den här källan.



![Téléchargement et installation APK](assets/fr/11.webp)



**Steg 3**: Följ onboarding-skärmarna, som presenterar funktionerna:




- Handla Bitcoin fritt - ingen KYC** : Handla utan identitetsverifiering tack vare Nostr
- Sekretess som standard**: Välj mellan Reputation-läge och Full privacy-läge
- Säkerhet i varje steg**: Skydd med fakturor som inte innehåller förvarstagande



![Écrans d'accueil Mostro](assets/fr/12.webp)



**Steg 4**: Fortsätt onboarding för att upptäcka :




- Helt krypterad chatt**: End-to-end-krypterad kommunikation
- Ta ett erbjudande**: Bläddra i orderboken och välj ett erbjudande
- Hittar du inte vad du behöver? ** : Skapa din egen anpassade order



![Suite onboarding](assets/fr/13.webp)



**Steg 5: När onboardingen är klar genererar appen automatiskt ett par Nostr-nycklar. Gå till menyn (☰) och sedan **Account** för att spara dina **Secret Words** (återställningsfras). Det är också på den här skärmen som du har möjlighet att ändra sekretessläget som tidigare nämnts.



![Menu et sauvegarde des clés](assets/fr/15.webp)



**Viktigt**: Skriv ner din återställningsfras på en säker plats (lösenordshanterare, pappersskåp).



### Initial säkerhetskonfiguration



Oavsett vilken plattform du använder:





- Dedikerad nyckel**: Använd en separat Nostr-identitet för handel
- Små belopp**: Börja med mindre än 10 000 sats för att komma igång
- Flera reläer**: Konfigurera 3-5 geografiskt spridda reläer
- Nätverksskydd**: Aktivera VPN eller Tor för att dölja din IP-adress
- Wallet säker**: Aktivera automatisk låsning av din wallet Lightning



## Använd med CLI



I detta avsnitt demonstreras köp av bitcoins via Mostro CLI enligt ett verkligt användningsfall.



### Steg 1: Lista tillgängliga order



Kommandot "Lista order" visar alla aktiva order:



```bash
mostro-cli listorders
```



Du kommer att se en tabell med detaljer om varje order: ID, typ (köp/sälj), belopp, valuta, betalningsmetod.



![Liste des ordres disponibles](assets/fr/05.webp)



I detta exempel syns en order om att sälja 5 EUR via Revolut (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).



### Steg 2: Ta emot beställningen



För att köpa dessa bitcoins, ta ordern med `takesell` :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



Mostro kommer att be dig att tillhandahålla en **Lightning-faktura** för att ta emot BTC. Det exakta beloppet i satoshis anges (här: 4715 sats).



![Prise d'ordre de vente](assets/fr/06.webp)



### Steg 3: Ange din Lightning-faktura



Skapa en Lightning-faktura från din wallet (Phoenix, Breez, etc.) för det exakta beloppet och skicka den sedan :



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



Systemet bekräftar försändelsen och säger att du ska vänta på att säljaren betalar väntelägesfakturan innan du aktiverar spärren.



![Envoi de la Lightning invoice](assets/fr/07.webp)



### Steg 4: Kontakta säljaren



När spärren har aktiverats använder du `dmtouser` för att begära betalningsuppgifter från säljaren:



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### Steg 5: Hämta svaret



Kontrollera direktmeddelanden för att se säljarens svar:



```bash
mostro-cli getdm
```



Säljaren ger dig sitt betalnings-ID (här hans Revtag: `@satoshi`).



![Réception de la réponse](assets/fr/09.webp)



### Steg 6: Göra fiat-betalningen



Skicka betalningen via den överenskomna metoden (Revolut i detta exempel) till de kontaktuppgifter som anges. **Behåll alla styrkande handlingar** (skärmdumpar, transaktionsreferenser).



### Steg 7: Bekräfta betalningens avsändande



När betalningen är genomförd, meddela Mostro :



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### Steg 8: Mottagande av bitcoins



Så snart säljaren bekräftar mottagandet av fiat och frigör spärren med kommandot `release`, får du omedelbart dina bitcoins på den Lightning-faktura du angav.



### Steg 9: Utvärdering



Betygsätt säljaren för att bidra till det decentraliserade ryktet:



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### Användbara kommandon



**Annullera en order** (innan den har tagits) :


```bash
mostro-cli cancel -o <order-id>
```



**Skapa en ny försäljningsorder** :


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**Öppna en tvist** :


```bash
mostro-cli dispute -o <order-id>
```



## Använd med mobilapplikationen



I detta avsnitt demonstreras försäljningen av bitcoins via Mostro Mobile genom att följa ett verkligt användningsfall.



### Interface huvud



Applikationen har 3 huvudflikar:





- Orderbok**: Bläddra bland tillgängliga köp- (BUY BTC) och säljorder (SELL BTC)
- Mina affärer**: Visa dina aktiva och historiska order
- Chatta**: Kommunicera med dina motparter med hjälp av siffror



![Interface principale](assets/fr/14.webp)



### Rekommenderad konfiguration



Innan du börjar handla ska du göra några inställningar via menyn (☰) > **Inställningar** :





- Blixten Address** (valfritt): För att ta emot betalningar direkt
- Reläer**: Lägga till flera Nostr-reläer för motståndskraft (t.ex. `wss://nos.lol`, `wss://relay.damus.io`)
- Mostro Pubkey**: Kontrollera den publika nyckeln för den Mostro-instans du använder



![Paramètres de l'application](assets/fr/16.webp)



**Viktigt för CLI/Mobil synkronisering**: Om du använder både CLI och mobilappen ska du konfigurera **exakt samma Nostr-reläer och Mostro Pubkey** i båda klienterna. Utan denna identiska konfiguration kommer du inte att se samma order tillgängliga på båda gränssnitten. De reläer och Mostro Pubkey som syns i Inställningar (skärmdump ovan) måste matcha dem i din CLI `.env'-fil.



### Steg 1: Skapa en säljorder



Tryck på den gröna **"+"**-knappen längst ned till höger och välj sedan **SELL** (röd knapp).



![Boutons de création d'ordre](assets/fr/17.webp)



Fyll i formuläret för skapande :



1. **Valuta**: Välj den valuta som du vill ta emot (EUR, USD, etc.)


2. **Belopp** : Ange beloppet i fiat (t.ex. 1 till 3 EUR)


3. **Betalningsmetoder** : Välj metod (t.ex. "Revolut")


4. **Pris typ**: Välj "Marknadspris"


5. **Premie**: Justera premien (skjutreglage från -10% till +10%, rekommenderas: 0% för att sälja snabbt)



Tryck på **Sänd** för att publicera din order.



### Steg 2: Bekräftelse av publicering



Din order är nu publicerad! Den kommer att vara tillgänglig i 24 timmar. Du kan avbryta den när som helst innan en köpare tar den genom att utföra kommandot `cancel`.



![Ordre publié](assets/fr/18.webp)



Ordern visas på fliken **My Trades** med statusen "Pending" och märket "Created by you".



### Steg 3: En köpare tar emot din beställning



När en köpare tar din order får du ett meddelande. Se detaljer i **Mina affärer**.



![Ordre pris par un acheteur](assets/fr/19.webp)



**Viktig instruktion**: Du måste nu **betala den hållfaktura** som visas för att låsa dina bitcoins (här 4674 sats för 1-5 EUR) i spärren. Du har **15 minuter max** annars kommer växlingen att avbrytas.



Kopiera spärrfakturan och betala den från din wallet Lightning (Phoenix, Breez, etc.).



### Steg 4: Kommunicera med köparen



När spärren har aktiverats trycker du på **CONTACT** för att öppna den krypterade chatten med köparen.



Köparen (här "anonymous-gloriaZhao") kommer att kontakta dig för att begära dina betalningsuppgifter. Vänligen svara med dina uppgifter (Revtag, IBAN, etc.).



![Chat avec l'acheteur](assets/fr/20.webp)



### Steg 5: Mottagande av fiat-betalning



Vänta tills du får fiat-betalningen på ditt Revolut-konto (eller annan överenskommen metod). **Kontrollera noggrant**:




- Det exakta beloppet
- Avsändaren
- Referens om så önskas



Köparen kommer att informera dig via chatten att han har skickat betalningen. Mostro kommer också att visa ett meddelande som bekräftar att fiaten har skickats till dig.



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### Steg 6: Frigör spärren



När du har **bekräftat mottagandet** av fiat-betalningen på ditt konto, tryck på den gröna **RELEASE**-knappen och bekräfta att du skickar satss till köparen.



![Libération de l'escrow](assets/fr/20.webp)



Bitcoins överförs omedelbart till köparen via hans Lightning-faktura.



### Steg 7: Utvärdera övervägandena



Efter frisläppandet, tryck på **RATE** för att betygsätta köparen. Välj mellan 1 och 5 stjärnor (här 5/5) och tryck på **Submit Rating**.



![Évaluation de la contrepartie](assets/fr/21.webp)



Utbytet är över!



### Köp bitcoins med mobilappen



Processen för att **köpa ** bitcoins är liknande men omvänd:



1. Bläddra i fliken **Orderbok** > **KÖP BTC** för att se säljorder


2. Klicka på en intressant order för att se detaljer


3. Tryck **Ta order**


4. Lämna in din Lightning-faktura (genererad från din wallet)


5. Vänta på att säljaren ska aktivera spärren


6. Kontakta säljaren via **CONTACT** för betalningsinformation


7. Skicka fiat-betalning (behåll bevis)


8. Säljaren släpper spärren efter verifiering


9. Ta emot bitcoins direkt på din Lightning-faktura


10. Betygsätt säljaren (1-5 stjärnor)



### Hantering av problem



**Avbryta en order**: I **My Trades** trycker du på din order och sedan på knappen **CANCEL** (endast tillgänglig innan den tas).



**Öppna en tvist**: Om en oenighet uppstår, tryck på **DISPUTE** i orderinformationen. Bifoga alla bevis (skärmdumpar från chatten, referenser till banktransaktioner).



## Fördelar och begränsningar



### Fördelar



**Finansiell suveränitet**: Dina bitcoins lämnar aldrig din direkta kontroll tack vare hold invoice-mekanismen, vilket eliminerar risken för börskonkurs eller piratkopiering.



**Censurresistent**: Ingen myndighet kan stänga ner nätverket eller censurera dina order. Systemet fungerar så länge Nostr-reläerna är i drift.



**Default anonymitet**: Endast en pseudonym Nostr-nyckel identifierar dig, utan KYC eller personuppgifter. End-to-end krypterad kommunikation.



**Flexibilitet i betalningen**: Alla betalningsmetoder som accepteras av båda parter är möjliga (överföringar, mobilappar, kontanter, byteshandel).



### Begränsningar



**Tidig utveckling**: Rudimentära gränssnitt och teknisk inlärningskurva krävs.



**Begränsad likviditet**: Begränsat antal order, särskilt för stora belopp eller sällsynta valutor.



**Tekniska krav**: Grundläggande förståelse för Lightning och Nostr krävs.



**Individuellt ansvar**: Inget centraliserat stöd vid problem, försiktighet krävs.



## Slutsats



Mostro P2P utgör ett lovande alternativ till centraliserade börser och kombinerar Lightning Network, Nostr och automatiserad spärr för verkligt decentraliserad handel. Trots sin tidiga utveckling och begränsade likviditet erbjuder plattformen redan finansiell suveränitet, censurmotstånd och anonymitet som standard.



För bitcoiners som föredrar autonomi och sekretess är Mostro ett genomförbart alternativ som är värt att utforska. Dess decentraliserade arkitektur garanterar gemenskap snarare än kommersiell utveckling, vilket banar väg för en framtid med verkligt fria Bitcoin-börser.



## Resurser



### Officiell dokumentation




- [Mostros officiella webbplats](https://mostro.network)
- [Teknisk dokumentation](https://mostro.network/docs-english/index.html)
- [Mostro Foundation](https://mostro.foundation)



### Källkod och utveckling




- [Huvudarkiv på GitHub](https://github.com/MostroP2P/mostro)
- [Webbklient](https://github.com/MostroP2P/mostro-web)
- [Kund CLI](https://github.com/MostroP2P/mostro-cli)



### Gemenskap




- [Nostr Protocol](https://nostr.com)
- [Lightning Network guider](https://lightning.network)