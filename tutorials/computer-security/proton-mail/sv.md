---
name: Proton Mail
description: Konfigurera en säker e-postlåda
---
![cover](assets/cover.webp)


E-postlådan är en central del av din online-aktivitet och spelar ofta en avgörande roll för din dators säkerhet. Om en angripare lyckas ta sig in i din e-postlåda får de lätt tillgång till dina andra konton via funktionen "*glömt lösenord*". Detta kan göra det möjligt för dem att kontrollera dina sociala nätverk, dina bankkonton och andra onlinetjänster, eftersom e-postmeddelandet Address idag ofta används som en unik identifierare av din onlineidentitet. Därför är det mycket viktigt att säkra din e-postlåda för att skydda dig mot attacker.


För att garantera säkerheten i din e-postlåda är det viktigt att tillämpa några enkla goda rutiner som vi studerar i denna handledning som riktar sig till nybörjare inom databehandling. Det är också viktigt att välja en säker e-postleverantör som erbjuder avancerade skyddsalternativ och en robust policy för integritetsskydd. Det är därför jag rekommenderar i den här handledningen att upptäcka ProtonMail. Även om du föredrar att inte använda den här leverantören kan de goda metoder som presenteras här tillämpas på vilken e-postlåda som helst för att förbättra dess säkerhet.


## Varför använda ProtonMail?


ProtonMail är en ganska säker meddelandelösning tack vare flera funktioner. För det första säkerställer ProtonMail end-to-end-kryptering av dina e-postmeddelanden, vilket innebär att endast avsändaren och mottagaren kan läsa deras innehåll. I teorin kan inte ens ProtonMail komma åt sina användares e-postmeddelanden. Krypteringen sker automatiskt och kräver ingen särskild teknisk kompetens från användarna.


Dessutom integrerar ProtonMail avancerad teknik för att skydda din integritet, inklusive blockering av vissa spårningssystem och maskering av din IP Address. Proton-företaget är baserat i Schweiz och drar nytta av några av de dataskyddslagar som inte finns i andra länder. Dessutom är ProtonMail öppen källkod, vilket gör det möjligt för oberoende experter att fritt granska programvarukoden.


Protons affärsmodell är baserad på ett prenumerationssystem, vilket är betryggande eftersom det indikerar att företaget finansieras utan att nödvändigtvis utnyttja användarnas data. I den här handledningen kommer vi att utforska hur man använder den kostnadsfria versionen av ProtonMail, men det finns också flera prenumerationsnivåer som erbjuder fler funktioner. Denna affärsmodell är att föredra framför ett helt gratis system, vilket skulle kunna leda till oro för om våra personuppgifter används i vinstsyfte. Lyckligtvis verkar detta inte vara fallet med ProtonMail.


## Skapa ett Proton-konto


Besök den officiella protonwebbplatsen: https://proton.me/


![proton](assets/notext/01.webp)


Klicka på knappen "*Create an account*":

Du har möjlighet att välja mellan olika planer efter dina behov. Till att börja med kan du välja ett gratis konto, vilket gör att du kan testa de grundläggande tjänsterna i ProtonMail. Senare, om du vill komma åt ytterligare funktioner och annan Proton-programvara som Kalender, VPN eller Password Manager, kan du överväga att prenumerera på en betald plan.


Du kommer då till sidan för skapande av konto.


Du kan välja det domännamn som du föredrar för din e-post Address genom att klicka på den lilla pilen. Detta val har ingen inverkan på vad som följer.


Välj också användarnamn för din e-post Address.


Du ombeds sedan att ange ett lösenord. Det är viktigt att välja ett starkt lösenord i det här skedet, eftersom det ger tillgång till din brevlåda. Ett starkt lösenord ska vara så långt som möjligt, innehålla många olika tecken och väljas slumpmässigt. År 2024 är minimirekommendationerna för ett säkert lösenord 13 tecken inklusive siffror, små och stora bokstäver samt symboler, förutsatt att lösenordet verkligen är slumpmässigt. Jag rekommenderar dock att man väljer ett lösenord med minst 20 tecken, inklusive alla möjliga typer av tecken, för att garantera säkerheten under längre tid.


