---
name: Wallet of Satoshi - Vlastní úschova
description: Zjistěte, jak nakonfigurovat režim vlastní úschovy portfolia Wallet of Satoshi
---

![cover](assets/cover.webp)



***Není to vaše klíče, nejsou to vaše mince* je víc než jen rčení, je to základní princip Bitcoin, což znamená, že pokud nemáte pod kontrolou **privátní klíče**, které odemykají vaše bitcoiny, ve skutečnosti je nevlastníte.



Mnoho uživatelů zpravidla začíná s **používajícím wallet** a poté přechází na **samostatně používající wallet**, kde si své soukromé klíče řídí sami.


V tomto návodu vás nebudeme seznamovat s novou samoobslužnou knihovnou wallet. Místo toho vás seznámíme s novou funkcí ***Wallet of Satoshi*** wallet: **samostatný kustodický režim**.



Cílem této nové integrace je umožnit uživatelům zachovat si kontrolu nad svými soukromými klíči a zároveň využívat jednoduchost a plynulost uživatelského prostředí.



Než se dostaneme k jádru věci, věnujme chvíli speciálnímu režimu vlastní úschovy, který nabízí Wallet of Satoshi (WoS).



## Zvláštnost režimu vlastní úschovy



Jednoduchost a plynulost režimu vlastního úschovy služby WoS eliminuje složitost otevírání kanálů Lightning, správy uzlů... Jak je to ale možné?



Samočinný režim Wallet of Satoshi je poháněn systémem **Spark**. Jedná se o řešení Layer 2 pro Bitcoin vytvořené společností Lightspark, které využívá technologii **statechains**.



V důsledku toho neprovádíte transakce přímo na terminálu Lightning Network. Interakce mezi sítí **LN** a sítí **Spark** probíhají prostřednictvím **atomických výměn**.



Například společnost Bob si přeje zaplatit fakturu Lightning pomocí služby WoS. Převede své satoshi, ale ty jsou na pozadí přesměrovány na **Spark Service Provider (SSP)** v síti Spark, který následně provede platbu v síti Lightning.



Naproti tomu společnost Alice chce získat finanční prostředky přímo ze svého portfolia WoS. V tomto případě **SSP** obdrží sats prostřednictvím LN a okamžitě připíše prostředky do portfolia Alice.



Je tedy důležité si uvědomit, že pokud chcete využívat jednoduchost a plynulost WoS, musíte být závislí na serverech Spark. Z hlediska bezpečnosti však máte v případě, že se SSP stane škodlivým nebo nedostupným, k dispozici mechanismus **jednostranného odchodu**, což je bezpečnostní opatření, které vám umožňuje získat zpět své prostředky na Bitcoin on-chain (i když to může být pomalé a nákladné) , což zaručuje vlastní úschovu srovnatelnou s privátním uzlem Lightning.



S přihlédnutím ke všem těmto parametrům se můžete rozhodnout, kolik sats si chcete ponechat ve vlastní úschově WoS.



Pokud jste v Wallet of Satoshi noví, musíte si samozřejmě stáhnout mobilní aplikaci wallet. Pokud ji však již používáte a chcete se dozvědět, jak používat **samostatný režim**, přejděte rovnou na část **Konfigurace samostatného režimu** tohoto návodu.



## Začínáme s Wallet of Satoshi



Přejděte do obchodu s aplikacemi a stáhněte si WoS.



![screen](assets/fr/03.webp)



Po dokončení stahování otevřete aplikaci a stiskněte tlačítko **Start**.



![screen](assets/fr/04.webp)



Budete přesměrováni do hlavního rozhraní aplikace. Při prvním přístupu do WoS je portfolio ve skutečnosti již funkční a ve výchozím nastavení se systematicky otevírá v režimu úschovy.



![screen](assets/fr/05.webp)



I když nechcete používat službu WoS v režimu správce, doporučujeme ji nejprve nakonfigurovat. Chcete-li tak učinit, nahlédněte do tohoto návodu.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Přejděme ke konfiguraci našeho systému WoS v režimu vlastní úschovy.



