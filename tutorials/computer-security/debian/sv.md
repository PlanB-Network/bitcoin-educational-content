---
name: Debian
description: En Linux-distribution som är känd för sin stabilitet, robusthet och kompatibilitet.
---

![cover](assets/cover.webp)



Debian är en fri GNU/Linux-distribution som är känd för sin robusthet och tillförlitlighet. Linuxkärnan och alla dess paket är noggrant testade för att säkerställa en bergfast stabilitet och en hög säkerhetsnivå. Debian är lämplig för både servrar och arbetsstationer och erbjuder en lättanvänd upplevelse och en stor katalog med programvara. Oavsett om du letar efter ett säkert system för daglig användning eller en produktionsmiljö är Debian det rätta valet.



## Varför välja Debian?





- Fri och öppen**: Debian är helt öppen källkod, vilket garanterar transparens och inga licensavgifter.
- Stabilitet och säkerhet**: varje release genomgår en grundlig testprocess, vilket gör Debian till en av de mest pålitliga och säkra distributionerna på marknaden.
- Aktivt community**: ett stort community och omfattande dokumentation finns tillgängliga för att stödja dig när du behöver det.
- Lätt och skalbar**: du kan installera Debian på maskiner med blygsamma resurser och samtidigt bibehålla bra prestanda.
- Omfattande programvarukatalog**: över 50 000 officiella paket finns tillgängliga via arkiven.



## Välj en Interface-grafik



Debian erbjuder flera skrivbordsmiljöer för att passa dina behov:





- GNOME**: modern, intuitiv Interface, perfekt för nybörjare. Den erbjuder en smidig, lättanvänd grafisk meny för åtkomst till applikationer.
- XFCE**: lätt och snabb, perfekt för mindre kraftfulla maskiner.
- KDE Plasma**: mycket anpassningsbar, med ett Windows-liknande utseende.
- Cinnamon**: enkel, elegant Interface, inspirerad av Windows.
- LXDE / LXQt**: ultralätt, lämplig för äldre datorer.
- MATE**: enkelt och klassiskt, nära det gamla GNOME.



💡 För en bekväm och greppvänlig upplevelse rekommenderas **GNOME**.



## Installera och konfigurera Debian


### Krav på hårdvara



Innan du påbörjar installationen ska du se till att du har följande utrustning:





- USB-nyckel**: minst 8 GB för att lagra den startbara ISO-bilden.
- Slumpmässigt åtkomstminne (RAM)**: 4 GB för smidig installation och drift.
- Diskutrymme**: minst 15 GB ledigt utrymme för systemet och uppdateringar.



### Nedladdningar



Valet av Debian-image beror på din processorarkitektur:





