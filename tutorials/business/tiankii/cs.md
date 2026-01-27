---
name: Tiankii
description: Sada nástrojů Lightning pro maloobchodníky a spotřebitele
---

![cover](assets/cover.webp)



V ekosystému Bitcoin zůstává přijímání plateb v reálném čase pro podniky i jednotlivce velkou výzvou. Tradiční řešení často vyžadují pokročilé technické znalosti, složitou infrastrukturu, kterou je třeba udržovat, nebo vyžadují, aby finanční prostředky byly v držení zprostředkovatelů. Tato situace brzdí masové přijetí Bitcoin jako každodenní měny, a to navzdory příslibu technologického pokroku Lightning Network.



Salvadorská společnost Tiankii, která se zrodila v roce 2021, na tento problém reaguje nabídkou dostupné modulární infrastruktury Bitcoin. Místo toho, aby nutila k přijetí uzavřeného ekosystému, nabízí Tiankii sadu vzájemně propojených nástrojů, které umožňují komukoli integrovat Bitcoin Lightning do svého podnikání, aniž by se vzdal kontroly nad svými prostředky.



## Co je Tiankii?



### Původ a filozofie



Tiankii - výraz v jazyce nahuatl, který znamená "trh pod širým nebem přístupný všem" - je první 100% Bitcoin start-up v Salvadoru. Společnost založil Darvin Otero poté, co byl systém Bitcoin přijat jako zákonné platidlo v zemi, a jejím cílem je přeměnit systém Bitcoin z úložiště hodnoty na transakční měnu pro každodenní nákupy. Na rozdíl od depozitářských platforem Tiankii uplatňuje neúvěrový přístup, kdy si uživatelé ponechávají kontrolu nad svými prostředky a infrastruktura slouží pouze jako technický zprostředkovatel.



### Technická architektura



Společnost Tiankii se profiluje jako poskytovatel infrastruktury Bitcoin jako služby založené na Lightning Network. Tato technologie druhé vrstvy umožňuje téměř okamžité transakce se zanedbatelnými náklady, což umožňuje mikroplatby a každodenní nákupy.



Architektura je založena na třech pilířích:



**První blesk**: Systematicky upřednostňujte síť Lightning kvůli její rychlosti a nižším nákladům, přičemž zachovejte podporu transakcí on-chain pro velké částky.



**Otevřené standardy**: Pro automatizaci platebních požadavků se používá LNURL, Lightning Address pro čitelné e-mailové ID a Bolt Card pro interoperabilní platby NFC.



**Modularita kompatibilní s wallet**: Možnost připojení různých portfolií Lightning (LNbits, Blink, BlueWallet) nebo vlastního uzlu, což nabízí maximální flexibilitu v závislosti na požadované úrovni odbornosti a autonomie.



## Nástroje ekosystému Tiankii



### Bitcoin POS - Platební terminál v obchodě



Aplikace promění smartphone nebo tablet v terminál Lightning. Obchodník zadá částku v místní měně a aplikace vygeneruje QR kód Lightning nebo přijme kartu Bolt. Transakce jsou okamžitě připisovány bez provizí, s automatickými převody ve více než 150 měnách, správou spropitného a historií prodejů.



### Merchant Dashboard - Jednotné řízení prodeje



Interface web centralizovaný pro připojení wallet Lightning, sledování transakcí v reálném čase, vystavování faktur a účetních výkazů generate. Platforma sdružuje všechny kanály: platby v obchodě (POS), online prodej (zásuvné moduly e-commerce) nebo integrace API. Platby se sbíhají na zvoleném systému wallet.



### Bezkontaktní karta Bitcoin (karta Bolt)



Karta NFC Bolt představuje hlavní inovaci společnosti Tiankii v oblasti demokratizace karty Bitcoin pro širokou veřejnost. Funguje jako bezkontaktní bankovní karta a umožňuje platit za nákupy pomocí blesku Bitcoin pouhým poklepáním na kompatibilní terminál.



Na rozdíl od tradičních úschovných řešení se tato karta řídí otevřeným standardem zaručujícím interoperabilitu. Uživatelé ji mohou prostřednictvím aplikace IBI propojit s vlastní kartou wallet, a zachovat si tak své soukromé klíče a plnou kontrolu nad přidruženými prostředky. Platba trvá pouhou sekundu, přičemž není nutné vytahovat chytrý telefon ani mít v době platby aktivní připojení k internetu.



Toto řešení je vhodné zejména pro lidi, kteří neznají chytré telefony, a nabízí přístupnou bránu do ekonomiky Bitcoin.



### Aplikace IBI - Interface jednotlivé Bitcoin



