---
term: MAELEZO YA MAANDIKO YA PATO
---

Vifafanuzi vya hati ya pato, au vifafanuzi tu, ni semi zilizoundwa ambazo zinafafanua kikamilifu hati ya pato (`scriptPubKey`) na kutoa taarifa zote zinazohitajika ili kufuatilia miamala kwenda au kutoka kwa hati mahususi. Vifafanuzi hivi hurahisisha usimamizi wa funguo katika pochi za HD kupitia maelezo ya kawaida ya muundo na aina za anwani zinazotumiwa.


Nia kuu ya vifafanuzi iko katika uwezo wao wa kujumuisha habari zote muhimu za kurejesha Wallet katika safu moja (pamoja na kifungu cha uokoaji). Kwa kuokoa maelezo na misemo inayofanana ya Mnemonic, inawezekana kurejesha funguo za kibinafsi tu bali pia muundo sahihi wa Wallet na vigezo vya script vinavyohusiana. Kwa hakika, kurejesha Wallet hakuhitaji ujuzi tu wa seed ya awali bali pia faharasa mahususi kwa ajili ya kupata jozi muhimu za watoto, pamoja na `xpub` ya kila kipengele katika kesi ya Multisig Wallet. Hapo awali, ilichukuliwa kuwa habari hii ilikuwa inajulikana kwa wote. Hata hivyo, kwa mseto wa hati na kuibuka kwa usanidi changamano zaidi, maelezo haya yanaweza kuwa magumu kueleza, hivyo basi kubadilisha data hizi kuwa taarifa za faragha na za Hard-to-bruteforce. Matumizi ya vifafanuzi hurahisisha sana mchakato: inatosha kujua maneno ya uokoaji na maelezo yanayolingana ili kurejesha kila kitu kwa uhakika na kwa usalama.


Kifafanuzi kina Elements kadhaa:


- Hati hufanya kazi kama `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-PubKey-Hash), `tr`, `tr`, (7), `tr`, (7), na `tr` tr. `sortedmulti` (Sahihi nyingi zilizo na vitufe vilivyopangwa);
- Njia za utokaji, kwa mfano, `[d34db33f/44h/0h/0h]` ikionyesha njia inayotolewa na alama ya vidole ya ufunguo mkuu mahususi;
- Vifunguo katika miundo mbalimbali kama vile vitufe vya umma vya heksadesimali au vitufe vilivyopanuliwa vya umma (`xpub`);
- Cheki, ikitanguliwa na Hash, ili kuthibitisha uadilifu wa kifafanuzi.


Kwa mfano, maelezo ya P2WPKH Wallet yanaweza kuonekana kama:


```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```

Katika kifafanuzi hiki, chaguo la kukokotoa `wpkh` linaonyesha aina ya hati ya Pay-to-Witness-Public-Key-Hash. Inafuatwa na njia ya derivation ambayo ina:


- `cdeab12f`: alama ya kidole ya ufunguo mkuu;
- `84h`: ambayo inaashiria matumizi ya madhumuni ya BIP84, yanayokusudiwa kwa anwani za SegWit v0;
- `0h`: ambayo inaonyesha kuwa ni sarafu ya BTC kwenye Mainnet;
- `0h`: ambayo inarejelea nambari mahususi ya akaunti iliyotumika katika Wallet.


Kifafanuzi pia kinajumuisha ufunguo uliopanuliwa wa umma unaotumika katika Wallet hii:


```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```


Kisha, nukuu `/<0;1>/*` inabainisha kuwa kifafanuzi kinaweza anwani za generate kutoka kwa mnyororo wa nje (`0`) na wa ndani (`1`), na kadi-mwitu (`*`) ikiruhusu utokezaji mfuatano wa anwani nyingi kwa njia inayoweza kusanidiwa, sawa na kudhibiti "kikomo cha pengo" kwenye programu ya jadi ya Wallet.


Hatimaye, `#jy0l7nr4` inawakilisha checksum ili kuthibitisha uadilifu wa kifafanuzi.