- AMD64**: ladda ner "live hybrid"-utgåvan från [download]-listan (https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/).
- ARM64**: hämta DVD-avbildningen från den officiella [Debian]-webbplatsen (https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/).
- Andra arkitekturer**: hitta den ISO som motsvarar din arkitektur [här](https://debian.obspm.fr/debian-cd/12.11.0/).



![download](assets/fr/01.webp)



### Skapa ett startbart USB-minne



När du har hämtat rätt ISO-bild fortsätter du med att skapa ditt installationsmedium:




- Ladda ner Balena Etcher** från den [officiella webbplatsen] (https://etcher.balena.io/), hämta sedan binärfilen för ditt system och installera den.



![etcher](assets/fr/02.webp)





- Starta Etcher**: öppna programvaran och välj den tidigare nedladdade Debian ISO-imagen.
- Välj USB-nyckel**: ange din nyckel (8 GB+) som mål.
- Starta flash**: klicka på **Flash!** och vänta tills processen är klar.



![flash](assets/fr/03.webp)



Ditt USB-minne är nu redo att börja installera Debian.



## Installera Debian på ditt system



### Starta från USB-nyckel



För att starta installationen från ditt USB-minne:




- Stäng av** datorn helt och hållet.
- Starta om** och gå sedan till BIOS/UEFI genom att omedelbart trycka på `ESC`, `F2`, `F11` (eller den dedikerade tangenten beroende på ditt varumärke).
- I startmenyn **väljer du din USB-nyckel** som startenhet.
- Bekräfta** med Enter-tangenten för att starta Debian-imagen: detta tar dig till installationsprogrammets välkomstskärm.



### Starta installationen



Startskärm:



![starting](assets/fr/04.webp)



När du startar från USB-minnet erbjuder Debians välkomstskärm flera alternativ:




- Live System**: Startar Debian utan att installera det, perfekt för att testa miljön.
- Start Installer**: startar installationen direkt på Hard-disken.
- Advanced Install Options**: ger dig tillgång till anpassade installationslägen.



Om du vill utforska Debian i live-läge väljer du **Live System** och bekräftar med **Enter**. Du kan sedan starta installationen genom att klicka på **Install Debian** i live-miljön.



![system](assets/fr/05.webp)





- Val av språk** (tillval)



Välj huvudspråket för Debian-systemet i listan och klicka sedan på OK.



![language](assets/fr/06.webp)





- Tidszon** (GMT)



Välj din geografiska zon för att automatiskt ställa in datum och tid.



![timezone](assets/fr/07.webp)





- Layout för tangentbord



Välj språk och layout för tangentbordet. Använd det inbyggda testfältet för att kontrollera att varje tangent producerar det förväntade tecknet.



![keyboard](assets/fr/08.webp)



### Diskpartitionering





- Erase disk**: om du har en särskild partition kommer detta alternativ att radera allt dess innehåll.
- Manuell partitionering**: välj det här alternativet för att skapa, ändra storlek på eller ta bort partitioner efter behov.



![disk](assets/fr/09.webp)





- Skapa ett användarkonto



Ange ditt fullständiga namn, kontonamn och ett starkt lösenord för att säkerställa att din session är säker.



![user](assets/fr/10.webp)





- Sammanfattning av parametrarna**



En sammanfattning av dina val visas: kontrollera varje objekt och gå tillbaka för att ändra om det behövs.



![settings](assets/fr/11.webp)





- Starta installationen



Klicka på **Install** för att börja kopiera filer och konfigurera systemet, vänta sedan tills processen är klar.



![install](assets/fr/12.webp)





- Starta om**



När installationen är klar startar du om datorn för att tillämpa alla konfigurationer och få tillgång till ditt nya Debian-system.



![restart](assets/fr/13.webp)



Vid start anger du användarnamn och lösenord för att få tillgång till systemet.



![login](assets/fr/14.webp)



## Uppdatering av systemet



Innan du börjar använda ditt system är det viktigt att du uppdaterar det. På så sätt kan du dra nytta av de senaste programkorrigeringarna, uppdaterade arkiv och i vissa fall säkerhetsuppdateringar för själva operativsystemet.



### Alternativ 1: Uppdatering via grafisk Interface (GNOME)



Om du har installerat Debian med GNOME-skrivbordsmiljön kan du utföra uppdateringar grafiskt. För att göra detta, öppna programmet **Software** och gå sedan till fliken **Updates**. Klicka sedan på **Starta om och uppdatera** för att starta processen.



### Alternativ 2: Uppdatering via terminal (rekommenderas)



Den här metoden ger mer fullständig kontroll. Den låter dig uppdatera arkiv, programvarupaket och, vid behov, kärnan.




- Öppna terminalen med hjälp av kortkommandot `Ctrl + Alt + T`.
- Uppdatera listan över tillgängliga paket med följande kommando:



```shell
sudo apt update
```



Ange ditt lösenord när du uppmanas att göra det (observera att inga tecken visas när du skriver - det är normalt).





- För att installera tillgängliga uppdateringar:



```shell
sudo apt full-upgrade
```



## Upptäck de grundläggande uppgifterna



### Surfa på Internet



Standardwebbläsaren på Debian är **Firefox**. Om du föredrar en annan webbläsare kan du installera en annan, förutsatt att den finns tillgänglig i Debians arkiv (t.ex. Chromium, Brave ...).



### Ordbehandling



Sviten **LibreOffice** är installerad som standard på Debian.





- För att skriva dokument använder du **LibreOffice Writer**, motsvarigheten till Microsoft Word.
- För kalkylblad fungerar **LibreOffice Calc** som ett alternativ till Excel.
- Slutligen kan du med **LibreOffice Impress** skapa presentationer, precis som med PowerPoint.



## Installera program



Det finns två sätt att installera program på Debian:



### Grafisk metod:



Du kan använda **programvaruhanteraren** (nås via den grafiska Interface) för att enkelt söka efter och installera program.



### Metod för kommandoraden:



Om programmet du letar efter inte visas i den grafiska Interface, eller om du föredrar terminalen, använder du följande kommando:



```shell
sudo apt install <name>
```



Ersätt `<namn>` med paketnamnet. Till exempel, för att installera `curl`:



```shell
sudo apt install curl
```



### Installera ett manuellt nedladdat paket:



Om du har hämtat en `.deb`-fil (Debian-paket) kan du installera den med följande kommando:



```shell
sudo apt install ./name.deb
```



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af

Ditt Debian-system är nu installerat och klart att användas för dina dagliga uppgifter.


Tack vare skrivbordsmiljön **GNOME** får du tillgång till ett brett utbud av applikationer via en användarvänlig grafisk Interface, perfekt för både nybörjare och avancerade användare.



Det är också möjligt att byta skrivbordsmiljö (t.ex. till XFCE, KDE, etc.) utan att behöva installera om Debian. För att göra detta använder du helt enkelt terminalen och installerar den nya miljö som du väljer.



Om du vill lära dig mer om Debian, och mer allmänt om GNU/Linux-distributioner, rekommenderar jag att du läser den här kursen:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1