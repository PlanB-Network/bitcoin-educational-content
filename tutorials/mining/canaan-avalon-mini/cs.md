---
name: Canaan Avalon Mini 3
description: Konfigurace zařízení ASIC Avalon pro solomining nebo sdružování Miner
---

![cover](assets/cover.webp)



V tomto návodu se podíváme na to, jak nastavit zařízení Canaan Avalon Mini 3 pro snadné domácí použití Miner.



Až dosud byly stroje ASIC (*Application Specific Integrated Circuit*) speciálně navržené k provádění určitého úkolu - v tomto případě výpočtu Hash (SHA-256) pro Miner z Bitcoin - pro domácí použití obzvláště nevhodné. Obtěžující hluk, generované teplo a nutnost přizpůsobit elektrickou instalaci tak, aby podporovala obrovský výkon těchto zařízení, bránily většině z nás v účasti.



Dnes se společnost Canaan, jeden z předních výrobců strojů ASIC, rozhodla oslovit trh soukromých osob, které chtějí mít doma Miner, a nabízí řadu výrobků, které jsou relativně tiché a velmi snadno se instalují (plug & play).



Tato zařízení se prodávají buď jako přídavné topení v případě modelu **Avalon Nano 3S (140 W)**, nebo jako miniaturní chladič s výkonem **800 W** v případě modelu **Avalon Mini 3**.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

Vezměte prosím na vědomí, že cenový rozdíl oproti tradičním ohřívačům stejného výkonu vám v naprosté většině případů neumožní dosáhnout finančního zisku. Saturace vygenerovaná činností Mining tento cenový rozdíl nikdy nevyrovná, pokud nemáte přístup k bezplatné (přebytečné) nebo velmi levné elektřině.



Podle mého názoru by tato zařízení měla být vnímána spíše jako jednoduchý způsob, jak doma používat Miner pro ty, kteří si to přejí z osobních důvodů: *a zároveň **jako bonus** využívat teplo vyrobené k vytápění svého pokoje v zimě.* Nikoliv však jako způsob úspory peněz, alespoň ve většině případů (západní země).



## Rozbalení a funkce



### Avalon Nano 3S



Nejprve se podívejme, co se nachází uvnitř krabice Avalon Mini 3.



![image](assets/fr/24.webp)



Po otevření krabice máte přímo před sebou návod k obsluze, ale co je důležitější, modul přijímače WIFI se skrývá pod kulatou bílou nálepkou vlevo od návodu k obsluze. Budete ho potřebovat později.



![image](assets/fr/25.webp)



Pod pěnovým blokem je zařízení, po vyjmutí z krabice pak napájecí jednotka Supply.



![image](assets/fr/26.webp)




![image](assets/fr/27.webp)



## Zapnutí a připojení k místní síti



Po vybalení umístěte zařízení Avalon Mini 3 pokud možno na relativně otevřené místo, aby mohlo teplo řádně cirkulovat. Poté začněte zasunutím malého modulu přijímače WIFI do portu USB na spodní straně zařízení, připojte napájení Supply a ujistěte se, že je tlačítko napájení v poloze "1".



![image](assets/fr/28.webp)



Po dokončení těchto kroků se na displeji LED zařízení rozsvítí symbol "Bluetooth", což znamená, že je zařízení připraveno k připojení k místní síti prostřednictvím aplikace Avalon Family.



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



Za tímto účelem přejděte do obchodu s mobilními aplikacemi, vyhledejte a stáhněte aplikaci **Avalon Family**.



![image](assets/fr/11.webp)


Po instalaci ji otevřete kliknutím na tlačítko "Přeskočit" v pravém horním rohu, poté na tlačítko "Přidat" a nakonec na "Hledat". Ujistěte se, že máte ve smartphonu povolenou funkci Bluetooth, aby detekce zařízení proběhla bez problémů.



![image](assets/fr/12.webp)


Jakmile aplikace detekuje zařízení, klikněte na něj a vyberte možnost "Připojit". Poté se zobrazí obrazovka, kde můžete zadat údaje o připojení WIFI.


