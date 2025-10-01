---
term: IKIMENYETSO (UKWISHURA MU CECERE)
---

Mu nzira y'ukwishyura mu gacerere, ibimenyetso ni imibare yose ikoreshwa mu guhindura Address y'intango kugira ngo haboneke izindi aderesi nyinshi zidahinduka. Ikoreshwa ry’izo nkuru rituma habaho ugutandukanya amafaranga yoherezwa biciye ku Mafaranga y’Iceceko, hakoreshejwe amaderesi atandukanye y’ikoreshwa ryose, ata kwongerera cane umuzigo w’ibikorwa wo kumenya ayo mafaranga (gupima). Bob ikoresha Address $B$ idahinduka, igizwe n'imfunguruzo zibiri za bose: $B_{\umwandiko{scan}}$ wo gupima na $B_{\umwandiko{gukoresha}}$ wo gukoresha. Hash ya $b_{\text{scan}}$ n'umubare wose $m$, scalar-igwijwe n'inzira y'umuyagankuba $G$, yongerwa ku rufunguzo rwa bose rukoresha $B_{\text{spend}}$ kugira ngo ureme ubwoko bushasha bw'urufunguzo rwa bose rukoresha $B_m$:


$$ B_m = B_{\umwandiko{gukoresha}} + \umwandiko{Hash}(b_{\umwandiko{gupima}} \umwandiko{‖ } m) \cdot G $$


Nk'akarorero, urufunguzo rwa mbere $B_1$ ruronka muri ubu buryo:


$$ B_1 = B_{\umwandiko{gukoresha}} + \umwandiko{Hash}(b_{\umwandiko{gupima}} \umwandiko{‖ } 1) \cdot G $$


Address idahinduka yasohowe na Bob ubu izoba igizwe na $B_{\text{scan}}$ na $B_m$. Nk'akarorero, Address ya mbere idahinduka ifise ikimenyetso $1$ izoba:


$$ B = B_{\umwandiko{gupima}} \umwandiko{‖ } B_1 $$


Dutangura gusa n'ikimenyetso $1$, kuko ikimenyetso $0$ kigenewe guhinduka. Alice, yipfuza kohereza amafaranga y’ibiceri ku Address idahinduka yatanzwe na Bob, azoronka amahera yihariye Address $P_0$ akoresheje $B_1$ nshasha aho gukoresha $B_{\text{spend}}$:


$$ P_0 = B_1 + \umwandiko{Hash}(\umwandiko{injizaHash} \cdot a \cdot B_{\umwandiko{gupima}} \cdot{ ‖ } 0) \cdot G $$


Mu vy’ukuri, Alice yoshobora mbere kutamenya ko Bob afise Address yanditsweko, kuko akoresha gusa igice ca kabiri ca Address idahinduka yatanze, muri iki gihe kikaba ari agaciro $B_1$ aho gukoresha $B_{\text{spend}}$. Kugira ngo ukoreshe amahera, Bob azokwama akoresha agaciro ka Address yiwe y'intango n' $B_{\text{spend}}$ muri ubu buryo:


$$ P_0 = B_{\umwandiko{gukoresha}} + \umwandiko{Hash}(\umwandiko{injizaHash} \cdot b_{\umwandiko{gupima}} \cdot A \umwandiko{ ‖ } 0) \cdot G $$

Hanyuma, azokura gusa agaciro abona ku $P_0$ ku gisohoka cose kimwe kimwe. Araheza asuzuma nimba kimwe muri ivyo bimenyetso biva muri ivyo bihembo bihuye n’agaciro k’imwe mu nkuru akoresha ku mpapuro ziwe zo mu bwoko bwa Wallet. Niba bihuye, nk'akarorero, ku gisohoka #4 gifise ikimenyetso $1$, ivyo bisigura ko ico gisohoka ari Ukwishura kw'Iceceka gifitaniye isano n'Ikigobe ciwe gihoraho Address gifise ikimenyetso $B_1$:

$$ Isohoka_4 - P_0 = \umwandiko {Hash}(b_{\umwandiko{gupima}} \umwandiko{‖ } 1) \cdot G $$


Ibi birakora kuko:


$$ B_1 = B_{\umwandiko{gukoresha}} + \umwandiko{Hash}(b_{\umwandiko{gupima}} \umwandiko{‖ } 1) \cdot G $$


Ukoresheje ubu buryo, Bob ashobora gukoresha amaderesi menshi cane (afise $B_1$, $B_2$, $B_3$...), yose akomoka ku nzira yiwe y’ishimikiro Address ($B = B_{\umwandiko{scan}} \umwandiko{‖s } B_{\umwandiko{gukoresha pro.$ ku rutonde}$ly),


Ariko rero, ukwo gutandukanya amaderesi adahinduka ni ngirakamaro gusa bivanye n’uburongozi bw’umuntu ku giti ciwe bwa Wallet, ariko ntivyemera gutandukanya akaranga. Kubera ko zose zifise $B_{\text{scan}}$ imwe, biroroshe cane gufatanya amaderesi yose adahinduka hamwe maze ugaca ufata ingingo y'uko ari ay'ikintu kimwe.