---
name: Seedkeeper - Správce hesel
description: Jak uložit hesla pomocí čipové karty Seedkeeper?
---

![cover](assets/cover.webp)



Seedkeeper je čipová karta vyvinutá belgickou společností Satochip, která se specializuje na hardwarová řešení pro správu a ochranu digitálních tajemství. Společnost Satochip, známá svou řadou čipových karet pro ekosystém Bitcoin, koncipovala Seedkeeper jako alternativu k tradičním metodám ukládání mnemotechnických frází a dalších digitálních tajemství.



Konkrétně má Seedkeeper podobu multifunkční čipové karty s certifikací EAL6, která je vybavena zabezpečeným procesorem a pamětí odolnou proti manipulaci (tzv. "Secure Element"). Jak již název napovídá, jeho úkolem je šifrovaně a chráněně ukládat mnemotechniky a hesla portfolia Bitcoin. S nástrojem Seedkeeper můžete svá tajemství generate importovat, organizovat a ukládat přímo do zabezpečeného prvku karty.



Podle mého názoru má Seedkeeper dvě hlavní využití, kterým se budeme věnovat ve dvou samostatných tutoriálech:




- Uložení mnemotechnické fráze Bitcoin**: místo toho, abyste si 12 nebo 24 slov zapisovali na papír, můžete je importovat na čipovou kartu a chránit je kódem PIN.
- Správa hesel**: prostřednictvím aplikace Seedkeeper můžete používat silná hesla generate a ukládat je přímo na čipové kartě, čímž získáte pohodlného a snadno použitelného offline správce hesel.



