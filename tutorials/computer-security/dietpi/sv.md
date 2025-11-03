---
name: DietPi
description: Lättviktigt operativsystem optimerat för maskiner med låg prestanda. Med en preferens för självhanterande
---

![cover](assets/cover.webp)



I icke-tekniska kretsar är varumärken som "Odroid", "Raspberry Pi", "Orange Pi" eller "Radxa" föga kända. Men man behöver bara titta ut i teknikkretsar för att upptäcka att **SBC**-datorer - byggda på ett enda moderkort, ofta mikroskopiska i storlek jämfört med vanliga datorer - blir oumbärliga som stöd för alla personliga projekt.



Det här är datorer som tillverkas i en mängd olika modeller. De är företrädesvis värdar för Linux-distributioner, som ofta är anpassade för att fungera smidigt på dessa underdimensionerade maskiner.



**DietPi är inget undantag**: det är ett Debian-baserat operativsystem, optimerat för att vara så lätt som möjligt och göra även den minst presterande `SBC` mycket snabb. Det byttes från Debian12 Bookworm till Debian13 Trixie precis när den här handledningen skrevs, och stöder nu även `RISC-V` processorbaserade SBC:er med öppen källkod. DietPi är en trevlig upptäckt som förtjänar ytterligare studier.



## Styrkor



Detta är inte den "vanliga kopian" av Debian för små kort av Raspberry-typ. DietPi är det:




