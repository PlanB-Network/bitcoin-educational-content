---
name: Een BitAxe instellen
description: Hoe stel ik een BitAxe in?
---
![video](https://youtu.be/tvLSK8v0MK8)


### Inleiding


BitAxe is een open-source project gemaakt door Skot en [beschikbaar op GitHub](https://github.com/skot/bitaxe) dat kosteneffectieve Mining experimenten mogelijk maakt.


Het heeft de werking van de beroemde Antminer S19 van Bitmain, de marktleider in ASIC's, de gespecialiseerde machines voor Bitcoin Mining omgekeerd. Nu is het mogelijk om deze krachtige chips te gebruiken in nieuwe open-source projecten. In tegenstelling tot de Nerdminer heeft BitAxe voldoende rekenkracht om aangesloten te worden op een Mining pool, waarmee je regelmatig wat satoshis kunt verdienen. De Nerdminer daarentegen kan alleen worden aangesloten op een zogenaamde solopool, die werkt als een lot uit de loterij: je hebt een kleine kans om de volledige Block reward te winnen.


Er zijn verschillende versies van BitAxe, met verschillende chips en prestaties:


| Bitaxe Model Series      | ASIC Chip | Used On                     | Expected Hash Rate          | Ideal For                                                                                                  |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Series 100)  | 1 x BM1397| Antminer Series 17          | 400 GH/s (up to 450 GH/s)   | Bitcoin mining beginners, offering a solid hash rate with moderate power consumption.                      |
| Bitaxe Ultra (Series 200)| 1 x BM1366| Antminer S19 XP and S19k Pro| 500 GH/s (up to 550 GH/s)   | Serious miners aiming to balance efficiency and higher hash rate.                                          |
| Bitaxe Hex (Series 300)  | 6 x BM1366| Antminer S19k Pro and S19 XP| 3.0 TH/s (up to 3.3 TH/s)   | Miners seeking scalability and high performance without sacrificing efficiency.                             |
| Bitaxe Supra (Series 400)| 1 x BM1368| Antminer S21                | 600 GH/s (up to 700 GH/s)   | Serious enthusiasts seeking the highest hash rates and efficiency.                                         |

In deze tutorial gebruiken we een BitAxe Ultra 204 uitgerust met een BM1366 chip, gebruikt voor de Antminer S19XP. Deze is al geassembleerd en geflashed door de verkoper.


### [De lijst met retailers is beschikbaar op deze pagina](https://bitaxe.org/legit.html)


![signup](assets/2.webp)


Over het algemeen wordt de Supply meegeleverd. Zo niet, dan moet je een Supply kopen met een 5V aansluitkabel en minstens 4A.


![signup](assets/1.webp)


### Configuratie

Als je de BitAxe voor het eerst aansluit, probeert hij standaard verbinding te maken met een Wi-Fi-netwerk. Na vijf pogingen geeft hij de naam van zijn eigen Wi-Fi-netwerk weer, zodat je er verbinding mee kunt maken en het kunt configureren.

Hiervoor kun je elke computer of smartphone gebruiken. Ga naar je Wi-Fi-instellingen, zoek naar nieuwe netwerken en je ziet een Wi-Fi genaamd Bitaxe_XXXX. Hier is het `Bitaxe_A859`. Maak verbinding met dit Wi-Fi-netwerk en er wordt automatisch een venster geopend.


![signup](assets/3.webp)


Klik in dit venster op de drie kleine horizontale balken linksboven en vervolgens op `Instellingen`.


![signup](assets/4.webp)


Je moet je Wi-Fi-netwerkgegevens handmatig invoeren, want er is geen automatisch detectiesysteem.


![signup](assets/5.webp)


Geef daarom de SSID van de Wi-Fi op, dat wil zeggen de naam van je netwerk, het wachtwoord en de informatie van de Mining pool die je hebt gekozen. Let op, hier wordt de URL van de pool niet op dezelfde manier gepresenteerd. Voor Braiins is de URL van de pool bijvoorbeeld: `stratum+tcp://eu.stratum.braiins.com:3333`.


![signup](assets/6.webp)


Zoals je op het scherm kunt zien, moet je het `stratum+tcp://` en `:3333` gedeelte verwijderen, zodat alleen `eu.stratum.braiins.com` overblijft. Vul vervolgens in het `Port` veld de 4 cijfers in aan het eind van de URL die door de pool wordt gegeven, maar zonder de `:`. Hier is het dus `3333`.


In deze tutorial gebruiken we de Braiins Mining pool, maar je bent vrij om een andere te kiezen. Je kunt onze tutorials over Mining zwembaden vinden [op de PlanB Network website] (https://planb.network/en/tutorials/mining).


Voer vervolgens in `User` je identifier in en vervolgens het `Password`, meestal is dit `"x"` of `"Anything123"`.


De `Core Voltage` instelling moet standaard op `1200` blijven staan, en voor `Frequentie` moet ook in eerste instantie de standaardwaarde blijven staan. Het is mogelijk om deze instelling later aan te passen om meer rekenkracht te verkrijgen. Het is echter belangrijk om ervoor te zorgen dat de temperatuur van de chip niet hoger wordt dan 65-70°C, omdat de BitAxe geen systeem heeft dat de prestaties vermindert in geval van oververhitting. Als de temperatuur te veel boven de 65°C komt, kan dit uw BitAxe beschadigen.


![signup](assets/7.webp)


Als je alle instellingen correct hebt ingevoerd, klik je op de knop `Opslaan` onderaan. Start je BitAxe vervolgens opnieuw op door de stekker uit het stopcontact te halen en er weer in te steken.

Als je je gegevens correct hebt ingevoerd, moet het apparaat snel verbinding maken met je Wi-Fi en vervolgens met de Mining pool, en informatie op het kleine schermpje weergeven. Het duurt waarschijnlijk een paar minuten voordat het op het dashboard van de Mining pool verschijnt.

### Dashboard en scherm


Drie verschillende schermen zullen doorlopen. Op de derde pagina zie je de `IP` informatie, dat is het IP van Address waarmee je verbinding kunt maken met het dashboard. Hier is de Address `192.168.1.19`.


![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)


Om toegang te krijgen tot het dashboard, voer je deze Address in je internetbrowser in.


Op het dashboard vind je alle informatie die wordt weergegeven op het kleine scherm, dat we nu in detail zullen bekijken.


![signup](assets/11.webp)


| BitAxe Screen | Dashboard                                   | Description                                                                                                                                                                                                               |
| ------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gh            | Hashrate                                    | The current computing power, expressed in GigaHash/s                                                                                                                                                                      |
| W/THs         | Efficiency                                  | This is the efficiency of your BitAxe expressed in W/THs. It's the ratio between the electrical power consumed and the computing power produced.                                                                          |
| A/R           | Shares                                      | Quantity of `Shares` sent by your BitAxe to the pool, representing the amount of work provided.                                                                                                                          |
| UT            | Uptime                                      | Time since your BitAxe has been operating without interruption (available in the left menu under `Logs`).                                                                                                                |
| BD            | Best Difficulty                             | Maximum difficulty reached since the last restart. For comparison, the current network difficulty is about 85T.                                                                                                          |
| FAN           | FAN in the `Heat` box                       | Fan rotation speed, expressed in rotations per minute.                                                                                                                                                                    |
| Temp          | ASIC temperature in the `Heat` box          | Chip temperature, which should not exceed 65°C.                                                                                                                                                                           |
| Pwr           | Power                                       | Power in watts consumed. However, this information does not take into account the screen, the fan, or the power supply. For example, when it displays 11.7W, the total consumption is actually 15.8W.                    |
| mV mA         | Input Voltage Input Current                 | Voltage and current consumed by the machine. The power in watts is equal to the voltage multiplied by the current.                                                                                                        |
| FH            | Free Heap Memory (left menu -> `Logs`)      | The available memory.                                                                                                                                                                                                     |
| vCore         | ASIC Voltage (in the Performance box)       | Voltage measured on the ASIC chip.                                                                                                                                                                                        |
| IP            | NA                                          | IP Address.                                                                                                                                                                                                               |
| V2.1.0       | Version (left menu -> `Logs`)               | Firmware version.                                                                                                                                                                                                         |

Je kunt de Wi-Fi- of poolinstellingen op elk moment zonder problemen wijzigen.

Afhankelijk van de ventilatie en de temperatuur van je kamer, moet je misschien de prestaties verhogen of verlagen zodat de temperatuur niet boven de 65°C komt. Als je de prestaties verhoogt, verdien je meer satoshis, maar je BitAxe zal ook meer elektriciteit verbruiken!