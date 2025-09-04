---
name: Elementär OS
description: Den perfekta ersättaren för Windows och MacOS
---

![cover](assets/cover.webp)



Elementary OS är ett Ubuntu-baserat operativsystem som är utformat för att vara enkelt, snabbt och stabilt för många vardagliga användningsområden. Det är ett balanserat Linux-alternativ till MacOS och Windows. Dess flytande, intuitiva och överskådliga grafiska Interface gör det lätt att lära sig, även för nybörjare. Det fokuserar också på ergonomi, säkerhet och prestanda.



https://planb.network/tutorials/computer-security/operating-system/ubuntu-78a3be56-5d51-4ec3-8629-0dd27c352ab5

## Varför välja Elementary OS





- Enkelhet och användarvänlighet**: Elementary OS:s grafiska Interface ligger mitt emellan MacOs och Windows. Detta gör det lätt att använda, även för oerfarna användare.





- Säkerhet**: Liksom de flesta Linux-distributioner har Elementary OS en hög säkerhetsnivå. Regelbundna uppdateringar, rättighetshantering och avsaknad av vanliga virus gör det till ett pålitligt system.





- Hastighet**: Elementary OS är en lättviktig distribution. Den kräver få resurser, vilket gör den snabb och lämplig för datorer med blygsamma konfigurationer.





- Gratis**: Systemet är helt gratis. När du laddar ner det kan du dock göra en donation för att stödja utvecklarna.





- Aktiv gemenskap**: Gemenskapen kring Elementary OS är mångsidig och lyhörd. Om du stöter på problem kan du enkelt hitta hjälp i forumet eller på sociala nätverk.



## Installation och konfiguration


### Förutsättningar för hårdvara



Innan du påbörjar installationen ska du se till att du har följande utrustning:





- En **USB-nyckel** på minst 12 GB
- RAM-minne** på minst 4 GB
- En **Hard-disk på 20 GB** eller mer för bekväm användning



## Ladda ner ISO-bild



