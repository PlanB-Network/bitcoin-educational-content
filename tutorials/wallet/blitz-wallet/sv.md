---
name: Blitz Wallet

description: Den enklaste Bitcoin Wallet.
---
![cover](assets/cover.webp)



Användarupplevelsen är en av de avgörande faktorerna när det gäller att komma igång med en Wallet. I den här handledningen introducerar vi dig till en Wallet som har gjort sin användarupplevelse till en avgörande faktor: Blitz Wallet erbjuder dig den enklaste och en av de mest kompletta Bitcoin-plånböckerna du kan hitta.



## Vad är Blitz Wallet?



Blitz Wallet är en Bitcoin självförvaltande Wallet vars källkod är tillgänglig (Open Source), som fokuserar på din suveränitet och en användarupplevelse som gör det enkelt att ta tag i.



[Blitz Wallet] (https://blitz-Wallet.com/) är en mobil Wallet som finns tillgänglig på Android (Play Store) och iOS (App Store).



⚠️**VIKTIGT**: Att ladda ner en Bitcoin Wallet på en officiell plattform är viktigt för att verifiera applikationens äkthet och i förlängningen stärka säkerheten för dina medel.



I den här handledningen kommer vi att basera oss på Android-versionen av Blitz Wallet, men alla processer som presenteras nedan är lika giltiga på iOS.



![installation](assets/fr/01.webp)



Eftersom Blitz Wallet är en självinnehavande Wallet av Bitcoin kan du välja att skapa en ny Wallet eller importera de 12/24 återhämtningsorden från en Wallet du redan har.



Här börjar vi med att skapa en ny Wallet. Se nedan för våra rekommendationer om säkerhetskopiering av dina säkerhetskopieringsfraser.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

❗**VIKTIGT**: Dessa 12 / 24 återställningsord är väsentliga för åtkomst till dina bitcoins. Om du förlorar dem kommer du inte längre att vara behörig att spendera dina bitcoins.



Inte dina nycklar, inte dina bitcoins.




Skapa sedan en PIN-kod för att verifiera åtkomsten till din Wallet.



![setup-wallet](assets/fr/02.webp)



## Att komma igång med Blitz



Att handla med Blitz är mer intuitivt än med de flesta andra Bitcoin-plånböcker.



I Wallet-menyn har du en minimalistisk Interface som enbart fokuserar på huvudåtgärderna:



### Ta emot bitcoins



För att ta emot bitcoins på din Blitz Wallet, klicka på ikonen "Nedåtpil", ange det belopp i satoshis som du vill ta emot och Wallet kommer att skapa en Invoice som du kan dela med din avsändare.



⚠️ **NOTER**: Satoshi (eller "sat") representerar den minsta enheten av Bitcoin: 1 Bitcoin = 100 000 000 000 satoshis



En av de speciella egenskaperna hos Blitz Wallet är att den stöder olika nätverk och kanaler från Bitcoin-ekosystemet:





- **Lightning Network**: En av Bitcoin-överlagringarna som låter dig utföra mikrotransaktioner direkt.





- **Bitcoin Mainnet**: Huvudkedjan i Bitcoin-protokollet, lämplig för transaktioner med stora värden.





- **Liquid Network**: En parallell kedja till Bitcoin Mainnet utvecklad av BlockStream som använder Liquid Bitcoins för att utföra snabba, Confidential Transactions.



https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a

Som standard kommer alla dina transaktioner att ske på Liquid Network, men med Blitz kan du definiera det nätverk som du vill ta emot satoshis på genom att klicka på knappen **Välj format**.



![receive-sats](assets/fr/03.webp)



### Skapa kontakter med Blitz



Blitz Wallet gör det enkelt för dig att skicka bitcoins från sin Wallet.



I menyn **Kontakter** kan du registrera de Blitz-användarnamn eller Lightning-URL:er som du interagerar mest med.



Det innebär att du enkelt kan skicka satoshis till dessa adresser och kringgå skanning och manuell inmatning av Address.



![add-contacts](assets/fr/04.webp)



### Skicka bitcoins



Förutom de klassiska metoderna för att skicka Bitcoins (QR-kod, manuell inmatning) kan du genom att använda de kontakter som är förregistrerade i din Wallet skicka Satss till din mottagare med bara tre klick.



I menyn ** Wallet** klickar du på knappen "Uppåtpil", väljer metoden för att skicka bitcoins, anger sedan beloppet som ska skickas och fortsätter med bekräftelse.



Det lägsta beloppet för att skicka Bitcoin i Blitz Wallet är för närvarande 1 000 satoshis.



![send-bitcoin](assets/fr/05.webp)



## Blitz-butiken



Förutom Bitcoin-överföringsoperationer erbjuder Blitz Wallet dig en butik där du kan använda dina bitcoins för att betala för digitala tjänster.





- **Få tillgång till AI-tjänster**: Använd generativa modeller för artificiell intelligens som t.ex: Claude 3-5 sonnet, gpt-4o, gpt-4o-mini gemini-flash-1.5 och betala direkt i bitcoins.



![ia-credits](assets/fr/06.webp)





- **Skicka textmeddelanden var som helst i världen**: I Blitz-butiken har du tillgång till en GSM-tjänst som låter dig skicka textmeddelanden anonymt överallt i världen, med direktfakturering i Bitcoin.



![sms-credit](assets/fr/07.webp)





- **Surfa i total sekretess**: Betala för en WireGuard VPN-prenumeration (Virtual Private Network) i Wallet Blitz-butiken med dina bitcoins.



![wireguard](assets/fr/08.webp)



https://planb.network/tutorials/exchange/centralized/bitrefill-8c588412-1bfc-465b-9bca-e647a647fbc1

https://planb.network/tutorials/wallet/mobile/speed-wallet-8715e454-1720-4a7f-8c1d-3da02cf67312

## Wallet Blitz bakom kulisserna: Att gå längre



Bakom enkelheten i Blitz Wallet:s funktion ligger en mängd kraft och anpassningsmöjligheter.



Som vi påpekade tidigare är alla bitcoins du får som standard Liquid Network.



Blitz använder Liquid Network mikroväxlar för att presentera ditt saldo i Satoshi när du har ett saldo på mindre än 500 000 satoshis.



Detta tillvägagångssätt motiveras av önskan att underlätta uppstartsupplevelsen och hjälpa nya användare att genomföra transaktioner på Lightning Network med små belopp så enkelt som möjligt.



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Du kan se fördelningen av ditt saldo i menyn **Inställningar>Saldoinformation**.



![balance](assets/fr/09.webp)



Blitz Wallet ger dig dock flexibiliteten att aktivera Lightning-läget, som automatiskt öppnar en betalningskanal åt dig när du har nått ett saldo på 500 000 satoshis.



För att aktivera Lightning mode, gå till **Settings**, sedan i avsnittet **Technical Settings**, klicka på alternativet **Node Info**.



![enable-lightning](assets/fr/10.webp)



Genom att aktivera Lightning mode, när huvudvillkoret har uppfyllts (saldo på 500 000 satoshis eller 0,005 Bitcoin), kommer du att kunna utföra transaktioner på Lightning Network och behöver inte längre gå igenom BlockStreams Liquid Network.





- **Acceptera Bitcoin i din butik**:



Integreringen av Bitcoin-betalningar i butiker är fortfarande i experimentfasen med Blitz Wallet. Vi rekommenderar att du använder den sparsamt.



I menyn **Settings>Point-of-sale** kan du ange den unika identifieraren som är kopplad till din butik och den lokala fiat-valutan som du vill ta emot betalningar i.



![pos](assets/fr/11.webp)



Om den här handledningen hjälpte dig att komma igång med Blitz, är vi säkra på att du kommer att tycka om Muun Wallet-handledningen lika mycket. Upptäck Muun, en enkel Wallet som är lika kraftfull som Bitcoin.



https://planb.network/tutorials/wallet/mobile/muun-111b56b0-4872-4130-ad2e-e58f8363451d