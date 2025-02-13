---
name: Liana
description: Nastavení a používání peněženky v systému Liana
---
![cover](assets/cover.webp)

V tomto návodu vám krok za krokem vysvětlíme, jak používat aplikaci Liana v počítači. Mimo jiné se dozvíte, jak nastavit automatický plán nástupnictví, přijímat a odesílat bitcoiny v běžných situacích a po uplynutí určitého období získat prostředky z existujícího portfolia.

V lednu 2025 byly hardwarové peněženky kompatibilní se systémem Liana: BitBox02, Blockstream Jade, Blockstream Jade Plus, COLDCARD MK4, COLDCARD Q, Ledger Nano S, Ledger Nano S Plus, Ledger Nano X, Ledger Flex, Specter DIY.

Pokud chcete získat zpět prostředky z existující peněženky Liana, přečtěte si níže uvedenou prezentaci a přejděte přímo do sekce "Získání bitcoinů".

## Představujeme software Liana

Liana je softwarový balík s otevřeným zdrojovým kódem určený pro vytváření a správu pokročilých portfolií, zejména jako součást automatizovaného systému dědictví nebo robustního zálohovacího mechanismu. Projekt vyvíjí od roku 2022 společnost Wizardsardine, kterou spoluzaložili Kévin Loaec a Antoine Poinsot. Na oficiálních stránkách je Liana prezentována jako "jednoduché portfolio pro osobní kurátorství s funkcemi obnovy a dědictví". Software běží na počítačích - Linux, MacOS, Windows - a jeho (otevřený) zdrojový kód je k dispozici [na GitHubu](https://github.com/wizardsardine/liana).

Liana staví na programovatelnosti Bitcoinu a vytváří pokročilou peněženku. Využívá zejména časové zámky (*timelocks*), které umožňují utrácení prostředků až po uplynutí daného časového období a které se podílejí na obnově bitcoinů. Peněženka Liana se tedy skládá z několika cest utrácení:


- Hlavní výdajová cesta, která je vždy k dispozici;
- Alespoň jedna cesta obnovy, která je přístupná po určité době.

Níže uvedený diagram znázorňuje fungování portfolia se dvěma výdajovými cestami:

![Schéma explicatif](assets/fr/01.webp)

Tato operace umožňuje nastavit různé konfigurace, včetně :


- Dědický plán, který umožňuje dědicům získat zpět finanční prostředky v případě úmrtí uživatele. Další informace k tomuto tématu doporučujeme přečíst v [části 4](https://planb.network/courses/btc102/233c88d3-2e8e-5eba-ac06-efe67a209038) kurzu BTC102.
- Posílená záloha s dobou obnovy, která uživateli dává možnost používat peněženku, aniž by musel uchovávat příslušnou tajnou frázi a riskovat její odcizení, například při vloupání.
- Bezpečnostní síť pro lidi, kteří s bitcoiny začínají: budou spravovat svou vlastní peněženku a jejich "opatrovník" (například příbuzný) si vyhradí právo získat jejich prostředky po určité době zpět.
- Podpisové schéma pro více účastníků (*multisig*) se sníženými požadavky v čase, aby bylo možné se vypořádat se zánikem jednoho nebo více účastníků, například partnerů společnosti.

Velkou předností systému Liana je, že zavádí standardizovaný způsob, jak zaručit navrácení finančních prostředků v případě ztráty hlavního klíče, který se používá na běžné výdaje. To představuje obrovskou inovaci pro čistou úschovu finančních prostředků, která je plná rizik, zejména pokud nejste v této oblasti dobře informováni. Liana by proto mohla povzbudit i ty uživatele, kteří se nebojí riskovat, aby přestali využívat úschovnu (například směnárenskou platformu) k držení svých prostředků a získali zpět vlastnictví svých peněz, což je v souladu s cypherpunkovým étosem Bitcoinu.

Liana má samozřejmě i své nevýhody. První z nich je, že musíte pravidelně aktualizovat svou peněženku provedením transakce v blockchainu Bitcoinu. To může být nepříjemné (v závislosti na tom, jak často software používáte) a nákladné (v závislosti na výši poplatků v daném okamžiku), ale je to cena, kterou platíte za vyšší bezpečnost.

Druhým negativním bodem může být důvěrnost. Pokud do konfigurace zapojíte jinou osobu, bude mít přístup ke všem vašim adresám, a může tedy sledovat vaši činnost. To však nebude problém, pokud se rozhodnete pro posílené zálohování nebo pro plán nástupnictví, kdy váš dědic nemá bezprostřední znalost údajů o portfoliu.

## Příprava

V tomto tutoriálu si sestavíme plán nástupnictví. Budeme používat :


- Ledger Nano S Plus pro každodenní výdaje;

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

- Blockstream Jade, který se používá k vymáhání finančních prostředků;

https://planb.network/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3

- Dvě paměťová média (USB klíče) pro uložení deskriptoru portfolia;
- Dědický dopis s pokyny pro vymáhání finančních prostředků;
- Zapečetěný sáček s číslem, který zajistí, že zařízení pro regeneraci (Jade) nebylo použito.

## Instalace a konfigurace

Navštivte oficiální webové stránky Wizardsardine a stáhněte si Lianu na adrese https://wizardsardine.com/liana/. Můžete si také stáhnout nejnovější verzi [z repozitáře GitHub](https://github.com/wizardsardine/liana/releases), kde si můžete ověřit pravost softwaru. Verze použitá v tomto návodu je 0.9.

![Télécharger Liana](assets/fr/02.webp)

Chcete-li zjistit, jak ručně ověřit pravost a integritu softwaru před instalací, doporučujeme vám nahlédnout do tohoto návodu :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Nainstalujte software do počítače a spusťte jej. Vyberte možnost "*Vytvořit novou peněženku Liana*" a nakonfigurujte peněženku.

![Accueil Liana](assets/fr/03.webp)

Vyberte si typ portfolia. Pokud chcete nastavit rozšířenou zálohu s dobou obnovy, můžete vybrat možnost "*Vytvořit vlastní*" a zvolit výchozí schéma. To bude fungovat v podstatě stejným způsobem, až na to, že nebudete muset zachovávat frázi o obnově hardwarové peněženky.

Nebereme zde v úvahu případ *Rozšiřujícího se multisig*, který nastavuje složitější konfiguraci.

Pro účely tohoto výukového kurzu budeme používat jednoduchou dědičnost.

![Choisir type de portefeuille](assets/fr/04.webp)

Následuje stručné vysvětlení.

![Rapide explication](assets/fr/05.webp)

Po přečtení vysvětlení budete moci nastavit klíče k peněžence Liana. Jedná se o zásadní krok, protože určuje výdajové charakteristiky vašeho účtu.

![Configurer clés](assets/fr/06.webp)

V nabídce "Rozšířená nastavení" můžete nejprve rozhodnout o "typu deskriptoru", tj. způsobu, jakým bude smlouva zapsána v řetězci. Můžete si vybrat mezi dvěma typy: P2WSH (SegWit) nebo Taproot. V obou případech bude sémantika podmínek utrácení stejná. Zatímco P2WSH usnadňuje pochopení kontraktu, Taproot je lepší v tom, že skrývá nepoužívané podmínky a šetří náklady při načítání.

Tato volba je nepovinná: v případě pochybností ponechte výchozí volbu (P2WSH v případě verze 0.9, ale ta se může změnit).

![Choisir le type de descripteur](assets/fr/07.webp)

Dále nakonfigurujte primární klíč (*primární klíč*). Tento klíč (nebo spíše tato sada klíčů) bude použit pro aktuální výdaje finančních prostředků, které nepodléhají žádným časovým podmínkám. Kliknutím na tlačítko "*Nastavit*" můžete vybrat odpovídající *podpisové zařízení*. V našem případě jsme zvolili hardwarovou peněženku Ledger Nano S Plus.

Povolit sdílení rozšířeného veřejného klíče ze zařízení. Dejte tomuto klíči smysluplný název (v tomto případě "Nano S+"). Všimněte si, že všechny aplikace nainstalované v zařízení budou nadále normálně fungovat.

![Configurer clé principale](assets/fr/08.webp)

Dále nastavte zpoždění návratnosti, tj. dobu, po které lze prostředky utratit pomocí klíče *dědictví*. Toto zpoždění je definováno v blocích, přičemž každý blok je oddělen v průměru 10 minutami. Může se pohybovat od 10 minut (1 blok) do přibližně 15 měsíců (65 535 bloků). Tato horní hranice je omezením protokolu Bitcoin, protože doba uzamčení je kódována na 16 bitů.

Pokud nenastanou zvláštní okolnosti, zvolte nejdelší dobu dodání: 15 měsíců nebo 65 535 bloků. Tím ušetříte náklady. Doporučujeme však, abyste postup aktualizace (popsaný v části "Aktualizace portfolia") prováděli jednou ročně, vždy ve stejnou roční dobu, abyste si tento postup "ritualizovali" a nezapomínali.

Zde jsme nastavili dobu zotavení na jednu hodinu (6 bloků) pro provedení našich testů.

![Configurer temps de verrouillage](assets/fr/09.webp)

Nakonec nastavte klíč k majetku. Tento klíč (nebo spíše sada klíčů) bude sloužit k získání finančních prostředků v případě vašeho zmizení. Klikněte na tlačítko "*Nastavit*", vyberte podepisovací zařízení a potvrďte na něm sdílení rozšířeného veřejného klíče.

Pro tento výukový program jsme vybrali Jade. Dejte klíči výstižný název (zde "Jade"). Stejně jako u prvního zařízení budou i nadále fungovat běžné účty.

![Configurer clé de succession](assets/fr/10.webp)

Po dokončení všech těchto úkonů zkontrolujte, zda je vše v pořádku, a kliknutím na tlačítko "*Pokračovat*" potvrďte své volby.

![Confirmer clés](assets/fr/11.webp)

Dalším krokem je uložení deskriptoru portfolia. To jsou informace, které potřebujete k vyhledání prostředků na svém účtu. Na rozdíl od mnemotechnické fráze vám deskriptor neumožňuje utrácet finanční prostředky, takže jeho zveřejnění bude představovat pouze problém s důvěrností (dotyčná osoba bude znát všechny vaše transakce).

Uložte dvě kopie deskriptoru na elektronická média, například na USB klíče. Nezapomeňte si také vytisknout dvě kopie na papír, abyste k nim měli přístup v případě poškození elektronického média. Každá záloha musí být spojena s podpisovým zařízením.

![Sauvegarder descripteur](assets/fr/12.webp)

Náš deskriptor (který je rozebrán na konci výukového programu) je následující:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

Posledním krokem počáteční konfigurace portfolia je ověření deskriptoru v každém z portfolií hardwaru, které slouží jako podpisová zařízení.

![Enregistrer descripteur](assets/fr/13.webp)

Totéž proveďte pro každé podepisovací zařízení. Budete muset zkontrolovat a potvrdit, že deskriptor byl přidán do každého portfolia hardwaru.

![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)

Informace o vaší peněžence jsou nyní zaregistrovány a zbývá jen nastavit, jak se chcete připojit k síti Bitcoin. Můžete si vybrat, zda chcete použít svůj vlastní uzel (místní nebo vzdálený), nebo využít infrastrukturu WizardSardine. V druhém případě budete muset s peněženkou propojit e-mailovou adresu, která vám umožní získat deskriptor. WizardSardine bude mít přístup ke všem vašim transakcím. Doporučujeme tedy první možnost.

![Sélectionner connexion réseau](assets/fr/15.webp)

Rozhodli jsme se použít vlastní uzel. Můžete použít existující uzel nebo si na svůj počítač nainstalovat *odříznutý uzel*. Pokud nemáte přístup k žádnému jinému uzlu, nainstalujte si na svůj počítač vlastní uzel, což by mělo nějakou dobu trvat (řádově několik dní).

![Choisir type de nœud](assets/fr/16.webp)

Pro tento návod jsme použili existující (veřejný) server Electrum. Ale pozor! Měl přístup ke všem našim aktivitám s peněženkou Liana. Pokud tedy chcete chránit své soukromí, použijte vlastní uzel.

![Connexion serveur Electrum public](assets/fr/17.webp)

Po dokončení konfigurace uzlu by se měla otevřít hlavní obrazovka s čerstvě vytvořenou peněženkou Liana.

Využijte možnosti uložit regenerační jednotku na bezpečné místo. Měla by být uložena na strategickém místě, aby ji v případě vaší smrti mohli najít vaši dědicové.

Pro větší bezpečnost můžete komponenty použité k obnově vložit do zapečetěného sáčku (*sáček odolný proti zneužití*) a někam si zapsat jeho sériové číslo. Tím zajistíte, že se k němu nikdo nedostal a že vaše zařízení zůstane platné.

V našem příkladu jsme sestavili následující prvky:


- Blockstream Jade jako podpisové zařízení pro majetek;
- Kabel USB pro připojení a dobíjení zařízení;
- Papírová záloha věty pro případ poruchy nebo poškození zařízení (všimněte si, že médium může být také kovové, a tedy chráněné před povětrnostními vlivy, jako je tomu například u kapslí Cryptosteel);
- Klíč USB obsahující deskriptor portfolia ;
- Papírová záloha deskriptoru pro případ poruchy nebo poškození klíče USB (tato záloha zde není vyfotografována);
- Dědický dopis s popisem kroků, které je třeba podniknout za účelem zpětného získání finančních prostředků.

![Éléments de récupération](assets/fr/18.webp)

A tyto položky jsme zapečetili!

![Sachet scellé récupération](assets/fr/19.webp)

## Přijetí finančních prostředků

Na hlavní obrazovce Liany se zobrazuje váš zůstatek a transakce (minulé i aktuální) spojené s vaším portfoliem. V našem případě je zůstatek nulový, což je normální.

![Écran principal](assets/fr/20.webp)

Chcete-li získat finanční prostředky, přejděte na kartu "*Příjem*" a klikněte na "*Vygenerovat adresu*". Na obrazovce by se měla objevit nová adresa. Je delší než v běžných portfoliích: je to adresa spojená se samostatnou smlouvou (P2WSH nebo Taproot).

![Générer nouvelle adresse](assets/fr/21.webp)

Tuto adresu je třeba ověřit na hardwarovém portfoliu kliknutím na "*Ověřit na hardwarovém zařízení*".

![Vérifier adresse portefeuille matériel](assets/fr/22.webp)

Po odeslání prostředků se transakce zobrazí na hlavní obrazovce (nejprve jako nepotvrzená a poté jako potvrzená). Zde jsme pro tento test poslali 50 000 satošů (v době převodu něco přes 50 USD). Je samozřejmé, že ve vašem případě bude muset být převáděná částka kvůli transakčním poplatkům řádově vyšší než tato hodnota.

![Vérifier solde](assets/fr/23.webp)

Stav vypršení platnosti svých prostředků můžete zkontrolovat na kartě "*Mince*". Na této kartě se zobrazují různé mince (UTXO) ve vaší peněžence. Zde vidíme, že platnost mince 50 000 satoši vytvořené naší transakcí vyprší ve stejný den (za hodinu).

![Obtenir informations pièce](assets/fr/24.webp)

Chcete-li lépe pochopit model reprezentace UTXO používaný v Bitcoinu, můžete si přečíst první část kurzu o důvěrnosti v Bitcoinu, který napsal Loïc Morel :

https://planb.network/courses/btc204
## Běžné výdaje

Běžné výdaje jsou běžnou situací pro použití Liany. Posílání bitcoinů pomocí hlavního klíče funguje stejně jako ve všech klasických bitcoinových peněženkách, jako je Electrum nebo Sparrow.

Chcete-li provést poplatek, přejděte na kartu "*Odeslat*" a zadejte základní informace: adresu BTC příjemce, částku, která má být odeslána, a požadovanou sazbu poplatku. Pro vaše osobní pohodlí můžete přidat také popis (uložený lokálně). V našem příkladu jsme poslali 10 000 satošů jistému Bobovi za sazbu poplatku 4 satošů/ov, tedy 0,67 USD v době transakce.

Liana také nabízí "kontrolu mincí": určíte, kterou minci (UTXO) chcete utratit. Zde jsme zvolili dříve vytvořenou minci 50 000 satoši.

![Envoyer fonds clé principale](assets/fr/25.webp)

Poté podepište transakci pomocí podpisového zařízení propojeného s hlavním klíčem kliknutím na "*Podepsat*". Transakci budete muset ověřit a potvrdit ve své hardwarové peněžence. Zde jsme k podpisu transakce použili zařízení Nano S Plus.

![Signer transaction clé principale](assets/fr/26.webp)

Nakonec transakci odvysílejte po síti kliknutím na tlačítko "*Vysílání*". Všimněte si, že odesláním prostředků se vynuluje doba obnovy použitých mincí.

![Diffuser transaction clé principale](assets/fr/27.webp)

Transakce se zobrazí na hlavní obrazovce a váš zůstatek se aktualizuje.

![Solde après dépense](assets/fr/28.webp)

## Aktualizace portfolia

Jak bylo vysvětleno výše, peněženka Liana vyžaduje, abyste pravidelně aktualizovali své prostředky provedením transakce v blockchainu. Pokud tak neučiníte, mohou být vaše prostředky obnoveny dědicem (nebo vaším druhým zařízením v případě rozšířené zálohy). Tato situace není nijak extrémně nebezpečná, ale znemožňuje účel zřízení tohoto mechanismu: zůstat pod kontrolou svých bitcoinů, aniž byste se museli obracet na důvěryhodnou třetí stranu, a zároveň využívat výhod bezpečnostní sítě.

Před vypršením platnosti vašich prostředků (nebo jejich části) se zobrazí upozornění, že je lze utratit pomocí klíče pro obnovení. Bude informovat o tom, že vaše "cesta obnovy" (*cesta obnovy*) bude brzy k dispozici. Vzhledem ke krátkosti doby obnovy (jedna hodina) se tato zpráva zobrazuje přímo v našem případě.

![Avertissement chemin récupération](assets/fr/29.webp)

Po uplynutí lhůty se zobrazí tlačítko s výzvou k aktualizaci příslušných prostředků.

![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)

Chcete-li aktualizovat své mince, přejděte na kartu "*Mince*" a klikněte na "*Obnovit mince*" v příslušném poli mince. Pokud máte více mincí, měli byste je z důvodu zachování důvěrnosti obnovovat postupně a v relativně krátkých intervalech. Chcete-li snížit náklady, můžete své prostředky konsolidovat odesláním celého portfolia na novou přijímací adresu, což však ovlivní důvěrnost.

![Actualiser pièce](assets/fr/31.webp)

Uveďte požadovanou sazbu poplatku za transakci. Vzhledem k tomu, že se jedná o převod na sebe, můžete nastavit poměrně nízkou sazbu poplatku, zejména pokud to uděláte několik dní před vypršením platnosti.

![Transfert à soi-même](assets/fr/32.webp)

Transakce (označená jako "*samostatný převod*") bude viditelná pouze na kartě "*Transakce*".

![Transactions après auto-transfert](assets/fr/33.webp)

Po potvrzení je vaše mince v bezpečí! Až do příštího data expirace můžete být v klidu.

## Obnova bitcoinu

Při vymáhání finančních prostředků z portfolia Liana se můžete setkat s jednou ze dvou situací. Můžete mít přístup k počítači, na kterém je software nainstalován, a v takovém případě jej stačí pouze otevřít (což se stane v případě rozšířeného modelu zálohování). Je však možné, že k tomuto počítači přístup nemáte, takže zde začneme od nuly. Všimněte si, že postup obnovy je v obou případech stejný.

Chcete-li začít, stáhněte si Lianu z [oficiální stránky Wizardsardine](https://wizardsardine.com/liana/) nebo z [repozitáře GitHub](https://github.com/wizardsardine/liana/releases), kde si můžete ověřit pravost softwaru. Nainstalujte software a spusťte jej. V našem případě byla použita verze 0.9, takže vizuální podoba se mohla změnit. Na uvítací obrazovce vyberte možnost "Add an existing Liana wallet" (Přidat existující peněženku Liana).

![Ajouter portefeuille existant](assets/fr/34.webp)

Nakonfigurujte způsob připojení k síti. Můžete si vybrat, zda chcete použít vlastní uzel (místní nebo vzdálený), nebo infrastrukturu WizardSardine. V druhém případě budete potřebovat e-mailovou adresu, kterou používá tvůrce portfolia, aby bylo možné automaticky vyhledat fondy. Pokud tyto informace nemáte, zvolte první možnost.

![Sélectionner connexion réseau](assets/fr/35.webp)

Pokud používáte vlastní uzel, importujte deskriptor portfolia. Jedná se o technický popis účtu, který vám umožní načíst prostředky na něm uložené. V našem případě jsou to následující informace:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

![Importer descripteur](assets/fr/36.webp)

Liana vás poté požádá o zadání mnemotechnické fráze. Pokud máte funkční podpisové zařízení (hardwarovou peněženku), tuto část přeskočte. Pokud vaše zařízení chybí nebo je poškozené, ale máte příslušných 12 nebo 24 slov, můžete tuto možnost použít i tak. Pro jistotu (pokud je částka, kterou je třeba obnovit, vysoká) přesto doporučujeme pořídit si novou hardwarovou peněženku a použít mnemotechnickou pomůcku k obnově klíčů v ní.

V našem případě používáme jako zařízení pro obnovu hardwarovou peněženku Blockstream Jade a rozhodli jsme se tento krok přeskočit ("*Skip*").

![Passer phrase mnémotechnique](assets/fr/37.webp)

Zkontrolujte a uložte deskriptor v podpisovém zařízení jeho výběrem na obrazovce. Pokud se hardwarová peněženka nezobrazí, zkontrolujte, zda je připojená a odemčená. Zkontrolujte a potvrďte, že tyto informace byly do zařízení přidány.

![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)

Konfigurace uzlu. Můžete použít existující uzel nebo si do počítače nainstalovat *odříznutý uzel*. V našem případě jsme použili existující uzel.

![Choisir type de nœud](assets/fr/39.webp)

V tomto tutoriálu jsme použili veřejný server Electrum. Ten však měl přístup ke všem našim aktivitám s peněženkou Liana. Pokud chcete chránit své soukromí, raději použijte vlastní uzel.

![Connexion serveur Electrum public](assets/fr/17.webp)

Po nastavení uzlu se dostanete na hlavní obrazovku peněženky, kde si můžete prohlédnout zůstatek a minulé transakce spojené s účtem. Můžete také zjistit, zda lze prostředky získat zpět. Zde vidíme, že mince lze získat zpět.

![Accueil Liana récupération](assets/fr/40.webp)

Chcete-li obnovit prostředky v portfoliu, přejděte do Nastavení ("*Nastavení*") vlevo dole a klikněte na "*Obnovení*".

![Récupération dans paramètres](assets/fr/41.webp)

Mince v peněžence utratíte zaškrtnutím příslušného políčka. Uveďte adresu BTC, na kterou chcete peníze poslat, a také sazbu transakčního poplatku. Poté klikněte na tlačítko "*Další*".

![Récupération des pièces](assets/fr/42.webp)

Podepište transakci kliknutím na "*Podepsat*" a ověřte transakci ve své hardwarové peněžence.

![Signer transaction clé de récupération](assets/fr/43.webp)

Poté jej odvysílejte po síti kliknutím na "*Vysílání*".

![Diffuser transaction clé de récupération](assets/fr/44.webp)

Transakce by se měla zobrazit na hlavní obrazovce. Po potvrzení je obnova dokončena!

![Écran principal après récupération](assets/fr/45.webp)

## Videa

Pokud se chcete o Lianě dozvědět více, najdete zde několik videí, která vám přiblíží její fungování. Zde je videoprezentace systému Liana s Kévinem Loaecem a Antoinem Poinsotem :

![Vidéo de présentation avec Kévin Loaec et Antoine Poinsot](https://youtu.be/siuLmQo1lM8)

A zde je návod, jak používat Lianu, s Antoinem Poinsotem :

![Vidéo-tutoriel avec Antoine Poinsot](https://youtu.be/JrG4WMVPZDQ)

Manipulace, které jsou v něm uvedeny, jsou podobné těm, které jsou prezentovány v tomto výukovém programu.

## Bonus: analýza deskriptorů

Deskriptor je lidsky čitelný řetězec znaků, který vyčerpávajícím způsobem popisuje sadu adres. Kombinuje řadu základních informací pro vyhledávání částí (UTXO) pokročilého portfolia. Způsob zápisu deskriptoru vychází ze [syntaxe Miniscript](https://bitbox.swiss/blog/understanding-bitcoin-miniscript-part-2/), skriptovacího jazyka, který v roce 2019 vyvinuli Andrew Poelstra, Pieter Wuille a Sanket Kanjalkar.

Abychom lépe pochopili, proč je tento řetězec znaků důležitý, analyzujme deskriptor v našem příkladu, který je :

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

Z tohoto deskriptoru lze získat následující informace:


- `wsh` (zkratka pro *witness script hash*): Jedná se o typ vytvořeného transakčního výstupu. Pokud bychom se rozhodli použít Taproot, identifikátor by byl `tr`.
- `or_d`: Je to logický operátor, který označuje, že *jedna z následujících dvou* podmínek musí být splněna, aby byl výdaj uznán (`_d` označuje konkrétní syntaxi).
- `pk` (zkratka pro *veřejný klíč*): Tento operátor porovná daný podpis s následujícím veřejným klíčem a odpověď poskytne jako logickou hodnotu (TRUE nebo FALSE).
- `[3689a8e7/48'/0'/0'/2']`: Tento prvek obsahuje *otisk* hlavního klíče pro hlavní hardwarovou peněženku (v tomto případě Nano S Plus) a odvozovací cestu k propojenému rozšířenému soukromému klíči (od kterého jsou odvozeny všechny ostatní soukromé klíče).
- `xpub6FKY ... WQa`: Jedná se o rozšířený veřejný klíč spojený s hlavním portfoliem hardwaru (zde Nano S Plus)
- `/<0;1>/*`: To jsou odvozovací cesty pro získání jednoduchých klíčů a adres: `0` pro příjem, `1` pro interní operace (*změna*), s "divokým znakem" (`*`) umožňujícím postupné odvození několika adres konfigurovatelným způsobem, podobně jako při řízení "mezer" v klasickém portfoliovém softwaru.
- and_v`: Je to logický operátor, který označuje, že *musí být splněny následující dvě* podmínky, aby byl výdaj uznán (`_v` označuje konkrétní syntaxi).
- `v:pkh` (zkratka pro *verify: public key hash*): Tento operátor ověřuje daný podpis a veřejný klíč proti následujícímu hashi veřejného klíče (*hash*). Jedná se v podstatě o stejnou kontrolu jako u skriptů P2PKH a P2WPKH.
- `[42e629dd/48'/0'/0'/2']`: Jedná se o stejný prvek jako výše (skládající se ze stopy a cesty odvození), s tím rozdílem, že je uvedena stopa hlavního klíče hardwarového portfolia obnovy (v tomto případě Jade).
- `xpub6DpQ ... WQd`: Jedná se o rozšířený veřejný klíč spojený s hardwarovou peněženkou pro obnovu (zde Jade).
- `older(6)` : Tento operátor kontroluje, zda vytvořený transakční výstup musí mít stáří striktně větší než 6 bloků, aby mohl být použit.

Poslední datová položka (`8alrve5h`) je kontrolní součet deskriptoru a odpovídá identifikátoru portfolia.

Skripty vytvořené v rámci tohoto portfolia budou mít následující podobu:

```plaintext
<primary_key> CHECKSIG IFDUP NOTIF DUP HASH160 <recovery_key_hash> EQUALVERIFY CHECKSIGVERIFY <locktime> CHECKSEQUENCEVERIFY ENDIF
```

Protože bezpečnost vaší peněženky Bitcoin závisí také na tom, jak rozumíte jejímu fungování, doporučuji vám, abyste si podrobně prostudovali mechanismy deterministických a hierarchických peněženek na tomto bezplatném školení na téma Plan ₿ Network :

https://planb.network/courses/cyp201