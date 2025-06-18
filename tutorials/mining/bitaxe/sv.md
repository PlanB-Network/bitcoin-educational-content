---
name: Konfigurera en BitAxe
description: Hur ställer man in en BitAxe?
---

### Inledning


BitAxe är ett öppen källkodsprojekt skapat av Skot och [finns på GitHub](https://github.com/skot/bitaxe) som möjliggör kostnadseffektiva Mining-experiment.


Det har omvänt konstruktionen av den berömda Antminer S19 av Bitmain, marknadsledaren inom ASIC, de specialiserade maskinerna för Bitcoin Mining. Nu är det möjligt att använda dessa kraftfulla chips i nya öppen källkodsprojekt. Till skillnad från Nerdminer har BitAxe tillräcklig datorkraft för att anslutas till en Mining pool, vilket gör att du regelbundet kan tjäna några satoshis. Nerdminer kan å andra sidan bara anslutas till en så kallad solopool, som fungerar som en lotterilott: du har en liten chans att vinna hela Block reward.


Det finns flera versioner av BitAxe, med olika chips och prestanda:


| Bitaxe Model Series      | ASIC Chip | Used On                     | Expected Hash Rate          | Ideal For                                                                                                  |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Series 100)  | 1 x BM1397| Antminer Series 17          | 400 GH/s (up to 450 GH/s)   | Bitcoin mining beginners, offering a solid hash rate with moderate power consumption.                      |
| Bitaxe Ultra (Series 200)| 1 x BM1366| Antminer S19 XP and S19k Pro| 500 GH/s (up to 550 GH/s)   | Serious miners aiming to balance efficiency and higher hash rate.                                          |
| Bitaxe Hex (Series 300)  | 6 x BM1366| Antminer S19k Pro and S19 XP| 3.0 TH/s (up to 3.3 TH/s)   | Miners seeking scalability and high performance without sacrificing efficiency.                             |
| Bitaxe Supra (Series 400)| 1 x BM1368| Antminer S21                | 600 GH/s (up to 700 GH/s)   | Serious enthusiasts seeking the highest hash rates and efficiency.                                         |

I denna handledning kommer vi att använda en BitAxe Ultra 204 utrustad med ett BM1366-chip, som används för Antminer S19XP. Den här är redan monterad och flashad av återförsäljaren.


### [Listan över återförsäljare finns på den här sidan] (https://bitaxe.org/legit.html)


![signup](assets/2.webp)


I allmänhet säljs strömförsörjningen Supply tillsammans med den. Om inte, måste du köpa en strömförsörjd Supply med en 5V jackkabel och minst 4A.


![signup](assets/1.webp)


### Konfiguration

När du först ansluter din BitAxe kommer den som standard att försöka ansluta till ett Wi-Fi-nätverk. Efter fem försök visar den namnet på sitt eget Wi-Fi-nätverk så att du kan ansluta till det och konfigurera det.

För att göra detta kan du använda vilken dator eller smartphone som helst. Gå till dina Wi-Fi-inställningar, sök efter nya nätverk och du kommer att se ett Wi-Fi som heter Bitaxe_XXXX. Här är det `Bitaxe_A859`. Anslut till detta Wi-Fi-nätverk så öppnas ett fönster automatiskt.


![signup](assets/3.webp)


I detta fönster klickar du på de tre små horisontella staplarna längst upp till vänster och sedan på `Settings`.


![signup](assets/4.webp)


Du måste manuellt ange information om ditt Wi-Fi-nätverk, eftersom det inte finns något automatiskt upptäcktssystem.


![signup](assets/5.webp)


Ange därför SSID för Wi-Fi, det vill säga namnet på ditt nätverk, lösenordet samt informationen om den Mining pool du har valt. Var försiktig, här presenteras inte poolens URL på samma sätt. Till exempel, för Braiins, är poolens URL: `stratum+tcp://eu.stratum.braiins.com:3333`.


![signup](assets/6.webp)


Som du kan se på skärmen måste du ta bort delarna `stratum+tcp://` och `:3333`, så att bara `eu.stratum.braiins.com` återstår. I fältet `Port` anger du sedan de 4 siffrorna i slutet av URL:en som ges av poolen, men utan `:`. Här är det därför `3333`.


I den här handledningen använder vi Braiins Mining pool, men du är fri att välja en annan. Du kan hitta våra handledningar om Mining-pooler [på PlanB Network-webbplatsen] (https://planb.network/en/tutorials/mining).


Därefter anger du din identifierare i `User` och sedan `Password`, vanligtvis är det `"x"` eller `"Anything123"`.


Inställningen `Core Voltage` bör lämnas på `1200` som standard, och för `Frequency` bör också standardvärdet lämnas initialt. Det kommer att vara möjligt att justera denna inställning senare för att få mer datorkraft. Det är dock viktigt att se till att chipets temperatur inte överstiger 65-70°C, eftersom BitAxe inte har något system för att minska prestandan vid överhettning. Om temperaturen överstiger 65°C för mycket kan det skada din BitAxe.


![signup](assets/7.webp)


När du har angett alla inställningar korrekt klickar du på knappen "Spara" längst ner och startar sedan om din BitAxe genom att koppla ur den och koppla in den igen.

Om du har angett dina uppgifter korrekt ska enheten snabbt ansluta till ditt Wi-Fi och sedan till Mining pool och börja visa viss information på sin lilla skärm. Det kommer förmodligen att ta några minuter innan den visas på Mining pool:s instrumentpanel.

### Instrumentpanel och skärm


Tre olika skärmar kommer att rulla igenom. På den tredje sidan ser du `IP`-informationen, som är IP Address som gör att du kan ansluta till instrumentpanelen. Här är Address `192.168.1.19`.


![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)


För att komma åt instrumentpanelen, ange bara denna Address i din webbläsare.


På instrumentpanelen hittar du all information som visas på den lilla skärmen, som vi nu ska titta närmare på.


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

Du kan ändra Wi-Fi- eller poolinställningarna när som helst utan problem.

Beroende på ventilationen och temperaturen i ditt rum kan du behöva öka eller minska prestandan så att temperaturen inte överstiger 65°C. Om du ökar prestandan kommer du att tjäna fler satoshis, men din BitAxe kommer också att förbruka mer el!