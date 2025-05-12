---
name: Keet
description: Peer-to-peer chat
---
![cover](assets/cover.webp)



Keet je aplikace pro zasílání rychlých zpráv navržená tak, aby fungovala bez serverů. Aplikace, kterou v roce 2022 spustila společnost Holepunch (financovaná společnostmi Tether a Bitfinex), je založena výhradně na síti peer-to-peer a vyznačuje se radikálně decentralizovaným přístupem: zprávy, hovory a soubory si uživatelé vyměňují přímo, bez prostředníků.



Společnost Keet šifruje veškerou komunikaci end-to-end a nevyžaduje žádné osobní údaje. Registrace je anonymní, není vyžadováno telefonní číslo ani e-mail. Kromě výměny textových zpráv nabízí Keet také velmi kvalitní videohovory a neomezené sdílení souborů. Aplikaci lze tedy používat hybridním způsobem, a to jak pro osobní, tak pro pracovní použití.



![Image](assets/fr/01.webp)



V současné době (duben 2025) není Keet zcela open-source. Část zdrojového kódu je k dispozici na [repozitáři Holepunch GitHub](https://github.com/holepunchto), zejména kryptografické a síťové komponenty, ale klient Interface zatím ne. Holepunch však oznámil svůj záměr celou aplikaci nakonec zpřístupnit jako open-source. V závislosti na tom, kdy objevíte tento návod, je možné, že se tak již stalo.




| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| **Keet**             | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-end šifrování*



## Instalace systému Keet



Keet je k dispozici na všech platformách. Aplikaci si můžete stáhnout přímo z obchodu s aplikacemi v telefonu:




- [Google Play](https://play.google.com/store/apps/details?id=io.keet.app&pli=1);
- [App Store](https://apps.apple.com/us/app/keet-by-holepunch/id6443880549);



V systému Android je také možné [instalovat přes APK](https://github.com/holepunchto/keet-mobile-releases/releases).



V tomto návodu se zaměříme na mobilní verzi, ale upozorňujeme, že k dispozici jsou také [počítačové verze](https://keet.io/) (MacOS, Linux a Windows). Je také možné synchronizovat účet na více zařízeních.



## Vytvoření účtu na portálu Keet



Při prvním spuštění můžete prezentační obrazovky ignorovat.



![Image](assets/fr/02.webp)



Klikněte na tlačítko "*Jsem nový uživatel*".



![Image](assets/fr/03.webp)



Přijměte podmínky používání a klikněte na "*Rychlé nastavení*".



![Image](assets/fr/04.webp)



Vyberte jméno nebo přezdívku a klikněte na "*Dokončit nastavení*".



![Image](assets/fr/05.webp)



Váš profil je nyní vytvořen. Kliknutím na tlačítko "*Dokončit nastavení*" znovu dokončete nastavení.



![Image](assets/fr/06.webp)



Svůj profil můžete kdykoli upravit na kartě "*Profil*".



## Uložte svůj účet Keet



Nejdříve je třeba na nový účet Keet uložit frázi pro obnovení. Jedná se o sekvenci 24 slov, která vám umožní obnovit přístup k účtu v případě ztráty nebo změny zařízení. Tato fráze poskytuje plný přístup k vašemu účtu komukoli, kdo ji zná, proto je důležité vytvořit si spolehlivou zálohu a nikdy ji neprozradit.



Za tímto účelem klikněte na kartu "*Profil*" v pravém dolním rohu okna Interface.



![Image](assets/fr/07.webp)



Poté přejděte do nabídky "*Nastavení*".



![Image](assets/fr/08.webp)



Vyberte možnost "*Soukromí a zabezpečení*".



![Image](assets/fr/09.webp)



Poté klikněte na položku "*Fráze pro obnovení*".



![Image](assets/fr/10.webp)



Stisknutím tlačítka "*Zobrazit frázi*" zobrazíte svou frázi pro obnovení. Pečlivě si ji zkopírujte a uschovejte na bezpečném místě.



![Image](assets/fr/11.webp)



## Odesílání zpráv pomocí služby Keet



Chcete-li komunikovat v síti Keet, musíte vytvořit "*Rooms*". To provedete kliknutím na ikonu tužky v pravém horním rohu Interface.



![Image](assets/fr/12.webp)



Vyberte možnost "*Nový skupinový chat*".



![Image](assets/fr/13.webp)



Zvolte název a popis místnosti "*Room*" a klikněte na "*Create group chat*".



![Image](assets/fr/14.webp)



Nyní je vytvořen váš "*pokoj*". Kliknutím na ikonu "*+*" vpravo nahoře pozvete účastníky.



![Image](assets/fr/15.webp)



Definujte práva, která novým členům udělíte prostřednictvím pozvánky, a dobu platnosti odkazu. Poté klikněte na "*generate invite*".



![Image](assets/fr/16.webp)



Keet zobrazí odkaz generate pro připojení k vaší "*pokoj*". Můžete ho buď zkopírovat a sdílet, nebo nechat naskenovat QR kód lidem, které chcete pozvat.



![Image](assets/fr/17.webp)



Nyní můžete začít vyměňovat zprávy a multimediální soubory. Chcete-li zahájit hovor, klikněte na ikonu telefonu v pravém horním rohu.



![Image](assets/fr/18.webp)



Z této skupiny můžete také posílat soukromé zprávy konkrétnímu členovi. Klikněte na profilový obrázek skupiny a poté vyberte požadovaného člena v sekci "*Členové*".



![Image](assets/fr/19.webp)



Klikněte na tlačítko "*Odeslat žádost o DM*" a zadejte zprávu.



![Image](assets/fr/20.webp)



Po přijetí žádosti o DM najdete tento kontakt na domovské stránce, kde si s ním můžete soukromě promluvit.



![Image](assets/fr/21.webp)



## Synchronizace účtu na více zařízeních



Když už víte, jak Keet používat, a máte účet, můžete jej synchronizovat i na jiném zařízení, například v počítači. Za tímto účelem otevřete aplikaci v mobilním telefonu, poté klikněte na "*Profil*" a přejděte do "*Nastavení*".



![Image](assets/fr/22.webp)



Poté přejděte do nabídky "*Moje zařízení*".



![Image](assets/fr/23.webp)



Klikněte na "*Přidat zařízení*". Keet generate zobrazí odkaz pro synchronizaci nového zařízení. Zkopírujte tento odkaz.



![Image](assets/fr/24.webp)



Do druhého zařízení nainstalujte aplikaci Keet. Na domovské obrazovce vyberte možnost "*Jsem současný uživatel*".



![Image](assets/fr/25.webp)



Poté klikněte na "*Propojit zařízení*".



![Image](assets/fr/26.webp)



Vložte odkaz poskytnutý prvním zařízením a klikněte na "*Spustit synchronizaci*".



![Image](assets/fr/27.webp)



Na prvním zařízení klikněte na "*Potvrdit propojení zařízení*" a autorizujte připojení.



![Image](assets/fr/28.webp)



Na druhém zařízení dokončete proces kliknutím na "*Propojit zařízení*".



![Image](assets/fr/29.webp)



Z tohoto nového zařízení máte nyní přístup ke všem svým "*pokojům*" a konverzacím.



![Image](assets/fr/30.webp)



Gratulujeme, nyní jste se seznámili s používáním aplikace Keet messaging, která je skvělou alternativou k aplikaci WathsApp! Pokud se vám tento návod zdál užitečný, budu vám velmi vděčný, když mi níže zanecháte palec Green. Neváhejte tento návod sdílet na svých sociálních sítích. Moc vám děkuji!



Doporučuji také tento další tutoriál, ve kterém vám představím Proton Mail, alternativu Gmailu, která je mnohem šetrnější k soukromí:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2