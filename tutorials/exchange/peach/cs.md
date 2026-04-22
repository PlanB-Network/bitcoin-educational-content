---
name: Peach
description: Kompletní průvodce používáním Peach a obchodováním s bitcoiny v P2P
---

![cover](assets/cover.webp)





## Úvod



Výměny mezi peer-to-peer (P2P) bez KYC jsou nezbytné pro zachování důvěrnosti a finanční nezávislosti uživatelů. Umožňují přímé transakce mezi jednotlivci bez nutnosti ověřování totožnosti, což je zásadní pro ty, kteří si cení soukromí. Podrobnější informace o teoretických konceptech naleznete v kurzu BTC204:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. Co je Peach?



Peach je výměnná platforma P2P, která uživatelům umožňuje nakupovat a prodávat bitcoiny bez nutnosti KYC. Nabízí intuitivní rozhraní a pokročilé bezpečnostní funkce. Ve srovnání s jinými řešeními, jako jsou Bisq, HodlHodl a Robosat, vyniká Peach snadným používáním.


Systém úschov multisignature (2-2) zaručuje bezpečnost finančních prostředků během transakcí. Peach podporuje různé platební metody a je vybaven systémem reputace, který obchodníkům pomáhá při jejich činnostech. Jako obvykle u platforem P2P je proto důležité udržovat si dobrou pověst, abyste si udrželi důvěryhodnost u ostatních obchodníků.



### 2. Ochrana soukromí a shromážděné údaje



**Jaké informace shromažďuje společnost Peach?



Společnost Peach se snaží ukládat naprosté minimum údajů o svých uživatelích. Zde je přehled údajů uložených na našich serverech:





- hash vašeho jedinečného identifikátoru aplikace (AdID)
- hash vašich platebních údajů
- Vaše šifrované konverzace
- Údaje o transakcích, aby se zajistilo, že anonymní uživatelé nepřekročí obchodní limit (typy použitých platebních metod, částky nákupu a prodeje)
- Addresses slouží k odesílání a přijímání z depozitního účtu
- Údaje o používání (Firebase a Google Analytics), pouze s vaším souhlasem



Připomínáme, že hash jsou data, která se podobně jako při šifrování stávají nerozpoznatelnými. Stejná data vždy vytvoří stejný kód hash, což umožňuje odhalit duplikáty bez znalosti původních dat.



*Podrobnější vysvětlení technologie hashing naleznete v tomto kurzu:*



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**Kdo může vidět mé platební údaje?





- Vaše platební údaje vidí pouze vaše protistrana
- Data jsou přenášena prostřednictvím serverů Peach, ale jsou plně šifrována od konce ke konci
- V případě sporu budou vaše platební údaje a historie konverzace viditelné přidělenému zprostředkovateli Peach



## Instalace a konfigurace



### 1. Instalace aplikace Peach



![Installation de Peach](assets/fr/01.webp)





