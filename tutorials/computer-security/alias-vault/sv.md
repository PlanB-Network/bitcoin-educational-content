---
name: Alias Vault
description: Kraftfullt verktyg för att hantera lösenord, tvåfaktorsautentisering och alias (med inbyggd e-postserver) - Även självhanterande!
---

![cover](assets/cover.webp)



Sekretess och säkerhet på nätet är ett ämne som alla, oavsett verksamhet, bör ägna stor uppmärksamhet åt.



Dessa frågor är dessutom en del av en värld i ständig förändring: allt fler utvecklare deltar i ämnet och tar med sig implementeringar till etablerade lösningar och nya produkter.



Detta är fallet med **Leendert de Borst** och hans "Alias Vault", ett revolutionerande verktyg (det första i sitt slag) som gör att du kan hantera och lagra lösenord, använda lösenordsposter för att autentisera dig till webbtjänster, administrera tvåfaktorsautentisering, men viktigast av allt generate riktiga _aliaser_, allt i en enda Interface.



**Men Alias Vault slutar inte där**.



## Viktiga funktioner



Alias Vault fungerar i molnet på utvecklarens servrar eller självhostad i sin egen infrastruktur, ett alternativ för vilket Docker-filer och image finns tillgängliga för installation med en scipt. Förutom webben Interface finns tillägg tillgängliga för alla populära webbläsare, liksom mobilappar för iOS och Android; den senare kan också laddas ner från F-Droid, kringgå den officiella Google-butiken.



I en Interface är Alias Vault:




- Fri och öppen källkod**
- Password Manager**, för att lagra alla komplexa lösenord. Med hjälp av webbläsartillägget slutför lösenordshanteraren inloggningar på webbplatser
- 2FA**, för att stödja tvåfaktorsautentisering
- Aliashanterare med inbäddad e-postserver**: Alias Vault skapar inte alias som vidarebefordrar e-post till en användares brevlåda, utan skapar faktiska alter-egon, kompletta med förnamn, efternamn, kön, användarnamn, lösenord och födelsedag (om denna information krävs).



En omfattande och grundlig dokumentation ingår i paketet, som kommer att följa nykomlingar till upptäckten av detta kraftfulla verktyg.



## Inga personuppgifter!



Det börjar, som alltid, från webbplatsen [aliasvault.net](aliasvault.net). Som nämnts kan Alias Vault användas på den egna servern eller från utvecklarens moln för att bekanta sig med det innan man går över till den självhostade lösningen.



Webbplatsen har riktigt iögonfallande och väl underhållen grafik, men de bra grejerna kommer om du börjar få tag på den: **skapa ditt konto**.



![img](assets/en/01.webp)



Till din enorma förvåning kommer du att upptäcka att Alias Vault inte ber om personlig information: allt du behöver för att skapa kontot är något smeknamn, ett ord som du känner till, så länge det är tillgängligt. Godkänn användarvillkoren, välj ordet och fortsätt.



![img](assets/en/02.webp)



Ställ in **`masterlösenordet`** nu, vilket är den viktigaste informationen i hela ditt nya system. Med detta enda lösenord kommer du faktiskt att vara den enda som kan komma åt / återställa kontot, eftersom det kommer att hålla ditt "valv" krypterat på servern som kommer att vara värd för din information.



![img](assets/en/03.webp)



Fakta: Du har skapat din egen lösenordshanterare och aliashanterare, men utan att ange din egen fungerande, privata e-post Address.



![img](assets/en/04.webp)



Alias Vault välkomnar dig till ett tryggt, nytt, personligt men också tomt utrymme. Och nu börjar vi befolka det lite grann.



Om du redan har en lösenordshanterare kan du importera filen från den du använder, för att utvärdera skillnaderna med andra leverantörer, eller kanske eliminera aliashanteraren så att du kan hantera allt i ett program.



![img](assets/en/05.webp)



Alias Vault är extremt enkelt: du har en huvudsida, som är `Home`, med två menyer:




- `Credentials`: som gör att du kan skapa och sedan hantera identiteter och alias
- "E-post": en inkorg där du kan kontrollera inkommande meddelanden för alias som du har skapat.



