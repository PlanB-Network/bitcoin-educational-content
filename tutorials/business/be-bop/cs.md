---
name: be-BOP
description: Praktický průvodce zpeněžením vašeho podnikání pomocí be-BOP
---

![cover-bebop](assets/cover.webp)



**be-BOP** je platforma pro elektronické obchodování určená pro podnikatele, kteří chtějí prodávat online i offline, zcela samostatně a přijímat platby v Bitcoin, prostřednictvím bankovního účtu a v hotovosti. Řešení je také užitečné pro jakýkoli typ organizace, která chce vybírat dary nebo zpeněžit své různé aktivity.



Řešení je jednoduché, lehké a autonomní. Umožňuje vytvořit internetový obchod i v prostředí, kde jsou tradiční finanční služby omezené nebo chybí. Systém **be-BOP** byl totiž navržen tak, aby mohl efektivně fungovat s přístupem k bankám i bez něj a jako platební infrastrukturu využíval Bitcoin.



V tomto návodu vás krok za krokem provedeme:





- Vytvořte si svůj první internetový obchod s **be-BOP**
- Přizpůsobte si svou vitrínu a své produkty
- Konfigurace dostupných platebních metod
- Pochopte osvědčené postupy pro efektivní prodej online pomocí **be-BOP**



Tento výukový program nevyžaduje pokročilé technické dovednosti. Je určen vývojářům i řemeslníkům, obchodníkům, družstvům nebo podnikatelům, kteří se chtějí pustit do suverénního a odolného digitálního obchodu.



## Předpoklady pro instalaci be-BOP na vlastní server



Než začnete instalovat be-BOP, ujistěte se, že máte k dispozici následující technickou infrastrukturu. Tyto Elements jsou nezbytné pro správné fungování platformy:



### Úložiště kompatibilní s S3



be-BOP používá ke správě souborů (například obrázků produktů) systém ukládání. To vyžaduje přístup ke službě S3, například:





- [MinIO](https://min.io/) na vlastním serveru
- Amazon S3 (AWS)
- Úložiště objektů Scaleway



Je třeba nakonfigurovat kbelík a zadat následující informace:





- S3_BUCKET**: název kbelíku
- S3_ENDPOINT_URL**: přístupový odkaz ke službě S3
- S3_KEY_ID** a S3_KEY_SECRET: vaše přístupové kódy
- S3_REGION**: region vaší služby S3



### Databáze MongoDB v režimu ReplicaSet



be-BOP používá MongoDB k ukládání dat o obchodech, uživatelích, produktech a dalších dat.



Máte dvě možnosti:





- Lokální instalace MongoDB s povoleným režimem **ReplicaSet**
- Použijte online službu, například **MongoDB Atlas**



Budete potřebovat následující proměnné:





- MONGODB_URL**: připojení k databázi Address
- MONGODB_DB**: název databáze



## Prostředí Node.js



be-BOP pracuje s Node.js. Ujistěte se, že máte **Node.js** verze 18 nebo vyšší a povolený **Corepack** (potřebný pro správu správců balíčků, jako je pnpm). Příkaz, který je třeba spustit, je `corepack enable`



### Nainstalovaný systém Git LFS



Některé prostředky (například velké obrázky) jsou spravovány prostřednictvím systému Git LFS (Large File Storage). Ujistěte se, že máte v počítači nainstalovaný systém Git LFS pomocí příkazu `git lfs install`. Jakmile jsou tyto předpoklady splněny, můžete přejít k dalšímu kroku: stažení a konfiguraci be-BOP.



**Poznámka:** Technický průvodce nasazením softwaru je k dispozici v samostatném tutoriálu.



## Vytvoření účtu Super-Admin



Při prvním spuštění systému be-BOP je vytvořen účet **Super Admin**. Tento účet má všechna oprávnění potřebná ke správě funkcí back-office. Chcete-li vytvořit účet, postupujte podle následujících kroků:





- Přejděte na `všechny stránky/admin/přihlášení`
- Vytvoření účtu superadmina se zabezpečeným přihlašovacím jménem a heslem



Tento účet vám umožní přístup ke všem funkcím back-office. Po jeho vytvoření se můžete přihlásit zadáním uživatelského jména a hesla.



![login](assets/fr/001.webp)



## Konfigurace a zabezpečení Back-Office



Před konfigurací připojení k back-office Interface je třeba vytvořit jedinečné připojení Hash. To poskytuje ochranu před záškodníky, kteří se snaží ukrást odkaz na připojení k vašemu správci Interface.



Chcete-li vytvořit Hash, přejděte do `/admin/Settings`. V části věnované zabezpečení (např. "Admin Hash") definujte jedinečný řetězec (Hash). Po registraci bude upravena adresa URL back-office (např. `/admin-yourhash/login`), aby byl omezen přístup neoprávněným osobám.



![hash-login](assets/fr/002.webp)



2.2. Aktivujte režim údržby (je-li to nutné)



Ještě v /admin/Nastavení (Nastavení > Obecné přes grafiku Interface) zaškrtněte možnost "povolit režim údržby" v dolní části stránky.



![maintenance-mode](assets/fr/003.webp)



V případě potřeby můžete zadat seznam autorizovaných adres IPv4 (oddělených čárkami), aby byl během údržby umožněn přístup k front office. Back office zůstává přístupný správcům.



![ip-bebop](assets/fr/004.webp)



## Nastavení komunikace



Chcete-li, aby be-BOP zasílal oznámení (např. o objednávkách, registracích nebo systémových zprávách), musíte nakonfigurovat alespoň jednu komunikační metodu. K dispozici jsou dvě možnosti: e-mail (SMTP) nebo Nostr.



### Konfigurace SMTP (e-mail)



be-BOP může odesílat e-maily prostřednictvím serveru SMTP. Budete potřebovat platné přihlašovací údaje SMTP, které často poskytuje e-mailová služba (např. Mailgun, Gmail atd.).



Tady je to, co byste měli vědět:



SMTP_HOST: SMTP server Address (např. smtp.mailgun.org)



SMTP_PORT: port, který se má použít (často 587 nebo 465)



SMTP_USER: vaše uživatelské jméno (obvykle e-mail Address)



SMTP_PASSWORD: vaše heslo nebo klíč API



SMTP_FROM: e-mail Address, který se zobrazí jako odesílatel




### Konfigurace Nostr



be-BOP umožňuje odesílat oznámení prostřednictvím protokolu Nostr, decentralizované infrastruktury pro zasílání zpráv. K tomu potřebujete generate nebo Supply soukromý klíč Nostr (NSEC). Tento klíč generate můžete získat přímo prostřednictvím Interface v be-BOP, v části věnované Nostr. Pokud jsou tyto Elements správně nakonfigurovány, bude be-BOP schopen automaticky odesílat zprávy a upozornění vašim uživatelům.



## Kompatibilní platební metody



be-BOP je kompatibilní s několika platebními řešeními, což vám umožní nabídnout svým zákazníkům větší flexibilitu. Zde je uvedeno, co potřebujete k nastavení způsobu platby, který vám nejlépe vyhovuje.



### Bitcoin Onchain



be-BOP umožňuje jednoduše a bezpečně přijímat platby Bitcoin přímo na Blockchain (On-Chain).



**Kroky konfigurace:**





- Přejděte do nabídky **Nastavení plateb**
- Kliknutím na **Bitcoin Nodeless** získáte přístup k parametrům platby On-Chain.
- Vyplňte následující pole:



| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)



