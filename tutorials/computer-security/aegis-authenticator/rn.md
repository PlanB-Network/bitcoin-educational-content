---
name: Aegis Authenticator
description: Wokoresha gute Aegis Authenticator kugira ngo ukingire amakonti yawe ukoresheje uburyo bwo kwemeza ko ari bwo bubiri?
---

![cover](assets/cover.webp)



Muri iki gihe, uburyo bwo kwemeza ko umuntu ari uwundi (2FA) ni ngombwa kugira ngo umuntu ashobore gukingira amakonti yo kuri Internet. Uretse ijambo banga, ryongerako ikindi kintu ca kabiri (kenshi ni kode y’imirongo 6) kigahera inyuma y’amasegonda 30, ivyo bikaba bituma abasuma b’amakuru bagorwa cane. Gukoresha porogarama yihariye yitwa TOTP (*Ijambobanga ry’igihe kimwe*) biratekanye kuruta ubutumwa bwa SMS, bushobora gufatwa n’ibitero vyo guhindura SIM.



Ariko rero, si ibikorwa vyose vyo kwemeza ko umuntu ari uwundi vyaremwe bingana. Ivyiyumviro vyinshi vy’abanyagihugu (Google Authenticator, Authy, n’ibindi) biratera ingorane: ni ivy’abanyagihugu kandi bifise inkomoko yugaye (ntibishoboka gusuzuma umutekano wavyo), rimwe na rimwe bishiramwo abakurikirana amatangazo, ntibitanga ububiko bw’amakode yawe, kandi birashobora mbere kubuza gutuma konti zawe zigufunga.



Ku rundi ruhande, Aegis Authenticator yiyerekana nk’ubundi buryo bwo gukoresha ivyo bikoresho ku buntu kandi bushingiye ku nyifato runtu. Aegis ni porogaramu y’ubuntu, itekanye, yuguruye yo gucunga ibimenyetso vyawe vy’igenzura ry’intambwe zibiri kuri Android. Iterambere ryayo ryibanda ku bintu vy’ingenzi izindi porogarama zidatanga, harimwo no gukingira amakuru yo mu karere bikomeye be n’ubushobozi bwo gukingira amakuru ataco akora. Muri vyose, Aegis itanga umuti wo kwemeza ivy’ukuri bibiri, ushobora gusuzumwa, mwiza ku muntu wese yipfuza kuguma afise ububasha bwose ku makode yiwe ya 2FA.



## Gutangaza umugenzuzi wa Aegis



Aegis Authenticator ni porogaramu y’ubuhinga bwa 2FA ifunguye kuri Android, yasohotse hakurikijwe uruhusha rwa GPL v3. Iratandukanye n'ubuhinga bwayo bwo "ubuzima bwite kubera umugambi": porogaramu ikora yose ata n'umurongo kandi ntabwo isaba gufatanya n'igikorwa co kure. Ivyo bituma ibimenyetso vyawe biguma bibitswe aho hantu ku gikoresho cawe, mu kigega gitekanye aho ari wewe wenyene ufise urufunguzo.



### Ibirango nyamukuru



**Ikibanza c'ibanga:** amakode yawe yose ya OTP abikwa mu kibanza c'ibanga ca AES-256 (uburyo bwa GCM), kirindwa n'ijambobanga ry'ibanga ry'umukoresha. Ushobora gufungura iki kibanza ukoresheje ijambobanga canke amakuru y’ibinyabuzima (ikimenyetso c’urutoke, ukumenya mu maso) kugira ngo bibe vyiza cane. Iyo ata jambobanga rihari, amakuru yoba ataco akora - rero turagusavye cane ko ushiraho ijambobanga.



