---
name: LN Markets
description: Bitcoin handelsplattform på Lightning Network
---

![cover](assets/cover.webp)



LN Markets är den första verkligt Lightning-nativa Bitcoin-handelsplattformen, så att du kan handla Bitcoin-derivat med hävstångseffekt direkt från din wallet Lightning, utan KYC, omedelbar avveckling och minimal förvaring. Den lanserades 2020 och eliminerar friktionerna hos traditionella börser: ingen identitetsverifiering, inga blockerade insättningar, ingen väntan på blockkedjebekräftelser. Din wallet Lightning blir ditt handelskonto.



## Vad är LN Markets?



LN Markets erbjuder **Futures** (eviga kontrakt med hävstångseffekt upp till 100×) och **Options** (Call/Put med risk begränsad till den betalda premien). Plattformen fungerar som ett likviditetsaggregeringslager som konsoliderar flera handelsplatser för optimalt utförande utan slippage. Dina medel är endast låsta under den exakta varaktigheten för dina aktiva positioner, inte dagar eller veckor som med ett traditionellt depåkonto.



### Handelsprodukter tillgängliga



**Futures (evighetskontrakt)**



Eviga kontrakt är terminer utan utgångsdatum, vilket gör att du kan spekulera i Bitcoin-prisutvecklingen med hävstångseffekt. LN Markets erbjuder två marginalhanteringslägen:



**Isolerat läge**: Varje position har sin egen dedikerade marginal. Endast de medel som tilldelats den här specifika positionen är i riskzonen. Om positionen når likvidationspriset likvideras **endast denna position**, dina andra positioner och återstående saldo påverkas inte. Perfekt för att strikt begränsa risken per handel.



**Cross Mode (Cross Margin)** : Marginalen delas mellan alla dina öppna positioner. Ditt totala kontosaldo fungerar som säkerhet för alla dina positioner. Om en position går dåligt använder systemet hela ditt tillgängliga saldo för att undvika likvidation. **Risk**: om ditt totala saldo tar slut kan alla dina positioner likvideras samtidigt. Rekommenderas endast för erfarna handlare som vill maximera kapitaleffektiviteten.



**Positionshantering** :





- Lång position**: du satsar på ökningen av BTC/USD. Om priset stiger vinner du; om det faller förlorar du. **Exempel**: Bitcoin på 100 000 USD, du öppnar en Long med 10 000 sats och 10× hävstång. Om Bitcoin stiger till 105 000 USD (+5 %) vinner din position 50 % (5 % × 10), dvs. ~5 000 sats i vinst. Om Bitcoin faller till 95 000 USD (-5 %) förlorar du 50 %, dvs. en förlust på ~5 000 sats.





- Kort position**: du satsar på att BTC/USD faller. Om priset går ner vinner du; om det går upp förlorar du. **Exempel**: Bitcoin på 100 000 USD, du öppnar en short med 10 000 sats och 10× hävstång. Om Bitcoin faller till 95 000 USD (-5 %) vinner du 50 %, dvs. ~5 000 sats. Om Bitcoin stiger till 105 000 USD (+5 %) förlorar du 50 %.



Hävstångseffekten (upp till 100×) förstärker vinster och förluster proportionellt. En mekanism för **finansieringsgrad** (periodiska avgifter var 8:e timme) balanserar långa och korta positioner. Du kan hantera upp till 100 terminspositioner samtidigt.



**Alternativ**



En option är som en **lotterilott med utgångsdatum**. Du betalar en premie för att satsa på riktningen för Bitcoin-priset. **Stor fördel**: du kan aldrig förlora mer än den betalda premien, ingen avveckling möjlig.





- Köpoption (hausseinriktad satsning)**: Du satsar på att Bitcoin kommer att stiga över lösenpriset före utgången av löptiden. Du vinner om priset stiger, förlusten begränsas till premien om priset faller.





