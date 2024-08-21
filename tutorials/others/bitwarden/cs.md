---
name: BITWARDEN
description: Jak nastavit správce hesel?
---
![cover](assets/cover.webp)

Ve digitálním věku potřebujeme spravovat množství online účtů, které pokrývají různé aspekty našeho každodenního života, včetně bankovnictví, finančních platforem, emailů, úložiště souborů, zdraví, administrativy, sociálních sítí, videoher atd.

Pro autentizaci na každém z těchto účtů používáme identifikátor, často emailovou adresu, doprovázenou heslem. Vzhledem k nemožnosti zapamatovat si velké množství unikátních hesel by se člověk mohl být lákán k opětovnému použití stejného hesla nebo k mírné modifikaci společného základu pro snadnější zapamatování. Tyto praktiky však vážně ohrožují bezpečnost vašich účtů.

Prvním principem, kterého bychom se měli držet u hesel, je jejich neopakování. Každý online účet by měl být chráněn unikátním a zcela odlišným heslem. To je důležité, protože pokud by útočník dokázal kompromitovat jedno z vašich hesel, nechcete, aby měl přístup ke všem vašim účtům. Mít unikátní heslo pro každý účet izoluje potenciální útoky a omezuje jejich rozsah. Například, pokud používáte stejné heslo pro platformu videoher a pro váš email, a toto heslo je kompromitováno prostřednictvím phishingové stránky spojené s herní platformou, útočník by pak mohl snadno získat přístup k vašemu emailu a ovládnout všechny vaše další online účty.

Druhým zásadním principem je síla hesla. Heslo je považováno za silné, pokud je obtížné ho uhodnout metodou hrubé síly, tj. pokusem a omylem. To znamená, že vaše hesla musí být co nejvíce náhodná, dlouhá a obsahovat různorodé znaky (malá písmena, velká písmena, čísla a symboly).

Aplikace těchto dvou principů zabezpečení hesel (unikátnost a robustnost) může být v každodenním životě obtížná, protože si zapamatovat unikátní, náhodné a silné heslo pro všechny naše účty je téměř nemožné. Zde přichází na řadu správce hesel.

Správce hesel generuje a bezpečně ukládá silná hesla, což vám umožňuje přistupovat ke všem vašim online účtům bez nutnosti je individuálně pamatovat. Potřebujete si zapamatovat pouze jedno heslo, hlavní heslo, které vám dává přístup ke všem vašim uloženým heslům ve správci. Používání správce hesel zvyšuje vaši online bezpečnost, protože brání opětovnému použití hesel a systematicky generuje náhodná hesla. Ale také zjednodušuje vaše každodenní používání účtů centralizací přístupu k vašim citlivým informacím.
V tomto tutoriálu prozkoumáme, jak nastavit a používat správce hesel pro zvýšení vaší online bezpečnosti. Představím vám Bitwarden a v dalším tutoriálu se podíváme na další řešení nazvané KeePass.
https://planb.network/tutorials/others/keepass

Varování: Správce hesel je skvělý pro ukládání hesel, ale **nikdy v něm neukládejte mnemonickou frázi vaší Bitcoinové peněženky!** Pamětní fráze by měla být výhradně uložena ve fyzickém formátu, jako je kus papíru nebo kovu.

## Úvod do Bitwarden