**Imitunganirize iteye imbere:** Aegis iguma itunganije neza amakonti yawe menshi ya 2FA. Ushobora gutoranya ivyanditswe vyawe hakurikijwe inyuguti canke mu buryo uhisemwo, ukabishira mu migwi hakurikijwe ivyiciro (nk'akarorero, Ivy'umuntu ku giti ciwe, Ivy'Akazi, Ivy'Imibano) kugira ngo ushobore kubironka bitagoranye, maze ugatanga ikintu cose winjije ikimenyetso c'umuntu ku giti ciwe. Umurongo w’ugushakisha urashizwemwo kugira ngo ubone ubwo nyene serivisi canke konti mw’izina.



**Ivyiyumviro vy'imbere mu gihugu:** Kugira ngo ntuzokwigere utakaza uburenganzira bwo gukoresha amakonti yawe, Aegis itanga ivy'inyuma vy'ibanga ryawe. Ivyo bifise amakuru (biciye mw’ijambobanga) kandi bishobora kubikwa aho uhisemwo (ububiko bwo mu mutima, dosiye y’igicu, n’ibindi). Porogaramu irashobora kandi kwohereza hanze urutonde rw’amakuru rwa konti yawe n’amaboko, mu buryo bushizwemwo canke butashizwemwo nk’uko bisabwa. Kwinjiza amakonti mu zindi porogaramu za 2FA ni nk’uko vyoroshe (Aegis ishigikira kwinjiza amakonti avuye muri Authy, Google Authenticator, FreeOTP, naOTP, n’ibindi).



**Umutekano n'ubuzima bwite:** porogaramu iri hanze y'umurongo ku buryo busanzwe. Nta ruhusha rw’urubuga rusaba - bisobanura ko ata makuru yohereza kw’isi yo hanze, kandi nta n’ivyo gukurikirana amatangazo canke ibice vyo gusesangura inyifato. Aegis ntiyerekana amatangazo, kandi ntisaba konti y’ukoresha: iyo imaze gushirwamwo, iratangura gukora ata kwiyandikisha. Kubera ko kode yayo y’inkomoko iri ku rubuga rwa GitHub, umuryango urashobora kuyigenzura mu mwidegemvyo, ugatanga icemeza ko ata bikorwa bibi canke vyihishijwe.



**Interface y'ubu:** Aegis ikoresha ubuhinga bw'ibikoresho, n'insanganyamatsiko y'umwiza (harimwo n'uburyo bwa AMOLED) mbere n'uburyo bwo kubona amabuye y'agaciro kugira ngo ugaragaze amakode yawe nk'ibipande. Interface nta n’ibintu biteye akaga, nta n’ibintu biteye igomwe, kandi irabuza gufata amakode ku rubuga nk’ingero y’umutekano.



## Gushiramwo



Kubera ko Aegis Authenticator ari inkomoko yuguruye, abayikora barakunda imihora yo gukwiragiza ibereye. Hari uburyo bubiri nyamukuru bwo kuyishiramwo:



### Biciye kuri F-Droid (ni vyiza)



Inzira itekanye kandi yoroshe ni F-Droid, iduka ry’ubuntu ry’ubundi buryo. Nimba F-Droid itarashirwa kuri telefone yawe, tangura kuyikura ku rubuga rwemewe [F-Droid.org](https://f-droid.org). None :





- Gufungura F-Droid maze urabe ko wahinduye ububiko bwawe kugira ngo ubone urutonde rwa nyuma rw'ibikorwa
- Rondera "Ivyemezo vya Aegis" muri F-Droid. Igikoresho cemewe gikwiye kuboneka (uwasohoye: Beem Development)
- Tangira gushiramwo ukanda Install. Nk’uko Aegis ari imwe mu porogarama zigenzuwe na F-Droid, uraronka inyungu mu gukuraho ibintu vyizewe kandi bitekanye .



Gushiramwo biciye kuri F-Droid bitanga akamaro ko kuronka amakuru mashasha y’iporogarama igihe nyene asohotse. Ikindi, F-Droid iratanga icemezo c’uko iyo porogarama idafise ibihimba vy’umunyagihugu bidakenewe.



### Biciye kuri GitHub (APK yashizweko umukono)



Niba ushaka gushiramwo porogaramu utaciye mu iduka, urashobora gukura APK yemewe kuri paji ya GitHub y’umugambi. Ku bubiko bwa Aegis ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)), genda ku gice c’Ivyasohotse aho amaverisiyo ahamye asohorwa.





