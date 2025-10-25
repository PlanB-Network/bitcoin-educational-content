---
name: Electrum OP_RETURN
description: Kwandika ubutumwa kuri Blockchain Bitcoin na Electrum
---

![cover](assets/cover.webp)




Iyi nyigisho y’intambwe ku yindi ikwereka ingene wondika ubutumwa kuri Blockchain Bitcoin ukoresheje Wallet Electrum. Iyi nzira ikoresha amabwirizwa ya OP_RETURN kugira ngo winjize umwandiko mu gucuruza, uboneke ku mugaragaro kuri Blockchain. Kurikiza izi ntambwe zoroshe kugira ngo ushobore kwiyandikisha neza.



---
## Ibisabwa





- Mudasobwa (Idirisha, macOS canke Linux).
- Uguhuzwa na Internet.
- Ama satoshi makeyi (Sats) canke ama bitcoins (BTC) muri Wallet yawe kugira ngo ushobore kwishura amahera y’ugucuruza n’amahera.
- Igihindura inyandiko mu nyuguti zitandatu (nk’akarorero urubuga rwo kuri interineti) canke igikoresho kigenewe nk’[iki gikoresho co guhindura inyandiko za OP_RETURN](https://resources.davidcoen.it/opreturnelectrum/).



---

## Intambwe ya 1: Gukuraho no gushiramwo Electrum



![image](assets/fr/01.webp)



1. Sura urubuga rwemewe rwa Electrum: [electrum.org](https://electrum.org/).


2. Gukuraho verisiyo ihuye n’ivyo ukoresha (Windows, macOS, Linux).


3. Shiraho Electrum nk’uko uwuyishizeho abivuga.


4. Suzuma ubutungane bwa dosiye yakuwe kuri interineti (ntibikenewe, ariko ni vyiza kubera imvo z’umutekano) mu kugereranya umukono wa dosiye canke Hash.



→ Ibindi bisobanuro ku nyigisho ya Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Intambwe ya 2: Rema canke ushiremwo Wallet



1. Gutanguza Electrum.


2. Hitamwo Rema Wallet nshasha canke Gusubizaho Wallet iriho nimba usanzwe ufise ijambo rya seed (ijambo ryo gusubizaho).


3. Kurikiza amabwirizwa kugira ngo utunganye Wallet yawe :




 - Ku bijanye n’igitabu gishasha ca Wallet, nushire akamenyetso k’interuro yawe ya seed maze uyishire ahantu heza (impapuro, igitabu c’umutekano, n’ibindi).
 - Ku Wallet iriho, shiramwo ijambo ryawe rya seed kugira ngo uyigarure.


4. Shiraho ijambobanga kugira ngo ukingire Wallet yawe.



→ Ibindi bisobanuro ku nyigisho ya Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Intambwe ya 3: Suzuma amafaranga ariho



Raba neza ko Wallet yawe irimwo amafaranga ahagije (BTC) canke amasatoshi (Sats) kugira ngo :




- Amafaranga y’ugucuruza (nk’akarorero, 0,00001 BTC canke 1000 Sats).
- Amafaranga y’ugucuruza, ahinduka bivanye n’ubunini bw’urubuga (muri rusangi ni ibihumbi bikeyi vy’ama Sats).



Raba Balance iri muri Electrum kugira ngo umenye amahera yawe.



![image](assets/fr/02.webp)



Niba ari ngombwa, ushire BTC canke Sats kugira ngo ugaburire Wallet yawe. Kugira ngo ubikore, genda kuri 'Kwakira' hanyuma ukande kuri 'Rema Igisabwa' :



![image](assets/fr/03.webp)



Ivyo bizokwerekana ukwakira Address:



![image](assets/fr/04.webp)



→ Ibindi bisobanuro ku nyigisho ya Electrum :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Intambwe ya 4: Tegura ubutumwa buzokwandikwa .



Hitamwo ubutumwa wipfuza kwinjiza (nk'akarorero `Urakoze Satoshi`). Iciyumviro: Ubutumwa bwa OP_RETURN bushobora gushika kuri bytes 80, ni ukuvuga inyuguti 80 za ASCII.



*Fata umwanya wiyumvire: ivyo wandika kuri Blockchain Bitcoin ni ivy'ibihe bidahera kandi birashikira bose, rero :*




- usige insiguro nziza y'ubumuntu bwacu,
- wirinde kwinjiza ibirimwo ushobora kwicuza



*Ikibanza ca Blockchain n'ama bitcoins yawe ni agaciro, ukoreshe neza kandi ufise intumbero*



Guhindura ubutumwa bwawe mu bice cumi na gatandatu :




- Ushobora gukoresha [igikoresho co kuri interineti](https://www.rapidtables.com/convert/number/ascii-to-hex.html), ariko urabe ko udakoresha amakuru y’agaciro ng’aho (naho, mu ngingo ngenderwako, amakuru agenewe gusohorwa kuri Blockchain Bitcoin biciye ku kibazo c’ibanga ca OP_RETURN ataco atanga);
- Kugira ngo ubone ibanga rikomeye, kora uguhindura mu karere ukoresheje Python ntoyi :



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



Akarorero: `Urakoze Satoshi` muri ASCII itanga `5468616e6b73205361746f736869` mu bice cumi na bitandatu.



Tegura inyandiko y’ugucuruza. Aha niho akarorero k'uburyo bwitezwe:



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



igizwe na :





- Iyo uja Address**: Igikoresho gikora Bitcoin Address. Ici, `bc1q879cv4p5q6s9537umutuku3zss33d3turzad8`. Ivyo bishobora kuba Address yawe bwite, nimba wipfuza kwisubiza amahera wimuriwe;
- Amafaranga yimuriwe**: amafaranga y’ugucuruza, hano `0.00001` BTC. **Iciyumviro**: kuko igice gikoreshwa muri Electrum ari BTC, amafaranga yerekanwa mu nyandiko y’ugucuruza na yo nyene ategerezwa kugaragazwa muri BTC, atari muri Sats ;
- Inyandiko **OP_RETURN**: Ubutumwa bwahinduwe mu nkuru cumi n'itandatu bubanjirijwe n'inyandiko(`OP_RETURN <ubutumwa>), 0`. Aha, `5468616e6b73205361746f736869` ku butumwa buri mu bice cumi na bitandatu.



⚠️ **Iciyumviro**: Ni vyiza cane kwerekana `0` inyuma ya OP_RETURN, kuko iyi opcode igaragaza ko inyandiko idakora, igatuma igisohoka kidashobora gukoreshwa ubuziraherezo. Ivyuma vy'urubuga bizokuraho iki gisohoka mu gice cabo ca UTXO. Niwinjiza agaciro katari `0`, kazobura ataco kazosubirwamwo: ama bitcoins yawe azofatwa nk'ayaturitse. Ushobora rero kwama winjiza `0` ukoresheje OP_RETURN kugira ngo wandike amakuru wipfuza, ariko utafatanije amahera na yo, ivyo vyoba vyatakaye.



Impanuro: Koresha igikoresho [OP_RETURN Generator] kugira ngo generate inyandiko ubwayo. Naho iki gikoresho coba gisaba kwinjiza amahera muri BTC, ugume ukoresha iyo unit muri Electrum.



![image](assets/fr/05.webp)



Kugira ngo uhindure igice gikoreshwa na Electrum, mu rutonde rw'ibiharuro urondere "Ivyo ukunda", hanyuma mu gice ca "Ibiharuro" uhitemwo BTC / mBTC / bits canke Sats :



![image](assets/fr/06.webp)




---

## Intambwe ya 5: Wohereze amafaranga



Muri Electrum, genda ku rubuga rwo kohereza.



![image](assets/fr/07.webp)



Mu kibanza ca "Pay to", ushiremwo inyandiko wateguye (nk'akarorero, iyo iri hejuru).



![image](assets/fr/08.webp)



Ubuhinga bwa "Pay to" bukwiye kwerekanwa muri Green, kandi amahera y'ugukoresha akwiye kugaragara ku murongo uri musi.



Suzuma umubare n'igice cawo mu kibanza Umubare.



Fyonda kuri "Pay..." maze utunganye amafaranga yawe y'ugucuruza akurikije amahera wifuza kwishura n'umuvuduko ushaka ko ugucuruza kwawe gukorwa na Miner maze bishizwe mu gice.



![image](assets/fr/09.webp)



Fyonda OK maze wemeze ko ukoresheje ijambobanga ryawe. Idirisha ryo kwemeza rizoboneka.




---

## Intambwe ya 6: Suzuma ko wiyandikishije



Igihe amafaranga yemejwe (ivyo bishobora gutwara iminota mikeyi), genda kuri "History" tab.



![image](assets/fr/10.webp)



Fyonda iburyo kuri iyo transaction uhitemwo "View on Explorer" kugira ngo ubone ido n'ido.



Canke, kopira aho uja Address (nk'akarorero, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) maze uyibone ku gikoresho co gutohoza Blockchain nka [Mempool.ikibanza](https://Mempool.ikibanza/) [amakuru y'uruzitiro](https://amakuru y'uruzitiro/).



Rondera ahantu OP_RETURN mu makuru y’ibikorwa kugira ngo ubone ubutumwa bwawe.



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## Impanuro n'ibikorwa vyiza





- Igerageza n’amahera make: Tangura n’amahera make (nk’akarorero Sats 1000) kugira ngo wirinde amakosa atwara amahera menshi.
- Raba neza ko igisohoka kirimwo OP_RETURN kingana na zero, ahandi ho ama bitcoins yawe azozimangana ubuziraherezo.
- Suzuma igice: Raba neza ko amahera winjije ahuye n’igice kigaragara muri Electrum (BTC, mBTC canke Sats).
- Amafaranga y’ugucuruza: Nimba urubuga rwuzuye, wongere amafaranga kugira ngo wemeze ningoga.
- Ubutumwa bugufi: Ivyinjira muri OP_RETURN bigarukira kuri bytes 80. Tegura ubutumwa bwawe bihuye n’ivyo.



---

## Ibikoresho vy'ingirakamaro





- Gukuraho umuyagankuba: [umuyagankuba.org](https://umuyagankuba.org/)
- OP_RETURN umuyagankuba: [ibikoresho.davidcoen.it/uguhindura umuyagankuba/](https://ibikoresho.davidcoen.it/uguhindura umuyagankuba/)
- Blockchain Abashakashatsi: [Mempool.ikirere](Mempool.ikirere/), [amakuru y'uruzitiro](amakuru y'uruzitiro/)