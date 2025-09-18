---
name: Bitcoin Core (Linux)
description: Gukoresha node yawe bwite na Bitcoin core kuri Linux
---

![cover](assets/cover.webp)


## Gukoresha node yawe bwite na Bitcoin core.


Intangamarara ya Bitcoin n’iciyumviro c’uruzitiro, rwuzuzwa n’uburongozi bwo gushiramwo kuri Linux.


Kimwe mu bintu biteye umunezero cane muri Bitcoin ni ubushobozi bwo gutwara porogarama ubwiwe, gutyo akagira uruhara ku rugero rw'ubuhinga n'ugusuzuma ibikorwa vya Leta Ledger.


Bitcoin, nk’umugambi w’inkomoko yuguruye, warabonetse ku buntu kandi ugakwiragizwa ku mugaragaro kuva mu 2009. Haciye hafi imyaka 17 itanguye, Bitcoin ubu ni urubuga rw’amahera rw’ubuhinga bwa none rukomeye kandi rudashobora guhagarara, rwungukira ku ngaruka zikomeye z’urubuga rw’ibinyabuzima. Kubera utwigoro twabo n’iyerekwa ryabo, Satoshi Nakamoto barakwiriye gushimwa. N’ubundi, turakira igitabu cera ca Bitcoin hano kuri Agora 256 (iciyumviro: na co nyene kuri kaminuza).


### Kuba banki yawe bwite


Gukoresha node yawe bwite vyacitse ikintu gihambaye ku bakurikiza inyifato ya Bitcoin. Ata n’umwe asavye uruhusha, birashoboka ko umuntu ashobora gukuraho Blockchain kuva mu ntango, gutyo akagenzura amafaranga yose akora kuva kuri A gushika kuri Z hakurikijwe amategeko ya Bitcoin.


Iyo porogarama kandi irimwo Wallet yayo bwite. Gutyo, turafise ububasha ku bijanye n’amahera twohereza ku yindi nzira, ata n’umwe adufasha canke uwundi muntu agira gatatu. Uri banki yawe bwite.


Ibindi bice vy’iki kiganiro rero ni ubuyobozi bwo gushiramwo Bitcoin core — verisiyo ya porogarama ya Bitcoin ikoreshwa cane — cane cane ku bikoresho vya Linux bihuye na Debian nka Ubuntu na Pop!OS. Kurikiza iyi nzira kugira ngo utere intambwe imwe wegere ubusegaba bwawe bwite.


## Bitcoin core Inyigisho yo gushiramwo Debian/Ubuntu


**Ibisabwa**


- Nibura 6GB y'ububiko bw'amakuru (pruned node) — 1TB y'ububiko bw'amakuru (Full node)
- Nimwitege ko *Igikoresho ca mbere co gukuraho* (IBD) kizofata nibura amasaha 24. Ivyo bikorwa ni ngombwa mbere no ku nzira ya pruned.
- Kwemerera ~600GB y'uburebure bw'uruja n'uruza ku IBD, mbere no ku nzira ya pruned.


**Iciyumviro:💡** aya mategeko akurikira yarasobanuwe mbere kuri Bitcoin core verisiyo 24.1.


### Gukuraho no kugenzura amadosiye



- `Bitcoin-24.1-x86_64-linux-gnu.tar.gz`, hamwe n'amadosiye `SHA256SUMS` na `SHA256SUMS.asc` (biragaragara ko ukeneye gukuraho verisiyo ya nyuma ya porogarama).



- Gufungura terminal mu bubiko aho amadosiye yavanwe ari. Akarorero: `cd ~/Ivyo gukuraho/`.



- Genzura ko umubare w'isuzuma wa dosiye ya verisiyo uri ku rutonde muri dosiye y'umubare w'isuzuma ukoresheje itegeko `sha256sum --kwirengagiza-kubura --suzuma SHA256SUMS`.



- Igisohoka c'iri tegeko gikwiye kubamwo izina rya dosiye ya verisiyo yakuweho ikurikiwe na `OK`. Akarorero: `Bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: Ni vyiza`.



- Gushiramwo git ukoresheje itegeko `sudo apt gushiramwo git`. Hanyuma, ushireho ububiko burimwo imfunguruzo za PGP z’abasinye ba Bitcoin core ukoresheje itegeko `git clone https://github.com/Bitcoin-core/guix.sigs`.



