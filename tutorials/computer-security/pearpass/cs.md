---
name: PearPass
description: Získejte zpět kontrolu nad svými hesly pomocí místního správce hesel bez použití cloudu
---

![cover](assets/cover.webp)



V době, kdy každý člověk spravuje desítky, dokonce stovky online účtů, se zabezpečení přihlašovacích údajů stalo ústředním tématem v oblasti IT bezpečnosti. Sociální sítě, systémy pro zasílání zpráv, profesionální služby, finanční platformy: každý z těchto přístupů se opírá o tajemství, jehož prozrazení může mít vážné důsledky pro váš život.



Navzdory rostoucímu počtu útoků jsou mezi lidmi stále rozšířené špatné postupy: slabá hesla, opakovaně používaná hesla, hesla uložená v čistém textu nebo hesla, která se přibližně pamatují. Řešením, jak tyto problémy vyřešit, aniž by si člověk každodenně komplikoval život, je používání správce hesel.



Existují již desítky správců hesel a pro většinu z nich nabízí Plan ₿ Academy výukový program. V tomto tutoriálu bych vám však rád představil jeden, který svým fungováním jasně vybočuje z řady ostatních: **PearPass**.



**PearPass je správce hesel s otevřeným zdrojovým kódem, který je založen na principu peer-to-peer a je navržen tak, aby uživatelům poskytoval úplnou kontrolu nad jejich daty



![Image](assets/fr/01.webp)



## Proč si vybrat PearPass?



Správce hesel je softwarový program, který bezpečně generuje, ukládá a organizuje všechna vaše hesla. Namísto zapamatování nebo opakovaného používání hesel máte k dispozici pouze jedno tajemství: hlavní heslo, které zašifruje celý váš trezor. Tento přístup umožňuje používat jedinečná, dlouhá a náhodná hesla pro každou službu, což snižuje riziko zapomenutí i kompromitace a zároveň omezuje dopad případného úniku. Dnes se jedná o základní nástroj IT, který by měl používat každý.



Existují dvě hlavní kategorie správců hesel. Na jedné straně existuje software pouze pro místní použití, který je velmi bezpečný, protože data nejsou nikdy uložena na centrálním serveru, ale není příliš praktický, protože neumožňuje snadnou synchronizaci přihlašovacích údajů mezi několika zařízeními (počítač, smartphone, tablet...). Naproti tomu cloudoví správci hesel ukládají vaše pověření na svých serverech a synchronizují je ve všech vašich zařízeních. Jejich hlavní výhodou je pohodlí, ale zahrnují kompromis v oblasti bezpečnosti, protože vaše hesla jsou uložena na infrastruktuře, nad kterou nemáte kontrolu.



PearPass se záměrně rozchází s oběma modely. Nachází se mezi místními správci a cloudovými řešeními: umožňuje synchronizaci vašich hesel a zároveň zaručuje, že nebudou nikdy uložena na vzdálených serverech. Ve výsledku jsou všechna vaše pověření uložena lokálně ve vašich zařízeních a synchronizace mezi více počítači probíhá výhradně peer-to-peer. Tato architektura eliminuje jednotlivá místa selhání spojená s centralizovanými databázemi: neexistují žádné servery, které by mohly být ohroženy, ani infrastruktura třetích stran, která by měla přístup k vašim pověřením. Komunikace mezi vašimi zařízeními je šifrována end-to-end, což zajišťuje, že přístup k datům umožňují pouze klíče, které máte v držení.



![Image](assets/fr/02.webp)



Aby to bylo možné, spoléhá se PearPass, jak napovídá jeho název, na **Pears**, ekosystém technologie peer-to-peer určený k vytváření a spouštění aplikací bez serveru. Pears poskytuje exekuční prostředí, distribuční mechanismy a síťové vrstvy potřebné k provozování plně decentralizovaných aplikací, které jsou schopny synchronizace přímo mezi peery, bez jakékoli centrální infrastruktury. V případě PearPass poskytuje Pears zjišťování zařízení, navazování šifrovaných spojení a synchronizaci trezoru hesel mezi počítači. Tento přístup zajišťuje, že PearPass zůstává funkční, odolný a nezávislý na jakékoli externí autoritě.



