---
name: Sparrow Wallet - Multisig
description: Skapa en multi-signatur Wallet på Sparrow
---
![cover](assets/cover.webp)



En Wallet med flera signaturer (ofta kallad "*Multisig*") är en Bitcoin Wallet-struktur som kräver flera kryptografiska signaturer, från olika nycklar, för att godkänna en utgift. Till skillnad från en konventionell ("*singlesig*") Wallet, där en enda privat nyckel är tillräcklig för att låsa upp en UTXO, baseras Multisig på en **m-av-n**-modell: av de _n_ nycklar som är associerade med Wallet måste _m_ absolut samsignera varje transaktion.



Denna mekanism gör att kontrollen av en Wallet kan delas mellan flera enheter eller anordningar. I en 2-av-3-konfiguration genereras till exempel tre oberoende uppsättningar nycklar, men endast två behövs för att frigöra medel. Denna arkitektur minskar drastiskt de risker som är förknippade med att en nyckel äventyras eller förloras: en tjuv med tillgång till bara en nyckel kan inte tömma Wallet, och en användare som förlorar en kan fortfarande komma åt sina pengar med de återstående två.



![Image](assets/fr/01.webp)



Denna högre säkerhet medför dock en högre komplexitet. För att konfigurera en Multisig Wallet krävs flera Mnemonic-fraser (en per signaturfaktor) och utökade publika nycklar ("*xpub*"). Om du använder en Multisig 2-av-3 Wallet måste du för att hämta Wallet antingen ha alla tre Mnemonic-fraserna eller minst två av de tre fraserna. Men om du bara har två av de tre fraserna behöver du också tillgång till de tre *xpubs*, utan vilka det kommer att vara omöjligt att hämta de offentliga nycklar som behövs för att komma åt de bitcoins de skyddar.



Sammanfattningsvis, för att återställa en Multisig Wallet, måste du :




- Eller få tillgång till alla Mnemonic-fraser som är associerade med varje signaturfaktor;
- Antingen har du det minsta antal Mnemonic-fraser som krävs enligt tröskelvärdet för att kunna signera, och du har också tillgång till xpubarna för alla faktorer för att kunna hämta de nödvändiga publika nycklarna.



![Image](assets/fr/02.webp)



Denna hantering av Multisig Wallet säkerhetskopior underlättas av *Output Script Descriptors*, som grupperar alla offentliga data som krävs för att komma åt fonderna. Denna funktionalitet är dock ännu inte implementerad i all programvara för Wallet-hantering.



Multisig är särskilt lämpad för bitcoinanvändare som vill ha ökad säkerhet eller kollektiv förvaltning av medel: företag, föreningar, familjer eller enskilda användare som innehar en betydande mängd bitcoins. Den kan användas för att skapa decentraliserade styrsystem, t.ex. för att fördela signeringsbehörighet mellan flera chefer eller teammedlemmar.



I den här handledningen lär vi oss hur man skapar och använder en klassisk multisignatur Wallet med **Sparrow wallet**. Om du vill skapa en anpassad multisignatur Wallet med tidslås rekommenderar jag att du använder Liana istället:



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

## Förkunskapskrav



