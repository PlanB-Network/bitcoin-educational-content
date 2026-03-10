---
name: Delta Chat
description: Praktický průvodce decentralizovaným nástrojem pro zasílání zpráv
---

![image](assets/cover.webp)




## Úvod - Kontrola chatu a soukromí



V posledních letech se stále častěji hovoří o regulačním návrhu Chat Control, jehož cílem je zavést automatické skenování soukromých zpráv na hlavních komunikačních platformách. Deklarovaným cílem je boj proti nelegálnímu obsahu, problémem je, že tento mechanismus by ve skutečnosti zahrnoval masový dohled, který by narušil end-to-end šifrování, a tím i soukromí všech uživatelů, nejen pachatelů.



Skutečné riziko spočívá v tom, že se chaty stanou kontrolovaným prostředím, kde může být každá zpráva, obrázek nebo příloha zkontrolována ještě předtím, než se dostane k příjemci. A právě zde přichází jedno z možných řešení: odklon od centralizovaných platforem a přechod k decentralizovaným systémům pro zasílání zpráv, které nejsou závislé na jediném poskytovateli a nemohou být snadno podrobeny takové kontrole.



Jedno takové řešení bude představeno v tomto výukovém kurzu: Delta Chat. Jedná se o vyspělý a již použitelný nástroj.




## Proč Delta Chat a jak funguje



Delta Chat je již velmi dobré řešení pro zasílání zpráv pro každodenní použití: velmi užitečné pro komunikaci s přáteli, rodinou a dalšími lidmi, stejně jako skutečná obdoba aplikace WhatsApp.



Jedná se o decentralizovaný systém zasílání zpráv založený výhradně na e-mailu. V podstatě využívá infrastrukturu tradičního e-mailu, ale na jejím základě vytváří moderní rozhraní a prostředí instant messengeru. Na první pohled se to může zdát trochu improvizované, ale ve skutečnosti to funguje velmi dobře a je to překvapivě robustní. Můžete používat specializované poštovní servery s názvem ChatMail, ale může také bezproblémově spolupracovat s běžnými e-mailovými servery. To znamená, že pokud chcete, můžete se přihlásit pomocí stávajícího účtu, aniž byste museli vytvářet něco nového.



Další zajímavostí je podpora WebXDC, což jsou malé webové aplikace, které lze používat přímo v chatech, podobně jako miniaplikace v Telegram. Důležitým rozdílem je, že tyto aplikace nemají přístup k internetu, takže nemohou sledovat uživatele ani odesílat data navenek.



Z hlediska zabezpečení používá Delta Chat ověřené end-to-end šifrování založené na PGP, ale s moderními rozšířeními, díky nimž je úroveň ochrany srovnatelná s Signal. Jediným současným nedostatkem je Perfect Forward Secrecy, ale to je vyvíjející se aspekt.



Vzhledem k tomu, že Delta Chat je založen výhradně na e-mailu, zcela se mu vyhýbá:




- povinná telefonní čísla
- Centralizované ID
- registrace spojené s jednou službou



A právě díky tomu je tento nástroj velmi odolný vůči invazivním regulacím, jako je například Chat Control.




## Instalace