Z technického hlediska má Seedkeeper kapacitu 8192 bajtů, což mu umožňuje uložit minimálně 50 samostatných tajemství (přesný počet závisí na jejich velikosti a metadatech, která jsou s nimi spojena). Ke službě Seedkeeper lze přistupovat buď [prostřednictvím čtečky čipových karet připojené](https://satochip.io/accessories/) k počítači, nebo prostřednictvím mobilní aplikace s připojením NFC. Celý systém funguje v offline režimu, bez připojení k internetu, což zaručuje omezený prostor pro útoky.



![Image](assets/fr/001.webp)



Zvláště zajímavou funkcí je možnost duplikovat obsah jednoho Seedkeeperu do druhého a vytvořit tak zálohu. V tomto návodu vám ukážeme, jak to udělat.



V tomto návodu se budeme zabývat pouze použitím nástroje SeedKeeper pro tradiční hesla na způsob správce hesel. Pokud chcete SeedKeeper používat k ukládání mnemotechnických frází Bitcoin wallet, podívejte se na tento další návod:



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1. Jak získám Seedkeeper?



Seedkeeper můžete získat dvěma hlavními způsoby. Můžete si ho [koupit přímo v oficiálním obchodě společnosti Satochip](https://satochip.io/product/seedkeeper/) nebo u autorizovaného prodejce. Protože je však [applet Seedkeeper open-source](https://github.com/Toporin/Seedkeeper-Applet), máte také možnost si jej sami nainstalovat na [prázdnou čipovou kartu](https://satochip.io/product/blank-javacard-for-diy-project/).



Pokud chcete využívat zálohovací funkce Seedkeeperu, budete si zřejmě muset zakoupit dvě čipové karty.



## 2. Instalace klienta Seedkeeper



Prvním krokem je instalace softwaru do počítače nebo chytrého telefonu. V počítači musíte [stáhnout nejnovější verzi programu Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). V mobilních telefonech je aplikace Seedkeeper k dispozici v [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) a v [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 3. Inicializace správce osiva



Spusťte aplikaci a klikněte na tlačítko "*Kliknout a skenovat*".



![Image](assets/fr/003.webp)



Budete požádáni o zadání kódu PIN pro váš Seedkeeper. Jelikož se jedná o novou kartu, nebyl dosud definován žádný PIN kód. Chcete-li tento krok přeskočit, zadejte libovolný kód a klikněte na tlačítko "*Další*".



![Image](assets/fr/004.webp)



Poté kartu přiložte na zadní stranu smartphonu. Aplikace zjistí, že aplikace Seedkeeper ještě nebyla inicializována, a vyzve vás k nastavení kódu PIN čipové karty o délce 4 až 16 znaků. Pro optimální zabezpečení zvolte robustní kód PIN, který bude co nejdelší, náhodný a složený z různých znaků. Tento kód PIN je jedinou překážkou proti fyzickému přístupu k vašim heslům.



**Nezapomeňte si tento kód PIN uložit**, například do správce hesel nebo na samostatné fyzické médium. V druhém případě nikdy neuchovávejte médium obsahující PIN na stejném místě jako Seedkeeper, jinak se toto zabezpečení stane zbytečným. Je důležité mít spolehlivou zálohu: bez PIN kódu nebudete moci obnovit tajemství uložená v zařízení Seedkeeper.



![Image](assets/fr/005.webp)



Potvrďte kód PIN podruhé.



![Image](assets/fr/006.webp)



Váš Seedkeeper je nyní inicializován. Můžete jej odemknout zadáním právě nastaveného kódu PIN.



![Image](assets/fr/007.webp)



Nyní budete přesměrováni na stránku pro správu čipových karet.



![Image](assets/fr/008.webp)



## 4. Uložení hesel v aplikaci Seedkeeper



Po odemčení nástroje Seedkeeper klikněte na tlačítko "*+*".



![Image](assets/fr/009.webp)



Vyberte možnost "Generovat tajné*". Možnost "*Importovat tajenku*" umožňuje uložit existující tajenku (například heslo, které jste vytvořili v minulosti).



![Image](assets/fr/010.webp)



V našem případě chceme uložit heslo. Klikněte na "*Heslo*".



![Image](assets/fr/011.webp)



Přiřaďte tomuto tajemství "*Značku*", abyste jej mohli snadno identifikovat, pokud v nástroji Seedkeeper uložíte více informací. Můžete také přidat identifikátor spojený s heslem a adresou URL webu.



![Image](assets/fr/012.webp)



Zvolte délku a parametry hesla, klikněte na "*Generovat*" a poté na "*Importovat*".



![Image](assets/fr/013.webp)



Umístěte zařízení Seedkeeper na zadní stranu smartphonu.



![Image](assets/fr/014.webp)



Vaše heslo bylo zaregistrováno.



![Image](assets/fr/015.webp)



## 5. Přístup k vašemu heslu Seedkeeper



Pokud chcete zkontrolovat heslo, vezměte nástroj Seedkeeper a klikněte na tlačítko "*Kliknout a skenovat*".



![Image](assets/fr/016.webp)



Zadejte kód PIN a stiskněte tlačítko "*Další*".



![Image](assets/fr/017.webp)



Umístěte zařízení Seedkeeper na zadní stranu smartphonu.



![Image](assets/fr/018.webp)



Tím se dostanete na seznam všech vašich registrovaných tajemství. V tomto příkladu chci zobrazit heslo pro svůj účet Plan ₿ Academy, proto na něj kliknu.



![Image](assets/fr/019.webp)



Stiskněte tlačítko "*Odhalit*".



![Image](assets/fr/020.webp)



Znovu prohledejte nástroj Seedkeeper.



![Image](assets/fr/021.webp)



Na obrazovce se nyní zobrazí dříve uložené heslo. Můžete si ho zkopírovat a použít na příslušné webové stránce.



![Image](assets/fr/022.webp)



## 6. Zálohování aplikace Seedkeeper



Nyní vytvoříme zálohu mého nástroje Seedkeeper na druhém nástroji Seedkeeper, abychom měli dvě kopie. Tato redundance může být součástí strategie zabezpečení vašich nejdůležitějších hesel: například uložení vašich Seedkeeperů na dvou různých místech, aby se omezila fyzická rizika, nebo svěření kopie důvěryhodnému příbuznému.



K tomu si vezměte s sebou druhého hlídače semen (nezapomeňte jeden z nich označit značkou, aby nedošlo k záměně). Začněte jeho inicializací, jak je popsáno v kroku 3 tohoto návodu. Opět zvolte silný kód PIN. V závislosti na vaší strategii se můžete rozhodnout pro jiný kód PIN nebo si ponechat stejný.



![Image](assets/fr/023.webp)



Otevřete aplikaci, klikněte na "*Click & Scan*", zadejte kód PIN zařízení Seedkeeper č. 1 (zdroj) a poté jej naskenujte.



![Image](assets/fr/024.webp)



Tím se dostanete na domovskou stránku se seznamem vašich tajemství. Klikněte na tři malé tečky v pravém horním rohu rozhraní.



![Image](assets/fr/025.webp)



Vyberte možnost "*Provádět zálohování*" a stiskněte tlačítko "*Spustit*".



![Image](assets/fr/026.webp)



Zadejte PIN kód záložní karty (Seedkeeper č. 2).



![Image](assets/fr/027.webp)



Poté kartu naskenujte.



![Image](assets/fr/028.webp)



Totéž proveďte s hlavní kartou (Seedkeeper č. 1) a poté klikněte na "*Provést zálohu*".



![Image](assets/fr/029.webp)



Váš Seedkeeper č. 2 nyní obsahuje všechna tajemství uložená v Seedkeeperu č. 1.



![Image](assets/fr/030.webp)



Pro kontrolu zkopírování tajemství můžete naskenovat zařízení Seedkeeper č. 2.



![Image](assets/fr/031.webp)



To je vše! Nyní víte, jak používat Seedkeeper k ukládání hesel. V některém z příštích tutoriálů se podíváme na to, jak používat Seedkeeper k zálohování Bitcoin wallet. Zvu vás také k objevení jeho kombinovaného použití se SeedSignerem :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356