Aplikace IBI (Individual Bitcoin Interface) je určena pro jednotlivce, kteří chtějí používat blesk Bitcoin denně. Její hlavní výhoda spočívá ve vygenerování personalizovaného identifikátoru platby Address Lightning, který je čitelný ve formátu e-mailu (příklad: alice@ibi.me).



Tento identifikátor výrazně zjednodušuje příjem plateb: není třeba pro každou transakci zakládat novou fakturu generate, odesílatel může jednoduše zadat adresu Lightning. Rozhraní také umožňuje spravovat kartu Bolt (aktivace, deaktivace, výdajové limity), připojovat různé peněženky Lightning a provádět platby skenováním kódů QR.



### Zásuvné moduly pro elektronické obchodování



Připravené integrace pro WooCommerce, Shopify a Cloudbeds. Instalace během několika minut a přidání Bitcoin Lightning k pokladně. Výhody: nulová provize (oproti 2-3 % u kreditních karet), okamžité zúčtování, celosvětový přístup, eliminace chargebacků. Platby přicházejí přímo na připojené zařízení wallet obchodníka.



### Bitcoin API a vývojářské nástroje



Tiankii SDK umožňuje integrovat Bitcoin Lightning do stávajících aplikací bez nutnosti udržovat vlastní uzel. API se stará o vytváření faktur, ověřování plateb a hromadné rozesílání prostřednictvím robustní infrastruktury hostované na Google Cloud. Command Center doplňuje nabídku pro organizace s Address Lightning o vlastní domény, hromadné platby a centralizovanou správu terminálů a karet NFC.



## Instalace a první kroky



### Základní předpoklady



Používání systému Tiankii nevyžaduje žádné složité technické předpoklady. Aplikace fungují prostřednictvím webového prohlížeče na chytrém telefonu, tabletu nebo počítači. Není nutná instalace žádné nativní aplikace: k přístupu do IBI nebo na Merchant Dashboard stačí přístup k internetu a nejnovější prohlížeč.



