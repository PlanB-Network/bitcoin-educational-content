---
name: BIP-39 Passphrase Ledger
description: Hur lägger man till en passphrase till sin Ledger Wallet?
---
![cover](assets/cover.webp)


En BIP39 passphrase är ett valfritt lösenord som, när det kombineras med din Mnemonic-fras, ger ytterligare Layer i säkerhet för deterministiska och hierarkiska Bitcoin-plånböcker. I den här handledningen går vi tillsammans igenom hur du ställer in en passphrase på din säkra Bitcoin Wallet på en Ledger (oavsett modell).


Om du inte är bekant med begreppet passphrase, hur det fungerar och dess konsekvenser för din Bitcoin Wallet, rekommenderar jag starkt att du läser den här andra teoretiska artikeln där jag förklarar allt innan du börjar denna handledning:


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

## Hur fungerar passphrase på en Ledger?


Med Ledger-enheter har du två olika alternativ för att konfigurera en passphrase på din Wallet: alternativet "*PIN-tied*" och alternativet "*temporary*".


Med alternativet "*PIN-tied*" associerar du en passphrase med en andra PIN-kod på din Ledger. Detta innebär att du kommer att ha 2 PIN-koder: en för att komma åt din vanliga Wallet utan en passphrase, och den andra för att komma åt din andra Wallet som skyddas av passphrase.


![PASSPHRASE BIP39](assets/notext/03.webp)


I grund och botten, även med detta passphrase-alternativ knutet till den andra PIN-koden, förblir din passphrase din passphrase. Detta innebär att om du förlorar din Ledger och vill återställa dina bitcoins på en annan enhet eller programvara, behöver du absolut din 24 ords fras och din **kompletta passphrase**. Den PIN-kod som är kopplad till passphrase används endast för att komma åt den på din aktuella Ledger, men den fungerar inte på andra huvudböcker eller annan programvara. Det är därför viktigt att göra en fullständig säkerhetskopia av din passphrase på ett fysiskt medium. **Att känna till den sekundära PIN-koden räcker inte för att återfå åtkomst till din Wallet**; det är helt enkelt en bekvämlighetsfunktion på din Ledger.


Detta andra PIN-alternativ är särskilt intressant för att hantera fysiska attacker. Om en angripare till exempel tvingar dig att låsa upp din enhet för att stjäla dina pengar, kan du använda den första PIN-koden för att komma åt en falsk Wallet som innehåller en liten mängd bitcoins, samtidigt som dina huvudsakliga medel är säkra bakom den andra PIN-koden.


Det här alternativet erbjuder dessutom alla säkerhetsfördelar med BIP39 passphrase utan att du behöver ange det manuellt varje gång du använder din signeringsenhet. Detta gör att du kan använda en lång och slumpmässig passphrase och därmed stärka skyddet mot brute force-attacker, samtidigt som du slipper svårigheten att behöva skriva in den manuellt varje gång på enhetens små knappar.

Alternativet "tillfällig passphrase" lagrar inte passphrase på enheten. Varje gång du vill komma åt din skyddade Wallet måste du manuellt ange passphrase på Ledger. Detta gör användningen mer besvärlig men ökar också säkerheten något genom att inte lämna några spår av passphrase på enheten. Så snart du stänger av enheten återgår den till sitt standardtillstånd och kräver en ny inmatning av den fullständiga passphrase för att få åtkomst till de dolda kontona. Detta "tillfälliga passphrase"-alternativ liknar alltså funktionen hos andra hårdvaruplånböcker.

I denna handledning kommer jag att använda Ledger Flex som ett exempel. Men om du använder en annan Ledger-modell förblir processen densamma. För Ledger Stax är Interface densamma som för Ledger Flex. När det gäller modellerna Nano S, Nano S Plus och Nano X är processen och namnen på menyerna desamma, även om Interface är annorlunda.


**Om du redan har tagit emot bitcoins på din Ledger innan du aktiverar passphrase, måste du överföra dem via en Bitcoin-transaktion.** Passphrase genererar en uppsättning nya nycklar och skapar därmed en Wallet som är helt oberoende av din ursprungliga Wallet. När du lägger till passphrase kommer du att ha en ny Wallet som är tom. Detta innebär dock inte att din första Wallet utan passphrase raderas. Du kan fortfarande komma åt den, antingen direkt via din Ledger utan att ange passphrase eller via en annan programvara som använder din 24-ordsfras.


