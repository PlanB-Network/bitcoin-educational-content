---
name: Arvsplan Bitcoin
description: Så här överför du bitcoins till dina nära och kära
---

![cover](assets/cover.webp)



Överföringen av bitcoins utgör en stor teknisk utmaning som många innehavare förbiser. Till skillnad från traditionella banktillgångar, där ett finansinstitut kan överföra medlen till de rättmätiga ägarna, fungerar Bitcoin utan mellanhänder. Dina nära och kära kommer aldrig att kunna få tillgång till dina medel utan nödvändig teknisk information, oavsett deras juridiska legitimitet.



Denna handledning guidar dig genom skapandet av en teknisk arvsplan. Du får lära dig hur on-chain-mekanismerna för automatiserad överföring fungerar, hur du dokumenterar dina konfigurationer och hur du väljer rätt lösningar för att säkerställa att ditt Bitcoin-arv förblir tillgängligt för dina nära och kära.



## Varför en plan för det tekniska kulturarvet är nödvändig



Bitcoin bygger på en grundläggande kryptografisk princip: den som innehar de privata nycklarna kontrollerar medlen. Denna suveränitet blir en stor sårbarhet när innehavaren försvinner utan att ha överfört nödvändig information.



En Bitcoin-arvsplan måste uppfylla två till synes motsägelsefulla mål: att låta dina nära och kära få tillgång till dina medel när tiden är inne, samtidigt som du förhindrar att någon annan får tillgång till dem i förtid. Denna känsliga balans förlitar sig på Bitcoin:s inbyggda programmeringsfunktioner.



Teknisk komplexitet lägger till ett extra lager av svårigheter. Dina arvingar kommer att behöva manipulera begrepp som återhämtningsfraser, portföljdeskriptorer eller härledningsvägar. Utan tillräckliga förberedelser riskerar även en välmenande arvinge att göra oåterkalleliga misstag.



## Hur on-chain-arvet fungerar



Bitcoin använder sitt skriptspråk för att koda utgiftsvillkor direkt i transaktioner. on-chain-arvet utnyttjar denna programmerbarhet för att skapa alternativa återhämtningsvägar som aktiveras automatiskt.



### Tidlås



Timelocks är den grundläggande mekanismen för Bitcoin-arv. De gör det möjligt att låsa fonder tills ett tidsvillkor är uppfyllt.



**CLTV (CheckLockTimeVerify)**: Denna absoluta tidsspärr kontrollerar att en viss tid (datum eller blockhöjd) har uppnåtts innan utgiften godkänns. Till exempel "dessa medel kan endast användas efter block 900000" eller "efter den 1 januari 2026". Fördelen med CLTV är att det tillåter långa fördröjningar (flera år), men datumet är fast och gäller identiskt för alla UTXO:er i portföljen. För att behålla kontrollen över dina medel måste du med jämna mellanrum skapa en ny portfölj med ett förlängt utgångsdatum och överföra dina medel till den.



**CSV (CheckSequenceVerify)**: Denna relativa tidslåsning verifierar att ett visst antal block har förflutit sedan UTXO skapades. Till exempel, "dessa medel kan endast spenderas 52560 block (~1 år) efter mottagandet". Fördelen med CSV är att varje UTXO har sin egen oberoende räknare. Varje gång du utför en transaktion återställer de nyskapade UTXO:erna sin egen tidsgräns. Den tekniska gränsen på 65535 block (~15 månader maximalt) begränsar dock de möjliga tidsramarna. Detta tillvägagångssätt är mer naturligt för daglig användning, eftersom din normala aktivitet automatiskt skjuter upp tidsfristerna.



### Flera utgiftsvägar



En arvsportfölj kombinerar flera utgiftsvägar i varje adress:





- Huvudväg** : Ägaren kan när som helst spendera sina pengar med sin huvudnyckel, utan tidsbegränsningar.
- Återhämtningsväg(ar)**: En eller flera alternativa nycklar kan spendera medel först efter att en viss tid har förflutit.



Varje transaktion som utförs av ägaren "uppdaterar" UTXO och skapar nya utgångar med återställda tidslås. Den här mekanismen säkerställer att återställningsvägarna aldrig aktiveras så länge ägaren är aktiv.



### Miniscript och Taproot



**Miniscript** är ett strukturerat språk som utvecklats av Andrew Poelstra, Pieter Wuille och Sanket Kanjalkar och som gör det enkelt att skriva och analysera komplexa Bitcoin-skript. Det gör att du kan komponera läsbara och verifierbara utgiftsvillkor, vilket är viktigt för arvskonfigurationer som involverar flera nycklar och tidslås.



