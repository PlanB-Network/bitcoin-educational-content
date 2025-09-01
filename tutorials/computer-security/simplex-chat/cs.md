---
name: SimpleX Chat
description: První poštovní schránka bez ID uživatele
---
![cover](assets/cover.webp)



SimpleX je bezplatná aplikace pro zasílání rychlých zpráv s radikálně odlišným přístupem k ochraně soukromí, která byla spuštěna v roce 2021. Na rozdíl od aplikací WhatsApp, Signal a dalších centralizovaných služeb pro zasílání zpráv se SimpleX vyznačuje správou uživatelů: nejsou zde žádné identifikátory uživatelů, pseudonymy, čísla ani viditelné veřejné klíče. Tato naprostá absence identifikátorů prakticky znemožňuje korelaci uživatelů a zaručuje vysokou úroveň soukromí.



Na rozdíl od většiny aplikací, které vyžadují účet nebo telefonní číslo, umožňuje SimpleX zahájit konverzaci sdílením odkazu nebo efemérního kódu QR. Každý odkaz vytvoří jedinečný šifrovaný kanál a kontakty nemohou odesílatele najít nebo znovu kontaktovat bez výslovného zadání Exchange. Zprávy jsou šifrovány od konce do konce a procházejí přes relay servery, které je po odeslání smažou a nevidí ani odesílatele, ani příjemce, ani jejich klíče.



![Image](assets/fr/01.webp)



Architektura sítě je zcela decentralizovaná a nefederovaná: servery se navzájem neznají, nevedou globální adresář a nehostí žádné uživatelské profily. A co víc, každý uživatel může nasadit a používat svůj vlastní relay server, přičemž zůstává interoperabilní s relay servery ve veřejné síti.



SimpleX je kompletně open-source (klienti, protokoly i servery) a je k dispozici pro systémy Android, iOS, Linux, Windows a macOS. Jeho místní úložiště je šifrované a přenosné, takže můžete přenášet profil z jednoho zařízení do druhého, aniž byste se museli spoléhat na centralizovaný server.



SimpleX integruje všechny klasické funkce aplikací pro zasílání zpráv. Jeho ergonomie však zůstává méně plynulá než u aplikací WhatsApp nebo Signal. Její používání může být také omezenější, zejména při přidávání kontaktů. Podle mého názoru se tedy jedná o relevantní alternativu k aplikacím WhatsApp nebo Signal pro uživatele, kteří kladou důraz na důvěrnost a kteří jsou z tohoto důvodu ochotni udělat několik ústupků v oblasti každodenního uživatelského komfortu.



| Aplikace             | E2EE 1:1       | E2EE skupiny   | Anonymní registrace | Licence klienta open-source | Licence serveru open-source | Decentralizovaný server | Rok vytvoření     |
| -------------------- | -------------- | -------------- | ------------------- | --------------------------- | ---------------------------- | ----------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                           | ❌                            | ❌                       | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                           | ❌                            | ❌                       | 2011              |
| Facebook Messenger   | ✅              | 🟡 (volitelné) | ❌                   | ❌                           | ❌                            | ❌                       | 2011              |
| Telegram             | 🟡 (volitelné) | ❌              | 🟡                  | ✅                           | ❌                            | ❌                       | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                           | ❌                            | ❌                       | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                           | ✅                            | ❌                       | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                           | ❌                            | ❌                       | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                           | ✅                            | 🟡 (federovaný)     | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                           | N/A                          | 🟡 (přes email)     | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                           | ✅                            | 🟡 (federovaný)     | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                           | ✅                            | ✅                       | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                           | ✅                            | ✅                       | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                           | ❌                            | 🟡(žádný adresář)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                           | N/A                          | ✅                       | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                           | N/A                          | ✅                       | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                           | N/A                          | ✅                       | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                           | N/A                          | ✅                       | 2013              |

*E2EE = End-to-end šifrování*



## Instalace aplikace SimpleX Chat



