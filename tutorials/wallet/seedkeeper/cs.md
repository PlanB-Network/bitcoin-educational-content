---
name: Seedkeeper
description: Jak mohu zálohovat své zařízení wallet Bitcoin pomocí čipové karty Seedkeeper?
---

![cover](assets/cover.webp)



Seedkeeper je čipová karta vyvinutá belgickou společností Satochip, která se specializuje na hardwarová řešení pro správu a ochranu digitálních tajemství. Společnost Satochip, známá svou řadou čipových karet pro ekosystém Bitcoin, navrhla Seedkeeper jako alternativu k tradičním metodám ukládání mnemotechnických frází.



Konkrétně má Seedkeeper podobu multifunkční čipové karty s certifikací EAL6, která je vybavena zabezpečeným procesorem a pamětí odolnou proti manipulaci (tzv. "Secure Element"). Jak již název napovídá, jeho úkolem je šifrovaně a chráněně ukládat mnemotechnické údaje Bitcoin wallet a hesla. Pomocí nástroje Seedkeeper můžete svá tajemství generate importovat, organizovat a ukládat přímo do zabezpečeného prvku karty.



Podle mého názoru má Seedkeeper dvě hlavní využití, kterým se budeme věnovat ve dvou samostatných tutoriálech:




- Uložení mnemotechnické fráze Bitcoin**: namísto zapisování 12 nebo 24 slov na papír je můžete importovat na čipovou kartu a chránit je kódem PIN.
- Správa hesel**: prostřednictvím aplikace Seedkeeper můžete používat silná hesla generate a ukládat je přímo na čipové kartě, čímž získáte pohodlného a snadno použitelného offline správce hesel.