![image](assets/fr/13.webp)


Po připojení k místní síti se na displeji zařízení Mini 3 zobrazí informace, jako je IP Address, čas, Hashrate a elektrický výkon.



Níže je uvedena souhrnná tabulka obecných technických specifikací modelu Mini 3:




| Charakteristika                                      | Hodnota                                                    |
| ---------------------------------------------------- | --------------------------------------------------------- |
| Hashrate                                             | 37.5 Th/s +- 5%                                           |
| Spotřeba elektřiny                              | 800 W                                                     |
| Hluk                                                | 35-55 dB                                                  |
| Teplota výstupního vzduchu                       | 60-70°C (při okolní teplotě 25°C)                  |
| Požadavky na okolní teplotu pro použití | -5° C - 40°C                                              |
| Rozsah vstupního napětí zařízení                         | 110V-240V AC 50/60Hz                                      |
| Rozměry stroje                                 | Délka: 760 mm / Hloubka: 104 mm / Výška: 214.5 mm |
| Hmotnost stroje                                  |  8.35 kg                                                  |

## Připojení k zařízení Mining pool



**Tato část je společná pro zařízení Nano 3s a Mini 3, protože procesy jsou naprosto identické **



Ať už chceme "solominovat", nebo "poolovat" Miner, budeme se muset připojit ke Mining pool. Naše zařízení není vlastně nic jiného než Hash-výrobce bez povědomí o síti Bitcoin. Připojení k poolu mu umožní přístup k síti Bitcoin a umožní mu přijímat šablony bloků, se kterými může pracovat.



### Použití aplikace k připojení k zařízení Mining pool



V aplikaci Avalon Family vyberte zařízení, jak je znázorněno níže. Poté budete automaticky vyzváni ke změně hesla správce zařízení. Pokud tak chcete učinit, klikněte na tlačítko "OK", nebo na tlačítko zrušit, chcete-li ponechat výchozí přístupové heslo "admin".


![image](assets/fr/16.webp)


Poté zvolte "Settings", poté "Pool Config" a zadejte parametry pro 3 požadované pooly.


Bazény č. 2 a č. 3 budou sloužit jako záložní v případě selhání jednoho z nich, takže váš Miner nebude fungovat zbytečně. Ve výchozím nastavení bude Hashrate nasměrován do fondu č. 1



V našem případě jsme zvolili:




- 1 - Veřejný bazén,
- 2 - CkPool,
- 3 - Oceán.



![image](assets/fr/17.webp)



Podrobnější informace o připojení k zařízení Mining pool naleznete v těchto výukových materiálech :



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.academy/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

Abychom to shrnuli, potřebujeme





- pool Address, obvykle **stratum+tcp://xxxxxxxx:port**.





- název "pracovníka" složený z *vašeho Bitcoin Address* a *pseudonymu*, který jste si zvolili pro své zařízení, přičemž tyto dva znaky jsou odděleny *tečkou*, například:**bc1qxxxxxxxxxxxxx.MonAvalonNano3S**





- heslo, které je obvykle vždy "**x**"



Po zadání informací o bazénu klikněte na tlačítko "Uložit".



![image](assets/fr/18.webp)


Restartujte přístroj podle pokynů a počkejte několik minut, dokud nebude zařízení Hashrate namířeno na preferovaný bazén (č. 1).



### Použití prohlížeče k připojení k serveru Mining pool



Můžete se také připojit k zařízení Mining pool a obecněji přistupovat k systému správy zařízení Interface prostřednictvím oblíbeného prohlížeče.



Za tímto účelem zadejte do vyhledávacího řádku prohlížeče adresu IP Address zařízení zobrazeného na obrazovce níže, v našem případě **192.168.144.6**



![image](assets/fr/15.webp)



Zobrazí se následující stránka s výzvou k otevření aplikace Avalon Family a naskenování QR kódu zobrazeného v aplikaci.



![image](assets/fr/20.webp)



