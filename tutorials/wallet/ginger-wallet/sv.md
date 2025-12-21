---
name: Ginger Wallet
description: Öppen källkod, självförsvar Bitcoin wallet programvara, fork från Wasabi Wallet, integrering av Coinjoins
---
![cover](assets/cover.webp)



Ginger Wallet är en Bitcoin-portfölj med öppen källkod som inte är frihetsberövande och som fokuserar på konfidentialitet och integritet. Den började som fork från Wasabi Wallet (efter version 2.0.7.2 - MIT-licens).



Ginger Wallet behåller Wasabis tekniska arkitektur men lägger till några specifika funktioner. Enligt [Ginger Wallet documentation](https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet) betonar Wasabi **autonomi och kontroll**, medan Ginger fokuserar på **användarvänlighet, säkerhet och en förenklad upplevelse**, vilket gör den tillgänglig för dem som är mindre bekanta med tekniska aspekter.



Ginger Wallet är wallet programvara endast för datorer (ingen mobilapplikation).



## Vad är Coinjoin?



**coinjoin** är en speciell Bitcoin-transaktionsstruktur som sammanför flera deltagare i en enda samarbetstransaktion. Denna mekanism blandar olika användares poster i en gemensam transaktion, vilket gör det extremt svårt - om inte ofta omöjligt, om det görs på rätt sätt - att spåra medel. Som ett resultat blir det nästan omöjligt för en utomstående observatör att med säkerhet identifiera ursprunget och destinationen för de involverade bitcoins, till skillnad från konventionella Bitcoin-transaktioner.



För dig som användare hjälper coinjoin till att bevara din konfidentialitet. Om du till exempel får en donation på 10 000 sats på en Bitcoin-adress kan avsändaren spåra dessa medel och i vissa fall dra slutsatsen att du innehar en större mängd bitcoins eller observera dina aktiviteter. Genom att göra en coinjoin efter denna donation på 10 000 sats bryter du spårbarheten: avsändaren kommer inte längre att kunna härleda någon information om dig från denna betalning.



Chaumian coinjoin erbjuder en hög säkerhetsnivå, eftersom medlen alltid är under användarens exklusiva kontroll. Inte ens operatörerna av de samordnande servrarna kan under några omständigheter avleda deltagarnas bitcoins. Varken användare eller koordinatorer behöver lita på varandra: var och en behåller kontrollen över sina privata nycklar och är ensam behörig att validera transaktioner. Ingen tredje part kan därför tillägna sig dina bitcoins under en coinjoin eller upprätta en direkt länk mellan dina inmatningar och utmatningar.



För att lära dig mer om coinjoin, kolla in Plan ₿ Academy's BTC 204-kurs :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Installera Ginger Wallet



