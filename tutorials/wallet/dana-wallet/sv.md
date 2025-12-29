---
name: Dana Wallet
description: Minimalistisk portfölj för Silent Payments (BIP-352)
---

![cover](assets/cover.webp)



Återanvändning av Bitcoin-adresser är ett av de mest direkta hoten mot användarnas konfidentialitet. När en mottagare delar en enda adress för att ta emot flera betalningar kan alla observatörer spåra alla associerade transaktioner och rekonstruera deras ekonomiska historia. Detta problem påverkar särskilt innehållsskapare, välgörenhetsorganisationer eller aktivister som vill visa en donationsadress offentligt utan att äventyra sin egen eller sina donatorers integritet.



Dana Wallet svarar på detta problem med en elegant lösning: Tysta betalningar. Denna minimalistiska wallet med öppen källkod, som lanserades 2024, genererar en återanvändbar statisk adress samtidigt som den garanterar att varje mottagen betalning hamnar på en separat adress i blockkedjan. Avsändaren behöver ingen tidigare interaktion med mottagaren, och ingen extern observatör kan länka samman enskilda transaktioner. På blockkedjan ser dessa betalningar ut som helt vanliga Taproot-transaktioner.



Dana Wallet är tillgänglig på Mainnet och Signet, men utvecklarna anser fortfarande att det är experimentellt och rekommenderar att du inte sätter in pengar som du inte är beredd att förlora. I den här handledningen använder vi Signet-versionen för att upptäcka Silent Payments utan att riskera några riktiga medel.



## Vad är Dana Wallet?



### Filosofi och mål



Dana Wallet använder en "SP-first"-strategi: wallet genererar endast Silent Payments-adresser och accepterar endast denna typ av betalning. Du kommer inte att kunna skapa en klassisk Bitcoin-adress (äldre, SegWit- eller Taproot-standard) med den här applikationen. Denna avsiktliga begränsning gör att du kan koncentrera dig helt på att lära dig BIP-352-protokollet utan att distraheras av andra funktioner. Det överskådliga gränssnittet är medvetet utformat så att det är lättare att använda än att ha en mängd olika alternativ, vilket gör verktyget tillgängligt även för användare som är nya inom on-chain-konfidentialitet.



Projektet är helt open source och har utvecklats med Flutter för mobilgränssnittet och Rust för den interna kryptografiska logiken. Denna arkitektur kombinerar en smidig användarupplevelse med optimal prestanda för intensiva skanningsoperationer.



### Hur fungerar tysta betalningar?



Tysta betalningar (BIP-352) baseras på en sofistikerad kryptografisk mekanism som använder Elliptic Curve Diffie-Hellman Key Exchange (ECDH). Mottagaren genererar en statisk adress (som börjar med `sp1...` på mainnet eller `tsp1...` på Signet) som består av två olika publika nycklar: en skanningnyckel ($B_{scan}$) för att upptäcka inkommande betalningar och en utgiftsnyckel ($B_{spend}$) för att spendera mottagna medel. Denna separation gör det möjligt att behålla utgiftsnyckeln på wallet-hårdvaran medan skanningnyckeln används på en ansluten enhet.



När en avsändare vill göra en betalning kombinerar hans wallet summan av sina inmatningars privata nycklar med mottagarens offentliga skanningnyckel för att beräkna en delad ECDH-hemlighet. Denna hemlighet genererar en kryptografisk "tweak" som, adderad till mottagarens utgiftsnyckel, skapar en unik Taproot-adress för den transaktionen.



Mottagaren kan reproducera denna beräkning med hjälp av sin privata skanningnyckel och de publika nycklar som är synliga i transaktionen (Diffie-Hellman matematisk egenskap). Detta gör det möjligt för honom att upptäcka och spendera pengarna utan någon föregående interaktion med avsändaren.



Detta tillvägagångssätt erbjuder flera fördelar:




