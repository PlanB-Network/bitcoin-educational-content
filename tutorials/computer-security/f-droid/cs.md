---
name: F-Cold
description: Katalog svobodných aplikací a aplikací s otevřeným zdrojovým kódem.
---

![cover](assets/cover.webp)



V digitálním věku se velké korporace a instituce snaží o větší centralizaci internetu, aby jeho kontrolu vložily do svých rukou, a tím omezily soukromí a svobodu všech uživatelů. To není utopie, to se již děje. Jako bitcoináři považujete decentralizaci, respekt k soukromí a individuálním svobodám za zásady, které jsou vám drahé, zejména v nástrojích, které denně používáte. Android na rozdíl od iOS již léta umožňuje koexistenci několika obchodů s aplikacemi v rámci svého ekosystému, což vám dává svobodu vyhledávat a instalovat aplikace z vašich oblíbených zdrojů.



V tomto návodu se podíváme na F-droid, adresář aplikací, který představuje alternativu k obchodům s aplikacemi, jako jsou Google Play Store a Microsoft Store.



## Začínáme s aplikací F-Droid



F-Droid je obchod s aplikacemi a nástroji, který umožňuje instalovat bezplatné aplikace s otevřeným zdrojovým kódem na platformě Android. Samotný F-droid je open source projekt, který v roce 2010 spustil Ciaran Gultnieks a několik dalších přispěvatelů. Hlavním cílem projektu je zpřístupnit aplikace s otevřeným zdrojovým kódem a umožnit iniciátorům projektů s otevřeným zdrojovým kódem najít platformu, kde mohou publikovat své nástroje, aniž by museli odkazovat na obchod Google Play.



F-Droid bohužel není aplikace dostupná pro iOS a obsahuje mnoho nástrojů určených pro systémy Android.



Aplikaci F-droid si můžete stáhnout z [oficiální webové stránky](https://f-droid.org/) ve formátu APK a nainstalovat ji ručně do svého telefonu se systémem Android.



![download](assets/fr/02.webp)



V systému Android se ujistěte, že jste udělili oprávnění k instalaci prohlížeče, ze kterého jste F-Droid stáhli.



Po dokončení instalace spustí F-Droid aktualizaci adresářů aplikací s otevřeným zdrojovým kódem, aby obohatil aplikace v obchodě.



![repositories](assets/fr/03.webp)



Nyní můžete do telefonu instalovat aplikace, aniž byste museli procházet obchodem Google Play.



## Knihkupectví F-Droid



V obchodě s aplikacemi najdete několik kategorií aplikací, které vyhovují vašim potřebám. Na kartě **Kategorie** najdete více než 20 typů aplikací, od prohlížečů po volně dostupné textové editory, a všechny vyžadují co nejméně informací z vaší strany.



Chcete nainstalovat konkrétní aplikaci? Klikněte na tlačítko **Hledat** a zadejte název hledané aplikace.



![search](assets/fr/04.webp)



F-Droid poskytuje komplexní informace o každé aplikaci, kterou chcete nainstalovat.



Po kliknutí na aplikaci najdete mimo jiné:




- Funkce a změny přidané v nejnovější dostupné verzi
- Podrobný popis aplikace, jejích funkcí, důvodů pro její používání a komunity Open Source, která za projektem stojí.



![features](assets/fr/05.webp)





- Licence použitá v projektu, odkazy na zdrojový kód a problémy, které se vyskytly při používání aplikace
- Oprávnění vyžadovaná aplikací



![permissions](assets/fr/06.webp)



Další informace najdete v našem výukovém programu Thunderbird:



https://planb.network/tutorials/computer-security/communication/thunderbird-91d02325-0361-4641-b152-8975890284a8

F-Droid vám poskytne všechny informace, které potřebujete k rozhodnutí, zda používání aplikace chrání vaše data a zvyšuje vaše soukromí. Prohledejte všechny aplikace, které chcete používat, a poté kliknutím na tlačítko **Install** stáhněte a nainstalujte aplikaci.


Povolením této možnosti v nastavení udělíte instalační práva aplikaci F-Droid.



![settings](assets/fr/07.webp)



## Exchange vaše aplikace



F-Droid podporuje používání otevřeného zdrojového kódu a přispívání komunity, zejména prostřednictvím možnosti **Near By** Exchange. Připojte se k uživatelům ve svém okolí prostřednictvím:




- Detekce Bluetooth;
- Stejná síť Wi-Fi;
- QR kód nebo IP:PORT Address zadejte do prohlížeče.



Díky této možnosti můžete v několika krocích sdílet a přijímat aplikace nainstalované v telefonu se systémem Android s přáteli a rodinou.



![swap](assets/fr/08.webp)



## Aktualizace



Na kartě **Aktualizace** si prohlédněte seznam dostupných aktualizací a nezapomeňte si také přečíst informace o nových verzích jednotlivých aplikací, abyste zjistili, zda nedošlo k významným změnám ve verzi, kterou používáte.



![updates](assets/fr/09.webp)



Seznam dostupných aplikací můžete také aktualizovat obnovením stránky (posuňte se dolů).



## Přidání vlastních aplikací



F-Droid je projekt s otevřeným zdrojovým kódem, který podporuje příspěvky k aplikacím, které upřednostňují soukromí uživatelů. Vlastní mobilní aplikaci pro Android můžete do obchodu přidat prostřednictvím příspěvků do zdrojového kódu F-Droid GitLab.



Vaše aplikace musí mít otevřený zdrojový kód, který je veřejně dostupný například na GitHubu nebo GitLabu.


Poté musíte připravit soubor YAML (metadata) popisující vaši aplikaci, včetně všech informací a oprávnění potřebných pro její použití, podle [šablony metadat](https://f-droid.org/docs/Build_Metadata_Reference/) navržené společností F-Droid.



V sekci **Vývojáři** v [dokumentaci](https://f-droid.org/en/docs/) najdete všechny zdroje, které potřebujete k publikování a údržbě aplikací v systému F-Droid.



### Integrita a bezpečnost



Umístění aplikace do otevřeného zdrojového kódu je často synonymem vyšší bezpečnosti, ale také značného rizika. Jak lze zajistit, aby ve zdrojovém kódu aplikace dostupné v systému F-Droid nedošlo ke škodlivým změnám?



Společnost F-Droid kompiluje aplikace na svých vlastních serverech na základě oficiálního zdrojového kódu a pokynů pro kompilaci. Každá zveřejněná aplikace je znovu sestavena a ověřena, aby se zajistilo, že nebyla kompromitována. Tím je zajištěno, že nabízený soubor APK je věrný zdrojovému kódu zveřejněnému vývojáři. Navíc je každá aplikace nainstalovaná prostřednictvím služby F-Droid digitálně podepsána a poté je otisk podpisu porovnán s otiskem zveřejněným vývojáři aplikace na oficiálních webových stránkách nebo v úložišti Git.



Pokud se vám tento výukový kurz líbil, zjistěte více o našem kurzu bezpečnosti IT a správy dat:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1