- Kuvanaho verisiyo ya APK nshasha
- Imbere yo gushiramwo APK, nurabe neza ko wemereye gushiramwo porogarama zivuye mu bibanza bitazwi ku gikoresho cawe (mu Mitunganyirize ya Android) .
- APK itangwa kuri GitHub isinywe n'umuhinguzi n'urufunguzo rumwe n'urwo kuri F-Droid .



Inyuma yo gushiramwo n’amaboko, iyo porogarama izokora nk’uko nyene. Iyumvire ko ivyo guhindura bitazokwihuta: uzokenera gusuzuma GitHub buri gihe kugira ngo ubone verisiyo nshasha.



### Iduka rya google na F-Droid



Igikoresho co kwemeza Aegis kiraboneka kuri Google Play Store no kuri F-Droid, kiguha amahitamwo y’uburyo bwo kugishiramwo:



**Iduka rya Google:**




- ✅ Ivyagezwe vyihuta vyinjijwe muri sisitemu ya Android
- ✅ Gushiramwo vyoroshe, bimenyerewe
- ✅ APK yasinywe nk'iyo ku yindi mihora



**F-Droid (ni vyiza) :**




- ✅ Iduka ry'ubuntu kandi ry'inkomoko yuguruye
- ✅ Ubwubatsi bushobora gusubirwamwo kandi bugasuzumwa
- ✅ Nta serivisi ya Google isabwa
- ✅ Kwubaha filozofiya ya porogaramu y'ubuntu



Guhitamwo hagati y'izo nzira zibiri bivana n'ivyo ukunda ku bijanye n'ibidukikije vya Google. Niba ukunda ivyoroshe, Play Store ni nziza cane. Niba ushaka uburyo bwo gukoresha ubuzima bwite, butajanye n’ibikorwa vya Google, F-Droid ni yo nzira nziza.



## Itunganywa rya mbere



Igihe Aegis itanguzwa ku ncuro ya mbere, uburyo bwo gutunganya bwa mbere burashikirizwa kugira ngo kode yawe ya 2FA ibe nziza:



![Configuration initiale Aegis](assets/fr/01.webp)



*Igikorwa ca mbere co gutunganya Aegis: igicapo c'akabazo, amahitamwo y'umutekano, insobanuro y'ijambobanga n'ugusozera*



### Gushiraho ijambobanga ry'ingenzi



Aegis izobanza kukusaba guhitamwo ijambobanga ry’umukuru. Iri jambobanga rizokoreshwa mu gupfuka ibimenyetso vyawe vyose vy’ukwemeza bibitswe mu bubiko. Turagusavye cane gushinga ijambobanga rikomeye kandi ridasanzwe, wewe wenyene uzomenya.



**⚠️ Imburi:** ntimwibagire iri jambo banga - nimwaritakaza, ama code yanyu ya 2FA yashizwemwo amabanga azoba ataco ashobora gukora (nta backdoor). Aegis izogusaba kwinjiza ijambobanga incuro zibiri kugira ngo wemeze.



### Gushoboza gufungura biometric (ubusabe)



Nimba igikoresho cawe ca Android gifise igikoresho co gusoma urutoke canke ikindi gikoresho co gupima ubuzima, Aegis izogusaba gufungura ubuzima. Iryo hitamwo ni ryo guhitamwo ariko rirakora cane: rituma ushobora gufungura ningoga porogarama ukoresheje urutoke canke mu maso, aho kwandika ijambobanga igihe cose.