- Säljoption (bearish bet)**: Du satsar på att Bitcoin kommer att falla under lösenpriset. Du vinner om priset faller, förlusten är begränsad till premien om priset stiger.





- Straddle (volatilitetsspel)**: Du köper en Call OCH en Put samtidigt. Du vinner om Bitcoin gör en stor rörelse i någon riktning, du förlorar båda premierna om priset förblir stabilt.



Begränsning: 50 samtidiga positioner. Perfekt för att börja handla med hävstång utan rädsla för likvidation.



**sats ↔ sUSD**: Omedelbart konvertera dina satoshis till syntetiska dollar (sUSD) för att skydda dig mot volatilitet, eller vice versa för att återfå Bitcoin-exponering.



## Tillgång till plattform och skapande av konto



### Gå till LN Markets



Gå till [lnmarkets.com] (https://lnmarkets.com) och klicka på "Open App".



![Page d'accueil LN Markets](assets/fr/01.webp)



### Skapa ditt konto



Välkomstskärmen erbjuder flera anslutningsmetoder:



![Méthodes de connexion](assets/fr/02.webp)



**Optioner tillgängliga** :


1. **Registrera med en Lightning wallet** (rekommenderas) : LNURL-auth med Phoenix, Breez, Zeus eller BlueWallet


2. **Registrera med e-post**: klassiskt konto (begränsar Lightning-upplevelsen)


3. **Alby** eller **Ledger**: webbläsartillägg



### Anslutning via Lightning (LNURL-auth)



Klicka på "Registrera dig med en Lightning wallet". Skanna QR-koden med din wallet Lightning :



![QR code LNURL-auth](assets/fr/03.webp)



Din wallet signerar automatiskt en kryptografisk begäran och ditt konto skapas direkt, utan e-post eller lösenord. Stark säkerhet och total anonymitet.



### Inledande konfiguration



![Configuration post-connexion](assets/fr/04.webp)



**Tillgängliga parametrar** :




- Användarnamn**: anpassa ditt användarnamn
- Automatiska uttag**: aktivera automatiska uttag till din wallet efter handelsstängning
- Tvåfaktorsautentisering**: förbättrad säkerhet med 2FA
- Dokumentation**: tillgång till officiella resurser



## Interface turné



LN Markets-gränssnittet är organiserat i flera sektioner som nås från sidomenyn:



### Instrumentpanel



![Dashboard](assets/fr/06.webp)



Visar dina resultat per produkttyp (Futures Cross, Futures Isolated, Options) med P&L, handlade volymer och din personliga Address Lightning (t.ex. `pivi@lnmarkets.com`).



### Profil



![Profil trader](assets/fr/07.webp)



Detaljerad statistik: antal avslut, typ av handlare (SCALPER etc.), medianpositionens varaktighet, uppdelning Long/Short, vinstprocent, medelvärden (kvantitet, marginal, hävstång) och progressiv avgiftsstruktur enligt volym.



### Handel



![Historique des trades](assets/fr/08.webp)



På fliken Trades visas en fullständig historik över dina positioner, med alla viktiga uppgifter: skapandedatum, riktning (Long/Short), positionsstorlek (kvantitet), bekräftad marginal, in- och utgångspris, realiserad vinst/förlust (P&L) och handelsavgifter. Du kan filtrera efter produkttyp (terminer/optioner) och exportera dina data för extern analys eller redovisning.



### Inställningar



![Paramètres de la plateforme](assets/fr/05.webp)



Fliken Inställningar har två flikar: **Konto** och **Interface**.



*fliken *Konto**:



Kontohantering med redigerbara fält :




- Användarnamn**: ändra ditt användarnamn (t.ex. "pivi") med knappen "Uppdatera"
- E-post**: lägg till/ändra din e-postadress
- Deposit bitcoin address**: den bitcoin-adress du kan använda för att sätta in on-chain-medel.



**Tre konfigurationsknappar** :




- Visas i topplistor**: välj om du vill visas i offentliga topplistor eller inte
- Använd Taproot-adresser**: använd Bitcoin-adresser Taproot för on-chain-insättningar/uttag
- Aktivera automatiska uttag**: aktivera automatiska uttag till din wallet Lightning efter handelsstängning



**Migrering av konto**: Avsnitt som gör det möjligt att migrera ditt Lightning-konto till klassisk autentisering med e-post/lösenord.



**Session hantering**: knappen "Rensa session och lokala data" för att koppla bort och rensa lokala webbläsardata.



**Interface** flik:



Anpassa användarupplevelsen med sju reglage:




- Hoppa över orderbekräftelse**: inaktivera bekräftelsemodal före handelsutförande (snabb handel)
- Visa verktygstips**: visa verktygstips när du håller muspekaren över element
- Privat läge (maskerar känsliga uppgifter)**: maskerar belopp och känsliga uppgifter i gränssnittet (privat läge)
- Show net PL in profile**: visa nettovinsten/förlusten i din offentliga profil
- Använda enhetsikoner**: visa ikoner för valutaenheter (sats, $)
- Aktivera ljudaviseringar**: aktivera ljudaviseringar för handelshändelser
- Enable desktop notifications**: aktivera skrivbordsaviseringar för operativsystemet



### Wallet



![Wallet](assets/fr/09.webp)



Bitcoin och syntetiska USD-saldon med historik över insättningar, uttag, korsvisa överföringar, swappar, finansiering och on chain adresshantering.



### API



![API V3](assets/fr/10.webp)



LN Markets erbjuder en komplett API REST (V2 och V3) för att helt automatisera din handel via skript eller bots. Du kan skapa API-nycklar med anpassningsbara behörigheter (skrivskyddad, handel, uttag) direkt från gränssnittet. Officiella SDK:er för TypeScript och Python finns tillgängliga för enkel integration. Fullständig API V3-dokumentation finns tillgänglig på [api.lnmarkets.com/v3] (https://api.lnmarkets.com/v3).



## Första insättningen av medel



Klicka på "Insättning". Tre metoder finns tillgängliga:



![Modal de dépôt](assets/fr/11.webp)



1. **LNURL**: skanna QR-koden med din wallet Lightning


2. **Invoice**: ange ett belopp och skanna sedan blixtfakturan


3. **On-Chain**: depå Bitcoin on chain



## Handel i praktiken



### Handla Futures Long: satsa på uppsidan



Från instrumentpanelen klickar du på "Futures" och sedan "Isolated". Klicka på **"Buy"** för att öppna en Long-position.



![Interface Futures Long](assets/fr/12.webp)



Klicka på ikonen **kalkylator** bredvid knappen "Köp" för att visa positionskalkylatorn:



![Calculateur de position Long](assets/fr/13.webp)



**Konkret exempel** :




- Kvantitet**: $100 (positionsstorlek)
- Handelsmarginal**: 12.336 sats (fastställd marginal)
- Hävstångseffekt **: 7.73 × (varje 1% BTC-variation = 7,73% på ditt kapital)
- Ingångspris** : $104,863.5
- Avveckling**: $92,852 (kritiskt automatiskt likvidationspris)
- Utgångspris**: 110 000 USD (för vinstberäkning)
- PL** : 4.492 sats (vinst om exit vid 110.000 dollar)



**Scenarier** :




- Ökning +4,9%** (110.000 dollar) : +4.492 sats vinst (+36,4%)
- Neutral** (104 863 USD) : -185 sats (endast avgifter)
- Ned -11,5%** (92 852 USD): total likvidation (-100%)



Klicka på knappen "Köp" för att bekräfta affären. **Två möjliga fall** :





- Om du har tillräckligt med likviditet** på ditt konto: en bekräftelsemodal visas direkt (bilden nedan). Klicka på "Ja" för att genomföra affären direkt.



![Confirmation trade Long](assets/fr/14.webp)





- Om du inte har tillräckligt med kontanter**: en Lightning QR-kod visas istället. Skanna den med din wallet Lightning för att betala den nödvändiga marginalen. Handeln öppnas automatiskt när betalningen har mottagits



### Korta terminskontrakt: satsa på nedsidan



Klicka på **"Sell"** för att öppna en kort position (du vinner om priset faller). Öppna kalkylatorn med kalkylatorikonen för att ställa in din position:



![Calculateur de position Short](assets/fr/15.webp)



Klicka på "Sälj" för att bekräfta. När det gäller Long, **två möjliga fall**:





- Om du har tillräckligt med kontanter**: direkt bekräftelse, klicka på "Ja"
- Om du inte har tillräckligt med kontanter**: en Lightning QR-kod visas (bilden nedan). Skanna den med din wallet Lightning för att betala den begärda marginalen:



![Paiement Lightning pour Short](assets/fr/16.webp)



När Lightning-betalningen har tagits emot öppnas din Short-position automatiskt. Du kan sedan hantera den från handelsgränssnittet.



#### Stänga en position



För att stänga din position (lång eller kort) klickar du på **det lilla krysset i det nedre högra hörnet** i administrationsgränssnittet:



![Interface de clôture](assets/fr/17.webp)



En bekräftelsedialog visas för att bekräfta avslutet av affären:



![Confirmation clôture](assets/fr/18.webp)



Modalrutan visar din aktuella P&L (vinst eller förlust). Klicka på "Ja" för att stänga. Saldot läggs omedelbart till (vinst) eller dras av (förlust) från din Wallet via Lightning.



### Handel med optioner Call: villkorad rätt att köpa



Optioner erbjuder **risk begränsad** till den betalda premien, utan möjlighet till likvidation. En Call ger dig rätten (inte skyldigheten) att köpa Bitcoin till lösenpriset före utgången av löptiden. Till skillnad från terminer kan du aldrig förlora mer än den investerade premien.



Klicka på "Alternativ" i instrumentpanelen och välj sedan fliken "Samtal".



![Interface Options Call](assets/fr/19.webp)



Konfigurera din handel med följande parametrar:




- Kvantitet**: $100 (storleken på ditt kontrakt)
- Utgångsdatum** : 2025-11-15 (utgångsdatum)
- Strike**: 96 000 dollar (riktkurs)



De övriga fälten beräknas automatiskt:




- Marginal**: 1.045 sats (premie betalas, din investering)
- Breakeven**: 96 923 USD (pris för att återfå din insats)
- Delta**: 40 (priskänslighet för Bitcoin)



**Hur beräknar du din vinst?



Din vinst beror på Bitcoin-priset vid utgången. Formel för detta: **(BTC-pris - Strike) × Contract-storlek - Betald premie**.



**Konkreta exempel** :





- Bitcoin till 96 000 USD** (aktuellt pris) : Inneboende värde = $0. **Förlust: -1,045 sats** (du förlorar premien)





- Bitcoin till 97 000 dollar**: Inneboende värde = (97 000 - 96 000) × 0,00105 BTC = 1,05 USD. Omvandlat till sats ≈ 2 175 sats. **Vinst: 2,175 - 1,045 = +1,130 sats** (+108 % vinst)





- Bitcoin till 98 000 USD**: inneboende värde = 2 000 USD ≈ 3 224 sats. **Vinst: +2 179 sats** (+208% vinst)





- Bitcoin till 100 000 USD**: inneboende värde = 4 000 USD ≈ 5 263 sats. **Vinst: +4 218 sats** (+403% vinst)





- Bitcoin under 96 000 dollar**: Optionen förfaller värdelös. **Begränsad förlust: -1 045 sats**, ingen avveckling möjlig



Klicka på "Köpa Call". En dialogruta för bekräftelse visas:



![Confirmation Call option](assets/fr/20.webp)



Klicka på "Buy Call" igen för att bekräfta. Optionen visas i "Löpande optioner". Vid förfallodagen beräknar LN Markets automatiskt det inneboende värdet och justerar din vinst/förlust.



**Notering om säljoptioner** : Operationen är identisk med den för ett samtal, men i omvänd ordning. Med en Put satsar du på att Bitcoin-priset ska **ned**. Om Bitcoin faller under din strike vinner du; om det stannar över förlorar du bara den betalda premien. Beräkningen av vinster följer samma logik: **(Strike - BTC-pris) × Contract-storlek - Betald premie**.



### Uttag av blixtfond



Klicka på "Uttag":



![Modal de retrait](assets/fr/21.webp)



**Metoder** : LNURL, Invoice, Blixten Address, On-Chain.



**Invoice förfarande** :


1. Skapa en Lightning-faktura från din wallet


2. Kopiera fakturan (börjar med `lnbc...`)


3. Klistra in den i LN Markets-fältet


4. Bekräfta uttag


5. Din wallet krediteras inom 1-3 sekunder



Inga avgifter för blixtuttag, endast minimala routningskostnader (<0,1% i praktiken).



## Risker och bästa praxis



**Huvudrisker** :




- Total likvidation**: hög hävstångseffekt kan utplåna 100 % av marginalen på några minuter
- Experimentell tjänst**: alfafas, tekniska osäkerheter
- Motpartsrisk**: plattformen förblir en enda motpart



**Bästa praxis** :



1. **Kapitalhantering**: anta en riskhanteringsstrategi som är skräddarsydd för din profil. Till exempel: avsätt 5 % av dina totala tillgångar till hävstångshandel och riskera sedan högst 1 % av detta kapital per handel (t.ex.: 1 BTC-tillgång → 5M sats att handla → 50k sats maxrisk per position)



2. **Systematisk stop-loss**: Konfigurera stop-loss för att begränsa dina förluster per handel. Med en riskregel på 1 %, till exempel, utgör även 10 förlustaffärer i följd endast 10 % av ditt handelskapital



3. **Starta i liten skala**: testa först med några tusen satss för att förstå mekanismerna innan du tillämpar din kapitalförvaltningsstrategi



4. **Ta ut dina vinster regelbundet**: säkra dina vinster på din huvudsakliga wallet och lämna endast aktivt handelskapital på plattformen



5. **Se upp för hävstångseffekten**: undvik hävstångseffekt >20× om du inte är fullt medveten om likvidationsriskerna



** Kostnader **: inga avgifter för blixtinsättning / uttag, spridning ~ 0,1% per handel (sjunker till 0,06% beroende på volym).



## Fördelar och begränsningar



**Fördelar** :




- Icke-förvaltande (total kontroll exklusive handelsperioder)
- KYC-fri (anonymitet via Lightning/Nostr)
- Omedelbar avveckling (insättningar/uttag på några sekunder)
- Exekvering utan slippage med likviditetsaggregering
- API allmänhet och Nostr support



**Begränsningar** :




- Tjänsten alfa (möjliga utvecklingar)
- Lägre likviditet än Binance/Deribit
- Förbjudet för personer bosatta i USA



## Slutsats



LN Markets innebär en stor utveckling av Bitcoin-handeln genom att integrera Lightning Network för att ge tillbaka kontrollen till användarna. För smarta bitcoiners som vill spekulera utan att kompromissa med sin suveränitet är det ett unikt alternativ till traditionella centraliserade börser.



Plattformen fortsätter att utvecklas med USDT linjära terminer och handel utan förvar via Discreet Log Contracts (DLC) under utveckling. Genom att tillämpa god riskhanteringspraxis (små belopp, stop-loss, regelbundna uttag) blir LN Markets ett kraftfullt verktyg för att utforska Bitcoin-hävstång på ett ansvarsfullt sätt.



Börja i liten skala, testa med några tusen satss och utforska gradvis denna nya Lightning Network-gräns. Trevlig suverän handel ⚡️!



## Resurser





- [LN Markets:s officiella webbplats] (https://lnmarkets.com)
- [Dokumentation] (https://docs.lnmarkets.com)