---
name: Bitaxe
description: Как да настроите BitAxe?
---
![video](https://youtu.be/tvLSK8v0MK8)


## Въведение


BitAxe е проект с отворен код, създаден от Skot и [достъпен в GitHub](https://github.com/skot/bitaxe), който позволява икономически ефективни експерименти с mining.


Той е направил обратен инженеринг на работата на известния Antminer S19 на Bitmain, лидер на пазара на ASIC, специализираните машини за биткойн mining. Сега е възможно тези мощни чипове да се използват в нови проекти с отворен код. За разлика от Nerdminer, BitAxe разполага с достатъчна изчислителна мощност, за да бъде свързан към пул mining, което ще ви позволи редовно да печелите по няколко сатоши. Nerdminer, от друга страна, може да бъде свързан само към т.нар. солопул, който функционира като лотариен билет: имате малък шанс да спечелите пълната награда за блока.


Съществуват няколко версии на BitAxe с различни чипове и характеристики:


| Bitaxe Model Series      | ASIC Chip | Used On                     | Expected Hash Rate          | Ideal For                                                                                                  |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Series 100)  | 1 x BM1397| Antminer Series 17          | 400 GH/s (up to 450 GH/s)   | Bitcoin mining beginners, offering a solid hash rate with moderate power consumption.                      |
| Bitaxe Ultra (Series 200)| 1 x BM1366| Antminer S19 XP and S19k Pro| 500 GH/s (up to 550 GH/s)   | Serious miners aiming to balance efficiency and higher hash rate.                                          |
| Bitaxe Hex (Series 300)  | 6 x BM1366| Antminer S19k Pro and S19 XP| 3.0 TH/s (up to 3.3 TH/s)   | Miners seeking scalability and high performance without sacrificing efficiency.                             |
| Bitaxe Supra (Series 400)| 1 x BM1368| Antminer S21                | 600 GH/s (up to 700 GH/s)   | Serious enthusiasts seeking the highest hash rates and efficiency.                                         |

В този урок ще използваме BitAxe Ultra 204, оборудван с чип BM1366, използван за Antminer S19XP. Този модел е вече сглобен и флашнат от търговеца на дребно.


[Списъкът на дистрибуторите е достъпен на тази страница](https://bitaxe.org/legit.html)


![signup](assets/2.webp)


Обикновено захранването се продава заедно с него. В противен случай ще трябва да закупите захранване с кабел за жак 5 V и поне 4 A.


![signup](assets/1.webp)


## Конфигурация

Когато включите BitAxe за първи път, той ще се опита да се свърже с Wi-Fi мрежа по подразбиране. След пет опита тя ще покаже името на собствената си Wi-Fi мрежа, за да можете да се свържете с нея и да я конфигурирате.

За целта можете да използвате всеки компютър или смартфон. Влезте в настройките на Wi-Fi, потърсете нови мрежи и ще видите Wi-Fi, наречена Bitaxe_XXXX. Тук тя е `Bitaxe_A859`. Свържете се с тази Wi-Fi мрежа и автоматично ще се отвори прозорец.


![signup](assets/3.webp)


В този прозорец щракнете върху трите малки хоризонтални ленти в горния ляв ъгъл и след това върху `Настройки`.


![signup](assets/4.webp)


Ще трябва да въведете ръчно информацията за Wi-Fi мрежата си, тъй като няма система за автоматично откриване.


![signup](assets/5.webp)


Затова посочете SSID на Wi-Fi, т.е. името на вашата мрежа, паролата, както и информацията за избрания от вас пул mining. Бъдете внимателни, тук URL адресът на пула не е представен по същия начин. Например за Braiins предоставеният URL адрес на пула е: `stratum+tcp://eu.stratum.braiins.com:3333`.


![signup](assets/6.webp)


Както можете да видите на екрана, трябва да премахнете частите `stratum+tcp://` и `:3333`, като оставите само `eu.stratum.braiins.com`. След това в полето `Port` въведете 4-те цифри в края на URL адреса, даден от пула, но без `:`. Тук това е `3333`.


В този урок използваме басейна Braiins mining, но вие можете да изберете друг. Можете да намерите нашите уроци за басейни mining [на уебсайта на Plan ₿ Academy](https://planb.academy/en/tutorials/mining).


След това в полето `User` (Потребител) въведете своя идентификатор и след това `Password` (Парола), обикновено това е `"x"` или `"Anything123"`.


Настройката `Core Voltage` трябва да бъде оставена на `1200` по подразбиране, а за `Frequency` (Честота) също трябва да оставите първоначалната стойност по подразбиране. По-късно ще бъде възможно да коригирате тази настройка, за да получите по-голяма изчислителна мощност. Важно е обаче да се уверите, че температурата на чипа не надвишава 65-70°C, тъй като BitAxe не разполага със система за намаляване на производителността в случай на прегряване. Ако температурата надвиши твърде много 65°C, това може да повреди вашия BitAxe.


![signup](assets/7.webp)


След като сте въвели правилно всички настройки, щракнете върху бутона `Save` (Запази) в долната част, след което рестартирайте BitAxe, като просто го изключите от електрическата мрежа и го включите отново.

Ако сте въвели правилно информацията, устройството трябва бързо да се свърже с Wi-Fi, след това с басейна mining и да започне да показва информация на малкия си екран. Вероятно ще са необходими няколко минути, за да се появи на таблото за управление на басейна mining.

## Информационно табло и екран


Ще се превъртят три различни дисплея. На третата страница ще видите информацията за `IP`, която е IP адресът, който ви позволява да се свържете с таблото за управление. Тук адресът е `192.168.1.19`.


![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)


За да получите достъп до таблото за управление, просто въведете този адрес в интернет браузъра си.


На таблото за управление ще намерите цялата информация, изведена на малкия екран, която сега ще разгледаме подробно.


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

Можете да промените настройките на Wi-Fi или басейна по всяко време без проблем.

В зависимост от вентилацията и температурата в помещението може да се наложи да увеличите или да намалите производителността, така че температурата да не надвишава 65°C. Ако увеличите производителността, ще спечелите повече сатоши, но вашият BitAxe ще консумира и повече електроенергия!