- Injira imfunguruzo za PGP z'abasinye bose ukoresheje itegeko `gpg --injira guix.sigs/imfunguruzo z'ubwubatsi/*`



- Genzura ko dosiye y'umubare w'isuzuma yashizweko umukono n'imfunguruzo za PGP z'abashizeko umukono ukoresheje itegeko `gpg --genzura SHA256SUMS.asc`.



Buri sinyatire ibereye izokwerekana umurongo utangura na: `gpg: Sinyatire nziza` n'uwundi murongo uhera na: `Ikimenyetso c'urutoke rw'urufunguzo rwa mbere: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320` (akarorero k'urutoke rwa PGPy).


**Iciyumviro💡:** si ngombwa ko imfunguruzo zose z'abasinya zigarukana "OK". Nkako, kimwe gusa coshobora kuba gikenewe. Ni ku mukoresha guhitamwo urugero rwiwe rwo kwemeza kugira ngo asuzume PGP.


Ushobora kwirengagiza imburi:



- `Uru rufunguzo ntirwemejwe n'umukono wizewe!'



- `Nta kimenyetso kigaragaza ko umukono ari uwa nyen'uwo mukono.'


### Gushiramwo igishushanyo ca Bitcoin core Interface



- Mu nzira, ikiri mu bubiko aho dosiye ya verisiyo ya Bitcoin core iri, koresha itegeko `tar xzf Bitcoin-24.1-x86_64-linux-gnu.tar.gz` kugira ngo ukureho amadosiye ari mu bubiko.



- Shiraho amadosiye yasohowe mbere ukoresheje itegeko `sudo shiraho -m 0755 -o umuzi -g umuzi -t /usr/aho hantu/bin Bitcoin-24.1/bin/*`



- Gushiramwo ibikenewe ukoresheje itegeko `sudo apt-get gushiramwo libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-ibikoresho qtwayland5 libqrencode-dev`



- Tangira _bitcoin-qt_ (Bitcoin core igishushanyo Interface) ukoresheje itegeko `Bitcoin-qt`.



- Kugira uhitemwo urudodo rwa pruned, reba _Umupaka w'ububiko bwa Blockchain_ maze ushireho umupaka w'amakuru azobikwa:


![welcome](assets/fr/02.webp)


### Insozero y'Igice ca 1: Inyobora yo Gushiraho


Bitcoin core imaze gushirwaho, birakenewe ko iguma ikora uko bishoboka kwose kugira ngo itange umusanzu ku rubuga rwa Bitcoin mu kugenzura ibikorwa no gutanga amabuye mashasha ku bandi bagenzi.


Ariko rero, gukoresha no guhuza urudodo rwawe mu bihe bimwe bimwe, mbere no kwemeza gusa amafaranga yakiriwe n’ayoherejwe, biracari akamenyero keza.


![Creation wallet](assets/fr/03.webp)


## Gutunganya Tor ku nzira ya Bitcoin core


**Iciyumviro💡:** iyi nkuru yagenewe Bitcoin core 24.0.1 ku bikoresho vya Linux bihuye na Ubuntu/Debian.


### Gushiramwo no gutunganya Tor ya Bitcoin core


Ica mbere, turakeneye gushiramwo igikorwa ca Tor (The Onion Router), urubuga rukoreshwa mu guhanahana amakuru ata mazina, ivyo bizotuma tutamenyekana ivyo dukorana n’urubuga rwa Bitcoin. Kugira ngo umenye intangamarara y’ibikoresho vyo kurinda ubuzima bwite bwo kuri Internet, harimwo na Tor, raba ingingo yacu ivuga kuri iyo nkuru.


Kugira ngo ushiremwo Tor, fungura urubuga maze winjize `sudo apt -y ushiremwo tor`. Iyo iyo nzira imaze gushirwaho, mu bisanzwe iyo serivisi izoca itangura ubwayo mu nyuma. Suzuma ko iriko irakora neza n'itegeko `sudo systemctl ikibazo tor`. Inyishu ikwiye kwerekana `Ikora: ikora (yasohotse)`. Kanda `Ctrl+C` kugira ngo usohoke muri iyi nzira.


**Impanuro:** uko biri kwose, ushobora gukoresha aya mabwirizwa akurikira muri terminal kugira ngo utangure, uhagarike, canke wongere utangure Tor:


```shell
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```


Igikurikira, reka dutangure igishushanyo ca Bitcoin core Interface n'itegeko `Bitcoin-qt`. Hanyuma, ushoboze ubuhinga bwikora bwa porogarama kugira ngo burungike amahuzu yacu biciye ku nzira ya Tor: _Ivyagezwe > Urubuga_, hanyuma uhereye ng’aho usuzume _Huza biciye ku nzira ya SOCKS5 (inzira y’imbere)_ hamwe n’_Koresha nzira itandukanye ya SOCKS5 kugira ngo ushikire bagenzi bawe biciye ku bikorwa vya Tor onion_.


![option](assets/fr/04.webp)


Bitcoin core ihita imenya nimba Tor ishizweho kandi, nimba ari ukwo biri, izokora amahuzu asohoka n’izindi nzira na zo nyene zikoresha Tor, uretse n’amahuza n’izindi nzira zikoresha imihora ya IPv4/IPv6 (clearnet).


**Iciyumviro💡:** kugira ngo uhindure ururimi rwerekana ururimi rw'igifaransa, genda kuri Display tab mu Settings.


### Itunganywa rya Tor riteye imbere (ubusabe)


Birashoboka ko Bitcoin core ikoresha gusa urubuga rwa Tor kugira ngo ihuze n’urunganwe rwacu, gutyo bigatuma tutamenyekana biciye ku nzira yacu. Kubera ko ata mikorere yubatswe muri ivyo mu gishushanyo Interface, tuzokenera gukora dosiye y’imiterere n’amaboko. Genda kuri Settings, hanyuma Gende ku Mahitamwo.


![option 2](assets/fr/05.webp)


Aha, kanda kuri _Gufungura dosiye y'imiterere_. Igihe uri muri dosiye y'inyandiko `Bitcoin.conf`, wongereko umurongo `onlynet=onion` maze ubike dosiye. Ukeneye gusubira gutangura Bitcoin core kugira ngo iri tegeko rikore.


Tuzoheza dutunganye igikorwa ca Tor kugira ngo Bitcoin core ishobore kwakira amakuru yinjira biciye ku nzira y’ubuhinga, ivyo bikaba bizotuma izindi node ziri ku rubuga zikoresha node yacu kugira ngo zikure amakuru ya Blockchain ataco zihungabanya ku mutekano w’imashini yacu.


Mu nzira, shiramwo `sudo nano /n'ibindi/tor/torrc` kugira ngo ushikire dosiye y'imiterere ya serivisi ya Tor. Muri iyi dosiye, rondera umurongo `#ControlPort 9051` hanyuma ukureho `#` kugira ngo uyishoboze. Ubu wongereko imirongo ibiri mishasha kuri dosiye:


```
HiddenServiceDir /var/lib/tor/bitcoin-service/
HiddenServicePort 8333 127.0.0.1:8334
```


Kugira ngo usohoke muri dosiye mu gihe uriko urayibika, kanda `Ctrl+X > Y > Injira`. Gusubira mu nzira, subiramwo Tor winjiza itegeko `sudo systemctl subiramwo tor`.


Ivyo bizotuma Bitcoin core ishobora gushinga amasano yinjira n’asohoka n’izindi nzira ziri ku rubuga biciye ku rubuga rwa Tor (Onion) gusa. Kugira ngo wemeze ivyo, fyonda ku _Idirisha_, hanyuma _Abagenzi_.


![Nodes Window](assets/fr/06.webp)


### Ibindi bikoresho


Ubwanyuma, gukoresha urubuga rwa Tor gusa (`onlynet=onion`) bishobora gutuma ushobora gushikirwa na Sybil Attack. Ni co gituma bamwe basaba ko umuntu aguma afise ubuhinga bwo gukoresha amakuru menshi kugira ngo agabanye ubwo bwoko bw’ingorane. Ikindi, amahuzu yose ya IPv4/IPv6 azoca muri proxy ya Tor iyo imaze gutunganirizwa, nk’uko vyagaragajwe mbere.


Canke, kugira ngo ugume gusa ku rubuga rwa Tor no kugabanya ingorane za Sybil Attack, ushobora kwongerako Address y'iyindi nzira yizigirwa kuri dosiye yawe `Bitcoin.conf` wongeyeko umurongo `addnode=trusted_address.onion`. Ushobora kwongerako uyu murongo incuro nyinshi nimba ushaka kwifatanya n'ibihimba vyinshi vyizigiwe.


Kugira ngo ubone inyandiko z'urudodo rwawe rwa Bitcoin rwerekeye cane cane imigenderanire yarwo na Tor, wongereko `debug=tor` kuri dosiye yawe ya `Bitcoin.conf`. Ubu uzoba ufise amakuru y'ingenzi ya Tor mu gitabo cawe co gukosora, ushobora kuraba mw'idirisha rya _Amakuru_ ukoresheje buto _Dosiye yo gukosora_. Birashoboka kandi kubona izo nyandiko mu buryo butaziguye mu nzira n'itegeko `bitcoind -debug=tor`.


**Impanuro💡:** ng'aya ama links aryoshe cane:


- [Urupapuro rwa Wiki rusobanura Tor n'isano rifise na Bitcoin]
- [Igikoresho co guhingura dosiye ya Bitcoin core cakozwe na Jameson Lopp]
- [Igitabu c'imiterere ya Tor cakozwe na Jon Atack]


Nk'uko bisanzwe, nimba ufise ikibazo, ntutinye kugisangiza umuryango wa Agora256. Twigira hamwe kuba beza ejo kurusha uko turi uno musi!