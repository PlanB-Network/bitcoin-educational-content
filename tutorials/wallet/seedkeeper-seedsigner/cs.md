---
name: Seedkeeper x SeedSigner
description: Jak mohu Seedkeeper používat se svým SeedSignerem?
---

![cover](assets/cover.webp)



*Děkujeme týmu [Satochip](https://satochip.io/) za souhlas s opětovným použitím [jejich videí](https://www.youtube.com/@satochip/videos) v tomto návodu. Děkujeme také [CryptoGuide](https://www.youtube.com/@CryptoGuide/) za jeho fork firmwaru SeedSigner, který umožňuje podporu čipových karet



---

SeedSigner je hardware wallet, který si sami sestavíte ze standardního hardwaru, obvykle z Raspberry Pi Zero. Tento wallet se nazývá "*stateless*": na rozdíl od většiny ostatních modelů na trhu (Coldcard, Trezor, Ledger atd.) neukládá žádná data do trvalé paměti a pracuje pouze živě z paměti RAM. Výsledkem je, že vaše portfolio seed není nikdy uloženo v SeedSigneru. Při každém restartu jej musíte vyplnit, aby zařízení mohlo podepisovat vaše transakce. Nejběžnější metodou je uložení seed jako QR kódu, který pak při každém použití naskenujete (*SeedQR*).



Tento přístup však představuje významné riziko: kód seed musí zůstat přístupný v otevřeném textu, aby jej bylo možné skenovat. V případě krádeže nebo vniknutí by se k němu mohl útočník snadno dostat a ukrást vaše bitcoiny.



K překonání této slabiny lze SeedSigner kombinovat s [**Seedkeeper**](https://satochip.io/product/seedkeeper/), čipovou kartou vyvinutou společností Satochip. Ta umožňuje ukládat mnemotechnické fráze (nebo jiná tajemství) na kartu secure element chráněnou kódem PIN. Applet Seedkeeper je open-source a jeho secure element má certifikaci EAL6+. Při použití ve spojení s aplikací SeedSigner nabízí velmi zajímavou bezpečnostní funkci: vaše klíče zůstávají spravovány zcela off-line, transakce podepisujete na důvěryhodné obrazovce a seed je fyzicky chráněn v čipové kartě odolné proti fyzickému útoku.



K dokončení instalace potřebujete pouze následující položky:




- Obvyklé vybavení potřebné pro klasický SeedSigner: Raspberry Pi Zero, 1,3" obrazovka Waveshare, kompatibilní fotoaparát a karta microSD (více informací najdete v níže uvedeném návodu SeedSigner);
- Sada rozšíření SeedSigner, která je k dispozici [v oficiálním obchodě Satochip](https://satochip.io/product/seedsigner-extension-kit/) a která umožňuje číst a zapisovat na čipovou kartu přímo z vašeho SeedSigneru. Další možností je použití externí čtečky čipových karet, kterou lze připojit kabelem k portu Micro-USB na počítači Raspberry Pi. Toto řešení jsem však sám netestoval;
- Seedkeeper nebo prázdnou čipovou kartu, na kterou lze nainstalovat applet Seedkeeper (sada rozšíření prodávaná společností Satochip již obsahuje prázdnou čipovou kartu).



![Image](assets/fr/01.webp)



Tento výukový program se zabývá dvěma scénáři:




- Pokud již máte portfolio Bitcoin spravované prostřednictvím SeedSigner, stačí nainstalovat nový firmware. Poté můžete nadále používat svůj stávající wallet, tentokrát však s využitím nástroje Seedkeeper pro větší bezpečnost.
- Pokud ještě nemáte s vaším SeedSignerem spojený modul Bitcoin wallet, musíte postupovat podle kroků **5** a **6** níže uvedeného návodu. V těchto částech je vysvětleno, jak vytvořit mnemotechnickou frázi generate se SeedSignerem, uložit ji prostřednictvím *SeedQR* a poté tuto frázi wallet připojit ke Sparrow Wallet a spravovat ji. Nebudu zde tyto postupy rozebírat a **předpokládám, že již máte funkční Bitcoin wallet, nakonfigurovaný s Sparrow a vaším SeedSignerem**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Instalace firmwaru



Chcete-li používat SeedSigner s nástrojem Seedkeeper, musíte nainstalovat alternativní firmware, který se liší od firmwaru původního SeedSigneru, aby podporoval čtení čipových karet. Za tímto účelem [doporučuji použít fork z "*3rdIteration*"](https://github.com/3rdIteration/seedsigner). Stáhněte si [nejnovější verzi obrazu](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) odpovídající modelu Raspberry Pi, který používáte.



![Image](assets/fr/02.webp)



Pokud jej ještě nemáte, stáhněte si software [Balena Etcher](https://etcher.balena.io/) a postupujte následovně:




- Vložte kartu microSD do počítače;
- Spuštění nástroje Etcher ;
- Vyberte soubor `.zip`, který jste právě stáhli;
- Jako cíl vyberte kartu microSD;
- Klikněte na `Flash!`.



![Image](assets/fr/03.webp)



Počkejte na dokončení procesu: vaše microSD je nyní připravena k použití. Nyní můžete přejít k sestavení zařízení.



Podrobnější informace o instalaci firmwaru a ověření softwaru (což je krok, který důrazně doporučuji provést) naleznete v následujícím návodu:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Montáž čtečky čipových karet



![video](https://youtu.be/jqE8HDMCImA)



Začněte instalací kamery na Raspberry Pi Zero, opatrně ji zasuňte do kolíku kamery a zajistěte ji černým výstupkem. Poté umístěte počítač Pi na dno pouzdra a dbejte na to, abyste zarovnali porty s příslušnými otvory.



![Image](assets/fr/04.webp)



Poté připojte čtečku čipových karet ke GPIO pinům Raspberry Pi Zero.



![Image](assets/fr/05.webp)



Posuňte plastový kryt na čtečku čipových karet, dokud není správně umístěn.



![Image](assets/fr/06.webp)



Poté přidejte obrazovku na piny GPIO rozšíření.



![Image](assets/fr/07.webp)



Nakonec vložte kartu microSD s firmwarem do bočního portu počítače Raspberry Pi Zero.



![Image](assets/fr/08.webp)



SeedSigner nyní můžete připojit buď přes port Micro-USB počítače Raspberry Pi Zero, nebo přes port USB-C rozšiřujícího zařízení. Obě možnosti fungují. Počkejte několik sekund na spuštění a poté by se měla zobrazit uvítací obrazovka.



![Image](assets/fr/09.webp)



Pro více informací o počátečním nastavení SeedSigneru doporučuji následující návod:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Flashování čipové karty pomocí appletu Seedkeeper (volitelné)



![video](https://youtu.be/NF4HemyEcOY)



Pokud již vlastníte Seedkeeper, můžete tento krok přeskočit a přejít rovnou ke kroku 4. V této části se podíváme na to, jak nainstalovat applet Seedkeeper na prázdnou čipovou kartu (metoda DIY).



Chcete-li začít, otevřete v aplikaci SeedSigner nabídku `Nástroje > Nástroje čipové karty`.



![Image](assets/fr/10.webp)



Poté vyberte `DIY Tools > Install Applet`.



![Image](assets/fr/11.webp)



Vložte čipovou kartu do čtečky SeedSigner čipem dolů a vyberte applet `SeedKeeper`.



![Image](assets/fr/12.webp)



Během instalace buďte trpěliví: proces může trvat několik desítek sekund.



![Image](assets/fr/13.webp)



Po úspěšné instalaci appletu můžete přejít ke kroku 4.



![Image](assets/fr/14.webp)



## 4. Uložení existujícího SeedQR v nástroji Seedkeeper



![video](https://youtu.be/X-vmFHU9Ec8)



Nyní, když je váš Seedkeeper funkční, můžete na čipovou kartu uložit mnemotechnickou pomůcku Bitcoin wallet. Chcete-li začít, zapněte SeedSigner jako obvykle a poté naskenujte *SeedQR* svého wallet, abyste jej nahráli do zařízení. Jakmile je karta seed importována, jednoduše zvolte `Done`.



![Image](assets/fr/15.webp)



Po načtení seed přejděte do nabídky `Záložní osivo`.



![Image](assets/fr/16.webp)



Poté vložte Seedkeeper do jednotky SeedSigner a vyberte možnost `To SeedKeeper`.



![Image](assets/fr/17.webp)



Poté vás SeedSigner požádá o zadání kódu PIN pro váš Seedkeeper. Jelikož se jedná o prázdnou kartu, žádný kód ještě nebyl definován. Zadejte libovolný kód, abyste tento krok přeskočili, a poté jej potvrďte.



![Image](assets/fr/18.webp)



SeedSigner zjistí, že Seedkeeper ještě nebyl inicializován (tj. nebylo nastaveno heslo). Pro pokračování klikněte na `Rozumím`.



![Image](assets/fr/19.webp)



Nyní zvolte nový kód PIN vašeho zařízení Seedkeeper, který může mít 4 až 16 znaků. Pro zvýšení bezpečnosti zvolte dlouhý, náhodný kód: je to jediná překážka chránící fyzický přístup k vaší mnemotechnické frázi.



Nezapomeňte tento kód PIN uložit ihned po jeho vytvoření, a to buď do spolehlivého správce hesel, nebo na samostatné fyzické médium v závislosti na vaší strategii. V druhém případě dbejte na to, abyste nikdy neuchovávali médium obsahující kód PIN na stejném místě jako nástroj Seedkeeper, jinak se ochrana stane neúčinnou. Je důležité mít záložní kopii: **Bez tohoto PINu nebudete mít přístup ke svému seed a vaše bitcoiny budou ztraceny**.



![Image](assets/fr/20.webp)



Poté můžete definovat `Značku` spojenou s vaší mnemotechnickou frází. Tento štítek je užitečný, pokud v Seedkeeperu ukládáte několik tajemství, abyste je mohli snadno identifikovat.



![Image](assets/fr/21.webp)



Vaše mnemotechnická fráze je nyní uložena na čipové kartě.



![Image](assets/fr/22.webp)



Pokud jde o strategii zabezpečení, je možné zvolit několik přístupů v závislosti na vašich potřebách a míře vystavení riziku. Osobně doporučuji uchovávat alespoň dvě kopie seed:




- Jedná se o první čipovou kartu, kterou můžete mít snadno přístupnou pro každodenní operace, jako je ověřování adres nebo podepisování transakcí. Tato metoda je praktická (jak uvidíme v části 5) a díky ochraně, kterou nabízí kód PIN, zůstává bezpečná, takže ji můžete mít přístupnou bez většího rizika;
- Druhá kopie nešifrované mnemotechnické fráze sloužící jako konečná záloha vašeho portfolia, která se použije pouze v případě ztráty nebo krádeže nástroje Seedkeeper. Jelikož je tato verze nešifrovaná, musí být uchovávána na odděleném, bezpečnějším místě, aby se zabránilo současnému ohrožení obou záloh.



V závislosti na vaší strategii ochrany a rizikovém profilu můžete také duplikovat seed na několika různých Seedkeeperech nebo vytvořit několik fyzických kopií mnemotechniky. Chcete-li se o těchto postupech dozvědět více, podívejte se na následující výukový program:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. Načítání seed od Seedkeeper



![video](https://youtu.be/ms0Iq_IyaoE)



Nyní můžete pomocí nástroje Seedkeeper při spuštění načíst mnemotechnickou frázi do nástroje SeedSigner a podepsat tak transakce Bitcoin. Chcete-li začít, zapněte SeedSigner jeho zapojením a otevřete nabídku `Seeds`.



![Image](assets/fr/23.webp)



Poté vyberte možnost `Ze SeedKeeperu`.



![Image](assets/fr/24.webp)



Vložte zařízení Seedkeeper do čtečky čipových karet a zadejte kód PIN pro odemknutí. Zadání potvrďte stisknutím potvrzovacího tlačítka vpravo dole, `KEY3`.



![Image](assets/fr/25.webp)



Seedkeeper může obsahovat několik tajemství, takže SeedSigner vás poté vyzve, abyste si vybrali to, které chcete načíst. Zobrazený štítek odpovídá názvu, který jste definovali v kroku 4. Pokud jste, jako v mém případě, zaregistrovali pouze jeden seed, bude k dispozici pouze jedna možnost.



![Image](assets/fr/26.webp)



Vaše zařízení seed je nyní načteno. Porovnáním otisku prstu zobrazeného na obrazovce s otiskem zadaným v nastavení Sparrow Wallet zkontrolujte, zda se jedná o správný wallet. Tento otisk prstu byl rovněž zadán při prvním vytvoření wallet.



Používáte-li přípravek passphrase, můžete jej v této fázi použít (viz část 6 tohoto návodu). V opačném případě jednoduše klikněte na tlačítko `Done`.



![Image](assets/fr/27.webp)



Poté můžete wallet používat jako obvykle: kontrolovat doručovací adresy a podepisovat transakce stejně jako s klasickým SeedSignerem. Chcete-li se dozvědět více o tom, jak jej používat, podívejte se na specializovaný návod :



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Použití nástroje Seedkeeper s nástrojem passphrase BIP39



Používáte k ochraně svého portfolia Bitcoin zařízení passphrase? Můžete si ho zaregistrovat v programu Seedkeeper spolu s seed. Toto řešení vám umožní rychlé načtení wallet do SeedSigneru, aniž byste museli při každém použití ručně zadávat passphrase na malé klávesnici.



Tuto metodu považuji za obzvláště zajímavou, protože umožňuje využívat bezpečnostní výhody passphrase a zároveň eliminuje omezení spojená s jeho každodenním používáním. Zde je příklad konfigurace, kterou bych doporučil:




- Uchovávejte zařízení seed a passphrase ve schránce Seedkeeper chráněné silným kódem PIN (to je důležité). Tato záloha vám umožní snadné každodenní používání zařízení wallet. Pokud chcete, můžete tyto informace duplikovat na druhém zařízení Seedkeeper;
- Uchovávejte si také přehlednou kopii mnemotechnické pomůcky a passphrase, a to na papíře nebo na kovu. Jedná se o zálohu poslední instance, pokud ztratíte svůj Seedkeeper nebo jeho PIN. Nezapomeňte tyto kopie uchovávat na oddělených místech, aby nemohly být ohroženy současně.



V této konfiguraci, pokud se někdo dostane k vašemu mnemotechnickému kódu s otevřeným textem, nebude schopen nic ukrást, aniž by znal kód passphrase (samozřejmě za předpokladu, že je dostatečně silný, aby odolal útoku hrubou silou). A naopak, pokud někdo objeví váš passphrase v prostém textu, zůstane bez odpovídající mnemotechnické fráze nepoužitelný.



A konečně, pokud se někomu podaří získat fyzický přístup k vašemu zařízení Seedkeeper obsahujícímu seed a passphrase, nebude moci bez znalosti kódu PIN nic vyjmout. Na rozdíl od passphrase nelze tento kód vylomit, protože čipová karta se po pěti neplatných pokusech automaticky uzamkne.



Bezpečnost této konfigurace je proto založena na dvou základních bodech:




- A **passphrase strong**: musí být dlouhý, náhodný a obsahovat širokou škálu znaků. Jeho složitost pro vás nepředstavuje problém, protože jej budete muset zadat pouze jednou na klávesnici během inicializace; poté bude přenášen nástrojem Seedkeeper ;
- **silný kód PIN** pro Seedkeeper: rovněž náhodný a složený ze 16 znaků.



Chcete-li toto nastavení nastavit, začněte tím, že do aplikace SeedSigner obvyklým způsobem nahrajete svůj kód passphrase. Můžete postupovat podle postupu podrobně popsaného v tomto návodu:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Jakmile je vaše portfolio s passphrase správně načteno do SeedSigneru, otevřete nabídku `Seeds` a vyberte otisk odpovídající tomuto portfoliu. Všimněte si, že tento otisk se liší od otisku portfolia bez passphrase.



![Image](assets/fr/28.webp)



Poté klikněte na `Zálohovat Seed`, vložte Seedkeeper do jednotky a vyberte `Do SeedKeeper`.



![Image](assets/fr/29.webp)



Zadáním kódu PIN odemkněte aplikaci Seedkeeper a přiřaďte jí štítek. Jako štítek můžete ponechat otisk prstu, abyste zachovali určitou formu věrohodného popření, nebo můžete například výslovně uvést `Passphrase Wallet`.



![Image](assets/fr/30.webp)



Vaše portfolio passphrase je nyní zaregistrováno ve službě Seedkeeper.



![Image](assets/fr/31.webp)



Při příštím spuštění jednoduše vložte Seedkeeper do jednotky a přejděte na `Seeds > From SeedKeeper`.



![Image](assets/fr/32.webp)



Zadáním kódu PIN odemkněte čipovou kartu a poté vyberte wallet odpovídající vašemu passphrase.



![Image](assets/fr/33.webp)



Zkontrolujte otisk passphrase a wallet a potvrďte.



![Image](assets/fr/34.webp)



Nyní můžete přistupovat ke svému portfoliu pomocí passphrase a podepisovat transakce jako obvykle na SeedSigneru.



## 7. Další možnosti



V nabídce `Nástroje > Nástroje čipové karty` najdete několik možností správy nástroje Seedkeeper:





- V nabídce `Běžné nástroje` můžete :
 - Zkontrolujte pravost karty;
 - Změna kódu PIN ;
 - Změňte štítky související s vašimi tajemstvími ;
 - Zakázat funkci NFC (doporučeno, pokud používáte pouze čtečku čipů) ;
 - Proveďte obnovení továrního nastavení.





- V nabídce `Funkce nástroje SeedKeeper` můžete :
 - Nahlédněte do seznamu registrovaných tajemství ;
 - Uložit nové tajemství ;
 - Odstranění existujícího tajemství ;
 - Uložit nebo načíst deskriptory (užitečná funkce pro portfolia multi-sig).





- V nabídce `DIY Tools` můžete :
 - Kompilace appletu Seedkeeper ;
 - Nainstalujte applet na prázdnou kartu ;
 - Odstraněním appletu Seedkeeper jej resetujete a znovu jej vyprázdníte.



Nyní víte, jak bezpečně zálohovat své portfolio pomocí nástroje Seedkeeper v kombinaci s nástrojem SeedSigner.



Pokud vás toto nastavení přesvědčilo, neváhejte podpořit projekty, které to umožňují:




- Zakoupením zařízení přímo [na webových stránkách Satochip](https://satochip.io/shop/);
- Přispěním [na projekt SeedSigner](https://seedsigner.com/donate/);
- Přihlášením k odběru kanálu [Crypto Guide na YouTube](https://www.youtube.com/@CryptoGuide/), který provozuje osoba spravující repozitář GitHub, na němž je umístěn upravený firmware.