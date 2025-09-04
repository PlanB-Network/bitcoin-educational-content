---
name: Mozilla VPN
description: Skydda dina enheter och dina surfdata på Internet.
---
![cover](assets/cover.webp)



I den digitala tidsåldern med datainsamling har integritet på nätet blivit en viktig fråga för oss internetanvändare. Spårning av reklam, riskerna med att hacka via offentliga nätverk och geografiska begränsningar gör att allt fler användare vänder sig till VPN (*Virtual Private Networks*) för att säkra sin surfning. Bland de många alternativ som finns tillgängliga för dem sticker en tjänst från Mozilla-stiftelsen, känd för sin Commitment till ett fritt och etiskt Internet, ut. I den här handledningen tar vi en titt på Mozilla VPN för att ta kontroll över din integritet på Internet.



## Vad är Mozilla VPN?



Ett ***Virtual Private Network*** (VPN) är ett system för att skapa en direktlänk mellan fjärrdatorer som är anslutna till olika lokala nätverk. Med andra ord är det ett system som isolerar och krypterar dina utbyten från resten av trafiken på Internet. För att lära dig mer om VPN, deras användningsområden och fördelarna med att använda ett, ta en titt på SCU 101-kursen:



https://planb.network/courses/99c46148-7080-4915-a7e0-9df0e145cd47

Baserat på denna princip är [Mozilla VPN] (https://www.mozilla.org/fr/products/vpn/download/) en VPN-tjänst med öppen källkod som utvecklades 2020 av Mozilla Foundation. Den är tillgänglig på:





- Android,
- iOS,
- Mac,
- Linux,
- Fönster,
- och även som ett tillägg till Mozillas webbläsare Firefox.



![download](assets/fr/01.webp)



Den är tillgänglig i över 30 länder och har över 500 servrar som ansvarar för att maskera din IP Address för att flytta dig samtidigt som du säkerställer sekretessen för dina interaktioner på Internet. Mozilla VPN kännetecknas av:





- Användarvänlighet: en strömlinjeformad, minimalistisk Interface-grafik som visar de viktigaste servrarna och länderna som du kan välja mellan.





- WireGuard-teknik: ett kommunikationsprotokoll och en programvara med öppen källkod som använder toppmodern kryptografi för att skapa krypterade tunnlar och erbjuder ett lättviktigt alternativ som är enklare att driftsätta med en mindre kodbas och med fokus på hastighet och säkerhet.





- Transparent prissättning: cirka 10 euro för en månadsavgift och 5 euro per månad för ett årsabonnemang.





- Flera anslutna enheter: Anslut upp till 5 enheter samtidigt till ditt Mozilla VPN-konto.



## Komma igång med Mozilla VPN



Du kan ladda ner [Mozilla VPN] (https://www.mozilla.org/fr/products/vpn/download/) beroende på ditt operativsystem. I den här handledningen kommer vi att titta på Mozilla VPN under Windows-operativsystemet.



⚠️ Eftersom Mozilla VPN inte är tillgängligt i vissa länder kan du stöta på det här meddelandet när du hämtar Mozilla VPN-programmet från Google Play Store.



![playstore](assets/fr/02.webp)



När installationen är klar klickar du på knappen **Register** för att skapa ett nytt konto.



![inscription](assets/fr/03.webp)



Ange ditt lösenord och bekräfta ditt konto genom att fylla i OTP-koden som skickats till din e-post Address. Eftersom Mozilla VPN är en betaltjänst från Mozilla Foundation behöver du en prenumeration för att använda Mozilla VPN till sin fulla potential. Klicka på "Prenumerera nu" för att omdirigeras till prissidan för Mozilla VPN.



![tarifs](assets/fr/04.webp)



Välj sedan en prenumerationsplan som passar dig.



![plans](assets/fr/05.webp)



Gå sedan vidare till betalning med PayPal eller kreditkort.



![paiement](assets/fr/06.webp)



När du har aktiverat din prenumeration öppnar du Mozilla VPN-programvaran och tillåter Mozilla VPN att samla in tekniska data om din surfning eller inte.



![collecte](assets/fr/07.webp)



Du kan också aktivera alternativ för antireklam, webbläsarövervakning och blockering av skadlig programvara.



![privacy](assets/fr/08.webp)



När konfigurationsprocessen är klar ser Mozilla VPN Interface ut så här:



![home](assets/fr/09.webp)



Du kan aktivera VPN genom att klicka på alternativknappen nedan, vilket flyttar datorns IP Address till ett antal IP-adresser på den plats du valt. Du kan också visa listan över enheter som är anslutna till ditt Mozilla VPN-konto direkt från startsidan.



![activate](assets/fr/10.webp)



Med Mozilla VPN kan du välja din plats i två format:





- Single-Hop: som flyttar din dators IP Address och krypterar data till en server i en specifik utvald region, i vårt exempel Sofia i Vitryssland.





- Multi-Hop: skapar en krypterad anslutning från din dator till två fjärrservrar. Detta är en dubbel kryptering: dina data krypteras via server A, sedan från server A krypteras data igen till server B.



![hops](assets/fr/11.webp)



Genom att klicka på ikonen **Inställningar** kan du komma åt de olika anpassningsalternativen som Mozilla VPN erbjuder. I menyn **Nätverksinställningar** kan du konfigurera Mozilla VPN för alla dina applikationer eller välja de applikationer som du inte vill använda Mozilla VPN med. Det här alternativet är en av de innovationer som skiljer Mozilla VPN från de flesta andra VPN: tunneluppdelning.



![permissions](assets/fr/12.webp)



Split tunneling är en praktisk funktion som gör att du kan dirigera en del av din internettrafik via ett VPN och en del utan VPN under samma session. Detta kan vara användbart för internetbank eller annan internettrafik som inte fungerar korrekt med ett VPN.



⚠️Mozilla VPN erbjuder split tunneling på alla produkter utom MacOs och iOS. Tyvärr Apple-användare, du kommer inte att kunna använda den här funktionen. Det är troligt att de kommer att göra det, eftersom de bara tillät den här funktionen via sin Android-app och nu utvidgas den till andra operativsystem.



För att alltid garantera ökad konfidentialitet för sina användare har Mozilla VPN ett **Kill Switch**-system som gör det möjligt att avsluta din internetanslutning om VPN går ner av någon anledning. Detta skyddar din IP Address och annan personlig information.



Nu är du redo att surfa på Internet på ett säkert och konfidentiellt sätt. Om du gillade den här handledningen, vänligen ge den en Green tummen upp. Vi är också säkra på att du kommer att tycka om vår handledning om MULLVAD VPN, en annan VPN-lösning som inte kräver några personuppgifter från sina användare och låter dig betala för din prenumeration i bitcoins (ett mer konfidentiellt alternativ än kreditkort):



https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8