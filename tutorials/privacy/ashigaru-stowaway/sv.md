---
name: Ashigaru - fripassagerare
description: Hur gör jag en Payjoin-transaktion på Ashigaru?
---
![cover](assets/cover.webp)



> *Tvinga blockchain-spioner att ompröva allt de tror att de vet.*

Payjoin är en Bitcoin-transaktionsstruktur som är utformad för att förbättra användarnas konfidentialitet genom att involvera direkt samarbete med betalningsmottagaren. Det finns flera implementeringar för att underlätta genomförandet och automatisera processen. Den mest kända av dessa är utan tvekan Stowaway, som ursprungligen utvecklades av Samurai Wallet-teamet och nu är integrerad i fork Ashigaru.



## Hur fungerar Stowaway?



Som tidigare nämnts integrerar Ashigaru ett PayJoin-verktyg som heter "Stowaway". Detta finns tillgängligt i Ashigaru-appen på Android. För att en Payjoin ska kunna genomföras måste mottagaren (som också tar på sig rollen som medarbetare) använda programvara som är kompatibel med Stowaway, dvs. för närvarande endast Ashigaru.



Stowaway bygger på en kategori av transaktioner som Samurai kallade "Cahoots". En Cahoot är en samarbetstransaktion mellan flera användare, som innebär ett utbyte av information utanför Bitcoin-blockkedjan. Ashigaru erbjuder för närvarande två Cahoots-verktyg: Stowaway (Payjoins) och StonewallX2.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b

Cahoots-transaktioner kräver utbyte av delvis signerade transaktioner mellan användare. Den här processen kan vara lång och tråkig, särskilt när den utförs på distans. Det är dock fortfarande möjligt att göra detta manuellt, om medarbetarna befinner sig på samma plats. Konkret handlar det om att skanna fem QR-koder i följd, som utväxlas mellan de två deltagarna.



På avstånd blir denna metod alltför komplicerad. För att råda bot på detta har Samourai utvecklat ett Tor-baserat krypterat kommunikationsprotokoll kallat "*Soroban*". Tack vare Soroban är de utbyten som krävs för en Payjoin automatiserade och sker i bakgrunden.



Dessa krypterade kommunikationer kräver en anslutning och autentisering mellan Cahoot-deltagarna. Det är därför Soroban förlitar sig på användarnas Paynyms. Om du ännu inte är bekant med hur Paynyms fungerar, ta en titt på denna dedikerade handledning för att lära dig mer:



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

I ett nötskal är en Paynym en unik identifierare som är kopplad till din wallet och som gör det möjligt för dig att aktivera olika funktioner, inklusive krypterade utbyten. Den har formen av en identifierare som åtföljs av en illustration. Här är till exempel den som jag använder på Testnet:



![Image](assets/fr/01.webp)



**Sammanfattningsvis





- payjoin" = Specifik transaktionsstruktur för samarbete;





- `Stowaway` = Payjoin-implementering tillgänglig på Ashigaru ;





- "Kahoots" = Samourais namn på alla deras typer av samarbetstransaktioner, särskilt Payjoin "Stowaway", som idag tagits över på Ashigaru ;





- soroban = Krypterat kommunikationsprotokoll etablerat på Tor som möjliggör samarbete med andra användare i en `Cahoots`-transaktion;





- paynym" = Unik wallet-identifierare som används för att upprätta kommunikation med en annan användare på "Soroban", för att genomföra en "Chahoots"-transaktion.



För en mer djupgående titt på hur Payjoins fungerar och deras användbarhet i onchain-sekretess rekommenderar jag den här andra handledningen:



https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

## Hur skapar jag en förbindelse mellan Paynyms?



För att komma igång måste du naturligtvis installera Ashigaru och skapa en :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

För att genomföra en Cahoots-transaktion på distans, inklusive en PayJoin (*Stowaway*) via Ashigaru, måste du först "följa" den användare du vill samarbeta med, med hjälp av dennes Paynym. När det gäller en fripassagerare innebär detta att du följer den person som du vill skicka bitcoins till. Om du ännu inte vet hur man följer en annan Paynym hittar du den detaljerade proceduren i denna handledning :



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## Hur gör jag en Payjoin på Ashigaru?



För att genomföra en Stowaway-transaktion klickar du på bilden av din Paynym längst upp till vänster på skärmen och öppnar sedan menyn `Collaborate`. Den person som deltar i transaktionen med dig måste göra samma sak, såvida ni inte utbyter QR-koder personligen.



![Image](assets/fr/02.webp)



Du har två alternativ: välj `Initiate` om du är avsändare av betalningen, eller `Participate` om du är betalningsmottagare för denna payjoin.



![Image](assets/fr/03.webp)