Zirikana ko biometrics ari ikintu congereweko: ijambobanga ryawe ry’ingenzi riracari ngombwa iyo biometrics ihinduwe canke igikoresho kigasubira gukora.



### Kubona amagenamiterere y'ikoreshwa



Uhejeje kwinjira muri porogarama (Interface nyamukuru mu ntango iri ubusa), menya neza uburyo bwo gutunganya buriho. Ushobora gushika ku mategeko biciye ku rutonde ruri hejuru iburyo bw'ibarabara (utudomo dutatu duhagaze), hanyuma uhitemwo "Imiterere".



![Interface principale et paramètres](assets/fr/02.webp)



*Interface main Aegis ubusa mu ntango, gushika ku rutonde rw'ibipimo n'insiguro y'amahitamwo ariho*



Ivyo bikoresho vya Aegis bikoranya ibice bihambaye:





- Uko usa**: Guhindura insanganyamatsiko (umuco, umwijima, AMOLED), ururimi n'ibindi bigaragara
- Inyifato**: Gutunganya inyifato y'ikoreshwa igihe ukorana n'urutonde rw'ibintu vyinjijwe
- Ivyuma vy'ibishushanyo**: gucunga no kwinjiza mu gihugu ibishushanyo vy'ibishushanyo kugira ngo uhindure uko konti yawe isa n'uko yumva
- Umutekano**: Amagenamiterere y'ugushiramwo amakuru, gufungura biometric, gufunga ubwavyo n'ibindi bipimo vy'umutekano
- Ivy'ububiko**: Gutunganya ivy'ububiko bwite ku kibanza uhisemwo
- Import & Export**: Injira mu bindi bikoresho vy'ukwemeza maze ushire hanze n'amaboko ububiko bwawe bwa Aegis
- Igitabo c'igenzura**: Igitabo c'ido n'ido c'ibintu vyose bihambaye vyabaye mu gikorwa



Iryo shirahamwe ritomoye rituma ushobora gutunganya Aegis bivanye n’ivyo ukunda be n’ivyo ukeneye mu bijanye n’umutekano.



## Kwongerako konti ya 2FA



Aegis imaze gutunganirizwa, reka tujane ku bintu vy’ingenzi: kwongerako amakonti yawe y’ibintu bibiri. Ivyo bikorwa ni vyoroshe, kandi Aegis itanga uburyo bwinshi bwo gushiramwo amakode yawe y’ukwemeza.



### Uburyo butatu bwo kwongerako buboneka



Kuva kuri Aegis Interface nyamukuru, kanda kuri buto ya **+** iri hasi iburyo kugira ngo ushikire amahitamwo yo kwongerako. Ufise uburyo butatu:





- Scan QR code**: Scan kode ya QR yerekanwa na serivisi y'urubuga
- Scan ishusho**: Scan kode ya QR ivuye ku ishusho yabitswe ku gikoresho cawe
- Injira n'amaboko**: Injira amakuru ya konti ya 2FA n'amaboko



### Akarorero ngirakamaro: gutunganya Bitwarden



Reka dufate akarorero nyako k’ugukora kwa 2FA kuri Bitwarden kugira ngo tugaragaze ingene bigenda:



![Exemple avec Bitwarden](assets/fr/04.webp)



*Akarorero k'ugukoresha 2FA kuri Bitwarden: Urubuga rwa Interface rufise uburyo bwo kwemeza n'impanuro za Aegis*





- Kwinjira no gushika ku mategeko**: Injira muri konti yawe ya Bitwarden maze ugere ku mategeko, "Umutekano" tab
- Igice c'abatanga**: Genda ku gice ca "Abatanga" hanyuma ukande kuri "Gucungera" mu gice ca "Iporogarama y'ukwemeza"



![Configuration 2FA avec QR code](assets/fr/05.webp)



*Igikorwa cose co kwongerako konti: QR code yerekanwa na service, urufunguzo rw'ibanga ruboneka na code yo kugenzura yinjijwe*