Otevřete aplikaci a klikněte na 3 pomlčky vpravo nahoře a poté na skenování. Naskenujte QR kód prohlížeče, poté zadejte heslo správce aplikace a klikněte na tlačítko OK.



![image](assets/fr/21.webp)



Zde se nacházíte na webové stránce, která vám umožňuje komunikovat s vaším vozem Avalon. Jedná se spíše o přístrojový panel pro zobrazení metrik stroje než o prostředek pro jeho konfiguraci.



Nastavení bazénu je však stále přístupné tímto způsobem, a to kliknutím na **"Konfigurace bazénu "** v pravém dolním rohu.



![image](assets/fr/22.webp)



Stejně jako v mobilní aplikaci zde můžete zadat parametry bazénu.



![image](assets/fr/23.webp)



## Ovládání zařízení prostřednictvím aplikace Avalon Family



Nyní jsme připojili náš domácí Miner k místní síti a nasměrovali jsme náš Hashrate do bazénů Minings. Nyní si prostřednictvím aplikace Avalon Family odkryjeme základní funkce našeho stroje.



V hlavní nabídce aplikace rodiny Avalon klikněte na ikonu odpovídající zařízení Avalon Mini 3. Dostanete se přímo do nabídky pro správu provozních režimů.



k dispozici jsou 3 možnosti: režim "Heater", režim "Mining" nebo režim "Night".





- V režimu "Heater" máte k dispozici 2 úrovně výkonu "Eco" nebo "Super".


Úroveň "Eco" odpovídá topnému výkonu 500 W při rychlosti Hashrate přibližně 25 Th/s a hladině hluku 40 dB.


Úroveň "Super" odpovídá výstupnímu výkonu 650 W při rychlosti cca 30Th/s a 45 dB. Tento režim umožňuje nastavit maximální teplotu okolí, při jejímž překročení jednotka přestane pracovat.



![image](assets/fr/36.webp)




- V režimu "Mining" pracuje jednotka maximální rychlostí bez možnosti nastavení cílové teploty (samozřejmě kromě vestavěného limitu přehřátí). Cílem je maximálně využít výkon Miner. Zde se výstupní výkon blíží 800 W při rychlosti přibližně 37,5 Th/s a hlučnosti 50-55 dB.



![image](assets/fr/37.webp)


A konečně, v režimu "Noc" pracuje váš Mini 3 při nejnižších možných otáčkách s minimálním hlukem. 400 W, 20 Th/s a přibližně 33 dB.



I zde můžete nastavit cílovou teplotu, při jejímž překročení jednotka přejde do neaktivního režimu a přestane používat Miner. Pokud teplota klesne, jednotka se znovu spustí a obnoví vytápění a Miner. V tomto režimu jsou LED diody na displeji standardně vypnuté, ale v případě potřeby je můžete zapnout, aby osvětlovaly místnost ve tmě jako noční světlo (viz fotografie níže).



![image](assets/fr/38.webp)



![image](assets/fr/39.webp)



Nakonec si můžete pohrát s LED diodami svého Avalonu prostřednictvím nabídky "Displej". Můžete si vybrat, zda chcete procházet příslušné provozní informace, zvolit zobrazení času nebo dokonce vlastní (pixelový) obrázek.



![image](assets/fr/40.webp)



![image](assets/fr/41.webp)



Stejně jako u modelu Avalon Nano 3S můžete v nabídce "Nastavení" změnit heslo správce, nastavení bazénu, zkontrolovat neprůchodnost filtru (nachází se na spodní straně zařízení), kontaktovat podporu nebo zobrazit protokoly zařízení.



![image](assets/fr/42.webp)



Filtr ve spodní části přístroje lze opět čistit vysavačem, čím pravidelněji, tím lépe.



Dostali jsme se na konec tohoto návodu, ve kterém jsme se dozvěděli, jak připojit náš Avalon Mini 3 k místní síti, jak nasměrovat náš Hashrate na bazény Mining a jak procházet možnosti a nastavení pomocí aplikace Avalon Family.



Chcete-li se dozvědět více, podívejte se na náš návod na menší verzi modelu Avalon: Nano 3S.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6