Användningen av en lösenordshanterare är en utmärkt praxis. Det gör inte bara att du kan lagra dina lösenord säkert utan att behöva memorera dem, utan det kan också generate långa och slumpmässiga lösenord åt dig. Människor är verkligen mycket dåliga på att skapa slumpmässiga sekvenser, och ett lösenord som inte är tillräckligt slumpmässigt kan vara sårbart för brute force-attacker. Jag rekommenderar också att du läser vår fullständiga handledning om hur du ställer in en lösenordshanterare för mer information om detta ämne:


https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

Klicka på knappen "*Create Account*".


Lös CAPTCHA.


Välj ett visningsnamn. Det här är det namn som visas för mottagaren när du skickar ett e-postmeddelande. Välj ditt riktiga namn eller ett smeknamn.

Proton erbjuder dig också möjligheten att ställa in en metod för att återställa ditt konto, antingen via ditt telefonnummer eller med ett alternativt e-postmeddelande Address. Det är viktigt att förstå att det här alternativet kan öka attackytan i din e-postinkorg. För dig är det en extra säkerhetsåtgärd för att återfå åtkomst till ditt konto om du glömmer ditt lösenord, men för en hackare är det en extra möjlighet att försöka bryta sig in på ditt konto. Du är inte skyldig att välja detta återställningsalternativ, men om du bestämmer dig för att inte göra det, se till att du har en säker kopia av ditt lösenord. Om du förlorar ditt lösenord kommer du inte att kunna återfå åtkomsten till din e-postinkorg.

![proton](assets/notext/11.webp)


## Konfigurera din Proton-brevlåda


Grattis, din Proton-brevlåda är nu skapad! Börja med att välja färger för ditt brevlådetema.


![proton](assets/notext/12.webp)


Om du vill kan du också ställa in vidarebefordran av dina e-postmeddelanden från ditt gamla Gmail-konto till ditt nya ProtonMail-konto.


![proton](assets/notext/13.webp)


När du väl är på Interface i din brevlåda rekommenderar jag dig att ta en titt på inställningarna för att anpassa dem. Klicka på kugghjulsikonen i det övre högra hörnet.


![proton](assets/notext/14.webp)


Klicka sedan på knappen "*Alla inställningar*".


![proton](assets/notext/15.webp)


På fliken "*Dashboard*" hittar du information som rör ditt konto. Genom att scrolla ner i detta avsnitt har du möjlighet att välja vilka typer av e-postmeddelanden du vill få från Proton. Om du föredrar att inte ta emot reklam- eller informationsmeddelanden kan du välja att avmarkera alla.


![proton](assets/notext/16.webp)


På fliken "*Upgrade plan*" kan du välja en betald plan med nya funktioner.


![proton](assets/notext/17.webp)


På fliken "*Recovery*" kan du lägga till eller ändra dina återställningsmetoder.


![proton](assets/notext/18.webp)


Under fliken "*Account and password*" kan du ändra dina användarnamn samt metoderna för att skydda ditt konto.


![proton](assets/notext/19.webp)


För närvarande är din brevlåda endast säkrad med ett lösenord. Jag råder dig att åtminstone lägga till tvåfaktorsautentisering med en app. För att göra detta klickar du på kryssrutan.


![proton](assets/notext/20.webp)


Bekräfta ditt lösenord.


![proton](assets/notext/21.webp)


Skanna sedan QR-koden med hjälp av din 2FA-app.


![proton](assets/notext/22.webp)


För mer information rekommenderar jag att du tittar på vår handledning om hur du använder en 2FA-app.

På fliken "*Language and time*" kan du ändra Interface:s språk och tidszon.


![proton](assets/notext/23.webp)


På fliken "*Appearance*" kan du ändra färgerna på din Interface.


![proton](assets/notext/24.webp)


På fliken "*Säkerhet och integritet*" har du tillgång till olika säkerhetsalternativ. Vissa av dessa alternativ är endast tillgängliga med en betald plan. Du har också möjlighet att inaktivera insamlingen av dina uppgifter av Proton, som använder denna information för diagnostik och bugglösningar.


![proton](assets/notext/25.webp)


Under fliken "*Import*" har du möjlighet att hantera migreringen av dina gamla e-postmeddelanden till ditt nya ProtonMail-konto. Om du föredrar att börja med en helt ny brevlåda, utan att importera dina gamla e-postmeddelanden, kan du välja att ignorera detta alternativ.


![proton](assets/notext/26.webp)