- Mottagarsekretess**: varje betalning hamnar på en annan adress
- Sekretess för avsändaren**: ingen beständig identifierare som kopplar samman betalningar
- Ingen server från tredje part**: protokollet fungerar självständigt
- Transaktioner som inte kan särskiljas**: Tysta betalningar ser ut som vanliga Taproot-transaktioner



Den största nackdelen är kostnaden för skanning: mottagaren måste analysera varje ny Taproot-transaktion för att upptäcka de som är avsedda för honom.



Om du vill lära dig mer om den tekniska driften av Silent Payments rekommenderar vi BTC204-kursen om sekretess i Bitcoin, som innehåller ett kapitel tillägnad Silent Payments:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Plattformar som stöds



Dana Wallet är tillgänglig som en Android-applikation. APK:en kan laddas ner via det dedikerade F-Droid-arkivet som tillhandahålls av utvecklarna, via Obtainium eller direkt från GitHub. För Linux-användare är det tekniskt möjligt att kompilera Flutter-applikationen för skrivbordet.



Appen är inte tillgänglig på iOS eller via de officiella butikerna (Google Play, App Store), vilket återspeglar dess experimentella status och dess fokus på en teknisk publik.



## Installation



### Viktiga förutsättningar



För att installera Dana Wallet på Android behöver du en Android-enhet med alternativet "Okända källor" aktiverat i säkerhetsinställningarna. Inget konto eller registrering krävs.



### Lägg till F-Cold deposition



Den rekommenderade metoden är att lägga till Dana Wallet: s dedikerade F-Droid-förvar. Gå till `fdroid.silentpayments.dev` där du hittar förvarslänken och en QR-kod att skanna. Förvaret erbjuder för närvarande 3 applikationer: Mainnet-versionen, Development och Signet.



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### Installation via F-Droid



Öppna F-Droid-applikationen på din Android-enhet och gå sedan till Inställningar via ikonen längst ner till höger. Välj "Repositories" för att hantera appkällor. Tryck på "+" -knappen för att lägga till ett nytt arkiv, skanna sedan QR-koden eller klistra in länken `https://fdroid.silentpayments.dev/fdroid/repo`. När källan har lagts till ser du de tre versionerna av Dana Wallet som finns tillgängliga. Välj "Dana Wallet - Bookmark" och tryck på "Installera".



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## Inledande konfiguration



### Skapande av portfölj



Vid den första lanseringen visar Dana Wallet en välkomstskärm som presenterar dess uppdrag: "Skicka och ta emot donationer utan mellanhänder". Tryck på "Börja" för att fortsätta. På nästa skärm presenteras applikationens tre viktigaste fördelar:




- Smidiga donationer**: börja ta emot donationer på några sekunder
- Sekretess som standard**: inget behov av servrar eller komplex infrastruktur
- E-postliknande upplevelse**: skicka och ta emot bitcoins lika enkelt som ett e-postmeddelande



Du kan välja mellan "Restore" för att återställa en befintlig portfölj eller "Create new wallet" för att skapa en ny. Tryck på "Skapa ny wallet".



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



Programmet genererar sedan en återställningsfras, som du noggrant bör notera på ett fysiskt medium. Även för testfonder utan verkligt värde bör du använda dig av goda säkerhetskopieringsrutiner.



### Interface och parametrar



När portföljen har skapats kommer du till huvudgränssnittet, som är uppdelat i två flikar: "Transact" och "Settings".



Fliken **Transact** visar ditt bitcoinsaldo (och dess omvandling till dollar), en lista över senaste transaktioner och två åtgärdsknappar: "Pay" för att skicka pengar, och en mottagningsknapp (nedladdningsikon).



Fliken **Settings** erbjuder fyra alternativ:




- Visa seed-fras**: visar din återställningsfras för säker förvaring
- Ändra fiat-valuta**: ändra visningsvalutan (USD som standard)
- Set backend url**: konfigurera Blindbit-serverns URL (se nästa avsnitt)
- Wipe wallet**: raderar wallet helt och hållet från enheten



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### Blindbit-servern