Z technického hlediska má Seedkeeper kapacitu 8192 bajtů, což mu umožňuje uložit minimálně 50 samostatných tajemství (přesný počet závisí na jejich velikosti a metadatech, která jsou s nimi spojena). Ke službě Seedkeeper lze přistupovat buď [prostřednictvím čtečky čipových karet připojené](https://satochip.io/accessories/) k počítači, nebo prostřednictvím mobilní aplikace s připojením NFC. Celý systém funguje v offline režimu, bez připojení k internetu, což zaručuje omezený prostor pro útoky.



![Image](assets/fr/001.webp)



Zvláště zajímavou funkcí je možnost duplikovat obsah jednoho Seedkeeperu do druhého a vytvořit tak zálohu. V tomto návodu vám ukážeme, jak to udělat.



Seedkeeper je také velmi zajímavý v kombinaci s bezstavovým hardwarem wallet, jako je SeedSigner nebo Specter DIY. V takovém případě není třeba používat klienta Satochip v počítači nebo mobilním telefonu. Seedkeeper uchovává seed ve svém secure element a lze jej používat přímo s podepisovacím zařízením, čímž odpadá potřeba papírového QR kódu. Tento konkrétní případ použití nebudu v tomto tutoriálu rozvíjet, protože je předmětem jiného specializovaného tutoriálu :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1. Jaký je případ použití nástroje Seedkeeper?



V tomto tutoriálu se budu zabývat pouze případy použití souvisejícími s Bitcoin, protože o tom je tento tutoriál. Nebudeme se zabývat funkcemi správy hesel, které budou předmětem jiného tutoriálu.



Ve srovnání s prostou papírovou zálohou mnemotechnické fráze má použití Seedkeeperu několik výhod:





- Odolný proti krádeži:** Číslo seed ve vašem čísle wallet není přístupné v otevřeném textu. K jeho extrakci potřebujete znát PIN kód Seedkeepera. Zloděj, který se zařízení zmocní, s ním bez tohoto kódu nebude moci nic dělat.





- Rozložení rizika na dva faktory:** můžete rozdělit zabezpečení na digitální a fyzický faktor. Pokud například uložíte PIN kód Seedkeeper do správce hesel, budete k získání seed potřebovat jak přístup k tomuto správci, tak fyzické držení čipové karty (výrazně nižší pravděpodobnost útoku).





- Centralizovaná správa:** Seedkeeper usnadňuje správu více osiv z různých portfolií.





- Snadné zálohování:** jednoduše duplikujte zašifrované zálohy do jiných SeedKeepers.



V porovnání s jednoduchou papírovou zálohou seed má však řadu nevýhod:





- Cena:** je sice mírná (asi 25 eur), ale stále vyšší než cena listu papíru.





- Závislost na univerzálním výpočetním zařízení:** zadávání a správa seed vyžaduje počítač nebo chytrý telefon, což znamená, že vaše mnemotechnika prochází strojem s mnohem širším povrchem pro útoky než hardware wallet. To může představovat riziko, pokud je stroj kompromitován. Proto nedoporučuji používat Seedkeeper k ukládání seed hardwaru wallet (s výjimkou bezstavového použití bez počítače, jako je tomu u SeedSigner). Úkolem hardwaru wallet je právě ukládání seed v minimalistickém, vysoce zabezpečeném prostředí. Ručním zadáním kódu seed do běžného počítače již není omezen na hardware wallet: ocitá se také na univerzálním počítači, který je vystaven mnoha vektorům útoku. Proto je lepší používat Seedkeeper pro horký wallet než pro studený (s výjimkou SeedSigner / bezstavový hardware wallet).





- Riziko ztráty spojené s PIN:** přímá nedostupnost seed na rozdíl od papírové zálohy skutečně poskytuje ochranu proti fyzické krádeži. Jako vždy je však zabezpečení otázkou rovnováhy mezi rizikem krádeže a rizikem ztráty. Pokud vaše záloha vyžaduje PIN, ztráta tohoto kódu znemožní obnovení mnemotechnické fráze, a tím i přístup k vašim bitcoinům.



Vzhledem k těmto výhodám a nevýhodám se domnívám, že nejlepší využití nástroje Seedkeeper (kromě jeho funkce správce hesel) je jednak ukládání semínek z vašeho **softwarového portfolia**, protože se již nacházejí ve vašem telefonu nebo počítači, nebo z vašeho bezobrazovkového hardwaru wallet, jako je Satochip, a jednak jeho použití v kombinaci s bezobrazovkovým hardwarem wallet, jako je SeedSigner, kde se skutečně uplatní.



Dalším obzvláště zajímavým případem použití nástroje Seedkeeper je možnost bezpečného a spolehlivého zálohování *Deskriptorů* vašich portfolií.



## 2. Jak získám Seedkeeper?



Seedkeeper můžete získat dvěma hlavními způsoby. Můžete si ho [koupit přímo v oficiálním obchodě společnosti Satochip](https://satochip.io/product/seedkeeper/) nebo u autorizovaného prodejce. Protože je však [applet Seedkeeper open-source](https://github.com/Toporin/Seedkeeper-Applet), máte také možnost si jej sami nainstalovat na [prázdnou čipovou kartu](https://satochip.io/product/blank-javacard-for-diy-project/).



Pokud chcete využívat zálohovací funkce Seedkeeperu, budete si zřejmě muset zakoupit dvě čipové karty.



## 3. Instalace klienta Seedkeeper



V tomto návodu budeme zálohovat naše portfolio seed v nástroji Seedkeeper. Prvním krokem je instalace softwaru do počítače nebo chytrého telefonu. V počítači je třeba [stáhnout nejnovější verzi programu Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases). V mobilních zařízeních je aplikace Seedkeeper k dispozici v [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) a také v [Apple App Store](https://apps.apple.com/be/app/seedkeeper/id6502836060).



![Image](assets/fr/002.webp)



## 4. Inicializace správce osiva



Spusťte aplikaci a klikněte na tlačítko "*Kliknout a skenovat*".



![Image](assets/fr/003.webp)



Budete požádáni o zadání kódu PIN pro váš Seedkeeper. Jelikož se jedná o novou kartu, nebyl dosud definován žádný PIN kód. Chcete-li tento krok přeskočit, zadejte libovolný kód a klikněte na tlačítko "*Další*".



![Image](assets/fr/004.webp)



Poté kartu přiložte na zadní stranu smartphonu. Aplikace zjistí, že aplikace Seedkeeper ještě nebyla inicializována, a vyzve vás k nastavení kódu PIN čipové karty o délce 4 až 16 znaků. Pro optimální zabezpečení zvolte silné heslo, které bude co nejdelší, náhodné a složené z různých znaků. Tento kód PIN je jedinou překážkou proti fyzickému přístupu k vaší frázi pro obnovení.



**Nezapomeňte si tento kód PIN uložit**, například do správce hesel nebo na samostatné fyzické médium. V druhém případě nikdy neuchovávejte médium obsahující PIN na stejném místě jako Seedkeeper, jinak se toto zabezpečení stane zbytečným. Je důležité mít spolehlivou zálohu: bez PIN kódu nebudete moci obnovit tajemství uložená v zařízení Seedkeeper.



![Image](assets/fr/005.webp)



Potvrďte kód PIN podruhé.



![Image](assets/fr/006.webp)



Váš Seedkeeper je nyní inicializován. Můžete jej odemknout zadáním právě nastaveného kódu PIN.



![Image](assets/fr/007.webp)



Nyní budete přesměrováni na stránku pro správu čipových karet.



![Image](assets/fr/008.webp)



## 5. Registrace seed v nástroji Seedkeeper



Po odemčení nástroje Seedkeeper klikněte na tlačítko "*+*".



![Image](assets/fr/009.webp)



Vyberte možnost "Importovat tajné*". Možnost "*Vygenerovat tajenku*" umožňuje vytvořit novou mnemotechnickou frázi přímo z aplikace.



![Image](assets/fr/010.webp)



V našem případě chceme v našem portfoliu zachránit společnost seed. Klikněte na "*Mnemonic*".



![Image](assets/fr/011.webp)



Přiřaďte tomuto tajemství "*Značku*", abyste jej mohli snadno identifikovat, pokud v nástroji Seedkeeper uložíte více informací.



![Image](assets/fr/012.webp)



Poté zadejte frázi pro obnovení do příslušného pole. Pokud si přejete, můžete také přidat passphrase BIP39 nebo své *Deskriptory*. Poté klikněte na tlačítko "Importovat*".



![Image](assets/fr/013.webp)



*Mnemotechnická pomůcka zobrazená na tomto obrázku je smyšlená a nikomu nepatří. Jedná se pouze o příklad. Nikdy nikomu neprozrazujte vlastní mnemotechniku, jinak vám budou bitcoiny ukradeny



Umístěte zařízení Seedkeeper na zadní stranu smartphonu.



![Image](assets/fr/014.webp)



Vaše zařízení seed bylo zaregistrováno.



![Image](assets/fr/015.webp)



## 6. Přístup ke svému účtu seed v nástroji Seedkeeper



Pokud si chcete zkontrolovat svou mnemotechnickou frázi, vezměte si nástroj Seedkeeper a klikněte na tlačítko "*Kliknout a skenovat*".



![Image](assets/fr/016.webp)



Zadejte kód PIN a stiskněte tlačítko "*Další*".



![Image](assets/fr/017.webp)



Umístěte zařízení Seedkeeper na zadní stranu smartphonu.



![Image](assets/fr/018.webp)



Tím se dostanete na seznam všech vašich registrovaných tajemství. V tomto příkladu chci zobrazit seed svého portfolia "*Blockstream App*", takže na něj kliknu.



![Image](assets/fr/019.webp)



Stiskněte tlačítko "*Odhalit*".



![Image](assets/fr/020.webp)



Znovu prohledejte nástroj Seedkeeper.



![Image](assets/fr/021.webp)



Na obrazovce se nyní zobrazí dříve nahraná mnemotechnická fráze.



![Image](assets/fr/022.webp)



## 7. Zálohování aplikace Seedkeeper



Nyní vytvoříme zálohu mého nástroje Seedkeeper na druhém nástroji Seedkeeper, abychom měli dvě kopie. Tato redundance může být součástí strategie zabezpečení vašich bitcoinů: například uložení vaší fáze na dvou oddělených místech, aby se omezila fyzická rizika, nebo svěření kopie důvěryhodnému příbuznému v rámci dědického plánu.



K tomu si vezměte s sebou druhého hlídače semen (nezapomeňte jeden z nich označit značkou, aby nedošlo k záměně). Začněte jeho inicializací, jak je popsáno v kroku 4 tohoto návodu. Opět zvolte silné heslo. V závislosti na vaší strategii se můžete rozhodnout pro jiné heslo nebo ponechat stejné.



![Image](assets/fr/023.webp)



Otevřete aplikaci, klikněte na "*Click & Scan*", zadejte heslo svého Seedkeepera č. 1 (zdroj) a poté jej naskenujte.



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



To je vše! Nyní již víte, jak pomocí nástroje Seedkeeper uložit mnemotechnickou frázi Bitcoin wallet. V některém z příštích tutoriálů se podíváme na to, jak používat Seedkeeper k ukládání hesel. Zvu vás také k objevení jeho kombinovaného použití se SeedSignerem :



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

V tomto návodu jsme několikrát zmínili ***Deskriptory*** v portfoliu Bitcoin. Nevíte, co jsou zač? V tom případě vám doporučuji absolvovat náš bezplatný vzdělávací kurz CYP 201, který se podrobně věnuje všem mechanismům souvisejícím s provozem portfolia HD!



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f