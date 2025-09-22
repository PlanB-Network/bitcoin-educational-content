---
name: Electrum OP_RETURN
description: Sajili ujumbe kwenye Blockchain Bitcoin ukitumia Electrum
---

![cover](assets/cover.webp)




Mafunzo haya ya hatua kwa hatua yanakuonyesha jinsi ya kuandika ujumbe kwenye Blockchain Bitcoin kwa kutumia Wallet Electrum. Operesheni hii hutumia maagizo ya OP_RETURN ili kuingiza maandishi kwenye shughuli, inayoonekana hadharani kwenye Blockchain. Fuata hatua hizi rahisi kwa usajili uliofanikiwa.



---
## Masharti





- Kompyuta (Windows, macOS au Linux).
- Muunganisho wa mtandao.
- Satoshi chache (Sats) au bitcoins (BTC) katika Wallet yako ili kufidia kiasi na ada za muamala.
- Kigeuzi cha maandishi-hadi-heksi (k.m. tovuti ya mtandaoni) au zana maalum kama vile [jenereta hii ya hati ya OP_RETURN](https://resources.davidcoen.it/opreturnelectrum/).



---

## Hatua ya 1: Pakua na usakinishe Electrum



![image](assets/fr/01.webp)



1. Tembelea tovuti rasmi ya Electrum: [electrum.org](https://electrum.org/).


2. Pakua toleo linalolingana na mfumo wako wa uendeshaji (Windows, macOS, Linux).


3. Weka Electrum kulingana na maagizo ya kisakinishi.


4. Angalia uadilifu wa faili iliyopakuliwa (si lazima, lakini inapendekezwa kwa sababu za usalama) kwa kulinganisha sahihi ya faili au Hash.



→ Maelezo zaidi juu ya mafunzo ya Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Hatua ya 2: Unda au uingize Wallet



1. Kuzindua Electrum.


2. Chagua Unda Wallet mpya au Rejesha iliyopo Wallet ikiwa tayari una maneno ya seed (maneno ya kurejesha).


3. Fuata maagizo ili kusanidi Wallet yako:




 - Kwa Wallet mpya, andika sentensi yako ya seed na uiweke mahali salama (karatasi, salama, n.k.).
 - Kwa Wallet iliyopo, weka maneno yako ya seed ili kuirejesha.


4. Weka nenosiri ili kulinda Wallet yako.



→ Maelezo zaidi juu ya mafunzo ya Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Hatua ya 3: Angalia fedha zilizopo



Hakikisha Wallet yako ina bitcoins za kutosha (BTC) au satoshis (Sats) hadi:




- Kiasi cha shughuli (kwa mfano, 0.00001 BTC au 1000 Sats).
- Ada za muamala, ambazo hutofautiana kulingana na saizi ya mtandao (kwa ujumla elfu chache za Sats).



Wasiliana na Salio katika Electrum ili kuangalia pesa zako.



![image](assets/fr/02.webp)



Ikihitajika, hamisha BTC au Sats ili kulisha Wallet yako. Ili kufanya hivyo, nenda kwenye kichupo cha 'Pokea' na ubofye 'Unda Ombi':



![image](assets/fr/03.webp)



Hii itaonyesha mapokezi ya Address:



![image](assets/fr/04.webp)



→ Maelezo zaidi juu ya mafunzo ya Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Hatua ya 4: Tayarisha ujumbe ili uandikwe



Chagua ujumbe unaotaka kuingiza (k.m. `Asante Satoshi`). Kumbuka: Ujumbe wa OP_RETURN una mipaka ya baiti 80, yaani takriban herufi 80 za ASCII.



*Chukua muda kidogo kufikiria: unachoandika kwenye Blockchain Bitcoin ni cha milele na kinapatikana kwa wote, kwa hivyo :*




- acha mwonekano mzuri wa ubinadamu wetu,
- epuka kuingiza maudhui ambayo unaweza kujutia



*Nafasi ya Blockchain na bitcoins zako ni za thamani, zitumie kwa busara na kwa nia*



Badilisha ujumbe wako kuwa hexadecimal :




- Unaweza kutumia [zana ya mtandaoni](https://www.rapidtables.com/convert/number/ascii-to-hex.html), lakini kuwa mwangalifu usichakate data nyeti hapo (ingawa, kimsingi, maelezo yanayokusudiwa kuchapishwa kwenye Blockchain Bitcoin kupitia OP_RETURN haitoi masuala yoyote ya usiri);
- Kwa usiri mkubwa, fanya ubadilishaji wa ndani kwa kutumia Python ndogo :



```py
#!/usr/bin/env python3

def main():
ascii_text = input("Enter ASCII text: ")
try:
hex_output = ascii_text.encode('ascii').hex()
print(hex_output)
except UnicodeEncodeError:
print("Error: Input contains non-ASCII characters.", file=sys.stderr)

if __name__ == "__main__":
import sys
main()
```



Mfano: `Asante Satoshi` katika ASCII inatoa `5468616e6b73205361746f736869` katika heksadesimali.



Tayarisha hati ya muamala. Hapa kuna mfano wa umbizo linalotarajiwa:



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



ambayo inaundwa na:





- **Lengwa Address**: Bitcoin Address halali. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. Hii inaweza kuwa Address yako mwenyewe, ikiwa ungependa kurejesha fedha zilizohamishwa kwako mwenyewe;
- **Kiasi kilichohamishwa**: kiasi cha muamala, hapa `0.00001` BTC. **Tafadhali kumbuka**: kwa kuwa kitengo kinachotumiwa katika Electrum ni BTC, kiasi kilichoonyeshwa katika hati ya shughuli lazima pia kionyeshwe katika BTC, na si katika Sats;
- Hati **OP_RETURN**: Ujumbe uliogeuzwa kuwa heksadesimali ukitanguliwa na hati(`OP_RETURN <ujumbe>`), 0. Hapa, `5468616e6b73205361746f736869` kwa ujumbe katika hexadecimal.



⚠️ **Tahadhari**: Ni muhimu sana kuashiria `0` baada ya OP_RETURN, kwa kuwa opcode hii inaashiria hati kuwa batili, na kufanya towe lisitumike kabisa. Nodi za mtandao zitafuta pato hili kutoka kwa seti yao ya UTXO. Ukiweka thamani nyingine zaidi ya `0`, itapotea kabisa: bitcoins zako zitachukuliwa kuwa zimeteketezwa. Kwa hivyo unapaswa kuingiza `0` kila wakati na OP_RETURN ili kurekodi data unayotaka, lakini bila kuhusisha pesa nayo, ambayo itapotea.



Kidokezo: Tumia zana ya [OP_RETURN Jenereta] (https://resources.davidcoen.it/opreturnelectrum/) ili generate hati kiotomatiki. Hata kama zana hii inapendekeza kuweka kiasi katika BTC, kuweka kitengo kimesanidiwa katika Electrum.



![image](assets/fr/05.webp)



Ili kubadilisha kitengo kinachotumiwa na Electrum, kwenye upau wa menyu pata "Mapendeleo", kisha kwenye kichupo cha "Vitengo" chagua BTC / mBTC / bits au Sats :



![image](assets/fr/06.webp)




---

## Hatua ya 5: Tuma muamala



Katika Electrum, nenda kwenye kichupo cha Tuma.



![image](assets/fr/07.webp)



Katika sehemu ya "Lipa kwa", bandika hati iliyotayarishwa (kwa mfano, ile iliyo hapo juu).



![image](assets/fr/08.webp)



Sehemu ya "Lipa kwa" inapaswa kuonyeshwa katika Green, na kiasi cha muamala kinapaswa kuonekana kwenye laini iliyo hapa chini.



Angalia kiasi na kitengo chake katika sehemu ya Kiasi.



Bofya kwenye "Lipa..." na urekebishe ada zako za muamala kulingana na kiasi ambacho uko tayari kulipa na kasi ambayo ungependa shughuli yako ishughulikiwe na Miner na kuunganishwa kwenye kizuizi.



![image](assets/fr/09.webp)



Bofya Sawa na uthibitishe muamala kwa nenosiri lako. Dirisha la uthibitisho litaonekana.




---

## Hatua ya 6: Thibitisha usajili



Baada ya shughuli kuthibitishwa (hii inaweza kuchukua dakika chache), nenda kwenye kichupo cha "Historia".



![image](assets/fr/10.webp)



Bofya kulia kwenye shughuli na uchague "Tazama kwenye Explorer" ili kuona maelezo.



Vinginevyo, nakili lengwa la Address (kwa mfano, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) na uitazame kwenye kivumbuzi cha Blockchain kama vile [Mempool.space](https://Mempool.space/) au [block.info]



Tafuta sehemu ya OP_RETURN katika maelezo ya muamala ili kuona ujumbe wako.



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## Vidokezo na mbinu bora





- Jaribu kwa kiasi kidogo: Anza na muamala mdogo (k.m. Sats 1000) ili kuepuka makosa ya gharama kubwa.
- Hakikisha kuwa pato lililo na OP_RETURN ni sawa na sifuri, vinginevyo bitcoins zako zitapotea kabisa.
- Angalia kitengo: Hakikisha kiasi kilichowekwa kinalingana na kitengo kilichoonyeshwa kwenye Electrum (BTC, mBTC au Sats).
- Ada ya muamala: Ikiwa mtandao una msongamano, ongeza ada kwa uthibitisho wa haraka.
- Ujumbe mfupi: Maingizo ya OP_RETURN yana mipaka ya baiti 80. Panga ujumbe wako ipasavyo.



---

## Rasilimali muhimu





- Pakua Electrum: [electrum.org](https://electrum.org/)
- Jenereta ya hati ya OP_RETURN: [resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Blockchain Explorers: [Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)