- Scan QR code**: Idirisha rifunguka rifise kode ya QR n'urufunguzo rw'ibanga
- Mu **Aegis**: Koresha "Scan QR code" kugira ngo ufate amakuru ubwawe
- Igenzura**: Injira kode y'imibare 6 yakozwe na Aegis mu kibanza ca "Kode y'igenzura"
- Gukoresha**: Fyonda kuri "Gufungura" kugira ngo uheze gukoresha



### Kwongerako ibisobanuro n'amaboko



Niba ushaka canke udashobora gucapura kode ya QR, koresha uburyo bwo "Injira n'amaboko". Urupapuro ruraguha uburenganzira bwo kwinjira :



![Ajout d'un compte 2FA](assets/fr/03.webp)



*Uburyo bwo kwongerako konti nshasha ya 2FA: Interface ubusa, wongereko amahitamwo, urupapuro rwo kwinjira n'amaboko na konti yongeweko neza*





- Izina**: Izina rya serivisi (nk'akarorero Bitwarden, GitHub...)
- Uwutanga**: Uwutanga (kenshi asa n’izina)
- Itsinda**: Ni ubusabe, gutunganya konti zawe hakurikijwe ivyiciro
- Iciyumviro**: Ivyiyumviro vy'umuntu ku giti ciwe kuri iyi konti
- Ibanga**: Urufunguzo rw'ibanga rutangwa na serivisi (rupfutse ku buryo busanzwe)
- Iterambere**: Iterambere ry'imirongo (algorithme, igihe, umubare w'imibare)



Iyo konti imaze kwongerwako, iraboneka kuri list yawe iriko kode yayo y’ubu be n’ikimenyetso c’igihe kigaragaza igihe gisigaye imbere y’uko ivugururwa.



### Uguhuza kw'isi yose



Aegis irahuye n’ibikorwa vyose bikoresha ingingo ngenderwako za TOTP na HOTP, harimwo n’imbuga hafi zose zitanga 2FA: imihora y’ubudandaji, amabanki, abacungera amajambo banga, imbuga z’ubuhinga bwa none, n’ibindi.



### Itunganywa ry'injira



Umaze kwongerako amakonti menshi, uzoshima ibikoresho vya Aegis vyo gutunganya:





- Gutoranya:** Ku mburabuzi, amakonti ari ku rutonde rw'inyuguti, ariko ushobora guhindura urutonde n'amaboko
- Amatsinda n’ivyiciro:** Rema amatsinda yo gutandukanya amakonti yawe bwite n’ay’ubucuruzi, canke uyashire mu matsinda hakurikijwe ubwoko bw’ibikorwa (banki, e-mail, imihora y’ubudandaji, n’ibindi)
- Ibishushanyo vy'abantu:** Aegis igerageza gutanga ikimenyetso kibereye iyo kiriho, ahandi ho ushobora guhitamwo mu bishushanyo vyinshi rusangi canke ukazana ishusho
- Gushakisha vyihuse:** Umurongo w'ishakisha uri hejuru uragufasha kwandika inyuguti nkeyi kugira ngo ucungurure ubwo nyene ivyinjijwe bihuye



Mu gukora ku kintu winjije, kode ya OTP iragaragara mu bunini bwose (niba yari yihishije) kandi ushobora kuyikopa ku rutonde rw’ibintu ukoresheje akamenyetso kare - ni ngirakamaro mu kuyishira muri porogarama ushaka gufatanya.



## Umutekano n'ububiko



Kubera umutekano uri mu mutima wa Aegis, birahambaye gutahura ingene amakode yawe ya 2FA akinzwe, n’ingene womenya ko agumaho iyo habaye ingorane.



### Ubwubatsi bw'umutekano



**Ugushiramwo amakuru akomeye**: Amakode yawe yose abikwa mu gitereko gifise amakuru akoresheje **ubuhinga bwa AES-256 mu buryo bwa GCM**, afatanijwe n’ijambobanga ryawe ry’ingenzi. Ivyiyumviro bishingiye kuri **scrypt**, bitanga uburinzi bwongerewe ku bitero vy’inguvu z’agahomerabunwa.



**Gufungura mu mutekano** : Ijambobanga ry'umukuru rirakenewe kugira ngo ushobore gufungura amakuru yawe. Biometrics (ntibikenewe) ikoresha **Ububiko bw’urufunguzo rwa Android** na TEE (Ibidukikije vy’Ibikorwa vyizigirwa) kugira ngo ikingire urufunguzo rwo gukingira.



**Uruhusha rutoyi**: Aegis ikora itari mu murongo ku buryo busanzwe, isaba gusa gushika ku kamera (QR scan), biometrics na vibrator. Nta makuru yegeranywa canke asangizwa.



### Amahitamwo yo gusubiza inyuma



Aegis itanga ingamba nyinshi zo gusubiza inyuma kugira ngo zijane n’umutekano utandukanye n’ivyo umuntu akeneye:



![Configuration des sauvegardes](assets/fr/06.webp)



*Interface yuzuye na konti yongeweko, imburi yo gusubiza inyuma, amasetingi yo gusubiza inyuma yikora n'ingene yosubiza inyuma*



**1. Ububiko bw'aho hantu bwikora**




- Kugena ububiko bw'aho uhisemwo
- Incuro zishobora guhindurwa (inyuma y'ihinduka ryose, ku musi, n'ibindi)
- Dosiye zikingiwe n'ijambobanga (.aesvault)
- Ihuye n'amadosiye ahujwe (Nextcloud, Dropbox, n'ibindi)



