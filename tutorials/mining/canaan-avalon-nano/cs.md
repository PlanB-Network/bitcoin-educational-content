---
name: Canaan Avalon Nano 3S
description: Konfigurace zařízení ASIC Avalon pro solomining nebo sdružování Miner
---

![cover](assets/cover.webp)



V tomto návodu se podíváme na to, jak nastavit Canaan Avalon Nano 3S pro snadné domácí použití Miner.



Až dosud byly stroje ASIC (*Application Specific Integrated Circuit*) speciálně navržené k provádění určitého úkolu - v tomto případě výpočtu Hash (SHA-256) pro Miner z Bitcoin - pro domácí použití obzvláště nevhodné. Obtěžující hluk, generované teplo a nutnost přizpůsobit elektrickou instalaci tak, aby podporovala obrovský výkon těchto zařízení, bránily většině z nás v účasti.



Dnes se společnost Canaan, jeden z předních výrobců strojů ASIC, rozhodla oslovit trh soukromých osob, které chtějí mít doma Miner, a nabízí řadu výrobků, které jsou relativně tiché a velmi snadno se instalují (plug & play).



Tato zařízení se prodávají buď jako přídavné topení v případě modelu **Avalon Nano 3S (140 W)**, nebo jako miniaturní chladič s výkonem **800 W** v případě modelu **Avalon Mini 3**.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

Vezměte prosím na vědomí, že cenový rozdíl oproti tradičním ohřívačům stejného výkonu vám v naprosté většině případů neumožní dosáhnout finančního zisku. Saturace vygenerovaná činností Mining tento cenový rozdíl nikdy nevyrovná, pokud nemáte přístup k bezplatné (přebytečné) nebo velmi levné elektřině.



Podle mého názoru by tato zařízení měla být vnímána spíše jako jednoduchý způsob, jak doma používat Miner pro ty, kteří si to přejí z osobních důvodů: *a zároveň **jako bonus** využívat teplo vyrobené k vytápění svého pokoje v zimě.* Nikoliv však jako způsob úspory peněz, alespoň ve většině případů (západní země).



## Rozbalení a funkce



Nejprve se podívejme, co se nachází uvnitř krabičky Avalon Nano 3S.



![image](assets/fr/01.webp)




![image](assets/fr/02.webp)



Po otevření krabice najdete kartonové pouzdro obsahující přijímač WIFI, který, jak uvidíme později, musíte zapojit do portu USB zařízení, abyste se mohli připojit k místní síti. Součástí balení je také návod k použití a kovový kolík pro případné obnovení továrního nastavení zařízení.



![image](assets/fr/03.webp)




![image](assets/fr/04.webp)



Jakmile je vše vybaleno z krabice, máte po ruce: samozřejmě samotný přístroj, uživatelskou příručku, přijímač WIFI, výše zmíněný kovový hrot a napájení přístroje Supply. Dodávaná kreditní karta podle našeho názoru nestojí za zmínku.



![image](assets/fr/05.webp)



Níže je uvedena tabulka shrnující obecné technické specifikace modelu Nano 3S :



| Caractéristique                                      | Valeur                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Taux de hachage                                      | 6 Th/s +- 5%                                            |
| Consommation d'énergie                               | 140 W                                                   |
| Bruit                                                | 30 - 40 dB                                              |
| Plage de température de sortie d'air                 | 60-70°C (sous température ambiante 25°C)                |
| Exigences de température ambiante pour l'utilisation | de -5 à 30°C                                            |
| Plage d'entrée de l'appareil                         | 28V 5A continu                                          |
| Plage d'entrée de l'adaptateur                       | 110-240V AC 50/60Hz                                     |
| Taille de la machine                                 | Longueur: 205 mm /  Largeur: 115 mm / Hauteur:  58.5 mm |
| Poids de la machine                                  | 0.86 kg                                                 |

## Zapnutí a připojení k místní síti



Po vybalení umístěte zařízení Avalon Nano 3 S pokud možno na relativně otevřené místo, aby mohlo teplo cirkulovat. Poté začněte vložením malého modulu přijímače WIFI, jak je znázorněno níže:



![image](assets/fr/06.webp)


Poté zapojte konektor USB-C napájecího adaptéru Supply do portu USB-C zařízení a napájejte jej.



![image](assets/fr/07.webp)


![image](assets/fr/08.webp)



Zařízení se spustí a na obrazovce se objeví logo Avalon Nano, následované logem "mobilního telefonu" se slovy "Please Configure the Network With Avalon Family App".



![image](assets/fr/09.webp)




![image](assets/fr/10.webp)