Dana Wallet använder en indexeringsserver som heter **Blindbit** för att upptäcka dina Tysta betalningar. Att förstå hur det fungerar är viktigt för att utvärdera applikationens förtroendemodell.



**Varför behöver vi en server?



För att upptäcka en tyst betalning måste din wallet teoretiskt sett skanna alla Taproot-transaktioner i varje block och utföra en kryptografisk beräkning (ECDH) för var och en. På en mobiltelefon skulle denna operation vara alltför beräknings- och bandbreddsintensiv.



Blindbit-servern löser detta problem genom att förberäkna mellanliggande data (kallade "tweaks") för alla Taproot-transaktioner. Din wallet laddar sedan ner dessa tweaks (33 byte per transaktion) och utför den slutliga beräkningen **lokalt** för att kontrollera om en betalning tillhör dig.



**Bevarad sekretess**



Till skillnad från en vanlig Electrum-server där du avslöjar dina adresser, vet Blindbit-servern inte vilka betalningar som tillhör dig. Den tillhandahåller samma data till alla användare och det är din telefon som utför den slutliga verifieringen. Din konfidentialitet bevaras därför gentemot servern.



**Standardserver



Dana Wallet använder den publika servern `silentpayments.dev/blindbit/signet` (för Signet) eller `silentpayments.dev/blindbit/mainnet` (för Mainnet). Du kan ändra den här URL:en i inställningarna om du hostar din egen server.



**Hosta din egen Blindbit-server**



För användare som vill ha total suveränitet är det möjligt att vara värd för sin egen Blindbit Oracle-server. Detta kräver :




- En komplett Bitcoin Core-nod **inte utväxlad** (ej pruned)
- Installera Blindbit Oracle (finns på GitHub: `setavenger/blindbit-oracle`)
- Cirka 10 GB extra diskutrymme
- Tekniska färdigheter (Go-kompilering, serverkonfiguration)



Ingen paketerad applikation är ännu tillgänglig för Umbrel eller Start9. Installationen förblir manuell för tillfället. Detta är ett område i aktiv utveckling, och mer tillgängliga lösningar kan dyka upp i framtiden.



## Daglig användning



### Mottagande av medel



För att ta emot bitcoins, tryck på mottagningsknappen (nedladdningsikon) från huvudskärmen. Dana Wallet visar sedan din fullständiga Silent Payment-adress i formatet `tsp1q...` på Bookmark. Gränssnittet erbjuder flera alternativ:




- Visa QR-kod**: visar din adress QR-kod för enkel skanning
- Dela**: dela adressen via telefonens applikationer
- Copy**: kopierar adressen till urklipp



Som visas på skärmen kan du dela den här adressen offentligt på dina sociala nätverk utan att äventyra din integritet.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



För att få dina första testfonder på Signet, använd den dedikerade Silent Payments-kranen som är tillgänglig på `silentpayments.dev/faucet/signet`. Kopiera din adress `tsp1...`, klistra in den i fältet som finns på kranen och validera sedan begäran. Vänta på att ett block ska brytas (cirka 10 minuter på Signet).



### Skicka en betalning



För att skicka pengar, tryck på knappen "Pay" från huvudskärmen. Skärmen "Välj mottagare" visas med tre alternativ för att ange mottagaren:




- Ange betalningsinformation manuellt
- Klistra in från urklipp**: klistra in en adress från urklippet
- Skanna QR-kod**: skanna en QR-kod som innehåller adressen



När mottagarens adress har bekräftats kan du på skärmen "Ange belopp" ange det belopp som ska skickas i satoshis. Ditt tillgängliga saldo visas som referens. Tryck på "Fortsätt till val av avgift" för att fortsätta.



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



På nästa skärm visas tre avgiftsnivåer, beroende på hur brådskande ärendet är:




- Fast** (10-30 minuter): högre avgifter för snabb bekräftelse
- Normal** (30-60 minuter): måttliga kostnader
- Långsam** (1+ timme): lägsta avgift för icke-brådskande transaktioner



