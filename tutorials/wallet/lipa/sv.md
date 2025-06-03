---
name: Lipa
description: Konfigurera och använda Lipa Lightning Mobile Wallet
---
![cover](assets/cover.webp)


En Bitcoin Lightning Wallet är en mobilapplikation som möjliggör omedelbara transaktioner till låg kostnad på Bitcoin:s Lightning Network. Till skillnad från transaktioner på den huvudsakliga Blockchain (On-Chain) är Lightning-betalningar nästan ögonblickliga och kräver minimala avgifter, vilket gör dem särskilt lämpliga för små, vardagliga betalningar.


Lightning-plånböcker, liksom alla mobila plånböcker, betraktas som "Hot"-plånböcker eftersom de är anslutna till internet. De är därför främst avsedda för att hantera små summor pengar för dina dagliga utgifter. För större belopp är det bättre att använda säkrare lagringslösningar, t.ex. hårdvaruplånböcker.


Om du vill lära dig mer om Lightning Network och förstå hur den fungerar tekniskt rekommenderar jag att du går den här kursen:


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

I den här handledningen tar vi en titt på **Lipa**, en enkel och effektiv Lightning Wallet som utvecklats i Schweiz.


## Introduktion av Lipa


Lipa är en icke frihetsberövande Lightning Wallet som kännetecknas av sin enkla användning och snygga Interface. Den är utvecklad av ett schweiziskt team och betonar sekretess och användarvänlighet för nybörjare.


Viktiga egenskaper inkluderar:




- Intuitiv användare Interface
- Autonom hantering av blixtkanaler
- Stöd för LNURL-protokoll
- Möjlighet att köpa bitcoins direkt i applikationen


## Installera och konfigurera Lipa


Det första steget är att ladda ner Lipa-appen. För tillfället är den endast tillgänglig på iOS :




