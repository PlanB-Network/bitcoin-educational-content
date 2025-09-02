---
name: PureOS
description: Linux-distributionen som ger dig kontroll över ditt digitala liv.
---

![cover](assets/cover.webp)



Att skydda sin personliga information i den digitala tidsåldern är högsta prioritet för alla Internetanvändare. Företag, organisationer och till och med operativsystem är användbara informationskällor för att definiera din profil och livsstil. Att välja rätt operativsystem är det första steget i att stärka din integritet på nätet. I den här handledningen tittar vi på PureOS, en integritetsfokuserad Linux-distribution.



https://planb.network/tutorials/computer-security/operating-system/debian-d09a57ec-8372-40ca-bcff-499415209e1f

## Komma igång med PureOS



PureOS är ett Debian-baserat operativsystem som utvecklats av Purism. PureOS är lämpligt för både IT-proffs och användare som letar efter en enkel, lättanvänd distribution. Det är unikt eftersom det är *Free Software* och fokuserar på att skydda användarnas personuppgifter genom att skapa ett ramverk baserat på den integritet, frihet, säkerhet och stabilitet som Debian erbjuder.



### Varför välja PureOS?





- Enkel, intuitiv Interface**: GNOME erbjuder ett tydligt Interface-skrivbord som är utformat för att vara lätt att använda, även för personer som inte är bekväma med kommandoraden.





- Gratis**: Som de flesta Linux-distributioner är PureOS helt gratis att använda. En månatlig prenumeration är dock tillgänglig för att stödja utvecklare.





- Säkerhet och stabilitet**: PureOS arkitektur och driftläge gör det till en mycket säker distribution som garanterar dataskydd och systemstabilitet.





- Dokumentation och aktivt community**: PureOS har tydlig och lättillgänglig dokumentation och en engagerad och lyhörd community, vilket gör det enkelt att lösa problem och lära sig systemet steg för steg.



## Installation och konfiguration



För att installera och konfigurera PureOS på din dator krävs följande minimalistiska funktioner:




- Ett USB-minne på minst 8 GB för att flasha systemet.
- 4 GB RAM-MINNE.
- 30 GB ledigt utrymme på din Hard-disk.



