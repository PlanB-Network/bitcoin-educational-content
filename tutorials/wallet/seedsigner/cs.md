---
name: SeedSigner
description: DIY, bezstavový, cenově dostupný a plně vzduchem krytý hardware wallet
---

![cover](assets/cover.webp)



SeedSigner je hardware wallet Bitcoin s otevřeným zdrojovým kódem, který si může každý sám sestavit z levných elektronických součástek pro všeobecné použití. Na rozdíl od komerčních produktů, jako je Ledger, Coldcard nebo Trezor, se nejedná o zařízení připravené k použití, které by vyráběla nějaká společnost: jde o komunitní projekt, který umožňuje každému vytvořit si vlastní zařízení a kontrolovat každý krok.



SeedSigner je navržen tak, aby byl 100% ***air-gapped***: nikdy se nepřipojuje k internetu, nemá Wi-Fi ani Bluetooth (v případě Raspberry Pi Zero v1.3) a nikdy není připojen k počítači pro výměnu dat. Komunikace probíhá výhradně prostřednictvím systému výměny QR kódů. Konkrétně váš software pro správu portfolia (např. Sparrow Wallet) zobrazuje transakce, které mají být podepsány, ve formě QR kódů; vy je naskenujete pomocí fotoaparátu SeedSigneru a zařízení pak transakci podepíše pomocí vašich soukromých klíčů dočasně uložených v jeho paměti RAM. Nakonec vygeneruje QR kódy obsahující podepsanou transakci, které naskenujete pomocí svého softwaru a odešlete je do sítě Bitcoin.



![Image](assets/fr/001.webp)



SeedSigner je také ***stateless***. Jinými slovy, na rozdíl od jiných hardwarových peněženek neukládá vaše seed ani vaše soukromé klíče trvale. Při každém restartu je její paměť zcela prázdná, pokud zařízení nenakonfigurujete tak, aby ukládalo vaše nastavení na kartu microSD. Svůj klíč seed proto musíte při každém použití zadat znovu, přičemž nejpraktičtější metodou je uložit jej ve formě QR kódu, který se při spuštění naskenuje pomocí kamery zařízení SeedSigner. Tento způsob fungování výrazně omezuje plochu útoku: i když vám zloděj zařízení ukradne, nenajde v něm žádné informace, protože je ve výchozím nastavení vždy prázdné.



Další možností, jak uložit kartu seed a používat ji se SeedSignerem, je použití čipové karty *SeedKeeper* ve spojení s kompatibilní čtečkou. Získáte tak velmi robustní *bezpečný prvek* pro uložení seed a zároveň můžete k podepisování transakcí používat obrazovku SeedSigner. Tato konkrétní konfigurace je však předmětem jiného specializovaného tutoriálu. Zde se zaměříme na základní použití SeedSigneru:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

Projekt SeedSigner zaujímá v ekosystému Bitcoin důležité místo, protože nabízí všem lidem na celém světě možnost využívat pokročilé zabezpečení k ochraně svých bitcoinů. Jeho hlavní výhoda spočívá v jeho dostupnosti: potřebný hardware lze pořídit za méně než 50 USD. Navíc umožňuje lidem žijícím v zemích s omezeným přístupem sestavit si vlastní hardware wallet ze standardních počítačových komponent, které jsou snadno k sehnání a méně podléhají regulačním omezením.



Ale i mimo tyto konkrétní souvislosti pro vás může být SeedSigner zajímavou volbou: je to open-source, funguje bez stavu a vzduchem a omezuje vektory útoku spojené s dodavatelským řetězcem vašeho hardwaru wallet.



## 1. Požadované vybavení



K sestavení aplikace SeedSigner budete potřebovat následující komponenty:





