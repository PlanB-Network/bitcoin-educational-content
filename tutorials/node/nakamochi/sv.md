---
name: Nakamochi
description: Körning av nod enkelt - Hur man konfigurerar och använder Nakamochi Bitcoin- och Lightning-noden.
---

![image](assets/cover.webp)

Att köra sin egen Bitcoin och Lightning Full node behöver inte längre vara en komplex uppgift som är begränsad till tekniska experter. Traditionellt har det krävts djupgående kunskaper om kryptografi, nätverk och mjukvaruutveckling för att sätta upp och hantera noder. Nakamochi ändrar på detta genom att göra noder tillgängliga för alla, oavsett teknisk bakgrund.


Med Nakamochi kan vem som helst sätta upp och driva en nod hemifrån, vilket möjliggör full integritet och ekonomiskt oberoende. Att driva en Full node säkrar inte bara dina egna transaktioner utan bidrar också till Bitcoin-nätverkets styrka. Ett decentraliserat och motståndskraftigt Bitcoin-nätverk förlitar sig på en bred distribution av noder för att säkerställa dess säkerhet och oberoende.


### Innehållsförteckning



- Vad är Nakamochi och hur fungerar det?
- Uppsättning av Nakamochi
- Om Lightning Network
- Öppna kanaler och genomföra transaktioner i Lightning Network



## Vad är Nakamochi och hur fungerar det?


Nakamochi är en Full node med enbart Bitcoin som stöder både Bitcoin- och Lightning-nätverken. Den innehåller en integrerad Bitcoin och Lightning Wallet, vilket gör det möjligt för användare att köra en säker, självsuverän Bitcoin-nod samtidigt som de drar nytta av Lightning Network:s hastighet och låga transaktionskostnader.