## Konfigurace režimu vlastního opatrování



Klikněte na nabídku hamburgeru (ikona 3 sloupců) v pravém horním rohu hlavního rozhraní.



![screen](assets/fr/06.webp)



Poté v zobrazené nabídce klikněte na **Otevřít podnabídku Self Custody Wallet**.



![screen](assets/fr/07.webp)



WoS vám okamžitě oznámí, že *režim vlastní péče je spojen s frází o obnově. Také jste výhradně zodpovědní za bezpečnost svých prostředků*.



![screen](assets/fr/08.webp)



Zaškrtněte tlačítko "**Rozumím**" (1) a poté stiskněte tlačítko **Otevřít Self Custody Wallet** (2), které se zobrazí jasně žlutou barvou.



![screen](assets/fr/09.webp)



### Vytvoření portfolia pro vlastní péči



Po kliknutí na tlačítko **Otevřít kartu Wallet pro vlastní úschovu** klikněte na tlačítko **Vytvořit novou kartu Wallet**.



![screen](assets/fr/10.webp)



Společnost WoS pro vás poté vytvoří portfolio pro vlastní úschovu, opět v rámci stejné aplikace. Budete moci kdykoli přepínat mezi režimem **péče o majetek** (dostupný v některých regionech) a režimem **samopéče o majetek**, jak se vám to bude hodit.



![screen](assets/fr/11.webp)



Po vytvoření budete přesměrováni na hlavní rozhraní WoS pro vlastní úschovu. Všimněte si, že mezi obecným přehledem a rozhraním portfolia WoS custody a portfolia WoS self-custody nejsou žádné rozdíly.



### Uložení mnemotechnické fráze



Klepněte na ikonu **Klíčenka + zálohování Wallet** umístěnou v horní části obrazovky mezi názvem Wallet of Satoshi a hamburgerovou nabídkou.



![screen](assets/fr/12.webp)



WoS nabízí dva různé způsoby uložení 12 slov (mnemotechnických frází): **zálohování přes Disk Google** a **ruční zálohování**.



Přestože doporučujeme ruční zálohování, které je nejbezpečnější, ukážeme vám také, jak zálohovat prostřednictvím Disku Google.



#### Zálohování přes Disk Google



Klikněte na tlačítko **Zálohování na Disku Google**.



![screen](assets/fr/13.webp)



Pokud se rozhodnete pro zálohování pomocí Disku Google, existuje vysoké riziko, že bude váš účet Google ohrožen. Zlomyslná osoba by měla přístup k souboru obsahujícímu vašich 12 slov, a mohla by tak získat přístup k vašemu účtu wallet.



Přidání hesla k zašifrování souboru obsahujícího 12 slov je jistě dobrým způsobem, jak přidat další vrstvu zabezpečení.



V rozšířených možnostech proto aktivujte tlačítko **Šifrovat pomocí hesla**.



![screen](assets/fr/14.webp)



V novém rozhraní, které se zobrazí, nastavte silné heslo a znovu jej potvrďte.



![screen](assets/fr/15.webp)



Je důležité mít na paměti, že jakmile si heslo zvolíte, nesmíte ho zapomenout nebo ztratit médium, na kterém jste ho napsali. Pokud jej zapomenete nebo ztratíte, nebudete mít již nikdy přístup ke svým 12 slovům, a tedy ani k finančním prostředkům.



Po zvolení hesla vyberte účet Google pro zálohování a poté povolte přístupy požadované službou WoS.



![screen](assets/fr/16.webp)



![screen](assets/fr/17.webp)



Počkejte několik sekund. Bingo! Zálohování bylo úspěšně dokončeno.



![screen](assets/fr/18.webp)



Vždy máte možnost vytvořit další zálohu, a to výběrem druhé metody zálohování: ručního zálohování.


#### Ruční zálohování