Bitwarden je správce hesel vhodný jak pro začátečníky, tak pro pokročilé uživatele. Nabízí mnoho výhod. Především je Bitwarden multiplatformní řešení, což znamená, že jej můžete používat jako mobilní aplikaci, webovou aplikaci, rozšíření prohlížeče a desktopový software.
![BITWARDEN](assets/notext/01.webp)
Bitwarden vám umožňuje ukládat vaše hesla online a synchronizovat je napříč všemi vašimi zařízeními, přičemž zajišťuje end-to-end šifrování s vaším hlavním heslem. To vám například umožňuje přistupovat k vašim heslům jak na počítači, tak na smartphonu, se synchronizací mezi oběma. Jelikož jsou vaše hesla šifrována, zůstávají nedostupná pro kohokoli, včetně Bitwarden, bez dešifrovacího klíče, kterým je vaše hlavní heslo.
Navíc Bitwarden je open-source, což znamená, že software může být auditován nezávislými odborníky. Pokud jde o ceny, Bitwarden nabízí tři plány: - Bezplatnou verzi, kterou si probereme v tomto tutoriálu. I když je zdarma, poskytuje úroveň zabezpečení ekvivalentní placeným verzím. Můžete ukládat neomezené množství hesel a synchronizovat libovolný počet zařízení;
- Prémiovou verzi za 10 dolarů ročně, která zahrnuje další funkce, jako je úložiště souborů, záloha kreditních karet, možnost konfigurace 2FA s fyzickým bezpečnostním klíčem a přístup k autentizaci TOTP 2FA přímo s Bitwardenem;
- A rodinný plán za 40 dolarů ročně, který rozšiřuje výhody prémiové verze na šest různých uživatelů.
![BITWARDEN](assets/notext/02.webp)
Podle mého názoru jsou tyto ceny férové. Bezplatná verze je vynikající volbou pro začátečníky a prémiová verze nabízí velmi dobrý poměr cena/výkon ve srovnání s ostatními správci hesel na trhu, přičemž nabízí více funkcí. Navíc fakt, že Bitwarden je open-source, je velkou výhodou. Proto je to zajímavý kompromis, zejména pro začátečníky.
Další funkcí Bitwardenu je možnost vlastního hostování vašeho správce hesel, pokud například vlastníte NAS doma. Nastavením této konfigurace nejsou vaše hesla uložena na serverech Bitwardenu, ale na vašich vlastních serverech. To vám dává úplnou kontrolu nad dostupností vašich hesel. Tato možnost však vyžaduje pečlivé řízení záloh, aby se předešlo jakékoli ztrátě přístupu. Proto je vlastní hostování Bitwardenu vhodnější pro pokročilé uživatele a budeme o tom diskutovat v dalším tutoriálu.
## Jak vytvořit účet Bitwarden?

