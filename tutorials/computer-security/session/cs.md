---
name: Session
description: Odesílání šifrovaných zpráv, nikoli metadat
---
![cover](assets/cover.webp)



Session je šifrovaná aplikace pro zasílání zpráv vytvořená v roce 2020 a navržená tak, aby poskytovala vyšší úroveň důvěrnosti než tradiční zasílání zpráv. Nejprve ji vyvinula nadace *Oxen Privacy Tech Foundation* a poté nadace *Session Technology Foundation*.



Session se může pochlubit několika zajímavými technickými vlastnostmi: koncové šifrování zpráv, decentralizovaná síť organizovaná tak, aby byla zaručena dostupnost a redundance, a směrování inspirované technologií Tor. Na rozdíl od aplikací WathsApp nebo Signal, které k registraci vyžadují telefonní číslo, Session nepožaduje žádné osobní údaje (žádné číslo, žádný e-mail, pouze dvojici kryptografických klíčů).



Session umožňuje posílat zprávy, soubory, hlasové zprávy, zvukové hovory a také skupiny až o 100 členech (a komunity o více členech), přičemž minimalizuje únik metadat.



![Image](assets/fr/01.webp)



Zasedání je určeno především uživatelům, pro které je důvěrnost jednou z hlavních priorit. Tato služba pro zasílání zpráv představuje seriózní alternativu k aplikaci WhatsApp, jejíž architektura je navržena tak, aby odolala moderním modelům sledování.



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
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-end šifrování*



## Instalace aplikace Relace



Relace je k dispozici na všech platformách. Aplikaci si můžete stáhnout přímo z obchodu s aplikacemi v telefonu:




