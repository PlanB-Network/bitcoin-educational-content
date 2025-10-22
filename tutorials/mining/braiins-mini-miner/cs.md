---
name: Braiins Mini Miner
description: Snadná výroba Mining z domova.
---
![cover](assets/cover.webp)



## Úvod



Mini Miner braiins BMM 100 je produkt vytvořený společností Mining pool Braiins. Toto zařízení má atraktivní design a je mimořádně tiché. Produkuje výpočetní výkon 1,1 Th/s a spotřebuje přibližně 40 W. Na rozdíl od jiných zařízení není open source, ale jeho instalace je opravdu snadná, zabere opravdu jen několik kliknutí! Mini Miner BMM 100 je první vydanou verzí. Nyní se vyrábí verze 2 s názvem BMM 101, která se od té první liší větším displejem a přítomností Wi-Fi, ale postupy instalace jsou stejné.



Mnohem více důležitých informací najdete také v kompletní příručce přímo na stránkách [výrobce](https://braiins.com/hardware/mini-Miner-bmm-100).



## Přehled BMM 100



zařízení vypadá jako rovnoběžník s displejem na přední straně



![image](assets/en/01.webp)



ventilátor na horní straně



![image](assets/en/02.webp)



na zadní straně je otvor pro napájení, prostor pro kartu SD (která může být potřebná pro případné aktualizace), malé tlačítko s nápisem `IP REPORT`, které vás informuje o IP Address mini Miner, který Address je potřebný pro přístup k ovládacímu panelu zařízení. Po stisknutí tlačítka se IP Address zobrazí asi na 5 sekund, poté zmizí a znovu se objeví obrazovka nastavení. Pokud však potřebujete změnit některá nastavení, stačí znovu stisknout dané tlačítko a na obrazovce se znovu objeví IP Address. Pokračujeme-li v seznamu, nalezneme zde ethernetový port a přístup k provedení resetu zařízení, k čemuž je třeba uchopit pin a podržet jej po dobu 10 sekund, aby se resetovala všechna nastavení miniaturního Miner. Nakonec najdeme dvě kontrolky, jednu Green a jednu červenou, které nám ukazují stav zařízení Miner.



![image](assets/en/03.webp)



## Připojení zařízení Mini Miner



Zařízení je třeba připojit k internetu prostřednictvím ethernetu, ale v nové verzi (BMM 101) to již není nutné. Vraťme se k tomuto miniaturnímu zařízení Miner. Jakmile lokalizujeme jeho umístění, budeme jej muset nejprve připojit k internetové lince a poté k napájení: zařízení se automaticky zapne a na obrazovce se zobrazí jeho IP Address.



## Konfigurace



Musíme otevřít prohlížeč a do vyhledávacího řádku zadat adresu IP Address, která nám zobrazuje miniaturní Miner. Připomínám, že pro vyhledání zařízení v síti bude nutné být místní, takže počítač, který používáte, bude muset být připojen ke stejné síti jako mini Miner. Jakmile zadáme IP Address, stiskneme enter a na obrazovce se objeví přihlašovací stránka k operačnímu systému mini Miner, což je Braiins OS.



![image](assets/en/06.webp)



Pro přihlášení musíte jako uživatelské jméno zadat `root` a heslo můžete nechat prázdné. Klikněte na přihlášení a zobrazí se váš miniaturní ovládací panel Miner.



![image](assets/en/07.webp)



## Obecná nastavení



Přejděme na systém



![image](assets/en/24.webp)



v nastavení nalezneme některá obecná nastavení, jako je téma (světlé nebo tmavé), jazyk, časové pásmo a změna hesla.



![image](assets/en/25.webp)



Pokud místo toho přejdeme na "Mini Miner Screen", zobrazí se nastavení našeho mini Miner, například zobrazení obrazovky. Můžeme si vybrat, zda se má zobrazovat čas, nebo cena Bitcoin, nebo obrazovka s informacemi o stavu stroje, jako je výrobek Hash, teplota, spotřebované watty atd. Zde je na vás, abyste si vybrali, co chcete na obrazovce vidět; můžeme také změnit jas obrazovky, nastavit noční režim a zobrazit čas s 12hodinovým nebo 24hodinovým formátem.



![image](assets/en/26.webp)



Po provedení změn klikněte na `Uložit změny` a změny se zobrazí na obrazovce zařízení



![image](assets/en/27.webp)



## Připojení ke Mining pool



Nyní ještě nejsme v provozu, protože pro spuštění Mining se musíme připojit k poolu, takže musíme přejít do "Konfigurace"



![image](assets/en/08.webp)



a první položka je pouze `Pools`.



![image](assets/en/09.webp)



Zde se musíme rozhodnout, který bazén použijeme. V tomto návodu vám ukážu dvě možnosti. První z nich je připojení k Mining pool Braiins, který používají i profesionální těžaři, jak se můžete přesvědčit v tomto návodu:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Druhou možností je připojit nás k Mining pool, který mina v sólo, jako je Public Pool, postupujte podle tohoto návodu:



https://planb.network/it/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

### Bazén Braiins



Abychom se k tomuto fondu mohli připojit, musíme si vytvořit účet.Tento fond také provádí platby pomocí Lightning Network, takže budeme moci obdržet několik Sats denně. K tomu si musíme zřídit blesk Address, na který budeme odměny dostávat. Pokud nevíte, jak vytvořit účet na braiins poolu nebo jak nastavit blesk Address, můžete postupovat podle tohoto návodu:



https://planb.network/it/tutorials/mining/pool/braiins-pool-557be706-35a9-4375-a563-d55ab5c69f55

Jakmile je to hotovo, jsme v přístrojové desce bazénu Braiins. Musíme poolu sdělit, že se chceme připojit k jednomu z našich těžařů, takže na levé straně obrazovky najdete několik položek. Musíme přejít na položku "workers"



![image](assets/en/04.webp)



a musíme kliknout na fialové tlačítko vpravo s nápisem "Připojit pracovníky"



![image](assets/en/05.webp)



Zde se zobrazí okno s informacemi, které potřebujeme k připojení našeho mini Miner k bazénu. Zde můžeme provést jedinou změnu, a to zvolit Stratum V2. Co je to Stratum v2, se dozvíte z této položky ve [slovníku pojmů](https://planb.network/en/resources/glossary/stratum-v2).



![image](assets/en/10.webp)



Nyní musíme zkopírovat tento řetězec, který začíná stratumv2. Klikneme tedy na malý symbol "kopírovat" a přejdeme na ovládací panel našeho mini Miner, který jsme nechali v konfiguraci a bazénech. Klikneme na tlačítko přidat nový bazén



![image](assets/en/11.webp)



a zkopírovaný řetězec vložte do prostoru pod adresou URL bazénu.



![image](assets/en/12.webp)



Nyní je třeba přidat uživatelské jméno a heslo. Vraťme se zpět do dashboadu bazénu. Pod ním máme také uživatelské jméno a heslo. UserID a naše uživatelské jméno, to, které jsme zadali při vytváření účtu, plus název Miner, který chceme vložit. můžete se rozhodnout, zda chcete zařízení, které připojujete k poolu, dát jméno, je to nepovinné, ale je vhodné ho vložit, abyste je v případě připojení více zařízení mohli hned snáze identifikovat. Pokud místo něj nechcete nic uvádět, můžete ponechat `workerName`.



![image](assets/en/13.webp)



Poté přejdeme do našeho mini Miner a zadáme uživatelské jméno. Zde zadáme v mém případě "finalstepbitcoin", což je moje uživatelské ID, miniminer dot. To je název, který jsem se rozhodl zařízení dát. Pokud jej nechcete pojmenovat, stačí napsat userid tečka workername. V mém případě by to bylo finalstepbitcoin.workername. Po zadání uživatelského jména si můžete zvolit heslo a napsat ho do prázdného pole. Můžete také zadat anithing123, což je to, které se také zobrazuje na obrazovce poolu, ale chce to jen naznačit, že můžete zadat libovolné heslo.



Po zadání všech údajů je třeba stisknout tlačítko pro uložení vpravo (ve tvaru diskety), čímž jsou údaje o bazénu v mini Miner nakonfigurovány.



![image](assets/en/14.webp)



Nyní se musíte vrátit na ovládací panel bazénu a kliknout na "Připojeno! Vraťte se zpět."



![image](assets/en/15.webp)



Připojili jsme náš mini Miner k bazénu braiins! Nyní jej můžete vidět v seznamu pracovníků. Pokud se nezobrazuje, stačí provést obnovení a chvíli počkat. Jakmile se objeví, zkontrolujte, zda má stav "OK" s označením Green.



![image](assets/en/17.webp)



pokud se vrátíte na ovládací panel, měli byste na grafu vidět pohyb a vidět Hashrate našeho zařízení. To znamená, že bazén přijímá naši práci, a proto jsme pro všechny případy podminováni.



![image](assets/en/16.webp)



### Veřejný bazén



V tomto bazénu lze zkusit štěstí a těžit sólo, opírat se o bazén. V takovém případě sice nedostaneme odměnu, ale pokud se nám někdy podaří vytěžit blok, dostaneme odměnu v plné výši. Poté se napojíme na veřejný pool, pool určený pouze pro Mining, který je zcela otevřený. Otevřeme nové okno prohlížeče a přejdeme na adresu [web.public-pool.io](https://web.public-pool.io/#/).



![image](assets/en/18.webp)



je tu stránka se všemi potřebnými informacemi. Pak tam zkopírujeme vrstvu Address



![image](assets/en/19.webp)



pak se vrátíme na ovládací panel našeho mini Miner, přejdeme do konfigurace a do bazénů, klikneme na přidat nový bazén (stejný postup jako výše) a vložíme 'stratum Address pod url bazénu.



![image](assets/en/20.webp)



Nyní se vraťme na stránku bazénu a uvidíme, že jako uživatelské jméno musíme zadat Bitcoin Address, což bude ten, na kterém obdržíme odměnu v případě, že podkopeme blok, pak tečku a pak název našeho zařízení, stejně jako jsme to udělali dříve s Braiins Pool, zatímco heslo si můžeme zvolit sami.



![image](assets/en/21.webp)



Vrátíme se do mini Miner a pod uživatelské jméno vložíme Address Bitcoin, za kterým následuje tečka a jméno, já vložím `miniminer`. Do hesla místo něj vložím test, vy si zadejte, co chcete.



![image](assets/en/22.webp)



Nyní uložíme nastavení a zakážeme bazén Braiins.



![image](assets/en/23.webp)



Dobře! Nyní jsme Mining na veřejném bazénu!



![MINI MINER BRAIINS | un oggetto di design che mina BITCOIN.](https://www.youtube.com/watch?v=pzzWmM2tEAQ&t=284s)