Innan du påbörjar denna handledning ska du kontrollera att du redan har initialiserat din Ledger och genererat din Mnemonic-fras. Om detta inte är fallet och din Ledger är ny, följ den specifika handledningen för din modell som finns på PlanB Network. När detta steg är slutfört kan du återgå till den här handledningen.


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

## Hur sätter man upp en tillfällig passphrase med en Ledger?


På startsidan för din Ledger klickar du på kugghjulet för inställningar.


![PASSPHRASE BIP39](assets/notext/04.webp)


Välj menyn "Avancerat" och sedan "Ställ in passphrase".


![PASSPHRASE BIP39](assets/notext/05.webp)


Det här är steget där du kan välja mellan alternativet "kopplat till PIN" eller "tillfälligt" som vi pratade om i föregående del. Här kommer jag att förklara hur du ställer in en tillfällig passphrase, så klicka på "Ställ in tillfällig passphrase".


![PASSPHRASE BIP39](assets/notext/06.webp)

Du ombeds sedan att ange din passphrase. Välj en stark passphrase och gå omedelbart vidare till en fysisk säkerhetskopia, på ett medium som papper eller metall. I det här exemplet valde jag passphrase: `fH3&kL@9mP#2sD5qR!82`. När du har angett din passphrase klickar du på knappen "*Continue*".

![PASSPHRASE BIP39](assets/notext/07.webp)


Kontrollera att din passphrase stämmer överens med vad du har noterat på din fysiska säkerhetskopia och klicka sedan på knappen "*Yes, it's correct*" för att bekräfta.


![PASSPHRASE BIP39](assets/notext/08.webp)


För att slutföra skapandet av din passphrase, ange PIN-koden för din Ledger. Från och med nu, när du vill komma åt din Wallet med en passphrase på Ledger, måste du följa exakt samma steg som beskrivs här.


![PASSPHRASE BIP39](assets/notext/09.webp)


Du kan nu importera din uppsättning publika nycklar på Sparrow wallet för att hantera din Wallet. På Sparrow kommer detta att motsvara en annan Wallet än din ursprungliga Wallet utan en passphrase.


Öppna Sparrow wallet. Kontrollera att programvaran är ansluten till en nod, klicka sedan på fliken "*File*" och välj "*New Wallet*".


![PASSPHRASE BIP39](assets/notext/10.webp)


Välj ett namn för din Wallet som skyddas av en passphrase. I det här exemplet valde jag ett namn som uttryckligen innehåller termen "*passphrase*". Men om du föredrar att behålla diskretionen för denna Wallet på din dator, kan du välja ett mindre suggestivt namn.


![PASSPHRASE BIP39](assets/notext/11.webp)


Välj typ av skript för din Wallet. Jag råder dig att välja "*Taproot*" eller alternativt "*Native SegWit*".


![PASSPHRASE BIP39](assets/notext/12.webp)


Anslut din Ledger till din dator och klicka sedan på "*Anslutit Hardware Wallet*". Kontrollera att du redan har angett din passphrase på din Ledger. Om inte, gå tillbaka till föregående steg för att ange din passphrase. Innan du fortsätter med skanningen, kom också ihåg att öppna applikationen "*Bitcoin*" på din Ledger.


![PASSPHRASE BIP39](assets/notext/13.webp)


Klicka på knappen "*Scan...*".


![PASSPHRASE BIP39](assets/notext/14.webp)


Klicka på "*Importera Keystore*" bredvid din Ledger.


![PASSPHRASE BIP39](assets/notext/15.webp)


Din Wallet som skyddas av passphrase är nu skapad på Sparrow. För att bekräfta, klicka på knappen "*Apply*".


![PASSPHRASE BIP39](assets/notext/16.webp)

Välj ett starkt lösenord för att säkra åtkomsten till Sparrow wallet. Detta lösenord säkerställer åtkomst till dina Wallet-data på Sparrow, vilket hjälper till att skydda dina offentliga nycklar, adresser, etiketter och transaktionshistorik mot obehörig åtkomst.