**Tip:** Chcete-li získat svůj rozšířený veřejný klíč (Zpub), můžete se podívat do pokročilých nastavení Bitcoin Wallet (Sparrow wallet, BlueWallet, Specter atd.). Pokud hodláte používat historii transakcí, ujistěte se, že váš Wallet není **pouze pro čtení**.



### Lightning Network



be-BOP může díky Lightning Network přijímat také okamžité platby Bitcoin. V současné době jsou k dispozici dvě možnosti konfigurace:



**Fénixd**



Přejděte do nabídky `Nastavení plateb` a klikněte na `Fénixd`



![phoenixd](assets/fr/006.webp)



Poté budete muset zadat **heslo nebo ověření token**, které vás připojí k vaší instanci Phoenixd, backendu vyvinutému společností Acinq, který vám umožní spravovat platby Lightning pomocí vlastního uzlu, ale bez složité správy platebních kanálů.



**Švýcarská mzda Bitcoin**



Pokud nechcete spravovat uzel Lightning sami, **Swiss Bitcoin Pay** je řešení připravené k použití a snadno konfigurovatelné, které je ideální pro zahájení přijímání plateb Lightning bez složité infrastruktury.



Kroky konfigurace:





- V nabídce "Nastavení plateb" klikněte na `Swiss Bitcoin Pay`
- Přihlaste se ke svému účtu Swiss Bitcoin Pay (nebo si ho vytvořte, pokud ho ještě nemáte).
- Zadejte klíč API dodaný společností Swiss Bitcoin Pay a klikněte na tlačítko "Uložit"



Po nastavení bude be-BOP automaticky generate Lightning vystavovat faktury pro vaše zákazníky a vy budete dostávat platby přímo na svůj účet Swiss Bitcoin Pay. Toto řešení je ideální pro uživatele, kteří se chtějí vyhnout technické složitosti osobního uzlu a zároveň přijímat rychlé a levné platby.



![swissbtcpay](assets/fr/007.webp)



### PayPal



Kromě služby Bitcoin umožňuje be-BOP přijímat platby v hotovosti také prostřednictvím služby PayPal, která je známým a hojně využívaným mezinárodním řešením.



Kroky konfigurace:





- Přejděte do nabídky `Nastavení platby`
- Klikněte na `PayPal
- V účtu Paypal (sekce pro vývojáře) zadejte `Ident ID klienta` a `Tajné jméno`
- Zvolte požadovanou měnu (např. **USD**, **EUR**, **XOF** atd.)
- Klikněte na `uložit