![img](assets/en/06.webp)



Det är skapandet av en första "alias" som vi är intresserade av, så gå upp till höger på sidan och klicka på _+New Alias_.



![img](assets/en/07.webp)



Inledningsvis ser menyn minimal ut, i enlighet med Alias Vaults filosofi. För att upptäcka funktionerna i denna funktion, klicka på _Create via advanced mode_.



![img](assets/en/08.webp)



Den övre delen av den första skärmen kan du använda för att importera lösenordsuppgifter som du redan använder för tjänster som du har ett abonnemang på eller som du oftast använder online.



Om du har aktiverat tvåfaktorsautentisering på någon (eller alla) av ovanstående tjänster kan du med Alias Vault också hantera denna ytterligare Layer av säkerhet genom att importera den "hemliga nyckeln". Alias Vault kommer att skapa den `TOTP` som krävs för åtkomst.



![img](assets/en/09.webp)



**Försiktighetsåtgärd**: I det utrymme som reserverats för e-postadressen Address föreslår Alias Vault som standard en egen domän; för att kunna använda den korrekta Address som du tidigare skapat konton med klickar du på _Enter custom domain_, så att du kan ange rätt domän efter `@`.



![img](assets/en/14.webp)



Den nedre delen av den här skärmen är den roligaste. Klicka på _Generate Random Alias_ och Alias Vault kommer att skapa separata identiteter åt dig för olika behov, var och en med sin egen brevlåda, mycket robusta lösenord, kompletterat med andra detaljer som kön, födelsedatum och ett lämpligt smeknamn.



![img](assets/en/10.webp)



Från en särskild meny kan du ändra de inställningar som påverkar genereringen av lösenord, t.ex. att bara välja gemener och ta bort tecken som kan vara tvetydiga.



![img](assets/en/11.webp)



Du kan använda den alias-e-post som föreslås av Alias Vault eller byta domän om du klickar på motsvarande rullgardinsmeny.



![img](assets/en/12.webp)



Innan du använder det här e-postmeddelandet för en inloggningstjänst kan du testa dess funktionalitet genom att skicka ett meddelande från en egen Address till den nyskapade brevlådan.



![img](assets/en/13.webp)



**⚠️ VARNING**: Mottagning av e-postmeddelanden är möjlig tack vare Alias Vaults inbyggda server, men detta gör att du bara kan ta emot e-postmeddelanden och inte svara eller använda e-postlådan med de "konventionella" funktionerna i en `alias`-tjänst. Det skiljer sig således mycket från Simple Login, Addy och andra plattformar som uteslutande är avsedda för denna typ av tjänst. För exemplet med Simple Login kan du se den dedikerade handledningen:



https://planb.academy/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41

För att ta bort ett alias som du har skapat som ett test behöver du bara logga in på `Home`, sedan `Credentials` och klicka på den identitet som du vill ta bort. Kommandot _Delete_ visas i det övre högra hörnet så att du kan fortsätta.



![img](assets/en/16.webp)



## Tillägg till webbläsare



Beroende på vad du behöver kan du använda dig av webbläsartillägget, som finns i de mest använda webbläsarna.



![img](assets/en/15.webp)



Den installeras på samma sätt som alla andra tillägg, så jag tänker inte gå in på den detaljen.



Webbläsartillägget finns för att göra det enklare att logga in på onlinetjänster eller skapa nya alias vid behov: om tjänsten lagras bland dina Alias Vault-poster gör autofyllningen det som behövs.



![img](assets/en/17.webp)



Den enda försiktighetsåtgärden är att kontrollera att Alias Vault är aktivt. Faktum är att programmet har en standardinställning som gör att det pausas efter en tids inaktivitet. Detta är en mycket användbar funktion, **när du t.ex. måste gå bort från din dator och förhindra att någon annan får tillgång till dina konton**. En förenklad procedur gör att du kan logga in igen genom att ange "masterlösenordet", om den tidigare sessionen fortfarande finns kvar i cacheminnet. Tiden för utloggning är en av de parametrar som du kan anpassa, förkorta eller förlänga den enligt dina önskemål.



## Mobil app