Under fliken "*Get the apps*" kan du ladda ner Protons mobilapplikationer och skrivbordsprogram för att hantera din brevlåda på dessa plattformar. Om du föredrar det kan du fortsätta att bara använda webbversionen av din brevlåda, som du för närvarande använder, eftersom den erbjuder samma funktioner.


![proton](assets/notext/27.webp)


På fliken "*Messages and composing*" har du en mängd olika anpassningsmöjligheter för din brevlåda.


![proton](assets/notext/28.webp)


På fliken "*Email privacy*" kan du välja alternativ för sekretessen för dina e-postmeddelanden.


![proton](assets/notext/29.webp)


På fliken "*Identitet och adresser*" har du möjlighet att anpassa din e-postsignatur. Om du har ett betalkonto kan du också skapa flera olika e-postadresser som alla hanteras från samma konto. Detta kan vara mycket användbart för att separera dina olika användningsområden.


![proton](assets/notext/30.webp)


På fliken "*Folders and labels*" kan du skapa mappar och etiketter för att organisera din brevlåda.


![proton](assets/notext/31.webp)


På fliken "*Filters*" kan du hantera filter för de e-postmeddelanden du får.


![proton](assets/notext/32.webp)


På fliken "*Forward and auto-reply*" kan du hantera vidarebefordran och automatiska svar för dina e-postmeddelanden.


![proton](assets/notext/33.webp)


På fliken "*Domännamn*" har du möjlighet att skapa en Address med din egen domän, vilket kan vara användbart om du äger en webbplats. För personligt bruk är det inte nödvändigt att använda denna funktion.


![proton](assets/notext/34.webp)


På fliken "*Kryptering och nycklar*" kan du hantera krypteringsalternativen för dina e-postmeddelanden. För nybörjare är det i allmänhet inte nödvändigt att ändra inställningarna i det här avsnittet.

![proton](assets/notext/35.webp)

Och slutligen, fliken "*IMAP/SMTP*" ger dig möjlighet att konfigurera en brygga för att använda ProtonMail med e-postprogram som Outlook eller Apple Mail.


![proton](assets/notext/36.webp)


För att komma tillbaka till startsidan för din brevlåda, klicka på knappen "*Inbox*" längst upp till vänster.


![proton](assets/notext/37.webp)


## Använda din Proton-brevlåda


För att skicka ett e-postmeddelande är det mycket enkelt, klicka bara på knappen "*Nytt meddelande*" längst upp till vänster.


![proton](assets/notext/38.webp)


I fältet "*To*" anger du mottagarens e-post Address.


![proton](assets/notext/39.webp)


I fältet "*Subject*" skriver du in ämnet för ditt e-postmeddelande.


![proton](assets/notext/40.webp)


Skriv ditt meddelande.


![proton](assets/notext/41.webp)


Klicka slutligen på knappen "*Sänd*" för att skicka ditt e-postmeddelande.


![proton](assets/notext/42.webp)


Du hittar sedan dina skickade meddelanden under fliken "*Sänt*".


![proton](assets/notext/43.webp)


Fliken "*Inbox*" innehåller de e-postmeddelanden som du har fått.


![proton](assets/notext/44.webp)


Du kan läsa dina e-postmeddelanden genom att klicka på dem och sedan organisera dem i de olika mappar som du har skapat.


![proton](assets/notext/45.webp)


## Logga in på din Proton-brevlåda


Som tidigare nämnts har du möjlighet att använda din ProtonMail-brevlåda antingen via webbversionen, genom att ladda ner skrivbordsprogramvaran eller via mobilappen. För att ladda ner programvaran kan du besöka den officiella sidan: https://proton.me/mail/download


Om du föredrar att bara använda webbversionen av ProtonMail kan du överväga att lägga till sidan i din webbläsares favoriter för enklare åtkomst i framtiden och för att undvika nätfiskeförsök.


För att få tillgång till den, gå till följande URL: https://account.proton.me/mail


![proton](assets/notext/46.webp)


Ange ditt användarnamn och lösenord och klicka sedan på knappen "*Sign in*". Om du har aktiverat tvåfaktorsautentisering (2FA) kommer du också att uppmanas att ange de 6 dynamiska siffrorna som genereras av din app.


![proton](assets/notext/47.webp)


Du kommer att komma tillbaka till din ProtonMail-inkorg.


![proton](assets/notext/48.webp)