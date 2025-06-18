---
name: Signál
description: Vyjadřujte se svobodně
---
![cover](assets/cover.webp)



Signál je aplikace pro zasílání zpráv šifrovaných od konce ke konci, která je ve výchozím nastavení navržena tak, aby poskytovala dobrou důvěrnost. Každá zpráva, hovor a soubor jsou chráněny protokolem Signal, který je považován za jeden z nejodolnějších protokolů pro zasílání zpráv. Opakovaně jej využívá mnoho dalších aplikací, včetně aplikací WathsApp, Facebook Messenger, Skype a Google Messages pro komunikaci RCS.



Službu Signal spustila v roce 2014 Moxie Marlinspike (pseudonym) a od roku 2018 ji rozvíjí nezisková organizace Signal Foundation, která vznikla s podporou Briana Actona (spoluzakladatele WhatsApp).



![Image](assets/fr/01.webp)



V porovnání s aplikací WhatsApp se Signal vyznačuje transparentností: kód aplikace na straně klienta i serveru je zcela otevřený. To umožňuje komukoli provést audit, a zejména zkontrolovat, zda je šifrování použito tak, jak je inzerováno.



Služba Signal se však spoléhá na použití telefonního čísla, což je její hlavní slabina, pokud jde o anonymitu ve srovnání s jinými řešeními. Přesto je aplikace podle mého názoru jednou z nejspolehlivějších, pokud jde o bezpečnost a důvěrnost, a to díky zcela otevřené architektuře a široce přijatému šifrovacímu protokolu, a proto je na rozdíl od jiných okrajovějších aplikací testována a auditována.



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




## Instalace aplikace Signal



Signál je k dispozici na všech platformách. Aplikaci si můžete stáhnout přímo z obchodu s aplikacemi v telefonu:




- [Google Play](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms);
- [App Store](https://apps.apple.com/us/app/signal-private-messenger/id874139669);



V systému Android je také možné [instalovat přes APK](https://github.com/signalapp/Signal-Android/releases).



V tomto návodu se zaměříme na mobilní verzi, ale upozorňujeme, že jsou k dispozici také [verze pro stolní počítače](https://signal.org/fr/download/) (MacOS, Linux a Windows). Nejprve však musíte nastavit mobilní aplikaci, než budete moci synchronizovat svůj účet s verzí pro stolní počítače.



## Vytvoření účtu na službě Signal



Při prvním spuštění aplikace klikněte na tlačítko "*Pokračovat*".



![Image](assets/fr/02.webp)



Zadejte své telefonní číslo a klikněte na "*Další*".



![Image](assets/fr/03.webp)



Ověřovací kód vám bude zaslán prostřednictvím SMS. Tento kód zadejte do aplikace Signal.



![Image](assets/fr/04.webp)



Zvolte si kód PIN pro zabezpečení účtu Signal. Tento kód zašifruje vaše data a lze jej použít k obnovení přístupu k účtu v případě ztráty zařízení. Proto je důležité zvolit si robustní, co nejdelší a náhodný kód PIN a spolehlivě si jej zaznamenávat.



![Image](assets/fr/05.webp)



Potvrďte tento kód PIN podruhé.



![Image](assets/fr/06.webp)



Nyní si můžete přizpůsobit svůj uživatelský profil. Vyberte si fotografii, zadejte své jméno nebo přezdívku. V této fázi můžete také definovat, kdo vás může na službě Signal najít prostřednictvím vašeho čísla. Pokud chcete být viditelní, vyberte možnost "*Každý*", nebo "*Nikdo*", abyste zůstali prostřednictvím telefonního čísla nedohledatelní (pak můžete být přidáni pouze se svým "*Jménem uživatele*"). Jakmile provedete výběr, klikněte na "*Další*".



![Image](assets/fr/07.webp)



Nyní jste připojeni ke službě Signal a připraveni k odesílání zpráv Exchange.



![Image](assets/fr/08.webp)



## Nastavení účtu Signal



Kliknutím na profilovou fotografii v levém horním rohu získáte přístup k nastavení aplikace.



![Image](assets/fr/09.webp)



V nabídce "*Účet*" můžete spravovat nastavení svého profilu. Doporučuji ponechat výchozí nastavení. Můžete také aktivovat možnost "*Zámek registrace*", která chrání váš účet před určitými typy útoků. Tato nabídka obsahuje také možnosti, které potřebujete k přenosu účtu do nového zařízení.



![Image](assets/fr/10.webp)



Dalším kliknutím na profilový obrázek v nastavení se dostanete k možnostem přizpůsobení profilu. Doporučuji nastavit "*Jméno uživatele*": to vám umožní kontaktovat ostatní lidi, aniž byste museli odhalit své telefonní číslo.



![Image](assets/fr/11.webp)



Výběrem možnosti "*QR kód nebo odkaz*" získáte informace, které potřebujete sdílet s někým, kdo vás chce přidat do služby Signal.



![Image](assets/fr/12.webp)



Zvláště důležitá je nabídka "*Soukromí*". Zde najdete možnosti pro kontrolu viditelnosti vašeho čísla, správu zpráv s kontakty a také různá oprávnění udělená v aplikaci.



![Image](assets/fr/13.webp)



Nebojte se prozkoumat nabídky "*Vzhled*", "*Chaty*" a "*Oznámení*" a přizpůsobte si Interface a fungování aplikace svým osobním potřebám.



## Aplikace Connect pro stolní počítače



Chcete-li připojit desktopovou aplikaci, začněte instalací softwaru do počítače (viz první část tohoto návodu). Poté v telefonu přejděte do Nastavení a otevřete část "*Připojená zařízení*".



![Image](assets/fr/14.webp)



Klikněte na tlačítko "*Připojit nové zařízení*".



![Image](assets/fr/15.webp)



V počítači spusťte software a pomocí telefonu naskenujte kód QR zobrazený na obrazovce. Pokud chcete importovat konverzace, vyberte možnost "*Přenést historii zpráv*".



![Image](assets/fr/16.webp)



Vaše zařízení jsou nyní plně synchronizována.



![Image](assets/fr/17.webp)



## Odesílání zpráv pomocí služby Signál



Chcete-li s někým komunikovat v aplikaci Signal, musíte si ho nejprve přidat jako kontakt. Existuje několik možností: můžete je přidat prostřednictvím jejich telefonního čísla (pokud má dotyčná osoba aktivovanou možnost vyhledání tímto způsobem) nebo použít jejich ID služby Signal.



Klikněte na ikonu tužky v pravém dolním rohu okna Interface.



![Image](assets/fr/18.webp)



V mém případě chci přidat osobu podle uživatelského jména. Kliknu tedy na "*Najít podle uživatelského jména*".



![Image](assets/fr/19.webp)



Poté můžete vložit jeho přihlašovací jméno nebo naskenovat jeho QR kód.



![Image](assets/fr/20.webp)



Pošlete mu zprávu a navažte s ním kontakt.



![Image](assets/fr/21.webp)



Konverzace se poté zobrazí na domovské stránce. Pokud osoba přijme vaši žádost o kontakt, zobrazí se její jméno a profilová fotografie.



![Image](assets/fr/22.webp)



Gratulujeme, nyní jste se seznámili s používáním aplikace Signal messaging, která je skvělou alternativou k aplikaci WathsApp! Pokud se vám tento návod zdál užitečný, budu vám velmi vděčný, když mi níže zanecháte palec Green. Neváhejte tento návod sdílet na svých sociálních sítích. Děkuji vám mnohokrát!



Doporučuji také tento další tutoriál, ve kterém vám představím Proton Mail, alternativu Gmailu, která je mnohem šetrnější k soukromí:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2