**Pro soukromé uživatele (aplikace IBI)**: Není vyžadován předchozí wallet Lightning. Při vytvoření účtu Tiankii automaticky nakonfiguruje funkční Address Lightning prostřednictvím [Breez SDK Liquid](https://sdk-doc-liquid.breez.technology/guide/about_breez_sdk_liquid.html), bezuzlové implementace, která na pozadí využívá síť Liquid. Můžete okamžitě přijímat a odesílat platby bez jakékoli technické konfigurace. Toto řešení výrazně zjednodušuje přístup pro začátečníky a zároveň zůstává samoobslužné.



**Pro obchodníky (Merchant Dashboard)** : Připojení stávajícího wallet Lightning je povinné pro používání terminálů prodejních míst a přijímání plateb. Tiankii podporuje mnoho řešení: mobilní peněženky (Blink, Strike), samohostitelská řešení (LNbits, LND/CLN node) nebo webové peněženky (Alby). Podrobné průvodce připojením naleznete v části Zdroje tohoto návodu.



### Pro soukromé zákazníky: Aplikace IBI



**Vytvoření účtu



Pro vytvoření účtu přejděte na stránku accounts.ibi.me. Na této stránce si můžete vybrat ze dvou typů účtů: "Personal Use" pro individuální použití nebo "Business Use" pro komerční použití. Výběrem možnosti "Personal Use" získáte přístup k nástrojům pro příjem a odesílání plateb v Bitcoin.



![Choix du type de compte](assets/fr/01.webp)



Po výběru možnosti "Osobní použití" budete automaticky přesměrováni na stránku go.ibi.me, kde dokončíte registraci. Tu můžete provést prostřednictvím e-mailu, telefonního čísla nebo účtu Google, Microsoft nebo Twitter. Po vytvoření můžete okamžitě přistupovat k rozhraní IBI, přičemž váš Lightning Address již bude funkční.



![Création du compte](assets/fr/02.webp)



**Interface main**



Rozhraní IBI zobrazuje váš zůstatek v satoši a místní měně (USD). Tři tlačítka umožňují interakci: "Receive" pro příjem plateb, "Scan" pro skenování QR kódu a "Send" pro odeslání satošů.



![Interface IBI](assets/fr/03.webp)



**Přijmout platbu**



Chcete-li přijímat satoši, stiskněte tlačítko "Receive". Aplikace automaticky vygeneruje QR kód a zobrazí váš personalizovaný blesk Address (formát nom@ibi.me). Sdílejte tuto adresu nebo QR kód s odesílatelem: finanční prostředky dorazí okamžitě na váš účet IBI.



![Réception avec Lightning Address](assets/fr/04.webp)



Po připsání zůstatku můžete tyto satoši použít k platbám.



**Zaslání platby**



Chcete-li odeslat satoši, stiskněte tlačítko "Odeslat". Můžete buď naskenovat QR kód blesku, nebo přímo zadat cíl blesku Address.



![Solde et boutons IBI](assets/fr/05.webp)



![Interface d'envoi](assets/fr/06.webp)



Zadejte požadovanou částku v satoších, zkontrolujte ekvivalentní částku v místní měně a potvrďte platbu.



![Confirmation du montant](assets/fr/07.webp)



Oznámení o úspěšné transakci potvrdí odeslání s podrobnostmi: odeslaná částka, poplatek za transakci a příjemce.



![Paiement réussi](assets/fr/08.webp)



**Správa účtů



V Nastavení můžete spravovat karty Bitcoin NFC (karty Bolt). Rozhraní umožňuje aktivovat, deaktivovat nebo nastavit limity výdajů pro karty.



![Historique des transactions](assets/fr/09.webp)



![Paramètres IBI](assets/fr/10.webp)



### Pro obchodníky: Dashboard obchodníka a POS



**Vytvoření podnikatelského účtu



Pro vytvoření účtu přejděte na stránku accounts.ibi.me. Pro přístup k nástrojům pro obchodníky vyberte možnost "Business Use". Tento typ účtu odemkne přístup k panelu pro obchodníky a terminálům v místě prodeje.



Po výběru možnosti "Business Use" budete automaticky přesměrováni na panel obchodníka (pay.tiankii.com). Tím se dostanete do rozhraní pro správu podniku se sledováním příjmů, transakcí a platebními nástroji. Chcete-li začít přijímat platby, musíte nejprve připojit svůj wallet Lightning kliknutím na odkaz v horní části stránky (viz šipka na obrázku).



![Dashboard marchand](assets/fr/11.webp)



*připojení *wallet Lightning**



Klíčový krok při aktivaci prodejního místa: připojte wallet Lightning pro příjem plateb. Rozhraní nabízí několik možností připojení. Upozorňujeme, že některé možnosti (Bitcoin Onchain a Lightning Network) jsou stále ve fázi vývoje a v rozhraní se zobrazují šedě.



![Options de connexion wallet](assets/fr/12.webp)



V tomto návodu používáme připojení Lightning Address, které je kompatibilní s produkty Chivo, Blink Wallet a Strike. Zadejte svůj Lightning Address (formát nom@domaine.com), například od společnosti LN Markets, Alby nebo jiného kompatibilního dodavatele.



![Saisie de la Lightning Address](assets/fr/13.webp)



Po přihlášení je váš účet funkční. Nyní můžete přistupovat k pokladně nebo se vrátit na ovládací panel a konfigurovat další nastavení.



![Connexion réussie](assets/fr/14.webp)



*odkazy na platby** *Odkazy na platby



Nabídka "Platební nástroje" umožňuje přístup k "Žádosti o platbu", která umožňuje vytvářet a spravovat platební odkazy. Tato funkce je užitečná pro vytváření personalizovaných platebních odkazů, které se zasílají e-mailem nebo zprávou: dary, jednorázové platby, vícenásobné platby nebo dokonce platební brány pro ochranu obsahu. Můžete vytvářet různé typy odkazů, které vyhovují vašim obchodním potřebám.



![Liens de paiement](assets/fr/15.webp)



**Konfigurace prodejního terminálu**



Chcete-li přijímat platby v obchodě, otevřete nabídku "Prodejní terminál" v části "Platební nástroje". V této části můžete vytvářet a spravovat své prodejní terminály (počet terminálů závisí na vašem tarifu, viz níže Freemium vs. Business tarify). Kliknutím na tlačítko "Otevřít" otevřete rozhraní pokladního terminálu v prohlížeči.



![Gestion des terminaux](assets/fr/16.webp)




**Generování prodeje**



Na pokladním terminálu se zobrazí číselná klávesnice pro zadání částky prodeje. Zadejte částku v místní měně (např. 500 sats odpovídá 630,74 ARS) a potvrďte stisknutím tlačítka "OK".



![Saisie du montant](assets/fr/17.webp)



Aplikace okamžitě vygeneruje bleskový kód QR a bleskový kód Address pro platbu. Zákazníci mohou QR kód naskenovat pomocí karty wallet nebo použít kartu Bolt na terminálu NFC.



![QR code de paiement](assets/fr/18.webp)



Jakmile platbu obdržíte, zobrazí se potvrzovací obrazovka s přijatou částkou v místní měně a v satoších. Můžete odeslat potvrzení e-mailem, vytisknout lístek nebo okamžitě zahájit nový prodej.



![Paiement encaissé](assets/fr/19.webp)



**Monitorování a řízení**



Všechny transakce jsou zaznamenány na vašem obchodním panelu. Máte k dispozici kompletní sledování tržeb podle období, celkový počet prodejů a podrobnou historii pro vaše účetnictví.



Rozhraní Nastavení nabízí několik konfiguračních karet. Karta "Obecná nastavení" umožňuje spravovat profil obchodníka a oznámení. Karta "Uživatelé" umožňuje přidávat a spravovat přístup k panelu obchodníka pro váš tým (správa více uživatelů podle vašeho plánu). Karta "Development Workspace" (Pracovní prostor pro vývoj) poskytuje přístup ke klíčům API pro pokročilé integrace, zatímco karta "Subscription" (Předplatné) umožňuje spravovat vaše předplatné.



![Paramètres du compte marchand](assets/fr/20.webp)



**Freemium vs Business plány



Tiankii nabízí dva balíčky pro Merchant Dashboard. Plán **Freemium** (zdarma) je vhodný pro začínající firmy s omezeními: jedno prodejní místo, jeden uživatel, měsíční objem omezený na 1 000 USD a žádný přístup k e-commerce konektorům. Plán **Business** (poplatek 0,5 % za transakci) nabízí neomezený počet terminálů, neomezený počet uživatelů, neomezený objem, přístup ke konektorům WooCommerce/Shopify/Cloudbeds a exkluzivní oznámení přes WhatsApp.



![Comparaison plans Freemium et Business](assets/fr/21.webp)



## Výhody a omezení



### Nejdůležitější informace



**Samostatné opatrovnictví**: Své soukromé klíče a plnou kontrolu nad svými prostředky si ponecháte. Žádné riziko zmrazení účtu nebo bankrotu platformy třetí strany.



**Jednoduchost**: NFC platby jednoduchým klepnutím, intuitivní rozhraní bez nutnosti technických znalostí.



**Kompletní ekosystém**: Nástroje pro všechny profily (jednotlivci, prodejci, vývojáři) s modulárními integracemi, které vyhovují vašim potřebám.



**Odborná shoda**: Dodržování předpisů v Salvadoru, soulad s PCI-DSS.



### Omezení



**Blesková omezení**: Vyžaduje trvalé připojení wallet, řízení likvidity pro velké objemy, riziko selhání, pokud je příjemce offline. Tiankii tyto aspekty zmírňuje pomocí integrovaných LSP.



**Závislost na službě SaaS**: Pokud je Tiankii nedostupná, generování faktur je dočasně nemožné (vaše prostředky zůstávají v bezpečí).



**Soukromí**: Tiankii může sledovat metadata transakcí (částky, data). Méně soukromí než u samostatně hostovaných řešení, jako je například server BTCPay.



## Závěr



Tiankii ukazuje, jak může dobře navržená infrastruktura odstranit technické překážky, které brání masovému přijetí Bitcoin jako každodenního platidla. Kombinací síly Lightning Network s neúřednickým přístupem a dostupnými nástroji nabízí tento ekosystém vyváženou cestu mezi finanční suverenitou a snadným používáním.



Pro obchodníky představuje Tiankii příležitost, jak výrazně snížit transakční náklady a zároveň získat přístup k nové zákaznické základně. Pro spotřebitele se díky kartám Lightning Address a NFC stává z Bitcoin praktická měna bez technických složitostí.



Přestože široké přijetí Bitcoin zůstává výzvou vyžadující vzdělání a čas, infrastruktury jako Tiankii ukazují, že technické nástroje již existují. Poslání zjednodušit platby Bitcoin již není vzdálenou vizí, ale realitou dostupnou každému, kdo je ochoten se do toho pustit.



## Zdroje



### Oficiální dokumentace




- [oficiální stránky Tiankii](https://tiankii.com)
- [Centrum nápovědy Tiankii](https://help.tiankii.com)
- [aplikace IBI](https://go.ibi.me)
- [Merchant Dashboard](https://pay.tiankii.com)
- [Velitelské centrum](https://cc.ibi.me)



### Vodítka pro připojení Wallet




- [Connect LNbits](https://help.tiankii.com/portal/en/kb/articles/connect-your-lnbits-wallet)
- [Connect BlueWallet (LNDHub)](https://help.tiankii.com/portal/en/kb/articles/connect-your-lndhub-bluewallet)
- [Connect Alby Wallet](https://help.tiankii.com/portal/en/kb/articles/connect-your-alby-wallet)
- [Connect Strike Wallet](https://help.tiankii.com/portal/es/kb/articles/como-vincular-strike-wallet)



### Společenství




- [Lightning Network Plus](https://lightningnetwork.plus) - Vzdělávací zdroj Lightning
- [Bitcoin Beach](https://www.bitcoinbeach.com) - Salvadorská iniciativa pro oběhové hospodářství Bitcoin



### Související nástroje




- [Blink Wallet](https://blink.sv) - Doporučujeme kompatibilní s Wallet Lightning
- [LNbits](https://lnbits.com) - Samostatně hostované řešení wallet
- [Standardní karta Bolt](https://github.com/boltcard) - Technické specifikace karet NFC