![Sélection du dossier de sauvegarde](assets/fr/07.webp)



*Uburyo bwo guhitamwo dosiye y'ububiko: umugenzuzi wa dosiye, dosiye y'aho ija n'uruhusha rwo kuyironka*



**2. Ububiko bw'igicu bwa Android**




- Ugushiramwo ubusabe na sisitemu y'ububiko bwa Android
- Iboneka gusa ku ma safe yashizwemwo amakuru (umutekano urazigamye)
- Ububiko buboneka n'ayandi makuru ya Android
- Gusubiza ubwavyo ku guhindura igikoresho



**3. Ivyoherezwa hanze mu maboko**




- Gusohora hanze ku bisabwa biciye ku **Imiterere > Gushiramwo no Gusohora**
- Guhitamwo uburyo bubitswe (bwiza) canke butomoye
- Ni ngirakamaro ku kwimuka canke gusubiza inyuma rimwe na rimwe



### Ivyiza vyo kwirinda





- Bika verisiyo nyinshi z'ububiko kugira ngo wirinde ibiturire
- Ubudasiba **gerageza** ama backups yawe mu kugerageza gusubizaho
- Bika amakode yawe yo gusubizaho **bitandukanye**
- **Ijambobanga ryawe ry'ingenzi** riracari ngombwa mbere n'aho woba ufise ububiko bwo mu gicu
- Gukingira ijambobanga ryawe ry'ingenzi**: koresha ijambobanga ry'umwihariko, rikomeye ribitswe mu mucungerezi w'ijambobanga
- Gumana ubusabe bwawe **bugezweho** n'ibice vy'umutekano bishasha
- Gukoresha **auto-lock** mu mitunganyirize kugira ngo ushobore gushika kuri porogaramu
- Guhagarika **amafoto** (uburyo mburabuzi) kugira ngo amakode yawe ntafatwe
- Koresha biometrics bike**: guhitamwo amajambo banga ku nzira zihambaye



## Kugereranya n'ibindi bikoresho



Ni gute Aegis irundanya n’izindi porogarama zizwi cane zo kwemeza ko umuntu ari uwundi?