För att installera Ginger Wallet, besök webbplatsen [Ginger Wallet](https://gingerwallet.io).



Tryck på **Download** för att ladda ner rätt version för din dator (Windows / MacOs / Linux).



![screen](assets/fr/03.webp)



Ett annat alternativ är att gå till projektets [GitHub](https://github.com/GingerPrivacy/GingerWallet/releases) för att ladda ner den.



![screen](assets/fr/04.webp)



Kör sedan installationsprogrammet.



![screen](assets/fr/05.webp)




## Parameterinställningar



### Preliminära konfigurationer



Öppna Ginger Wallet och välj det språk du vill använda.



![screen](assets/fr/06.webp)



Redan från början påminner Ginger dig om de kostnader som är förknippade med coinjoin-processen.



![screen](assets/fr/07.webp)



Tryck sedan på **Start** och sedan på **Ny** för att skapa en ny portfölj.



![screen](assets/fr/08.webp)



Spara och bekräfta sedan din seedphrase.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



För ökad säkerhet ger Ginger Wallet dig möjlighet att lägga till en passphrase.



![screen](assets/fr/11.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

När denna passphrase har lagts till kommer den att begäras varje gång du försöker komma åt din portfölj.



![screen](assets/fr/12.webp)



Ginger aktiverar automatiskt standardinställningen **Coinjoin** när du skapar din portfölj. Du informeras om detta och kan sedan anpassa inställningen så att den passar dina behov.



![screen](assets/fr/13.webp)




### Allmänna inställningar



När du har skapat din första portfölj kommer du till Ginger Wallet-gränssnittet.



![screen](assets/fr/14.webp)



Aktivera **Diskret läge** om du vill dölja saldot i dina plånböcker.



![screen](assets/fr/15.webp)



Du kan skapa flera portfolios på Ginger Wallet. Klicka bara på **Lägg till en portfölj**.



![screen](assets/fr/16.webp)



Ginger stöder användning av hårdvaruportföljer via standardgränssnittet Bitcoin Core, även om direkt integration från eller till en hårdvaruportfölj ännu inte är tillgänglig.



Kompatibla hårdvaruportföljer inkluderar (men är inte begränsade till) :




- Blockström Jade
- Kallkort MK4
- Coldcard Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor modell T
- Trezor Safe 3
- etc.



Klicka nu på **Inställningar**.



![screen](assets/fr/17.webp)



Dessa inställningar gäller för programmet i allmänhet och de konfigurationer du gör där kommer att gälla för alla portföljer.



I **Inställningar** har du flikarna :





- Allmänt**



![screen](assets/fr/18.webp)





- Utseende



På den här fliken kan du bland annat ändra språk, valuta och avgiftsvisningsenhet (BTC/Satoshi).



![screen](assets/fr/19.webp)





- Bitcoin**



På den här fliken kan du aktivera Bitcoin Knots så att den körs vid programstart, välja nätverk (Main/RegTest) och laddningsleverantör (Mempool Space/Blockstream info/Full Node), etc.



![screen](assets/fr/20.webp)





- Säkerhetsdetaljer**



På fliken Säkerhet kan du aktivera tvåfaktorsautentisering, aktivera eller avaktivera Tor och till och med inaktivera det när Ginger-programmet stängs.



![screen](assets/fr/21.webp)



**NB** :




- För tvåfaktorsautentisering, se till att din autentiseringsapplikation stöder SHA256-protokollet och 8-siffriga koder. Ginger Wallet kräver en 8-siffrig 2FA-kod för att förbättra säkerheten. Detta längre format gör koden mycket svårare att gissa eller kompromissa med, vilket ger ett bättre skydd mot obehörig åtkomst.
- Som standard passerar all Ginger-nätverkstrafik genom Tor, vilket eliminerar behovet av manuell konfiguration. Om Tor redan är aktivt på ditt system kommer Ginger automatiskt att prioritera det.



Men när du har avaktiverat Tor i inställningarna förblir din integritet i allmänhet bevarad, utom i två situationer:




- under en Coinjoin kan koordinatorn koppla dina in- och utgångar till din IP-adress;
- när du sänder en transaktion kan en illasinnad nod som du ansluter till associera din transaktion med din IP.



Glöm inte att trycka på **Done** (i nedre högra hörnet) varje gång för att spara dina inställningar. Vissa inställningar kräver att Ginger Wallet startas om för att träda i kraft.



Dessutom kan du via sökfältet högst upp i portföljerna söka efter och få tillgång till alla parametrar etc.



![screen](assets/fr/22.webp)




### Konfiguration av portföljen



Det går att skapa flera portföljer i programmet, så att varje portfölj kan konfigureras efter dina behov. Klicka på **tre prickar** framför portföljnamnet och sedan på **Portföljinställningar**.



![screen](assets/fr/23.webp)



Som du kan se kommer du, förutom wallet-parametern, att kunna se dina UTXO:er (lista över tokens du äger), statistik och wallet-information (den utökade offentliga nyckeln, till exempel).



För att återgå till vår portföljkonfiguration, när du klickar på portföljparametrar, kommer du till följande flikar:




- Allmänt** (där du kan ändra portföljens namn) ;



![screen](assets/fr/24.webp)





- Coinjoin** (där du kan anpassa inställningarna för coinjoin för denna wallet) ;



![screen](assets/fr/25.webp)





- Tools** (där du kan kontrollera din seedphrase, synkronisera din portfölj igen eller ta bort den).



![screen](assets/fr/26.webp)




## Ta emot bitcoins



![video](https://youtu.be/cqv35wBDWMQ)



För att ta emot bitcoins i din wallet på Ginger Wallet:




- tryck på **Mottagning** ;



![screen](assets/fr/27.webp)





- Ange namnet på den källa som du vill koppla adressen till. Detta är en märkning för att hålla reda på dina betalningar. Detta har inga on-chain-konsekvenser; det är helt enkelt spårbarhetsinformation som lagras lokalt i din applikation;



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- klicka på den lilla pilen till vänster om **Generate** för att välja adressformat (**SegWit** /**Taproot**), klicka sedan på **Generate** för att generate en adress och QR-kod.



![screen](assets/fr/29.webp)



Denna adress eller QR-kod kommer att användas av din avsändare för att skicka bitcoins till dig.



![screen](assets/fr/30.webp)




## Skicka bitcoins




![video](https://youtu.be/2nf5aAimfhg)



För att göra detta :




- Tryck på knappen **Sänd**;
- ange mottagarens adress, det belopp som ska skickas och en etikett;
- kontrollera transaktionsöversikten och bekräfta att du vill skicka.



![screen](assets/fr/31.webp)




## Spendera bitcoins



Det är lätt att köpa och sälja Bitcoin med Ginger Wallet. I bara några steg kan du spendera dina bitcoins.



### Köpa bitcoins



![video](https://youtu.be/lEqTBzm5MEA)



Ginger Wallet-användare kan köpa bitcoins.





- Tryck på knappen **Köp**. Denna knapp förblir synlig även om wallet är tom.



![screen](assets/fr/32.webp)





- Välj ditt land, eller till och med din stat (i vissa regioner, som Kanada), innan du fortsätter med ett bitcoin-köp. Faktum är att när du klickar på **Köp**-funktionen för första gången måste du också ange din region.



![screen](assets/fr/33.webp)



Tryck på **Continue** för att gå vidare i inköpsprocessen.





- Ange sedan det antal bitcoins du vill köpa i det dedikerade fältet. Du kan också välja transaktionsvaluta.



![screen](assets/fr/34.webp)



Varje valuta har en lägsta och högsta köpgräns. I USD är t.ex. den högsta gränsen 30 000 USD.



Om du redan har gjort ett köp kan du se din transaktionshistorik genom att klicka på knappen **Tidigare beställningar**. En lista över tidigare transaktioner och deras status visas.





- Välj det erbjudande som passar dig bäst.



Nu ser du en lista över alla tillgängliga erbjudanden. För varje erbjudande har du :




 - leverantörens namn (1) ;
 - antalet bitcoins som motsvarar det belopp som tidigare angetts, betalningsmetod och inköpsavgift (2) ;
 - knappen **Accept** (3).



![screen](assets/fr/35.webp)



De avgifter som anges i erbjudandet utgör inte en extra kostnad. De ingår redan i det totala beloppet för erbjudandet.



I det övre högra hörnet av skärmen, märkt **All**, kan du filtrera erbjudanden efter betalningsmetod. Den valda betalningsmetoden är förvald som standard, men kan ändras när som helst.



![screen](assets/fr/36.webp)



Om du hittar ett lämpligt erbjudande klickar du på knappen **Accept** för att gå vidare med köpet. Du kommer då att omdirigeras till säljarens sida, där du kan slutföra transaktionen.



### Sälja bitcoins



Ginger Wallet användare kan sälja Bitcoin. Knappen **Sälj** är endast synlig när det finns tillgängliga medel i portföljen.





- Klicka på **Sälj**.



![screen](assets/fr/37.webp)





- Precis som med alternativet **Buy** måste du, när du använder säljfunktionen för första gången, välja ditt land innan du fortsätter med en bitcoinförsäljning.





- Därefter måste du ange hur många Bitcoins du vill sälja. Du kan ange beloppet i BTC eller i en fiatvaluta som t.ex. US-dollar (USD).





- När du har gjort detta ser du en lista över tillgängliga erbjudanden. Välj ett erbjudande som passar dig och klicka sedan på **Acceptera** för att fortsätta.





- Nu måste du slutföra transaktionen:
 - När du har accepterat ett erbjudande kommer du att omdirigeras till leverantörens sida;
 - Följ anvisningarna på leverantörssidan ;
 - Så småningom kommer du att få en mottagaradress och det exakta beloppet att skicka;
 - Gå sedan tillbaka till Ginger Wallet för att fortsätta processen;
 - När du är tillbaka i Ginger Wallet visas en dialogruta där du kan fortsätta genom att klicka på **Sänd**.



Då öppnas skärmen **Sänd** med mottagarens adress och belopp förifyllda. Du kan också använda knappen **Sänd** på startskärmen. Även om du kan skicka transaktionen manuellt, rekommenderar vi att du slutför den via dialogrutan för en optimerad process.



## Gör en coinjoin på Ginger Wallet



![Vidéo](https://youtu.be/AJe67RDfB1A)



Skydda sekretessen för dina bitcoins med **Coinjoin**, integrerad direkt i Ginger Wallet. wallet använder **WabiSabi**, ett Chaumian coinjoin-protokoll utformat för att underlätta mer tillgängliga och effektiva coinjoins.



Det är upp till dig att välja den coinjoin-strategi (automatisk eller manuell) som passar dig bäst.



Ginger Coinjoin är redo att användas så snart du laddar ner den (inga ytterligare steg krävs). Ginger Coinjoin körs automatiskt i bakgrunden för att skydda din integritet vid varje transaktion. I praktiken kommer Coinjoin-spelaren att dyka upp när du har ett saldo som kan anonymiseras.



När det gäller manuell uppstart av coinjoin är det en operation med ett klick. Starta omgången och vänta på att coinjoin-transaktionen ska byggas och bekräftas. Du kommer att se anonymiseringspoängen i gränssnittet.



Flera mixar kan utföras tills önskad nivå av anonymitet har uppnåtts. Du kan också utesluta vissa delar från mixen.



Som standard använder Ginger sin egen koordinator med alla förkonfigurerade parametrar och garanterade avgifter. Coinjoins av tokens värda mer än 0,03 BTC medför en koordinatoravgift på 0,3% utöver mining avgiften. Registreringar på 0,03 BTC eller mindre, liksom remixer, är undantagna från koordinatoravgifter, även efter en enda transaktion. En betalning som görs med Coinjoin-medel gör det därför möjligt för både avsändare och mottagare att remixa sina mynt utan att ådra sig koordinatoravgifter.



Ginger föredrar coinjoins med fler deltagare framför mindre, snabbare rundor. Större coinjoins erbjuder mer anonymitet, lägre kostnader och större effektivitet i blockutrymmet.




## Säkerhet och bästa praxis



Önskemålet om decentralisering och bevarandet av den personliga integriteten kräver att flera bästa metoder används:




- Förvara alltid din seedphrase på en säker plats utanför nätet;
- Om du förlorar din dator eller misstänker obehörig åtkomst, skapa en ny wallet omedelbart. För över dina pengar till den nya portföljen och radera den gamla;
- Använd en annan adress för varje mottagning för att undvika återanvändning av adresser;
- Ladda alltid ner dina portföljapplikationer uteslutande från det officiella GitHub-kontot eller den officiella webbplatsen.



Nu är du bekant med att använda Ginger Wallet-applikationen för att skicka, ta emot och spendera dina bitcoins.



Om du tyckte att den här handledningen var användbar, vänligen lämna mig en grön tumme nedan. Du är välkommen att dela den här artikeln via dina sociala medieplattformar. Tack så mycket!



Jag föreslår också att du kollar in den här handledningen om hur du använder datorprogrammet Liana för att skicka och ta emot bitcoins, samt implementerar en automatiserad fastighetsplan.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04