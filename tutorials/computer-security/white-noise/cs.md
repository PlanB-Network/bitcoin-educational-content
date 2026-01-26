---
name: White Noise
description: Soukromá decentralizovaná aplikace pro zasílání zpráv založená na protokolech Nostr a MLS
---

![cover](assets/cover.webp)




## Úvod



"Uprostřed obtíží se skrývá příležitost". Tento citát Alberta Einsteina nám připomíná, že problémy nejsou definitivní, ale obsahují v sobě zárodky nových, inovativních řešení.



Motivace, která stála za spuštěním řešení, jež představujeme v tomto tutoriálu, to dokonale ilustruje. Jedná se o **White Noise**, které se zrodilo z nutnosti.



Podle slov jejího zakladatele Maxe Hillebranda, která uvedl časopis *Bitcoin Magazine*: "Tento projekt jsme spustili z nedostatku alternativ." Vysvětluje, že "stávající šifrovací aplikace jsou ve velkém měřítku neefektivní: přidání 100 lidí do skupinové konverzace značně zpomaluje šifrování. Decentralizované platformy mezitím nenabízejí soukromé zprávy. A konečně, otevřená relay síť Nostr umožňuje každému šířit myšlenky, ale ochrana přímých zpráv zůstává dramaticky nedostatečná. Uvědomili jsme si: abychom ochránili svobodu, musíme tyto systémy sloučit."



## Co je White Noise?



White Noise je open source aplikace pro zasílání zpráv vyvinutá neziskovým týmem. Aplikace podporuje bezpečnost, soukromí a decentralizaci. Na rozdíl od běžných aplikací nevyžaduje telefonní číslo ani e-mailovou adresu.


White Noise se vyznačuje integrací dvou základních protokolů - Nostr a MLS - které tvoří jeho technický základ.



Nostr (Notes and Other Stuff Transmitted by Relays) je decentralizovaný protokol s otevřeným zdrojovým kódem navržený tak, aby odolával cenzuře.  Protokol používá relé, páry klíčů a klienty.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

U bílého šumu si dokonce můžete zvolit vlastní nastavení přenosu, abyste maximalizovali soukromí.



MLS (Messaging Layer Security) je naopak bezpečnostní protokol, který umožňuje koncové šifrování zpráv. Jinými slovy, zprávy jsou přístupné pouze v koncových bodech, tj. u odesílatele a příjemce zprávy. To znamená, že relé zapojená do směrování zpráv nemají přístup k jejich obsahu.



Zde je rychlé srovnání White Noise s několika nejznámějšími aplikacemi pro zasílání zpráv.





| Body srovnání               | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| Šifrování E2EE / 1:1        | ✅ Ano        | Volitelné  | ✅ Ano            | ✅ Ano   | ✅ Ano    | ✅ Ano             | ✅ Ano  |
| Skupinové šifrování E2EE    | ✅ Ano        | ❌ Ne       | ✅ Ano            | ✅ Ano   | ✅ Ano    | Volitelné         | ✅ Ano  |
| Anonymizace identity        | ✅ Ano        | Volitelné  | ❌ Ne             | ✅ Ano   | ❌ Ne     | ❌ Ne              | ❌ Ne   |
| Open source server          | ✅ Ano        | ❌ Ne       | ❌ Ne             | ✅ Ano   | ❌ Ne     | ❌ Ne              | ✅ Ano  |
| Open source klient          | ✅ Ano        | ✅ Ano       | ❌ Ne             | ✅ Ano   | ❌ Ne     | ❌ Ne              | ✅ Ano  |
| Decentralizovaný server     | ✅ Ano        | ❌ Ne       | ❌ Ne             | ✅ Ano   | ❌ Ne     | ❌ Ne              | ❌ Ne   |
| Rok založení                | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |

## Začínáme s White Noise



### Instalace White Noise