### Aegis n'Ivyemezo vya Google



**Umukingira :**




- ✅ Inkomoko yuguruye kandi ishobora gusuzumwa
- ✅ Ububiko bw'aho hantu
- ✅ Itunganywa riteye imbere (amatsinda, ibishushanyo, ubushakashatsi)
- ✅ Nta gukusanya amakuru
- ❌ Android gusa



**Ivyemezo vya Google :**




- ✅ Iboneka kuri Android na iOS
- ✅ Guhuza ibicu (kuva muri 2023)
- ❌ Kode y'inkomoko yugaye
- ❌ Ibikorwa bifise aho bigarukira
- ❌ Ikusanya ry'amakuru ya Google



### Aegis na Authy



**Umukingira :**




- ✅ Inkomoko yuguruye
- ✅ Nta konti isabwa
- ✅ Gusohora kode hanze birashoboka
- ✅ Gucungera amakuru yose hamwe
- ❌ Nta guhuza ibikoresho vyinshi



**Uburenganzira :**




- ✅ Guhuza ibikoresho vyinshi
- ✅ Iboneka kuri Android na iOS
- ❌ Kode y'inkomoko yugaye
- ❌ Bisaba inomero ya telefone
- ❌ Ntibishobora kohereza hanze amakode
- ❌ Porogaramu zo kuri mudasobwa zakuweho muri Ntwarante 2024



Aegis iraruta ayandi ku bakoresha Android baha agaciro uguseruka, umutekano wo mu karere no kugenzura neza amakuru yabo. Ibindi bikoresho nka Authy birabereye cane nimba ukeneye cane gukorana n’ibikoresho vyinshi.




## Iciyumviro



Aegis Authenticator ni umuti mwiza ku barondera ubuhinga bwa 2FA bushobora gukingira ubuzima bwite, butekanye kandi buboneka. Uburyo bwayo bwo gufungura, bufatanijwe n’ugushiramwo amakuru akomeye be n’ubuhinga bwa Interface busukuye, bituma iba ihitamwo rya mbere ryo gukingira amakonti yawe yo kuri Internet.



Naho bigarukira kuri Android kandi bitagira ubuhinga bwo gukorana n’igicu, Aegis iraheza igasubiza ivyo bibazo n’ubuhinga bwayo bwo gukora ubuzima bwite n’ugucungera amakuru yose. Ku bakoresha bahagaritse umutima ku bijanye n’ubuzima bwite bwabo bwa digitale, Aegis itanga ubundi buryo bwizewe kandi bukomeye bwo gutorera umuti ibibazo vy’ubutunzi vy’isoko.



Umutekano w’amakonti yawe yo kuri internet ntubwirizwa kuva ku buntu bwiza bw’amashirahamwe y’ubudandaji. Ukoresheje Aegis, uraguma ugenzura amakode yawe y’ukwemeza, mu gitereko c’amahera c’ubuhinga bwa none wewe wenyene ufise urufunguzo.



## Ubutunzi



### Urubuga rwemewe




- Urubuga rwemewe**: [getaegis.app](https://getaegis.app/) - Gushikiriza ubusabe no gukuraho
- Kode y'inkomoko**: [github.com/iterambere ry'umuyaga/Aegis) - Ububiko buzwi bwa GitHub
- F-Droid**: Gushiramwo biciye ku bubiko bw'ubuntu



### Inyandiko z'ubuhinga




- Ivyandiko vy'ububiko**: [Igishushanyo c'ububiko](https://github.com/beemdevelopment/Aegis/blob/master/docs/ububiko.md) - Insobanuro y'ubuhinga y'ububiko n'ubwubatsi butekanye
- Ibibazo vyemewe**: Inyishu ku bibazo bikunda kubazwa
- Umugambi wiki**: [github.com/iterambere ry'ibikoko/Aegis/wiki) - Inyandiko z'abakoresha zose