Pokud se rozhodnete pro ruční zálohování, důrazně doporučujeme prostudovat tento návod, který se zabývá osvědčenými postupy pro bezpečné zálohování mnemotechnické fráze, abyste neztratili přístup ke svým bitcoinům.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Stiskněte tlačítko **Ruční zálohování**.



![screen](assets/fr/19.webp)



V následujícím rozhraní vás systém WoS upozorňuje na několik bezpečnostních opatření, která je třeba vzít v úvahu před zahájením ručního zálohování.



Aktivujte tlačítko **Rozumím** a stiskněte tlačítko **Další**.



![screen](assets/fr/20.webp)



Poté se vám zobrazí 12 slov. Uložte je a klikněte na tlačítko **Další**.



![screen](assets/fr/21.webp)



Na tomto novém rozhraní stiskněte slova ve správném pořadí.



![screen](assets/fr/22.webp)



Nakonec klikněte na tlačítko **Další**. Gratulujeme! Vaše zálohování je nyní dokončeno.



![screen](assets/fr/23.webp)



## Obnova portfolia pro vlastní úschovu



Pokud chcete obnovit nebo obnovit službu WoS self-custody wallet po změně telefonu nebo z jiného důvodu, postupujte podle následujících kroků.



Chcete-li otevřít portfolio WoS, klikněte na hamburgerové menu v pravém horním rohu hlavního rozhraní.


V zobrazené nabídce klikněte na **Otevřít podnabídku Self Custody Wallet**.


V novém rozhraní, které se zobrazí, stiskněte tlačítko **Obnovit stávající Wallet**.



![screen](assets/fr/24.webp)



Vyberte metodu obnovy a přejděte k dalšímu kroku.



![screen](assets/fr/25.webp)



### Obnovení prostřednictvím Disku Google



1. Stiskněte tlačítko **Obnovit z Disku Google**.


2. Vyberte účet Google a nechte WoS načíst data pro obnovení uložená na vašem Disku Google.


3. Poté zadejte své šifrovací heslo (pokud jste ho samozřejmě předtím definovali) ze souboru obsahujícího 12 slov.


4. Počkejte několik okamžiků, než se obnovení projeví, a budete mít opět přístup ke svému portfoliu.



### Ruční obnova



1. Stiskněte tlačítko **Restore Manually**.


2. Poté zadejte 12 slov své mnemotechnické fráze a napište každé slovo před jeho počáteční číslo.


3. Počkejte několik okamžiků, než se obnovení projeví, a budete mít opět přístup ke svému portfoliu.




### Převod bitcoinů mezi úschovou WoS a vlastní úschovou WoS



Pokud máte bitcoiny (sats) ve svém WoS custody wallet a vytvoříte WoS self-custody wallet, o své prostředky nepřijdete. A co víc, můžete je převést do svého self-custody portfolia a naopak.



Za tímto účelem :


Můžete zkopírovat svou bleskovou adresu pro vlastní úschovu WoS nebo vytvořenou fakturu.



![screen](assets/fr/26.webp)



Nyní otevřete své opatrovnictví wallet a stiskněte tlačítko **Envoyer**.



Poté vložte adresu nebo fakturu. Podruhé stiskněte tlačítko **Envoyer**.



Vraťte se do svého portfolia s vlastní úschovou a uvidíte, že jste prostředky skutečně obdrželi.



![screen](assets/fr/27.webp)



## Odesílání a přijímání bitcoinů



Pokud jde o odesílání a přijímání bitcoinů v režimu self-custody, stejně jako obecný přehled a rozhraní se neliší od odesílání a přijímání bitcoinů prostřednictvím WoS custody wallet.



Přečtěte si základní návod k použití Wallet of Satoshi v síti Plan₿.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Nyní můžete sami konfigurovat a provozovat systém Wallet of Satoshi v režimu vlastního úschovy.



Pokud pro vás byl tento návod užitečný, zanechte mi prosím níže zelený palec. Moc vám děkuji!