![paypal](assets/fr/008.webp)



**Poznámka:** Abyste mohli tyto identifikátory generate používat, musíte mít firemní účet PayPal. Můžete je získat prostřednictvím portálu [pro vývojáře] (https://developer.paypal.com)



### SumUp



Software nyní integruje platební řešení **SumUp**, které vám umožní jednoduše, bezpečně a efektivně přijímat platby kreditními kartami. Abyste mohli tuto funkci využívat, je nutná počáteční konfigurace. Zde jsou uvedeny kroky, které je třeba dodržet, očíslované pro přehlednou a postupnou implementaci:





- Začněte zadáním svého klíče **API Key**, důvěrného klíče, který vám společnost SumUp poskytla při vytváření účtu vývojáře. Ten vytvoří bezpečné spojení mezi vaším účtem SumUp a softwarem.
- Vyplňte pole `Kód obchodníka` jedinečným kódem, který identifikuje vaši firmu v rámci platformy SumUp. Tento kód je nezbytný pro přiřazení transakcí k vašemu podniku.
- V poli `Měna` vyberte hlavní měnu, kterou používáte pro své transakce (např. **EUR**, **USD**, **CDF** atd.).
- Po správném vyplnění všech polí klikněte na tlačítko `Uložit` a uložte nastavení. Systém poté vytvoří spojení s vaším účtem SumUp a váš software bude připraven přijímat platby.



![payment-sumup](assets/fr/009.webp)



Po této konfiguraci bude integrace **SumUp** aktivní a funkční, což vám umožní rychle vybírat hotovost a sledovat transakce přímo ze softwaru.



### Proužek



be-BOP také nabízí plnou integraci s **Stripe**, jednou z nejoblíbenějších platforem pro online platby. Stripe umožňuje přijímat online platby prostřednictvím kreditních karet, digitálních Wallet a několika dalších platebních metod. Zde najdete návod, jak ji aktivovat:





- Zadejte **tajný klíč** uvedený na ovládacím panelu služby Stripe.
- Vyplňte pole **Veřejný klíč**, které rovněž poskytuje společnost Stripe.
- Vyberte **hlavní měnu**.
- Uložte konfiguraci a klikněte na tlačítko `Uložit`.



![payment-stripe](assets/fr/010.webp)



⚠️ **Upozornění:** Pro správnou konfiguraci možností fakturace v **be-BOP** je nezbytné znát režim DPH, který se na vaši činnost vztahuje (např.: prodej v režimu DPH v zemi prodávajícího, osvobození od daně podle odůvodnění nebo prodej v režimu DPH v zemi kupujícího).



## Konfigurace měny



**be-BOP** nabízí pokročilou správu měn a je přizpůsoben prostředí s více měnami a specifickým účetním požadavkům. Pro zajištění konzistence finančních operací a výkaznictví je nezbytné správně nakonfigurovat různé měny používané v systému. Zde jsou uvedeny kroky, kterými je třeba se při této konfiguraci řídit:





- Vyberte **hlavní měnu** (`Hlavní měna`)
- Vyberte `Druhotná měna
- Definice **referenční měny** (`Cenová referenční měna`)
- Uveďte `Účetní měna



Po správném nastavení všech měn software zajišťuje automatický a přesný převod transakcí ve více měnách při zachování přísné účetní konzistence.



![settings-currencies](assets/fr/011.webp)



## Konfigurace přístupu k obnovení prostřednictvím e-mailu nebo Nostr



Ještě v `/admin/settings` se přes modul **ARM** ujistěte, že účet superadmina obsahuje **email Address** nebo **recovery pub**, což usnadní postup v případě zapomenutí hesla.



![settings-users](assets/fr/012.webp)



## Nastavení jazyka



Software nabízí více jazyků, aby se přizpůsobil mezinárodnímu publiku a zvýšil uživatelský komfort. Pro aktivaci vícejazyčné funkce je důležité nakonfigurovat dostupné jazyky a definovat **výchozí jazyk**.



![settings-languages](assets/fr/13.webp)



## Konfigurace Interface a identity v be-BOP



**be-BOP** poskytuje návrhářům všechny nástroje, které potřebují k návrhu webových stránek. Prvním krokem je otevření sekce `/Admin > Merch > Layout` v nastavení. Začněte konfigurací **Horního pruhu**, **Navigačního panelu** a **Zápatí**.



### Le Top Bar



Konfigurace **Top Bar** umožňuje přizpůsobit vizuální identitu softwaru zobrazením klíčových informací hned na prvním řádku Interface. To posiluje rozpoznatelnost značky a poskytuje uživatelům jasný kontext.



#### Kroky konfigurace:





- Do pole `Brand name` zadejte název své společnosti, organizace nebo produktu. Tento název se zobrazí v horní části Interface a bude představovat vaši hlavní vizuální identitu.
- Uveďte název webové stránky**: zvolený název by měl shrnovat účel platformy. Tento název se může objevit v záhlaví nebo na kartě prohlížeče.
- Přidat popis webové stránky**: zde zadejte stručný popis své iniciativy. Tento popis pomáhá kontextualizovat nástroj pro uživatele a může být také použit pro účely SEO.



Po zadání těchto informací se na **Horním panelu** zobrazí jasná, profesionální a ucelená prezentace vašeho řešení.



#### Odkazy na horním panelu



Sekce `Odkazy` na horním panelu umožňuje přidávat zkratky na důležité stránky v aplikaci nebo na externí weby. Tyto odkazy se zobrazují přímo v horním panelu a nabízejí uživatelům rychlý a strukturovaný přístup.



#### Kroky konfigurace:





- Zadejte název odkazu (Text)**: do pole `Text` zadejte název nebo označení odkazu tak, jak se bude zobrazovat (např. Home, Contact, Help...).
- Uveďte odkaz Address (Url)**: do pole `Url` zadejte celý odkaz Address cílové stránky (interní nebo externí).
- V případě potřeby přidejte další odkazy**: každý konfigurační řádek umožňuje přidat další odkaz pomocí polí `Text` a `Url`.
- Uložení odkazů**: Po zadání všech odkazů je uložte kliknutím na tlačítko "Přidat odkaz na horní lištu".



Tato konfigurace vám umožní nabídnout přehlednou, plynulou a přístupnou navigaci po různých částech webu nebo k doplňkovým zdrojům.



![settings-topbar](assets/fr/014.webp)



### La Nav Bar



V části **Navigační panel** můžete nakonfigurovat hlavní navigační nabídku systému be-BOP, která se obvykle nachází na boku nebo v horní části okna Interface. Tato nabídka vede uživatele k různým stránkám a funkcím aplikace. Konfigurace odkazů je jednoduchá a intuitivní. Funguje to následovně:





- Zadejte název odkazu (`Text`)**: na konfiguračním řádku začněte vyplněním pole `Text`. To odpovídá názvu odkazu zobrazeného v navigačním panelu (příklady: *Dashboard*, *Users*, *Settings*...).
- Zadejte odkaz Address (`Url`)**: vedle pole `Text` se nachází pole `Url`. Do tohoto pole zadejte číslo Address stránky, na kterou má odkaz přesměrovat. Může se jednat o interní cestu nebo odkaz na externí stránku.
- V případě potřeby přidejte více odkazů**: pod prvním řádkem jsou k dispozici nová pole `Text` a `Url` pro přidání libovolného počtu odkazů. Každý řádek představuje další navigační odkaz.
- Uložení odkazů**: Po zadání všech údajů Elements klikněte na tlačítko `Přidat odkaz na navigační lištu`, čímž uložíte a zobrazíte výsledky na navigační liště.



Tato konfigurace umožňuje efektivní strukturování přístupu k různým částem softwaru, což zlepšuje ergonomii a uživatelský komfort.



![navbar](assets/fr/015.webp)



### Zápatí



Sekce **Patička** umožňuje přizpůsobit patičku softwaru a přidat do ní užitečné informace nebo odkazy. Před konfigurací odkazů začněte aktivací konkrétní možnosti:





- Povolit zobrazení štítku "Powered by be-BOP "**: aktivujte tlačítko `Zobrazit Powered by be-BOP`, aby se tento štítek zobrazil v zápatí.
- Zadejte název odkazu (`Text`)**: vyplňte pole `Text`, které odpovídá znění odkazu v zápatí (příklady: *Podmínky*, *Soukromí*, *Kontakt*...).
- Uveďte odkaz Address (`Url`)**: do pole `Url` zadejte odkaz Address cílové stránky (interní nebo externí).
- V případě potřeby přidejte další odkazy**: pomocí dalších řádků vytvořte libovolný počet odkazů.
- Uložení odkazů**: odkazy uložíte kliknutím na tlačítko "Přidat odkaz v zápatí".



![footer](assets/fr/016.webp)



### Vizuální personalizace



**⚠️ Nezapomeňte nastavit loga pro světlé a tmavé motivy a také favikonu prostřednictvím** `Admin > Merch > Pictures`.



Zde se dozvíte, jak přizpůsobit vzhled webu:



#### Přejít do sekce Obrázky



Menu `Admin` > `Merch` > `Obrázky`.



#### Přidání nového obrázku



Klikněte na `Nový obrázek`.



#### Výběr místního souboru



Klikněte na `Vybrat soubory` a vyberte obraz z disku Hard.



#### Vyberte soubor, který chcete importovat



Dvakrát klikněte na obrázek, který chcete importovat (světlé logo, tmavé logo nebo favicon).



#### Pojmenování obrázku



Vyplňte pole `Název obrázku`.



#### Přidat obrázek



Kliknutím na tlačítko `Přidat` dokončíte import.



![pictures](assets/fr/017.webp)



### Nastavení identity prodávajícího



#### Nastavení identity



Tato část je přístupná přes `Admin > Identita` (nebo `Nastavení > Identita`) a umožňuje konfigurovat administrativní a právní informace o vaší společnosti.



#### Právní informace





- Obchodní název**: oficiální název společnosti.
- IČO**: právní identifikátor nebo registrační číslo (RCCM, SIRET...).



#### Business Address





- Street**: poštovní číslo Address (ulice, číslo...).
- Země**: země.
- Stát**: provincie nebo region.
- Město**: město.
- PSČ**: poštovní směrovací číslo.



#### Kontaktní informace





- E-mail**: profesionální e-mail Address.
- Telefon**: telefonní číslo společnosti.



#### Bankovní účet





- Jméno držitele účtu**: jméno držitele účtu.
- Držitel účtu Address**: Address držitele.
- IBAN**: Číslo mezinárodního bankovního účtu.
- BIC**: SWIFT/BIC kód.



![bank-account](assets/fr/019.webp)



#### Fakturace





- Kliknutím na `Vyplnit hlavními údaji obchodu` předvyplníte údaje.
- Velmi pravdivé informace o vydavateli**: pole pro právní/daňové informace viditelné na fakturách.
- Kliknutím na tlačítko `Aktualizovat` uložte změny.



**Poznámka:** podle svých potřeb můžete zadat i další informace, které se mají zobrazit na displeji Invoice.



![vat](assets/fr/019.webp)



![issuer-info](assets/fr/020.webp)



#### Fyzický obchod Address



Pro ty, kteří mají fyzický obchod, přidejte konkrétní plný Address v `Admin > Nastavení > Identita` nebo ve vyhrazené sekci. To umožní jeho zobrazení na oficiálních dokladech a v případě potřeby i v zápatí.



![seller-id](assets/fr/021.webp)



## Řízení produktů



### Vytvoření nového produktu



Chcete-li přidat nebo upravit produkt, přejděte na `Admin > Merch > Products`. Vyplňte následující pole:



#### Základní informace





- Název produktu**: název produktu (např. *BOP T-shirt limited edition*).
- Slimák**: Např. `tshirt-bop-edition-limitee`).
- Alias** *(nepovinné)*: užitečné pro rychlé přidání do košíku prostřednictvím vyhrazeného pole.