Gå till [PureOS officiella webbplats] (https://pureos.net/) och ladda sedan ner ISO-bilden av operativsystemet enligt din maskins arkitektur.



För att starta PureOS-installationen måste du skapa en startbar USB-nyckel med hjälp av flash-programvara som [Balena Etcher] (https://www.balena.io/etcher).



I tre enkla steg får du ett USB-minne som startas med operativsystemet PureOS.





- Anslut USB-minnet och kör den nedladdade Balena-programvaran.
- Välj sedan PureOS ISO-avbildningen
- Välj USB-nyckeln som utmatningsenhet, klicka sedan på ** Flash ** -knappen och vänta på att processen ska slutföras.



![0_01](assets/fr/01.webp)



När USB-nyckeln har startats startar du om den dator som du vill installera PureOS på.



När du startar upp BIOS trycker du på ESC, F9 eller F11, beroende på vilken maskin du använder. Välj USB-nyckeln som startenhet och tryck sedan på `ENTER` för att bekräfta.



### Startskärm



PureOS erbjuder flera alternativ för att starta upp operativsystemet. Välj alternativet **Testa eller installera PureOS** för att starta installationen av operativsystemet.



![0_02](assets/fr/02.webp)



Ställ in det språk och den tangentbordslayout som du vill använda på datorn.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



Tillåt eller neka åtkomst till din **geografiska plats** för applikationer för personliga rekommendationer baserade på ditt område.



![0_05](assets/fr/05.webp)



Du kan ansluta till ditt befintliga **NextCloud**-konto för att hämta data som är kopplade till den kontorssvit du använder på ett annat system.



![0_06](assets/fr/06.webp)



Du får en handledning, men du kan stänga fönstret om du vill hoppa över det här steget.



![0_08](assets/fr/08.webp)



### Starta installationen



Klicka på menyn **Activities** och utforska de program och verktyg som är förinstallerade på systemet. Klicka på **Install PureOS** för att starta installationen



![0_09](assets/fr/09.webp)



Ställ in systemspråk och tangentbordslayout efter behov och konfigurera sedan Hard-diskpartitioneringsläget.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



Du har två alternativ för partitionering av din Hard-disk:




- Radera disk**: För en fullständig installation av PureOS, radera all befintlig data på din Hard-disk.



![0_14](assets/fr/14.webp)





- Manuell partitionering** för att skapa dina egna poäng



⚠️ När du manuellt skapar partitioner för operativsystemet ska du se till att allokera en partition på minst 2 GB för PureOS-drift och sedan en annan partition för data.



![0_15](assets/fr/15.webp)



Aktivera **diskkryptering** om du vill skydda dina data. Ange ett starkt och komplext lösenord.



Koppla en användare till operativsystemet genom att definiera ett användarnamn och ett alfanumeriskt lösenord på minst 20 tecken för att stärka säkerheten för dina data.



![0_16](assets/fr/16.webp)



Granska de inställningar du har gjort och ändra dem om det behövs.



![0_17](assets/fr/17.webp)



Klicka på **Install** och sedan på **Install Now** för att bekräfta att PureOS har installerats på din dator.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



När installationen är klar markerar du rutan **Restart now** för att starta om datorn och bekräftar sedan:




- Språket.
- Tangentbordets layout.
- Ditt NextCloud-konto (valfritt).



![0_25](assets/fr/25.webp)



## Uppdateringar



Innan du börjar använda PureOS är det viktigt att du uppdaterar ditt system. På så sätt kan du dra nytta av de senaste funktionerna och säkerhetsuppdateringarna och få bättre stabilitet.





- Uppdatering via Interface-grafik**:


Öppna programmet **Software** och gå sedan till fliken **Updates**. Tillgängliga uppdateringar visas automatiskt. Klicka på **Download** och sedan på **Install** när nedladdningen är klar.





- Uppdatering via terminal**:


Öppna terminalen och ange följande kommando för att uppdatera listan över tillgängliga paket:



```shell
sudo apt update
```



Ange ditt lösenord och bekräfta. Installera sedan uppdateringarna med:



```shell
sudo apt full-upgrade
```



## PureOS för utveckling



Som standard innehåller PureOS inte alla verktyg som behövs för utveckling.


Du kan installera dem snabbt med följande kommando:



```shell
sudo apt install build-essential git curl
```



Detta kommer att installera kompileringsverktygen **Git** och **Curl**, som är användbara i de flesta utvecklingsmiljöer.



## PureOS-miljö



PureOS utmärker sig genom sin innovativa strategi för verklig konvergens: ett enda operativsystem säkerställer smidig och sömlös drift på en mängd olika enheter, inklusive bärbara datorer, surfplattor, mini-pc:er och smartphones.



PureOS-applikationer är utformade för att vara anpassningsbara: de justeras automatiskt efter skärmstorlek och inmatningsläge (pekskärm eller tangentbord/mus). Till exempel anpassar GNOME-webbläsaren dynamiskt sin Interface för att ge en optimal upplevelse på både mobila och stationära enheter.



PureOS innehåller också kontorspaketet **LibreOffice**, som inkluderar:





- Writer**: en komplett ordbehandlare för att skapa och redigera dokument.
- Calc**: ett kraftfullt kalkylbladsprogram för hantering av data och beräkningar.
- Impress**: ett verktyg för att skapa professionella presentationer.



Med den här kostnadsfria sviten kan du arbeta effektivt utan att behöva vara beroende av proprietär programvara.



PureOS erbjuder en enhetlig, säker och flexibel miljö, baserad på en 100% öppen källkodsdistribution som garanterar total kontroll och strikt respekt för privatlivet. Den verkliga konvergensen gör det möjligt att skapa applikationer som är kompatibla med olika typer av enheter, t.ex. datorer, surfplattor och smartphones, utan behov av komplexa anpassningar.



Med inbyggd tillgång till viktiga verktyg, robusta pakethanterare och ett rikt ekosystem för öppen källkod förenklar PureOS utveckling, testning och driftsättning av applikationer i en säker miljö. Dess stabila arkitektur och Commitment till konfidentialitet gör den till en pålitlig plattform för en mängd olika användningsområden, inklusive Blockchain-utveckling, snabb prototypning eller produktionsmiljöer.



Upptäck vår kurs om hur du stärker din säkerhet och skyddar din digitala integritet.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1