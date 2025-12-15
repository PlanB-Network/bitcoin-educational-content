---
name: Satochip x SeedSigner
description: Jak používat Satochip se SeedSignerem?
---

![cover](assets/cover.webp)



*Děkujeme [Crypto Guide](https://www.youtube.com/@CryptoGuide/) za fork firmwaru SeedSigner pro podporu čipových karet, který budeme používat v tomto návodu



---

Satochip je hardware formátu čipové karty wallet s bezpečnostním prvkem certifikovaným podle EAL6+, což je jeden z nejvyšších bezpečnostních standardů. Je navržen a vyráběn stejnojmennou belgickou společností Satochip.



Satochip za cenu kolem 25 eur vyniká mezi konkurencí vynikajícím poměrem ceny a výkonu. Díky zabezpečenému čipu nabízí odolnost proti fyzickým útokům. Jeho zdrojový kód appletu je navíc zcela otevřený a licencovaný pod *AGPLv3*.



Na druhou stranu jeho formát přináší určitá funkční omezení. Hlavní nevýhodou Satochipu je absence integrované obrazovky: uživatelé proto musí podepisovat transakce naslepo a spoléhat se pouze na displej svého počítače.



K překonání této slabiny je obzvláště zajímavá konfigurace ve spojení s nástrojem SeedSigner. V této konfiguraci již neprobíhá komunikace přímo mezi počítačem a Satochipem, ale prostřednictvím výměny QR kódů mezi počítačem a SeedSignerem. SeedSigner pak funguje jako důvěryhodná obrazovka: zobrazuje informace, které mají být podepsány, zatímco samotný podpis provádí Satochip. Na rozdíl od běžného použití SeedSigneru (nebo dokonce použití v kombinaci s nástrojem Seedkeeper) se seed nikdy nenačítá do SeedSigneru. SeedSigner se tak stává obrazovkou Satochipu, čímž se eliminují rizika spojená s podepisováním naslepo.



Pokud se na problém podíváme z druhé strany, pak použití SeedSigneru se Satochipem vyplňuje hlavní mezeru v SeedSigneru: možnost ukládat a používat seed v rámci secure element.



Podle mého názoru má tato konfigurace oproti běžným hardwarovým peněženkám několik výhod:




- Satochip stojí přibližně 25 eur, a protože jde o open-source applet, můžete si jej sami nainstalovat na prázdnou čipovou kartu. K tomu je třeba připočítat náklady na komponenty SeedSigner a rozšíření pro čtení čipových karet: podle toho, kde tento hardware koupíte, by se celková částka měla pohybovat mezi 70 a 100 EUR.
- Veškerý software zapojený do nastavení je open-source: firmware SeedSigner a applet Satochip.
- Využíváte výhod certifikovaného bezpečnostního prvku.
- Konfigurace může být provedena zcela svépomocí, bez použití hardwaru výslovně určeného pro použití Bitcoin, což může poskytnout určitou formu věrohodného popření a odolnosti vůči určitým vnějším hrozbám (včetně, v závislosti na zemi, státního tlaku). Jedná se také o zajímavé řešení, pokud je ve vašem regionu omezen nebo znemožněn přístup ke komerčním hardwarovým peněženkám.




## 1. Požadované materiály



K provedení tohoto nastavení budete potřebovat následující položky:




- Obvyklé vybavení, které potřebuje klasický SeedSigner :
 - raspberry Pi Zero s GPIO piny,
 - 1.3" obrazovka Waveshare,
 - kompatibilní fotoaparát,
 - kartu microSD.



![Image](assets/fr/01.webp)





- Sada rozšíření SeedSigner, která je k dispozici [v oficiálním obchodě Satochip](https://satochip.io/product/seedsigner-extension-kit/) a která umožňuje číst a zapisovat na čipovou kartu přímo z vašeho SeedSigneru. Další možností je použít [externí čtečku čipových karet](https://satochip.io/product/chip-card-reader/), kterou lze připojit kabelem k portu Micro-USB na počítači Raspberry Pi. Toto řešení jsem však sám netestoval;
- [Satochip](https://satochip.io/product/satochip/), případně [prázdnou čipovou kartu](https://satochip.io/product/card-for-diy-project/), na kterou lze nainstalovat applet Satochip (sada rozšíření prodávaná společností Satochip již obsahuje prázdnou čipovou kartu). Sada rozšíření Satochip podporuje také formát [SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/). Pokud tedy dáváte přednost tomuto formátu, můžete se pro něj rozhodnout.



![Image](assets/fr/02.webp)



Další podrobnosti o vybavení potřebném k sestavení SeedSigneru najdete v 1. části tohoto dalšího návodu:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Instalace firmwaru



Chcete-li používat SeedSigner s čipem Satochip, musíte nainstalovat alternativní firmware, který se liší od originálního SeedSigneru, aby podporoval čtení čipových karet. Za tímto účelem [doporučuji použít fork z "**3rdIteration**"](https://github.com/3rdIteration/seedsigner). Stáhněte si [nejnovější verzi obrazu](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) odpovídající modelu Raspberry Pi, který používáte.



![Image](assets/fr/03.webp)



Pokud jej ještě nemáte, stáhněte si software [Balena Etcher] (https://etcher.balena.io/) a postupujte následovně:




- Vložte kartu microSD do počítače;
- Spuštění nástroje Etcher ;
- Vyberte soubor `.zip`, který jste právě stáhli;
- Jako cíl vyberte kartu microSD;
- Klikněte na `Flash!`.



![Image](assets/fr/04.webp)



Počkejte na dokončení procesu: vaše microSD je nyní připravena k použití. Nyní můžete přejít k sestavení zařízení.



Podrobnější informace o instalaci firmwaru a ověření softwaru (což je krok, který důrazně doporučuji provést) naleznete v následujícím návodu:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Montáž čtečky čipových karet



Začněte instalací kamery na Raspberry Pi Zero, opatrně ji zasuňte do kolíku kamery a zajistěte ji černým výstupkem. Poté umístěte počítač Pi na dno pouzdra a dbejte na to, abyste zarovnali porty s příslušnými otvory.



![Image](assets/fr/05.webp)



Poté připojte čtečku čipových karet ke GPIO pinům Raspberry Pi Zero.



![Image](assets/fr/06.webp)



Posuňte plastový kryt na čtečku čipových karet, dokud není správně umístěn.



![Image](assets/fr/07.webp)



Poté přidejte obrazovku na piny GPIO rozšíření.



![Image](assets/fr/08.webp)



Nakonec vložte kartu microSD s firmwarem do bočního portu počítače Raspberry Pi Zero.



![Image](assets/fr/09.webp)



Nyní můžete SeedSigner připojit buď přes port Micro-USB počítače Raspberry Pi Zero, nebo přes port USB-C rozšiřujícího zařízení. Obě možnosti fungují. Počkejte několik sekund na spuštění a poté by se měla zobrazit uvítací obrazovka.



![Image](assets/fr/10.webp)



Další podrobnosti o počátečním nastavení SeedSigneru najdete ve 4. části následujícího návodu:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Flashování čipové karty pomocí appletu Satochip (volitelné)



Pokud již vlastníte Satochip, můžete tento krok přeskočit a přejít rovnou ke kroku 4. V této části se podíváme na to, jak nainstalovat applet Satochip na prázdnou čipovou kartu (metoda DIY). Applet je jednoduše malý program spuštěný na kartě Smartcard, který nám umožňuje spravovat specifické funkce.



Chcete-li začít, otevřete v aplikaci SeedSigner nabídku `Nástroje > Nástroje čipové karty`.



![Image](assets/fr/11.webp)



Poté vyberte `DIY Tools > Install Applet`.



![Image](assets/fr/12.webp)



Vložte čipovou kartu do čtečky SeedSigner čipem dolů a vyberte applet `Satochip`.



![Image](assets/fr/13.webp)



Během instalace buďte trpěliví: proces může trvat několik desítek sekund.



![Image](assets/fr/14.webp)



Po úspěšné instalaci appletu můžete přejít ke kroku 4.



![Image](assets/fr/15.webp)




## 5. Vytvoření a uložení seed



### 5.1. Generování seed



Nyní, když máte všechen hardware a software správně zprovozněn, můžete přistoupit k vytvoření portfolia Bitcoin. Za tímto účelem připojte svůj SeedSigner a poté generate seed jako u běžného SeedSigneru, a to buď hodem kostkou, nebo pořízením fotografie:




- Přejděte do nabídky `Nástroje > Kamera / Hody kostkou`;
- Poté následuje proces generování entropie podle zvolené metody;
- Nakonec vytvořte zálohu systému seed na fyzické médium a zálohu pečlivě zkontrolujte.



![Image](assets/fr/16.webp)



Chcete-li se seznámit s podrobnostmi tohoto postupu, přečtěte si část 5 tohoto návodu:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. Uložení seed do programu Seedkeeper



Po vygenerování kódu seed se tento kód nachází v paměti RAM SeedSigneru pouze jednou. V mém případě jej chci uložit na [Seedkeeper](https://satochip.io/product/seedkeeper/), další produkt společnosti Satochip určený k ukládání tajemství. Toto zařízení budu používat jako poslední možnost v případě ztráty svého Satochipu.



Zvolená strategie zálohování závisí na vašich preferencích, ale je nutné mít alespoň jednu kopii mnemotechnické fráze, a to buď na fyzickém médiu (papírovém nebo kovovém), nebo, jako zde, v Seedkeeperu. Počet záloh můžete také podle potřeby znásobit. Pro více informací o strategiích zálohování portfolia doporučuji přečíst si tento návod :



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Chcete-li zálohovat svůj program seed v nástroji Seedkeeper, přejděte přímo do nabídky `Zálohování semen`.



![Image](assets/fr/17.webp)



Poté vložte zařízení Seedkeeper do čtečky čipových karet a vyberte možnost `To SeedKeeper`.



![Image](assets/fr/18.webp)



Zadejte kód PIN a odemkněte jej.



![Image](assets/fr/19.webp)



Zvolte si `Značku` pro snadnou identifikaci různých tajemství uložených ve službě Seedkeeper. Můžete například jednoduše zachovat otisk wallet nebo výslovně uvést `Seed`. Volba závisí na vašich preferencích a riziku.



![Image](assets/fr/20.webp)



Pokud se vaše strategie zálohování spoléhá pouze na tento nástroj Seedkeeper, důrazně doporučuji, abyste nyní provedli prázdný test obnovení a poté porovnali otisky prstů a zkontrolovali, zda zálohování funguje.



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Kód PIN Seedkeeper by měl být co nejdelší a náhodný, aby se zabránilo pokusům o hrubou sílu v případě fyzického zneužití karty. Měli byste si také ponechat záložní kopii tohoto kódu PIN, uloženou na jiném místě než v aplikaci Seedkeeper. Bez tohoto kódu PIN nebudete mít přístup k mnemotechnice uložené ve službě Seedkeeper a vaše bitcoiny budou trvale ztraceny.



### 5.3. Uložit seed na Satochip



Po vygenerování, uložení a ověření vašeho portfolia jej přeneseme do systému Satochip. Za tímto účelem se ujistěte, že je v paměti RAM SeedSigneru načten soubor seed. Poté přejděte do `Nástroje > Nástroje čipové karty > Funkce Satochip`.



![Image](assets/fr/21.webp)



Vložte čip Satochip do čtečky čipových karet a zvolte možnost `Inicializovat pomocí Seed`.



![Image](assets/fr/22.webp)



Přístroj vás vyzve k zadání kódu Satochip PIN; jelikož je karta nová a neinicializovaná, žádný kód PIN ještě neexistuje. Zadáním libovolného kódu tento krok přeskočíte (nejedná se o blokování).



![Image](assets/fr/23.webp)



SeedSigner zjistí, že váš Satochip nebyl inicializován. Klikněte na `Rozumím` pro potvrzení.



![Image](assets/fr/24.webp)



Poté můžete nastavit kód Satochip PIN, který může mít 4 až 16 znaků. Chcete-li posílit zabezpečení zařízení wallet, zvolte dlouhý, náhodný kód: je to jediná ochrana proti fyzickému přístupu k vaší mnemotechnické frázi.



Nezapomeňte si tento kód PIN uložit ihned po jeho vytvoření, a to buď do zabezpečeného správce hesel, nebo na fyzické médium, v závislosti na vaší osobní strategii. V druhém případě dbejte na to, abyste médium obsahující kód PIN nikdy neukládali na stejné místo jako čip Satochip, jinak se ochrana stane zbytečnou. Je důležité mít záložní kopii: **Bez tohoto kódu PIN nebudete mít přístup ke svému seed a vaše bitcoiny budou navždy ztraceny**.



![Image](assets/fr/25.webp)



Poté se vás SeedSigner zeptá, který seed má importovat do Satochipu. Vyberte ten, jehož otisk prstu odpovídá právě vytvořenému portfoliu.



![Image](assets/fr/26.webp)



Váš seed je nyní importován do systému Satochip.



![Image](assets/fr/27.webp)



Nyní můžete SeedSigner vypnout.



Pokud chcete použít BIP39 passphrase pro zvýšení bezpečnosti wallet, přečtěte si část 6 tohoto návodu:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. Import wallet do Sparrow



Nyní, když je vaše portfolio zprovozněno, naimportujeme jeho veřejné informace ("*skladiště*") do softwaru Sparrow Wallet nebo jiného softwaru pro správu portfolia. Tento software bude sloužit k vytváření, distribuci a sledování vašich transakcí. Nebude je však moci podepisovat, protože soukromé klíče potřebné pro tuto operaci má pouze Satochip (a případné zálohy).



### 6.1 Příprava SeedSigneru a Satochipu



Vložte kartu microSD s operačním systémem a zapněte SeedSigner. V tuto chvíli nemůže nic dělat, protože ještě nezná váš seed. Musíte začít tím, že vložíte Satochip do čtečky čipových karet, protože právě v ní je váš seed.



Na domovské obrazovce přejděte do nabídky `Nástroje > Nástroje čipové karty > Funkce satochipu`.



![Image](assets/fr/28.webp)



Poté klikněte na `Exportovat Xpub`.



![Image](assets/fr/29.webp)



Vyberte typ portfolia. V našem případě se jedná o jedno portfolio: vyberte `Jednoznačné`.



![Image](assets/fr/30.webp)



Dále je třeba zvolit standard skriptování. Zvolte nejnovější: `Nativní SegWit`.



![Image](assets/fr/31.webp)



Nakonec vyberte `Koordinátor`, tj. software pro správu portfolia, který chcete používat. Zde budeme používat Sparrow Wallet.



![Image](assets/fr/32.webp)



Zobrazí se varovná zpráva: To je zcela normální. Rozšířený veřejný klíč (`xpub`) umožňuje zobrazit všechny adresy odvozené z vašeho seed (na prvním účtu). Neumožňuje však přístup k vašim finančním prostředkům: jeho zveřejnění by ohrozilo vaše soukromí, ale ne bezpečnost vašich bitcoinů. Jinými slovy, umožňuje vám sledovat vaše zůstatky, ale ne je utrácet.



Klikněte na `Rozumím`.



![Image](assets/fr/33.webp)



Poté zadejte kód PIN zařízení Satochip a odemkněte jej. Jedná se o kód, který jste definovali a uložili v kroku 5.



![Image](assets/fr/34.webp)



Pokud jste se zobrazenými informacemi spokojeni, klikněte na `Exportovat Xpub`.



![Image](assets/fr/35.webp)



SeedSigner pak vygeneruje váš xpub ve formě dynamického QR kódu, který obsahuje všechny údaje potřebné ke správě vašeho portfolia v Sparrow Wallet. Pomocí joysticku můžete nastavit jas obrazovky, abyste si usnadnili skenování QR kódu.



### 6.2 Import nového portfolia do Sparrow Wallet



Zkontrolujte, zda je v počítači nainstalován software Sparrow Wallet. Pokud nevíte, jak jej stáhnout, zkontrolovat jeho pravost a správně nainstalovat, podívejte se na náš úplný návod na toto téma :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

V počítači otevřete program Sparrow Wallet a v nabídce klikněte na `Soubor → Importovat Wallet`.



![Image](assets/fr/36.webp)



Přejděte dolů na položku `SeedSigner` a vyberte možnost `Scan...`. Aktivuje se vaše webová kamera: naskenujte dynamický QR kód zobrazený na obrazovce SeedSigner.



![Image](assets/fr/37.webp)



Přiřaďte svému portfoliu název a klikněte na tlačítko `Vytvořit Wallet`. Poté vás Sparrow vyzve k nastavení hesla pro uzamčení místního přístupu k tomuto wallet. Zvolte silné heslo: chrání vaše data v Sparrow (veřejné klíče, adresy, štítky a historii transakcí). Toto heslo však není nutné pro budoucí obnovení wallet: bude jím pouze vaše mnemotechnická fráze (a případně váš passphrase).



Doporučuji, abyste si toto heslo uložili do správce hesel, abyste ho neztratili.



![Image](assets/fr/38.webp)



Úložiště klíčů bylo úspěšně importováno.



![Image](assets/fr/39.webp)



Nyní zkontrolujte, zda se otisk `Master fingerprint` zobrazený v Sparrow Wallet shoduje s otiskem, který byl dříve nalezen ve vašem SeedSigneru.



Poté vás SeedSigner požádá o naskenování náhodné přijímací adresy z vašeho Sparrow wallet, aby potvrdil platnost importu.



![Image](assets/fr/40.webp)



Váš Satochip (prostřednictvím SeedSigner) a Sparrow Wallet jsou nyní bezpečně propojeny. Sparrow funguje jako kompletní rozhraní pro správu, zatímco Satochip zůstává jediným zařízením schopným podepisovat vaše transakce. Nyní jste připraveni přijímat a odesílat bitcoiny ve zcela vzduchem chráněné konfiguraci.



![Image](assets/fr/41.webp)



## 7. Přijímání a odesílání bitcoinů



Vaše zařízení Satochip a Sparrow Wallet jsou nyní nakonfigurovány ke spolupráci. V této části vám krok za krokem vysvětlíme, jak v tomto režimu přijímat a odesílat bitcoiny.



### 7.1 Přijímání bitcoinů



#### 7.1.1 Generování adresy příjmu



V počítači otevřete Sparrow Wallet a pomocí hesla odemkněte svůj `Satochip-SeedSigner` wallet. Zkontrolujte, zda je software připojen k serveru (indikátor vpravo dole). Poté v postranním panelu klikněte na `Příjem`.



![Image](assets/fr/42.webp)



Zobrazí se nová adresa Bitcoin. Najdete zde :




- Adresa v textovém formátu (začínající `bc1q...`, pokud používáte P2WPKH, jako v tomto příkladu) ;
- Související QR kód ;
- Pole `Label`, které je užitečné pro sledování transakcí.



Důrazně doporučuji přidat štítek ke každé účtence bitcoinů v wallet. To vám pomůže snadno identifikovat původ každého UTXO a lépe spravovat své soukromí. Chcete-li se o tomto důležitém tématu dozvědět více, podívejte se na specializované školení na stránkách Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Chcete-li přidat štítek, jednoduše zadejte název do pole `Štítek` a potvrďte.



Například:



```txt
Label : Sale of the Raspberry Pi Zero
```



Vaše adresa je nyní přiřazena k tomuto štítku ve všech sekcích Sparrow.



![Image](assets/fr/43.webp)



#### 7.1.2 Ověření Address na zařízení SeedSigner



Před sdělením přijímací adresy plátci je důležité zkontrolovat, zda patří vaší společnosti seed. Tento krok zajistí, že váš Satochip pak bude moci podepisovat transakce spojené s touto adresou. Zabraňuje také případným útokům, kdy by Sparrow zobrazoval podvodnou adresu. Mějte na paměti, že Sparrow běží v nezabezpečeném prostředí (váš počítač), jehož útočný povrch je mnohem větší než u vašeho Satochipu, který je zcela izolovaný. Proto byste nikdy neměli slepě důvěřovat adresám zobrazeným v systému Sparrow dříve, než si je ověříte na hardwaru wallet.



V aplikaci Sparrow klikněte na QR kód adresy a zvětšete jej: zobrazí se na celou obrazovku.



![Image](assets/fr/44.webp)



V aplikaci SeedSigner vložte Satochip do čtečky a v hlavní nabídce vyberte možnost `Scan`. Naskenujte QR kód zobrazený na počítači a poté vyberte možnost `Použít kartu Satochip`.



![Image](assets/fr/45.webp)



Poté potvrďte typ použitého skriptu (v tomto případě `Native SegWit`), zadejte kód PIN Satochip pro jeho odemčení a potvrďte informace `xpub`.



![Image](assets/fr/46.webp)



Pokud se naskenovaná adresa shoduje s adresou odvozenou z vašeho seed, zobrazí SeedSigner zprávu: gW-67 ověřeno".



![Image](assets/fr/47.webp)



Můžete si tak být jisti, že adresa patří do vašeho portfolia.



#### 7.1.3 Příjem finančních prostředků



Tuto adresu můžete nyní předat v textové podobě nebo prostřednictvím kódu QR osobě nebo oddělení, které vám má zaslat satss. Jakmile bude transakce odvysílána v síti, objeví se na kartě `Transakce` v aplikaci Sparrow Wallet.



![Image](assets/fr/48.webp)



### 7.2 Odeslání bitcoinů



Odesílání bitcoinů pomocí konfigurace Satochip-SeedSigner zahrnuje 3 kroky:




- Vytváření transakcí v systému Sparrow ;
- Podepsání této transakce na Satochipu prostřednictvím SeedSigner ;
- Nakonec je transakce vysílána po síti ze serveru Sparrow.



Veškeré výměny mezi oběma zařízeními probíhají výhradně prostřednictvím kódů QR.



#### 7.2.1 Vytvoření transakce v systému Sparrow



V aplikaci Sparrow Wallet můžete vytvořit transakci kliknutím na kartu `Odeslat` v levém postranním panelu. Já však raději používám záložku `UTXOs`, která vám umožní procvičit si *Ovládání Coin*. Tato metoda nabízí přesnou kontrolu nad vynaloženými UTXO, abyste omezili informace odhalené během vašich transakcí.



Na kartě `UTXOs` vyberte mince, které chcete utratit, a klikněte na `Odeslat vybrané`.



![Image](assets/fr/49.webp)



Poté vyplňte pole transakce:




- Do pole `Platba příjemci` vložte adresu příjemce nebo naskenujte jeho QR kód pomocí ikony fotoaparátu;
- V poli `Label` přidejte štítek pro sledování tohoto výdaje;
- Do pole `Částka` zadejte částku, která má být odeslána;
- Nakonec zvolte rychlost nabíjení podle aktuálních podmínek sítě (odhady jsou k dispozici na adrese [mempool.space](https://mempool.space/)).



Po vyplnění všech polí pečlivě zkontrolujte informace a klikněte na `Vytvořit transakci >>`.



![Image](assets/fr/50.webp)



Naposledy zkontrolujte správnost údajů o transakci a klikněte na `Finalizovat transakci k podpisu`.



![Image](assets/fr/51.webp)



Transakce je nyní připravena, ale ještě nebyla podepsána. Chcete-li zobrazit [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) jako QR kód, klikněte na `Show QR`.



![Image](assets/fr/52.webp)



#### 7.2.2 Podpis transakce se společností Satochip



Zapněte svůj SeedSigner a vložte svůj Satochip jako obvykle. Na domovské obrazovce vyberte možnost `Scan` a naskenujte QR kód zobrazený na Sparrow.



![Image](assets/fr/53.webp)



Vyberte možnost `Použít kartu Satochip`.



![Image](assets/fr/54.webp)



Zadejte kód PIN a odemkněte čipovou kartu.



![Image](assets/fr/55.webp)



SeedSigner zjistí, že se jedná o PSBT, a zobrazí souhrn transakce:




   - Odeslaná částka,
   - Cílové adresy,
   - Související transakční náklady.



Klikněte na `Review Details` a zkontrolujte všechny informace přímo na obrazovce SeedSigner. Nejdůležitějšími body, které je třeba zkontrolovat, jsou odeslané částky, cílové adresy a transakční poplatky.



![Image](assets/fr/56.webp)



Pokud je vše v pořádku, vyberte možnost `Schválit PSBT` a podepište transakci pomocí Satochipu.



![Image](assets/fr/57.webp)



Jakmile je podpis dokončen, SeedSigner vygeneruje nový QR kód obsahující podepsanou transakci, který je připraven ke skenování pomocí Sparrow.



#### 7.2.3 Vysílání transakce z Sparrow



Nyní, když je transakce podepsána a ověřena, zbývá ji jen odvysílat v síti Bitcoin, aby ji těžař mohl zahrnout do bloku. V síti Sparrow klikněte na `Scan QR`.



![Image](assets/fr/58.webp)



Předložte kód QR zobrazený na vašem SeedSigneru (ten, který obsahuje podepsanou transakci) webové kameře. Sparrow poté zobrazí všechny podrobnosti o transakci. Zkontrolujte, zda jsou všechny informace správné, a poté kliknutím na "Broadcast Transaction" (Vysílat transakci) ji odvysílejte v síti Bitcoin.



![Image](assets/fr/59.webp)



Vaše transakce je nyní přenesena do sítě. Její potvrzení můžete sledovat na kartě `Transakce` v Sparrow Wallet.



![Image](assets/fr/60.webp)



## 8. Získejte zpět svůj wallet



Jak jsme viděli v předchozích částech, v závislosti na vaší bezpečnostní strategii existuje několik způsobů zálohování vaší fráze pro obnovení kromě vašeho Satochipu :




- Použití klasického *SeedQR* se SeedSignerem ;
- Zaznamenáním mnemotechnické fráze na fyzické médium;
- Nebo uložením na server Seedkeeper, jak je vysvětleno v části 5.2.



V každém případě existují 2 hlavní situace, ve kterých je třeba zasáhnout: ztráta Satochipu nebo ztráta SeedSigneru. Podívejme se, jak reagovat v každém z těchto scénářů.



### 8.1. Získejte svůj wallet pomocí Satochipu



Pokud máte stále svůj Satochip, ale váš SeedSigner je rozbitý nebo ztracený, je situace poměrně jednoduchá, protože váš wallet je stále v Satochipu.



Nejlepší možností je doporučit potřebné komponenty a sestavit nový SeedSigner od začátku. Protože se jedná o "bezstavové" zařízení, nezáleží na tom, zda používáte stejný nebo jiný SeedSigner: pokud můžete vložit svůj Satochip, bude vše fungovat normálně.



Pokud nechcete žádný přestavovat, můžete svůj Satochip používat i klasickým způsobem, tj. přímo z počítače, bez nutnosti procházet SeedSignerem. Tento způsob funguje bezvadně, ale výrazně snižuje bezpečnost vašeho Bitcoin wallet: ztrácíte izolaci "*vzduchového uzávěru*" a musíte nyní podepisovat naslepo, protože SeedSigner fungoval jako důvěryhodná obrazovka. Může se však jednat o dočasné řešení v případě nouze, nebo pokud nemůžete obnovit SeedSigner.



K tomu budete potřebovat čtečku čipových karet USB nebo NFC. V programu Sparrow otevřete kartu wallet, kterou chcete obnovit, přejděte na kartu `Nastavení` a klepněte na tlačítko `Nahradit`.



![Image](assets/fr/61.webp)



Vložte čip Satochip do čtečky čipových karet připojené k počítači a klikněte na `Importovat` vedle položky `Satochip`.



![Image](assets/fr/62.webp)



Nakonec zadejte PIN čipové karty a odemkněte ji. Poté budete moci přistupovat ke své wallet, vytvářet transakce a podepisovat je přímo pomocí připojeného Satochipu.



### 8.2. Získejte své portfolio pomocí SeedSigner



Druhý, choulostivější scénář nastane, když ztratíte přístup ke svému čipu Satochip obsahujícímu zařízení seed: ať už je rozbitý, ztracený, ukradený, nebo jste zapomněli jeho kód PIN. Pokud byl váš Satochip odcizen nebo ztracen, důrazně doporučujeme, abyste po obnovení přístupu k vašim prostředkům okamžitě převedli své bitcoiny na zcela nový wallet, vygenerovaný s jiným seed. Tím zajistíte, že potenciální útočník nikdy nezíská přístup k vašim satschipům.



Chcete-li znovu získat přístup ke svému portfoliu a přesunout své prostředky, jednoduše vložte svůj účet seed do SeedSigner. V závislosti na použitém záložním médiu máte několik možností:





- Zadejte mnemotechnickou frázi ručně v nabídce `Seeds > Enter 12-word seed`.



![Image](assets/fr/63.webp)





- Kliknutím na tlačítko `Scan` na domovské stránce naskenujte svůj *SeedQR*.



![Image](assets/fr/64.webp)





- Nebo načtěte seed z programu Seedkeeper prostřednictvím nabídky `Seeds > From SeedKeeper` (tuto metodu používám v tomto návodu). Stačí zadat PIN kód Seedkeeperu a vybrat tajenku, která se má použít jako seed v SeedSigneru.



![Image](assets/fr/65.webp)



Po nahrání seed do SeedSigneru, ať už použijete jakoukoli metodu, budete moci podepsat jednu nebo více skenovacích transakcí a přesunout své bitcoiny na nový, nekomprimovaný wallet. Jak to provést, se dozvíte v části 7.2 následujícího návodu:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Nyní víte, jak používat Satochip k bezpečné správě portfolia Bitcoin v kombinaci se SeedSigner.



Pokud vás toto nastavení přesvědčilo, neváhejte podpořit projekty, které to umožňují:




- Zakoupením zařízení přímo [na webových stránkách Satochip](https://satochip.io/shop/);
- Přispěním [na projekt SeedSigner](https://seedsigner.com/donate/);
- Přihlášením se k odběru kanálu YouTube [Crypto Guide](https://www.youtube.com/@CryptoGuide/), který provozuje osoba spravující repozitář GitHub, na němž je umístěn upravený firmware, který jsme použili v tomto návodu.