För denna handledning ska jag visa dig hur du gör en Multisig med [Sparrow wallet Wallet management software] (https://sparrowwallet.com/download/). Om du ännu inte har installerat den här programvaran ska du göra det nu. Om du behöver hjälp har vi också en detaljerad handledning om hur du konfigurerar Sparrow wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)

För att sätta upp en Wallet med flera signaturer behöver du olika hårdvaruplånböcker. För en Multisig 2-de-3 kan du till exempel använda :




- En Trezor modell ett;
- Ledger Flex;
- En Coldcard MK3.



![Image](assets/fr/03.webp)



Det är en bra idé att använda olika fabrikat av Hardware Wallet i din Multisig-konfiguration. Detta säkerställer att om en specifik modell stöter på ett allvarligt problem kommer det inte att påverka den övergripande säkerheten för din Multisig. Dessutom kan du dra nytta av de specifika fördelarna med varje enhet. Till exempel, i min konfiguration :





- Trezor Model One är helt öppen källkod, vilket gör det möjligt att verifiera seed-generationen. Men eftersom den inte är utrustad med ett Secure Element är den fortfarande sårbar för fysiska attacker;





- Ledger Flex, å andra sidan, drar nytta av okontrollerbar proprietär firmware, men innehåller ett Secure Element som erbjuder utmärkt fysiskt skydd;





- Coldcard är utrustat med ett Secure Element och dess kod är sökbar. Det är ett intressant val för vår konfiguration, eftersom det erbjuder verifieringsfunktioner som inte finns på andra modeller.



Innan du konfigurerar din Multisig Wallet, se till att varje Hardware Wallet är korrekt konfigurerad (generering och sparande av Mnemonic, PIN-definition). För detaljerade instruktioner kan du konsultera våra handledningar för varje Hardware Wallet, till exempel :



https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

Som vi kommer att se senare i den här handledningen är det också möjligt att integrera en faktor i din Multisig-konfiguration som inte är kopplad till en Hardware Wallet, men vars privata nycklar lagras på din dator. Den här metoden är naturligtvis mindre säker än den exklusiva användningen av hårdvaruplånböcker, men den kan vara relevant i vissa fall. För en Multisig 2-de-3 kan du till exempel välja två hårdvaruplånböcker och en Software Wallet.



## Skapa en Multisig Wallet



Öppna Sparrow wallet, klicka på fliken "*File*" och välj sedan "*New Wallet*".



![Image](assets/fr/04.webp)



Tilldela ett namn till din multisignatur Wallet och klicka sedan på "*Create Wallet*" för att bekräfta.



![Image](assets/fr/05.webp)



I rullgardinsmenyn "*Policy Type*" väljer du alternativet "*Multi Signature*".



![Image](assets/fr/06.webp)



I det övre högra hörnet kan du nu definiera det totala antalet nycklar i din Multisig, samt antalet medundertecknare som krävs för att godkänna en utgift. I mitt exempel är detta ett 2-av-3-system.



![Image](assets/fr/07.webp)



Längst ner i fönstret visar Sparrow wallet tre "*Keystore*". Var och en representerar en uppsättning nycklar. Här använder jag tre hårdvaruplånböcker, så varje "*Keystore*" motsvarar en av dem. Vi ska nu konfigurera dem.



Jag börjar med Coldcard. På fliken "*Keystore 1*" väljer jag alternativet "*Airgapped Hardware Wallet*".



![Image](assets/fr/08.webp)



På Coldcard, när enheten är upplåst, går jag till menyn "* Inställningar *" och sedan till "* Multisig plånböcker *".



![Image](assets/fr/09.webp)



I den här menyn kan du hantera de Multisig-plånböcker som Coldcard deltar i. Jag vill skapa en ny, så jag väljer "*Export XPUB*".



![Image](assets/fr/10.webp)



För fältet "*Kontonummer*" kan du, om du bara hanterar ett konto, lämna det tomt och validera direkt genom att trycka på bekräftelseknappen.



![Image](assets/fr/11.webp)



Coldcard kommer då att generate en fil som innehåller din xpub, sparad på Micro SD-kortet.



![Image](assets/fr/12.webp)



Sätt i detta Micro SD-kort i din dator. I Sparrow wallet klickar du på knappen "*Import File...*" bredvid "*Coldcard Multisig*" och väljer sedan den fil som skapats av Coldcard på kortet.



![Image](assets/fr/13.webp)



Din xpub har importerats framgångsrikt. Vi ska nu upprepa proceduren med de andra två hårdvaruplånböckerna.



![Image](assets/fr/14.webp)



För Ledger Flex väljer jag "*Keystore 2*" och klickar sedan på "*Connected Hardware Wallet*". Se till att Ledger är ansluten till datorn, olåst och att Bitcoin-applikationen är öppen.



![Image](assets/fr/15.webp)



Klicka sedan på knappen "*Scan...*".



![Image](assets/fr/16.webp)



Bredvid namnet på din Hardware Wallet klickar du på "*Import Keystore*".



![Image](assets/fr/17.webp)



Den andra firmatecknaren är nu korrekt registrerad i Sparrow wallet.



![Image](assets/fr/18.webp)



Jag upprepar exakt samma procedur med Trezor One för att slutföra Multisig-konfigurationen.



![Image](assets/fr/19.webp)



I min konfiguration täcker vi inte detta fall, men om du vill inkludera en signatur via en Software Wallet i Sparrow (Hot Wallet) i din Multisig, klickar du bara på knappen "*Ny eller importerad Software Wallet*".



Nu när alla dina signaturenheter har importerats till Sparrow wallet kan du slutföra skapandet av Multisig genom att klicka på "*Apply*".



![Image](assets/fr/20.webp)



Välj ett starkt lösenord för att säkra åtkomsten till din Sparrow wallet Wallet. Detta lösenord skyddar dina publika nycklar, adresser, etiketter och transaktionshistorik från obehörig åtkomst.



Kom ihåg att spara lösenordet på ett säkert ställe, t.ex. i en lösenordshanterare, så att du inte tappar bort det.



![Image](assets/fr/21.webp)



## Säkerhetskopiering av en Multisig Wallet



Vi kommer nu att spara vår *Output Script Descriptor* på Coldcard (detta gäller endast användare med ett Coldcard i sin Multisig), och framför allt kommer vi att hålla en säkerhetskopia av den på ett oberoende medium.



*Descriptor* innehåller alla xpubar i din Multisig Wallet, samt de härledningsvägar som använts för att generate nycklarna. Kom ihåg vad vi såg i del 1: för att återställa en Multisig Wallet måste du antingen ha **alla** Mnemonic-fraserna, eller bara det minsta antal som krävs för att nå signaturtröskeln. I det senare fallet är det dock också viktigt att ha **expubarna** för de saknade undertecknarna. *Descriptor* innehåller alla dina Multisig:s xpubar.



Om detta inte är tydligt, kom ihåg detta: för att hämta en Multisig behöver du det minsta antalet Mnemonic-fraser för varje Hardware Wallet som används, beroende på tröskelvärdet (i mitt fall: 2 fraser), samt *Descriptor*.



Denna *Deskriptor* innehåller inga privata nycklar, endast offentliga. Det innebär att den inte ger tillgång till pengarna. Den är därför inte lika kritisk som Mnemonic-fraser, som ger full tillgång till dina bitcoins. Risken med *Descriptor* är enbart relaterad till konfidentialitet: i händelse av kompromisser kan en tredje part observera alla dina transaktioner, men kan inte spendera dina pengar.



Jag rekommenderar starkt att du skapar flera kopior av denna *Descriptor* och förvarar dem med varje signeringsenhet på din Multisig. I mitt fall skriver jag till exempel ut *Descriptor* på papper och förvarar en kopia med Coldcard, en annan med Trezor och en med Ledger. Jag sparar också *Descriptor* som en PDF-fil på tre USB-minnen, vart och ett med en av hårdvaruplånböckerna. På så sätt maximerar jag mina chanser att aldrig förlora denna *Descriptor*, och jag är säker på att ha två kopior (en fysisk och en digital) med varje enhet.



När din Multisig Wallet har skapats förser Sparrow dig automatiskt med denna *Descriptor*. Klicka på knappen "*Spara PDF...*" för att spara den både som text och som QR-kod.



![Image](assets/fr/22.webp)



Du kan sedan skriva ut den här PDF-filen och kopiera den till dina USB-minnen.



![Image](assets/fr/23.webp)



Vi kommer också att registrera denna *Descriptor* i Coldcard (om du använder ett sådant i din konfiguration). Detta kommer att göra det möjligt för Coldcard att verifiera att varje transaktion som signeras senare motsvarar den ursprungliga Wallet: korrekta xpubar, korrekt Address-format, korrekt härledningsväg ... Utan denna importerade *Descriptor* kan Coldcard inte bekräfta att Exchange-adresser inte har kapats eller att PSBT inte har manipulerats.



Det är detta som gör Coldcard så intressant i en Multisig: den erbjuder ytterligare kontroller mot vissa sofistikerade attacker, vilket andra hårdvaruplånböcker inte tillåter (förutsatt, naturligtvis, att du använder den för att signera).



I Sparrow öppnar du menyn "*Settings*" och klickar sedan på "*Export...*".



![Image](assets/fr/24.webp)



Bredvid alternativet "*Coldcard Multisig*" klickar du på "*Export File...*" och sparar textfilen på Micro SD-kortet.



![Image](assets/fr/25.webp)



Sätt sedan in kortet i Coldcard. Gå till menyn "*Inställningar*", sedan "*Multisig plånböcker*" och välj "*Importera från SD*".



![Image](assets/fr/26.webp)



Välj lämplig fil och bekräfta importen.



![Image](assets/fr/27.webp)



Klicka på namnet på din nyligen importerade Multisig.



![Image](assets/fr/28.webp)



Kontrollera Multisig:s konfigurationsparametrar och bekräfta sedan registreringen.



![Image](assets/fr/29.webp)



Din Multisig är nu korrekt sparad i ditt Coldcard. Om du har flera Coldcards i samma Multisig upprepar du denna procedur för varje Coldcard.



Förutom att spara *Descriptor*, glöm inte att ägna särskild uppmärksamhet åt att spara Mnemonic-fraserna för var och en av dina signaturenheter. Om du precis har börjat rekommenderar jag starkt att du läser den här andra handledningen för att lära dig hur du sparar och hanterar dem på rätt sätt:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Innan du tar emot dina första bitcoins på din Multisig, **råder jag dig starkt att utföra ett tomt återställningstest**. Anteckna viss referensinformation, till exempel den första mottagande Address, och återställ sedan dina hårdvaruplånböcker medan Wallet fortfarande är tom. Försök sedan återställa dina Multisig Wallet på hårdvaruplånböckerna med hjälp av dina Mnemonic fraspapperskopior, sedan på Sparrow med hjälp av *Descriptor*. Kontrollera att den första Address som genereras efter återställningen matchar den som du ursprungligen skrev ner. Om den gör det kan du vara säker på att dina pappersbackuper är tillförlitliga.



Om du vill veta mer om hur du utför ett återställningstest föreslår jag att du läser den här andra handledningen:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Ta emot bitcoins på din Multisig



Din Wallet är nu redo att ta emot bitcoins. I Sparrow klickar du på fliken "*Receive*".



![Image](assets/fr/30.webp)



Innan du använder Address som genererats av Sparrow wallet, ta dig tid att kontrollera den direkt på skärmen på dina hårdvaruplånböcker. Detta kommer att säkerställa att Address inte har ändrats och att dina enheter har de privata nycklar som behövs för att spendera de tillhörande pengarna. Detta hjälper till att skydda dig mot ett antal attackvektorer.



För att göra detta klickar du på "*Display Address*" för att visa Address på din Trezor eller Ledger, när den är ansluten via kabel.



![Image](assets/fr/31.webp)



Med Coldcard kan denna verifiering utföras utan någon interaktion med Sparrow. Öppna helt enkelt menyn "*Address Explorer*" och välj sedan din Multisig längst ner.



![Image](assets/fr/32.webp)



Du kommer då att se de mottagningsadresser som genereras av Multisig.



![Image](assets/fr/33.webp)



Kontrollera att den Address som visas på varje Hardware Wallet exakt motsvarar den i Sparrow wallet. Det är lämpligt att göra detta precis innan du delar Address med betalaren för att vara säker på dess integritet.



Du kan sedan tilldela en "*Label*" till denna Address för att ange ursprunget för de mottagna bitcoins. Detta är ett bra sätt att organisera hanteringen av dina UTXO:er.



![Image](assets/fr/34.webp)



När detta har verifierats kan du använda Address för att ta emot bitcoins.



![Image](assets/fr/35.webp)



## Skicka bitcoins med din Multisig



Nu när du har fått dina första Satss på din Multisig Wallet kan du spendera dem också! I Sparrow går du till fliken "*Sänd*" för att skapa en ny transaktion.



![Image](assets/fr/36.webp)



Om du vill använda *Coin Control*, dvs. manuellt välja de UTXO du vill spendera, går du till fliken "*UTXO*". Välj de UTXO:er du vill använda och klicka sedan på "*Send Selected*". Du kommer automatiskt att omdirigeras till fliken "*Send*", där UTXO:erna redan är förifyllda.



![Image](assets/fr/37.webp)



Ange destinationen Address. Flera adresser kan läggas till genom att klicka på "*+ Add*".



![Image](assets/fr/38.webp)



Lägg till en "*Label*" för att beskriva syftet med denna kostnad, så att det blir lättare att spåra dina transaktioner.



![Image](assets/fr/39.webp)



Ange det belopp som ska skickas till den valda Address.



![Image](assets/fr/40.webp)



Justera laddningsgraden efter aktuella nätverksförhållanden. Se till exempel [Mempool.space] (https://Mempool.space/) för att välja en lämplig laddningsnivå.



När du har kontrollerat alla transaktionsparametrar klickar du på "*Create Transaction*".



![Image](assets/fr/41.webp)



Om du är nöjd med allt klickar du på "*Finalize Transaction for Signing*".



![Image](assets/fr/42.webp)



Längst ner på skärmen ser du att Sparrow väntar på 2 signaturer. Detta är normalt: den Wallet som används här är en Multisig 2-de-3.



![Image](assets/fr/43.webp)



Jag börjar med att signera med mitt Coldcard. För att göra detta sätter jag in ett Micro SD-kort i datorn och klickar sedan på "*Save Transaction*".



![Image](assets/fr/44.webp)



Det finns tre sätt att överföra transaktionen som ska signeras till din Hardware Wallet och sedan hämta den från Sparrow. Det första är att använda ett Micro SD-kort, som vi kommer att göra här för Coldcard. Den andra är via en kabelanslutning, som vi kommer att använda för den andra signaturen (Ledger och Trezor). Slutligen är det möjligt att använda QR-kodkommunikation för kamerautrustade enheter som Coldcard Q, Jade Plus eller Passport V2.



När PSBT (*Partially Signed Bitcoin Transaction*) har sparats på Micro SD-kortet sätter jag in det i Coldcard MK3 och väljer sedan menyn "*Ready to Sign*".



![Image](assets/fr/45.webp)



På din Hardware Wallet-skärm kontrollerar du noggrant transaktionsparametrarna: mottagarens Address, det skickade beloppet och avgifterna. När transaktionen har bekräftats validerar du för att gå vidare till underskrift.



![Image](assets/fr/46.webp)



Återlämna sedan Micro SD till din dator och klicka på "*Load Transaction*" i Sparrow. Välj PSBT signerad av Coldcard från dina filer.



![Image](assets/fr/47.webp)



Du kan se att Coldcard-signaturen har lagts till. Jag kommer nu att använda en andra enhet, i det här fallet Ledger, för att utföra den andra signaturen som krävs. Jag ansluter den, låser upp den och klickar sedan på "*Sign*" på Sparrow.



![Image](assets/fr/48.webp)



Klicka på "*Sign*" bredvid namnet på din Hardware Wallet.



![Image](assets/fr/49.webp)



Första gången du använder din Ledger med denna Multisig kommer Sparrow att be dig att verifiera medsignaturernas utökade publika nycklar (xpubs). Precis som med Coldcard förhindrar detta steg att du signerar i blindo senare. För att validera denna information jämför du den xpub som visas på Ledger-skärmen med de som tillhandahålls direkt av dina andra hårdvaruplånböcker.



![Image](assets/fr/50.webp)



Kontrollera mottagarens Address, det överförda beloppet och transaktionsavgiften, och underteckna sedan transaktionen.



![Image](assets/fr/51.webp)



Tryck på skärmen för att signera.



![Image](assets/fr/52.webp)



Sparrow har nu de två signaturer som behövs för att frigöra medlen från Multisig Wallet. Kontrollera transaktionen en sista gång och om allt går bra klickar du på "*Broadcast Transaction*" för att sända den över nätverket.



![Image](assets/fr/53.webp)



Du hittar den här transaktionen i Sparrow wallet:s flik "*Transaktioner*".



![Image](assets/fr/54.webp)



Grattis, du vet nu hur man ställer in och använder en multisignatur Wallet på Sparrow. Om du tyckte att den här handledningen var användbar skulle jag vara tacksam om du lämnar en Green-tumme nedan. Du får gärna dela den här artikeln på dina sociala nätverk. Tack för att du delar med dig!



För att gå vidare rekommenderar jag att du läser den här handledningen om en annan metod för att öka säkerheten för din Bitcoin Wallet, passphrase BIP39 :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7