Som alla appar med självrespekt av det här slaget har Alias Vault en version för mobila enheter, i både Android- och iOS-miljöer. För Android kan du ladda ner appen från [F-Droid] (https://f-droid.org/packages/net.aliasvault.app/).



När detta skrivs (slutet av augusti 2025) anser mobilappen att "automatisk fyllning" är en experimentell funktion som inte fungerar annat än med mycket få webbplatser. Tills den är helt implementerad kräver användning av Alias Vault på mobilen kopiering/klistring av data.



När du har laddat ner appen från butiken loggar du in genom att ange den användare och det "huvudlösenord" som skapats i webbappen.



![img](assets/en/18.webp)



När du öppnar ditt "valv" får du frågan om du vill aktivera biometriskt kontrollerad åtkomst, en extra Layer säkerhetsåtgärd för att förhindra att någon annan kommer åt dina lösenord om de råkar hålla i din telefon.



![img](assets/en/19.webp)



Om du bestämmer dig för att ställa in biometrisk kontroll, fortsätt. Om du hoppar över steget och ångrar dig kan du också konfigurera det senare från menyn _Settings_.



När du har loggat in kommer du att se att de uppgifter du redan har skapat synkroniseras igen.



![img](assets/en/20.webp)



Mobilappen kan dirigeras till länken till "valvet" som finns på den egna servern.



![img](assets/en/22.webp)



Och det är just den självhostade versionen som vi kommer att Address, kortfattat, i nästa avsnitt.



## Självhosting: full kontroll över dina data



Alias Vault, för att vara rättvis, är inte den första "lösenordshanteraren" som låter dig distribuera tjänsten på din infrastruktur. Det finns andra, men vissa har antingen begränsningar eller är delvis slutna källor.



Möjligheten är unik: **Sluta vara beroende av externa tjänsteleverantörer eller moln, utan använd din egen lokala server för att skydda och hantera lösenord, alias och extremt känslig information som är förknippad med allt detta**. Med Alias Vault kan du också låta e-posttjänsten peka mot din egen e-postserver för extra sekretess.



Det är dags att vända sig till [dokumentation] (https://docs.aliasvault.net/installation/), för att ta reda på hur man går vidare till självhosting Alias Vault.



![img](assets/en/23.webp)



Alias Vault körs på Docker Compose, så minimal erfarenhet av Linux och Docker krävs. Du kan börja med den grundläggande installationen och sedan komplettera med mer avancerade lösningar.



Din server måste köras på en 64-bitars maskin, med en Linux-distribution, 1 GB RAM och minst 16 GB lagringsutrymme; Docker-versionen (CE) måste vara minst 20.10 eller högre, medan Docker Compose kräver en version från 2.0 och uppåt.



Jag bestämde mig för att prova Alias Vault med en tunn klient, på vilken DietPi är installerad som en distribution, en Debian Bookworm-bas, optimerad till det väsentliga och som redan kör `Docker` och `Docker Compose`.



Först, för att få lite ordning, skapar du en katalog i ditt hem, öppnar `terminal` och klistrar in kommandot för att köra installationsskriptet.



```bash
curl -L -o install.sh https://github.com/lanedirt/AliasVault/releases/latest/download/install.sh
```



![img](assets/en/24.webp)



![img](assets/en/25.webp)



När installationen är klar kommer du att hitta dina inloggningsuppgifter:


```
Admin Panel: https://localhost/admin
Username: admin
Password: yyy0xyx1yxy2zxx4
```



Kontrollera innehållet i katalogen efter installationen.



![img](assets/en/29.webp)



För att starta Alias Vault använder du kommandot:



``` Starta alias-valv


./install.sh start


```

Alias Vault adesso gira sul tuo server personale.

![img](assets/en/30.webp)

Apri un browser e digita l'url: ti comparirà la pagina per fare login come `Admin` di Alias Vault.

![img](assets/en/26.webp)

Il più è fatto! Hai davanti a te il pannello per amministrare Alias Vault in maniera personalizzata.

![img](assets/en/27.webp)

Da questa interfaccia, potrai controllare quanti e quali utenti stanno utilizzando il servizio, limitarne l'uso, cancellare gli utenti (azione irreversibile) e soprattutto controllare tutti i `log`.

Se si tratta di una nuova installazione, non avrai altri utenti oltre ad `admin`; per crearne di nuovi, apri un'altra `tab` del browser e digita:

```


localhost/user/start


```

![img](assets/en/28.webp)

Da qui in poi, tutto procede come abbiamo visto in precedenza nella guida, con la differenza che adesso stai usando Alias Vault sul tuo server. Se la tua macchina è adeguatamente configurata e protetta, questo è un modo elegante e sicuro di gestire un tuo password e alias manager, senza servizi di terze parti.

Per fermare Alias Vault, torna al terminale e digita:

``` Stop-Alias-Vault
./install.sh stop

```



![img](assets/en/31.webp)



## Överväganden om kryptering och säkerhet



![img](assets/en/32.webp)



Enligt vad Lanedirt uppger på webbplatsen, i dokumentationen och på Github, med Alias Vault **all information (komponenter) som du placerar på Alias Vault, förblir tätt bunden till enheten, krypterad och oåtkomlig för alla som inte känner till "huvudlösenordet" **.



Huvudlösenordet är alltså det grundläggande elementet i hela "valvet". Efter att det har angetts bearbetas det med algoritmen "Argon2id", en Hard-minnesnyckelavledningsfunktion, för att förhindra att hemligheten lämnar enheten.



Allt förblir dolt även från moln- eller värdtjänsthanteraren. Faktum är att du från adminpanelen inte kan komma åt användaruppgifter, du kan bara veta om de har skapat alias, mottagit e-postmeddelanden och lite annat.



Allt lagrat innehåll krypteras och dekrypteras med kryptografiska nycklar som härrör från "huvudlösenordet". **Endast krypterade data lagras på servern, ingenting visas i klartext**. Om en användare glömmer eller förlorar sitt "huvudlösenord" förloras det konto som är kopplat till det oåterkalleligt, eftersom servern inte kan komma åt innehållet i klartext.



För den självhostade versionen finns det ett skript för att återställa "huvudlösenordet", men detta förhindrar inte dataförlust.



![img](assets/en/33.webp)



Eftersom Alias Vault är i _Beta_-stadiet kan du ha svårt att komma åt det om du ändrar/uppdaterar huvudlösenordet. Jag föreslår att du väljer ett robust och komplext lösenord från början så att du kan experimentera med tjänsten och så småningom bestämma dig för om du vill använda den. Om du har svårt att komma åt molnet efter lösenordsuppdateringen, vänligen kontakta Alias Vaults support.



För en fullständig förståelse av arkitekturen och säkerheten i Alias Vault rekommenderar jag starkt att du läser [denna sida] (https://docs.aliasvault.net/architecture/), som innehåller detaljer om den kryptografi som ligger till grund för dess funktion.



## Vägkarta


Utvecklarnas avsikt är att göra Alias Vault moget och stabilt i slutet av 2025, så att man kan definiera dess framtida användningsegenskaper.



Alias Vault är och kommer alltid att förbli öppen källkod och gratis, men förmodligen inte obegränsat som i beta. Vissa betalda funktioner håller på att implementeras, eftersom de redan har tillkännagivits.



Det finns team-/familjeplaner och stöd för hårdvarunycklar, det senare för autentisering med FIDO2 eller WebAuth.



## Vem behöver Alias Vault



**Ett verktyg som detta är perfekt för alla som sätter integritet på nätet främst**.



Din identitet är med all sannolikhet kärnan i de affärer du gör på nätet och måste skyddas på alla sätt för att hålla **den** informationen borta från tjänster, företag och mäklare som är villiga att göra vad som helst för att få tag på ditt beteende på nätet.



Alias Vault ger dig fullständig kontroll över dina uppgifter, vilket minskar eller helt eliminerar behovet av att förlita dig på tredje part för att skydda och kryptera dina mest känsliga data.



Alias Vaults arkitektur och kryptografiska faciliteter är idealiska för suveräna privatpersoner, små och medelstora företag, utvecklingsteam och alla entusiaster av **open source**-applikationer. Om du tillhör någon av dessa kategorier: ha kul när du upptäcker Alias Vault.