Om du är mottagaren är proceduren mycket enkel. För samarbete på distans via Soroban-nätverket klickar du på `Participate`, väljer det konto du vill använda och trycker sedan på `LISTEN FOR CAHOOTS REQUESTS` för att invänta den begäran som betalaren skickar.



![Image](assets/fr/04.webp)



För personligt samarbete via QR-kodskanning går du till startsidan i din wallet, trycker på QR-kodsikonen högst upp på skärmen och skannar sedan QR-koden som tillhandahålls av betalaren som initierar transaktionen.



![Image](assets/fr/05.webp)



Om du har rollen som betalare, dvs. den som initierar transaktionen, går du till menyn "Collaborate" och väljer sedan "Initiate".



![Image](assets/fr/06.webp)



För transaktionstyp, eftersom vi vill göra en Payjoin Stowaway, väljer du detta alternativ.



![Image](assets/fr/07.webp)



Du kan sedan välja mellan samarbete online (*Cahoots* via *Soroban*) eller ansikte mot ansikte, med utbyte av QR-koder.



![Image](assets/fr/08.webp)



### Cahoots online



Om du har valt alternativet `Online` väljer du mottagaren från de Paynyms du följer.



![Image](assets/fr/09.webp)



Klicka på `Set up transaction` och välj sedan det konto från vilket du vill göra utlägget.



![Image](assets/fr/10.webp)



På nästa sida anger du transaktionsuppgifterna: det belopp som ska skickas till mottagaren och debiteringsgraden. Det finns ingen anledning att ange en mottagningsadress, eftersom mottagaren kommer att sända den själv under PSBT-utbyten.



Klicka sedan på "Granska transaktionsinställningar".



![Image](assets/fr/11.webp)



Kontrollera informationen noggrant, se till att din samarbetspartner lyssnar på *Cahoots*-förfrågningarna och klicka sedan på den gröna knappen `BEGIN TRANSACTION` för att inleda utbytet av PSBTs via Soroban.



![Image](assets/fr/12.webp)



Vänta tills båda deltagarna har signerat transaktionen och sänd den sedan i Bitcoin-nätverket.



![Image](assets/fr/13.webp)



### Diskussioner ansikte mot ansikte



Om du vill utföra växlingen personligen väljer du transaktionstypen `STONEWALL X2` och sedan alternativet `In Person / Manual`.



![Image](assets/fr/14.webp)



Klicka på `Set up transaction` och välj sedan det konto från vilket du vill göra utlägget.



![Image](assets/fr/15.webp)



På nästa sida anger du transaktionsuppgifterna: beloppet som ska skickas till mottagaren och avgiftssatsen. Du behöver inte ange någon mottagaradress, eftersom mottagaren själv skickar den vid PSBT-utbyten.



Klicka sedan på "Granska transaktionsinställningar".



![Image](assets/fr/16.webp)



Kontrollera detaljerna och tryck sedan på den gröna knappen `BEGIN TRANSACTION` för att börja växla PSBTs via QR-kodskanning.



![Image](assets/fr/17.webp)



Utbytet sker genom att skanningen växlar med medarbetaren: klicka på "Visa QR-kod" för att visa din QR-kod för din medarbetare, som skannar den. Han klickar sedan på "Visa QR-kod" för att visa sin, och du skannar den med "Starta QR-skanner". Upprepa denna process tills alla fem utbytesstegen har slutförts.



![Image](assets/fr/18.webp)



När alla utbyten har slutförts kontrollerar du transaktionsinformationen och frigör den genom att dra i den gröna pilen längst ned på skärmen.



![Image](assets/fr/19.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/82efd3700bba87b0f172e9cc045e441b38622c95a60df9f39a21f63eb4590a96). Dess struktur är som följer:



![Image](assets/fr/20.webp)



*Kredit: [mempool.space](https://mempool.space/)*



Om vi analyserar denna transaktion ser vi min UTXO på 164 211 sats` på inmatningssidan, samt UTXO på 190 002 sats` som tillhör den faktiska mottagaren av betalningen. På utmatningssidan får jag en UTXO på 63 995 sats`, medan mottagaren får en UTXO på 290 002 sats`. Om vi jämför input och output kan vi se att mottagaren verkligen har tjänat 100 000 sats`, vilket motsvarar beloppet för min faktiska betalning, och att jag har förlorat 100 000 sats`, till vilket jag har lagt till kostnaderna för mining.



Självklart kan jag beskriva denna struktur eftersom jag själv byggt upp transaktionen. Men för en utomstående observatör är det i allmänhet omöjligt att avgöra vilka UTXO:er som tillhör vilken deltagare, varken i inmatningar eller utmatningar.



För att fördjupa din kunskap om onchain-sekretesshantering på Bitcoin rekommenderar jag att du tar min BTC 204-utbildning på Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c