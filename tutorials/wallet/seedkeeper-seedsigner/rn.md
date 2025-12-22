---
name: Seedkeeper x SeedSigner
description: Nokoresha gute Umucungezi w'Imbuto n'Umucungezi wanje w'Imbuto?
---

![cover](assets/cover.webp)



*Turashimira umugwi wa [Satochip](https://satochip.io/) wemeye gusubira gukoresha [amasanamu yabo] muri iyi nyigisho. Turashimira kandi [Igitabu c'Ivy'Ibanga](https://www.youtube.com/@Igitabu c'Ivy'Ibanga/) kubera fork yayo ya porogarama y'Imbuto, ishoboza gushigikira amakarata y'ubwenge



---

SeedSigner ni igikoresho ca wallet ukoranya wewe nyene ukoresheje ibikoresho bisanzwe, akenshi bikikuje Raspberry Pi Zero. Iyi wallet yitwa "*stateless*": itandukanye n'izindi modoka nyinshi ziri kw'isoko (Coldcard, Trezor, Ledger, n'izindi), nta makuru ibika mu bubiko buhoraho, kandi ikora gusa mu buryo buhoraho ivuye kuri RAM. Nk’inyishu, seed y’ibitabo vyawe ntiyigera ibikwa kuri SeedSigner. Igihe cose uzosubira gutangura, uzokenera kuvyuzuza kugira ngo ico gikoresho gishobore gusinya amafaranga yawe. Uburyo busanzwe ni ubwo kubika seed yawe nk’ibara rya QR, ugaca uyicapura igihe cose uyikoresheje (*SeedQR*).



Ariko rero, ubwo buryo burafise ingorane zikomeye: seed itegerezwa kuguma ishobora gushikira mu nyandiko zitomoye kugira ngo ishobore gucapurwa. Iyo umuntu yivye canke yinjiye, uwutera yoshobora kuyifata bitamugoye maze akayiba ama bitcoins yawe.



Kugira ngo umuntu ashobore gutsinda iyo ntege nke, SeedSigner irashobora gufatanywa na [**Umucungezi w’imbuto**](https://satochip.io/igicuruzwa/umucungezi w’imbuto/), ikarita y’ubwenge yakozwe na Satochip. Ivyo bituma amajambo y’ukwibuka (canke ayandi mabanga) abikwa muri secure element irindwa na kode ya PIN. Igikoresho ca Seedkeeper ni igikoresho gifunguye, kandi secure element yaco ifise icemezo ca EAL6+. Ikoreshwa hamwe na SeedSigner, itanga ikintu gishimishije cane co gucungera umutekano: imfunguruzo zawe ziguma zicungiwe zose zitari ku murongo, ushirako umukono ku bikorwa vyawe ku gicapo cizigirwa, kandi seed irindwa ku mubiri mu karata y’ubwenge idashobora guterwa n’abantu.



Ivyo ukeneye vyose kugira ngo urangize gushiramwo ni ibi bikurikira:




- Ibikoresho bisanzwe bikenewe ku gikoresho ca kera co gukoresha SeedSigner: Raspberry Pi Zero, igicapo ca Waveshare 1.3", kamera ihuye n'ikarita ya microSD (uzosanga ibindi mu nyigisho ya SeedSigner iri musi);
- Igikoresho co kwagura SeedSigner, kiboneka [ku iduka ryemewe rya Satochip](https://satochip.io/igicuruzwa/igikoresho co kwagura-seedsigner/), kigufasha gusoma no kwandika ku ikarita y’ubwenge ukoresheje SeedSigner yawe. Iyindi nzira ni ugukoresha igikoresho co gusoma amakarata y’ubuhinga bwo hanze, gishobora gufatanywa n’umugozi ku nzira ya Micro-USB iri kuri Raspberry Pi. Ariko rero, jewe ubwanje sinarigeze ngerageza uwo muti;
- Seedkeeper, canke ikarita y’ubwenge idafise ikintu umuntu yoshirako applet ya Seedkeeper (igikoresho co kwagura kigurishwa na Satochip kirasanzwe kirimwo ikarita y’ubwenge idafise ikintu).



![Image](assets/fr/01.webp)



Iyi nyigisho ivuga ku bintu bibiri:




- Niba usanzwe ufise igitabo ca Bitcoin gicungiwe biciye ku SeedSigner yawe, ushobora gushiramwo gusa iyo porogarama nshasha. Ushobora rero kubandanya ukoresha wallet yawe isanzweho, ubu rero ukoresheje Seedkeeper kugira ngo ubone umutekano wongereweko.
- Niba utaragira Bitcoin wallet ifatanye na SeedSigner yawe, uzokenera gukurikiza intambwe **5** na **6** z’inyigisho zivugwa aha hepfo. Ibi bice bisigura ingene wokora generate y'ijambo ry'ubwenge ukoresheje SeedSigner, ukarizigama biciye ku *SeedQR*, hanyuma ukahuza iyo wallet na Sparrow Wallet kugira ngo uyirongore. Sinzoja muri izo nzira hano kandi **Ndiko niyumvira ko usanzwe ufise Bitcoin wallet ikora, itunganijwe na Sparrow na SeedSigner yawe**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Shiraho porogaramu



Kugira ngo ukoreshe SeedSigner yawe n’Umucungezi w’Imbuto, ukeneye gushiramwo iyindi porogarama, itandukanye n’iya SeedSigner y’intango, kugira ngo ushobore gufasha gusoma ikarita y’ubwenge. Ku bw'ivyo, [ndabahimiriza gukoresha fork ivuye muri "*Isubiramwo rya 3*"](https://github.com/Isubiramwo rya 3/umusinyi w'imbuto). Gukuraho [verisiyo nshasha y'ishusho](`.zip`) ihuye n'akarorero ka Raspberry Pi uriko urakoresha.



![Image](assets/fr/02.webp)



Niba utayifise, fungura porogarama ya [Balena Etcher](https://etcher.balena.io/), hanyuma ugende gutya:




- Injira ikarita ya microSD muri mudasobwa yawe;
- Gutanguza Etcher ;
- Hitamwo dosiye `.zip` uherutse gukuraho;
- Hitamwo ikarita ya microSD nk’intumbero;
- Fyonda kuri `Umuco!`.



![Image](assets/fr/03.webp)



Rindira gushika iyo nzira irangiriye: microSD yawe ubu irateguwe gukoreshwa. Ubu urashobora gutera imbere mu gukoranya igikoresho cawe.



Ku bindi bisobanuro ku bijanye no gushiramwo porogarama n’ukugenzura porogarama (intambwe ndagusavye cane gutera), raba inyigisho ikurikira:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Gukoranya igikoresho co gusoma ikarata y'ubwenge



![video](https://youtu.be/jqE8HDMCImA)



Tangana n’ugushira kamera kuri Raspberry Pi Zero, uyishire neza mu gipimo ca kamera hanyuma uyifunge n’agace k’umwirabura. Hanyuma ushire Pi hasi mu gitereko, urabe neza ko ivyuho bihuye n’ibifunguruzo bihuye.



![Image](assets/fr/04.webp)



Hanyuma ushire igikoresho co gusoma ikarita y’ubwenge ku bipimo vya GPIO vya Raspberry Pi Zero.



![Image](assets/fr/05.webp)



Nimushire igipfukisho c’ipulasitike hejuru y’igikoresho co gusoma ikarata y’ubwenge gushika gishizwe neza.



![Image](assets/fr/06.webp)



Hanyuma wongereko igicapo ku bipimo vya GPIO vy’ivyo bikoresho.



![Image](assets/fr/07.webp)



Ubwa nyuma, shiramwo ikarata ya microSD irimwo porogarama y’ivyuma mu gicapo co ku ruhande kiri kuri Raspberry Pi Zero.



![Image](assets/fr/08.webp)



Ubu ushobora gufatanya SeedSigner yawe biciye ku nzira ya Micro-USB ya Raspberry Pi Zero, canke biciye ku nzira ya USB-C y'iyo nzira. Ivyo vyose birakora. Rindira amasegonda make kugira ngo utangure, hanyuma ubone igicapo c’akabazo kigaragara.



![Image](assets/fr/09.webp)



Ku bindi bisobanuro ku bijanye n'ugutegura kwa mbere kwa SeedSigner yawe, ndagusavye inyigisho ikurikira:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Gucapura ikarita y'ubwenge ifise porogaramu ya Seedkeeper (ntibikenewe)



![video](https://youtu.be/NF4HemyEcOY)



Niba usanzwe ufise Seedkeeper, urashobora gusimbuka iyi ntambwe maze ukaja ku ntambwe ya 4. Muri iki gice, turaza kuraba ingene woshira applet ya Seedkeeper ku smartcard y’ubusa (uburyo bwa DIY).



Kugira ngo utangure, fungura `Ibikoresho > Ibikoresho vy'ikarita y'ubwenge` kuri SeedSigner yawe.



![Image](assets/fr/10.webp)



Hanyuma uhitemwo `Ibikoresho vyo kwikorera > Shiraho Applet`.



![Image](assets/fr/11.webp)



Injira ikarata yawe y'ubwenge mu gisomyi ca SeedSigner, igice kiraba hasi, hanyuma uhitemwo `SeedKeeper`.



![Image](assets/fr/12.webp)



Turagusavye wihangane mu gihe co gushiramwo: iyo nzira ishobora gutwara amasegonda mirongo.



![Image](assets/fr/13.webp)



Iyo applet imaze gushirwamwo neza, ushobora gukomeza ku ntambwe ya 4.



![Image](assets/fr/14.webp)



## 4. Bika SeedQR iriho kuri Seedkeeper



![video](https://youtu.be/X-vmFHU9Ec8)



Ubu ko Seedkeeper yawe iriko irakora, urashobora kubika igiharuro cawe ca Bitcoin wallet ku ikarita y’ubwenge. Kugira utangure, fungura SeedSigner yawe nk’uko bisanzwe, hanyuma ushireko *SeedQR* ya wallet yawe kugira ngo uyishire mu gikoresho. Igihe seed imaze kwinjizwa, uhitemwo gusa `Vyarangiye`.



![Image](assets/fr/15.webp)



Igihe seed ishizwemwo, genda kuri `Imbuto yo Gusubizaho`.



![Image](assets/fr/16.webp)



Hanyuma winjize Umucungezi w'Imbuto yawe mu muduga wa SeedSigner, hanyuma uhitemwo `Ku Mucungezi w'Imbuto`.



![Image](assets/fr/17.webp)



Uwo SeedSigner azoca agusaba kwinjiza kode ya PIN y’Umucungezi wawe w’Imbuto. Kubera ko iyi ari ikarita y’ubusa, nta kode irasobanurwa. Injira kode iyo ari yo yose kugira ngo usimbuke iyi ntambwe, hanyuma wemeze.



![Image](assets/fr/18.webp)



SeedSigner ibona ko Seedkeeper itaratangura (ni ukuvuga ko ata jambobanga ryashizweho). Fyonda `Ndatahura` kugira ngo ukomeze.



![Image](assets/fr/19.webp)



Ubu rero uhitemwo kode nshasha ya PIN y’Umucungezi w’Imbuto yawe, iri hagati y’inyuguti 4 na 16. Kugira ngo ubone umutekano wongereweko, hitamwo kode ndende, idasanzwe: ni yo nzitizi yonyene irinda ukuntu umuntu ashobora gushika ku majambo yawe y’ukwibuka.



Ibuka kubika iyi PIN igihe nyene iremwe, haba mu gikoresho co gucungera ijambobanga ryizigirwa, canke ku kindi gikoresho gitandukanye bivanye n’ingene ukoresha ingamba zawe. Mu gihe ca nyuma, urabe neza ko utazokwigera ugumya umurongo urimwo PIN ahantu hamwe n’Umucungezi wawe w’Imbuto, ahandi ho uburinzi buzoba butagira akamaro. Ni vyiza kugira kopi y'inyuma: **Udafise iyi PIN, ntuzoshobora gushika ku seed yawe, kandi ama bitcoins yawe azobura**.



![Image](assets/fr/20.webp)



Ushobora rero gusobanura `Ikimenyetso` gifitaniye isano n'ijambo ryawe ry'ukwibuka. Iryo kete ni ngirakamaro iyo ubitse amabanga menshi kuri Seedkeeper, kugira ngo ushobore kuyamenya bitagoranye.



![Image](assets/fr/21.webp)



Ijambo ryawe ry’ukwibuka ubu ryabitswe ku ikarita y’ubwenge.



![Image](assets/fr/22.webp)



Ku bijanye n’ingene wocungera umutekano, uburyo bwinshi burashoboka, bivanye n’ivyo ukeneye be n’urugero rwo gushikirwa n’ingorane. Ku bwanje, ndagusavye ko wobika n’imiburiburi kopi 2 z’igitabu cawe ca seed:




- Iyi ni iya mbere ku makarita y’ubwenge, ushobora kuguma uyironka bitagoranye mu bikorwa vya misi yose, nko kugenzura amaderesi canke gusinya amafaranga. Ubwo buryo burakora (nk’uko tuzobibona mu gice ca 5) kandi buraguma butekanye kubera uburinzi butangwa na kode ya PIN, ku buryo ushobora kuguma uyironka ata ngorane nini;
- Kopi ya kabiri y’ijambo ryawe ry’ukwibuka ritagiramwo amajambo, rikora nk’inyuma y’iherezo ry’ibitabu vyawe, rizokoreshwa gusa mu gihe Umucungezi w’Imbuto yoba atakaje canke yibwe. Kubera ko iyi verisiyo idashizwemwo amakuru, itegerezwa kubikwa mu kibanza gitandukanye, gifise umutekano mwinshi, kugira ngo ntihagire uwushobora gusenyura icarimwe ivyo bimenyetso 2 vy’ububiko.



Bivanye n’ingene wikingira n’ingene woba ufise ingorane, urashobora kandi gusubiramwo seed ku bikoresho bitandukanye vy’Imbuto, canke ugakora kopi nyinshi z’ivyo bimenyetso. Kugira ngo umenye vyinshi ku bijanye n’ivyo bikorwa, raba inyigisho ikurikira:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. Gushiramwo seed ivuye ku Mucungezi w'Imbuto



![video](https://youtu.be/ms0Iq_IyaoE)



Ubu ushobora gukoresha Seedkeeper yawe kugira ngo ushire ijambo ryawe ry'ukwibuka muri SeedSigner igihe utanguye, maze gutyo ushire umukono ku bikorwa vyawe vya Bitcoin. Kugira ngo utangure, fungura SeedSigner yawe mu kuyishiramwo, hanyuma ufungure `Imbuto`.



![Image](assets/fr/23.webp)



Hanyuma uhitemwo `Kuva ku Mucungezi w'Imbuto`.



![Image](assets/fr/24.webp)



Injira Seedkeeper yawe mu gikoresho co gusoma ikarita y’ubwenge, hanyuma winjize kode yawe ya PIN kugira ngo uyifungure. Wemeze ivyo winjije ukanda buto yo kwemeza iri hasi iburyo, `KEY3`.



![Image](assets/fr/25.webp)



Seedkeeper ishobora kubamwo amabanga menshi, rero SeedSigner iragusaba guhitamwo iyo wipfuza gushiramwo. Iryo kete ryerekanywe rihuye n’izina wasobanuye mu ntambwe ya 4. Nimba, nk’uko vyagenze kuri jewe, wanditse seed imwe gusa, uburyo bumwe gusa buzoboneka.



![Image](assets/fr/26.webp)



seed yawe ubu irashizwemwo. Suzuma ko ari wallet ibereye mu kugereranya ikimenyetso c’urutoke kigaragara ku rubuga n’ico kigaragara mu mitunganyirize ya Sparrow Wallet yawe. Ico kimenyetso c’urutoke na co nyene caratanzwe igihe wallet yaremwa ubwa mbere.



Niba uriko urakoresha passphrase, urashobora kuyishira mu ngiro muri iyi ntambwe (raba igice ca 6 c’iyi nyigisho). Ahandiho, gusa ukande kuri `Vyarangiye`.



![Image](assets/fr/27.webp)



Ushobora rero gukoresha wallet yawe nk’uko bisanzwe: usuzume amaderesi yawe yo gushikanako no gusinya amafaranga, nk’uko bigenda ku SeedSigner ya kera. Kugira ngo umenye vyinshi ku buryo bwo kuyikoresha, raba inyigisho yihariye :



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Gukoresha Umucungezi w’Imbuto afise passphrase BIP39



Woba ukoresha passphrase kugira ngo ukinge igitabu cawe ca Bitcoin? Ushobora kandi kuyiyandikisha mu gitabu cawe c’imbuto, iruhande y’igitabu cawe ca seed. Uwo muti uzotuma ushobora gushiramwo ningoga wallet yawe kuri SeedSigner, utabwirizwa kwinjiza passphrase n’amaboko ku rupapuro rutoyi igihe cose uyikoresheje.



Nsanga ubwo buryo bushimishije cane, kuko butuma wungukira ku vyiza vy’umutekano vya passphrase, mu gihe ukuraho ingorane zijanye n’ugukoresha kwayo ku musi ku musi. Aha niho akarorero k'imiterere nobabwira:




- Bika seed na passphrase yawe mu Kigo c’Imbuto, ukingiwe na kode ikomeye ya PIN (ivyo birahambaye). Ivyo bizotuma ushobora gukoresha neza wallet yawe ku musi ku musi. Niba ubishaka, urashobora gusubiramwo aya makuru ku Mucungezi w’Imbuto wa kabiri;
- Kandi uzigame kopi itomoye y’igitabu cawe co kwibuka be n’ica passphrase, ku mpapuro canke ku cuma. Iyi ni backup yawe ya nyuma iyo utakaje Seedkeeper yawe canke PIN yayo. Raba neza ko izo kopi uzibika ahantu hatandukanye, kugira ngo ntizishobora guhungabanywa icarimwe.



Muri iyi ntunganyo, iyo umuntu ashize ibiganza vyiwe ku mnemonic yawe y’inyandiko rusangi gusa, ntaco azoshobora kwiba atazi passphrase (igihe cose, birashoboka, ko ikomeye bihagije kugira ngo ishobore guhangana n’igitero c’inkomezi z’ibikoko). Ku rundi ruhande, iyo umuntu abonye passphrase yawe mu nyandiko rusangi, izoguma idashobora gukoreshwa ata n’ijambo ry’ukwibuka rihuye n’iryo jambo.



Ubwa nyuma, iyo umuntu ashoboye kuronka uburenganzira bwo gushika ku Seedkeeper yawe irimwo seed na passphrase, ntaco azoshobora gukuramwo atazi kode ya PIN. Udakunze passphrase, iyo kode ntishobora gukoreshwa ku nguvu, kuko smartcard yifunga ubwayo inyuma y’ukugerageza 5 kutagira akamaro.



Umutekano w’iyi ntunganyo rero ushingiye ku ngingo 2 z’ingenzi:




- A **passphrase strong**: itegerezwa kuba ndende, igira ivyiyumviro kandi irimwo inyuguti zitandukanye cane. Ugusobanuka kwayo si ingorane kuri wewe, kuko uzobwirizwa kuyishiramwo rimwe gusa kuri klavye mu gihe co gutangura; hanyuma, izorungikwa n’Umucungezi w’Imbuto ;
- **Kode ya PIN ikomeye** ya Seedkeeper: na yo nyene iratandukanye kandi igizwe n’inyuguti 16.



Kugira ngo ushireho iyo nzira, tangura ushire passphrase yawe muri SeedSigner mu buryo busanzwe. Ushobora gukurikira uburyo buvugwa muri iyi nyigisho:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Igihe igitabu cawe gifise passphrase kimaze gushirwa neza kuri SeedSigner, fungura `Seeds` maze uhitemwo ikirenge gihuye n'ico gitabu. Zirikana ko iki gice c'ibirenge gitandukanye n'ico mu bitabo bitagira passphrase.



![Image](assets/fr/28.webp)



Hanyuma ukande kuri `Backup Seed`, winjize Umucungezi w'Imbuto mu muduga, hanyuma uhitemwo `Ku Mucungezi w'Imbuto`.



![Image](assets/fr/29.webp)



Injira PIN yawe kugira ngo ufungure Seedkeeper, hanyuma ushire ikimenyetso kuri iri banga. Ushobora gusiga urutoke nk'ikimenyetso kugira ngo ugume ufise uburyo bumwe bwo guhakana, canke ukavuga neza `Ijambo ry'ibanga Wallet`, nk'akarorero.



![Image](assets/fr/30.webp)



Igitabo cawe ca passphrase ubu caranditswe kuri Seedkeeper.



![Image](assets/fr/31.webp)



Igihe kizoza utanguye, ushiremwo Seedkeeper yawe muri drive, hanyuma ugende kuri `Imbuto > Kuva kuri SeedKeeper`.



![Image](assets/fr/32.webp)



Injira PIN yawe kugira ngo ufungure ikarata y’ubwenge, hanyuma uhitemwo wallet ihuye na passphrase yawe.



![Image](assets/fr/33.webp)



Suzuma passphrase n’icapa cawe ca wallet, hanyuma wemeze.



![Image](assets/fr/34.webp)



Ubu ushobora gushika ku rutonde rwawe ukoresheje passphrase maze ugashira umukono ku bikorwa vyawe nk’uko usanzwe ubigira kuri SeedSigner.



## 7. Ibindi vyo guhitamwo



Mu `Ibikoresho > Ibikoresho vya Smartcard`, uzosanga uburyo bwinshi bwo gucunga Umucungezi w'Imbuto yawe:





- Mu `Ibikoresho rusangi`, ushobora :
 - Suzuma ko ikarita ari iyo ukuri;
 - Guhindura kode ya PIN ;
 - Guhindura ibimenyetso bifitaniye isano n'amabanga yawe ;
 - Guhagarika igikorwa ca NFC (ni vyiza iyo ukoresheje umusomyi w'ibice gusa) ;
 - Gukora ivy’uruganda.





- Mu `Ibikorwa vy'Umucungezi w'Imbuto`, ushobora :
 - Raba urutonde rw'amabanga yanditswe ;
 - Zigama ibanga rishasha ;
 - Gukuraho ibanga ririho ;
 - Bika canke ushiremwo ibisobanuro vyawe (igikorwa c'ingirakamaro ku bipimo vya multi-sig).





- Mu `Ibikoresho vya DIY`, ushobora :
 - Gukoranya applet y'Umucungezi w'Imbuto ;
 - Gushiramwo applet ku ikarita y'ubusa ;
 - Gukuraho porogaramu ya Seedkeeper kugira ngo uyisubiremwo maze wongere uyihindure ubusa.



Ubu urazi gukoresha Seedkeeper kugira ngo ukoreshe ububiko bwawe mu buryo butekanye ufatanije na SeedSigner.



Niba iyi setup yakwemeje, ntukekeranye gushigikira imigambi ituma bishoboka:




- Mu kugura ibikoresho vyawe ataco ukoresheje [ku rubuga rwa Satochip](https://satochip.io/shop/);
- Mu gutanga [intererano ku mugambi w’Umushingantahe w’Imbuto](https://umushingantahe w’imbuto.com/intererano/);
- Mu kwiyandikisha kuri [umurongo wa YouTube wa Crypto Guide](https://www.youtube.com/@CryptoGuide/), urongowe n’umuntu abungabunga ububiko bwa GitHub bufise porogarama yahinduwe.