- Aplikaci si stáhněte z [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/). V systému iOS je třeba nejprve nainstalovat aplikaci [testflight](https://apps.apple.com/us/app/testflight/id899247664).
- Postupujte podle pokynů k instalaci v zařízení.
- Během instalace budete vyzváni, abyste si zvolili, zda chcete sdílet určitá data pro vylepšení aplikace Peach. (obrázek 1)
- Na další obrazovce (obrázek 2) máte dvě možnosti:
 - Pokud jste nový uživatel, klikněte na "Nový uživatel" a vytvořte si nový profil
 - Pokud již účet máte, obnovte svůj stávající profil pomocí funkce "Obnovit"
- Pokud máte doporučující kód, můžete ho zadat zde.
- Chcete-li obnovit existující účet (obrázek 3), budete potřebovat :
 - Váš záložní soubor
 - Heslo pro dešifrování tohoto souboru



### 2. Přehled hlavních obrazovek



Aplikace Peach je uspořádána do čtyř hlavních obrazovek přístupných ze spodního navigačního panelu:



![Navigation dans l'application](assets/fr/02.webp)





- Domů (4)** : Hlavní obrazovka, na které můžete vybírat nákup nebo prodej, vytvářet nové transakce a přistupovat k dostupným nabídkám:
 - vytvářet nabídky pomocí dvou tlačítek níže (vytvořit nákup / vytvořit prodej)
 - využít existující nabídky vytvořené jinými uživateli pomocí dvou tlačítek níže ("Koupit"/"Prodat").





- Wallet (5)** : Váš integrovaný bitcoin wallet, který vám umožní :
 - Zkontrolujte si zůstatek
 - Přijímání bitcoinů
 - Envoyer bitcoins (s kontrolou mincí)
 - Zobrazení historie transakcí
 - Financování prodeje





- Obchody (6)**: vaše současné a minulé smlouvy na třech kartách:
 - Probíhající nákupy
 - Probíhající prodej
 - Historie vašich výměn





- Nastavení (7)** : Konfigurační centrum pro
 - Zobrazit svůj profil (pověst, odznaky, limity atd.)
 - Správa zabezpečení (zálohování, pin)
 - Správa platebních metod
 - Kontaktovat podporu
 - Změna jazyka
 - atd.



### 3. Konfigurace platebních metod



![Accès aux paramètres de paiement](assets/fr/03.webp)



Způsoby platby můžete spravovat v nastavení (obrázek 8)



Peach nabízí online platby a osobní platby (pouze na registrovaných setkáních).



**Online platby



**Důležité:**


v zájmu ochrany uživatelů vyžaduje Peach, aby zdroj finančních prostředků odpovídal inzerovanému. Je na obchodnících, aby se o tom v zájmu své vlastní ochrany přesvědčili.



![Configuration des paiements en ligne](assets/fr/04.webp)



Přidání metody :




- Na kartě "online" klikněte na "přidat měnu/metodu"
- Zvolte si měnu
- Vyberte preferovaný způsob platby



*Dostupné typy platebních metod:*



***Pro bankovní převody: ***




- SEPA (standardní nebo okamžitá)
- Vyplňte bankovní údaje SEPA.



***Přijímáme online wallet :***




- V závislosti na zemi máte k dispozici několik možností (Revolut, Paypal, Wise, Strike atd.)
- Podle pokynů přidejte své přihlašovací údaje



*dárková karta použitelná:*** dárková karta použitelná:*** dárková karta použitelná:*** dárková karta použitelná:*** dárková karta použitelná:*** dárková karta použitelná:*** dárková karta použitelná:***




- Amazon, Steam atd.
- Zadejte zemi vydání karty a další potřebné informace



***Národní možnosti platby:***


Platební systémy specifické pro jednotlivé země :




- Satispay (Itálie)
- MB Way (Portugalsko)
- Bizum (Španělsko)
- Rychlejší platby (Velká Británie)
- atd.



***Při osobních platbách: ***



![Configuration des paiements en personne](assets/fr/05.webp)





- Vyberte možnost "Meetup" (obrázek 12)
- Poté si v seznamu vyberte schůzku (obrázek 13)



### Návod k použití





- Můžete přidat několik platebních metod
- Čím více metod přidáte, tím širší nabídku budete mít k dispozici
- Před registrací zkontrolujte správnost svých údajů
- Způsoby platby můžete kdykoli změnit nebo odstranit



**Bezpečnostní poznámka**: Vaše platební údaje jsou zašifrovány a jsou sdíleny pouze s vaším směnným partnerem během transakce, s výjimkou případu sporu, kdy má přístup také zprostředkovatel Peach.



### 4. Jak zabezpečit své portfolio



**Pochopení účtu Peach



Účet Peach nemá uživatelské jméno ani heslo. Jedná se o soubor uložený lokálně v telefonu, což znamená, že Peach nepotřebuje ukládat vaše data ani znát vaši identitu: máte ho pod kontrolou. Tento soubor obsahuje všechna vaše data: včetně 12 slov pro obnovení bitcoinů, klíčů PGP, platebních údajů atd. Proto je velmi důležité tento soubor uložit a chránit ho __důkladným__ heslem.



Tento přístup zaručuje určitou míru důvěrnosti a ponechává odpovědnost za správu dat a záloh v rukou uživatele. Ztráta telefonu bez zálohy znamená ztrátu přístupu k účtu Peach a finančním prostředkům.



**Vytvoření záloh**






- Přístup k nastavení z karty v pravém dolním rohu domovské obrazovky
- V nabídce nastavení vyberte možnost "zálohování"



![Processus de sauvegarde](assets/fr/06.webp)



K dispozici jsou dva typy zálohování:



**Uložení souboru účtu (obrázek 14)**




- Klikněte na "Vytvořit novou zálohu"
- Vytvoření **silného** hesla pro zašifrování záložního souboru
- Tento soubor odešlete na místo, které zajistí jeho redundanci v případě ztráty telefonu.



Záloha souborů obnoví celý účet Peach včetně :




- Vaše portfolio
- Vaše platební metody
- Platební údaje
- Historie transakcí s podrobnostmi o protistranách a rozhovorech s nimi



**Uložení fráze pro obnovení (obrázek 15)**




- Podle pokynů zobrazte frázi pro obnovení
- Pečlivě zapište slova ve správném pořadí
- Tuto zálohu uložte na bezpečném místě, ideálně jinde než soubor s účtem



Fráze pro obnovení umožňuje obnovit :




- Vaše pověst, vaše obchody
- Vaše bitcoinové fondy



Ale **ne** následující:




- Vaše aktuální a minulé konverzace
- Platební údaje
- Informace o protistraně v historii transakcí




## Nákup a prodej bitcoinů



### 1.a Jak koupit bitcoiny: Přijměte nabídku na prodej



Prvním reflexem kupujícího by měla být kontrola nabídek k prodeji, které jsou již financovány pomocí bitcoinů.



![Vue des offres de vente et filtres](assets/fr/07.webp)





- Na domovské obrazovce klikněte na tlačítko "Koupit" (obrázek 16)
- Poté si můžete prohlédnout seznam bitcoinů, které byly vloženy do systému úschovy a jsou připraveny k prodeji (obrázek 17). Můžete si prohlédnout částku, cenu (v % vzhledem k trhu KYC), způsoby platby a přijímané měny.
- Pomocí filtrů můžete nabídky třídit a řadit (obrázek 18).
- Poznámka: Tlačítko v dolní části stránky s filtry umožňuje přijímat oznámení o zveřejnění nabídky odpovídající vašim filtrům a tlačítko "resetovat", které jednoduše vymaže všechny filtry (obrázek 18).



![Sélection et confirmation d'achat](assets/fr/08.webp)





- Prohlédněte si nabídku, která vám vyhovuje, a odešlete žádost o výměnu (obrázek 19)
- Můžete podat několik žádostí o výměnu a první kladná nabídka zruší ostatní žádosti.
- Proveďte platbu dohodnutým způsobem.


**Připomínáme:** zdroj finančních prostředků musí odpovídat zdroji, který jste zadali při přidávání způsobu platby.




- Potvrďte svou platbu v aplikaci, jakmile bude provedena**.
- Počkejte, až prodávající obdrží platbu, a prohlaste ji za platbu (obrázek 20)
- A nakonec zhodnoťte své zkušenosti s prodejcem (obrázek 21)



![Réception des bitcoins](assets/fr/09.webp)





- Sledování stavu transakce
- Kontrola potvrzení o přijetí bitcoinů
- Finanční prostředky budou k dispozici v portfoliu Peach (obrázek 22 a 23)



### 1.b Jak koupit bitcoiny: Vytvořte nabídku



Pokud nenajdete vhodnou nabídku k prodeji, můžete vytvořit nabídku ke koupi. Protože tím v této fázi nezavazujete žádné bitcoiny, budete mít menší šanci najít partnera pro výměnu, zejména pokud jsou vaše dosavadní výsledky a pověst špatné nebo žádné. Chcete-li to napravit, je důležité při vytváření nabídky *předložit nabídku s vysokou prémií*, abyste prodávající motivovali k výběru vaší nabídky. Pokračujme dále:



![Creation d'ordre d'achat](assets/fr/10.webp)





- Na domovské obrazovce klikněte na tlačítko "Vytvořit nabídku nákupu" (obrázek 24)
- Přidejte způsob platby, pokud jste tak ještě neučinili, a zadejte své preference (množství, prémii atd.) (obrázek 25).


Možnost "okamžitě" umožňuje automaticky přijmout požadavek na obchod.




 - Pro pokračování klikněte znovu na "vytvořit nabídku"
- Po vytvoření je řada na prodávajících, aby se na vás obrátili s žádostí o výměnu. Aplikaci můžete bez obav zavřít a opustit.
- Pokud neobdržíte žádné žádosti, můžete pojistné změnit. Nezapomeňte: vyšší prémie bude prodávající motivovat k tomu, aby si přišli pro vaši nabídku (obrázek 26).
- Nabídku najdete na kartě "Koupit", která se sama nachází v okně "Exchange" (obr. 27)



![Reception d'une demande de vente, messagerie](assets/fr/11.webp)





- Když obdržíte žádost o nákup (obr. 28) (a pokud jste nedeaktivovali okamžitý obchod na obr. 25), přijměte obchod po kontrole reputace prodávajícího. Pokud je okamžitý obchod povolen, přejděte přímo na obrázek 29.
- Prodávající pak musí bitcoiny uložit do systému úschovy ("financovat trezor"). (obrázek 29)
- Poté zaplaťte prodávajícímu na místě určení uvedeném na obr. 30 prostřednictvím svého osobního bankovního systému. Dokud tak neučiníte, nepřetahujte kurzor "Provedl jsem platbu"!
- S prodejcem můžete komunikovat prostřednictvím systému zasílání zpráv (šifrovaně P2P). V případě problému můžete zahájit spor kliknutím na ikonu v pravém horním rohu (obrázek 31). Do diskuse poté vstoupí zprostředkovatel Peach.



![Offre de vente completée](assets/fr/12.webp)





- Jakmile prodávající obdrží peníze, nahlásí je a systém úschovy uvolní bitcoiny, které budou na cestě do vašeho účtu wallet (standardně prostřednictvím GroupHug, systému seskupování transakcí Peach, který se spouští jednou denně),
- Ohodnoťte své zkušenosti s prodejcem



A je to!



**Poznámka pro nové kupující:** prodávající vycházejí z pověsti kupujících a mají tendenci vyhýbat se nabídkám od kupujících bez dokončených obchodů. V první řadě je snazší vybudovat si reputaci tím, že přijmete existující nabídky k prodeji.




### 2.a Jak prodávat bitcoiny: Vytvořte prodej



Nejrychlejší a nejjednodušší způsob prodeje na Peach je **vytvořit nabídku k prodeji**.



![Création d'un ordre de vente](assets/fr/13.webp)





- Na domovské stránce klikněte na "Vytvořit prodejní nabídku" (obrázek 32)
- Nastavte nabídku, zkontrolujte, zda jste vložili způsob platby a správné parametry


můžete také :




  - vytvořit několik stejných nabídek
  - aktivovat "okamžitou výměnu", aby první kupující, který se objeví, mohl převzít smlouvu (bez vašeho potvrzení) a pokračovat v platbě.
  - zvolit adresu pro vrácení peněz
  - financovat kufr z vašeho wallet Peach
- Transakci financujte odesláním bitcoinů na zadanou adresu (obrázek 34)
- Počkejte na potvrzení transakce. Jakmile se tak stane, bude vaše nabídka viditelná na trhu.



![Attente du paiement](assets/fr/14.webp)





- Počkejte, až kupující přijme vaši nabídku. Chcete-li situaci urychlit, zvažte zvýšení pojistného (%) (obrázek 36)
- Jakmile obdržíte žádost o výměnu, zkontrolujte pověst kupujícího. Sami posuďte, zda je pro vás profil vhodný, a pokud ano, klikněte na tlačítko "přijmout". (37)
- Nyní je na řadě kupující, aby provedl platbu ze své banky do vaší. Ten vám pak platbu přepošle. Neváhejte kupujícího kontaktovat v chatu.
- po kontrole, že vaše banka obdržela finanční prostředky*, je uvolněte kliknutím na tlačítko "přijal jsem platbu" (obrázek 38). Nikdy nepotvrzujte přijetí platby dříve, než zkontrolujete, že byla přijata na váš účet.
- Vyhodnocení transakce
- Modely Bitcoin jsou automaticky uvolněny kupujícímu,



Tady to máte!



**Bezpečnostní pokyny a tipy pro úspěšnou transakci:**




 - Sledujte údaje kupujícího a zkontrolujte, zda původ prostředků odpovídá původu popsanému na Peach. Pokud původ prostředků neodpovídá oznámenému, přejděte na Chat, otevřete hádku (obrázek 39) a odešlete prostředky zpět na místo jejich původu.
 - Postupujte podle pokynů ve žluté kočce.
 - Rychle reagujte na zprávy od protistrany
 - pozor na přístup kupujícího, zejména pokud se jedná o profil s malými zkušenostmi
 - Pokud máte problém, neváhejte využít mediační službu



### 2.b Jak prodat bitcoiny: nabídka



Je také možné zobrazit a vybrat nabídky nákupu. Musíte být obzvláště opatrní, protože právě zde se vyskytuje nejvíce podvodníků.



![Prendre une offre d'achat](assets/fr/15.webp)





- Na domovské stránce klikněte na položku "Prodej" (obrázek 40)
- Pomocí filtrů si můžete prohlédnout a vybrat nejatraktivnější nabídky (obrázek 41)



![vérification de la réputation](assets/fr/16.webp)





- před podáním žádosti o obchod doporučujeme posoudit vhodnost profilu kupujícího. Můžete kliknout na nabídku a poté na ID uživatele a zobrazit jeho profil. Například nabídka na obrázku 42 by mohla být považována za "rizikovou" (nový uživatel, relativně vysoká částka). "Riziko", kterému se vystavujete přijetím této nabídky, spočívá pouze ve ztrátě času, pokud neuděláte chybu a neuvolníte bitcoiny, aniž byste obdrželi peníze. Bitcoiny můžete stále uložit do trezoru.


Naproti tomu ten na obrázku 43 pochází od zkušeného obchodníka (obrázek 44) a v jeho historii nejsou žádné spory. Jedná se tedy o méně rizikovou nabídku.



![Match avec vendeur](assets/fr/17.webp)





- Po vyžádání nabídky, pokud kupující vaši žádost přijme, se aplikace přesune na obrázek 34, kde můžete pokračovat v obchodování, jak je popsáno níže.




## Výhody a nevýhody



### Výhody Peach





- KYC není vyžadováno**: Zachovává důvěrnost informací o uživateli.
- Žádný přístup k bankovním údajům**: Peach nemá přístup k vašim bankovním údajům ani k vaší identitě.
- Interface intuitivní**: Snadné použití pro středně pokročilé uživatele.
- Open Source** : Zdrojový kód je veřejný a ověřitelný komunitou.



### Nevýhody Peach





- Omezená Liquidity**: Menší objem obchodů než u zavedenějších platforem.
- Regulační riziko** : Aplikaci spravuje švýcarská společnost. Podléhá proto švýcarským předpisům, které se mohou vyvíjet a případně aplikaci cenzurovat.



## Užitečné zdroje





- Francouzské vysvětlující video: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Stručný průvodce: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)
- [Support telegram](t.me/peachtopeach) (pozor na podvodníky, administrátoři vám nikdy nenapíší první soukromou zprávu)