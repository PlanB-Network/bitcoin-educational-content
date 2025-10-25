---
name: Nunchuk
description: Wallet mobile vhodný pro všechny
---
![cover](assets/cover.webp)



## Výkonný Wallet


Nunchuk přišel na konci roku 2020 s jasnou filozofií: udělat z více podpisů standard. Byl proto navržen tak, aby plnil velmi pokročilé funkce, přičemž cennou volbou bylo postavit design přímo na Bitcoin Core, referenčním softwaru pro ekosystém Bitcoin.



Po více než čtyřech letech vývoje a používání je připraven k vyzkoušení ve velkém měřítku. Pokud jste začátečníci a Nunchuk neznáte, pomůže vám tento průvodce udělat první kroky a objevit tento software, jehož pokročilé funkce budete moci poznat, až překonáte první náraz. Samotný návod je věnován středně pokročilým uživatelům, kteří mají potřebné dovednosti k provedení všech kroků, ale může být inspirací pro všechny, kteří chtějí zjistit, jak zvýšit své dovednosti. Začneme mobilní verzí, a toto upozornění je nutné, protože Nunchuk má software, který lze spustit i na počítačích.



## Stáhnout


Prvním krokem je určitě rozhodnutí, kde aplikaci stáhnout. Přejděte na [oficiální stránky](https://nunchuk.io/), kde najdete dokumentaci (není toho mnoho, ale je to začátek), prezentaci funkcí a také ke konci stránky všechny odkazy ke stažení.



📌 V tomto návodu jsem se rozhodl ukázat vám, jak stáhnout Software Wallet z úložiště Github a jak ověřit vydání před instalací do mobilního telefonu. **Následující postup lze provést pouze z počítače**, proto doporučuji provést všechny tyto kroky ze stolního počítače nebo notebooku a - po všech ověřeních - přenést soubor `.apk` do mobilního telefonu.



![image](assets/en/01.webp)



Pokud vaše znalosti nejsou příliš pokročilé, můžete si stáhnout soubor `.apk` z oficiálních obchodů a přejít přímo ke konfigurační části tohoto návodu. Pokud se naopak chcete pustit do skoku, pokračujte krok za krokem.



Na stolním počítači tedy klikněte na _Navštivte náš repozitář s otevřeným zdrojovým kódem_



Odkaz vás zavede na stránku Nunchuk na Githubu, kde najdete řadu repozitářů. My se zaměříme na _nunchuk-android_



![image](assets/en/02.webp)



Na další obrazovce vyhledejte vpravo část _Vydání_ a vyberte možnost _Nejnovější_



![image](assets/en/03.webp)



V části _Assets_ stáhněte verzi (v tomto případě 1.67.apk) spolu se souborem SHA256SUMS a SHA256SUMS.asc.



![image](assets/en/04.webp)



Chcete-li najít vývojářský klíč GPG, vraťte se do sekce _Vydání_ úložiště a vyhledejte verzi 1.9.53 (nebo starší), která obsahuje odkaz pro získání a stažení klíče _GPG_



![image](assets/en/05.webp)



Ověření provedeme pomocí praktického nástroje, který nabízí společnost Sparrow wallet. Ten má pro tento účel vyhrazené okno a podporuje podpisy PGP a manifesty SHA256.



Poté spusťte program Sparrow a v nabídce _Tools_ vyberte možnost _Verify Download_.



![image](assets/en/06.webp)



V okně, které se zobrazí, najdete pole, která je třeba "vyplnit": zvolte tlačítko _Browse_ vpravo a pro každé pole vyberte odpovídající soubory, které jste právě stáhli z Githubu. Po dokončení všech kroků bude okno vypadat následovně, se zaškrtávátky Green a potvrzením manifestu Hash.



![image](assets/en/07.webp)


**N.B. snímek obrazovky je z počítače s Windows, stejný postup lze použít pro jakýkoli operační systém v počítači, stačí mít nainstalovaný Sparrow wallet. A ověřeno!**



Ke stažení tohoto Software Wallet najdete průvodce Sparrow wallet


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Poté můžete soubor `.apk` přenést z počítače do telefonu



![image](assets/en/08.webp)



a nainstalujte Nunchuk



![image](assets/en/09.webp)



Před spuštěním aplikace Nunchuk v telefonu otevřete Orbot a zařaďte novinku do seznamu aplikací, které mají být směrovány pod Tor.



![image](assets/en/11.webp)



Nyní spusťte Nunchuk. Pokud jde o funkce projektu - které nejsou předmětem tohoto návodu -, Nunchuk vás po otevření vyzve k přihlášení prostřednictvím e-mailu nebo profilu Google. Dokud neplánujete využívat pokročilé plány společnosti Nunchuk Inc, **vyhněte se přihlašování** a pokračujte výběrem možnosti _Continue as guest_.



![image](assets/en/12.webp)



## Nastavení


Nunchuk se prezentuje v _domácím_ okně, kde lze snadno pochopit jeho filozofii ovládání, kterou si za chvíli podrobněji popíšeme.



V dolní části naleznete nabídky a v prvním kroku zvolte _Profil_ pro přístup k nastavení.



![image](assets/en/10.webp)



Poté vyberte možnost _Nastavení zobrazení_ a nadále ignorujte výzvu k vytvoření účtu.



![image](assets/en/14.webp)



Na níže uvedené obrazovce můžete zkontrolovat, zda je Wallet online a zda můžete připojit svůj server, přičemž věnujte pozornost pokynům na odkazu, který se nabízí po kliknutí na _tento návod_.



![image](assets/en/15.webp)



Uložte nastavení příkazem _Uložit nastavení sítě_, vraťte se do nabídky _Profil_ a vyberte možnost _Nastavení zabezpečení_.



![image](assets/en/16.webp)



V této nabídce nastavíte způsob obrany při otevření aplikace. Chcete-li zabránit nežádoucímu přístupu, můžete Nunchuk chránit pomocí biometrických údajů telefonu a/nebo přidat bezpečnostní kód PIN.



![image](assets/en/17.webp)



Podívejte se také do nabídky _O_, kterou vždy najdete v okně _Profil_



![image](assets/en/18.webp)



která vám umožní zkontrolovat verzi aplikace nebo v případě potřeby kontaktovat vývojáře.



![image](assets/en/19.webp)



## Generování klíčů a Wallet


Jak lze z filozofie Nunchuku snadno odhadnout, software je zamýšlen jako užitečný nástroj pro správu peněženek s více podpisy. K plnění této funkce umožňuje Nunchuk vytvářet Wallet oddělením od klíčů potřebných k uspořádání digitálních podpisů.



Ideální provoz Nunchuku ve skutečnosti zahrnuje vytvoření peněženek, které mohou být pouze hodinky, závislé na klíčích, které mohou být "studené"



Na předchozích obrazovkách jste si možná všimli, že v dolní části je nabídka s názvem _Keys_. Pokud jste si právě stáhli aplikaci Nunchuk, uvidíte jak v nabídce _Home_, tak v nabídce _Keys_ velké tlačítko s výzvou k přidání klíče, _Add Key_.



![image](assets/en/20.webp)


![image](assets/en/21.webp)



**Takto přesně funguje Nunchuk:** nejprve si generate/importujete klíče a poté vytvoříte Wallet a nakonfigurujete jej tak, aby si vybral, které klíče povolí odemknutí na něm uložených prostředků.



I v případě singlesig Wallet nejprve vytvoříte klíč a teprve poté Wallet. A přesně to nyní uděláme, začneme singlesigem Wallet, abychom prolomili ledy a objevili funkce Nunchuku.



Klikněte na tlačítko _Přidat klíč_



![image](assets/en/22.webp)



Nunchuk zobrazuje řadu podporovaných podpisových zařízení, ale pro začátek vyberte možnost _Software_.



![image](assets/en/23.webp)



Nunchuk bude generate Mnemonic, který bude uložen v zařízení. Poté je třeba zapsat posloupnost slov pro zálohování, vytvořit co nejlepší podmínky prostředí a ujistit se, že máte čas to udělat dobře a v klidu. Software zobrazí soubor Mnemonic pouze jednou, ať už se rozhodnete zobrazit jej nyní, nebo později, proto zvolte možnost _Create and backup now_ (Vytvořit a zálohovat nyní).



![image](assets/en/24.webp)



Nunchuk generuje 24slovné věty Mnemonic, které se zobrazí hned na další obrazovce



![image](assets/en/25.webp)



a poté provedl rychlou kontrolu, při níž vás požádal, abyste ze tří možností vybrali správné slovo odpovídající číslu v pořadí Mnemonic.


Pokud jste Mnemonic zapsali správně, bude tlačítko _Continue_ funkční. Stiskněte jej a pokračujte dále.



![image](assets/en/26.webp)



Pojmenujte svůj klíč a stiskněte _Continue_.



![image](assets/en/27.webp)



Na konci těchto kroků budete dotázáni, zda chcete k frázi Mnemonic přidat [passphrase](https://planb.network/en/resources/glossary/passphrase-bip39). Pokud nemáte potřebné povědomí o tom, jak používat frázi passphrase, jak zařídit její zálohování nebo jak funguje, doporučuji zvolit možnost _Nepotřebuji frázi_.



![image](assets/en/28.webp)



Klíč je nakonec vytvořen a zobrazí se v nabídce:




- Pomocí funkce _Key Spec_ je uveden hlavní otisk prstu
- Vpravo nahoře máte nastavení, tři tečky, kde můžete odstranit klíč nebo podepsat zprávu
- Vedle názvu klíče se nachází ikona vsuvky, po jejímž kliknutí můžete název klíče upravit, například abyste měli v budoucnu v klíčích pořádek.
- Jako poslední příkaz můžete zkontrolovat stav klíče: stisknutím tlačítka _Spustit kontrolu stavu_ můžete nechat aplikaci zkontrolovat, zda je klíč ohrožen.



Když jste v pořádku, klikněte na tlačítko _Done_



![image](assets/en/29.webp)



V nabídce _Keys_ se zobrazí první klávesa.



![image](assets/en/30.webp)



V nabídce _Home_ se objeví možnost vytvořit Wallet. Klepněte na tlačítko _Create new wallet_ (Vytvořit novou peněženku).



![image](assets/en/31.webp)



Nunchuk vám ukáže řadu možností, které z velké části souvisejí se službami, jež společnost nabízí a které nejsou předmětem tohoto tutoriálu.



V tomto průvodci si vytvoříme _Hot Wallet a _Vlastní peněženku_ s podrobným popisem.


Začněme s _Custom wallet_.



![image](assets/en/32.webp)



Aplikace vás jednoduchým způsobem vyzve k pojmenování tohoto nového Wallet a k výběru skriptu pro adresy. Pro tento návod jsem se rozhodl ponechat výchozí nastavení, tedy _Nativní segwit_. Po dokončení zvolte možnost _Continue_ (Pokračovat)



![image](assets/en/33.webp)



Konfigurace Wallet vás dále požádá o nastavení klíče, kterým se budou odemykat prostředky tohoto Wallet. Pokud existuje více klíčů, zobrazí se seznam, z něhož si můžete vybrat. My jsme prozatím vytvořili pouze jeden, a proto jsme se rozhodli zaškrtnout tento klíč. V pravém dolním rohu vidíte, jak vás Nunchuk požádá o nastavení budoucích více podpisů Wallet, čímž se zvýší počet _požadovaných klíčů_.



![image](assets/en/34.webp)



Protože vytváříme singlesig, ponecháme `1` a klikneme na _Continue_.



Nakonec se zobrazí ověřovací obrazovka, kde můžete zkontrolovat funkce Wallet:




- jméno
- tage `1/1 Multisig`, jak Nunchuk nazývá singlesig Wallet
- typ skriptu, `Nativní SegWit`
- klíč `Keys` s jeho otiskem a cestou odvození



Až budete spokojeni, stiskněte tlačítko _Create wallet_ (Vytvořit peněženku)



![image](assets/en/35.webp)



Wallet byl vytvořen a můžete si stáhnout soubor [.BSMS](https://github.com/Bitcoin/bips/blob/master/bip-0129.mediawiki) jako zálohu. Pro návrat do hlavní nabídky klikněte na šipku v levém horním rohu.



![image](assets/en/36.webp)



Nacházíte se v okně _Home_, kde se vám zobrazí nově vytvořený účet Wallet s informacemi o zůstatku a stavu připojení. Kliknutím do modrého prostoru získáte přístup k hlavním funkcím Wallet.



![image](assets/en/37.webp)





- Ikona objektivu v pravém horním rohu umožňuje vyhledat transakci;
- `Zobrazit konfiguraci Wallet` umožňuje přístup do konfigurační nabídky, kde můžete upravit název Wallet a povolit pokročilé možnosti vpravo nahoře (z nichž nelze získat snímky obrazovky). Zde můžete exportovat konfiguraci Wallet, štítky, nahradit klávesy, změnit [mezera limit](https://planb.network/en/resources/glossary/gap-limit) a další.



## Transakce s přístrojem Nunchuk



Ocenění _Přijímáme_



![image](assets/en/38.webp)



Aplikace je naprogramována tak, aby zobrazovala QR kód Address nebo kopírovala/sdílela skriptPubKey pro příjem prostředků v řetězci.



![image](assets/en/39.webp)



Na tento první Address dorazil UTXO,



![image](assets/en/40.webp)



ale přesto klikneme na tlačítko _Přijmout_, abychom obdrželi další.



![image](assets/en/41.webp)



Účelem je, abyste zjistili, že vám Nunchuk hlásí tuto novou adresu Address jako _nevyužitou adresu_, ale také vám ukazuje, že máte _využité adresy_ a jejich počet.



### Výdajová transakce s kontrolou mincí



Jakmile dorazí i druhý modul UTXO, vraťte se na hlavní obrazovku modulu Wallet, zkontrolujte stav obou příchozích transakcí a především klikněte na možnost _Zobrazit mince_



![image](assets/en/42.webp)



kde se zobrazí jednotlivé UTXO. Zde si můžete kliknutím na malou šipku vedle částky vybrat, zda chcete zobrazit konkrétní částku



![image](assets/en/43.webp)



a zkontrolovat, kdy dorazil, popis, blok UTXO, takže není strávil a další.



![image](assets/en/44.webp)



Pokud se však vrátíte do nabídky _Coins_ kliknutím na šipku v pravém horním rohu, můžete zapnout "Coin Control" a utrácet UTXO kontrolovaněji.



V následujícím příkladu jsem vybral položku UTXO z 21 000 Sats a poté jsem kliknul na symbol v levém dolním rohu.



![image](assets/en/45.webp)



Nunchuk automaticky otevře okno _Nová transakce_, ve kterém můžete utratit tuto částku UTXO. Ve výdajové transakci musíte nejprve nastavit částku ručně nebo výběrem možnosti _Odeslat vše vybrané_ odeslat celý kontrolní zůstatek mincí bez generování zbytků. Po nastavení částky zvolte možnost _Continue_ (Pokračovat)



![image](assets/en/46.webp)



Nyní Nunchuk ukazuje, kam vložit číslo Address, na které se mají tyto prostředky převést, podrobný popis a dokončení transakce.



![image](assets/en/47.webp)



Výběrem možnosti _Create transaction_ přenesete automatickou správu poplatků a transakcí na aplikaci. Pro větší kontrolu doporučuji zvolit možnost _Custom transaction_.



Na této nové obrazovce je důležité vybrat




- _Odpočítat poplatek od odeslané částky_, aby se zabránilo tomu, že poplatek zaplatí jiný UTXO přítomný v Wallet, utratí jej a vytvoří zbytek (což je ztráta soukromí, které se lze vyhnout);
- a poté po kontrole v průzkumníku nastavte poplatky ručně.



Po provedení všech těchto kroků klikněte na _Continue_



![image](assets/en/48.webp)



Na další obrazovce se zobrazí kompletní shrnutí transakce. Pokud je vše v pořádku, potvrďte volbou možnosti _Confirm and create transaction_ (Potvrdit a vytvořit transakci).



![image](assets/en/49.webp)



Pomocí funkce _Čeká na podpis_ vás Nunchuk upozorní, že transakcep čeká na váš podpis pro schválení výdaje, který připojíte kliknutím na tlačítko _Podepsat_.



![image](assets/en/50.webp)



V dolní části se objeví příkaz _Broadcast_, který propaguje dokončenou a podepsanou transakci.



![image](assets/en/51.webp)



### Výdajová transakce z nabídky _Odeslat_



Zatímco na hlavní stránce Wallet vidíme, že transakce odchází a čeká na potvrzení, pomocí nabídky _Odeslat_ simulujeme denní výdaj.



![image](assets/en/52.webp)



Kliknutím na tlačítko _Odeslat_ se zobrazí obrazovka pro odeslání transakce, která je stejná jako ta, kterou jsme právě viděli, ale bez kontroly mincí.



Také v tomto druhém příkladu jsem se rozhodl vybrat možnost _Custom transaction_ a odeslat celou částku, ale mohl jsem ji nastavit ručně. Jakmile se rozhodnete pro částku, kterou chcete odeslat, stiskněte tlačítko _Continue_.



![image](assets/en/53.webp)



Poté vždy proveďte případ, zda se poplatky odečtou od daného UTXO (v tomto příkladu je volba vynucená, protože je pouze jeden), ručně upravte poplatky podle aktuální situace v Mempool a stiskněte tlačítko .



![image](assets/en/54.webp)



Pokud je souhrnná obrazovka vyhovující, zvolte možnost _Confirm and create transaction_ (Potvrdit a vytvořit transakci).



![image](assets/en/55.webp)



Podepsat transakci pomocí _Sign_



![image](assets/en/56.webp)



a rozšířit ji do sítě.



![image](assets/en/57.webp)



Wallet je v tomto okamžiku zůstatek na nule a historie se aktualizuje.



![image](assets/en/58.webp)



## Vytvoření "Hot Wallet"



Na závěr, abychom nevynechali nic z počátečních fází Nunchuk mobile, se podívejme, jak vzniká to, co aplikace nazývá "Hot Wallet"



V nabídce _Home_ zařízení Nunchuk, kde se zobrazí seznam peněženek, klikněte na `+` v pravém horním rohu.



![image](assets/en/59.webp)



Z možností vyberte _Hot wallet_



![image](assets/en/60.webp)



Nunchuk vám na stránce s prezentací poskytne několik rad, jak zacházet s peněženkami Hot. Pro pokračování vyberte možnost _Continue_.



![image](assets/en/61.webp)



Po několika okamžicích se vytvoří položka Wallet a objeví se v seznamu v hnědé barvě. Touto barvou vás Nunchuk upozorní, že jste ještě nezálohovali Wallet.



![image](assets/en/62.webp)



Kliknutím na název Wallet získáte přístup k jeho konfiguraci a možná si všimnete výzvy k okamžitému zálohování fráze Mnemonic.



![image](assets/en/63.webp)



Postup je stejný, jako jsme viděli již dříve, takže se nad ním nebudeme znovu pozastavovat. Po jeho provedení vás Nunchuk přenese na příslušnou stránku klíče, kterou můžete upravit jako tu, kterou jste vytvořili postupem _Custom_.



![image](assets/en/64.webp)



Zkuste také _Spustit kontrolu stavu_



![image](assets/en/65.webp)



nebo se podívejte, jak zobrazit všechny peněženky v _Home_ aplikace.



![image](assets/en/66.webp)



## Mít na paměti, že je třeba pokračovat samostatně


Stejně jako existuje pořadí pro vytváření, tj. nejprve generování klíčů a poté Wallet, je třeba zachovat opačné pořadí pro odstraňování těchto položek z aplikace.



Pokud potřebujete odstranit jeden z klíčů, měli byste nejprve prozíravě odstranit Wallet nebo peněženky, které používají jeden z podpisových klíčů pro transakce: nejprve odstraníte peněženky a teprve poté klíče. Pokud toto pořadí nedodržíte, stane se, že klíč nebudete moci odstranit.



Nyní, když už víte, jak začít s aplikací Nunchuk, můžete pokračovat ve studiu této aplikace a objevovat její tajemství. V tomto návodu jsme se věnovali pouze prvním krokům, ale existují i složitější aplikace a pokročilé potřeby, které vám tento Software Wallet může pomoci splnit.