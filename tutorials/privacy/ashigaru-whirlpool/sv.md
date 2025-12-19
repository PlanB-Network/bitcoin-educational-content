---
name: Ashigaru - Whirlpool Coinjoin
description: Hur gör jag coinjoins på Ashigaru-applikationen?
---

![cover](assets/cover.webp)



"*en bitcoin wallet för gatorna*"



I den här handledningen lär du dig vad en coinjoin är och hur man gör en med Ashigaru Terminal-applikationen och Whirlpool-implementeringen, ett coinjoin-protokoll som ärvts från Samourai Wallet.



## Hur Whirlpool-kopplingarna fungerar



I den här handledningen kommer jag inte att gå tillbaka över begreppet coinjoin, dess användbarhet eller den teoretiska driften av Whirlpool, eftersom dessa ämnen redan förklaras i detalj i del 5 av BTC 204-utbildningskursen på Plan ₿ Academy. Om du ännu inte har behärskat driften av Whirlpool eller principen om en coinjoin, rekommenderar jag starkt att du konsulterar den här delen 5 innan du fortsätter :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Här är dock några snabba fakta och siffror som kan komma väl till pass.



Whirlpool-kompatibla portföljer använder 4 separata konton för att uppfylla behoven i coinjoin-processen:




- Kontot **Deposit**, identifierat med index `0'` ;
- Kontot **Bad Bank** (eller *doxxic exchange*), identifierat med indexet `2,147,483,644'` ;
- Kontot **Premix**, identifierat genom indexet "2 147 483 645" ;
- Kontot **Postmix**, identifierat genom indexet "2 147 483 646".



På Ashigaru, i november 2025, finns två poolvalörer tillgängliga (den här listan kommer förmodligen att utvecklas under de kommande månaderna: så kom ihåg att kontrollera värdena när du läser):