Navštivte [webové stránky Bitwarden](https://bitwarden.com/) a klikněte na "*Začít*".
![BITWARDEN](assets/notext/03.webp)
Začněte zadáním vaší e-mailové adresy a vašeho jména nebo přezdívky.
![BITWARDEN](assets/notext/04.webp)
Dále budete muset nastavit vaše hlavní heslo. Jak jsme viděli v úvodu, toto heslo je velmi důležité, protože vám dává přístup ke všem vašim ostatním uloženým heslům v manažeru. Představuje dva hlavní rizika: ztrátu a kompromitaci. Pokud ztratíte přístup k tomuto heslu, již nebudete moci přistupovat ke všem vašim pověřením. Pokud je vaše heslo ukradeno, útočník bude moci přistupovat ke všem vašim účtům.

Aby se minimalizovalo riziko ztráty, doporučuji udělat fyzickou zálohu vašeho hlavního hesla na papíře a uložit ji na bezpečném místě. Pokud je to možné, zapečetěte tuto zálohu do bezpečné obálky, abyste pravidelně zajišťovali, že k ní nikdo jiný neměl přístup.

Aby se předešlo kompromitaci vašeho hlavního hesla, musí být mimořádně robustní. Mělo by být co nejdelší, používat širokou škálu znaků a být vybráno náhodně. V roce 2024 jsou minimální doporučení pro bezpečné heslo 13 znaků včetně čísel, malých a velkých písmen, stejně jako symbolů, za předpokladu, že heslo je skutečně náhodné. Nicméně, doporučuji zvolit heslo o délce alespoň 20 znaků, včetně všech možných typů znaků, aby bylo zajištěno jeho zabezpečení na delší dobu.

Zadejte vaše hlavní heslo do příslušného pole a potvrďte ho v následujícím poli.
![BITWARDEN](assets/notext/05.webp)
Pokud chcete, můžete přidat nápovědu pro vaše hlavní heslo. Nicméně, radím to nedělat, protože nápověda neposkytuje spolehlivou metodu obnovy v případě, že ztratíte své heslo, a mohla by být dokonce užitečná útočníkům, kteří se pokoušejí uhodnout nebo prolomit vaše heslo brutální silou. Jako obecné pravidlo se vyhněte vytváření veřejných nápověd, které by mohly ohrozit zabezpečení vašeho hlavního hesla.
![BITWARDEN](assets/notext/06.webp)Poté klikněte na tlačítko "*Vytvořit účet*".
![BITWARDEN](assets/notext/07.webp)
Nyní se můžete přihlásit do svého nového účtu Bitwarden. Zadejte svou e-mailovou adresu.
![BITWARDEN](assets/notext/08.webp)
Poté zadejte své hlavní heslo.
![BITWARDEN](assets/notext/09.webp)
Nyní jste na webovém rozhraní vašeho správce hesel.
![BITWARDEN](assets/notext/10.webp)
## Jak nastavit Bitwarden?

Začneme potvrzením naší e-mailové adresy. Klikněte na "*Odeslat e-mail*".
![BITWARDEN](assets/notext/11.webp)
Poté klikněte na tlačítko, které obdržíte e-mailem.
![BITWARDEN](assets/notext/12.webp)
Nakonec se znovu přihlaste.
![BITWARDEN](assets/notext/13.webp)
Především vřele doporučuji nastavit dvoufaktorové ověření (2FA) pro zabezpečení vašeho správce hesel. Máte na výběr mezi použitím aplikace TOTP nebo fyzického bezpečnostního klíče. Aktivací 2FA budete při každém přihlášení do vašeho účtu Bitwarden požádáni nejen o vaše hlavní heslo, ale také o důkaz vašeho druhého faktoru ověření. Jedná se o další vrstvu zabezpečení, která je obzvláště užitečná v případě, že by byla ohrožena vaše papírová záloha hlavního hesla.

Pokud si nejste jisti, jak tyto zařízení 2FA nastavit a používat, doporučuji sledovat tyto 2 další tutoriály:

https://planb.network/tutorials/others/authy

https://planb.network/tutorials/others/security-key

Pro toto přejděte na záložku "*Bezpečnost*" v menu "*Nastavení*".
![BITWARDEN](assets/notext/14.webp)
Poté klikněte na záložku "*Dvoufázové přihlášení*".
![BITWARDEN](assets/notext/15.webp)
Zde si můžete vybrat preferovanou metodu 2FA. Například si vyberu 2FA s aplikací TOTP kliknutím na tlačítko "*Spravovat*".
![BITWARDEN](assets/notext/16.webp)
Potvrďte své hlavní heslo.
![BITWARDEN](assets/notext/17.webp)
Poté naskenujte QR kód pomocí vaší aplikace pro 2FA.
![BITWARDEN](assets/notext/18.webp)
Zadejte 6místný kód zaznamenaný ve vaší aplikaci pro 2FA, poté klikněte na tlačítko "*Zapnout*". ![BITWARDEN](assets/notext/19.webp)
Dvoufaktorové ověření bylo úspěšně nastaveno na vašem účtu.
![BITWARDEN](assets/notext/20.webp)
Nyní, pokud se pokusíte znovu přihlásit do vašeho správce, budete nejprve muset zadat své hlavní heslo, poté 6místný dynamický kód generovaný vaší aplikací pro 2FA. Ujistěte se, že máte vždy přístup k tomuto dynamickému kódu; bez něj nebudete moci obnovit svá hesla.
![BITWARDEN](assets/notext/21.webp)
V nastavení máte také možnost přizpůsobit svého správce v záložce "*Předvolby*". Zde můžete změnit dobu, než se váš správce automaticky zamkne, stejně jako jazyk a téma rozhraní.
![BITWARDEN](assets/notext/22.webp)
Vřele doporučuji upravit délku hesel generovaných Bitwardenem. Ve výchozím nastavení je délka nastavena na 14 znaků, což pro optimální zabezpečení může být nedostatečné. Nyní, když máte správce pro zapamatování všech vašich hesel, měli byste toho využít a používat velmi silná hesla.
Pro provedení této akce přejděte do menu "*Generator*". ![BITWARDEN](assets/notext/23.webp)
Zde můžete zvýšit hodnotu délky vašich hesel na 40 a zaškrtnout políčko pro zahrnutí symbolů.
![BITWARDEN](assets/notext/24.webp)
## Jak zabezpečit vaše účty s Bitwarden?

Nyní, když máte nastavený správce hesel, můžete začít ukládat přihlašovací údaje pro vaše online účty. Pro přidání nové položky klikněte přímo na tlačítko "*Nová položka*" nebo na tlačítko "*Nový*" umístěné v pravém horním rohu obrazovky, poté na "*položku*".
![BITWARDEN](assets/notext/25.webp)
Ve formuláři, který se otevře, začněte určením povahy položky, kterou chcete uložit. Pro uložení přihlašovacích údajů vyberte z rozevíracího menu možnost "*Přihlášení*".
![BITWARDEN](assets/notext/26.webp)
Do pole "*Název*" zadejte popisný název pro vaše přihlašovací údaje. To usnadní vyhledávání a organizaci vašich hesel, zejména pokud jich máte velké množství. Například, pokud chcete uložit vaše přihlašovací údaje pro web PlanB Network, můžete tuto položku pojmenovat způsobem, který ji během vašich budoucích vyhledávání okamžitě identifikuje.
![BITWARDEN](assets/notext/27.webp)
Pole "*Složka*" vám umožňuje klasifikovat vaše přihlašovací údaje do složek. V tuto chvíli jsme ještě žádné nevytvořili, ale později vám ukážu, jak na to.
![BITWARDEN](assets/notext/28.webp)
Do pole "*Uživatelské jméno*" zadejte své uživatelské jméno, které je obvykle vaše e-mailová adresa. ![BITWARDEN](assets/notext/29.webp)
Dále, v poli "*Heslo*", můžete zadat své heslo. Nicméně, silně doporučuji nechat Bitwarden vygenerovat pro vás dlouhé, náhodné a unikátní heslo. To zajistí, že budete mít silné heslo. Pro použití této funkce klikněte na ikonu se dvojitou šipkou nad polem, které má být vyplněno.
![BITWARDEN](assets/notext/30.webp)
Můžete vidět, že vaše heslo bylo vygenerováno.
![BITWARDEN](assets/notext/31.webp)
V poli "*URI 1*" můžete zadat název domény webové stránky.
![BITWARDEN](assets/notext/32.webp)
A nakonec, v poli "*Poznámky*", můžete přidat další podrobnosti, pokud je to nutné.
![BITWARDEN](assets/notext/33.webp)
Když jste dokončili vyplňování všech těchto polí, klikněte na tlačítko "*Uložit*".
![BITWARDEN](assets/notext/34.webp)
Vaše přihlašovací údaje se nyní objevují ve vašem správci Bitwarden.
![BITWARDEN](assets/notext/35.webp)
Kliknutím na ně můžete přistupovat k jejich detailům a upravovat je.
![BITWARDEN](assets/notext/36.webp)
Kliknutím na tři malé tečky vpravo máte rychlý přístup ke kopírování hesla nebo uživatelského jména.
![BITWARDEN](assets/notext/37.webp)
Gratulujeme, úspěšně jste uložili své první heslo do vašeho správce! Pokud chcete lépe organizovat vaše přihlašovací údaje, můžete vytvořit specifické složky. Pro to klikněte na tlačítko "*Nový*" umístěné v pravém horním rohu obrazovky, poté vyberte "*Složka*".
![BITWARDEN](assets/notext/38.webp)
Zadejte název pro vaši složku.
![BITWARDEN](assets/notext/39.webp)
Poté klikněte na "*Uložit*".
![BITWARDEN](assets/notext/40.webp)
Vaše složka se nyní objevuje ve vašem správci.
![BITWARDEN](assets/notext/41.webp)Při vytváření nového přístupového údaje mu můžete přiřadit složku, jak jsme to udělali dříve, nebo můžete upravit existující přístupový údaj. Například kliknutím na můj přístupový údaj pro PlanB Network, mohu poté zvolit jeho zařazení do složky "*Bitcoin*".
![BITWARDEN](assets/notext/42.webp)
Tímto způsobem můžete strukturovat váš správce hesel, aby bylo snazší nalézt vaše přístupové údaje. Můžete je organizovat do složek jako osobní, profesionální, banky, emaily, sociální sítě, předplatné, nákupy, administrativa, streaming, úložiště, cestování, zdraví atd.
Pokud dáváte přednost používání pouze webové verze Bitwarden, je to zcela možné. Doporučuji poté přidat váš správce hesel do oblíbených ve vašem prohlížeči pro snadný přístup a aby se zabránilo rizikům phishingu. Bitwarden však také nabízí celou řadu klientů, které vám umožní používat váš správce na různých zařízeních a zjednodušit jeho každodenní používání. Nabízejí zejména mobilní aplikaci, rozšíření prohlížeče a desktopový software. Podívejme se, jak je nastavit.

![BITWARDEN](assets/notext/43.webp)
## Jak používat rozšíření Bitwarden pro prohlížeč?

Nejprve si můžete nastavit rozšíření prohlížeče, pokud chcete. Toto rozšíření funguje jako zjednodušená verze vašeho správce a nabízí vám možnost automaticky ukládat nová hesla, generovat bezpečné návrhy hesel a automaticky vyplňovat vaše přístupové údaje ve formulářích pro přihlášení na webových stránkách.

Používání tohoto rozšíření na denní bázi je velmi pohodlné, ale může také otevřít nové vektory pro útok. Proto někteří odborníci na kybernetickou bezpečnost nedoporučují používat rozšíření prohlížeče pro správce hesel. Pokud se však rozhodnete použít rozšíření Bitwarden, postupujte takto:

Začněte tím, že navštívíte [oficiální stránku pro stažení Bitwarden](https://bitwarden.com/download/#downloads-web-browser).
![BITWARDEN](assets/notext/44.webp)
Vyberte svůj prohlížeč ze seznamu. Pro tento příklad používám Firefox, takže jsem přesměrován na oficiální rozšíření Bitwarden v obchodě Firefox Add-ons. Postup je velmi podobný pro ostatní prohlížeče.
![BITWARDEN](assets/notext/45.webp)
Klikněte na tlačítko "*Přidat do Firefoxu*".
![BITWARDEN](assets/notext/46.webp)
Poté můžete Bitwarden připojit k vaší liště rozšíření pro snadný přístup. Klikněte na rozšíření pro přihlášení.
![BITWARDEN](assets/notext/47.webp)
Zadejte svou emailovou adresu.
![BITWARDEN](assets/notext/48.webp)
Poté své hlavní heslo.
![BITWARDEN](assets/notext/49.webp)
A nakonec zadejte 6místný kód z vaší autentizační aplikace.
![BITWARDEN](assets/notext/50.webp)
Nyní jste připojeni k vašemu správci Bitwarden prostřednictvím rozšíření prohlížeče.
![BITWARDEN](assets/notext/51.webp)
Například, pokud se vrátím na stránku PlanB Network a pokusím se přihlásit k mému účtu, můžete vidět, že rozšíření Bitwarden integrované do prohlížeče rozpozná pole pro přihlášení a automaticky mi nabídne vybrat identifikátor, který jsem dříve uložil.
![BITWARDEN](assets/notext/52.webp)
Pokud vyberu tento identifikátor, Bitwarden za mě vyplní přihlašovací pole. Tato funkce rozšíření umožňuje rychlé připojení k webovým stránkám, bez nutnosti kopírovat přihlašovací údaje z webové aplikace nebo softwaru Bitwarden. ![BITWARDEN](assets/notext/53.webp) Rozšíření je také navrženo tak, aby detekovalo vytváření nových účtů. Například při vytváření nového účtu na PlanB Network, Bitwarden automaticky navrhuje uložení nového identifikátoru. ![BITWARDEN](assets/notext/54.webp) Kliknutím na tento návrh, který se objeví, se otevře rozšíření. Umožňuje mi zadat podrobnosti nového identifikátoru a vygenerovat silné, unikátní heslo. ![BITWARDEN](assets/notext/55.webp) Po dokončení informací a kliknutí na "*Uložit*", rozšíření uloží přihlašovací údaje. ![BITWARDEN](assets/notext/56.webp) Poté rozšíření automaticky přidá naše přihlašovací údaje do příslušných polí na webové stránce. ![BITWARDEN](assets/notext/57.webp) ## Jak používat software Bitwarden?
Pro instalaci desktopového softwaru Bitwarden začněte tím, že přejdete na [stránku ke stažení](https://bitwarden.com/download/#downloads-desktop). Vyberte a stáhněte verzi odpovídající vašemu operačnímu systému. ![BITWARDEN](assets/notext/58.webp) Jakmile je stažení dokončeno, pokračujte instalací softwaru na vašem počítači. Při prvním spuštění softwaru Bitwarden budete muset zadat své přihlašovací údaje, abyste odemkli správce hesel. ![BITWARDEN](assets/notext/59.webp) Poté se dostanete na domovskou stránku vašeho správce. Rozhraní je téměř stejné jako ve webové aplikaci. ![BITWARDEN](assets/notext/60.webp) ## Jak používat aplikaci Bitwarden?

Pro přístup k vašim heslům z telefonu můžete nainstalovat mobilní aplikaci Bitwarden. Začněte tím, že přejdete na [stránku ke stažení](https://bitwarden.com/download/#downloads-mobile) a použijte svůj smartphone k naskenování QR kódu odpovídajícího vašemu operačnímu systému. ![BITWARDEN](assets/notext/61.webp) Stáhněte a nainstalujte oficiální mobilní aplikaci Bitwarden. Při prvním otevření aplikace zadejte své přihlašovací údaje, abyste odemkli přístup k vašemu správci hesel. ![BITWARDEN](assets/notext/62.webp) Jakmile se připojíte, budete moci přímo z aplikace konzultovat a spravovat všechna vaše hesla. ![BITWARDEN](assets/notext/63.webp) Pro zvýšení bezpečnosti vaší aplikace doporučuji jít do nastavení a aktivovat ochranu PINem. Tím přidáte další vrstvu zabezpečení v případě ztráty nebo krádeže vašeho telefonu. ![BITWARDEN](assets/notext/64.webp) ## Jak zálohovat Bitwarden?
Abyste nikdy nepřišli o přístup k vašim heslům, i v případě ztráty hlavního hesla nebo katastrofy ovlivňující servery Bitwarden, doporučuji pravidelně provádět šifrovanou zálohu vašeho správce na externím médiu.

Myšlenka je zašifrovat všechna vaše přihlašovací údaje Bitwarden heslem odlišným od vašeho hlavního hesla a uložit tuto zašifrovanou zálohu na USB klíč nebo pevný disk, který si necháte doma, například. Pak můžete uchovat fyzickou kopii dešifrovacího hesla na odděleném místě, kde je uloženo zálohovací médium. Například byste mohli USB klíč nechat doma a fyzickou kopii šifrovacího hesla svěřit důvěryhodnému příteli.

Tato metoda zajišťuje, že i když je vaše zálohovací médium ukradeno, vaše data zůstanou nedostupná bez dešifrovacího hesla. Podobně, váš přítel nebude moci přistupovat k vašim datům bez fyzického média.
Pokud by však nastal problém, můžete použít heslo a externí médium k opětovnému získání přístupu k vašim přihlašovacím údajům nezávisle na Bitwardenu. Takže i v případě, že by servery Bitwardenu byly zničeny, stále byste měli možnost získat zpět svá hesla.
Proto vám radím, abyste tyto zálohy prováděli pravidelně, aby vždy obsahovaly vaše nejnovější přihlašovací údaje. Aby vás neobtěžovalo neustálé kontaktování vašeho přítele, který má kopii šifrovacího hesla, při každé nové záloze, můžete toto heslo uložit ve vašem správci hesel. To není zamýšleno jako záloha, protože váš přítel už má fyzickou kopii, ale spíše k zjednodušení vašich budoucích exportních procedur.

Pro provedení exportu je to velmi jednoduché: přejděte do sekce "*Nástroje*" vašeho správce Bitwarden, poté vyberte "*Exportovat trezor*".
![BITWARDEN](assets/notext/65.webp)
Pro formát vyberte "*.json (Zašifrovaný)*".
![BITWARDEN](assets/notext/66.webp)
Poté vyberte možnost "*Chráněno heslem*".
![BITWARDEN](assets/notext/67.webp)
Zde je důležité zvolit silné, unikátní a náhodně generované heslo pro zašifrování zálohy. To zajistí, že i v případě krádeže vaší zašifrované zálohy bude pro útočníka nemožné ji dešifrovat hrubou silou.
![BITWARDEN](assets/notext/68.webp)
Klikněte na "*Potvrdit formát*" a zadejte své hlavní heslo pro pokračování v exportu.
![BITWARDEN](assets/notext/69.webp)
Po dokončení exportu najdete svůj zašifrovaný záložní soubor ve vašich stažených souborech. Přeneste jej na bezpečné externí úložiště, jako je USB klíč nebo pevný disk. Tuto operaci opakujte pravidelně v závislosti na vašem používání. Například můžete obnovit zálohu každý týden nebo každý měsíc, podle vašich potřeb.