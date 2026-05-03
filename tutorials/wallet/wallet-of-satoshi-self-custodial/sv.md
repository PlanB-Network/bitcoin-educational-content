---
name: Wallet of Satoshi - Självförvaltande
description: Ta reda på hur du konfigurerar självförvaringsläget för en Wallet of Satoshi-portfölj
---

![cover](assets/cover.webp)



***Not your keys, not your coins* är mer än ett talesätt, det är en grundläggande princip i Bitcoin, vilket innebär att om du inte kontrollerar de **privata nycklarna** som låser upp dina bitcoins, äger du dem inte riktigt.



Många användare börjar i allmänhet med en **custodial wallet** och migrerar sedan till en **self-custodial wallet**, där de själva kontrollerar sina privata nycklar.


I den här handledningen kommer vi inte att introducera dig till en ny självförvaltande wallet. Istället kommer vi att introducera dig till en ny funktion i ***Wallet of Satoshi*** wallet:or: **det självförvarade läget**.



Syftet med den nya integrationen är att användarna ska kunna behålla kontrollen över sina privata nycklar och samtidigt dra nytta av enkelhet och en smidig användarupplevelse.



Innan vi går in på kärnan i frågan, låt oss ta en stund för att undersöka det speciella självförvarsläge som erbjuds av Wallet of Satoshi (WoS).



## Den speciella egenskapen hos självförvaltarläget



Enkelheten och smidigheten i WoS:s självförvaltande läge eliminerar komplexiteten i att öppna blixtkanaler, administrera noder... Men hur är detta möjligt?



Wallet of Satoshi:s självförvarsläge drivs av **Spark**. Detta är en Layer 2-lösning för Bitcoin, skapad av Lightspark, med hjälp av **statskedjor**-teknik.



Som ett resultat utför du inte dina transaktioner direkt på Lightning Network. Interaktioner mellan **LN**-nätverket och **Spark** sker via **atomiska swappar**.



Till exempel vill Bob betala en Lightning-faktura med WoS. Han överför sina satoshi, men i bakgrunden dirigeras dessa till en **Spark Service Provider (SSP)** på Spark, som i sin tur utför betalningen på Lightning-nätverket.



Omvänt vill Alice erhålla medel direkt från sin WoS-portfölj. I detta fall tar **SSP** emot sats via LN och krediterar omedelbart Alice:s portfölj.



Så det är viktigt att notera att för att dra nytta av WoS enkelhet och smidighet måste du vara beroende av Spark's servrar. Men när det gäller säkerhet, om en SSP blir skadlig eller otillgänglig, har du **unilateral exit**-mekanismen, en säkerhetsåtgärd som gör att du kan återfå dina pengar på Bitcoin on-chain (även om detta kan vara långsamt och kostsamt) , vilket garanterar en självförvarsupplevelse som kan jämföras med den för en privat Lightning-nod.



Med hänsyn till alla dessa parametrar kan du sedan bestämma hur mycket sats du vill behålla i din WoS-förvaring.



Om du är ny på Wallet of Satoshi behöver du naturligtvis ladda ner den mobila wallet-applikationen. Men om du redan använder den och vill veta hur du använder **självförsvarsläget**, gå direkt till avsnittet **konfiguration av självförsvarsläget** i denna handledning.



## Komma igång med Wallet of Satoshi



Gå till din applikationsbutik och ladda ner WoS.



![screen](assets/fr/03.webp)



Öppna programmet när nedladdningen är klar och tryck på **Start**.



![screen](assets/fr/04.webp)



Du kommer att omdirigeras till applikationens huvudgränssnitt. Faktum är att när du öppnar WoS för första gången är portföljen redan funktionell och öppnas systematiskt i förvaringsläge som standard.



![screen](assets/fr/05.webp)



Även om du inte vill använda WoS i custodial-läge rekommenderar vi att du först konfigurerar det. För att göra det, se denna handledning.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Låt oss gå vidare till konfigurationen av vår WoS i självförvar.



## Konfiguration av självbevarelsedrift



Klicka på hamburgermenyn (ikonen med tre staplar) i det övre högra hörnet av huvudgränssnittet.



![screen](assets/fr/06.webp)



I menyn som visas klickar du sedan på undermenyn **Open Self Custody Wallet**.



![screen](assets/fr/07.webp)



WoS berättar omedelbart att * självförvaringsläge kommer med en återställningsfras. Du är också ensam ansvarig för säkerheten för dina medel*.



![screen](assets/fr/08.webp)



Kontrollera knappen "**I Understand**" (1) och tryck sedan på knappen **Open Self Custody Wallet** (2), som visas i ljusgult.



![screen](assets/fr/09.webp)



### Skapa en portfölj för självförvaltare



När du har klickat på knappen **Öppna egenvård Wallet** klickar du på knappen **Skapa en ny Wallet**.



![screen](assets/fr/10.webp)



WoS kommer sedan att skapa en portfölj med egen vårdnad åt dig, återigen i samma applikation. Du kommer att kunna växla mellan **custodial**-läge (tillgängligt i vissa regioner) och **self-custodial**-läge när du vill och när som helst.



![screen](assets/fr/11.webp)



När du har skapat den kommer du att omdirigeras till WoS huvudgränssnitt för självförvaring. Du kommer att märka att det inte finns några skillnader mellan den allmänna översikten och gränssnitten för en WoS custody-portfölj och de för en WoS self-custody-portfölj.



### Spara din mnemotekniska fras



Tryck på ikonen **Keychain + Backup Wallet** som finns högst upp på skärmen mellan Wallet of Satoshi-namnet och hamburgermenyn.



![screen](assets/fr/12.webp)



