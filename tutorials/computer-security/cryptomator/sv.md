---
name: Cryptomator
description: Kryptera dina filer i molnet
---
![cover](assets/cover.webp)



___



*Denna handledning är baserad på originalinnehåll av Florian BURNEL publicerat på [IT-Connect](https://www.it-connect.fr/). Licens [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Ändringar kan ha gjorts i originaltexten.*



___



## I. Presentation



I den här handledningen använder vi Cryptomator-programmet för att kryptera data som lagras i molnet, oavsett om det är på Microsoft OneDrive, Google Drive, Dropbox, Box eller till och med iCloud.



Det bästa sättet att skydda dina filer och din integritet är att kryptera de data som du lagrar på onlinelagringslösningar som Drive. Tack vare krypteringen är du den enda som kan dekryptera och läsa dina data, även om de lagras på en server i USA eller ett annat land runt om i världen.



I den här demonstrationen används en Windows 11 22H2-maskin med OneDrive, men proceduren är identisk med andra versioner av Windows och andra lagringstjänster. Allt du behöver göra är att installera synkroniseringsklienten och lägga till ditt konto. Detta gör det möjligt för Cryptomator att lagra sina data i valvet.



![Image](assets/fr/020.webp)



Cryptomator är ett alternativ till andra applikationer, särskilt Picocrypt som presenteras i en annan artikel, som ser annorlunda ut, men är lika enkelt att använda. Cryptomator är också ** öppen källkod **, RGPD-kompatibel och kommer ** att kryptera data med AES-256-bitars krypteringsalgoritm **. Picocrypt förlitar sig däremot på den snabbare XChaCha20-algoritmen (även den 256-bitars).



https://planb.network/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

Cryptomator-applikationen är tillgänglig på **Windows** (exe / msi), **Linux**, **macOS,** men också **Android** och **iOS**. Förresten, alla applikationer är gratis, förutom Android-applikationen, som du måste betala för (14,99 euro).



På din maskin kommer **Cryptomator att skapa en mapp inom vilken den kommer att skapa ett kassaskåp**. Inom valvet, som kan lagras på din OneDrive, Google Drive eller liknande, kommer dina data att krypteras. Så om du lagrar alla dina data i kassaskåpet som finns på ditt Drive-lagringsutrymme kommer det att skyddas (eftersom det är krypterat).



**I den här artikeln används lagringstjänster online som ett exempel, men Cryptomator kan användas för att kryptera data på en lokal disk, en extern disk eller till och med en NAS. Det finns faktiskt inga begränsningar.**



## II. Installera Cryptomator



För att komma igång behöver du **ladda ner** och **installera** **Cryptomator**. När nedladdningen är klar är några klick allt som krävs för att slutföra installationen. Liksom [Rclone] (https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/) kommer Cryptomator att förlita sig på WinFsp för att ** montera en virtuell enhet på din Windows-maskin **.





- [Ladda ner Cryptomator från den officiella webbplatsen] (https://cryptomator.org/downloads/)



![Image](assets/fr/025.webp)



## III. Använda Cryptomator på Windows



### A. Skapa ett nytt kassaskåp



För att skapa ett nytt kassaskåp klickar du på knappen "**Lägg till**" och väljer "**Nytt kassaskåp...**". Dina befintliga och kända kassaskåp på den här maskinen visas då i Interface, till vänster. **Ett kassaskåp som skapats på maskin A kan öppnas och ändras på maskin B**, förutsatt att den är utrustad med Cryptomator (och att krypteringsnyckeln är känd).



![Image](assets/fr/015.webp)



Börja med att ge valvet ett namn, t.ex. "**IT-Connect**". Detta kommer att skapa en katalog med namnet "**IT-Connect**" i min OneDrive.



![Image](assets/fr/011.webp)



I nästa steg kommer Cryptomator sannolikt att ** upptäcka "Drive"** som finns på din maskin: Google Drive, OneDrive, Dropbox, etc.... Så att du kan välja leverantör direkt. Jag försökte detta på två olika Windows 11-maskiner, med flera enheter, och det upptäcktes inte. Det är inget problem, definiera bara en "**Custom location**" och välj roten till ditt lagringsutrymme. Till exempel: **C:\Users\<Username>\OneDrive**.



![Image](assets/fr/018.webp)



Därefter kan du justera ett alternativ under expertinställningar.



![Image](assets/fr/021.webp)



Därefter måste du definiera **ett lösenord som motsvarar krypteringsnyckeln**. Med detta lösenord kan du **låsa upp ditt Cryptomator-kassaskåp** och komma åt dess data. **Om du förlorar det, förlorar du tillgång till dina data**. Slutligen har du fortfarande möjlighet att **skapa en säkerhetskopia** genom att markera alternativet "**Yes, better safe than sorry**", ungefär i samma anda som [BitLocker]-återställningsnyckeln (https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/). Detta är tillrådligt, men lagra inte denna säkerhetskopieringsnyckel i roten till din OneDrive!



Klicka på "**skapa ett kassaskåp**".



![Image](assets/fr/019.webp)



Kopiera återställningsnyckeln och förvara den i din favoritlösenordshanterare. Klicka på "**Nästa**".



![Image](assets/fr/013.webp)



Nu är din nya trunk skapad och klar att användas!



![Image](assets/fr/014.webp)



### B. Åtkomstsiffror



För att komma åt ett kassaskåp och dess data, antingen för att **läsa befintlig data eller lägga till ny data**, måste du **låsa upp** det. Cryptomator listar kända kassaskåp: IT-Connect-kassaskåpet visas, så det är bara att välja det och klicka på "**Unlock**".



![Image](assets/fr/016.webp)



Du måste ange ditt lösenord för att låsa upp kassaskåpet. Klicka sedan på "**Release drive**".



![Image](assets/fr/022.webp)



**Ditt kassaskåp monteras på Windows-maskinen som en virtuell enhet.** Denna enhet, som här ärver bokstaven E, ger dig tillgång till dina data (i klartext, eftersom kassaskåpet är upplåst).



![Image](assets/fr/017.webp)



På OneDrive-sidan kan vi inte bläddra i Cryptomator-valvet direkt. Vi kan inte se data (varken filnamn eller innehåll). Det betyder att du inte behöver lägga till data i ditt Cryptomator-valv via den vanliga OneDrive-genvägen. **Du måste lägga till dina data med hjälp av Cryptomators virtuella enhet.**



![Image](assets/fr/012.webp)



### C. Alternativ för trunk



Du kommer åt kassaskåpets inställningar via knappen "**Encrypted volume options**" (när det är låst) och kan aktivera automatisk låsning vid inaktivitet, precis som du kan göra med ditt lösenordsskåp. Alternativet "**Unlock encrypted volume on startup**", som namnet antyder, låser upp enheten utan att du behöver göra något och monterar den virtuella enheten. Av säkerhetsskäl är det bäst att undvika att aktivera detta alternativ.



Via fliken "**Mounting**" kan du också välja att montera den skrivskyddad eller tilldela en specifik bokstav.



![Image](assets/fr/024.webp)



Dessutom kan du i Cryptomator-inställningarna **aktivera automatisk programstart**.



## IV. Slutsatser



Med **Cryptomator** kan du **skapa ett krypterat kassaskåp** på bara några minuter för att skydda de data du vill lagra på OneDrive och konsorter. Det är väldigt lätt att använda när det gäller att "para ihop" det med en enhet: för detta ändamål har det min preferens framför Picocrypt.