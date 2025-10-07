---
term: URUPFUZO RWA BOSE
---

Urufunguzo rwa bose rukoreshwa mu nyandiko (rwaba mu buryo butaziguye mu buryo bw’urufunguzo rwa bose canke nk’urufunguzo rwa Address) kugira ngo umuntu yakire kandi akingire ama bitcoins. Urufunguzo rwa bose rudasanzwe rugereranywa n'akarongo ku nzira y'uruzitiro, rugizwe n'ibiharuro bibiri (`x, y`) kimwe cose gifise ibice 256. Mu buryo butagiramwo ivyiza, urufunguzo rwa bose rero rupima ibice 512, rudaharura byte y’inyongera kugira ngo umenye uburyo. Urufunguzo rwa bose rwacitse, ku rundi ruhande, ni uburyo bukomeye bwo guserukira urufunguzo rwa bose. Ikoresha gusa `x` n'intango (`02` canke `03`) yerekana uburinganire bw'umurongo wa `y` (ungana canke udasanzwe).


Nitwavyorohereza ivyo ku bijanye n’imibare nyayo, kubera ko umurongo w’uruzitiro uringaniye n’umurongo wa x, ku ntumbero iyo ari yo yose $P$ (`x, y`) iri ku murongo, hariho uturongo $P'$ (`x, -y`) na two nyene tuzoba kuri uwo murongo nyene. Ivyo bisigura ko kuri `x` yose, hariho gusa agaciro kabiri gashoboka ka `y`, keza n'akabi. Nk’akarorero, ku nzira y’umurongo `x`, hoba hariho uturongo tubiri $P1$ na $P2$ ku nzira y’umurongo w’uruzitiro, dusangiye umurongo umwe ariko ufise amabara atandukanye:


![](../../dictionnaire/assets/29.webp)

Kugira ngo uhitemwo hagati y'ibiharuro bibiri bishobora kuba biri ku nzira, intango y'ijambo `y` yo guhitamwo yongerwa kuri `x`. Ubu buryo bushobora kugabanya ubunini bw'urufunguzo rwa bose kuva ku bice 520 gushika ku bice 264 gusa (ibice 8 vy'intango + ibice 256 ku `x`). Ivyo bimenyetso bizwi nk'uburyo bushizwemwo urufunguzo rwa bose.


Ariko rero, mu bijanye n’ubuhinga bwo gupfuka amakuru y’uruzitiro, ntidukoresha imibare nyayo, ahubwo dukoresha urutonde rufise impera `p` (umubare w’intango). Muri iki gihe, "ikimenyetso" ca `y` kigenwa n'uburinganire bwaco, ni ukuvuga ko `y` ari umubare canke umubare. Intangamarara `0x02` rero yerekana `y`, mu gihe `0x03` yerekana `y` idasanzwe.


Rimbura akarorero gakurikira k'urufunguzo rwa bose rudasanzwe (akarongo ku nzira y'uruzitiro) mu gice c'icumi na gatandatu:

```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```


Turashobora gutandukanya intango, `x`, na `y`:

```plaintext
Prefix = 04
To determine the parity of `y`, we examine the last hexadecimal character of `y`:
```

Ishingiro rya 16 (icumi na gatandatu): f

Ishingiro rya 10 (icumi): 15

y ni ikidasanzwe

```

The prefix for the compressed public key will be `03`. The compressed public key in hexadecimal becomes:
```

K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6.

```