**Taproot** (aktiverad i november 2021) förbättrar on-chain-arvet avsevärt. Tack vare dess trädstruktur (MAST) avslöjas endast det utgiftsvillkor som används på blockkedjan. Om ägaren spenderar sina medel normalt förblir arvsvillkoren osynliga. Denna sekretess minskar också transaktionskostnaderna för komplexa vägar.



## Den avgörande betydelsen av deskriptorer



För äldre portföljer räcker inte återvinningsfrasen (seed) för att återställa tillgången till medel. **Deskriptorn** blir det kritiska elementet.



En deskriptor är en sträng som uttömmande beskriver en portföljs struktur: de offentliga nycklar som är inblandade, utgiftsvillkor, härledningsvägar och konfigurerade tidslås. Här är ett förenklat exempel:



```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```



Denna deskriptor säger: "antingen kan huvudnyckeln användas omedelbart, eller så kan återställningsnyckeln användas efter 52560 block".



Låt oss analysera det här exemplet:




- `wsh()` : Witness Script Hash, anger adresstyp (P2WSH)
- or_d()`: "eller"-villkor med en standardgren
- pk([fingeravtryck/väg]xpub...)`: Den publika huvudnyckeln med dess fingeravtryck och härledningsväg
- och_v()`: "och"-villkor som kombinerar återställningsnyckel med tidslås
- `äldre(52560)`: Den relativa tidslåsningen av 52560 block



**Utan descriptorn, även med alla återställningsfraser, kommer dina arvingar inte att kunna återuppbygga portföljen.** En standardportfölj kan endast återställas från seed eftersom den följer standardiserade härledningsvägar (BIP44, BIP84). En äldre portfölj, å andra sidan, använder anpassade skript som inte kan gissas. Säkerhetskopian av deskriptorn (eller konfigurationsfilen som exporteras av din programvara) måste följa med återställningsfraserna i din arvsplan.



## Dokumentära komponenter i en arvsplan



Utöver de tekniska mekanismerna vilar en effektiv legacy-plan på tre pelare av dokumentation.



### Arvsbrevet



Detta personliga brev är startpunkten för din plan. Det är skrivet för dina arvingar och förklarar sammanhanget och de försiktighetsåtgärder som ska vidtas.



Ditt brev måste innehålla tydliga säkerhetsregler:




- Ha inte bråttom, ta tid på dig att lära dig innan du flyttar pengar
- Kommunicera aldrig en fullständig återställningsfras till en enda person
- Ange aldrig en återställningsfras i ett okontrollerat program eller en dator
- Akta dig för bedrägerier och personer som erbjuder oönskad hjälp
- Rådfråga minst två personer som du litar på innan du fattar något beslut



Detta brev innehåller också din notaries kontaktuppgifter och platsen för ditt testamente. Det ska aldrig innehålla återställningsfraser eller lösenord.



### En katalog över betrodda kontakter



Ingen arvinge bör möta bitcoinåtervinning ensam. I den här katalogen finns en lista över personer som kan ge teknisk eller juridisk hjälp.



Dokumentera för varje kontakt: fullständigt namn, relation till dig, roll i planen, förtroendenivå, Bitcoin-kompetens och fullständiga kontaktuppgifter. Grundregeln: dina arvingar bör alltid rådfråga minst två olika personer innan de fattar ett viktigt beslut.



### Bitcoin inventering av tillgångar



I det här avsnittet kartläggs alla dina bitcoins med den tekniska information som behövs för att återvinna dem.



För varje portfölj, dokument :




- Portföljtyp**: hårdvara, mjukvara, konfiguration (single-sig, multisig, legacy)
- Enhetens plats**: fysisk plats för wallet-hårdvaran
- Descriptor/konfigurationsfilens plats**: kritisk för avancerade portföljer
- Återvinningsfrasens placering**: separat från deskriptorn
- Åtkomstkoder**: där PIN-koder och lösenfraser lagras
- Konfigurerade fördröjningar**: när återhämtningsvägarna aktiveras



## Tekniska lösningar tillgängliga



Flera programvarupaket implementerar on-chain:s arvsmekanismer. Varje paket har sina egna tekniska egenskaper.



### Liana



Liana är en skrivbordsprogramvara (Linux, macOS, Windows) som använder Miniscript för att skapa portföljer med tidsbestämda återhämtningsvägar. Projektet utvecklas av Wizardsardine, som grundades av Antoine Poinsot (Bitcoin Core contributor).



**Teknisk arkitektur**: Liana skapar P2WSH-portföljer (SegWit native) som standard, med Taproot-stöd tillgängligt beroende på kompatibiliteten hos din wallet-maskinvara. Arkitekturen är baserad på en huvudväg och en eller flera återställningsvägar. Den genererade deskriptorn kodar alla villkor och måste sparas.



**Timelocks används**: Liana använder relativa tidslås (CSV), begränsade till 65535 block (~15 månader). För att behålla kontrollen måste du utföra en uppdateringstransaktion innan tidslåset löper ut.



**Hårdvara wallet integration**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY och andra enheter är kompatibla för signering av transaktioner.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper



Bitcoin Keeper är en mobilapplikation (iOS, Android) som kombinerar multisig och tidslås via sina "Enhanced Vaults". Det mobila tillvägagångssättet med integrerad vägledning gör den tillgänglig för mindre tekniska användare.



**Teknisk arkitektur**: Enhanced Vaults använder Miniscript för att skapa multisig-konfigurationer där ytterligare nycklar aktiveras efter definierade fördröjningar. Inheritance-nyckeln lägger till det befintliga kvorumet, medan Emergency-nyckeln kan kringgå multisig helt.



**Timelocks används**: Bitcoin Keeper använder absoluta tidslås (CLTV), vilket möjliggör ledtider på över 15 månader. Aktiveringsdatumet ställs in vid skapandet av wallet och gäller för alla UTXO:er. Applikationen innehåller en "revaulting"-funktion som automatiskt hanterar uppdateringen: användaren följer helt enkelt de guidade stegen utan att manuellt behöva skapa en ny wallet.



**Ytterligare funktioner**: Integrerade arvsdokument, Canary Wallets för att upptäcka nyckelkompromisser och påminnelser om uppdatering.



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Kulturarv



Heritage är en skrivbordsapplikation som använder Taproot-skript för att koda arvsvillkor. Användningen av Taproot ger ökad konfidentialitet, eftersom oanvända sökvägar förblir osynliga i blockkedjan.



**Teknisk arkitektur**: Varje Heritage-adress innehåller en huvudväg och alternativa vägar för varje arvtagare, med progressiva tidsramar. Den hierarkiska strukturen gör det möjligt att definiera en personlig backup på 6 månader och familjearvingar på 12-15 månader.



**Användningsmöjligheter**: Fristående version med din egen nod (gratis) eller hanterad tjänst som lägger till påminnelser och meddelanden till arvingar (0,05%/år).



https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## Arvtagarens återhämtningsprocess



Att förstå återhämtningsprocessen hjälper till att förbereda en effektiv plan. Här är de tekniska steg som en arvinge måste följa.



### Krav på återvinning



Arvtagaren behöver :


1. **Deskriptor- eller konfigurationsfilen** för den ursprungliga portföljen (JSON- eller textformat, beroende på programvaran)


2. **Its recovery phrase** (den som är associerad med dess inheritance key, vanligtvis 12 eller 24 ord)


3. **Kompatibel programvara** (Liana, Bitcoin Keeper, Heritage eller Sparrow/Specter för standarddeskriptorer)


4. **En anslutning till en Bitcoin**-nod för att kontrollera status för tidslås och sända transaktionen



### Steg för återhämtning



1. **Installera programvaran** på en säker enhet och konfigurera anslutningen till Bitcoin-nätverket (personlig nod eller Electrum-server)


2. **Importera deskriptorn** för att rekonstruera portföljstrukturen. Programvaran kommer automatiskt att generate alla adresser som används


3. **Restore inheritance key** från återställningsfras. Programvaran kontrollerar att denna nyckel motsvarar en av de nycklar som är auktoriserade i deskriptorn


4. **Synkronisera portföljen** för att upptäcka alla UTXO:er och deras utgiftsvillkor


5. **Check timelock expiration**: programvaran kommer att ange för varje UTXO om återställningsvägen är aktiv


6. **Skapa återvinningstransaktionen** till en adress som endast kontrolleras av arvtagaren (helst en ny enskild wallet)


7. **Signera och sända** transaktionen på Bitcoin-nätverket



Om tidslåset ännu inte har löpt ut måste arvtagaren vänta. Programvaran visar det datum eller block från vilket återhämtning blir möjlig. Under denna väntetid förblir medlen säkra på blockkedjan.



### Poäng att hålla koll på för arvtagaren



Arvtagaren måste ägna särskild uppmärksamhet åt :




- Kontrollera äktheten hos nedladdad programvara** (kontrollsummor, signaturer)
- Dela aldrig med dig av din återhämtningsfras** till någon som erbjuder hjälp
- Rådgör med minst två personer som du litar på** innan du utför återställningen
- Överföra pengarna till en enkel portfölj** som han kontrollerar helt efter återhämtningen



## Bästa praxis



### Separering av information



Förvara aldrig all information på samma ställe. Deskriptorn måste vara åtskild från återställningsfraserna, som i sin tur är åtskilda från PIN-koderna. Denna fördelning gör det svårare för en angripare att komma åt informationen, samtidigt som den kan återskapas av dina legitima arvingar.



### Återhämtningstest



Innan du sätter in betydande medel, testa hela återställningsprocessen med en liten mängd. Verifiera att du kan återställa portföljen från beskrivnings- och återställningsfraserna på en tom enhet. Dokumentera stegen för dina arvingar.



### Underhåll av tidslås



Planera att uppdatera dina tidslås i god tid innan de löper ut. För ett tidslås på 12 månader ska du utföra en transaktion var 9:e-10:e månad. Programvaran erbjuder vanligtvis påminnelser eller automatiska uppdateringsfunktioner.



### Uppdatering av planen



Din Bitcoin-konfiguration utvecklas. Varje betydande förändring (ny portfölj, ändring av tidsfrister, tillägg av arvtagare) måste återspeglas i din dokumentation. Upprätta en årlig granskningsrutin.



## Att välja tillvägagångssätt



Valet mellan de olika lösningarna beror på din tekniska profil och dina specifika behov.



**Liana** är lämplig för stationära användare som föredrar programvara med öppen källkod och full kontroll via sin egen nod. Konfigurationen förblir tillgänglig tack vare det guidade gränssnittet. Relativa tidslås (CSV) förenklar underhållet, eftersom din normala aktivitet automatiskt skjuter upp deadlines. Begränsning: maximal fördröjning på ca 15 månader (65535 block).



**Bitcoin Keeper** riktar sig till mobila användare som vill ha ett intuitivt gränssnitt med integrerade dokument. Applikationen erbjuder två typer av specialnycklar: Inheritance Key (som ökar kvorumet) och Emergency Key (som helt kringgår det). Absoluta tidslås (CLTV) medger ledtider på över 15 månader, med en integrerad revaulting-funktion som förenklar uppdatering. Planen Diamond Hands låser upp avancerade äldre funktioner.



**Inheritance** vänder sig till tekniska användare som uppskattar Taproot-konfidentialitet och hierarkiskt arv med progressiva fördröjningar. Taproot:s trädstruktur döljer arvsvillkor under normala transaktioner och avslöjar endast det villkor som används vid återställning.



Alla tre lösningarna har en sak gemensamt: de kräver periodisk uppdatering för att förhindra för tidig aktivering av återställningsvägar. Denna begränsning är både priset och garantin för on-chain:s opålitliga arv. Schemalägg regelbundna påminnelser och gör detta underhåll till en del av din Bitcoin-hanteringsrutin.



## Slutsats



En teknisk Bitcoin-arvsplan kombinerar kryptografiska mekanismer (tidslås, Miniscript, Taproot) med rigorös dokumentation. Avancerade plånböcker gör att du kan överföra dina bitcoins automatiskt efter en period av inaktivitet, utan ingripande från tredje part.



De viktigaste delarna att lämna över till dina arvingar är: beskrivnings- eller konfigurationsfilen, deras återställningsfras, detaljerade återställningsinstruktioner och kontaktuppgifter till kompetenta personer som kan hjälpa dem.



Börja med att välja en teknisk lösning som passar din profil, testa den med en liten mängd och dokumentera sedan helheten i en strukturerad plan. Den inledande komplexiteten garanterar att dina Bitcoin-tillgångar kommer att föras vidare med fullt förtroende.



## Resurser



### Mall för arvsplan





- [Bitcoin Mall för arvsplan (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Plan ₿ Network Dokumentationsmall



### Tekniska referenser





- [BIP-65 : OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Specifikation av absoluta tidsur (CLTV)
- [BIP-112 : OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Specifikation av relativa tidslås (CSV)
- [Miniscript-referens](https://bitcoin.sipa.be/miniscript/) - Officiell Miniscript-dokumentation av Pieter Wuille



### Officiella webbplatser för lösningar





- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper] (https://bitcoinkeeper.app/) - Bithyve
- [Heritage Wallet](https://btc-heritage.com/) - Crypto7