- Raspberry Pi Zero
    - Doporučuje se verze 1.3, která neobsahuje Wi-Fi ani Bluetooth, což zajišťuje naprostou izolaci.
 - Verze W a v2 jsou také kompatibilní, ale obsahují čip Wi-Fi/Bluetooth. Proto je vhodné jej fyzicky deaktivovat vyjmutím rádiového modulu z karty. Operace je poměrně jednoduchá, ale vyžaduje přesnost (u modelu Zero W stačí jemné kleště, zatímco u modelu v2 je k odstranění kovové destičky, která modul ukrývá, zapotřebí horké pero). V tomto návodu nebudu zabíhat do podrobností, ale všechny pokyny najdete v tomto dokumentu: *[Zakázání WiFi/Bluetooth pomocí hardwaru](https://github.com/DesobedienteTecnologico/rpi_disable_wifi_and_bt_by_hardware)*.
 - Upozornění: některé modely Raspberry Pi Zero se prodávají bez předpájených pinů GPIO. Můžete si buď koupit verzi přímo s integrovanými piny (nejjednodušší řešení), nebo si piny koupit zvlášť a připájet je sami (složitější řešení).
 - Nezapomeňte přiložit napájecí zdroj micro-USB.



![Image](assets/fr/002.webp)





- Waveshare 1,3" obrazovka (240 × 240 px)** (ve francouzštině)
    - Je nutné zvolit tento konkrétní model: existují i jiné podobné obrazovky, ale s jiným rozlišením. Bez rozlišení 240 × 240 px bude displej nepoužitelný.
    - Na obrazovce jsou tři tlačítka a mini joystick pro uživatelské rozhraní.



![Image](assets/fr/003.webp)





- Kamera kompatibilní s Raspberry Pi Zero**
    - Možnost 1: standardní fotoaparát s širokou zlatou podložkou (ověřte kompatibilitu s vaším pouzdrem).
    - Možnost 2: kompaktnější kamera "*Zero*", navržená speciálně pro Pi Zero.



![Image](assets/fr/004.webp)





- Karta MicroSD**
    - Doporučená kapacita: 4 až 32 GB.





- Bydlení (nepovinné, ale doporučené)** (nepovinné, ale doporučené)** (nepovinné, ale doporučené)** (nepovinné, ale doporučené)**)
    - Chrání zařízení a usnadňuje jeho používání.
    - Nejoblíbenějším modelem je "*Orange Pill Case*", pro který jsou k dispozici [open-source soubory STL pro 3D tisk](https://github.com/SeedSigner/seedsigner/tree/dev/enclosureshttps://github.com/SeedSigner/seedsigner/tree/dev/enclosures).
    - Krabice jsou k dispozici také u [nezávislých prodejců spojených s projektem](https://seedsigner.com/hardware/).



![Image](assets/fr/005.webp)



Tyto komponenty si můžete zakoupit samostatně nebo si pro větší jednoduchost vybrat hotové balíčky, které obsahují veškerý potřebný hardware. Osobně jsem si objednal svůj balíček [na této francouzské stránce](https://bitcoinbazar.fr/), ale seznam prodejců pro jednotlivé oblasti světa najdete také na [stránce s hardwarem projektu SeedSigner](https://seedsigner.com/hardware/). Pokud dáváte přednost nákupu jednotlivých komponent, jsou k dispozici na hlavních platformách elektronických obchodů nebo ve specializovaných obchodech.



## 2. Příprava softwaru



Jakmile máte hardware pohromadě, musíte připravit kartu microSD a nainstalovat na ni systém SeedSigner. Za tímto účelem přejděte do svého běžného osobního počítače a připojte kartu microSD určenou pro SeedSigner.



### 2.1. Stáhnout



Přejděte na [oficiální repozitář projektu na GitHubu](https://github.com/SeedSigner/seedsigner/releases). Na nejnovější verzi softwaru stáhněte :




- Obraz `.img` odpovídající vašemu modelu počítače Pi.
- Soubor `.sha256.txt`.
- Soubor `.sha256.txt.sig`.



![Image](assets/fr/006.webp)



Před zahájením instalace zkontrolujme software.



### 2.2 Ověřování v systémech Linux a macOS



Začněte importem oficiálního veřejného klíče projektu SeedSigner přímo z databáze Keybase :



```
gpg --fetch-keys https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/007.webp)



Terminál by vám měl oznámit, že klíč byl importován nebo aktualizován. Poté spusťte příkaz pro ověření souboru s podpisem (nezapomeňte příkaz upravit podle své verze, zde `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/008.webp)



Pokud je vše v pořádku, na výstupu by mělo být napsáno `Dobrý podpis`. To znamená, že soubor `.sha256.txt` byl podepsán právě importovaným klíčem a že podpis je platný. Varovné hlášení `WARNING: This key is not certified with a trusted signature` ignorujte: je to normální, protože nyní je na vás, abyste zkontrolovali, zda použitý klíč patří do projektu SeedSigner.



Za tímto účelem porovnejte posledních 16 znaků zobrazeného otisku s těmi, které jsou k dispozici na [Keybase.io/SeedSigner](https://keybase.io/seedsigner), na jejich [oficiálním Twitteru](https://twitter.com/SeedSigner/status/1530555252373704707) nebo v souboru zveřejněném na [SeedSigner.com](https://seedsigner.com/keybase.txt). Pokud se tyto identifikátory přesně shodují, můžete si být jisti, že klíč je skutečně klíčem projektu. V případě pochybností okamžitě přestaňte a požádejte o pomoc komunitu SeedSigner (Telegram, X, GitHub...).



Po ověření klíče můžete zkontrolovat, zda stažený obraz nebyl změněn (nezapomeňte upravit příkaz podle své verze, zde `0.8.6.`):



```
shasum -a 256 --ignore-missing --check seedsigner.0.8.6.sha256.txt
```



![Image](assets/fr/009.webp)





- V systému Linux je tento příkaz integrovaný.
- Upozornění: Verze systému macOS před verzí `Big Sur (11)` nerozpoznávají možnost `--ignore-missing`. V takovém případě ji odstraňte a ignorujte varování o chybějících souborech.



Očekávaným výsledkem je hlášení `OK` u souboru `.img`. To potvrzuje, že nahraný obrázek je totožný s obrázkem zveřejněným projektem a nebyl upraven.



### 2.3 Ověřování systému Windows



V systému Windows je postup podobný, ale příkazy se liší. Začněte instalací [Gpg4win](https://www.gpg4win.org/) a otevřete aplikaci *Kleopatra*. Importujte veřejný klíč projektu SeedSigner z adresy URL Keybase :



```
https://keybase.io/seedsigner/pgp_keys.asc
```



![Image](assets/fr/010.webp)



Poté otevřete prostředí PowerShell ve složce, kde jsou umístěny stažené soubory (`Shift` + kliknutí pravým tlačítkem myši > `Otevřít PowerShell zde`). Spusťte následující příkaz pro kontrolu podpisu manifestu (nezapomeňte příkaz upravit podle své verze, zde `0.8.6.`):



```
gpg --verify seedsigner.0.8.6.sha256.txt.sig
```



![Image](assets/fr/011.webp)



Pokud je vše v pořádku, na výstupu by mělo být napsáno `Dobrý podpis`. To znamená, že soubor `.sha256.txt` byl podepsán právě importovaným klíčem a že podpis je platný. Varovné hlášení `WARNING: This key is not certified with a trusted signature` ignorujte: je to normální, protože nyní je na vás, abyste zkontrolovali, zda použitý klíč patří do projektu SeedSigner.



Za tímto účelem porovnejte posledních 16 znaků zobrazeného otisku s těmi, které jsou k dispozici na [Keybase.io/SeedSigner](https://keybase.io/seedsigner), na jejich [oficiálním Twitteru](https://twitter.com/SeedSigner/status/1530555252373704707) nebo v souboru zveřejněném na [SeedSigner.com](https://seedsigner.com/keybase.txt). Pokud se tyto identifikátory přesně shodují, můžete si být jisti, že klíč je skutečně klíčem projektu. V případě pochybností okamžitě přestaňte a požádejte o pomoc komunitu SeedSigner (Telegram, X, GitHub...).



Po ověření klíče je třeba zkontrolovat, zda nebyl soubor s obrázkem poškozen. K tomu použijte následující příkaz v prostředí PowerShell :



```
CertUtil -hashfile seedsigner_os.0.8.6.[your-Pi-model].img SHA256
```



Příklad pro Raspberry Pi Zero 2 (nezapomeňte příkaz upravit podle své verze, zde `0.8.6.`):



```
CertUtil -hashfile seedsigner_os.0.8.6.pi02w.img SHA256
```



![Image](assets/fr/012.webp)



Prostředí PowerShell poté vypočítá hash SHA256 souboru s obrázkem. Porovnejte tento hash s odpovídající hodnotou v souboru `seedsigner.0.8.6.sha256.txt`.




- Pokud jsou obě hodnoty zcela shodné, kontrola proběhla úspěšně a můžete pokračovat.
- Pokud se liší, je soubor poškozený nebo poškozený. Nepoužívejte jej a začněte stahovat znovu.



![Image](assets/fr/013.webp)



Úspěšné ověření zaručuje, že váš soubor `.img` je autentický (podepsaný SeedSignerem) a nezměněný (nemodifikovaný). Poté můžete bez obav přejít k dalšímu kroku.



### 2.4. Záblesk obrazu



Pokud jej ještě nemáte, stáhněte si software [Balena Etcher] (https://etcher.balena.io/) a poté :




- Vložte kartu microSD do počítače.
- Spuštění nástroje Etcher.
- Vyberte stažený a ověřený soubor `.img`.
- Jako cíl vyberte kartu microSD.
- Klikněte na `Flash!`.



![Image](assets/fr/014.webp)



Počkejte na dokončení procesu: vaše microSD je připravena k použití. Nyní je čas na montáž!



## 3. Sestava SeedSigner



Po přípravě karty microSD a jejím flashnutí pomocí softwaru SeedSigner můžete pokračovat v závěrečné montáži. Nespěchejte, protože některé součásti jsou křehké (zejména ubrus, kamera a piny GPIO).



### 3.1 Příprava pouzdra



Nejprve otevřete kufr. Zkontrolujte, zda je čistý a zda vnitřním spojovacím prvkům nepřekáží zbytky plastu z 3D tisku. Dávejte pozor na :




- Umístění kamery (malý kruhový otvor vpředu).
- Otevření obrazovky.
- Výřezy pro porty micro-USB a slot microSD počítače Raspberry Pi Zero.



### 3.2 Instalace kamery



Najděte na Raspberry Pi Zero páskový konektor kamery: je to tenký černý proužek na boku desky, který lze mírně nadzvednout a otevřít. Opatrně jej zvedněte, aniž byste jej nutili: měl by se jednoduše o několik milimetrů vyklopit.



![Image](assets/fr/015.webp)



Vložte kryt fotoaparátu. Hnědá/měděná část by měla směřovat dolů. Ujistěte se, že je pevně usazen v konektoru, aniž by se protáčel.



![Image](assets/fr/016.webp)



Zavřením černého pruhu ubrus zajistěte (ucítíte lehké cvaknutí). Opatrně zkontrolujte, zda zůstává na místě a nehýbe se.



![Image](assets/fr/017.webp)



Poté umístěte modul kamery do příslušného otvoru v krytu. V závislosti na modelu může být modul zacvaknut přímo nebo může být k jeho uchycení zapotřebí malý lepicí proužek. Objektiv musí být dokonale zarovnaný a směřovat ven.



### 3.3 Instalace Raspberry Pi Zero



Pokud používáte pouzdro, vložte do něj desku Raspberry Pi Zero. Pečlivě zarovnejte porty s připravenými otvory.



Poté umístěte displej Waveshare na zařízení Raspberry Pi Zero. Kolíky GPIO počítače Pi by měly dokonale lícovat se zásuvkou displeje. Pomalu přitlačte displej na kolíky a vyvíjejte rovnoměrný tlak na každou stranu, aby nedošlo k jejich ohnutí.



![Image](assets/fr/018.webp)



Pokud máte skříň, dokončete sestavu přidáním předního panelu a joysticku.



Nakonec vložte kartu microSD s flashovaným softwarem do slotu na okraji počítače Raspberry Pi Zero. Ujistěte se, že zapadla na své místo.



### 3.4 První spuštění



Připojte napájecí kabel micro-USB k vyhrazenému portu. Počkejte přibližně jednu minutu. Mělo by se zobrazit logo SeedSigner a poté domovská obrazovka.



![Image](assets/fr/019.webp)



Nejprve zkontrolujte, zda jednotlivé komponenty správně fungují, a to v nabídce `Nastavení > Test I/O`.



![Image](assets/fr/020.webp)



Otestujte všechna tlačítka a ujistěte se, že reagují správně. Poté klikněte na tlačítko `KEY1` a zkontrolujte, zda kamera funguje podle očekávání. Tím se pořídí snímek.



![Image](assets/fr/021.webp)



### 3.5 Nastavení kamery



V závislosti na způsobu upevnění zařízení SeedSigner může kamera zobrazovat obrácený obraz. Chcete-li to napravit, přejděte do `Nastavení > Rozšířené > Otočení kamery` a v případě potřeby zvolte otočení o 180°.



![Image](assets/fr/022.webp)



Pokud jste změnili orientaci fotoaparátu nebo chcete později změnit jiná nastavení (například jazyk rozhraní), musíte povolit zachování nastavení na kartě microSD. Jinak se vaše nastavení vrátí na výchozí při každém restartu, protože Raspberry Pi Zero nemá žádnou trvalou paměť.



Za tímto účelem otevřete nabídku `Nastavení > Trvalé nastavení` a vyberte možnost `Povoleno`.



![Image](assets/fr/023.webp)



Pokud je vše funkční, váš SeedSigner je nyní připraven k použití!



## 4. Nastavení SeedSigner



Před vytvořením účtu Bitcoin wallet nakonfigurujme SeedSigner. Protože běží na Raspberry Pi Zero bez trvalé paměti, jeho nastavení se neukládá automaticky, pokud je neuložíte na kartu microSD. Ujistěte se tedy, že jste tuto možnost povolili, jinak budou tato nastavení při restartu ztracena (viz krok 3.5).



### 4.1 Přístup k menu parametrů



Spusťte aplikaci SeedSigner a počkejte, až se zobrazí domovská obrazovka. Pomocí joysticku přejděte na možnost `Nastavení` a poté ji potvrďte stisknutím středového tlačítka. Nyní vstoupíte do hlavní nabídky nastavení.



![Image](assets/fr/024.webp)



### 4.2 Výběr softwaru pro správu portfolia



Poté přejděte do nabídky `Software koordinátoru`.



![Image](assets/fr/025.webp)



`Koordinátor` označuje software pro správu portfolia, se kterým bude váš SeedSigner komunikovat prostřednictvím QR kódů. Tento software je nainstalován buď v počítači, nebo ve vašem chytrém telefonu. Umožní vám spravovat vaše bitcoiny, ale bez toho, abyste měli přístup k vašim soukromým klíčům. SeedSigner zůstává jediným zařízením schopným podepisovat vaše transakce.



Aktuální verze firmwaru podporuje několik programů: Sparrow, Specter, BlueWallet, Nunchuk a Keeper. V mém případě používám **Sparrow Wallet**, který doporučuji zejména pro jeho jednoduchost a bohatou funkčnost.



Pokud nevíte, jak ji nainstalovat, můžete postupovat podle tohoto návodu:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Stačí si v nabídce vybrat požadovaný software.



![Image](assets/fr/026.webp)



### 4.3 Zobrazení jednotek a množství



V nabídce `Zobrazení nominální hodnoty` můžete zvolit jednotku, ve které se částky zobrazují:




- `BTC`
- mBTC` (milibitcoin nebo 0,001 BTC)
- gW-15 (satoši nebo 1/100 000 000 BTC)



Jednotka **sats** je obecně nejpraktičtější pro malá množství.



![Image](assets/fr/027.webp)



### 4.4 Rozšířená nastavení



Nyní přejděte do nabídky `Rozšířené`. Zde najdete několik užitečných možností:




- gW-17 network`: je třeba upravit pouze v případě, že chcete používat SeedSigner na Testnet.
- qR code density`: upravuje množství informací obsažených v každém QR kódu. Můžete ponechat výchozí hodnotu, pokud se vám při skenování nezdá obtížně čitelná.
- `Xpub export`: povoluje nebo zakazuje export vašeho rozšířeného veřejného klíče (`xpub`, `ypub`, `zpub`) do softwaru pro správu portfolia prostřednictvím QR kódu (funkce, kterou budeme používat později, takže ji prozatím ponechte povolenou).
- `Typy skriptů`: definuje typy skriptů, které mohou uzamknout vaše bitcoiny. Tento parametr nemusíte upravovat, protože typ skriptu bude nastaven přímo na Sparrow. Zde se jedná pouze o skripty, se kterými je SeedSigner oprávněn manipulovat.



### 4.5 Výběr jazyka



V nabídce `Jazyk` můžete změnit jazyk rozhraní podle svých preferencí.



![Image](assets/fr/028.webp)



## 5. Vytváření a ukládání seed



Základem vašeho portfolia Bitcoin je seed (nebo mnemotechnická fráze). Slouží k odvození vašich soukromých klíčů a adres a poskytuje přístup k vašim finančním prostředkům. SeedSigner nabízí několik způsobů jeho generování, na které se podíváme v této části.



Než začneme, připomeňme si několik zásadních věcí:




- Tato fráze poskytuje plný, neomezený přístup ke všem vašim bitcoinům.** Kdokoli, kdo má tuto frázi, může ukrást vaše prostředky, a to i bez fyzického přístupu k vašemu SeedSigneru;
- V případě ztráty nebo krádeže hardwaru wallet se k obnově obvykle používá fráze o 12 slovech. Protože je však SeedSigner *bezstavové* zařízení, nikdy neregistruje váš seed. Vaše fyzické zálohy tedy nejsou pouhými záložními kopiemi, ale **jediným způsobem, jak používat váš wallet**. Pokud o tyto zálohy přijdete, vaše bitcoiny budou trvale ztraceny. Zálohujte je proto pečlivě, na několika médiích a na bezpečných místech;
- Pokud teprve začínáte, doporučuji vám přečíst si tento návod, kde se podrobně seznámíte s riziky spojenými se správou mnemotechnické fráze :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.1 Přístup k nástroji pro vytvoření seed



Na domovské obrazovce aplikace SeedSigner přejděte do nabídky `Nástroje`.



![Image](assets/fr/029.webp)



Nyní budete mít generate seed. seed je jednoduše velké náhodné číslo. Čím náhodněji je generováno, tím je bezpečnější. SeedSigner nabízí dva způsoby, jak to provést:




- fotoaparátu": seed vzniká z vizuálního šumu fotografie. Pořídíte snímek náhodného prostředí (objektu, krajiny, obličeje atd.), jehož pixelové variace jsou použity pro entropii generate. Je to rychlá metoda, ale není reprodukovatelná.
- hody kostkou": házíte kostkou, abyste vytvořili potřebnou entropii. Je to časově náročnější, ale reprodukovatelné, a tudíž ověřitelné. Pokud se rozhodnete pro tuto metodu, postupujte podle rad v tomto návodu (zde není třeba počítat kontrolní součet, o to se postará SeedSigner):



https://planb.academy/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228

### 5.2 Vytvoření seed s fotografií



Pokud zvolíte metodu fotografie, klikněte na `Nový seed` (s ikonou fotoaparátu), pořiďte snímek a potvrďte jej. Poté zvolte délku věty (12 nebo 24 slov), která se zobrazí na obrazovce pro uložení. Následující kroky jsou totožné s částí 5.3.



### 5.3 Vytváření seed pomocí kostek



V tomto návodu použijeme metodu **Hody kostkou**. Klikněte na `Nový seed` (s ikonou kostky).



![Image](assets/fr/030.webp)



Poté zvolte délku mnemotechnické fráze. dvanáct slov již nabízí dostatečnou úroveň zabezpečení, takže tuto volbu doporučuji.



![Image](assets/fr/031.webp)



Hoďte kostkou a výsledná čísla zadejte pomocí kurzoru. Stisknutím prostředního tlačítka každý údaj potvrdíte. Pokud uděláte chybu, můžete se vrátit zpět. Použijte několik různých kostek, abyste snížili vliv případných nevyvážených kostek. Ujistěte se, že vás při této operaci nikdo nesleduje.



![Image](assets/fr/032.webp)



Jakmile zadáte svých 50 hodů, SeedSigner vygeneruje vaši větu. **Pokud začínáte, postupujte pečlivě podle pokynů v tomto návodu:**



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### 5.4 Zobrazení a uložení seed



Pečlivě si zapište slova mnemotechnické fráze na vhodnou fyzickou podložku (papír nebo kov).



![Image](assets/fr/033.webp)



### 5.5 Kontrola zálohy



Aby se předešlo chybám při zálohování, požádá vás SeedSigner o ověření zálohy. Klikněte na `Ověřit`.



![Image](assets/fr/034.webp)



Poté zadejte požadované slovo podle jeho pořadí ve větě. Například zde mám vybrat třetí slovo ve větě.



![Image](assets/fr/035.webp)



Pokud uděláte chybu, SeedSigner vás o tom bude informovat a vy budete muset začít znovu, přičemž si nezapomeňte poznamenat mnemotechnickou frázi, až vám ji předá. Tento ověřovací krok zajistí, že vaše záloha je správná a úplná. Po ověření se na obrazovce zobrazí `Záloha ověřena`.



![Image](assets/fr/036.webp)



Chcete-li provést úplnější test obnovení, postupujte podle tohoto návodu :



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

### 5.6 Porozumění konceptu "bezstavového zařízení



SeedSigner je zařízení bez trvalé paměti. To znamená, že vaše karta seed není v zařízení nikdy uložena (na rozdíl například od karty Ledger, Trezor nebo Coldcard). Jakmile vypnete napájení, zařízení seed z paměti RAM zcela zmizí. Po restartu se SeedSigner vrátí do prázdného stavu: pak mu budete muset znovu předat svůj seed, aby mohl podepisovat vaše transakce.



To poskytuje základní ochranu. Na rozdíl od jiných hardwarových peněženek je SeedSigner založen na Raspberry Pi Zero, které nemá žádnou fyzickou ochranu, včetně *Secure Element*. Protože však nejsou uložena žádná citlivá data, ani fyzicky napadené zařízení by útočníkovi neumožnilo získat vaše soukromé klíče nebo utratit vaše bitcoiny.



Na druhou stranu tato architektura znamená další odpovědnost: bez zálohy jsou vaše prostředky definitivně ztraceny. Proto doporučuji **dvojité zálohování**. Frázi pro obnovu již máte: jedná se o vaši hlavní dlouhodobou zálohu, kterou je třeba uchovávat na bezpečném místě. Nyní vytvoříme kopii této fráze ve formě **QR kódu**.



Při každém použití SeedSigneru naskenujete tento QR kód pomocí fotoaparátu zařízení, které si dočasně načte do paměti váš kód seed, zatímco podepisujete transakce. Tuto druhou zálohu, určenou pro každodenní použití, je rovněž třeba uchovávat s maximální opatrností: kdokoli, kdo má tento QR kód, má plný přístup k vašim bitcoinům.


Doporučuji vám také, abyste si kód QR a mnemotechnickou frázi uložili na dvě oddělená místa, abyste v případě reklamace o vše nepřišli.



Pokročilejší a bezpečnější alternativou je použití SeedSigneru se zařízením **SeedKeeper**, které ukládá kód seed do kódu secure element. Chcete-li se dozvědět více, podívejte se na tento návod:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

### 5.7 Zápis otisku hlavního klíče



Po dokončení ověření SeedSigner zobrazí otisk hlavního klíče wallet. Tento otisk identifikuje váš klíč wallet a zajistí, že v budoucnu použijete správnou frázi pro obnovení. Neodhaluje žádné informace o vašich soukromých klíčích, takže je můžete bezpečně uložit na digitální médium. Jen se ujistěte, že máte přístupnou kopii a nikdy ji neztratíte.



![Image](assets/fr/037.webp)



V této fázi můžete také přidat **passphrase BIP39**, abyste posílili zabezpečení svého wallet. V závislosti na vaší zálohovací strategii se tato možnost může vyplatit, ale nese s sebou také rizika: pokud ztratíte passphrase, přístup k bitcoinům bude trvale ztracen.



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Pokud ještě nejste obeznámeni s konceptem passphrase, doporučuji vám přečíst si tento obsáhlý návod:



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

![Image](assets/fr/038.webp)



### 5.8 Uložení seed ve formátu QR (*SeedQR*)



SeedSigner vám umožní převést váš seed na papírový QR kód s názvem *SeedQR*. Tato metoda zjednodušuje načítání kódu wallet, protože se vyhnete ručnímu přepisování každého slova.



K tomu budete potřebovat prázdný papír nebo kovový QR kód odpovídající délce vaší mnemotechnické fráze. Pokud jste si zakoupili kompletní balíček SeedSigner, jsou šablony obvykle součástí balení. Pokud ne, můžete si je stáhnout a vytisknout (nebo reprodukovat ručně) zde :




- [formát 12 slov](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)
- [formát 24 slov](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_29x29.pdf)
- [Kompaktní formát 12 slov](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_21x21.pdf)
- [Kompaktní formát 24 slov](https://github.com/SeedSigner/seedsigner/blob/dev/docs/seed_qr/printable_templates/grid_25x25.pdf)



Na obrazovce seed vyberte možnost `Backup Seed`.



![Image](assets/fr/039.webp)



Poté vyberte možnost `Exportovat jako SeedQR`.



![Image](assets/fr/040.webp)



Poté vyberte požadovaný formát (normální nebo kompaktní) podle dostupné šablony papíru.



![Image](assets/fr/041.webp)



Kliknutím na tlačítko `Začítat` zahájíte vytváření *SeedQR*. Poté SeedSigner zobrazí řadu mřížek (A1, A2, B1 atd.), z nichž každá odpovídá části kódu.



![Image](assets/fr/042.webp)



Pečlivě reprodukujte každou černou tečku na záznamovém archu a poté se pomocí joysticku přesuňte na další blok. Nespěchejte: pouhé chybné zarovnání může způsobit nepoužitelnost QR kódu.



Několik tipů:




- Začněte tužkou, abyste mohli opravit případné chyby, a po dokončení se vraťte k použití jemného černého pera;
- Stačí dobře vystředěný bod uprostřed čtverce, není třeba jej zcela vyplnit.



![Image](assets/fr/043.webp)



Poté klikněte na `Potvrdit SeedQR` a naskenujte QR kód, abyste zkontrolovali, zda funguje správně.



![Image](assets/fr/044.webp)



Pokud se zobrazí zpráva `Úspěch`, je váš *SeedQR* platný: můžete přejít k dalšímu kroku.



![Image](assets/fr/045.webp)



**Tento list uchovávejte stejně přísně jako svou větu o zotavení. Kdokoli, kdo vlastní tento QR kód, může rekonstruovat vaše soukromé klíče a ukrást vaše bitcoiny.**



Gratulujeme, vaše portfolio Bitcoin je nyní funkční! Nyní naimportujeme jeho veřejné součásti do **Sparrow Wallet**, abychom jej mohli snadno spravovat.



## 6. Import wallet do Sparrow



Po nastavení SeedSigneru a správném vygenerování a uložení seed je dalším krokem propojení tohoto portfolia se softwarem pro správu, například Sparrow Wallet. Váš seed zůstane vždy offline, protože do Sparrow bude přenášena pouze veřejná část vašeho portfolia. To umožní tomuto softwaru zobrazovat vaše adresy, transakce a vytvářet nové transakce, aniž byste kdy mohli utratit své bitcoiny. Chcete-li utratit své bitcoiny, váš SeedSigner bude muset vždy podepsat transakci připravenou Sparrow.



### 6.1 Příprava SeedSigner



Vložte kartu microSD s operačním systémem, zapněte SeedSigner a načtěte právě vytvořený kód seed ze záložního kódu QR. Na domovské obrazovce vyberte možnost `Scan` a poté pomocí SeedSigneru naskenujte svůj SeedQR.



![Image](assets/fr/046.webp)



Zkontrolujte, zda se otisk prstu na hlavním klíči shoduje s otiskem prstu na wallet. Pokud používáte klíč passphrase, zadejte jej v této fázi.



![Image](assets/fr/047.webp)



Tím se dostanete do nabídky vašeho portfolia, v mém případě s názvem `d4149b27`. Pokud jste zpět na domovské obrazovce, vyberte možnost `Seznamy` a poté vyberte tisk odpovídající vašemu portfoliu. Poté klikněte na `Exportovat Xpub`.



![Image](assets/fr/048.webp)



Vyberte typ portfolia. V našem případě se jedná o jedno portfolio: vyberte `Jednoznačné`.



![Image](assets/fr/049.webp)



Dále je třeba zvolit standard skriptování. Nejnovější a nejúspornější z hlediska transakčních nákladů je `Taproot`. Proto vám doporučuji zvolit tento standard.



![Image](assets/fr/050.webp)



Zobrazí se varovná zpráva. To je normální: tento rozšířený veřejný klíč (`xpub`) umožňuje zobrazit všechny adresy odvozené z vašeho seed (na prvním účtu). Neumožňuje vám utrácet vaše prostředky, ale odhaluje strukturu vašeho portfolia. Pokud někdy unikne, je to problém pro vaše soukromí, ale ne pro bezpečnost vašich bitcoinů: umožňuje je vidět, ale ne utrácet.



Pokud jste se zobrazenými informacemi spokojeni, klikněte na `Rozumím` a poté na `Exportovat Xpub`.



SeedSigner pak vygeneruje váš xpub v podobě dynamického QR kódu obsahujícího všechny údaje, které potřebujete ke správě svého portfolia v Sparrow Wallet.



![Image](assets/fr/051.webp)



Pomocí joysticku můžete nastavit jas obrazovky pro snadnější skenování QR kódu.



### 6.2 Import nového portfolia do Sparrow Wallet



Ujistěte se, že máte v počítači nainstalovaný software Sparrow Wallet. Pokud nevíte, jak jej správně stáhnout, zkontrolovat a nainstalovat, podívejte se na náš úplný návod na toto téma:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

V počítači otevřete program Sparrow Wallet a v panelu nabídek klikněte na možnost `Soubor → Importovat Wallet`.



![Image](assets/fr/052.webp)



Přejděte dolů na položku `SeedSigner` a vyberte možnost `Scan...`. Otevře se webová kamera: naskenujte dynamický QR kód zobrazený na obrazovce SeedSigner.



![Image](assets/fr/053.webp)



Přiřaďte svému portfoliu název a klikněte na tlačítko `Vytvořit Wallet`. Poté vás Sparrow vyzve k nastavení hesla pro uzamčení místního přístupu k tomuto wallet. Zvolte silné heslo: chrání přístup k datům vašeho portfolia v Sparrow (veřejné klíče, adresy, štítky a historie transakcí). Toto heslo není potřeba k pozdějšímu obnovení portfolia: k tomuto účelu je zapotřebí pouze vaše mnemotechnická fráze (a případně passphrase).



Doporučuji toto heslo uložit do správce hesel, abyste ho neztratili.



![Image](assets/fr/054.webp)



Úložiště klíčů bylo úspěšně importováno.



![Image](assets/fr/055.webp)



Poté zkontrolujte, zda se otisk `Master fingerprint` zobrazený v aplikaci Sparrow shoduje s otiskem dříve zaznamenaným v aplikaci SeedSigner.



Váš SeedSigner a Sparrow Wallet jsou nyní bezpečně propojeny. Sparrow funguje jako kompletní rozhraní pro správu, zatímco SeedSigner zůstává jediným zařízením schopným podepisovat vaše transakce. Nyní jste připraveni přijímat a odesílat bitcoiny ve zcela vzduchem chráněné konfiguraci.



## 7. Přijímání a odesílání bitcoinů



Vaše zařízení SeedSigner a Sparrow Wallet jsou nyní nakonfigurovány ke spolupráci. V této závěrečné části se podíváme na to, jak pomocí této konfigurace přijímat a odesílat bitcoiny.



### 7.1 Přijímání bitcoinů



#### 7.1.1 Generování adresy příjmu



V počítači otevřete Sparrow Wallet a odemkněte SeedSigner wallet pomocí hesla. Ujistěte se, že je software připojen k serveru (výřez vpravo dole). V postranním panelu klikněte na `Příjem`.



![Image](assets/fr/056.webp)



Zobrazí se nová adresa Bitcoin. Zobrazí se :




- Textová adresa (začíná `bc1p...`, pokud používáte P2TR jako já),
- Odpovídající QR kód,
- Pole `Label` pro sledování transakcí.



Důrazně doporučuji, abyste na každou účtenku za bitcoiny na wallet přidali štítek. To vám umožní snadno identifikovat původ každého UTXO a zlepší správu vašeho soukromí. Chcete-li do tohoto důležitého tématu proniknout hlouběji, můžete se podívat na specializované školení na stránkách Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Chcete-li přidat štítek, jednoduše zadejte název do pole `Štítek` a potvrďte.



Například:



```txt
Label : Sale of the Raspberry Pi Zero
```



Vaše adresa je nyní přiřazena k tomuto štítku ve všech sekcích Sparrow.



![Image](assets/fr/057.webp)



#### 7.1.2 Ověření Address v SeedSigneru



Před sdílením přijímací adresy je velmi důležité zkontrolovat, zda patří vaší společnosti seed. Tento krok zajistí, že váš SeedSigner bude moci podepisovat transakce spojené s touto adresou. Chrání také před možnými útoky, při nichž by Sparrow zobrazil podvodnou adresu. Nezapomeňte, že Sparrow běží v nezabezpečeném prostředí (váš počítač), které má mnohem větší plochu pro útoky než váš SeedSigner, který je zcela izolovaný. Proto byste nikdy neměli slepě věřit přijímacím adresám prezentovaným v systému Sparrow, dokud si je neověříte pomocí hardwaru wallet.



Na obrazovce Sparrow klikněte na QR kód adresy a zvětšete jej: poté se zobrazí na celou obrazovku.



![Image](assets/fr/058.webp)



V aplikaci SeedSigner vyberte v hlavní nabídce možnost `Scan`. Naskenujte QR kód zobrazený na obrazovce počítače a poté vyberte seed odpovídající vašemu wallet (v mém případě otisk `d4149b27`).



![Image](assets/fr/059.webp)



Pokud se naskenovaná adresa shoduje s adresou odvozenou z vašeho seed, zobrazí se na obrazovce SeedSigner zpráva: `Address ověřeno`.



![Image](assets/fr/060.webp)



Tím se potvrdí, že adresa patří vašemu účtu wallet a že z ní můžete bez obav přijímat bitcoiny.



#### 7.1.3 Příjem finančních prostředků



Tuto adresu (ve formě textu nebo QR kódu) můžete nyní sdělit osobě nebo oddělení, které vám má poslat satss. Jakmile bude transakce odvysílána v síti, objeví se na kartě `Transakce` v aplikaci Sparrow Wallet.



![Image](assets/fr/061.webp)



### 7.2 Odeslání bitcoinů



Odesílání bitcoinů pomocí SeedSigneru probíhá ve třech krocích:




- Vytváření transakcí v systému Sparrow ;
- Podpis transakce na SeedSigner ;
- Konečná distribuce transakce prostřednictvím Sparrow.



Veškeré výměny mezi oběma zařízeními probíhají výhradně pomocí kódů QR.



#### 7.2.1 Vytvoření transakce v Sparrow



V aplikaci Sparrow Wallet můžete kliknout na kartu `Odeslat` v levém postranním panelu. Já však raději používám záložku `UTXOs`, která vám umožní procvičit si "*Coin Control*". Tato metoda vám dává přesnou kontrolu nad použitými UTXO, takže můžete kontrolovat informace, které během transakce odhalíte.



Na kartě `UTXOs` vyberte mince, které chcete utratit, a klikněte na `Odeslat vybrané`.



![Image](assets/fr/062.webp)



Poté vyplňte pole transakce:




- Do pole `Platba příjemci` vložte adresu příjemce nebo klikněte na ikonu fotoaparátu a naskenujte QR kód;
- V poli `Label` přidejte štítek pro sledování tohoto výdaje;
- Do pole `Částka` zadejte částku, která má být odeslána;
- Nakonec zvolte sazbu poplatku podle aktuálních podmínek na trhu (odhady jsou k dispozici na adrese [mempool.space](https://mempool.space/)).



Po vyplnění polí pečlivě zkontrolujte údaje a klikněte na `Vytvořit transakci >>`.



![Image](assets/fr/063.webp)



Zkontrolujte podrobnosti transakce, zda je vše v pořádku, a poté klikněte na `Finalizovat transakci pro podpis`.



![Image](assets/fr/064.webp)



Transakce je nyní připravena, ale ještě není podepsána. Chcete-li zobrazit [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) jako kód QR, klikněte na `Show QR`.



![Image](assets/fr/065.webp)



#### 7.2.2 Podepsání transakce pomocí SeedSignera



Zapněte SeedSigner a naskenujte SeedQR pro přístup k portfoliu jako obvykle. Na domovské obrazovce vyberte možnost `Scan` a poté naskenujte QR kód zobrazený na Sparrow.



![Image](assets/fr/066.webp)



Pak si vyberte model seed, který bude odpovídat vašemu portfoliu.



![Image](assets/fr/067.webp)



SeedSigner automaticky zjistí, že se jedná o PSBT, a zobrazí shrnutí transakce:




   - Odeslaná částka,
   - Výstupní adresy,
   - Související transakční náklady.



Klikněte na `Review Details` a pečlivě zkontrolujte všechny informace přímo na obrazovce SeedSigner. Nejdůležitější položky, které je třeba zkontrolovat, jsou odeslaná částka, adresa příjemce a výše uplatněných poplatků.



![Image](assets/fr/068.webp)



Pokud je vše v pořádku, vyberte možnost `Schválit PSBT` a podepište transakci pomocí příslušného soukromého klíče (klíčů).



![Image](assets/fr/069.webp)



Po podepsání SeedSigner vygeneruje nový QR kód obsahující podepsanou transakci, který je připraven ke skenování pomocí Sparrow.



![Image](assets/fr/070.webp)



#### 7.2.3 Vysílání transakce z Sparrow



Nyní, když je transakce platná, je třeba ji odvysílat v síti Bitcoin, aby se dostala k těžaři, který ji přidá do bloku.



Na obrazovce Sparrow klikněte na položku `QR Scan`.



![Image](assets/fr/071.webp)



Předložte kód QR zobrazený vaším SeedSignerem (kód podepsané transakce) webové kameře. Sparrow dekóduje podpis a zobrazí úplné údaje o transakci. Proveďte závěrečnou kontrolu, zda jsou všechny informace správné, a poté kliknutím na tlačítko Broadcast Transaction (Vysílat transakci) ji odvysílejte v síti Bitcoin.



![Image](assets/fr/072.webp)



Vaše transakce byla odeslána do sítě Bitcoin. Její průběh můžete sledovat na kartě `Transakce` v systému Sparrow Wallet.



![Image](assets/fr/073.webp)



Nyní jste zvládli základy používání SeedSigneru. Chcete-li prohloubit své znalosti a prozkoumat pokročilejší použití, zvu vás k nahlédnutí do následujícího tutoriálu:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

**[Vývoj open-source projektu SeedSigner můžete podpořit také příspěvkem v bitcoinech!](https://seedsigner.com/donate/)**



*Kredit: některé obrázky v tomto návodu pocházejí z [oficiálních webových stránek projektu SeedSigner](https://seedsigner.com/) a [repozitáře GitHub](https://github.com/SeedSigner/seedsigner).*