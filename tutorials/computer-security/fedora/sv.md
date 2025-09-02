---
name: Fedora
description: Linux-distributionen som ger dig en fri, komplett och säker arbetsyta.
---


![cover](assets/cover.webp)





Fedora är ett Linux-baserat operativsystem med öppen källkod som lanserades 2003 och som utvecklats av **Fedora Project** och stöds av **Red Hat Linux**. Det är känt för sin stabilitet, goda prestanda och användarvänlighet, vilket gör det till ett utmärkt val för både nybörjare och avancerade användare. Systemet körs på de flesta moderna processorarkitekturer, vilket gör det enkelt att installera på i stort sett alla datorer. Fedora finns också i flera förkonfigurerade utgåvor, kallade "Fedora Spins" eller "Fedora Editions", som är utformade för specifika behov (videospel, astronomi, utveckling ...).



## Fedora Linux-arkitektur



Som du läste tidigare är Fedora ett gratis operativsystem baserat på Linux-kärnan. Linuxkärnan är den del av operativsystemet som kommunicerar med datorns maskinvara och hanterar systemresurser som minne och processorkraft.



Fedora Linux innehåller en mängd olika programverktyg och applikationer som krävs för att köra operativsystemet ovanpå Linuxkärnan. Fedoras modulära arkitektur innebär att det huvudsakligen består av en samling enskilda komponenter som enkelt kan läggas till, tas bort eller bytas ut efter behov. Detta gör att du kan forma operativsystemet med hjälp av endast de resurser du behöver.



Fedora innehåller också en skrivbordsmiljö, som är den Interface genom vilken användare utför uppgifter och får tillgång till applikationer. Fedoras standardskrivbordsmiljö är GNOME, en användarvänlig, lättanvänd och mycket anpassningsbar skrivbordsmiljö.



## Varför välja Fedora?



Bland de många Linux-distributioner som finns tillgängliga utmärker sig Fedora särskilt för:





- Modularitet**: Fedora är kompatibel med olika processorarkitekturer och kan installeras på de flesta datorer, även de med låg effekt, och anpassas perfekt till dina behov.





- En enkel, intuitiv Interface**: Fedora kombinerar en modern grafisk Interface med en kraftfull kommandorads-Interface, vilket gör den lätt att använda för alla profiler.





- Stabilitet i kärnan**: Fedora är baserat på Red Hat och är känt för sina tillförlitliga uppdateringar, särskilt uppdateringar av kärnan, som genomförs utan större buggar tack vare fria bidrag från en stor community.





- Snabb och enkel installation**: med en bildstorlek på bara 3 GB är installationen snabb och enkel, även på maskiner med begränsade resurser.



## Fedora-utgåvor



Beroende på din profil och användning erbjuder Fedora utgåvor som passar dina behov. Du kommer främst att hitta:





- Fedora Workstation**: Den här utgåvan är idealisk för personlig och/eller professionell användning på dina datorer och är installerad med generiska verktyg som webbläsare, en kontorssvit (textredigerare) och programvara för mediauppspelning.





- Fedora Server**: Denna utgåva är dedikerad till serverhantering. Fedora Server innehåller en mängd olika verktyg som hjälper dig att driftsätta och hantera servrar i din egen skala.





- Fedora CoreOS**: Vill du enkelt kunna köra och distribuera molnapplikationer? Fedora CoreOS är utgåvan som ger dig verktygen för att skapa och hantera avbildningar med till exempel Docker och Kubernets.



I den här handledningen kommer vi att ta hand om Fedora Workstation-utgåvan. Processerna som beskrivs nedan är dock liknande för de andra utgåvorna.



## Installera och konfigurera Fedora Workstation



Installation av Fedora Workstation kräver följande maskinvarukonfiguration:




- Ett USB-minne på minst **8 GB** för att starta operativsystemet.
- Minst **40 GB ledigt utrymme** på datorns Hard-disk.
- 4 GB RAM** för en smidig upplevelse.



### Ladda ner Fedora Workstation