Jag råder dig att spara det här lösenordet i en lösenordshanterare så att du inte glömmer det.


![PASSPHRASE BIP39](assets/notext/17.webp)


Och där har du det, din Wallet är nu skapad! I menyn "*Inställningar*" kommer Sparrow att förse dig med ditt "*Master fingeravtryck*". Detta representerar fingeravtrycket för din huvudnyckel, som används som grund för att härleda din Wallet. Jag rekommenderar starkt att du behåller en kopia av detta fingeravtryck. I mitt exempel motsvarar det: `281ee33a`.


![PASSPHRASE BIP39](assets/notext/18.webp)


Kom ihåg vad vi nämnde i de tidigare delarna: ett misstag, även ett mindre sådant, när du anger din passphrase kommer generate en helt ny Wallet med olika nycklar. Varje gång du behöver säkerställa att du kommer åt rätt Wallet med rätt passphrase, kontrollera att fingeravtrycket på din huvudnyckel matchar det du antecknade. Denna information utgör i sig ingen risk för säkerheten för dina medel eller din integritet.


Innan du använder din Wallet med en passphrase, rekommenderar jag starkt att du utför ett återställningstest med torrkörning. Anteckna en referensinformation som din xpub eller fingeravtrycket på din huvudnyckel och återställ sedan din Ledger medan Wallet fortfarande är tom. Försök sedan återställa din Wallet på Ledger med hjälp av dina pappersbackuper av 24-ordsfrasen och passphrase. Kontrollera att den information som genereras efter återställningen stämmer överens med vad du ursprungligen noterade. Om så är fallet kan du vara säker på att dina pappersbackuper är tillförlitliga.


## Hur ställer man in en passphrase kopplad till en PIN-kod med en Ledger?


På startsidan för din Ledger klickar du på kugghjulet för inställningar.


![PASSPHRASE BIP39](assets/notext/19.webp)


Välj menyn "*Avancerat*" och sedan "*Ställ in passphrase*".


![PASSPHRASE BIP39](assets/notext/20.webp)


Det här är steget där du kan välja mellan alternativet "*länkad till PIN-kod*" eller "*tillfällig*" som vi pratade om i föregående del. Här ska jag förklara hur du ställer in en passphrase som är kopplad till en PIN-kod, så klicka på "*Ställ in passphrase och koppla den till en ny PIN-kod*".


![PASSPHRASE BIP39](assets/notext/21.webp)

Du måste sedan välja den PIN-kod som ska kopplas till din passphrase. Precis som med huvud-PIN-koden rekommenderar vi att du väljer en 8-siffrig PIN-kod, så slumpmässig som möjligt. Se också till att spara denna kod på en annan plats än där din Ledger Flex är lagrad.

I mitt fall är huvud-PIN-koden `58293647` och jag valde `71425839` som sekundär PIN-kod för passphrase.


![PASSPHRASE BIP39](assets/notext/22.webp)


Du ombeds sedan att ange din passphrase. Välj en stark passphrase och gå omedelbart vidare till en fysisk säkerhetskopia, på ett medium som papper eller metall. I det här exemplet valde jag passphrase: `fH3&kL@9mP#2sD5qR!82`. När du har angett din passphrase klickar du på knappen "*Continue*".


![PASSPHRASE BIP39](assets/notext/23.webp)


Kontrollera att din passphrase stämmer överens med vad du har noterat på din fysiska säkerhetskopia och klicka sedan på knappen "*Ja, det stämmer*" för att bekräfta.


![PASSPHRASE BIP39](assets/notext/24.webp)


För att slutföra skapandet av din passphrase, ange huvud-PIN-koden för din Ledger (inte den som är kopplad till passphrase).


![PASSPHRASE BIP39](assets/notext/25.webp)


Från och med nu, när du vill komma åt din Wallet med en passphrase på Ledger, måste du inte ange den huvudsakliga PIN-koden utan den sekundära PIN-koden:


- Huvud-PIN-kod (`58293647`) > Wallet utan passphrase.
- Sekundär PIN-kod (`71425839`) > Wallet med passphrase.