- [För Apple] (https://apps.apple.com/app/lipa-Bitcoin-lightning/id1602180066)


Android-versionen är för närvarande under utveckling och kommer att finnas tillgänglig inom kort.


![Installation de Lipa](assets/fr/01.webp)


När du har startat programmet kommer du till startskärmen, där du har två alternativ:




- Skapa en ny Wallet
- Återställ en befintlig Wallet från en säkerhetskopia


När du har valt ditt alternativ uppmanar programmet dig att aktivera aviseringar. Detta steg är viktigt, eftersom aviseringar är nödvändiga för :




- Få aviseringar när betalningar har mottagits, även när ansökan är stängd
- Bli informerad om stegen för att köpa Bitcoin via deras integrerade lösning


Programmet presenterar sedan sina huvudfunktioner genom en serie introduktionsskärmar:




- Sömlös mottagning av betalningar**: Användare kan ta emot Bitcoin-betalningar även när applikationen är stängd, vilket garanterar tillförlitlighet och bekvämlighet.
- Lightning-adresser utan förmyndarskap**: Lipa stöder nu Lightning-adresser utan förmyndare, vilket förbättrar integriteten och säkerheten genom att ge användarna full kontroll över sina bitcoins.
- Kontroll över analytiska data** : Eftersom transparens och sekretess är av största vikt kan användarna se vilka typer av data som samlas in och välja hur de vill dela dem.
- Skicka via telefonnummer**: Inget behov av komplexa adresser - välj bara en kontakt, ange beloppet och skicka bitcoins direkt till deras telefonnummer.


Applikationen drar också nytta av kontinuerliga förbättringar när det gäller stabilitet, säkerhet och tillförlitlighet, för att garantera en optimal användarupplevelse.


## Applikationsnavigering


Lipa's Interface är organiserad kring 4 huvudflikar som nås via navigeringsfältet längst ner på skärmen:


![Navigation principale](assets/fr/02.webp)




- Hem**: Visar ditt aktuella saldo och din transaktionshistorik
- Skanner**: Gör att du kan skanna QR-koder för att göra betalningar
- Karta**: Visar en interaktiv karta över Bitcoin-godkännande företag i ditt område
- Inställningar**: Tillgång till programinställningar, säkerhetskopiering och preferenser


En ytterligare meny kan nås genom att dra ner startskärmen:


![Menu supplémentaire](assets/fr/03.webp)


Denna gest avslöjar ytterligare funktioner som :




- Köpa bitcoins
- On-Chain Bitcoin deposition
- Skapa Lightning-fakturor för att ta emot bitcoins
- Blixten Invoice betalning


## Spara din Wallet


För att säkerhetskopiera din Wallet går du till fliken "Inställningar" och väljer "Återställningsfras". Lipa använder en återställningsfras som det är viktigt att skriva ner noggrant på ett fysiskt medium (papper, metall). Denna fras är det enda sättet att återfå dina pengar om din telefon går förlorad eller blir stulen. För att validera din säkerhetskopia kommer applikationen att be dig att bekräfta 3 slumpmässiga ord från din fras.


![Backup](assets/fr/04.webp)


För mer information om hur du säkerhetskopierar och hanterar din återställningsfras på rätt sätt rekommenderar jag starkt att du följer den här andra handledningen, särskilt om du är nybörjare:


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Ta emot bitcoins


För att ta emot bitcoins har du två alternativ. För att komma åt dessa alternativ, gå tillbaka till startskärmen och dra ner skärmen. Då kan du antingen :




- Välj "Överför BTC" för att ta emot bitcoins On-Chain. Sedan skannar du bara QR-koden med din andra Wallet och slutför transaktionen.
- Välj "Request" för att ta emot via Lightning Network och ange det belopp du vill ta emot.


I båda fallen måste du betala en avgift som motsvarar 0,4% av beloppet, eller cirka 2 500 Sats om ansökan måste öppna en ny betalningskanal (vilket oundvikligen kommer att vara fallet för den första betalningen).


![Recevoir des bitcoins on chain](assets/fr/05.webp)


![Recevoir des bitcoins lightning](assets/fr/06.webp)


## Skicka bitcoins


För att skicka bitcoins, gå till startskärmen, dra ner skärmen och välj "Pay". Sedan helt enkelt antingen :




- delta i en blixt LNURL Address
- skanna en blixt QR-kod för att göra betalningen.


Du kan också gå till den andra fliken längst ner på skärmen för att skanna en QR-kod direkt.


![Envoi de bitcoins](assets/fr/07.webp)


## Köpa bitcoins


Lipa erbjuder möjligheten att köpa bitcoins direkt i applikationen mot en avgift på 1,5%. För att göra ett köp, gå till startskärmen och dra ner för att visa menyn. Välj sedan "Köp BTC". Tre introduktionsskärmar kommer att vägleda dig genom köpprocessen.


![Menu d'achat](assets/fr/08.webp)


Ange sedan bara bankuppgifterna för det konto som du ska använda för att göra köpet. Välj din valuta och ange din e-postadress Address.


Efter laddningsskärmen hittar du referensnumret som ska ingå i den överföring du ska göra, samt bankuppgifterna för Exchange.


![Sélection du montant](assets/fr/09.webp)


Allt du behöver göra är att använda din bank för att överföra önskat belopp, ställa in överföringen genom att ange den RIB som tidigare hämtats och ange referensen vid transaktionstillfället så att Lipa kan associera denna bankrörelse med din Lipa Wallet.


![Confirmation d'achat](assets/fr/10.webp)


## Fördelar och nackdelar


### Fördelar




- Intuitiv Interface
- Korrekta serviceavgifter
- Ej depåförvaring
- Integrerad inköpslösning Bitcoin
- Integration av BTCmap
- Stöd för NFC


### Nackdelar




- Det är inte möjligt att skicka bitcoins on chain
- Något längre än genomsnittlig betalning


Lipa är ett utmärkt val för att komma igång med Lightning Network och passar särskilt bra för användare som letar efter en enkel lösning för vardagliga betalningar. Dess användarvänlighet och överskådliga Interface gör den till en idealisk Wallet för nybörjare, samtidigt som den erbjuder de viktigaste funktionerna för daglig Lightning-användning.


## Resurser




- [Lipas officiella webbplats](https://lipa.swiss/)
- [Lipa support](https://getlipa.atlassian.net/servicedesk/customer/portal/1)