https://planb.academy/tutorials/computer-security/communication/pears-6d42b312-c69f-4504-8f71-b03b56c42fdd

Kromě této inovativní architektury je PearPass zcela open-source a všechny jeho funkce jsou zdarma. Software byl také nezávisle auditován společností Secfault Security. Kromě své specifické architektury nabízí PearPass samozřejmě všechny klasické funkce, které se od dobrého správce hesel očekávají a které objevíme v průběhu tohoto tutoriálu.



Stručně řečeno, zatímco tradiční správci hesel vás žádají, abyste důvěřovali společnosti a jejím serverům, PearPass používá logiku suverenity: žádný cloud, žádné centralizované účty, žádní prostředníci. Nad svými přihlašovacími údaji si ponecháváte výhradní kontrolu a zároveň využíváte výhod synchronizace mezi svými zařízeními.



## Jak nainstaluji PearPass?



PearPass je k dispozici na všech platformách: PearPass je dostupný pro Windows, Linux, macOS, Android, iOS a rozšíření prohlížeče. Není třeba instalovat Pears do počítače: PearPass funguje sám o sobě.



### Instalace v systému Windows



V systému Windows je aplikace PearPass dodávána jako klasický instalační program. Přejděte na [oficiální stránku ke stažení](https://pass.pears.com/download) a klikněte na tlačítko `Stáhnout instalační program pro Windows`.



Po stažení souboru otevřete instalační program a postupujte podle pokynů průvodce. Aplikaci lze poté spustit z nabídky `Start` nebo pomocí zástupce na ploše.



![Image](assets/fr/03.webp)



### Instalace v systému macOS



V systému macOS je PearPass distribuován jako obraz disku (`.dmg`). Přejděte na [oficiální stránku ke stažení](https://pass.pears.com/download) a vyberte verzi odpovídající architektuře vašeho počítače Mac (Intel nebo Apple Silicon). Po stažení otevřete soubor `.dmg` a spusťte aplikaci ze složky `Aplikace`.



Při prvním spuštění systému macOS se zobrazí bezpečnostní hlášení, že aplikace pochází z Internetu: pro pokračování stačí potvrdit.



### Instalace v systému Linux



V Linuxu je PearPass k dispozici ve formátu `.AppImage`, který zaručuje širokou kompatibilitu s většinou distribucí bez specifických závislostí. Stáhněte si soubor `.AppImage` z [oficiální stránky pro stahování](https://pass.pears.com/download) a poté jej spusťte přímo dvojitým kliknutím.



V závislosti na vašem prostředí může být nutné spustit soubor pomocí vlastností souboru (kliknutím pravým tlačítkem myši) nebo příkazem `chmod +x`. Po autorizaci se PearPass spustí jako samostatná aplikace.



### Instalace rozšíření prohlížeče



PearPass nabízí rozšíření prohlížeče pro automatické přihlášení a rychlý přístup k vašemu sejfu při procházení webu. Rozšíření je v současné době k dispozici pro prohlížeč Google Chrome a kompatibilní prohlížeče. Chcete-li jej nainstalovat, přejděte na [oficiální stránku ke stažení](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/04.webp)



Po přidání ji můžete připnout na panel nástrojů pro rychlý přístup. Aktivace rozšíření pak vyžaduje propojení s aplikací PearPass nainstalovanou lokálně v počítači (k tomu se vrátíme později v tomto návodu).



### Instalace v systémech iOS a Android



V zařízeních iPhone a Android stačí stáhnout aplikaci z obchodu s aplikacemi:




- [Obchod Google Play](https://play.google.com/store/apps/details?id=com.pears.pass);
- [App Store](https://apps.apple.com/us/app/pearpass/id6752954830).



![Image](assets/fr/05.webp)



Kromě těchto klasických způsobů instalace je také možné stáhnout software přímo z repozitářů GitHub, pro každý :




- [Desktop](https://github.com/tetherto/pearpass-app-desktop);
- [Mobilní](https://github.com/tetherto/pearpass-app-mobile);
- [Rozšíření prohlížeče](https://github.com/tetherto/pearpass-app-browser-extension).



Po instalaci aplikace PearPass na jednu nebo více platforem můžete přejít k počáteční konfiguraci. V tomto návodu začneme konfigurací softwaru na stolním počítači, poté jej synchronizujeme s rozšířením prohlížeče a mobilní aplikací.



## Jak vytvořím trezor PearPass?



Po prvním spuštění aplikace PearPass v počítači vás aplikace provede dvěma kroky: nastavením hlavního hesla a vytvořením prvního trezoru.



### Nastavení hlavního hesla



Při prvním spuštění aplikace na ploše klikněte na tlačítko `Přeskočit` a poté na `Pokračovat`, abyste prošli úvodní obrazovkou a dostali se do fáze konfigurace hlavního hesla.



![Image](assets/fr/06.webp)



Dalším důležitým krokem je výběr hlavního hesla. Jak jsme viděli v úvodu, toto heslo je velmi důležité, protože vám umožňuje přístup ke všem ostatním heslům uloženým ve správci. Z technického hlediska slouží k odvození kryptografických klíčů používaných k šifrování vašich dat.



Hlavní heslo s sebou nese dvě hlavní rizika: ztrátu a kompromitaci. Pokud ztratíte přístup k tomuto heslu, nebudete již mít přístup ke svým přihlašovacím údajům. PearPass nikdy neuchovává vaše hlavní heslo: **Pokud ho ztratíte, vaše přihlašovací údaje budou trvale ztraceny**. Neexistuje žádný mechanismus obnovy. Naopak, pokud je toto heslo prozrazeno a útočník získá přístup k jednomu z vašich zařízení, bude mít přístup ke všem vašim účtům.



Chcete-li omezit riziko ztráty, můžete si vytvořit fyzickou zálohu hlavního hesla, například na papíře, a uchovávat ji na bezpečném místě. V ideálním případě tuto zálohu zapečetěte v obálce, abyste mohli pravidelně kontrolovat, zda k ní nikdo neměl přístup. Na druhou stranu si nikdy nevytvářejte digitální zálohu tohoto hesla.



Abyste snížili riziko kompromitace, musí být hlavní heslo silné. Mělo by být co nejdelší, obsahovat širokou škálu znaků a být zvoleno skutečně náhodně. V roce 2025 minimální doporučení požadují alespoň 13 znaků zahrnujících velká a malá písmena, číslice a symboly, pokud je heslo náhodné. Pro zajištění trvalejší úrovně zabezpečení bych však doporučoval heslo o délce alespoň 20 znaků, ne-li více, se všemi typy znaků.



Zadejte hlavní heslo do příslušného pole, podruhé jej potvrďte a klikněte na tlačítko `Pokračovat`.



![Image](assets/fr/07.webp)



Poté budete přesměrováni na přihlašovací obrazovku: zadejte hlavní heslo a zkontrolujte, zda vše funguje správně.



![Image](assets/fr/08.webp)



### Vytvoření prvního trezoru



Po přihlášení vás PearPass vyzve k vytvoření prvního trezoru. Trezor je šifrovaná schránka, ve které jsou uložena vaše hesla, ID, bezpečné poznámky a další informace. Každý trezor je izolovaný a lze jej identifikovat odlišným názvem, což vám umožní uspořádat data podle způsobu použití (osobní, pracovní, konkrétní projekty...).



Klikněte na tlačítko `Vytvořit nový trezor`.



![Image](assets/fr/09.webp)



Zvolte název tohoto trezoru a znovu klikněte na tlačítko `Vytvořit nový trezor` pro dokončení vytvoření.



![Image](assets/fr/10.webp)



Váš trezor je okamžitě připraven k použití. Hned můžete začít přidávat hesla, přihlašovací údaje nebo bezpečné poznámky.



![Image](assets/fr/11.webp)



## Jak přidám přihlášení do PearPass?



Po vytvoření trezoru do něj můžete začít ukládat své položky. PearPass podporuje registraci mnoha typů položek:




- přihlášení k webu nebo službě ;
- identita: vaše osobní údaje pro rychlé vyplňování formulářů, ale také pro ukládání dokladů totožnosti přímo v PearPass ;
- kreditní karta: čísla vašich kreditních karet pro rychlejší platby při nakupování online;
- Wi-Fi: hesla pro sítě Wi-Fi ;
- PassPhrase: tajná fráze složená z několika slov (varování: důrazně nedoporučuji používat pro mnemotechnické fráze wallet Bitcoin);
- poznámka: vytváření zabezpečených poznámek ;
- vlastní: tato funkce umožňuje vytvořit vlastní typ prvku přizpůsobený vašim specifickým potřebám.



Začněte tím, že otevřete aplikaci PearPass a přihlásíte se pomocí hlavního hesla.



![Image](assets/fr/12.webp)



Vyberte trezor, do kterého chcete tento identifikátor uložit.



![Image](assets/fr/13.webp)



Na domovské stránce klikněte na tlačítko pro přidání nové položky v závislosti na typu informací, které chcete zaznamenat. V mém případě chci přidat přihlašovací údaje pro svůj účet na webové stránce Plan ₿ Academy: kliknu tedy na tlačítko `Vytvořit přihlašovací údaje`.



![Image](assets/fr/14.webp)



Po výběru typu položky, kterou chcete přidat, se zobrazí formulář, do kterého můžete zadat informace spojené s danou službou. V závislosti na svých potřebách můžete zadat název služby, přihlašovací jméno, heslo a v případě potřeby i adresu webové stránky a další poznámky.



PearPass také nabízí generátor hesel, který umožňuje vytvořit silné heslo přímo z formuláře. Chcete-li jej použít, klikněte na ikonu představující tři malé tečky v poli `Heslo`, zvolte požadovanou délku a poté klikněte na `Vložit heslo`.



Po vyplnění všech polí klikněte na tlačítko `Uložit` a uložte identifikátor do trezoru.



![Image](assets/fr/15.webp)



Identifikátor je nyní uložen. Zobrazí se v seznamu položek ve vybraném trezoru a lze jej zobrazit kliknutím na něj.



![Image](assets/fr/16.webp)



Prvek můžete snadno upravit kliknutím na něj a poté na tlačítko `Upravit`. Můžete jej také odstranit kliknutím na tři malé tečky v pravém horním rohu rozhraní a poté na `Odstranit prvek`.



![Image](assets/fr/22.webp)



V mobilním telefonu zůstává logika stejná, i když rozhraní bylo upraveno. Po přihlášení vyberte požadovaný trezor, klepněte na tlačítko `+`, vyberte typ položky, kterou chcete vytvořit, a poté vyplňte potřebné informace.



![Image](assets/fr/17.webp)



## Jak uspořádat PearPass?



Jak jsme viděli v předchozích částech, PearPass umožňuje vytvořit několik různých trezorů. To umožňuje oddělit různá použití a představuje první úroveň organizace správce hesel. Na domovské stránce můžete snadno přepínat z jednoho trezoru do druhého kliknutím na šipku v levém horním rohu rozhraní.



![Image](assets/fr/18.webp)



Dalším způsobem organizace hesel, a to i v rámci trezoru, je vytvoření složek. Za tímto účelem klikněte v levém sloupci rozhraní na symbol `+` vedle položky `Všechny složky` a poté zadejte název složky, kterou chcete vytvořit.



![Image](assets/fr/19.webp)



Vybrané identifikátory pak můžete uložit buď přímo při vytváření položky, nebo později kliknutím na tlačítko `Upravit`. Stačí pouze vybrat požadovanou složku v levém horním rohu formuláře.



![Image](assets/fr/20.webp)



Po otevření položky, například přihlášení, ji můžete kliknutím na ikonu hvězdičky v pravém horním rohu rozhraní přidat do oblíbených položek. Oblíbené položky lze kromě základní složky rychle najít ve vyhrazené složce.



![Image](assets/fr/21.webp)



V horní části rozhraní se nachází vyhledávací panel, takže můžete rychle najít hledanou položku, i když váš trezor obsahuje mnoho identifikátorů.



## Jak synchronizuji PearPass v mobilním telefonu?



Nyní, když máte funkční trezor s položkami uloženými v počítači, budete pravděpodobně chtít přistupovat ke svým heslům ze smartphonu nebo jiného zařízení. Aplikace PearPass umožňuje bezpečně synchronizovat správce na více počítačích pomocí Pears. Pojďme zjistit, jak na to.



Nejprve se ve zdrojovém počítači (například ve vašem počítači) přihlaste do trezoru pomocí hlavního hesla. Na domovské stránce klikněte na tlačítko `Přidat zařízení`, které se nachází v pravé dolní části rozhraní.



![Image](assets/fr/23.webp)



PearPass poté vygeneruje odkaz s pozvánkou, který je k dispozici také jako QR kód, a synchronizuje vybraný trezor na vámi zvoleném zařízení.



![Image](assets/fr/24.webp)



Pokud chcete synchronizovat v mobilním zařízení, nejprve nainstalujte aplikaci a poté ji spusťte. Budete vyzváni k vytvoření hlavního hesla pro mobilního správce. Můžete si vybrat, zda chcete použít stejné heslo jako v počítači, nebo jiné. Ve všech případech se řiďte stejným doporučením: silné, náhodné heslo uložené na fyzickém médiu.



![Image](assets/fr/25.webp)



Pokud chcete, můžete aktivovat biometrické ověřování, abyste nemuseli při každém odemykání mobilu ručně zadávat hlavní heslo.



![Image](assets/fr/26.webp)



Znovu zadejte hlavní heslo a klikněte na tlačítko `Pokračovat`.



![Image](assets/fr/27.webp)



Vyberte možnost `Načíst trezor`, klikněte na `Skenovat QR kód` a naskenujte QR kód pozvánky zobrazený programem PearPass na zdrojovém počítači.



![Image](assets/fr/28.webp)



Vaše trezory v počítači a mobilu jsou nyní synchronizovány. Každé ID přidané na jednom zařízení bude bezpečně uloženo a replikováno na druhém.



![Image](assets/fr/29.webp)



V mobilních telefonech můžete také aktivovat automatické vyplňování polí. To provedete tak, že přejdete do `Nastavení > Rozšířené` a v části `Automatické vyplňování` kliknete na tlačítko `Nastavit jako výchozí`.



![Image](assets/fr/30.webp)



## Jak synchronizuji PearPass s rozšířením prohlížeče?



Správce hesel synchronizovaný mezi počítačem a chytrým telefonem je již velmi praktický, ale jeho integrace přímo do prohlížeče je ještě praktičtější. Začněte tím, že si do prohlížeče [přidáte oficiální rozšíření PearPass](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/31.webp)



V softwaru PearPass nainstalovaném v místním počítači přejděte na `Nastavení > Rozšířené` a aktivujte možnost `Aktivovat rozšíření prohlížeče`.



![Image](assets/fr/32.webp)



PearPass generuje párovací soubor token. Zkopírujte jej.



![Image](assets/fr/33.webp)



Poté v prohlížeči otevřete rozšíření PearPass, vložte párování token a klikněte na tlačítko `Ověřit` a poté na `Dokončit`.



![Image](assets/fr/34.webp)



Správce hesel je nyní synchronizován s rozšířením prohlížeče.



![Image](assets/fr/35.webp)



Nyní se pomocí něj můžete snadno připojit k různým webovým účtům.



![Image](assets/fr/36.webp)



Nyní víte, jak používat správce hesel PearPass. Kromě tohoto nástroje závisí každodenní digitální bezpečnost na správném používání vhodných řešení. Pokud se chcete naučit, jak nastavit bezpečné, stabilní a efektivní osobní digitální prostředí, zvu vás k objevení našeho školení věnovaného tomuto tématu:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1