- 0.25 BTC`, med en anmälningsavgift på `0,0125 BTC`;
- 0.025 BTC, med en anmälningsavgift på 0,00125 BTC.



Varje mixningscykel kan involvera mellan 5 och 10 UTXO:er i in- och utmatning.



![Image](assets/fr/01.webp)



## Krav på programvara



För att göra coinjoins med Whirlpool behöver du tre separata program:





- Ashigaru Terminal**, som låter dig hantera dina coinjoins direkt från din dator;



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add



- Ashigaru Wallet**, applikationen på din smartphone med vilken du kan spendera dina bitcoins i *postmix* från var som helst ;



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f



- Dojo**, en Bitcoin-nodimplementering som garanterar dig en suverän anslutning till nätverket, utan beroende av en tredjepartsserver.



https://planb.academy/tutorials/node/bitcoin/dojo-aa818a21-e701-48a2-8421-63c6186ed23f

Installera vart och ett av dessa verktyg genom att följa deras respektive handledning, sedan kan du börja göra dina första coinjoins.



## Ta emot bitcoins



När du har skapat din portfölj börjar du med ett enda konto, som identifieras med indexet "0". Detta är kontot `Deposit`. Det är till detta konto som du skickar bitcoins avsedda för coinjoins. Du kan ta emot dem antingen via Ashigaru-applikationen (se del 5 i den dedikerade handledningen) eller via Ashigaru Terminal (även detaljerad i del 5 i den dedikerade handledningen).



När ditt insättningskonto innehåller minst det belopp som behövs för att delta i den minsta poolen (plus serviceavgifter och det minimum som krävs för att täcka mining-kostnader) är du redo att initiera dina första coinjoins.



![Image](assets/fr/02.webp)



## Gör Tx0



När pengarna har kommit in på ditt insättningskonto och transaktionen har bekräftats, kan du starta coinjoin-processen. För att göra detta, på Ashigaru Terminal, öppna `Wallets` menyn och välj sedan din wallet. Om din wallet är låst kommer programvaran att be dig om ditt lösenord och passphrase.



![Image](assets/fr/03.webp)



Välj sedan kontot `Deposit`.



![Image](assets/fr/04.webp)



Gå till menyn `UTXOs`.



![Image](assets/fr/05.webp)



Här ser du en lista över alla UTXO:er på ditt insättningskonto. Välj de som du vill skicka i coinjoin-cyklerna.



För större sekretess och för att undvika *Common Input Ownership Heuristic (CIOH)* rekommenderas att endast en UTXO används per inmatning i Whirlpool (en detaljerad förklaring av denna princip finns i BTC 204).



Tryck på tangenten `ENTER` på tangentbordet för att välja en UTXO: en asterisk `(*)` visas bredvid den för att visa att den är vald.



![Image](assets/fr/06.webp)



Klicka sedan på knappen `Mix Selected`.



![Image](assets/fr/07.webp)



Om du har en UTXO som är tillräckligt stor för att delta i någon av de två tillgängliga poolerna kan du välja destinationspool med hjälp av pilarna. På den här sidan ser du detaljerna för din Tx0 :




- antalet UTXO som kommer att ingå i poolen;
- de olika avgifter som tillämpas (serviceavgifter och mining-avgifter) ;
- beloppet av den *doxiska förändringen*.



Kontrollera informationen noggrant och klicka sedan på `Broadcast` för att sända Tx0.



![Image](assets/fr/08.webp)



Ashigaru kommer då att visa TXID för din Tx0, vilket bekräftar att transaktionen har sänts ut i nätverket.



![Image](assets/fr/09.webp)



## Göra coinjoins



När Tx0 har sänts, gå tillbaka till startsidan för ditt inlåningskonto, klicka sedan på "Konton" och välj "Premix"-kontot.



![Image](assets/fr/10.webp)



I `UTXOs`-menyn ser du de olika utjämnade delarna, redo att gå in i coinjoin-cyklerna. Så snart Tx0 är bekräftad kommer Ashigaru Terminal automatiskt att starta sin första blandningscykel.



![Image](assets/fr/11.webp)



När Tx0 har bekräftats kommer den första coinjoin-transaktionen att skapas och sändas automatiskt av Ashigaru Terminal. Genom att gå till `Konton > Postmix > UTXOs`, kan du se dina utjämnade UTXOs, i väntan på bekräftelse av deras första cykel.



![Image](assets/fr/12.webp)



Du kan nu låta Ashigaru Terminal köra i bakgrunden: den kommer att fortsätta att mixa och remixa dina spår automatiskt.



## Färdigställande av sammanfogningar



Nu kan du låta dina mynt remixa sig själva automatiskt. Whirlpool-modellen innebär att det inte finns några extra avgifter för remixning: inga serviceavgifter, inga mining-avgifter. Så att låta dina mynt delta i fler blandningscykler kan bara gynna din konfidentialitet.



För en bättre förståelse av denna mekanism och hur många cykler det är värt att vänta på rekommenderar jag att du läser den här artikeln:



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

För att se antalet remixer som utförts av vart och ett av dina verk, öppna menyn `UTXOs` i `Postmix`-kontot.



![Image](assets/fr/13.webp)



För att spendera dina blandade mynt, gå till Ashigaru-applikationen, som använder samma wallet som din Ashigaru Terminal-programvara. Den wallet som visas vid öppnandet motsvarar ditt `Deposit`-konto. För att komma åt kontot "Postmix", som innehåller dina blandade UTXO, klickar du på symbolen Whirlpool i det övre högra hörnet.



![Image](assets/fr/14.webp)



På det här kontot ser du alla dina mynt som för närvarande blandas. För att spendera dem trycker du på symbolen `+` längst ner till höger på skärmen och väljer sedan `Sänd`.



![Image](assets/fr/15.webp)



Fyll i detaljerna för din transaktion: mottagarens adress, beloppet som ska skickas och, om du vill, välj en specifik transaktionsstruktur för att ytterligare förbättra din sekretess (se motsvarande handledning).



![Image](assets/fr/16.webp)



Kontrollera noggrant transaktionsuppgifterna och dra sedan pilen längst ned på skärmen för att bekräfta sändningen.



![Image](assets/fr/17.webp)



Din transaktion har signerats och sänts ut i Bitcoin-nätverket.



![Image](assets/fr/18.webp)



## Spend Doxxic Förändring



Kom ihåg det: Whirlpool:s modell är baserad på utjämningen av dina pjäser vid Tx0, innan de går in i poolerna. Det är denna mekanism som bryter spårningen av UTXO. Enligt min mening är detta den mest effektiva coinjoin-modellen, men den har en nackdel: den genererar en * förändring* som inte går igenom coinjoin-processen.



Denna förändring motsvarar en UTXO som skapats för varje Tx0. Den isoleras i ett specifikt konto som heter "Doxxic Change" eller "Bad Bank", beroende på programvaran, för att undvika att den används med dina andra UTXO:er. Detta är mycket viktigt eftersom dessa UTXO:er inte har blandats: deras spårbarhetslänkar förblir intakta och de kan äventyra din konfidentialitet genom att upprätta en koppling mellan dig och din coinjoin-aktivitet. Så hantera dem med försiktighet och **använd dem aldrig tillsammans med andra UTXO**, oavsett om de är blandade eller inte. Att kombinera en giftig UTXO med en blandad UTXO kommer att utplåna alla integritetsvinster som du har fått från coinjoining.



För tillfället erbjuder Ashigaru inte direktåtkomst till detta `Doxxic Change`-konto (åtminstone har jag inte hittat det). Denna funktion kommer förmodligen att läggas till i en framtida uppdatering. Under tiden är det enda sättet att hämta dessa medel att importera din seed till Sparrow Wallet. Den senare kommer normalt automatiskt att upptäcka att detta är en wallet som används med Whirlpool och ge dig tillgång till alla fyra konton, inklusive `Doxxic Change`-kontot. Du kan sedan spendera dessa UTXO:er som vanliga bitcoins från Sparrow.



Här är flera möjliga strategier för att hantera din utländska valuta UTXOs från coinjoins utan att äventyra din integritet:





- Blanda dem i mindre pooler:** Om din toxiska UTXO är tillräckligt stor för att gå med i en mindre pool är detta i allmänhet det bästa alternativet. Var dock försiktig så att du aldrig slår samman flera toxiska UTXO:er för att uppnå detta, eftersom detta kommer att skapa en länk mellan dina olika poster i Whirlpool.





- Markera dem som icke spenderbara:** Ett annat försiktigt tillvägagångssätt är att helt enkelt behålla dem som de är på sitt separata konto och lämna dem orörda. Detta förhindrar att du av misstag spenderar dem. Om värdet på bitcoin ökar kan nya pooler som är anpassade till deras storlek öppnas.





- Gör donationer:** Du kan välja att förvandla dessa giftiga UTXO:er till donationer till Bitcoin-utvecklare, öppen källkodsprojekt eller föreningar som accepterar BTC. Detta gör att du kan göra dig av med dem på ett användbart sätt och samtidigt stödja ekosystemet.





- Köp förbetalda presentkort eller Visa-kort:** Plattformar som [Bitrefill](https://www.bitrefill.com/) låter dig byta dina bitcoins mot presentkort eller omladdningsbara Visa-kort som kan användas i butiker. Detta kan vara ett enkelt och diskret sätt att spendera dina giftiga UTXO.





- Byt dem mot Monero:** Samourai Wallet brukade erbjuda en nu nedlagd BTC / XMR atombytestjänst. Om en liknande tjänst finns (jag känner inte till någon personligen) är det en utmärkt lösning för att isolera dessa UTXO: er, konvertera dem till Monero och sedan så småningom skicka tillbaka dem till Bitcoin. Denna metod var dock dyr och beroende av tillgänglig likviditet.





- Överför dem till Lightning Network:** Att överföra dessa UTXO:er till Lightning Network för att dra nytta av reducerade transaktionsavgifter är ett potentiellt intressant alternativ. Denna metod kan dock avslöja viss information beroende på hur du använder Lightning, och bör därför användas med försiktighet.



## Hur kan jag få reda på kvaliteten på våra coinjoin-cykler?



För att en coinjoin ska vara verkligt effektiv måste den uppvisa en hög grad av enhetlighet mellan inkommande och utgående belopp. Denna enhetlighet ökar antalet möjliga tolkningar för en utomstående observatör, vilket i sin tur ökar osäkerheten om transaktionen. För att mäta denna osäkerhet använder vi begreppet entropi som tillämpas på transaktionen. Whirlpool-modellen är erkänd som en av de mest effektiva i detta avseende, eftersom den garanterar utmärkt homogenitet mellan deltagarna. För en mer djupgående titt på denna princip rekommenderar jag att du läser det sista kapitlet i del 5 i BTC 204-utbildningskursen.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Prestanda för flera coinjoin-cykler mäts genom storleken på de uppsättningar i vilka ett mynt är gömt. Dessa uppsättningar definierar vad som kallas *anonsets*. Det finns två typer: den första mäter sekretess inför retrospektiv analys (från nutid till dåtid) och den andra mäter motstånd mot prospektiv analys (från dåtid till nutid). För en fullständig förklaring av dessa två indikatorer, läs följande handledning (eller, än en gång, BTC 204-utbildningskursen):



https://planb.academy/tutorials/privacy/analysis/remix-whirlpool-2b887bd9-8a6a-4dca-8aa9-a1c33682b0aa

## Hur hanterar man postmixen?



Efter att ha kört flera coinjoin-cykler är den bästa strategin att behålla dina UTXO:er på kontot `Postmix` och låta dem remixas på obestämd tid tills du verkligen behöver spendera dem.



Vissa användare föredrar att överföra sina blandade bitcoins till en wallet som är säkrad av wallet-hårdvara. Detta alternativ är möjligt, men kräver en viss noggrannhet för att säkerställa att den sekretess som förvärvats med coinjoins inte äventyras.



Att slå samman UTXO:er är det vanligaste felet. Det är viktigt att aldrig kombinera blandade UTXO:er med oblandade UTXO:er i samma transaktion, annars riskerar du att utlösa *Common Input Ownership Heuristic (CIOH)*. Detta innebär en rigorös hantering av dina UTXO:er, särskilt genom tydlig och exakt märkning. Generellt sett är sammanslagning av UTXO:er en dålig metod som ofta leder till förlust av sekretess när den hanteras dåligt.



https://planb.academy/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Du bör också vara försiktig med att konsolidera blandade UTXO:er. Begränsade konsolideringar kan övervägas om UTXO:erna har betydande anonsets, men de minskar oundvikligen din konfidentialitetsnivå. Undvik massiva eller förhastade konsolideringar, som utförs innan ett tillräckligt antal remixer, eftersom de kan skapa inferentiella länkar mellan dina pre- och post-mixstycken. Om du är osäker är det bäst att inte konsolidera UTXO:erna från postmixen utan överföra dem en efter en till wallet-hårdvaran och generera en ny tom mottagningsadress varje gång. Glöm inte att märka varje överförd UTXO.



Vi avråder starkt från att flytta dina UTXO:er efter mixen till portföljer som använder minoritetsskript. Om du till exempel deltog i Whirlpool från en multi-sig-portfölj i `P2WSH`, kommer det att finnas få av dig som delar denna typ av skript. Genom att skicka dina postmix UTXO:er till samma typ av script minskar du din anonymitet avsevärt. Utöver typen av skript kan andra specifika wallet-fingeravtryck äventyra din sekretess, så det bästa du kan göra är att spendera dem från Ashigaru-applikationen.



Slutligen, som med alla Bitcoin-transaktioner, ska du aldrig återanvända en mottagningsadress. Varje betalning måste skickas till en ny, unik, tom adress.



Den enklaste och säkraste metoden är att låta dina blandade UTXO:er vila på sitt "Postmix"-konto, låta dem remixas naturligt och bara spendera dem vid behov från Ashigaru.



Ashigaru- och Sparrow-plånböckerna innehåller ytterligare skyddsåtgärder mot de vanligaste felen i samband med blockkedjeanalys, vilket hjälper dig att bevara sekretessen för dina transaktioner.