WoS erbjuder två olika sätt att spara dina 12 ord (mnemonisk fras): **backup via Google Drive** och **manuell backup**.



Även om vi rekommenderar manuell säkerhetskopiering, vilket är det säkraste, visar vi också hur du säkerhetskopierar via Google Drive.



#### Säkerhetskopiering via Google Drive



Klicka på knappen **Google Drive Backup**.



![screen](assets/fr/13.webp)



Om du väljer att säkerhetskopiera med Google Drive finns det en stor risk att ditt Google-konto blir komprometterat. En illvillig person skulle få tillgång till filen som innehåller dina 12 ord och skulle därmed kunna få tillgång till din wallet.



Att lägga till ett lösenord för att kryptera filen som innehåller dina 12 ord är verkligen ett bra sätt att lägga till ett extra säkerhetslager.



Aktivera därför knappen **Kryptera med ett lösenord** i de avancerade alternativen.



![screen](assets/fr/14.webp)



I det nya gränssnittet som visas anger du ett starkt lösenord och bekräftar det sedan igen.



![screen](assets/fr/15.webp)



Det är viktigt att komma ihåg att när du har valt ett lösenord får du inte glömma det eller tappa bort mediet som du har skrivit det på. Om du glömmer eller tappar bort det kommer du aldrig mer att kunna komma åt dina 12 ord och därmed dina pengar.



När du har valt ditt lösenord väljer du ett Google-konto för säkerhetskopian och ger sedan de åtkomster som krävs av WoS.



![screen](assets/fr/16.webp)



![screen](assets/fr/17.webp)



Vänta några sekunder. Bingo! Din säkerhetskopiering har slutförts framgångsrikt.



![screen](assets/fr/18.webp)



Du har alltid möjlighet att göra en extra säkerhetskopia genom att välja den andra säkerhetskopieringsmetoden: manuell säkerhetskopiering.


#### Manuell säkerhetskopiering



Om du väljer manuell säkerhetskopiering rekommenderar vi starkt att du läser den här handledningen, som utforskar bästa praxis för att säkerhetskopiera din minnesfras på ett säkert sätt, så att du inte förlorar tillgången till dina bitcoins.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Tryck på knappen **Manual Backup**.



![screen](assets/fr/19.webp)



I följande gränssnitt påminner WoS dig om några säkerhetsåtgärder som du måste ta hänsyn till innan du fortsätter med den manuella säkerhetskopieringen.



Aktivera knappen **Jag förstår** och tryck på knappen **Nästa**.



![screen](assets/fr/20.webp)



Du kommer då att få se dina 12 ord. Spara dem och klicka sedan på knappen **Nästa**.



![screen](assets/fr/21.webp)



I det nya gränssnittet ska du trycka på orden i rätt ordning.



![screen](assets/fr/22.webp)



Klicka till sist på knappen **Nästa**. Gratulerar till din säkerhetskopiering! Din säkerhetskopiering är nu klar.



![screen](assets/fr/23.webp)



## Återställande av portfölj med självförvaltare



När du vill återställa din WoS-förvaring wallet efter ett telefonbyte eller av någon annan anledning, följer här de steg som ska följas.



För att öppna WoS-portföljen klickar du på hamburgermenyn i det övre högra hörnet av huvudgränssnittet.


I menyn som visas klickar du på undermenyn **Open Self Custody Wallet**.


I det nya gränssnittet som visas trycker du på knappen **Restore Existing Wallet**.



![screen](assets/fr/24.webp)



Välj en återställningsmetod och gå vidare till nästa steg.



![screen](assets/fr/25.webp)



### Återställ via Google Drive



1. Tryck på knappen **Restore From Google Drive**.


2. Välj ett Google-konto och låt WoS hämta återställningsdata som sparats på din Google Drive.


3. Ange sedan ditt krypteringslösenord (om du tidigare har definierat det, förstås) från filen med dina 12 ord.


4. Vänta en stund så att återställningen träder i kraft och du kan komma åt din portfölj igen.



### Manuell restaurering



1. Tryck på knappen **Restore Manually**.


2. Ange sedan de 12 orden i din minnesfras genom att skriva varje ord framför dess startnummer.


3. Vänta några ögonblick så att återställningen träder i kraft och du kan komma åt din portfölj igen.




### Överföring av bitcoins mellan WoS förvaring och WoS egen förvaring



När du har bitcoins (sats) i din WoS-förvaring wallet och skapar en WoS-egenförvaring wallet, kommer du inte att förlora dina medel. Ännu bättre är att du kan överföra dem till din självförvaltande portfölj och vice versa.



För att göra det :


Du kan kopiera din blixt WoS självförvarsadress eller en faktura som du har skapat.



![screen](assets/fr/26.webp)



Öppna nu din vårdnadshavare wallet och tryck på **Envoyer**-knappen.



Klistra sedan in adressen eller fakturan. Tryck **Envoyer** en gång till.



Gå tillbaka till din portfölj med egen förvaring och du kommer att se att du verkligen hade fått pengarna.



![screen](assets/fr/27.webp)



## Sändning och mottagning av bitcoins



När det gäller att skicka och ta emot bitcoins i självförvaringsläge, precis som den allmänna översikten och gränssnitten, skiljer de sig inte från att skicka och ta emot bitcoins via en WoS-förvaring wallet.



Se den grundläggande handledningen om hur du använder Wallet of Satoshi i Plan₿-nätverket.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Du kan nu konfigurera och använda Wallet of Satoshi själv i självförvaltande läge.



Om du tyckte att den här handledningen var användbar, vänligen lämna mig en grön tumme nedan. Tack så mycket!