Za tímto účelem přejděte do obchodu s mobilními aplikacemi, vyhledejte a stáhněte aplikaci **Avalon Family**.



![image](assets/fr/11.webp)


Po instalaci ji otevřete kliknutím na tlačítko "Přeskočit" v pravém horním rohu, poté na tlačítko "Přidat" a nakonec na "Hledat". Ujistěte se, že máte ve smartphonu povolenou funkci Bluetooth, aby detekce zařízení proběhla bez problémů.



![image](assets/fr/12.webp)


Jakmile aplikace detekuje zařízení, klikněte na něj a vyberte možnost "Připojit". Poté se zobrazí obrazovka, kde můžete zadat údaje o připojení WIFI.


![image](assets/fr/13.webp)


Po připojení zařízení k místní síti bude obrazovka vypadat takto:



![image](assets/fr/14.webp)



Zobrazuje "fiktivní" Hashrate, protože dosud nebyl nakonfigurován žádný pool, a čas, datum, napájení a IP zařízení Address - velmi užitečné, pokud chcete přistupovat k Interface zařízení prostřednictvím počítače a prohlížeče (více o tom později).



![image](assets/fr/15.webp)




## Připojení k zařízení Mining pool



**Tato část je společná pro modely Nano 3s a Mini 3, protože procesy jsou naprosto identické**.



Ať už chceme "solominovat" nebo "poolovat" Miner, budeme se muset připojit k Mining pool. Naše zařízení není vlastně nic jiného než Hash-výrobce bez povědomí o síti Bitcoin. Připojení k poolu mu umožní přístup k síti Bitcoin a umožní mu přijímat šablony bloků, se kterými může pracovat.



### Použití aplikace k připojení k zařízení Mining pool



V aplikaci Avalon Family vyberte zařízení, jak je znázorněno níže. Poté budete automaticky vyzváni ke změně hesla správce zařízení. Pokud tak chcete učinit, klikněte na tlačítko "OK", nebo na tlačítko zrušit, chcete-li ponechat výchozí přístupové heslo "admin".


![image](assets/fr/16.webp)


Poté zvolte "Settings", poté "Pool Config" a zadejte parametry pro 3 požadované pooly.


Bazény č. 2 a č. 3 budou sloužit jako záloha pro případ selhání jednoho z nich, takže váš Miner nebude fungovat zbytečně. Ve výchozím nastavení bude Hashrate nasměrován do fondu č. 1



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


Restartujte přístroj podle pokynů a počkejte několik minut, dokud se Hashrate nenamíří na preferovaný bazén (#1).



### Použití prohlížeče k připojení k zařízení Mining pool



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



V aplikaci rodiny Avalon klikněte na ikonu odpovídající zařízení Avalon Nano 3S.


poté se zobrazí 3 nabídky: "Pracovní režim", "Ovládání světla" a "Nastavení". Nejprve klikněte na "Pracovní režim". Poté se vám nabídnou 3 režimy výkonu vašeho stroje.



**Nízká**: přináší přibližně 3 Th/s Hashrate při spotřebě 70 W energie


**Střední**: přináší přibližně 4,5 Th/s Hashrate při spotřebě 100 W


**Vysoká**: poskytne vám přibližně 6 Th/s Hashrate při maximální spotřebě 140 W



![image](assets/fr/31.webp)


Udělejme krok zpět a prozkoumejme nabídku "Ovládání světla". Ta je čistě kosmetická. K dispozici je celá řada možností pro změnu barvy, intenzity, tepla, vypnutí LED diod zařízení v noci atd... Snadno to zjistíte sami.



![image](assets/fr/32.webp)


![image](assets/fr/33.webp)



![image](assets/fr/34.webp)



A konečně poslední nabídkou, kterou máme k dispozici, je nabídka "Nastavení", kterou jsme již viděli při připojování k bazénům Mining. Zde můžete spravovat své bazény, měnit heslo správce zařízení a sledovat různé ukazatele, jako je datum vypršení záruky, čistota filtrů nebo způsob kontaktování podpory v případě poruchy.



![image](assets/fr/35.webp)


Pro údržbu a udržení co nejčistšího filtru doporučujeme používat vysavač a pravidelně vysávat vstupy a výstupy vzduchu, aby se zabránilo jejich ucpání.



Dostali jsme se na konec tohoto návodu, ve kterém jsme se dozvěděli, jak připojit zařízení Avalon Nano 3 S k místní síti, jak nasměrovat naše zařízení Hashrate na bazény Mining a jak procházet možnosti a nastavení pomocí aplikace Avalon Family.



Chcete-li se dozvědět více, podívejte se na náš návod k vyšší verzi modelu Avalon: Mini 3.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7