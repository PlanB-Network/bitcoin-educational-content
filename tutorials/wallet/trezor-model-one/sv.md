---
name: Trezor modell ett
description: Konfigurera och använda Hardware Wallet Model One
---
![cover](assets/cover.webp)



*Bildkredit: [Trezor.io] (https://trezor.io/)*



Trezor Model One är den allra första Hardware Wallet som någonsin släppts, lanserad 2014 av SatoshiLabs. Efter mer än tio år på marknaden är den fortfarande ett intressant val, särskilt för användare som letar efter en Hardware Wallet som är tillgänglig både tekniskt och budgetmässigt. Faktum är att den kostar 49 euro på Trezors officiella webbplats. Det är en av de enda hårdvaruplånböckerna i den här prisklassen. Den ligger mitt emellan instegsenheter på cirka 20 euro, som Tapsigner, som ofta saknar skärm, och mellanklassenheter på cirka 80 euro, som Ledger Nano S Plus eller Trezor Safe 3.



Model One har en 0,96-tums monokrom OLED-display och två fysiska knappar. Den fungerar utan batteri och använder endast en mikro-USB-anslutning för ström och data Exchange.



![Image](assets/fr/01.webp)



Den största nackdelen med Model One är att den saknar Secure Element, vilket gör den sårbar för en mängd olika fysiska attacker, varav vissa är relativt enkla att utföra. Dessa attacker kan omfatta analys av hjälpkanaler för att fastställa enhetens PIN-kod eller mer avancerade tekniker för att extrahera den krypterade seed för att senare kunna brute-forcea den. Observera att dessa attacker kräver fysisk tillgång till enheten. Denna sårbarhet kan dock minskas avsevärt genom att använda en solid passphrase BIP39. Om du väljer den här Hardware Wallet rekommenderar jag starkt att du konfigurerar en passphrase.



Model One erbjuder två viktiga fördelar:




- Den är baserad på en arkitektur med helt öppen källkod. Till skillnad från nyare modeller med Secure Element är alla maskinvaru- och programvarukomponenter i Model One granskningsbara;
- Den är utrustad med en skärm. Såvitt jag vet är detta den enda Hardware Wallet på marknaden i denna prisklass som har en skärm. Detta är en mycket viktig funktion, eftersom den gör det möjligt att verifiera signerad information och mottagningsadresser och därmed förhindra många digitala attacker.



Trezor Model One kan därför vara ett klokt val för nybörjare och medelgoda användare med en begränsad budget. Det är dock viktigt att vara medveten om dess begränsningar när det gäller fysiskt skydd, eftersom Secure Element saknas. Om din budget är begränsad är det här ett bra alternativ, men om du har råd att välja en bättre modell, som Trezor Safe 3 för 79 euro, är det att föredra eftersom den innehåller ett Secure Element.



## Unboxing av Trezor Model One



När du får din Model One ska du se till att lådan och Seal är intakta för att bekräfta att paketet inte har öppnats. En programvaruverifiering av enhetens äkthet och integritet kommer också att utföras när den installeras senare.



Innehållet i lådan inkluderar :




- Trezor Model One;
- Kartong för att skriva in din Mnemonic-fras, klistermärken och instruktioner;
- USB-A till mikro-USB-kabel.



![Image](assets/fr/02.webp)



Det är mycket enkelt att navigera i enheten:




- Högerklicka för att bekräfta och gå vidare till nästa steg;
- Använd vänsterknappen för att gå tillbaka.



## Förkunskapskrav



I den här handledningen ska jag visa dig hur du använder Trezor Model One med [Sparrow Wallet portfolio management software] (https://sparrowwallet.com/download/). Om du ännu inte har installerat den här programvaran, gör det nu. Om du behöver hjälp har vi också en detaljerad handledning om hur du konfigurerar Sparrow Wallet :



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Du behöver också programvaran Trezor Suite för att konfigurera Model One, kontrollera dess äkthet och installera den inbyggda programvaran. Vi kommer bara att använda den här programvaran för det, och efteråt kommer den bara att behövas för uppdateringar av firmware. För den dagliga hanteringen av Wallet kommer vi att använda Sparrow Wallet exklusivt, eftersom det är optimerat för Bitcoin och lätt att använda, även för nybörjare (Sparrow stöder endast Bitcoin, inte altcoins).



[Ladda ner Trezor Suite från den officiella webbplatsen] (https://trezor.io/trezor-suite)



![Image](assets/fr/03.webp)



För båda dessa program rekommenderar jag starkt att du kontrollerar både deras äkthet (med GnuPG) och deras integritet (via Hash) innan du installerar dem på din maskin. Om du inte vet hur du gör detta kan du följa den här andra handledningen :



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## Starta Trezor Model One



Anslut din Model One till datorn där Trezor Suite och Sparrow Wallet redan är installerade.



![Image](assets/fr/04.webp)



Öppna Trezor Suite och klicka sedan på "*Set up my Trezor*".



![Image](assets/fr/05.webp)



Välj "*Bitcoin-only firmware*" och klicka sedan på "*Install Bitcoin-only*".



![Image](assets/fr/06.webp)



Trezor Suite kommer sedan att installera den fasta programvaran på din Model One. Vänligen vänta under installationen.



![Image](assets/fr/07.webp)



Klicka på "*Fortsätt*".



![Image](assets/fr/08.webp)



## Skapa en Bitcoin-portfölj



På Trezor Suite klickar du på knappen "*Create new Wallet*".



![Image](assets/fr/09.webp)



Acceptera användarvillkoren på Hardware Wallet.



![Image](assets/fr/10.webp)



I Trezor Suite klickar du på "*Fortsätt att säkerhetskopiera*".



![Image](assets/fr/11.webp)



Programvaran innehåller instruktioner om hur du hanterar din Mnemonic-fras.



Denna Mnemonic ger dig full, obegränsad tillgång till alla dina bitcoins. Vem som helst som har den här frasen kan stjäla dina pengar, även utan fysisk tillgång till din Trezor Model One.



Frasen på 24 ord återställer åtkomsten till dina bitcoins i händelse av förlust, stöld eller brott på din Hardware Wallet. Det är därför mycket viktigt att spara den noggrant och förvara den på en säker plats.



Du kan skriva den på kartongen som medföljer i lådan, eller för extra säkerhet rekommenderar jag att du graverar den på en bas av rostfritt stål för att skydda den mot brand, översvämning eller kollaps.



Bekräfta instruktionerna och klicka sedan på knappen "*Create Wallet backup*".



![Image](assets/fr/12.webp)



Model One kommer att skapa din Mnemonic-fras med hjälp av sin slumptalsgenerator. Se till att du inte blir iakttagen under denna operation. Skriv ner de ord som visas på skärmen på valfritt fysiskt medium. Beroende på din säkerhetsstrategi kan du överväga att göra flera fullständiga fysiska kopior av frasen (men framför allt, dela inte upp den). Det är viktigt att hålla orden numrerade och i sekventiell ordning.



***Självklart får du aldrig dela dessa ord på Internet, vilket jag gör i denna handledning. Detta exempel Wallet kommer endast att användas på Testnet och kommer att raderas i slutet av handledningen



För mer information om det rätta sättet att spara och hantera din Mnemonic-fras rekommenderar jag starkt att du följer den här andra handledningen, särskilt om du är nybörjare:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Högerklicka för att gå vidare till nästa ord. När du har skrivit ner alla ord klickar du på högerknappen igen för att gå vidare till nästa steg.



![Image](assets/fr/13.webp)



Din Hardware Wallet visar dig återigen alla dina ord. Kontrollera att du har skrivit ner dem alla.



![Image](assets/fr/14.webp)



## Ställa in PIN-koden



Därefter kommer steget med PIN-koden. PIN-koden låser upp din Trezor. Den ger därför skydd mot obehörig fysisk åtkomst. Denna PIN-kod är inte inblandad i härledningen av din Wallet:s kryptografiska nycklar. Så även utan tillgång till PIN-koden kommer du att kunna få tillgång till dina bitcoins om du har din Mnemonic-fras med 12 ord.



På Trezor Suite klickar du på "*Continue to PIN*" och sedan på knappen "*Set PIN*".



![Image](assets/fr/15.webp)



Bekräfta på Model One.



![Image](assets/fr/16.webp)



Vi rekommenderar att du väljer en PIN-kod som är så slumpmässig som möjligt. Var noga med att spara denna kod på en annan plats än där din Trezor lagras (t.ex. i en lösenordshanterare). Du kan definiera en PIN-kod med mellan 8 och 50 siffror. Jag rekommenderar att du väljer en PIN-kod som är så lång som möjligt för att öka säkerheten.



PIN-koden måste anges i Trezor Suite på din dator genom att klicka på de punkter som motsvarar siffrorna, enligt den tangentbordskonfiguration som visas på Trezor Model One.



Denna specifika PIN-kod krävs varje gång du låser upp din Trezor Model One, oavsett om det sker via Trezor Suite eller Sparrow Wallet.



![Image](assets/fr/17.webp)



När du är klar klickar du på knappen "*Enter PIN*".



![Image](assets/fr/18.webp)



Skriv in din PIN-kod igen för att bekräfta.



![Image](assets/fr/19.webp)



På Trezor Suite, klicka på knappen "*Complete setup*".



![Image](assets/fr/20.webp)



Konfigurationen av din Model One är nu klar. Om du vill kan du ändra namn och startsida för din Hardware Wallet.



![Image](assets/fr/21.webp)



Vi kommer inte att behöva Trezor Suite-programvaran längre, förutom för att utföra regelbundna firmwareuppdateringar på din Hardware Wallet, eller om du vill köra ett återställningstest. Vi kommer nu att använda Sparrow för att hantera portföljen, eftersom den här programvaran är perfekt lämpad för användning av enbart Bitcoin.



## Konfigurera portföljen på Sparrow Wallet



Börja med att ladda ner och installera Sparrow Wallet [från den officiella webbplatsen] (https://sparrowwallet.com/) på din dator, om du inte redan har gjort det.



När du har öppnat Sparrow Wallet ska du kontrollera att programvaran är ansluten till en Bitcoin-nod, vilket indikeras av krysset i det nedre högra hörnet av Interface. Om du har problem med att ansluta Sparrow rekommenderar jag att du läser i början av denna handledning:



https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Klicka på fliken "*File*" och sedan på "*New Wallet*".



![Image](assets/fr/22.webp)



Namnge din portfölj och klicka sedan på "*Create Wallet*".



![Image](assets/fr/23.webp)



I rullgardinsmenyn "*Script Type*" väljer du vilken typ av script som ska användas för att säkra dina bitcoins. Jag rekommenderar "*Taproot*", eller om det inte går, "*Native SegWit*".



![Image](assets/fr/24.webp)



Klicka på knappen "*Ansluter Hardware Wallet*". Din Model One måste naturligtvis vara ansluten till datorn.



![Image](assets/fr/25.webp)



Klicka på knappen "*Scan*". Din Model One bör visas.



När du ansluter din Model One till en dator med Sparrow Wallet öppen, kommer du att uppmanas att ange en passphrase BIP39 på Sparrow. Detta avancerade alternativ kommer att tas upp i en framtida handledning. För närvarande kan du helt enkelt välja "*Toggle passphrase Off*" för att förhindra att din Trezor uppmanar dig att ange en passphrase varje gång du startar den.



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

![Image](assets/fr/26.webp)



Klicka på "*Importera Keystore*".



![Image](assets/fr/27.webp)



Du kan nu se detaljerna för din Wallet, inklusive den utökade publika nyckeln för ditt första konto. Klicka på knappen "*Apply*" för att slutföra skapandet av Wallet.



![Image](assets/fr/28.webp)



Välj ett starkt lösenord för att säkra åtkomsten till Sparrow Wallet. Detta lösenord garanterar säker åtkomst till dina Sparrow Wallet-data och skyddar dina publika nycklar, adresser, etiketter och transaktionshistorik från obehörig åtkomst.



Jag råder dig att spara det här lösenordet i en lösenordshanterare så att du inte glömmer det.



![Image](assets/fr/29.webp)



Och nu har din portfölj importerats till Sparrow Wallet!



![Image](assets/fr/30.webp)



Innan du får dina första bitcoins i din Wallet, **råder jag dig starkt att utföra ett tomt återställningstest**. Skriv ner lite referensinformation, t.ex. din xpub, och återställ sedan din Trezor Model One medan Wallet fortfarande är tom. Försök sedan återställa din Wallet på Trezor med hjälp av dina pappersbackuper. Kontrollera att den xpub som genereras efter återställningen matchar den som du ursprungligen skrev ner. Om den gör det kan du vara säker på att dina pappersbackuper är tillförlitliga.



Om du vill veta mer om hur du utför ett återställningstest föreslår jag att du läser den här andra handledningen:



https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## Hur tar man emot bitcoins med Trezor Model One?



På Sparrow klickar du på fliken "*Receive*".



![Image](assets/fr/31.webp)



Innan du använder den Address som föreslås av Sparrow Wallet, kontrollera den på din Trezors skärm. Denna metod gör att du kan bekräfta att den Address som visas på Sparrow inte är bedräglig och att Hardware Wallet verkligen har den privata nyckel som behövs för att därefter spendera de bitcoins som är säkrade med denna Address. Detta hjälper dig att undvika flera typer av attacker.



För att utföra denna kontroll klickar du på knappen "*Display Address*".



![Image](assets/fr/32.webp)



Kontrollera att den Address som visas på din Trezor stämmer överens med den som visas på Sparrow Wallet. Det är också lämpligt att utföra denna kontroll strax innan du kommunicerar din Address till avsändaren, för att vara säker på att den är giltig. Du kan trycka på högerknappen för att bekräfta.



![Image](assets/fr/33.webp)



Du kan också lägga till en "*Label*" för att beskriva källan till bitcoins som kommer att säkras med denna Address. Detta är en bra praxis som gör att du kan hantera dina UTXO:er bättre.



![Image](assets/fr/34.webp)



Du kan sedan använda denna Address för att ta emot bitcoins.



![Image](assets/fr/35.webp)



## Hur skickar jag bitcoins med Trezor Model One?



Nu när du har fått dina första Satss i din Model One-säkrade Wallet kan du spendera dem också! Anslut din Trezor till din dator, starta Sparrow Wallet och gå sedan till fliken "*Sänd*" för att skapa en ny transaktion.



![Image](assets/fr/36.webp)



Om du vill *Coin Control*, dvs. välja specifikt vilka UTXO:er som ska användas i transaktionen, går du till fliken "*UTXO:er*". Välj de UTXO:er du vill använda och klicka sedan på "*Send Selected*". Du kommer att omdirigeras till samma skärm på fliken "*Send*", men med dina UTXO:er redan valda för transaktionen.



![Image](assets/fr/37.webp)



Ange destinationen Address. Du kan också ange flera adresser genom att klicka på knappen "*+ Add*".



![Image](assets/fr/38.webp)



Skriv ner en "*Label*" för att komma ihåg syftet med denna kostnad.



![Image](assets/fr/39.webp)



Välj det belopp som ska skickas till denna Address.



![Image](assets/fr/40.webp)



Justera avgiftssatsen för din transaktion enligt den aktuella marknaden. Du kan t.ex. använda [Mempool.space] (https://Mempool.space/) för att välja en lämplig avgiftssats.



Kontrollera att alla dina transaktionsparametrar är korrekta och klicka sedan på "*Create Transaction*".



![Image](assets/fr/41.webp)



Om allt är till belåtenhet klickar du på "*Finalize Transaction for Signing*".



![Image](assets/fr/42.webp)



Klicka på "*Signera*".



![Image](assets/fr/43.webp)



Klicka på "*Sign*" bredvid din Trezor Model One.



![Image](assets/fr/44.webp)



Kontrollera transaktionsparametrarna på din Hardware Wallet-skärm, inklusive mottagarens mottagande Address, det skickade beloppet och avgiften. När transaktionen har verifierats på Trezor högerklickar du för att signera den.



![Image](assets/fr/45.webp)



Din transaktion är nu signerad. Kontrollera en sista gång att allt är OK och klicka sedan på "*Broadcast Transaction*" för att sända den i Bitcoin-nätverket.



![Image](assets/fr/46.webp)



Du hittar den på fliken "*Transaktioner*" i Sparrow Wallet.



![Image](assets/fr/47.webp)



Grattis, du är nu uppdaterad om den grundläggande användningen av Trezor Model One med Sparrow Wallet! För att ta saker ett steg längre rekommenderar jag denna omfattande handledning om att använda en Hardware Wallet Trezor med en passphrase BIP39 för att förstärka din säkerhet :



https://planb.network/tutorials/wallet/backup/trezor-passphrase-0474b5bf-496f-4f97-aefe-445368fdca42

Om du tyckte att den här handledningen var användbar skulle jag vara tacksam om du lämnar en Green-tumme nedan. Dela gärna den här artikeln på dina sociala nätverk. Tack så mycket!