- Optimerad för hastighet och lätthet**: en [jämförelse med andra Debian-distributioner för SBC](https://dietpi.com/blog/?p=888), DietPi är lättare i allt. DietPi ISO-bilden väger mindre än 1 GB, den absolut minsta bland dem som är avsedda för äldre modeller av Raspberry eller Orange PI (till exempel). Efterfrågan på RAM- och CPU-resurser är mycket låg, så att den alltid får ut det bästa av brädor, även äldre.
- Inbyggda automatiseringar och installatörer**: En serie dedikerade kommandon hjälper användare att övervaka systemresurser samt automatisera uppgifter för att installera och starta program, uppdatera versioner, göra säkerhetskopior och kontrollera alla loggar.
- En stark, experimentorienterad gemenskap**: [tutorials](https://dietpi.com/forum/c/community-tutorials/8) och projekt från DietPi-gemenskapen är perfekta för att få inspiration till programvara som du kan installera med ett klick tack vare DietPi.



**Det har aldrig varit enklare att få ut så mycket som möjligt av din SBC**.



## Automatiseringar för självhosting


Vill du experimentera med din egen server för att köra avancerade nätverkslösningar eller verktyg för att utveckla din Bitcoin-expertis? DietPi kan vara den lösning du har letat efter. Även om många människor vet hur man hanterar sin egen infrastruktur och kör perfekt konfigurerade och skyddade servrar, är DietPi ett lämpligt steg för dem som vill börja från början.



Istället för att manuellt utföra alla de komplexa uppgifter som en sådan uppgift kräver, låter DietPi dig bygga dem med en `wizard` och en egen kommandorad. Här kan du experimentera med ditt eget personliga moln, _smart home_-enhetshantering, automatiserade säkerhetskopior och crontab samt mer avancerade lösningar.



![img](assets/en/01.webp)



## Installation



### Nedladdningar



DietPi erbjuder en otalig uppsättning ISO-bilder, för att bränna operativsystemet till många olika enheter. Vissa stöds bara: ISO för Raspberry PI5 testas fortfarande, till exempel, men du kan definitivt hitta den som passar ditt kort.



För den här guiden valde jag att installera den på en tunn klient, så valet gick till _PC/VM_ och sedan till _Native PC_. Det finns två ISO-bilder för dessa enheter, som skiljer sig åt i genereringen av bootloader. Maskinen som används i handledningen är ganska gammal, så valet gick till _BIOS/CSM_-versionen. Om du har en nyare maskin kan den korrekta versionen vara `UEFI`.



![img](assets/en/02.webp)



Du kommer att hamna på en sida som innehåller `image of the installer`, `sha256` och `Signatures`.



![img](assets/en/03.webp)



Förbered en katalog i `home` på din dagliga dator, så att du kan ladda ner de nödvändiga filerna med `wget`.



![img](assets/en/04.webp)



Utvecklarens publika nyckel krävde en del efterforskningar, men du hittar den på den här länken: https://github.com/MichaIng.gpg.



![img](assets/en/05.webp)



Kontrollera innehållet i katalogen med `ls -la` och importera MichaIng-nyckeln till din nyckelring med `gpg --import`.



### Verifiering och flash



Slutligen, den del som jag rekommenderar mest: kontrollera äktheten hos det operativsystem som du har laddat ner och ska installera på din SBC.



![img](assets/en/06.webp)



Om du också fick resultatet `Good signature` och samma Hash-kontroll med kommandot sha256sum kan du fortsätta med att flasha ISO till ett USB-minne. Använd appar som Whale Etcher för att göra detta.



![img](assets/en/07.webp)



## DietPi Installation



![img](assets/en/09.webp)



Överför flashminnet till den enhet som ska vara värd för DietPi och påbörja installationen av operativsystemet lime Green. I den här övningen använder vi en tunn klient med 16 GB RAM, en 128 GB SSD för operativsystemet och en andra 1 TB datadisk. Installationen tog mindre än 30 minuter, men om du till exempel använder en Raspberry kan resurserna vara mindre och ta längre tid. Du kommer att se hur installationen fortskrider under tiden.



![img](assets/en/08.webp)



DietPi är designad för hallon och liknande, men dess sanna natur är den så kallade "huvudlösa" installationen, utan en grafisk miljö och med inbyggd "shsh"-åtkomst. I guiden kommer du istället att se en grafisk miljö, LXDE för att vara exakt.



Under detta steg kommer du också att bli ombedd att välja vilken webbläsare du vill använda som standard, mellan Chromium och Firefox. Båda fungerar bra; det finns inga särskilda kontraindikationer för någon av dem, annat än dina personliga preferenser.



Mot slutet kan installationsprogrammet fråga dig om du vill installera några program redan, men här **Råder jag dig att inte förinstallera något**. Du bör veta att du efter detta steg kommer att bli ombedd att ändra standardlösenorden för de två användarna, av säkerhetsskäl. Viktigast av allt är att du måste **ställa in det globala programvarulösenordet (GSP)`**, vilket kommer att säkerställa åtkomst till de olika programvarorna på ett kontrollerat sätt. **Om du laddar ner någon programvara under installationen av operativsystemet, utan att ange GSP, kommer den att förbli praktiskt taget oåtkomlig**. Du kommer att behöva avinstallera och installera om dem igen efter att du har ställt in `Global Software Password`: därför ska du **inte lägga in något för att undvika dubbelarbete**. (Olägenheten är sannolik, inte 100% säker).



Installationen avslutas med en begäran om att aktivera DietPi-Survey, en automatiserad datainsamlingstjänst som används för att stödja utvecklingen av operativsystemet. Enligt webbplatsen aktiveras datainsamlingen när du laddar ner någon av programvarorna från den automatisering som tillhandahålls av DietPi, eller när du uppgraderar till nästa version. Alla har möjlighet att välja att delta (_Opt IN_) eller välja bort (_Opt OUT_).



![img](assets/en/23.webp)



Efter avslutad installation och efterföljande omstart visas DietPi på skärmen som du ställer in den. För handledningen valde jag som nämnts den grafiska miljön `LXDE`. På skrivbordet hittade jag genvägen för att starta `htop` och den öppna terminalen.



![img](assets/en/10.webp)



### "Verktyg" från operativsystemet



Glöm de flesta av de program du använder på din Linux-distribution - DietPi är så optimerat att du har utelämnat en hel del. Du skulle i princip behöva installera en massa kommandon manuellt, men om du bara testar det, motstå frestelsen och försök att sätta DietPis automatiseringar under test.



Det är definitivt den terminal som är det första användbara verktyget för att komma igång med ditt nya operativsystem, och den öppnas automatiskt varje gång du slår på den.



![img](assets/en/11.webp)



På terminalskärmen visas en rad kommandon som föregås av `dietpi-` och som representerar [verktygen](https://dietpi.com/docs/dietpi_tools/) i det här operativsystemet:




- `dietpi-launcher`: för att komma åt operativsystemet, filhanteraren etc
- `dietpi-Software`: som representerar det verktyg med vilket du kan installera all programvara som redan finns i sviten
- `dietpi-config`: för att komma åt systemkonfigurationer, även de mest avancerade.



![img](assets/en/14.webp)



### Säkerhetskopiering



Säkerhetskopiering av en server är en rutin som systemadministratören bör ta hänsyn till redan vid första uppstarten.



Med DietPi finns kommandot `dietpi-Backup`, som jag rekommenderar att du utforskar för att hitta den perfekta lösningen: det låter dig ställa in en regelbunden säkerhetskopiering, inkrementell eller inte beroende på vilka applikationer som används, och alla alternativ för att anpassa rutinen.



![img](assets/en/22.webp)



Välj destination för säkerhetskopian, t.ex. en annan disk, genom att starta `dietpi-Drive_Manager` för att montera destinationsenheten och använda den för den här funktionen.



## Konfiguration



Självhosting är en tillrådlig upplevelse för alla, oavsett om man är nyfiken eller bara entusiastisk. Att dra upp och konfigurera en server innebär dock några inte obetydliga tekniska utmaningar. Det är här ** enkelheten i DietPi** kommer in, så att du kan konfigurera ett system som är skräddarsytt efter dina behov i några enkla steg.



![img](assets/en/24.webp)



Grundläggande och avancerade inställningar, allt finns till hands i den enda Interface som är tillgänglig med kommandot:



```dietpi-konfig


sudo dietpi-konfig


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


sudo dietpi-programvara


```