---
name: Angry IP Scanner
description: Een eenvoudige manier om je netwerk te scannen
---
![cover](assets/cover.webp)



___



*Deze zelfstudie is gebaseerd op originele inhoud van Florian BURNEL gepubliceerd op [IT-Connect](https://www.it-connect.fr/). Licentie [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Er kunnen wijzigingen zijn aangebracht in de oorspronkelijke tekst.*



___



## I. Presentatie



Hoe kun je snel en eenvoudig een Windows-netwerk scannen op aangesloten machines? Het antwoord is Angry IP Scanner. Met dit open source project kun je eenvoudig een netwerk scannen met behulp van een gebruiksvriendelijke grafische Interface.



Deze tool kan gebruikt worden door individuen om hun lokale **netwerk** te scannen, maar ook door IT-professionals voor hetzelfde doel. Het bewijs dat **deze tool zeer praktisch** is, is al gebruikt door **sommige cybercriminele groepen** om bedrijfsnetwerken te scannen (op dezelfde manier als Nmap). Een goed voorbeeld is [ransomware groep RansomHub](https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/). Het is nog steeds een degelijk stuk software, maar zoals met andere netwerk- en beveiligingsgerichte tools, kan het gebruik ervan misbruikt worden.



Hier gebruiken we het op **Windows 11**, maar het is perfect mogelijk om het op andere versies van **Windows** te gebruiken, evenals op **Linux** en **macOS**.



Minder uitgebreid dan Nmap, **Angry IP Scanner** is nog steeds interessant voor een snelle, basis netwerkanalyse, maar ook omdat het binnen ieders bereik ligt. Het detecteert hosts die verbonden zijn met het netwerk en identificeert **hostnamen** en **open poorten**.



Als je verder wilt gaan, bekijk dan de tutorial over Nmap:



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II. Aan de slag met Angry IP Scanner



### A. Angry IP Scanner downloaden en installeren



U kunt de laatste versie van Angry IP Scanner downloaden van de officiële website van de applicatie of van GitHub. Wij gebruiken de laatste optie. Klik op de onderstaande link en download de EXE-versie: "**ipscan-3.9.1-setup.exe**".





- [Angry IP Scanner GitHub](https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



Voer het uitvoerbare bestand uit om verder te gaan met de installatie. Er is niets speciaals te doen tijdens de installatie.



![Image](assets/fr/013.webp)



### B. Een eerste netwerkscan uitvoeren



Neem bij de eerste start de tijd om de instructies in het venster "**Aan de slag**" te lezen om meer te weten te komen over hoe de tool werkt. Er zijn trouwens verschillende termen waar je rekening mee moet houden:





- **Feeder**: module verantwoordelijk voor het genereren van lijsten met te scannen IP-adressen, vanuit een willekeurig IP-bereik of een bestand met een lijst met IP-adressen.
- **Fetcher**: een verzameling modules voor het ophalen van informatie over hosts op het netwerk. Er zijn bijvoorbeeld fetchers om MAC adressen te detecteren, poorten te scannen, hostnamen te detecteren of HTTP verzoeken te versturen.



![Image](assets/fr/018.webp)



Om een IP-subnet te scannen, voert u het **begin IP Address** en het **einde IP Address** in het veld "**IP-bereik**" in (anders wijzigt u het type aan de rechterkant). Klik dan op de knop "**Start**".



![Image](assets/fr/019.webp)



Enkele tientallen seconden later is het resultaat zichtbaar in Interface van de software. **Voor elk IP Address in het geanalyseerde bereik ziet u of Angry IP Scanner een host heeft gedetecteerd of niet.** Er verschijnt ook een samenvatting op het scherm met het aantal actieve hosts (in dit geval 6) en het aantal hosts met open poorten.



![Image](assets/fr/020.webp)



Hier zien we de aanwezigheid van een host met de naam "**OPNsense.local.domain**", geassocieerd met het IP Address "**192.168.10.1**" en toegankelijk op **ports 80** en **443** (HTTP en HTTPS). Rechts klikken op de host geeft toegang tot extra commando's, zoals pingen, trace route en browser openen via dit IP Address.



![Image](assets/fr/012.webp)



### C. Scanpoorten toevoegen



Standaard scant **Angry IP Scanner** 3 poorten: **80** (HTTP), **443** (HTTPS) en **8080**. U kunt meer poorten toevoegen om te scannen vanuit de applicatievoorkeuren. Klik op het menu "**Tools**" en vervolgens op het tabblad "**Ports**".



Hier kun je de poortlijst aanpassen via de optie "**Poortselectie**". Je kunt **specifieke poortnummers aangeven, gescheiden door een komma, of poortbereiken**. Het onderstaande voorbeeld voegt twee poorten toe: **445** (SMB) en **389** (LDAP). Om poorten van 1 tot 1000 te scannen, voer je "**1-1000**" in. Er wordt niet gespecificeerd of poortscans worden uitgevoerd in TCP, UDP of beide.



![Image](assets/fr/021.webp)



Als u de scan opnieuw uitvoert, krijgt u waarschijnlijk nieuwe informatie. In het onderstaande voorbeeld vertelt Angry IP Scanner me dat de poorten 389 en 445 open staan op de hosts "**SRV-ADDS-01**" en "**SRV-ADDS-02**", dankzij de nieuwe configuratie van de te scannen poorten.



![Image](assets/fr/022.webp)



**Noot**: in het menu "**Scanner**" kunt u scanresultaten exporteren naar een tekstbestand.



Als je verder wilt gaan met de scan, klik je op het menu "**Tools**" en vervolgens op "**Fetchers**". Dit voegt "mogelijkheden" toe aan de scan. Selecteer gewoon een fetcher en verplaats hem naar links om hem te activeren. Dit voegt een extra kolom toe aan het scanresultaat.



![Image](assets/fr/014.webp)



Het onderstaande voorbeeld toont de functies "**NetBIOS info**" en "**Webdetectie**". De eerste geeft aanvullende informatie zoals de MAC Address en domeinnaam van de machine, terwijl de tweede de titel van de webpagina weergeeft (die een indicatie kan geven van het type webserver of toepassing).



![Image](assets/fr/011.webp)



Tenslotte kun je vanuit de voorkeuren ook de methode veranderen die wordt gebruikt voor "**ping**", dat wil zeggen om te kijken of een host actief is of niet. Aangezien sommige hosts niet reageren op pings, kun je andere methoden proberen (UDP pakket, TCP poort sonderen, ARP, UDP + TCP combinatie, etc.).



## III. Conclusie



Eenvoudig en effectief: Angry IP Scanner detecteert hosts die met een netwerk verbonden zijn en laat u poortscans configureren. Qua opties is het niet zo flexibel als Nmap en gaat het niet zo ver, maar het is een goed begin om snel te scannen.



Als je **Nmap** wilt gebruiken met een grafische Interface, dan kun je **de Zenmap-toepassing** gebruiken (zie onderstaand overzicht).



![Image](assets/fr/015.webp)



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d