Du kan nu importera din uppsättning publika nycklar på Sparrow wallet för att hantera din Wallet. På Sparrow kommer detta att motsvara en annan Wallet än din ursprungliga Wallet utan en passphrase.


Öppna Sparrow wallet. Kontrollera att programvaran är ansluten till en nod, klicka sedan på fliken "*File*" och välj "*New Wallet*".


![PASSPHRASE BIP39](assets/notext/26.webp)


Välj ett namn för din Wallet som skyddas av en passphrase. I det här exemplet valde jag ett namn som uttryckligen innehåller termen "*passphrase*". Men om du föredrar att behålla diskretionen för denna Wallet på din dator kan du välja ett mindre suggestivt namn.


![PASSPHRASE BIP39](assets/notext/27.webp)


Välj skripttyp för din Wallet. Jag råder dig att välja "*Taproot*" eller, om det inte går, "*Native SegWit*".


![PASSPHRASE BIP39](assets/notext/28.webp)

Anslut din Ledger till din dator och klicka sedan på "*Ansluter Hardware Wallet*". Kontrollera att du redan har din passphrase på din Ledger genom att låsa upp den med den sekundära PIN-koden. Om inte, starta om din Ledger och ange den PIN-kod som är kopplad till passphrase. Innan du fortsätter att skanna, kom också ihåg att öppna applikationen "*Bitcoin*" på din Ledger.


![PASSPHRASE BIP39](assets/notext/29.webp)


Klicka på knappen "*Scan...*".


![PASSPHRASE BIP39](assets/notext/30.webp)


Klicka på "*Importera Keystore*".


![PASSPHRASE BIP39](assets/notext/31.webp)


Din Wallet som skyddas av passphrase är nu skapad på Sparrow. För att bekräfta, klicka på knappen "*Apply*".


![PASSPHRASE BIP39](assets/notext/32.webp)


Välj ett starkt lösenord för att säkra åtkomsten till Sparrow wallet. Detta lösenord säkerställer åtkomsten till dina Wallet-data på Sparrow, vilket hjälper till att skydda dina offentliga nycklar, adresser, etiketter och transaktionshistorik mot obehörig åtkomst.


Jag råder dig att spara det här lösenordet i en lösenordshanterare så att du inte glömmer det.


![PASSPHRASE BIP39](assets/notext/33.webp)


Och där har du det, din Wallet är nu skapad! I menyn "*Inställningar*" kommer Sparrow att förse dig med ditt "*Master fingeravtryck*". Detta representerar fingeravtrycket på din huvudnyckel, som används vid basen för din Wallet: s härledning. Jag rekommenderar starkt att du behåller en kopia av detta fingeravtryck. I mitt exempel motsvarar det: `281ee33a`.


![PASSPHRASE BIP39](assets/notext/34.webp)


Kom ihåg vad vi nämnde i de tidigare delarna: ett misstag, även ett mindre sådant, när du anger din passphrase kommer att generate en helt ny Wallet med olika nycklar. Varje gång du behöver säkerställa åtkomst till rätt Wallet med rätt passphrase ska du kontrollera att fingeravtrycket på din huvudnyckel matchar det du noterade. Denna information utgör i sig ingen risk för säkerheten för dina medel eller din integritet.

Innan du använder din Wallet med en passphrase rekommenderar jag starkt att du utför ett återställningstest med torrkörning. Anteckna en referensinformation, t.ex. din xpub eller fingeravtrycket på din huvudnyckel, och återställ sedan din Ledger medan Wallet fortfarande är tom. Försök sedan återställa din Wallet på Ledger med hjälp av dina pappersbackuper av 24-ordsfrasen och passphrase. Kontrollera att den information som genereras efter återställningen stämmer överens med vad du ursprungligen noterade. Om så är fallet kan du vara säker på att dina pappersbackuper är tillförlitliga.


Gratulerar, din Bitcoin Wallet är nu säkrad med en passphrase! Om du tyckte att den här handledningen var till hjälp skulle jag uppskatta om du kunde lämna tummen upp nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!


Jag rekommenderar också att du kollar in den här andra fullständiga handledningen om hur du använder din Ledger Flex:


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a