Přejděte na [webovou stránku White Noise](https://www.whitenoise.chat/) a klikněte na **Stáhnout**.



![screen](assets/fr/03.webp)



White Noise je v současné době k dispozici pouze na mobilních zařízeních.


V novém rozhraní, které se zobrazí, stiskněte tlačítko :





- tlačítko **Zapstore** nebo **Android APK**, pokud si jej chcete stáhnout na Android;
- na tlačítko **iOS TestFlight**, pokud používáte iPhone.



![screen](assets/fr/04.webp)



Pro účely tohoto návodu provedeme stažení systému Android.


Pokud se rozhodnete stahovat přes **Zapstore**, budete na něj přesměrováni. Po vstupu na Zapstore zadejte do vyhledávacího řádku **White Noise**. Poté pokračujte ve stahování kliknutím na **Install**.



![screen](assets/fr/05.webp)



![screen](assets/fr/06.webp)



Pokud se rozhodnete stáhnout soubor APK, budete přesměrováni do úložiště White Noise GitHub, kde si můžete vybrat správnou verzi pro svůj smartphone.



Dostupné soubory APK jsou :





- whitenoise-0.2.1-arm64-v8a.apk** (57,7 MB), vhodný pro nejnovější telefony s 64bitovými procesory;
- whitenoise-0.2.1-armeabi-v7a.apk** (47,5 MB) vhodný pro starší telefony s 32bitovými procesory.



K dispozici jsou také soubory **.sha256**, což jsou pouze kontrolní součty pro ověření integrity stahování.



![screen](assets/fr/07.webp)



Po dokončení stahování aplikaci nainstalujte a otevřete.



![screen](assets/fr/08.webp)



### Počáteční nastavení uživatelského účtu



Při prvním připojení ke White Noise stiskněte tlačítko **Registrace**.



![screen](assets/fr/09.webp)



Dále nakonfigurujte svůj profil výběrem profilové fotografie, jména a přidáním krátkého popisu své osoby. Nemusíte vyplňovat svou skutečnou identitu (jméno a fotografii).


Všimněte si, že White Noise pro vás automaticky vybere jméno (pseudonym), které si můžete ponechat nebo změnit. Nakonec stiskněte tlačítko **Konec**.



![screen](assets/fr/10.webp)



Budete přesměrováni na **hlavní obrazovku** služby White Noise, kde se zobrazí seznam vašich konverzací. Váš účet je nyní nastaven a připraven k použití. Můžete sdílet svůj profil nebo vyhledat přátele a začít chatovat.



![screen](assets/fr/11.webp)




### Zjištění rozhraní White Noise



V hlavním rozhraní se v horní části obrazovky zobrazí :



Ikona profilu v levém horním rohu je miniatura vaší profilové fotografie nebo první písmeno vašeho profilového jména. Klepnutím na ni získáte přístup k nastavení účtu.



![screen](assets/fr/12.webp)



![screen](assets/fr/13.webp)



V pravém horním rohu najdete ikonu pro zahájení nové konverzace.



![screen](assets/fr/14.webp)



![screen](assets/fr/15.webp)




## Nastavení uživatelského účtu



Stisknutím ikony profilu v levém horním rohu získáte přístup k nastavení.



![screen](assets/fr/16.webp)



V horní části rozhraní **Nastavení** najdete svou fotografii a jméno profilu, dále svůj veřejný klíč, který můžete sdílet pomocí QR kódu vedle něj.



![screen](assets/fr/17.webp)



Hned pod ním najdete tlačítko **Změnit účet**, které vám umožní připojit se k jinému profilu v aplikaci.



![screen](assets/fr/18.webp)



Pak máte první oddíl se čtyřmi (4) dílčími nabídkami, například :





- Upravit profil**



V této podnabídce můžete upravit název profilu, adresu Nostr (NIP-05)... Nezapomeňte kliknout na **Uložit**, abyste změny uložili.



![screen](assets/fr/19.webp)





- Profilové klíče**



Zde máte přístup ke svým veřejným a soukromým (tajným) klíčům. Jak připomíná White Noise, váš soukromý klíč nesmí být za žádných okolností prozrazen.



![screen](assets/fr/20.webp)





- Síťové relé



V této podnabídce můžete přidat nebo odebrat **obecná relé** (relé definovaná pro použití ve všech aplikacích Nostr), **relátka schránky** a **relátka sady klíčů**.



Klepnutím na ikonu **odpad** před relé jej odstraníte nebo klepnutím na ikonu **+** (plus) přidáte nové relé.



![screen](assets/fr/21.webp)





- Odpojení**



Kliknutím na tuto podnabídku odpojíte svůj účet od aplikace. Ujistěte se však, že jste uložili své soukromé klíče do režimu offline, jinak se později nebudete moci znovu přihlásit.



![screen](assets/fr/22.webp)




Druhá část nabízí dílčí nabídky:





- Nastavení aplikace



Zde můžete definovat vzhled (téma a jazyk zobrazení) aplikace a dokonce odstranit data, pokud máte pocit, že byla ohrožena, nebo pokud se sami cítíte ohroženi.



![screen](assets/fr/23.webp)





- Přispějte na White Noise



Tým White Noise (nezisková organizace) můžete podpořit dary prostřednictvím jejich Bleskové adresy nebo adresy pro tichou platbu Bitcoin.



![screen](assets/fr/24.webp)



A konečně úplně dole se nachází **nastavení vývojáře**.



![screen](assets/fr/25.webp)




## Začněte konverzaci



Nyní se podíváme na to, jak začít konverzaci. V době psaní tohoto článku nabízí White Noise tři možnosti komunikace. Postupně prozkoumáme **Soukromé konverzace** (**Konverzace 1:1**), tj. pouze mezi vámi a jednou další osobou, **Skupinové konverzace** a **Odesílání multimediálních souborů**.




### Kategorie 1:1



Chcete-li přidat nového korespondenta, klikněte v hlavním rozhraní na ikonu pro zahájení nové konverzace.


Poté naskenujte QR kód veřejného klíče (1) nebo vložte veřejný klíč (2) nového korespondenta do vyhledávacího řádku a vyhledejte ho.



![screen](assets/fr/26.webp)



Klepnutím na tlačítko **Začít konverzaci** zahájíte konverzaci se svým korespondentem. Svého korespondenta můžete také **sledovat** nebo ho pozvat do skupinové konverzace stisknutím tlačítka **Přidat do skupiny**.



![screen](assets/fr/27.webp)



Vaše první zpráva novému korespondentovi se podobá žádosti o pozvání. Tuto žádost musí korespondent přijmout, abyste s ním mohli komunikovat. Pokud odmítne, no, žádná konverzace není možná.



![screen](assets/fr/28.webp)



Navíc dokud vaši pozvánku nepřijmou, nebudou si moci přečíst obsah vaší úvodní zprávy.



Jakmile přijme vaši pozvánku, může vám odpovědět a vy dva spolu můžete bezproblémově a bezpečně komunikovat.



![screen](assets/fr/29.webp)



V diskusi máte navíc k dispozici další funkce.



Dlouhým stisknutím konkrétní zprávy můžete zobrazit možnosti, jako je například :




- reagovat na zprávu pomocí emoji (1) ;
- vytvořit **přímou citaci** a odpovědět na zprávu stisknutím tlačítka **Odpovědět** (2) ;
- zkopírujte zprávu stisknutím tlačítka **Kopírovat** (3).



![screen](assets/fr/30.webp)





- smazat zprávu tlačítkem **Smazat** pouze v případě, že pochází od vás.



![screen](assets/fr/31.webp)



V rámci konverzace můžete vyhledávat.



Klepnutím na avatar korespondenta v horní části obrazovky se dostanete do "informací o konverzaci" a klepněte na tlačítko **Vyhledat v konverzaci**.



![screen](assets/fr/32.webp)



![screen](assets/fr/33.webp)



Do zobrazeného vyhledávacího řádku zadejte slovo, které chcete vyhledat, a spusťte vyhledávání. Poté se vám zobrazí hledaná slova zvýrazněná **tučným písmem**.



![screen](assets/fr/34.webp)




### Skupinové rozhovory



Konverzační skupiny lze vytvářet na serveru White Noise.



To provedete tak, že se dotknete ikony v rozhraní pro spuštění nové konverzace a kliknete na možnost **Nová skupinová konverzace**. Poté do vyhledávacího řádku zadejte veřejný klíč prvního člena, kterého chcete do skupiny přidat.



![screen](assets/fr/35.webp)



![screen](assets/fr/36.webp)



Pokud tato možnost nefunguje, zadejte v rozhraní **Začít novou konverzaci** do vyhledávacího řádku veřejný klíč prvního člena, kterého chcete do skupiny přidat. Můžete také naskenovat QR kód spojený s jeho veřejným klíčem.



Tentokrát místo klepnutí na tlačítko **Začít konverzaci** klepněte na tlačítko **Přidat do skupiny**.



![screen](assets/fr/37.webp)



V zobrazené kontextové nabídce klepněte na možnost **Nová skupinová konverzace**.



![screen](assets/fr/38.webp)



Poté stiskněte tlačítko **Pokračovat** (nemusíte znovu zadávat jeho veřejný klíč).



![screen](assets/fr/39.webp)



Jako tvůrce skupiny jste automaticky jejím správcem. Vyplňte údaje o skupině, například **název a popis skupiny**, a poté klikněte na tlačítko **Vytvořit skupinu**.



![screen](assets/fr/40.webp)



Uživatel, kterého přidáte jako prvního člena, a všichni ostatní, které přidáte později, obdrží oznámení s pozvánkou do skupiny. Aby se ke skupině připojili, musí ji přijmout kliknutím na tlačítko **Přijmout**.



![screen](assets/fr/41.webp)



Je také možné přidat nového člena, se kterým již chatujete v existující skupině. Chcete-li tak učinit, klepněte na avatar korespondenta v horní části obrazovky, čímž se dostanete k "informacím o konverzaci", a klepněte na tlačítko **Přidat do skupiny**.



![screen](assets/fr/42.webp)



V novém rozhraní, které se zobrazí, **zaškrtněte** skupinu, do které ho chcete přidat, a klepněte na **Přidat do skupiny**. Zbývá jen počkat, až bude souhlasit s připojením ke skupině.



![screen](assets/fr/43.webp)



Všimněte si, že pouze správce skupiny může měnit informace o skupině a přidávat nebo vylučovat její členy. Rotace klíčů také zabraňuje zakázaným členům dešifrovat budoucí zprávy.



Chcete-li odebrat člena, klepněte v hlavním rozhraní skupiny na ikonu skupiny v horní části a přejděte do rozhraní s informacemi o skupině.



![screen](assets/fr/44.webp)



![screen](assets/fr/45.webp)



Poté klikněte na jméno člena a na možnost **Odstranit ze skupiny**. V tomto rozhraní mu také můžete poslat zprávu, sledovat ho nebo ho přidat do jiné skupiny.



![screen](assets/fr/46.webp)



### Odesílání multimediálních souborů



Na White Noise lze prozatím mezi uživateli sdílet pouze fotografie. Ať už jste v soukromé konverzaci, nebo ve skupinovém chatu, musíte k tomu :





- stiskněte symbol **plus (+)** na levé straně vstupního pole textové zprávy.



![screen](assets/fr/47.webp)





- poté klikněte na políčko označené **Fotografie** v dolní části, čímž získáte přístup do své galerie.



![screen](assets/fr/48.webp)





- vyberte fotografie, které chcete odeslat.



![screen](assets/fr/49.webp)



![screen](assets/fr/50.webp)



![screen](assets/fr/51.webp)





## Klíčové body k zapamatování



White Noise nabízí dobrou úroveň důvěrnosti a vynikající zabezpečení. Na druhou stranu se jedná o velmi novou aplikaci, která není příliš rozšířená a je stále v plenkách. V důsledku toho je ještě příliš brzy na to, aby bylo možné vyvozovat nějaké aktivní závěry. Během používání je možné se setkat s několika poruchami.



V současné době postrádá některé funkce (žádné audio ani video hovory, žádné posílání multimediálních audio ani video souborů) ve srovnání s populárními aplikacemi pro zasílání zpráv.



Nicméně White Noise zůstává zajímavou možností pro konverzace, kde je důvěrnost nejdůležitější (např. s rodinou, blízkými přáteli nebo aktivisty ve společné věci), i když vyžaduje trochu úsilí při instalaci (prostřednictvím alternativních obchodů s aplikacemi nebo souborů APK) a učení (zvládnutí konceptu párů klíčů, klientů a relé s protokolem Nostr).



Nyní už víte, jak pomocí White Noise bezpečně komunikovat s přáteli a rodinou. Pokud je pro vás tento návod užitečný, dejte nám palec nahoru.



Doporučujeme náš návod na Tox Chat, aplikaci, která umožňuje chatovat bez prostředníků přes decentralizovaný protokol Tox.



https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3