Na oficiálních stránkách [Delta Chat](https://delta.chat/download) můžete přejít do sekce Ke stažení. V Linuxu je pohodlně dostupný prostřednictvím Flathubu, ale existují také balíčky pro Arch, NixOS, Snap a samostatné verze.



![image](assets/it/01.webp)



K dispozici je také pro:




- [F-Droid](https://f-droid.org/app/com.b44t.messenger)
- [Obchod Play](https://play.google.com/store/apps/details?id=chat.delta)
- [iOS](https://apps.apple.com/it/app/delta-chat/id1459523234)
- [Windows](https://apps.microsoft.com/detail/9pjtxx7hn3pk)
- [macOS](https://apps.apple.com/it/app/delta-chat-desktop/id1462750497)
- [Ubuntu Touch](https://open-store.io/app/deltatouch.lotharketterer)
- a další obchody...



Pokud hledáte návod k instalaci F-Droid, mohl by vám pomoci tento návod:



https://planb.academy/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

Jedna velmi důležitá věc: verze pro stolní počítače nevyžadují telefon. Na rozdíl od aplikací WhatsApp nebo SimpleX Chat se nemusíte nejprve registrovat z mobilu. Profil si můžete vytvořit přímo v počítači nebo jej přenést z jiného zařízení.




## Vytvoření profilu



Po otevření aplikace se aplikace Delta Chat zeptá, zda chcete vytvořit nový profil, nebo použít stávající.



![image](assets/it/02.webp)



Vytvořením nového profilu můžete zadat:




- jméno
- obrázek (nepovinné)



Ve výchozím nastavení je navržen server ChatMail, ale je to možné:




- vybrat jiný server ChatMail
- používat klasický e-mailový účet
- ručně nakonfigurovat protokoly IMAP a SMTP
- zaregistrovat se pomocí pozvánky jiného uživatele



Po několika sekundách je profil připraven a můžete začít aplikaci používat.



![image](assets/it/03.webp)




## Interface a chat



Rozhraní je velmi jednoduché a přehledné:




- Zprávy zařízení, které jsou místní komunikací
- Uložené zprávy, podobné těm v Telegram a synchronizovatelné mezi zařízeními



![image](assets/it/04.webp)



Chcete-li přidat kontakt, jednoduše:




- Zobrazení kódu QR
- Naskenujte údaje o druhé osobě
- Pozvání prostřednictvím odkazu (sdílejte odkaz na pozvánku).



![image](assets/it/05.webp)



Po navázání spojení se automaticky nakonfiguruje koncové šifrování. Uživatelské rozhraní chatu je velmi podobné rozhraní aplikace WhatsApp:




- textové a hlasové zprávy
- fotografie, videa a soubory
- odpovědi na zprávy
- reakce
- vyskakovací zprávy
- přizpůsobitelná oznámení.



![image](assets/it/06.webp)



## WebXDC: aplikace v chatech:



Delta Chat umožňuje používat WebXDC, tj. malé aplikace vložené do konverzací. Zde je krátký seznam těch nejužitečnějších, které byly identifikovány:




- průzkumy
- rýsovací prkna
- dočasné soukromé chaty
- hry se sdílenými výsledky chatu



Lze spustit i složitější hry, což dokazuje flexibilitu tohoto nástroje.



![image](assets/it/07.webp)



## Skupiny, kanály a pokročilé funkce



Můžete vytvářet skupiny, používat nálepky (zejména na plochách) a po aktivaci experimentálních možností i kanály, podobně jako v Telegram.



V rozšířeném nastavení můžete zapnout:




- hlasové hovory (stále experimentální)
- pokročilá správa e-mailových profilů
- úplné zálohy.



![image](assets/it/08.webp)



## Více zařízení a zálohování



Delta Chat plně podporuje více zařízení:




- můžete přidat druhé zařízení pomocí QR kódu
- můžete provést úplný přenos prostřednictvím zálohování.



Během několika sekund opět najdete své konverzace, skupiny a kompletní historii, aniž byste byli závislí na centrálním serveru.



![image](assets/it/09.webp)




## Závěr



V době, kdy se stále častěji mluví o kontrole soukromé komunikace, představuje Delta Chat konkrétní odpověď: decentralizované šifrované zasílání zpráv, které je skutečně použitelné každý den.



Je to řešení, které mě ze všech, které jsem vyzkoušel, nejvíce přesvědčilo o své jednoduchosti, soukromí a svobodě. Pokud chcete, můžete mě také kontaktovat na Delta Chatu prostřednictvím následujícího [odkaz na pozvánku](https://i.delta.chat/#38824F04DD40600D5D4F079C1F5E0EBA875A6D7E&i=GStGfNW5LMIXhwQMiuQWj3QU&s=cVi5izRJ9NsbIcPlU8yC_SeB&a=9l4la5imj%40nine.testrun.org&n=SatoSats)



Pokud se vám tento průvodce líbil, můžete mě podpořit tím, že mi přispějete a zanecháte palec nahoru. A nezapomeňte: teprve používáním a prozkoumáváním aplikace Delta Chat z mobilního i stolního počítače skutečně objevíte její plnou funkčnost.



Do příště.