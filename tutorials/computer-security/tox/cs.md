---
name: Tox
description: Otevírání konverzací bez prostředníků na decentralizovaném protokolu Tox
---
![cover](assets/cover.webp)



Koncové šifrování je služba, kterou nabízí mnoho aplikací pro zasílání zpráv, například WhatsApp a Telegram. Šifrování zde znamená, že než odesílatel zprávu odešle, je zabezpečena kryptografickým zámkem, ke kterému má klíč pouze příjemce. Dnes se vydáme objevit zcela decentralizovanou aplikaci pro šifrování zpráv od konce ke konci, která je založena na podobných principech jako Blockchain a nabízí bezpečnou šifrovanou komunikaci od konce ke konci bez prostředníků: Tox Chat.



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
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = End-to-end šifrování*



## Co je to Tox?



Tox je svobodný (open source) decentralizovaný komunikační protokol, který využívá technologii *Networking and Cryptography Library* (NaCl) a kombinace šifrovacích algoritmů k zajištění bezpečnosti a důvěrnosti svých uživatelů. Tox umožňuje bezpečně, decentralizovaně a bez prostředníků posílat textové zprávy Exchange, uskutečňovat audio a video hovory, sdílet soubory a sdílet obrazovku s přáteli.



Technologie, kterou protokol Tox využívá, je podobná peer-to-peer sítím, jako jsou blockchainy, což podporuje decentralizaci infrastruktury protokolu. Na rozdíl od sociálních sítí a aplikací pro zasílání zpráv šifrovaných end-to-end je aplikace Tox Chat postavena na decentralizovaném protokolu, který nemá žádný centrální server. Všichni uživatelé komunikují v síti peer-to-peer bez prostředníků, která je odolná vůči cenzuře. Při komunikaci je každý uživatel identifikován pomocí jedinečného ID (ToxID) odvozeného z jeho veřejného klíče, který je uložen v distribuované tabulce Hash .



## Připojte se k Tox