Gå till operativsystemets officiella webbplats [elementary] (https://elementary.io/) och välj ett belopp för att stödja projektet. Detta steg är valfritt.


Om du vill hämta ISO-imagen utan kostnad anger du 0 i fältet **"Other"** och börjar hämta ISO-imagen för systemet.



![0_01](assets/fr/01.webp)



## Skapa ett startbart USB-minne



När du har hämtat ISO-bilden måste du göra den startbar på ett USB-minne för att kunna fortsätta med installationen.



Ladda ner programvara som [Balena Etcher] (https://etcher.balena.io/) eller ett liknande verktyg och starta sedan programvaran.


Välj den tidigare nedladdade **Elementary OS** ISO-imagen och ange din USB-nyckel som mål.



Klicka på knappen **flash** för att starta processen och vänta tills processen är klar innan du tar bort USB-nyckeln.



![0_02](assets/fr/02.webp)



## Nyckel för uppstart och BIOS-åtkomst



Stäng av den dator som du vill installera Elementary OS på och anslut sedan USB-nyckeln.


När datorn startar går du in i BIOS (`ESC`, `F9` eller `F11` beroende på fabrikat) och väljer USB-nyckeln som startenhet och trycker sedan på `Enter` för att starta startprocessen.



## Installera Elementary OS



Installationen startar automatiskt om USB-nyckeln är korrekt konfigurerad.



### Val av språk



Välj det språk som du vill installera systemet på. Du kan också välja en regional variant.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



### Layout för tangentbord



Välj den layout som motsvarar ditt tangentbord. Ett fält finns för att kontrollera att tangenterna producerar rätt tecken.



![0_05](assets/fr/05.webp)



![0_06](assets/fr/06.webp)



### Testläge



Med Elementary OS kan du testa systemet innan du installerar det. I det här läget kan du utforska Interface utan att ändra något på din Hard-disk.



### Starta installationen





- Klicka på **"Radera disk och installera"** för att installera direkt på hela disken.
- Klicka på **"Custom install"** om du vill hantera partitioner manuellt.



![0_07](assets/fr/07.webp)



### Val av skiva



Välj den disk som Elementary OS ska installeras på och klicka sedan på knappen Fortsätt.



![0_08](assets/fr/08.webp)



### Diskkryptering



Ett alternativ gör att du kan kryptera disken för att **skydda dina data**. Du måste ange ett starkt lösenord för att aktivera detta skydd. Det är dock valfritt.



![0_09](assets/fr/09.webp)



![0_10](assets/fr/10.webp)



### Starta installationen



Innan du startar installationen kan du godkänna automatisk installation av ytterligare maskinvarudrivrutiner, beroende på maskinens kompatibilitet.





- Klicka på "Radera och installera" för att påbörja installationen.
- Vänta tills processen är klar.



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



### Omstart



När du är klar klickar du på knappen **enter** för att starta om och tar sedan bort USB-nyckeln vid rätt tillfälle för att undvika att installationen startas om.



![0_13](assets/fr/13.webp)



## Konfiguration efter installation



Efter omstart krävs några ytterligare steg.



![0_14](assets/fr/14.webp)



### Val av språk



Bekräfta eller ändra systemspråket vid inloggning.



![0_15](assets/fr/15.webp)



### Layout för tangentbord



Kontrollera att tangentbordslayouten är den du vill ha.



![0_16](assets/fr/05.webp)



### Skapa ett användarkonto



Koppla ett användarkonto till operativsystemet genom att definiera ett användarnamn och sedan säkra åtkomsten till dina data med ett alfanumeriskt lösenord med minst 20 tecken och symboler.



![0_17](assets/fr/17.webp)



### Första anslutningen



När du loggar in för första gången låter Elementary OS dig anpassa din miljö med några grundläggande inställningar.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



## Uppdatering av systemet



Före långvarig användning är det viktigt att uppdatera systemet med de senaste korrigeringarna.


### Alternativ 1: Uppdatering via Interface-grafik



Gå in i **AppCenter** och klicka på uppdateringsikonen i det övre högra hörnet. Vänta tills uppdateringarna listas och klicka sedan på **"Uppdatera alla"** för att starta installationen.



![0_20](assets/fr/20.webp)



![0_21](assets/fr/21.webp)



### Alternativ 2: Uppdatering via terminal



Du kan också utföra uppdateringen från kommandoraden via din terminal: ett rekommenderat alternativ för dess noggrannhet.



```shell
sudo apt update
```



```shell
sudo apt full-upgrade
```



För dina första uppdateringar kräver operativsystemet ditt användarlösenord och bekräftelse för att uppdatera programpaket, även i Elementary-kärnan.



## Konfiguration av arbetsmiljön



Elementary OS innehåller endast de viktigaste verktygen. För att anpassa din miljö efter dina behov, särskilt om du är utvecklare, rekommenderar vi att du installerar ytterligare verktyg.





- Du kan lägga till användbara beroenden med följande kommando (anpassas efter dina behov):



```shell
sudo apt update && sudo apt install -y git python3 python3-pip build-essential wget curl zsh make snapd && sudo snap install code --classic
```



Detta kommando installerar **Git**, **Python 3**, **pip**, **compiler tools**, **wget**, **curl**, **zsh**, **make**, **snapd** och **vscode** för att förbereda en grundläggande utvecklingsmiljö.



Elementary OS är nu igång på din dator. Dess filosofi om enkelhet, lätthet och elegans gör det till ett utmärkt val för både personlig och professionell användning. Du får ett stabilt, smidigt och överskådligt system som är redo att anpassas efter dina önskemål. Oavsett om det gäller utveckling, kontorsanvändning eller dagligt surfande finns allt på plats för att skapa en effektiv, intuitiv och trevlig arbetsmiljö. Kolla även in vår handledning om Fedora, en lika enkel, robust och modulär Linux-distribution.



https://planb.network/tutorials/computer-security/operating-system/fedora-8c17b6ca-5acb-4825-a069-4474375534b0