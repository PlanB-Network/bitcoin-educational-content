---
name: Bitaxe
Opis: Kako postaviti BitAxe?

---
![video](https://youtu.be/tvLSK8v0MK8)
### Uvod


BitAxe je projekat otvorenog koda koji je kreirao Skot i [dostupan je na GitHub-u](https://github.com/skot/bitaxe) što omogućava isplativo eksperimentisanje sa Mining.


Obrnuto je inženjeringovao rad poznatog Antminer S19 od Bitmain-a, lidera na tržištu ASIC-a, specijalizovanih mašina za Bitcoin Mining. Sada je moguće koristiti ove moćne čipove u novim projektima otvorenog koda. Za razliku od Nerdminer-a, BitAxe ima dovoljnu računarsku snagu da bude povezan na Mining pool, što će vam omogućiti da redovno zarađujete neke satoshije. Nerdminer, s druge strane, može biti povezan samo na takozvani solopool, koji funkcioniše kao lutrijska karta: imate male šanse da osvojite puni Block reward.


Postoji nekoliko verzija BitAxe-a, sa različitim čipovima i performansama:


| Bitaxe Model Series      | ASIC Chip | Used On                     | Expected Hash Rate          | Ideal For                                                                                                  |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Series 100)  | 1 x BM1397| Antminer Series 17          | 400 GH/s (up to 450 GH/s)   | Bitcoin mining beginners, offering a solid hash rate with moderate power consumption.                      |
| Bitaxe Ultra (Series 200)| 1 x BM1366| Antminer S19 XP and S19k Pro| 500 GH/s (up to 550 GH/s)   | Serious miners aiming to balance efficiency and higher hash rate.                                          |
| Bitaxe Hex (Series 300)  | 6 x BM1366| Antminer S19k Pro and S19 XP| 3.0 TH/s (up to 3.3 TH/s)   | Miners seeking scalability and high performance without sacrificing efficiency.                             |
| Bitaxe Supra (Series 400)| 1 x BM1368| Antminer S21                | 600 GH/s (up to 700 GH/s)   | Serious enthusiasts seeking the highest hash rates and efficiency.                                         |

U ovom vodiču ćemo koristiti BitAxe Ultra 204 opremljen BM1366 čipom, koji se koristi za Antminer S19XP. Ovaj je već sastavljen i flešovan od strane prodavca.


### [Spisak prodavaca je dostupan na ovoj stranici](https://bitaxe.org/legit.html)


![signup](assets/2.webp)


Generalno, uz njega se prodaje napajanje Supply. Ako nije, potrebno je kupiti napajanje Supply sa 5V džek kablom i najmanje 4A.


![signup](assets/1.webp)


### Konfiguracija

Kada prvi put priključite svoj BitAxe, pokušaće da se poveže na Wi-Fi mrežu po defaultu. Nakon pet pokušaja, prikazaće ime svoje Wi-Fi mreže kako biste se mogli povezati na nju i konfigurisati je.

Da biste to uradili, možete koristiti bilo koji računar ili pametni telefon. Idite na podešavanja Wi-Fi mreže, potražite nove mreže i videćete Wi-Fi pod nazivom Bitaxe_XXXX. Ovde je to `Bitaxe_A859`. Povežite se na ovu Wi-Fi mrežu i prozor će se automatski otvoriti.


![signup](assets/3.webp)


U ovom prozoru kliknite na tri male horizontalne trake u gornjem levom uglu, zatim na `Settings`.


![signup](assets/4.webp)


Moraćete ručno uneti informacije o vašoj Wi-Fi mreži, jer ne postoji sistem za automatsko otkrivanje.


![signup](assets/5.webp)


Stoga, navedite SSID Wi-Fi mreže, odnosno ime vaše mreže, lozinku, kao i informacije o Mining pool koje ste odabrali. Budite pažljivi, ovde URL bazena nije predstavljen na isti način. Na primer, za Braiins, URL bazena koji je dat je: `stratum+tcp://eu.stratum.braiins.com:3333`.


![signup](assets/6.webp)


Kao što možete videti na ekranu, potrebno je ukloniti delove `stratum+tcp://` i `:3333`, ostavljajući samo `eu.stratum.braiins.com`. Zatim, u polje `Port`, unesite 4 cifre na kraju URL-a datog od strane pool-a, ali bez `:`. Ovde je to dakle `3333`.


U ovom vodiču koristimo Braiins Mining pool, ali slobodno možete odabrati drugi. Naše vodiče o Mining bazenima možete pronaći [na PlanB Network sajtu](https://planb.network/en/tutorials/mining).


Dalje, u `User`, unesite svoj identifikator, a zatim `Password`, obično je to `"x"` ili `"Anything123"`.


Podešavanje `Core Voltage` treba ostaviti na `1200` po defaultu, a za `Frequency`, takođe ostavite početnu vrednost. Biće moguće kasnije prilagoditi ovo podešavanje kako bi se dobila veća računarska snaga. Međutim, važno je osigurati da temperatura čipa ne prelazi 65-70°C, jer BitAxe nema sistem za smanjenje performansi u slučaju pregrevanja. Ako temperatura previše pređe 65°C, to bi moglo oštetiti vaš BitAxe.


![signup](assets/7.webp)


Kada pravilno unesete sva podešavanja, kliknite na dugme `Save` na dnu, zatim ponovo pokrenite vaš BitAxe jednostavno tako što ćete ga isključiti i ponovo uključiti.

Ako ste ispravno uneli svoje podatke, uređaj bi trebalo brzo da se poveže na vaš Wi-Fi, zatim na Mining pool, i počne da prikazuje neke informacije na svom malom ekranu. Verovatno će biti potrebno nekoliko minuta da se pojavi na kontrolnoj tabli Mining pool.

### Kontrolna tabla i Ekran


Tri različita prikaza će se smenjivati. Na trećoj stranici ćete videti informacije o `IP`, što je IP Address koji vam omogućava povezivanje na kontrolnu tablu. Ovde je Address `192.168.1.19`.


![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)


Da biste pristupili kontrolnoj tabli, jednostavno unesite ovaj Address u vaš internet pregledač.


Na komandnoj tabli, pronaći ćete sve informacije prikazane na malom ekranu, koje ćemo sada detaljno razmotriti.


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

Možete promeniti Wi-Fi ili podešavanja bazena u bilo kom trenutku bez ikakvih problema.

U zavisnosti od ventilacije i temperature vaše sobe, možda ćete morati povećati ili smanjiti performanse kako temperatura ne bi prešla 65°C. Ako povećate performanse, zaradićete više satoshija, ali će vaš BitAxe takođe trošiti više električne energije!