- [Google Play](https://play.google.com/store/apps/details?id=network.loki.messenger);
- [App Store](https://apps.apple.com/us/app/session-private-messenger/id1470168868);
- [F-Droid](https://fdroid.getsession.org/).



V systému Android je také možné [instalovat přes APK](https://github.com/session-foundation/session-android/releases).



V tomto návodu se zaměříme na mobilní verzi, ale upozorňujeme, že k dispozici jsou také [počítačové verze](https://getsession.org/download) (MacOS, Linux a Windows). Později se podíváme na to, jak synchronizovat účet ve více zařízeních.



## Vytvoření účtu na stránce Session



Při prvním spuštění klikněte na "*Vytvořit účet*".



![Image](assets/fr/02.webp)



Zvolte si zobrazovací jméno svého profilu. Může to být pseudonym nebo vaše skutečné jméno.



![Image](assets/fr/03.webp)



Poté budete muset zvolit jeden ze dvou režimů správy oznámení:





- Rychlý režim (**Firebase Cloud Messaging/Apple Push Notification Service**): umožňuje přijímat oznámení zpráv téměř v reálném čase díky oznamovacím službám poskytovaným společností Google nebo Apple (v závislosti na vašem systému). Aby tato funkce fungovala, jsou společnosti Google nebo Apple předány vaše IP Address a jedinečné ID oznámení a ID účtu relace je také zaregistrováno na serveru STF (prostřednictvím sítě Tor). Tento režim zahrnuje (sice minimální) odhalení metadat, ale neohrožuje obsah zpráv ani kontakty a neumožňuje sledovat vaši skutečnou činnost. Tento režim je tedy efektivnější z hlediska rychlosti odezvy, ale spoléhá na centralizovanou infrastrukturu a je o něco méně efektivní z hlediska důvěrnosti.





- Pomalý režim (**zpětné dotazování**): aplikace relace zůstává aktivní na pozadí a pravidelně dotazuje síť na nové zprávy. Tento přístup zaručuje větší důvěrnost než první, protože se žádná data nepřenášejí na servery třetích stran; servery Google, Apple ani STF nedostávají žádné informace. Na druhou stranu má tento režim dvě nevýhody: oznámení se mohou opozdit (až o několik minut) a spotřeba energie je obecně vyšší kvůli činnosti aplikace na pozadí.



![Image](assets/fr/04.webp)



Nyní jste připojeni k aplikaci Relace a můžete začít vyměňovat zprávy.



![Image](assets/fr/05.webp)



## Uložit účet relací



Než začnete používat aplikaci Session, nejprve si uložte svůj účet, abyste jej mohli obnovit, pokud zařízení ztratíte. To provedete kliknutím na tlačítko "*Pokračovat*" vedle položky "*Uložit heslo pro obnovení*".



![Image](assets/fr/06.webp)



Relace pak zobrazí větu Mnemonic. Pečlivě si ji zkopírujte a uschovejte na bezpečném místě. Tato fráze poskytuje plný přístup k vašemu účtu Session, proto je důležité ji neprozradit. Budete ji potřebovat pro přístup k účtu v jiném zařízení, zejména pokud dojde ke ztrátě nebo výměně vašeho stávajícího telefonu.



![Image](assets/fr/07.webp)



Tato věta funguje podobně jako věty Mnemonic používané v portfoliích Bitcoin. Doporučuji proto nahlédnout do tohoto dalšího návodu, ve kterém vysvětluji osvědčené postupy při ukládání fráze Mnemonic:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Upozornění**: Na rozdíl od frází Mnemonic, které se používají v portfoliích Bitcoin, musíte v případě Session **bezpodmínečně uložit každé slovo celé**. První 4 písmena nestačí!



## Nastavení aplikace Relace



Chcete-li se dostat do nastavení aplikace, klikněte na svou profilovou fotografii v levém horním rohu aplikace Interface. Zde můžete přidat profilovou fotografii.



![Image](assets/fr/08.webp)



V nabídce "*Soukromí*" můžete povolit nebo zakázat různé funkce (pozor, některé mohou odhalit vaši IP adresu Address). Doporučuji také aktivovat možnost "*Zamknout aplikaci*", která pro přístup k aplikaci vyžaduje ověření.



![Image](assets/fr/09.webp)



V nabídce "*Oznámení*" najdete volbu mezi "*Rychlý režim*" a "*Pomalý režim*" (viz předchozí části návodu). Oznámení si také můžete přizpůsobit podle svých preferencí.



![Image](assets/fr/10.webp)



Nakonec přejděte do nabídky "*Vzhled*" a přizpůsobte si Interface podle svého vkusu. Nabídka "*Heslo pro obnovení*" umožňuje načíst frázi Mnemonic, pokud si přejete vytvořit novou zálohu.



![Image](assets/fr/11.webp)



## Odesílání zpráv pomocí relace



Chcete-li kontaktovat další osoby, klikněte na tlačítko "*+*" na domovské stránce.



![Image](assets/fr/12.webp)



K dispozici je několik možností. Chcete-li vytvořit skupinu nebo se k ní připojit, vyberte možnost "*Vytvořit skupinu*" nebo "*Připojit se ke komunitě*".



![Image](assets/fr/13.webp)



Pokud chcete, aby si vás někdo přidal jako kontakt, můžete mu zadat naskenování ID relace jako QR kódu.



![Image](assets/fr/14.webp)



Chcete-li odeslat přihlašovací údaje na dálku, klikněte na "*Pozvat přítele*". Poté můžete zkopírovat ID relace a odeslat jej jiným komunikačním kanálem. Tyto informace můžete také získat kliknutím na svou profilovou fotografii na domovské stránce.



![Image](assets/fr/15.webp)



Pokud máte ID relace jiné osoby a chcete ji přidat, klikněte na "*Nová zpráva*".



![Image](assets/fr/16.webp)



Jeho identifikátor pak můžete vložit do textu nebo jej přímo naskenovat, pokud jej máte jako QR kód.



![Image](assets/fr/17.webp)



Poté této osobě pošlete úvodní zprávu.



![Image](assets/fr/18.webp)



Jakmile osoba přijme vaši žádost, zobrazí se její uživatelské jméno a vy s ní budete moci volně chatovat.



![Image](assets/fr/19.webp)



## Synchronizace softwaru Desktop



Chcete-li synchronizovat účet v počítači, musíte nainstalovat software. [Stáhněte si jej z oficiálních webových stránek](https://getsession.org/download). Před instalací doporučuji zkontrolovat jeho pravost a neporušenost.



![Image](assets/fr/20.webp)



Při prvním spuštění klikněte na "*Mám účet*".



![Image](assets/fr/21.webp)



Zadejte frázi Mnemonic a nezapomeňte mezi jednotlivými slovy nechat mezeru.



![Image](assets/fr/22.webp)



Nyní můžete ke svým konverzacím přistupovat z počítače.



![Image](assets/fr/23.webp)



Gratulujeme, nyní jste se naučili používat aplikaci Session messaging, která je vynikající alternativou k aplikaci WathsApp!



Doporučuji také tento další tutoriál, ve kterém představuji Threemu, další zajímavou alternativu pro vaši aplikaci pro zasílání zpráv:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74