![product-config](assets/fr/028.webp)



#### Stanovení cen





- Cena**: cena produktu (např. `25,00`).
- Cena Měna**: měna (EUR, USD, BTC atd.).
- Speciální produkty**:
  - jedná se o bezplatný produkt.
  - jedná se o produkt, za který se platí.



#### Možnosti produktu





- Jednotlivý produkt (`samostatný`)**: v jedné objednávce je možné přidat pouze jeden produkt (např. dar, vstupenku).
- Výrobek s variantami**:
  - Nezkoušejte `Standalone`.
  - Zaškrtněte políčko `Výrobek má lehké odchylky (bez rozdílu skladových zásob)`.
  - Přidat:
    - Název** (např. *Velikost*),
    - Hodnoty** (např.: S, M, L, XL),
    - Případné cenové rozdíly** (např.: `+2 USD` za XL).



![product-details](assets/fr/029.webp)



## Řízení zásob



### Rozšířené možnosti při vytváření produktu (Sklad, Dodávka, Lístky atd.)



#### Výrobek s omezenou zásobou



Pokud váš produkt není k dispozici v neomezeném množství, zaškrtněte políčko `The product has a limited stock`. Tím aktivujete automatické sledování zbývajícího množství. Po zaškrtnutí tohoto políčka se zobrazí pole s označením **dostupné zásoby**.