SimpleX Chat je k dispozici na všech platformách. Aplikaci si můžete stáhnout přímo z obchodu s aplikacemi v telefonu:




- [Google Play](https://play.google.com/store/apps/details?id=chat.simplex.app);
- [App Store](https://apps.apple.com/us/app/simplex-chat-secure-messenger/id1605771084);
- [F-Droid](https://simplex.chat/fdroid/).



V systému Android je také možné [instalovat přes APK](https://github.com/simplex-chat/simplex-chat/releases).



V tomto návodu se zaměříme na mobilní verzi, ale upozorňujeme, že jsou k dispozici také [verze pro stolní počítače](https://simplex.chat/downloads/) (MacOS, Linux a Windows). Je možné propojit desktopovou verzi s existujícím mobilním uživatelským profilem, ale aby tato synchronizace fungovala, musí být obě zařízení připojena ke stejné místní síti.



![Image](assets/fr/02.webp)



## Vytvoření účtu na SimpleX Chat



Při prvním spuštění aplikace klikněte na tlačítko "*Vytvořit profil*".



![Image](assets/fr/03.webp)



Zvolte si uživatelské jméno, které může být vaše skutečné jméno nebo pseudonym, a klikněte na "*Vytvořit*".



![Image](assets/fr/04.webp)



Dále nastavte frekvenci, s jakou bude aplikace kontrolovat nové zprávy. Pokud není problém s výdrží baterie telefonu, vyberte možnost "*Instant*", abyste zprávy dostávali v reálném čase. Pokud chcete raději šetřit baterii a zabránit tomu, aby aplikace běžela na pozadí, vyberte možnost "*Když je aplikace spuštěna*": zprávy pak budete dostávat pouze tehdy, když je aplikace otevřená. Možným kompromisem je zvolit pravidelnou kontrolu každých 10 minut.



Po výběru klikněte na "*Použít chat*".



![Image](assets/fr/05.webp)



Nyní jste připojeni k SimpleX Chat a můžete začít chatovat.



![Image](assets/fr/06.webp)



## Nastavení služby SimpleX Chat



Nejprve se do nastavení dostanete kliknutím na svou profilovou fotografii v pravém dolním rohu a poté na "*Nastavení*".



![Image](assets/fr/07.webp)



Výchozí nastavení jsou obecně vhodná pro většinu uživatelů. Doporučuji však přejít do nabídky "*Databáze passphrase a export*". Zde můžete exportovat databázi účtů SimpleX pro účely zálohování.



Můžete také upravit kód passphrase, který se používá k šifrování této databáze. Ve výchozím nastavení je náhodně vygenerována a uložena lokálně v zařízení. Pokud dáváte přednost, můžete si definovat vlastní passphrase a odstranit místní zálohu passphrase: pak ji budete muset zadávat ručně při každém otevření aplikace a také při migraci na jiné zařízení.



**Upozornění**: Pokud zvolíte tuto možnost, bude mít ztráta passphrase za následek trvalou ztrátu všech vašich profilů a zpráv SimpleX.



![Image](assets/fr/08.webp)



Doporučuji také přejít do nabídky "*Soukromí a zabezpečení*", kde můžete aktivovat možnost "*SimpleX Lock*". Ta chrání přístup k aplikaci pomocí zamykacího kódu.



![Image](assets/fr/09.webp)



V nabídkách "*Oznámení*" a "*Vzhled*" si můžete SimpleX Chat přizpůsobit podle svých preferencí.



![Image](assets/fr/10.webp)



## Odesílání zpráv pomocí SimpleX Chat



Chcete-li se spojit s jinou osobou na SimpleX, máte dvě možnosti:




- Použijte odkaz na jedno použití;
- Použijte opakovaně použitelný statický přístroj Address.



Statický kód Address umožňuje komukoli, kdo ho zná, kontaktovat vás na SimpleX. Jedná se o trvalou Address, kterou lze použít několikrát, různými lidmi, bez časového omezení. Právě tato perzistence ji činí zranitelnější vůči spamu. Na rozdíl od jiných aplikací pro zasílání zpráv však k zastavení veškerého spamu stačí smazat váš SimpleX Address, aniž by to mělo vliv na stávající konverzace. Ve skutečnosti se tento Address používá pouze k navázání počátečního spojení a po zahájení Exchange již není potřeba.



Naproti tomu odkazy na jedno použití může jakýkoli uživatel použít pouze jednou. Jakmile jej kontakt použije, odkaz se stává neplatným. Pro každé nové spojení je třeba vytvořit nový odkaz generate.



### Se statickým Address



Pokud chcete používat Address, klikněte na svůj profilový obrázek v levém dolním rohu Interface a poté vyberte možnost "*Vytvořit SimpleX Address*". Poté znovu klikněte na "*Create SimpleX Address*".



![Image](assets/fr/11.webp)



Vaše opakovaně použitelné zařízení Address bylo vytvořeno. Můžete jej sdílet s lidmi, kteří se s vámi chtějí spojit, a to buď tak, že jim ukážete QR kód, nebo jim pošlete odkaz.



![Image](assets/fr/12.webp)



Klikněte na tlačítko "*Nastavení Address*". Zde můžete nastavit oprávnění spojená s vaším Address. Volba "*Sdílet s kontakty*" zviditelní váš Address na vašem profilu SimpleX. Vaše kontakty do něj pak budou moci nahlížet a předávat jej dalším osobám, které vás chtějí kontaktovat.



Volba "*Auto-accept*" automaticky přijímá příchozí připojení přes Address. To znamená, že kdokoli s vaším Address bude moci vidět váš profil a poslat vám zprávu, pokud neaktivujete možnost "*Přijímat inkognito*". Ta při navázání nového spojení skryje vaše jméno a profilovou fotografii a nahradí je náhodným pseudonymem, odlišným pro každého účastníka hovoru.



![Image](assets/fr/13.webp)



### S opakovaně použitelným odkazem



Druhým způsobem, jak se s osobou spojit, je vytvoření jednorázového odkazu. To provedete kliknutím na ikonu tužky v pravém dolním rohu okna Interface a výběrem možnosti "*Vytvořit jednorázový odkaz*".



Pokud vám kontakt poslal odkaz, klikněte na "*Scan / Paste link*" a odkaz naskenujte nebo vložte.



![Image](assets/fr/14.webp)



SimpleX pak vygeneruje odkaz na jedno použití. Můžete jej přeposlat svému kontaktu jakýmkoli způsobem: fyzicky pomocí Exchange, jinými zprávami atd.



![Image](assets/fr/15.webp)



Můžete také zvolit, který profil se má s tímto odkazem na pozvánku spojit. To provedete kliknutím na svůj profil hned pod QR kódem. Poté budete moci:




- vyberte jeden z existujících profilů (v další části se podíváme, jak vytvořit několik profilů);
- nebo zvolte režim "*Incognito*", který skryje vaše jméno a profilovou fotografii s náhodně vygenerovaným pseudonymem pro vašeho korespondenta.



Zde jsem zvolil režim "*Incognito*".



![Image](assets/fr/16.webp)



Můj kontakt použil odkaz. Pokud jde o něj, neaktivoval režim "*Incognito*", a proto vidím jeho profilové jméno "*Bob*". Na druhou stranu Bob nevidí mé skutečné jméno "*Loïc Morel*", ale náhodný pseudonym, v tomto případě "*RealSynergy*".



![Image](assets/fr/17.webp)



Mohl bych okamžitě začít chatovat, ale nejprve bych chtěl ověřit, že mluvím s Bobem, a ne s nějakou škodlivou osobou, která mohla zachytit spojení nebo provést útok MITM.



Za tímto účelem zkontrolujeme náš bezpečnostní odkaz **mimo aplikaci**. To je důležité, protože v případě útoku MITM by bylo interní ověření ohroženo. Proto použijte jiný systém zabezpečených zpráv nebo ještě lépe zkontrolujte kódy osobně.



V chatu klikněte na Bobovu fotografii a poté na "*Ověřit bezpečnostní kód*". Totéž musí udělat Bob na své straně.



![Image](assets/fr/18.webp)



Pokud pracujete na dálku, porovnejte kódy v jiném systému zabezpečených zpráv (musí být totožné). Nebo ještě lépe, pokud se můžete setkat tváří v tvář, naskenujte QR kód svého kontaktu kliknutím na "*Scan code*".



![Image](assets/fr/19.webp)



Pokud je ověření úspěšné, zobrazí se vedle jména kontaktu ikona štítu se zatržítkem. Tím se ujistíte, že si s Bobem vyměňujete. Pokud je ověření neúspěšné, zobrazí se upozornění "*Nesprávný bezpečnostní kód!*".



![Image](assets/fr/20.webp)



Nyní můžete s Bobem volně Exchange zprávy, hovory a soubory v závislosti na oprávněních, která jste pro tuto konverzaci nastavili.



## Přizpůsobení profilů SimpleX Chat



Jednou z nejvýkonnějších funkcí systému SimpleX je možnost spravovat několik zcela samostatných uživatelských profilů, které jsou přístupné ze stejného místního účtu. To vám umožní přehledně oddělit různé identity, aniž by to komplikovalo správu zpráv.



Můžete například vytvořit:




- Profil s vaším skutečným jménem a skutečnou fotografií pro vaše profesionální výměny;
- Profil s vaším skutečným jménem a vtipnou fotografií pro rodinné výměny;
- Profil s falešnou fotografií a pseudonymem pro osobní konverzace;
- Další pseudonymní profil pro chatování s cizími lidmi.



To je to, co se chystáme udělat. Začnu konfigurací svého hlavního profilu, tedy profilu spojeného s mou skutečnou identitou. To provedu tak, že kliknu na svou profilovou fotografii v pravém dolním rohu a poté na své uživatelské jméno.



![Image](assets/fr/21.webp)



Poté kliknu na svou profilovou fotografii, abych ji změnil a přidal novou.



![Image](assets/fr/22.webp)



Chcete-li přidat další profily, klikněte na nabídku "*Vaše profily chatů*".



![Image](assets/fr/23.webp)



Zde uvidíte všechny své profily. Kliknutím na "*Přidat profil*" vytvoříte nový.



![Image](assets/fr/24.webp)



Poté zvolte informace pro svůj nový profil: jméno, fotografii atd. Zde používám pseudonym a jiný obrázek, abych v určitých výměnách skryl svou skutečnou identitu.



![Image](assets/fr/25.webp)



Podržením prstu na profilu jej můžete skrýt. Tím se v aplikaci zneviditelní spolu se všemi přidruženými konverzacemi. Můžete také zvolit možnost "*Ztlumit*", abyste přestali dostávat oznámení.



![Image](assets/fr/26.webp)



Po vytvoření profilů je můžete spravovat samostatně. Na domovské stránce jednoduše vyberte aktivní profil, který chcete zobrazit.



![Image](assets/fr/27.webp)



Při vytváření pozvánky nebo statického odkazu Address si nyní můžete vybrat, který profil s ním bude spojen. Pokud například pro odkaz generate vyberu profil "*Satoshi Nakamoto*" a pošlu jej Alici, uvidí pouze mou pseudonymní identitu "*Satoshi Nakamoto*", aniž by se dozvěděla mou skutečnou identitu "*Loïc Morel*". Naopak, pokud jí poskytnu odkaz ze svého skutečného profilu, nebude mít možnost se na můj pseudonymní profil nijak napojit.



![Image](assets/fr/28.webp)



Gratulujeme, nyní jste se seznámili s aplikací SimpleX messaging, která je vynikající alternativou k aplikaci WathsApp!



Doporučuji také tento další tutoriál, ve kterém představuji Threemu, další zajímavou alternativu pro vaši aplikaci pro zasílání zpráv:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74