Protokol Tox můžete používat prostřednictvím klienta pro zasílání rychlých zpráv, kterého si můžete stáhnout z webu [Tox Chat](https://tox.chat).



![download](assets/fr/01.webp)



V závislosti na operačním systému si můžete stáhnout a nainstalovat klienta Tox, který odpovídá :





- aTox: [aTox](https://github.com/evilcorpltd/aTox), klient Tox napsaný v jazyce Kotlin, který je k dispozici pouze pro Android



![aTox](assets/fr/02.webp)





- qTox: [open source](https://github.com/TokTok/qTox) založený na Qt Frameworku (C++), dostupný pro Windows, Linux, MacOs.



![qTox](assets/fr/03.webp)





- Toxic: [Toxic](https://github.com/JFreegman/toxic) je klient Toxu napsaný v jazyce C a spuštěný na systémech s rozhraním příkazového řádku.



![Toxic](assets/fr/04.webp)



V tomto tutoriálu budeme ke komunikaci používat klienty qTox v systému Windows a aTox.



## Začínáme s qTox



Po stažení nainstalujte klienta Tox a vytvořte si profil.



![qTox-acount](assets/fr/05.webp)



Gratulujeme, právě jste se připojili k protokolu Tox. V softwaru qTox najdete informace o svém profilu kliknutím na své uživatelské jméno.



![profil](assets/fr/06.webp)



Najdete zde zejména své Tox ID, které můžete uložit jako QR kód a sdílet s lidmi, kteří vás chtějí kontaktovat.



Exportujte soubor profilu Tox, abyste měli zálohu profilu a kontaktních informací, kterou můžete použít k obnovení. Klikněte na tlačítko **Export** a poté vyberte cestu k záložnímu souboru.



![export](assets/fr/07.webp)



V nabídce **Další** můžete přidávat přátele, importovat kontakty a spravovat přijaté žádosti o přátelství.



![friends](assets/fr/08.webp)



Můžete mě kontaktovat například prostřednictvím tohoto Tox ID: EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F



Po odeslání žádosti o přátelství bude muset příjemce vaši žádost přijmout nebo odmítnout, teprve pak ho budete moci kontaktovat.



![request](assets/fr/09.webp)



Klient Tox obsahuje všechny možnosti, které nabízejí aplikace pro zasílání rychlých zpráv:





- Videohovory





- Hlasové hovory





- Sdílení souborů





- emotikony



![chat](assets/fr/10.webp)



### Peer-to-peer skupiny



Klienti Tox vám také umožňují komunikovat se skupinou lidí zcela decentralizovaným způsobem: říká se jim konference. V nabídce **Skupiny** vytvořte novou konferenci nebo se podívejte do seznamu pozvánek k účasti na konferencích, které jste obdrželi.



![conferences](assets/fr/11.webp)



Po vytvoření konference můžete pozvat své přátele, aby se k ní připojili v klientovi Tox. V seznamu přátel klikněte pravým tlačítkem myši na uživatelské jméno přítele, kterého chcete pozvat. Klikněte na možnost **Pozvat na konferenci** a poté vyberte název konference, kterou jste vytvořili. Přítele můžete pozvat také implicitním vytvořením konference pomocí možnosti **Vytvořit novou konferenci**.



klienti ⚠️ Tox jsou stále ve fázi vývoje, takže se při práci se softwarem můžete setkat s chybami. Funkce konferencí a videohovorů zatím nejsou v klientovi Tox pro Android (aTox) k dispozici.



![invite](assets/fr/12.webp)



### Přenosy souborů



V nabídce **Přenosy souborů** najdete historii odeslaných souborů a souborů přijatých od kontaktů.



![files](assets/fr/13.webp)



Konfigurace sdílení souborů můžete také přizpůsobit pro každou diskusi, kterou vedete. Klikněte pravým tlačítkem myši na uživatelské jméno příjemce a vyberte možnost "Zobrazit další podrobnosti".



![details](assets/fr/14.webp)



V podrobnostech modulu Interface můžete spravovat oprávnění, která jste příjemci udělili pro :





- Automatické přijímání pozvánek na konference.





- Automatické přijímání souborů.





- Záložní cesty k souborům diskuse.



![permissions](assets/fr/15.webp)



### Další parametry



V nabídce **Nastavení** můžete upravit nastavení klienta Tox.





- V části **Obecné** změňte základní jazyk klienta Tox, definujte cesty zálohování souborů a maximální velikost souborů, které mají být automaticky přijímány.



![general](assets/fr/16.webp)





- V části **Uživatel Interface** upravte písma a velikosti zpráv. Můžete také změnit téma klienta Tox.



![ui](assets/fr/17.webp)





- Na kartě **Soukromí** můžete definovat pomíjivé zprávy zrušením zaškrtnutí políčka "Uchovávat historii chatu". Můžete také změnit svůj kód Nospamu, když zjistíte, že jste spamováni žádostmi o přátelství, kliknutím na tlačítko "generate náhodný kód NoSpam".



![privacy](assets/fr/18.webp)



### Co zaručuje důvěrnost informací o službě Tox?



Protokol Tox využívá distribuovanou tabulku Hash k vytvoření sítě decentralizovaných uzlů. Každý klient Tox je součástí sítě DHT a ukládá informace o ostatních uzlech. V případě Tox ukládá DHT IP adresy jako hodnoty spojené s veřejnými klíči Tox (Tox ID). Díky tomu je možné snadno vyhledat zařízení klienta Tox, aniž by bylo nutné se dotazovat centrálního serveru.



Představte si, že píšete našemu uživateli `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F`, kterého pojmenujeme **uživatel B**. Váš klient Tox vyhledá tento identifikátor v tabulce Hash Distributed a získá přidruženou IP adresu Address. Jakmile bude IP Address nalezen, váš klient Tox vytvoří přímý šifrovaný komunikační kanál s naším počítačem **uživatele B** nebo použije jiné uzly jako relé, aby se dostal k **uživateli B**. Šifrovací algoritmy zajistí, že bez ohledu na komunikační kanál bude moci obsah vaší zprávy přečíst pouze **uživatel B**.



Pokud se vám objevování Toxu líbilo a dokázali jste pochopit, jak je užitečný pro posílení vašeho soukromí, neváhejte dát tomuto návodu palec nahoru. Doporučujeme také náš tutoriál o nástroji Simple Login, který vám umožní přijímat a odesílat e-maily anonymně.



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41