Systém spravuje:





- Rezervované zásoby** → produkty v košících, které ještě nebyly zaplaceny
- Prodané zásoby** → již zakoupené produkty



**Čas rezervace koše**: Když si zákazník přidá produkt do košíku, je "rezervován" na omezenou dobu. Tuto dobu můžete upravit v: (hodnota v minutách)



#### Produkt, který má být dodán?



Zaškrtněte políčko `Výrobek má fyzickou součást, která bude odeslána na adresu zákazníka Address`. To je užitečné pro všechny produkty, které mají být zasílány fyzicky (knihy, trička atd.)



#### Další možnosti





- Vstupenka**: zaškrtněte, pokud je produkt vstupenkou na událost
- Rezervace**: zkontrolujte, zda se jedná o rezervační slot (např.: sezení, schůzka)



![product-options](assets/fr/030.webp)



### Nastavení akce (dole)



Tato část určuje **kde** a **jak** si lze produkt prohlédnout a zakoupit:



| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Zaškrtněte pouze kanály, které chcete používat.



## Vytváření a přizpůsobení stránek a widgetů CMS



### Povinné stránky CMS



Přejděte na `Admin > Merch > CMS`. Zobrazí se seznam existujících stránek a můžete přidat nové pomocí **Přidat stránku CMS**.



Stránky CMS jsou důležité pro:





- Informujte návštěvníky (např. podmínky používání)
- Dodržování zákonů (např. zásady ochrany osobních údajů)
- Vysvětlení některých funkcí obchodu (např. výběr IP, 0% DPH)



Podle potřeby můžete přidat další stránky:





- O nás / Kdo jsme
- Podpořte nás / Dary
- ČASTO KLADENÉ DOTAZY
- Kontakt
- atd.



**Tip: Kliknutím na každý odkaz nebo ikonu můžete upravit **obsah**, **název** nebo **viditelnost** každé stránky.



### Rozvržení a grafika Elements



Přejít na: `Admin > Merch > Layout`. Můžete si přizpůsobit vizuální stránku Elements:



![product-options](assets/fr/032.webp)



#### Horní lišta





- Úprava nebo odstranění odkazů (např.: DOMŮ, O NÁS,...)
- Navigace mezi klíčovými částmi webu



#### Navigační panel (hlavní navigační panel)





- V šedé oblasti pod horní lištou
- Obsahuje rychlý přístup k: `Konfigurace`, `Nastavení plateb`, `Transakce`, `Správa uzlů`, `Widgety` atd.
- Pouze ředitelé



#### Zápatí





- Lze upravit z `Admin > Merch > Layout`
- Obsahuje: kontaktní informace, užitečné odkazy, právní upozornění..



#### Přizpůsobení vizuálních prvků



Přejít na: `Admin > Merch > Pictures`



Můžete:





- Změna **hlavního loga**
- Úprava nebo přidání rozvržení **obrázků**



#### Popis webu



V závislosti na tématu lze také upravovat v části `Obrázky` a umožňuje zobrazit v záhlaví nebo zápatí **shrnutí nebo slogan**.



**Poznámka:** to vám umožní přizpůsobit vzhled identitě vaší značky (vzdělávací, komerční nebo komunitní).



### Integrace widgetů do stránek CMS



Widgety** obohacují stránky CMS o dynamické nebo vizuální prvky Elements.



#### Vytvoření widgetu



Přejít na: `Admin > Widgets`



Příklady dostupných widgetů:





- Výzvy**: výzvy nebo mise
- Štítky**: kategorie nebo klíčová slova
- Posuvníky**: karusely obrázků
- Specifikace**: Tabulky specifikací
- Formuláře**: formuláře (kontakt, zpětná vazba atd.)
- Odpočítávání**: časovače
- Galerie**: galerie obrázků
- Žebříčky**: hodnocení uživatelů



![widgets](assets/fr/033.webp)



#### Integrace do stránek CMS



V obsahu stránek CMS používejte **šortkové kódy**:



| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Aktuální parametry**:





- `slug`: jedinečný identifikátor widgetu
- `display=img-1`: obrázek specifický pro produkt
- `width`, `height`, `fit`: rozměry a styl obrázku
- autoplay=3000`: čas v ms mezi dvěma slajdy



**Výhody**:





- Snadné vkládání (kopírování a vkládání)
- Dynamický: jakákoli změna widgetu se automaticky projeví
- Není vyžadován žádný vývojář



## Správa objednávek a podávání zpráv



### Sledování objednávek



Chcete-li zobrazit a spravovat minulé objednávky, přejděte na: `Admin > Transakce > Objednávky`



Zde najdete **úplný seznam objednávek** zadaných na vašich stránkách.



![orders](assets/fr/034.webp)



#### Vizualizace a vyhledávání



Interface umožňuje vyhledávat a filtrovat zakázky podle několika kritérií:





- číslo objednávky: číslo objednávky
- alias produktu: identifikátor nebo název produktu
- payment Mean": použitá platební metoda (karta, krypto atd.)
- `Email`: e-mail zákazníka



Tyto filtry usnadňují rychlé vyhledávání a cílenou správu.



#### Podrobnosti o každé objednávce



Kliknutím na objednávku získáte přístup ke kompletnímu souboru obsahujícímu:





- Objednané produkty
- Informace pro zákazníky
- Dodávka Address (pokud je k dispozici)
- Veškeré poznámky spojené s objednávkou



#### Možné akce na objednávce



Můžete:





- Potvrzení objednávky (pokud čeká na vyřízení)
- Zrušit objednávku (v případě problému nebo požadavku zákazníka)
- Přidat **nálepky** (pro vnitřní organizaci)
- Konzultace / přidání **interních poznámek**



**Poznámka:** tato část je nezbytná pro dobrou logistiku a vztahy se zákazníky.



### Vykazování a export



Přístup ke statistikám prodeje a plateb:


správce > Nastavení > Hlášení



![reporting](assets/fr/035.webp)



Zde najdete přehled o své firmě v podobě **měsíčních a ročních výkazů**.



#### Obsah zprávy



Zprávy jsou rozděleny do oddílů:





- Detail objednávky**: počet objednávek, stav (potvrzené, zrušené, čekající), vývoj
- Detail produktu**: prodané produkty, množství, oblíbené produkty
- Detail platby**: vybrané částky, rozdělení podle způsobu platby



#### Export dat



Každá sekce obsahuje tlačítko **Export CSV**, které umožňuje:





- Stažení dat ve formátu CSV
- Otevřete je v aplikaci Excel, Google Sheets atd.
- Archivace pro administrativní nebo účetní účely
- Použijte je pro interní zprávy



**Poznámka:** ideální pro sledování výkonnosti, účetnictví a prezentace.



## Konfigurace služby Nostr Messaging (volitelné)



![nostr-config](assets/fr/036.webp)



Platforma podporuje protokol **Nostr** pro některé pokročilé funkce:





- Decentralizovaná oznámení
- Přihlášení bez hesla
- Interface lehká administrativa



### Generování a přidání soukromého klíče Nostr



Přejít na:


admin > Správa uzlů > Nostr





- Pokud nemáte nsec**, klikněte na **Vytvořit nsec**.
- Systém generate to dokáže automaticky.
- Případně můžete použít existující klíč (např. od Damusu nebo Ametystu).



Další:





- Zkopírování klíče `nsec`
- Přidejte jej do souboru `.env.local` (nebo `.env`): ```env NOSTR_PRIVATE_KEY=YourNsecIciKey



### Funkce aktivované pomocí Nostr



Po konfiguraci je k dispozici několik funkcí:



**Oznámení prostřednictvím služby Nostr**





- Odesílání upozornění na objednávky, platby nebo systémové události
- Pro správce nebo uživatele



**Interface lehká administrativa**





- Přístupné prostřednictvím klienta Nostr
- Umožňuje rychlou a mobilní správu



**Připojení bez hesla**





- Přihlášení pomocí zabezpečeného odkazu (zaslaného přes Nostr)
- Větší bezpečnost a plynulost uživatelů



## Přizpůsobení designu a tématu



Chcete-li přizpůsobit vzhled svého obchodu grafické kartě, přejděte na: `Admin > Merch > Theme`



Zde najdete všechny možnosti pro **vytvoření** a **konfiguraci** vlastního motivu.



### Vytvoření tématu



![theme](assets/fr/037.webp)



Při vytváření nebo úpravě motivu můžete definovat:





- Barvy**: pro tlačítka, pozadí, text, odkazy atd.
- Písma**: výběr řezů písma pro nadpisy, odstavce a nabídky
- Grafické styly**: okraje, okraje, mezery, blokové tvary



### Přizpůsobitelné sekce



Každou část webu lze upravit samostatně:





- Záhlaví**: horní navigační panel
- Tělo**: hlavní obsah
- Zápatí**: spodní část stránky



**Poznámka:** tato granularita zajišťuje konzistenci vizuální stránky a identity vaší značky.



### Aktivace tématu



Jakmile je téma nakonfigurováno:





- Klikněte na **Uložit**
- Aktivujte jej jako **hlavní motiv obchodu**



**Poznámka:** aktivní téma je to, které bude viditelné pro návštěvníky.



## Konfigurace e-mailových šablon



Platforma umožňuje přizpůsobit e-maily automaticky zasílané uživatelům. Přejděte na: > Nastavení > Šablony`



![emails-templates](assets/fr/038.webp)



### Vytváření / úpravy šablon



Každý e-mail (potvrzení objednávky, zapomenuté heslo atd.) má:





- Předmět**: předmět e-mailu (např. "Vaše objednávka byla potvrzena")
- Tělo HTML**: Obsah HTML zobrazený v e-mailu



**Poznámka:** můžete vkládat text, obrázky, odkazy atd. podle potřeby.



### Použití dynamických proměnných



Chcete-li, aby e-maily byly dynamické, vložte proměnné, například:





- `{orderNumber}}`: nahrazeno skutečným číslem objednávky
- `{invoiceLink}}`: odkaz na Invoice
- `{websiteLink}}`: URL vaší webové stránky



**Poznámka:** tyto značky jsou při odeslání automaticky nahrazeny.



### Pokročilé tipy





- Vytvářejte e-maily, které jsou **reaktivní** pro snadné čtení na mobilních zařízeních
- Přidání **akčních tlačítek** (platba, stažení, sledování objednávky)
- Otestujte své e-maily tím, že je před zveřejněním odešlete sami sobě



## Konfigurace konkrétních značek a widgetů



### Správa štítků



Značky lze použít ke strukturování a obohacení obsahu. Chcete-li k nim získat přístup: můžete si je otevřít: `Admin > Widgety > Tag`



![tags-config](assets/fr/039.webp)



### Vytvoření značky



Vyplňte následující pole:





- Tag Name**: zobrazený název tagu
- Slug**: jedinečný identifikátor (bez mezer a diakritiky)
- Tag Family**: seskupuje značky podle kategorií



![targsconfig](assets/fr/040.webp)



#### Dostupné rodiny:





- tvůrci`: autoři nebo producenti
- maloobchodníci: prodejci nebo prodejní místa
- `Temporal`: období nebo data
- události: přidružené události



### Nepovinná pole



Tato pole lze použít k obohacení značky, jako by se jednalo o stránku s obsahem:





- Název
- Podtitul
- Krátký** obsah
- Celý obsah** (ve francouzštině)
- CTA** (akční tlačítka)



### Používání značek



Tagy mohou být:





- Přiděleno produktům
- Integrace do stránek CMS pomocí značky: [Tag=slug?display=var-1]



## Konfigurace souborů ke stažení



Nabídka dokumentů ke stažení pro vaše zákazníky: `Admin > Merch > Files`



### Přidání souboru



1. Klikněte na **Nový soubor**


2. Informovat:




   - Název souboru** (např. *Instalační příručka*)
   - Soubor k nahrání** (PDF, obrázek, Word...)



**Poznámka:** po přidání platforma automaticky vytvoří **trvalý odkaz**.



### Použití odkazu



Tento odkaz pak lze vložit do:





- Stránka CMS** (jako textový odkaz nebo tlačítko)
- **e-mailový klient** (prostřednictvím šablony)
- **produktový list** (např. manuál ke stažení)



Je ideální pro poskytování *uživatelských příruček, technických návodů, produktových listů...* bez nutnosti externího hostingu.



## Nostr-bot



Platforma nabízí pokročilou integraci s protokolem **Nostr** prostřednictvím automatizovaného bota.



Přejděte na: Správa uzlů > Nostr



### Hlavní funkce



#### Správa relé





- Přidání nebo odebrání **relé** používaných botem
- Optimalizace **dosahu** a **spolehlivosti** odesílaných zpráv



#### Automatická úvodní zpráva





- Aktivace automatické zprávy při **první interakci uživatele**
- Ideální pro:
  - Představení služby
  - Odeslání užitečného odkazu (např. FAQ, kontakt, objednávka)



#### Certifikace vašeho `npub





- Přidání **loga** a **veřejného názvu**
- Odkaz na **ověřenou webovou doménu**
- Zvyšuje důvěryhodnost a rozpoznatelnost vaší identity Nostr



### Případy použití Nostr-bot





- Zasíláme vám **potvrzení objednávky**
- Automatická reakce na **události (např. novou objednávku)**
- Vytvoření **decentralizované interakce se zákazníky**



## Přetížení překladových štítků



be-BOP je vícejazyčný (FR, EN, ES...), ale překlady si můžete přizpůsobit svým potřebám.



Chcete-li tak učinit, přejděte na: `Nastavení > Jazyk`



### Načítání a úpravy



Překladové soubory jsou ve formátu JSON. Můžete:





- Stáhnout** jazykové soubory
- Upravit** stávající texty
- Přidejte** vlastní překlady



Odkaz na původní soubory:


[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations](https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)



**Příklad:** nahraďte `Přidat do košíku` výrazem `Přidat do košíku` nebo `Přistoupit`.



## Týmová práce a prodejní místa (POS)



### Správa uživatelů a přístupových práv



#### Vytváření rolí



Přejít na: `Admin > Nastavení > ARM`



Kliknutím na **Vytvořit roli** vytvoříte roli (např. `Super Admin`, `POS`, `Kontrolor vstupenek`).



Každá role obsahuje:





- přístup k zápisu**: přístup k zápisu
- přístup pro čtení**: přístup pro čtení
- zakázaný přístup**: sekce interdites



#### Vytvoření uživatele



Ve stejné nabídce `Admin > Nastavení > ARM` přidejte uživatele s:





- přihlášení
- alias
- obnovení e-mailu
- (nepovinné) `recovery npub` pro připojení přes Nostr



Přiřazení dříve definované role.



![pos-users](assets/fr/045.webp)



Uživatelé, kteří mají přístup pouze pro čtení**, uvidí nabídky v *italic* a nebudou moci měnit obsah.



## Konfigurace prodejního místa (POS)



### Přiřazení role POS



Chcete-li uživateli přidělit přístup k pokladně, přiřaďte roli `Point of Sale (POS) ` v: `Admin > Config > ARM`



Může se připojit prostřednictvím zabezpečené adresy URL: `/pos` nebo `/pos/touch`



### Specifické funkce pokladen



Be-BOP nabízí službu Interface určenou pro fyzický prodej (obchod, událost atd.).



#### Rychlé přidání pomocí aliasu



V poli `/cart` můžete přidat produkt:





- Naskenováním **čárového kódu** (ISBN, EAN13)
- Ruční zadání **přezdívky produktu**



**Poznámka:** výrobek je automaticky přidán do košíku.



#### Platební prostředky



POS podporuje:





- Druhy
- Kreditní karta
- Lightning Network (šifrování)
- Ostatní podle konfigurace



K dispozici jsou dvě pokročilé možnosti:





- Osvobození od DPH**: platí pro zdůvodnění (nevládní organizace, cizinci...)
- Dárková sleva**: mimořádná sleva s povinným komentářem



#### Zobrazení na straně klienta



Adresa URL `/pos/session` je určena pro **druhou obrazovku** (HDMI, tablet...):



Plakát:





- Rozpracované produkty
- Celková částka
- Způsob platby
- Uplatněné slevy



**Poznámka:** zákazník sleduje objednávku živě, zatímco prodejce ji zaznamenává na `/pos`.



### Shrnutí POS



| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Děkujeme, že jste pečlivě sledovali tento návod.