När du har valt avgiftsnivå sammanfattar bekräftelseskärmen "Redo att skicka?" alla detaljer: destinationsadress, belopp, beräknad tid och transaktionsavgift. Kontrollera informationen noggrant och tryck sedan på "Skicka" för att genomföra transaktionen.



När transaktionen har skickats visas den i din historik med statusen "Obekräftad" tills den ingår i en spärr. Ditt saldo uppdateras i enlighet med detta.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Fördelar och begränsningar



### Höjdpunkter





- Pedagogiskt**: förenklat gränssnitt med fokus på inlärning Tysta betalningar
- Dubbelriktad**: stöder både sändning och mottagning, till skillnad från andra portföljer
- Öppen källkod**: fullt granskningsbar kod på GitHub
- Dedikerad Faucet**: gör det lättare att få finansiering för tester
- Utan konto**: ingen registrering eller personuppgifter krävs



### Begränsningar att ta hänsyn till





- Experimental**: ej granskad programvara, använd med försiktighet på Mainnet
- Begränsad plattform**: huvudsakligen Android, ingen iOS-version
- Begränsad funktionalitet**: ingen myntkontroll, inga underkonton, ingen Lightning
- Intensiv skanning**: att upptäcka betalningar tar stora resurser i anspråk



## Bästa praxis



### seed säkerhet



Även för Signet-tester med värdelös bakgrund ska du behandla din återställningsfras seriöst. Använd alternativet "Visa seed-fras" i inställningarna för att skriva ner den noggrant. Som en fråga om god praxis, håll helt separata plånböcker för Signet och Mainnet: använd aldrig en seed skapad för testning på en wallet avsedd att ta emot riktiga medel.



### Varning om experimentell status



Dana Wallet betraktas fortfarande som experimentellt av sina utvecklare. Som de tydligt anger: "Använd inte medel som du inte är villig att förlora". För inlärningsändamål, välj Signet-versionen. Om du använder Mainnet-versionen ska du begränsa dig till token-belopp.



### Säkerhetskopiering och återställning



Återvinning av medel från tysta betalningar kräver en wallet som är kompatibel med BIP-352-protokollet. En standard wallet kan inte skanna blockkedjan för att hämta dina UTXO tysta betalningar. Behåll Dana Wallet installerad eller använd alternativet "Återställ" vid första lanseringen för att återställa en befintlig wallet.



## Jämförelse med BIP-47 och PayJoin



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Tysta betalningar eliminerar BIP-47-meddelandetransaktionen på bekostnad av en dyrare skanning. PayJoin löser ett annat problem (input correlation) och kan kombineras med Silent Payments.



## Slutsats



Dana Wallet är ett värdefullt utbildningsverktyg för att lära sig om tysta betalningar i en riskfri miljö. Dess minimalistiska tillvägagångssätt gör att du kan förstå de grundläggande mekanismerna i BIP-352-protokollet utan att bli distraherad av sekundära funktioner. Genom att experimentera med Signet kommer du att utveckla en praktisk förståelse för denna lovande teknik för Bitcoin-transaktioners konfidentialitet.



Tysta betalningar representerar ett betydande steg framåt för att förena användarvänlighet och respekt för integritet. Gemenskapens entusiasm och de första integrationerna i olika plånböcker (Cake Wallet, BitBox02, BlueWallet för sändning) pekar på en framtid där publicering av en donationsadress inte längre kommer att äventyra ägarens ekonomiska integritet.



## Resurser



### Officiell dokumentation




- Dana Wallet GitHub-arkiv: https://github.com/cygnet3/danawallet
- F-Cold deposition: https://fdroid.silentpayments.dev
- Silent Payments webbplats för allmänheten: https://silentpayments.xyz
- Specifikation BIP-352: https://bips.dev/352



### Signet testverktyg




- Faucet Tysta betalningar: https://silentpayments.dev/faucet/signet
- Signet Mempool Explorer: https://mempool.space/signet



### Blindbit-server (självhanterad)




- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle