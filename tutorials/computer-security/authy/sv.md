---
name: Authy 2FA
description: Hur använder man en 2FA-applikation?
---
![cover](assets/cover.webp)


Numera har tvåfaktorsautentisering (2FA) blivit viktigt för att förbättra säkerheten för onlinekonton mot obehörig åtkomst. I takt med att cyberattackerna ökar är det ibland otillräckligt att enbart förlita sig på ett lösenord för att skydda sina konton. 2FA introducerar ytterligare en Layer av säkerhet genom att kräva en andra form av autentisering utöver lösenordet. Denna verifiering kan ske på flera olika sätt, t.ex. genom en kod som skickas via SMS, en dynamisk kod som genereras av en särskild app eller en fysisk säkerhetsnyckel. Användningen av 2FA minskar kraftigt risken för att dina konton äventyras, även i händelse av att ditt lösenord blir stulet.


## 2FA via autentiseringsappar


Vi kommer att utforska andra lösningar som fysiska säkerhetsnycklar i andra handledningar, men i den här föreslår jag att jag specifikt diskuterar 2FA-applikationer. Funktionen för dessa applikationer är ganska enkel: när 2FA är aktiverat på ett konto, vid varje inloggning, kommer du att bli ombedd inte bara för ditt vanliga lösenord utan också för en 6-siffrig kod. Den här koden genereras av din 2FA-applikation. En viktig egenskap hos denna 6-siffriga kod är att den inte är statisk; en ny kod genereras av applikationen var 30:e sekund.

![AUTHY 2FA](assets/notext/01.webp)

Förnyelsen av koden var 30:e sekund gör det mycket svårt för en angripare att komma åt ditt konto. Detta system förhindrar att angripare kan återanvända en stulen eller uppsnappad kod, eftersom den går ut snabbt. Även om en angripare lyckas få tag i koden kommer denne därför bara att kunna använda den under en mycket kort tidsperiod innan en ny kod krävs. Det faktum att koden ändras så ofta minskar dessutom avsevärt den tid som står till buds för en hackare som försöker gissa sig till koden med hjälp av brute force.


2FA via autentiseringsappar är alltså en lättanvänd och kostnadsfri metod för att avsevärt förbättra säkerheten för dina onlinekonton.


Det finns många applikationer för att ställa in 2FA, bland vilka Google Authenticator och Microsoft Authenticator är de mest kända. Men i den här handledningen vill jag presentera dig för en annan, mindre känd lösning som heter Authy. Alla dessa applikationer fungerar med samma TOTP-protokoll (* tidsbaserat One Time Password *), vilket gör att de används ganska lika.

Authy erbjuder flera fördelar jämfört med andra lösningar från de stora teknikföretagen. Först och främst låter det dig synkronisera dina 2FA-tokens mellan flera enheter, vilket kan vara användbart vid förlust eller byte av telefon. Authy gör det också möjligt för dig att generate en krypterad säkerhetskopia och lagra den online, vilket säkerställer att du aldrig förlorar åtkomsten till dina tokens, även om du förlorar din primära enhet. Ur ett Interface användarperspektiv tycker jag personligen att Authy också erbjuder en trevligare och mer intuitiv upplevelse än sina alternativ.


## Hur installerar jag Authy?


På din smartphone går du till appbutiken (Google Play Store eller Apple Store) och söker efter "*Twilio Authy Authenticator*".



- [Apple] (https://apps.apple.com/us/app/twilio-authy/id494168017)
- [Android] (https://play.google.com/store/apps/details?id=com.authy.authy)

![AUTHY 2FA](assets/notext/02.webp)

När du startar appen för första gången måste du skapa ett konto. Välj ditt lands landskod samt ditt telefonnummer och klicka sedan på "*Submit*".

![AUTHY 2FA](assets/notext/03.webp)

Ange din e-postadress Address för kodåterställning.

![AUTHY 2FA](assets/notext/04.webp)

Ett e-postmeddelande kommer att skickas till dig för att verifiera din Address. Ange de 6 siffrorna som du fått för att bekräfta.

![AUTHY 2FA](assets/notext/05.webp)

Välj en av de två tillgängliga metoderna för att verifiera ditt telefonnummer. Om du väljer att ta emot ett SMS anger du den 6-siffriga kod som du fått i meddelandet för att bekräfta ditt nummer.

![AUTHY 2FA](assets/notext/06.webp)

Grattis, ditt Authy-konto har skapats!

![AUTHY 2FA](assets/notext/07.webp)

## Hur konfigurerar jag Authy?


Börja med att gå till appens inställningar genom att klicka på de tre små prickarna längst upp till höger på skärmen.

![AUTHY 2FA](assets/notext/08.webp)

Klicka sedan på "*Inställningar*".

![AUTHY 2FA](assets/notext/09.webp)

På fliken "*Mitt konto*" har du möjlighet att ändra ditt konto. Jag rekommenderar att du lägger till en PIN-kod i appen genom att välja "*App Protection*". Detta ger en extra Layer av säkerhet för att komma åt din applikation.

![AUTHY 2FA](assets/notext/10.webp)

På fliken "*Accounts*" kan du skapa en säkerhetskopia för dina tokens. Denna säkerhetskopia gör det möjligt att återställa dina koder om det skulle uppstå problem. Den är krypterad med ett lösenord som du måste definiera. Det är viktigt att lösenordet är starkt och förvaras på en säker plats. Det är inte nödvändigt att skapa en säkerhetskopia om du har andra återställningsmetoder, t.ex. en andra enhet med samma Authy-konto.

![AUTHY 2FA](assets/notext/11.webp)In the "*Devices*" tab, you can see all the devices synchronized with your Authy account. You have the option to disable the use of multiple devices, which restricts access to your account to that device only. If you use only one device, this can increase the security of your account, but make sure you have another backup method in case you lose that device.


Om du föredrar att tillåta tillägg av andra enheter rekommenderar jag att du aktiverar alternativet som kräver bekräftelse från de för närvarande auktoriserade enheterna på ditt Authy-konto innan du lägger till en ny enhet.

![AUTHY 2FA](assets/notext/12.webp)

För att lägga till en ny enhet upprepar du helt enkelt installationsprocessen som presenterades i föregående del med samma inloggningsuppgifter. Du kommer sedan att bli ombedd att bekräfta denna nya åtkomst från din huvudenhet.


## Hur ställer jag in 2FA på ett konto?


För att ställa in en 2FA-autentiseringskod via en app som Authy på ett konto måste kontot stödja den här funktionen. Numera erbjuder majoriteten av onlinetjänsterna detta 2FA-alternativ, men det är inte alltid fallet. Låt oss ta exemplet med Proton-postkontot som jag presenterade i en annan handledning:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

![AUTHY 2FA](assets/notext/13.webp)

Du hittar vanligtvis detta 2FA-alternativ i inställningarna för ditt konto, ofta under avsnittet "*Password*" eller "*Security*".

![AUTHY 2FA](assets/notext/14.webp)

När du aktiverar det här alternativet på ditt Proton-mailkonto får du en QR-kod. Du måste sedan skanna denna QR-kod med din Authy-app.

![AUTHY 2FA](assets/notext/15.webp)

På Authy klickar du på knappen "*+*".

![AUTHY 2FA](assets/notext/16.webp)

Klicka på "*Scan QR Code*". Skanna sedan QR-koden på webbplatsen.

![AUTHY 2FA](assets/notext/17.webp)

Du har också möjlighet att justera ditt användarnamn om det behövs. När du har gjort ändringarna klickar du på knappen "*SÄKRA*".

![AUTHY 2FA](assets/notext/18.webp)

Authy kommer då att visa din dynamiska 6-siffriga kod som är specifik för det kontot och som uppdateras var 30:e sekund.

![AUTHY 2FA](assets/notext/19.webp)

Ange den här koden på webbplatsen för att slutföra 2FA-inställningen.

![AUTHY 2FA](assets/notext/20.webp)

Vissa webbplatser kommer också att förse dig med återställningskoder efter att du har aktiverat 2FA. Med dessa koder kan du komma åt ditt konto om du förlorar åtkomsten till din Authy-app. Jag rekommenderar att du sparar dem på ett säkert ställe.

![AUTHY 2FA](assets/notext/21.webp)Your account is now secured with two-factor authentication via the Authy app.

![AUTHY 2FA](assets/notext/22.webp)

Varje gång du loggar in på kontot måste du ange den dynamiska koden som genereras av Authy. Du kan nu säkra alla dina konton som är kompatibla med denna 2FA-metod. För att lägga till ett nytt konto på Authy klickar du på de tre små prickarna längst upp till höger i appen.

![AUTHY 2FA](assets/notext/23.webp)

Klicka sedan på "*Add Account*".

![AUTHY 2FA](assets/notext/24.webp)

Följ samma steg som för det första kontot. Dina olika dynamiska koder kommer att synas på Authys startsida.