Din Nakamochi-nod hanteras via en mobilapp, [BitBanana (Android)](https://bitbanana.app) och [Zeus (iOS)](https://bitbanana.app), så att du kan styra den bekvämt från var som helst. Dessa appar fungerar som en fjärrkontroll för din nod och gör det möjligt för dig att betala direkt med Bitcoin eller Lightning, hantera transaktioner, öppna eller stänga kanaler, kontrollera saldon och övervaka din nods prestanda, allt på ett enkelt sätt.



## Att sätta upp Nakamochi tar bara 5 minuter


### Steg 1: Koppla in och kom igång


1. Anslut Nakamochi till ström och Wi-Fi.

2. Klicka på **"Setup New Wallet"** och lagra din 24 ord långa återställningsfras på ett säkert sätt.

3. Använd en app för nodhantering (Zeus eller BitBanana) för att ansluta till din Nakamochi:

4. Öppna appen och skanna QR-koden som visas på din Nakamochi.

5. För ökad säkerhet kan du ange en PIN-kod på din enhet.


![image](assets/en/01.webp)

_Anslut till ström och skriv ner din 24-ords fras_


![image](assets/en/02.webp)

_Vänta tills blockkedjan har hunnit ikapp_


![image](assets/en/03.webp)

_Ställ in ny plånbok i Lightning-fliken_


![image](assets/en/04.webp)

_Skanna QR-koden med Node Management-appen_


![image](assets/en/05.webp)

_För extra säkerhet ställ in en PIN-kod_


**Obs:** _Låt din Nakamochi-nod synkronisera med blockkedjan. Denna process kan ta lite tid beroende på din internetanslutning._



## Om Lightning Network


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Bitcoin Lightning Network revolutionerar Bitcoin-transaktioner genom att göra dem snabbare, billigare och mer effektiva. Den är perfekt för daglig användning och möjliggör nästan omedelbara betalningar med minimala avgifter, perfekt för mikrotransaktioner som att köpa kaffe eller hantera frekventa småköp.

Genom att driva off-chain är Lightning utformat för att skala upp och stödja tusentals transaktioner per sekund utan att överbelasta huvudplattformen Bitcoin Blockchain. Detta gör den till en nyckelspelare i Bitcoin:s utveckling till ett praktiskt, globalt betalningssystem.

Sekretess är en annan fördel, eftersom transaktioner på Lightning dirigeras genom privata betalningskanaler snarare än att registreras direkt på Blockchain. Detta säkerställer ett mer diskret sätt att göra transaktioner samtidigt som Bitcoin:s robusta säkerhet bibehålls.



#### Förklaring av betalningskanaler


Lightning Network fungerar genom betalningskanaler, som är anslutningar mellan två parter som möjliggör flera transaktioner utan att interagera direkt med Blockchain. När en kanal är öppen uppdateras saldot mellan de två parterna på denna andra Layer Lightning-lösning för varje transaktion, vilket säkerställer snabba betalningar till låg kostnad. Endast kanalens öppning och stängning registreras On-Chain, vilket minskar överbelastningen på Bitcoin Blockchain. Denna design säkerställer skalbarhet och integritet, eftersom enskilda transaktioner förblir oregistrerade på den offentliga Ledger.


**Exempel:** Alice och Bob öppnar en kanal genom att binda Bitcoin till den. Alice skickar Bitcoins till Bob, och deras off-chain-saldon uppdateras omedelbart utan en On-Chain-post. Om Alice sedan betalar Charlie, och Alice inte har någon direkt kanal till Charlie, kan betalningen dirigeras genom Bob:s kanal för att nå Charlie. Routning genom mellanliggande noder säkerställer betalningar även utan direkta anslutningar, vilket gör nätverket mycket effektivt.



## Öppna kanaler och göra transaktioner i Lightning Network


När din Nakamochi är konfigurerad och ansluten till en app för nodhantering kan du börja använda Lightning Network genom att öppna kanaler och göra transaktioner.


### Öppna kanaler på Zeus (iOS):


1. Gå till fliken **"Channels"** (nedre menyn).

2. Klicka på **"+"** för att öppna en ny kanal.

3. Skanna eller ange pubnyckeln för den nod du vill ansluta till.

4. Ange det låsta beloppet (välj tillsammans med din peer eller använd det lägsta fasta beloppet för välkända noder).

5. Klicka på **"Öppna kanal"**.


![image](assets/en/06.webp)

_ZEUS skärmdump_ _ZEUS skärmdump


För mer information: [Kanaler | Zeus-dokumentation](https://docs.zeusln.app/)


### Öppna kanaler på BitBanana (Android):


1. Öppna hamburgermenyn (till vänster).

2. Gå till **"Channels"**.

3. Klicka på **"+"** för att lägga till/öppna en ny kanal.

4. Skanna eller klistra in pubnyckeln.

5. Ange det låsta beloppet (välj tillsammans med din peer eller använd det lägsta fasta beloppet för välkända noder).


![image](assets/en/07.webp)

_Bitbanana skärmdump_ _Bitbanana skärmdump


För mer information: [BitBanana](https://bitbanana.com)


När din kanal är öppen kan betalningar dirigeras genom den till andra deltagare i nätverket. Saldon justeras off-chain, vilket säkerställer att transaktioner är nästan omedelbara och medför minimala avgifter.

Om du inte längre behöver en kanal kan du stänga den. Denna åtgärd reglerar det slutliga saldot mellan dig och din peer och registrerar det On-Chain. Helst ska båda parter vara överens och vara online för en "kooperativ stängning" (snabbare och mindre avgifter jämfört med en "påtvingad stängning" med en peer som inte svarar/är offline).

Generellt rekommenderar vi att du lämnar kanaler öppna för att minska kostnaderna och öka nätverkets tillförlitlighet och effektivitet. Genom att hålla kanalerna öppna minimerar du transaktionsavgifterna för On-Chain, undviker driftstopp för kanalåteranslutningar och upprätthåller en stabil routningskapacitet för sömlös betalningshantering. Detta tillvägagångssätt främjar ett robust och motståndskraftigt nätverk samtidigt som det förbättrar den övergripande användarupplevelsen och minskar de operativa omkostnaderna.



### Användbara länkar



- [Om Nakamochi](https://nakamochi.io/)
- [Prenumerera på Nakamochis nyhetsbrev](https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)