Du kan hämta [Fedora Workstation]-utgåvan (https://fedoraproject.org/fr/workstation/download) från Fedora-projektets officiella webbplats. Välj sedan den version som motsvarar din processorarkitektur (32-bitars - 64-bitars) och klicka på ikonen **Download**.



![download](assets/fr/01.webp)



![telecharger](assets/fr/02.webp)


### Skapa en startbar USB-nyckel



För att installera Fedora måste du skapa ett startbart USB-minne med hjälp av programvara som [Balena Etcher] (https://etcher.balena.io/).



![flashOs](assets/fr/03.webp)



![flash](assets/fr/04.webp)



När du har installerat Balena Etcher öppnar du programmet och väljer den nedladdade ISO-bilden för Fedora Workspace. Välj din USB-nyckel som destinationsmedia och klicka på knappen **Flash** för att börja skapa den startbara nyckeln.



![boot](assets/fr/05.webp)


### Installera Fedora



Stäng av datorn när du har startat USB-minnet.


Slå på datorn och öppna BIOS under uppstarten genom att trycka på tangenten F2, F12 eller ESC, beroende på vilken dator du har.



I startalternativen väljer du din USB-nyckel som primär startenhet. Genom att bekräfta detta val kommer datorn att starta om och automatiskt starta Fedora-installationsprogrammet** som finns på USB-nyckeln.



När datorn har startat från USB-minnet visas skärmen **GRUBB**.



I det här skedet har du följande alternativ:




- Testa media**: Med det här alternativet kan du kontrollera USB-minnets integritet och se till att alla beroenden som krävs för en korrekt installation finns tillgängliga. Detta är ett valfritt steg, men rekommenderas om du har några tvivel om USB-minnet.



![install](assets/fr/06.webp)



![testing](assets/fr/07.webp)





- Starta Fedora**: Detta startar Fedora i "live"-läge, utan installation.



På Fedora-skrivbordet (live-läge) klickar du på **Install Fedora** (eller Install on Hard disk) för att starta installationsprocessen. Du kan välja att installera senare och testa Fedora utan att behöva installera det.



![install-live](assets/fr/08.webp)



Det första steget är att välja Fedoras **installationsspråk** och **tangentbordslayout**



![language](assets/fr/10.webp)





- Välja installationsdiskett:



Välj den Hard-disk som du vill installera Fedora på.



Om disken är tom kommer Fedora automatiskt att använda allt tillgängligt utrymme. Annars kan du anpassa partitioneringen (manuellt eller automatiskt).



![disk](assets/fr/11.webp)





- Kryptering:



I det här skedet föreslår Fedora att du krypterar din disk för att lägga till en extra Layer av säkerhet. Detta säkerställer att dina data endast kan läsas av ditt Fedora-system.



![chiffrement](assets/fr/12.webp)



Innan installationen påbörjas visar Fedora en sammanfattning av dina val. Bekräfta och klicka på installationsknappen för att starta Fedora-installationen.



![resume](assets/fr/13.webp)



Under installationen kopierar Fedora filer och konfigurerar systemet. När det är klart startas datorn om automatiskt.



![installation](assets/fr/14.webp)



### Grundläggande konfiguration


Vid första användningstillfället måste du göra några inställningar:




- Ändra systemets språk om det behövs.



![language](assets/fr/15.webp)





- Välj en tangentbordslayout som passar dina önskemål.



![keyboard](assets/fr/16.webp)





- Välj din tidszon genom att skriva namnet på din stad i sökfältet och klicka sedan på motsvarande förslag.



![timezone](assets/fr/17.webp)





 - Aktivera eller inaktivera åtkomst till din position för applikationer som behöver det, samt automatisk sändning av felrapporter.



![location](assets/fr/18.webp)





- Bestäm om du vill aktivera programvaruarkiv från tredje part.



![logs](assets/fr/19.webp)





- Ange ditt fullständiga namn och definiera ett användarnamn för ditt konto.



![name](assets/fr/20.webp)





- Skapa ett säkert lösenord för din session: så långt som möjligt (minst 20 tecken), så slumpmässigt som möjligt och med en mängd olika tecken (gemener, versaler, siffror och symboler). Kom ihåg att spara ditt lösenord.



![mdp](assets/fr/21.webp)



När alla dessa steg har slutförts startar du Fedora och börjar använda det omedelbart, utan någon ytterligare omstart.



![welcome](assets/fr/22.webp)



![start](assets/fr/23.webp)



När installationen är klar kan du använda några förinstallerade verktyg i ditt Interface-hem.



![install-now](assets/fr/09.webp)



## Upptäck de grundläggande uppgifterna



### Surfa på Internet


Fedoras standardwebbläsare är **Firefox**. Den är enkel att använda och passar de flesta behov.


Om du föredrar en annan webbläsare kan du installera den från **programvaruhanteraren** eller via **terminalen**.


### Ordbehandling


Fedora innehåller kontorspaketet **LibreOffice** som standard, vilket erbjuder flera användbara verktyg:




- Writer** för ordbehandling.
- Calc** för kalkylblad.
- Impress** för att skapa presentationer.


## Installera program


För att installera nya program kan du använda Fedoras **programvaruhanterare** (kallad _Software_), som gör installationen enkel och visuell.  Att använda **terminalen** är dock ofta snabbare och mer exakt.



Innan du installerar någon programvara, kom alltid ihåg att uppdatera **repositories** för att se till att du har tillgång till de senaste tillgängliga versionerna.



Använd sedan följande kommando för att starta installationen av det önskade programmet:


sudo dnf installera programvara_namn`


## Uppdatering av operativsystemet


Efter installationen är det viktigt att uppdatera Fedora för att dra nytta av de senaste säkerhetsfixarna och programuppdateringarna.


### Alternativ 1: Via Interface-grafik




- Öppna Fedora **Settings** och gå sedan till avsnittet **System**.
- Klicka på **Software update**.
- Börja ladda ner uppdateringar och vänta tills processen är klar.



En **omstart** kan krävas när uppdateringarna har installerats.


### Alternativ 2: Via terminal




- Öppna en terminal och börja med att uppdatera **repositories** för att se till att du har de senaste versionerna av:



```shell
sudo dnf check-update
```





- Uppdatera sedan all installerad programvara med följande kommando:



```shell
sudo dnf upgrade
```



Nu är ditt Fedora-system uppdaterat och redo att användas för alla dina vardagliga uppgifter. Upptäck vår handledning om Linux Mint, en annan Linux-distribution, och hur du skapar en hälsosam och säker miljö för dina Bitcoin-transaktioner.



https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5