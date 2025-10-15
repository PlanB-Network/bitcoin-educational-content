---
name: StashPay
description: Den minimalistiska Bitcoin Wallet för alla
---

![cover](assets/cover.webp)



Användarupplevelsen är en nyckelfaktor för införandet av Bitcoin-lösningar runt om i världen. Att tillhandahålla en smidig, enkel och tekniskt obesvärad upplevelse är prioriteringen för många plånböcker och Exchange-plattformar. I detta avseende sticker StashPay ut för sitt minimalistiska tillvägagångssätt, samtidigt som det visar kraften i Lightning Network.



I den här handledningen tar vi en titt på den här portföljen för att ta reda på hur den fungerar och hur den är idealisk för småföretag eller solopreneurs.



## Att komma igång med StashPay



StashPay är en Lightning self-custodial Wallet som främst är känd för sin minimalistiska, användarcentrerade användarupplevelse.  Med denna Wallet behöver du inte någon teknisk kunskap för att ta emot och skicka dina första satoshis.



StashPay är ett öppen källkodsprojekt som utvecklats i React Native och syftar till att lösa problemet med höga transaktionsavgifter även vid transaktioner på Bitcoin-protokollets huvudkedja. Den finns tillgänglig som en mobilapp på Android- och iOS-plattformar via nedladdningslänkar på [webbplatsen] (https://stashpay.me/).



![introduce](assets/fr/01.webp)



Det är viktigt att ladda ner Android-applikationen från webbplatsen, eftersom den inte finns tillgänglig i Google Play Store.


När nedladdningen är klar ska du ge de nödvändiga behörigheterna så att du kan installera applikationen på din Android-telefon.



När programmet har installerats kommer StashPay att skapa en initial Bitcoin Wallet åt dig första gången du öppnar det. Före varje transaktion rekommenderar vi att du gör en säkerhetskopia av denna Wallet. Nedan hittar du alla våra riktlinjer för att säkerställa att dina återställningsfraser är korrekt säkerhetskopierade.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Gå till StashPay-inställningarna genom att klicka på ikonen "Inställningar" och sedan på alternativet ** Skapa säkerhetskopia**. Godkänn sedan visningen av återställningsfraser. Kopiera inte dina återställningsfraser till telefonens urklipp, eftersom de kan vara tillgängliga för andra bedrägliga applikationer som är installerade på din mobil.



![backup](assets/fr/02.webp)



Du kan också hämta en Bitcoin Wallet som du redan använder genom att klicka på alternativet **Hämta Wallet** och infoga dina 12 eller 24 återställningsord.



### Ta emot dina första satoshis på StashPay



På startskärmen klickar du på knappen **Receive** och ställer in ett belopp som är större än det belopp som anges i rött. I vårt fall kan vi inte ta emot mindre än 0,11 USD med StashPay Wallet.



![receive](assets/fr/03.webp)



När du har definierat beloppet kan du klicka på knappen **Create Invoice** och sedan skanna eller kopiera Invoice för att skicka den till din satoshis-avsändare.



![receive_sats](assets/fr/04.webp)



Du kan se din transaktionshistorik genom att klicka på ikonen "klocka" på startsidan.



![network_fee](assets/fr/05.webp)



Du har säkert märkt att du måste betala en nätverksavgift för att få satoshis. Dessa avgifter kommer att dras av från de satoshis du ska ta emot. Detta beror på att StashPay är en Wallet baserad på Breez Development Kit. För att ta emot satoshis med den Lightning-nodfria implementeringen av kitet kommer Breez att debitera kunden (StashPay i vårt fall) `0,25% + 40 satoshis`. Ta reda på mer i vår Misty Breez-handledning.



https://planb.network/tutorials/wallet/mobile/misty-breez-738ced2a-0764-4d7f-a150-ec0ce84a9d25

### Skicka bitcoins med StashPay



Att skicka bitcoins med StashPay är ganska intuitivt tack vare den minimalistiska Interface. På startskärmen klickar du på knappen **Sänd**. Skanna QR-koden eller klistra in den Address som du vill skicka satoshis till. StashPay kommer automatiskt att upptäcka Bitcoin protokollkedjan som du vill skicka bitcoins till.



![send](assets/fr/06.webp)



Eftersom StashPay är en Wallet baserad på Breez Development Kit har den en intressant fördel: att skicka bitcoins på huvudkedjan till låg kostnad. Breez använder Boltz-tjänsten för att utföra transaktioner mellan de olika kedjorna i Bitcoin-protokollet, vilket gör det möjligt för kunder som implementerar Development Kit att dra nytta av denna tjänst direkt i sin applikation.



https://planb.network/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

Breez SDK inför dock ett minimibelopp som du kan skicka bitcoins till en Address på huvudkedjan.



![onchain](assets/fr/07.webp)



Du kan också skicka bitcoins med din mottagares Lightning Address. Granska dina transaktionsuppgifter och bekräfta sedan genom att klicka på knappen **Sänd**.



![confirm](assets/fr/08.webp)



## Fler konfigurationer



I StashPay-inställningarna kan du justera konfigurationer för att anpassa din användning av Wallet.



StashPay låter dig Exchange satoshis baserat på den lokala valuta du väljer. Klicka på alternativet **Valutor** och sök sedan efter din valuta i listan med +113 valutor som erbjuds av StashPay.



![currencies](assets/fr/09.webp)



I menyn **Receive options** hittar du alla inställningar för att ta emot bitcoins med StashPay. Till exempel, genom att välja **Välj Lightning eller Onchain**, aktivera din Wallet för att ta emot bitcoins från huvudkedjan.



![receive-onchain](assets/fr/10.webp)



Med alternativet **Scan OnChain-adresser** kan du uppdatera saldot i din Wallet genom att kontrollera alla UTXO:er (bitcoins som du inte har använt ännu) som är kopplade till dina olika adresser.



![rescan](assets/fr/11.webp)



Menyn **Exportlogg** listar alla Breez- och Boltz-infrastrukturåtgärder som rör dina transaktioner och atomutbyten mellan de olika Bitcoin-protokollkedjorna.



![export](assets/fr/12.webp)



Du har precis kommit igång med StashPays minimalistiska Bitcoin Wallet. Om du tyckte att den här handledningen var användbar rekommenderar vi vår handledning om hur du kommer igång med Bitcoin och tjänar dina första bitcoins.



https://planb.network/courses/obtenir-ses-premiers-bitcoins-f3e3843d-1a1d-450c-96d6-d7232158b81f