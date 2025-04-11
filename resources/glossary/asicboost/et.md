---
term: ASICBOOST

---
ASICBOOST on 2016. aastal leiutatud algoritmiline optimeerimismeetod, mille eesmärk on suurendada Bitcoini kaevandamise tõhusust umbes 20% võrra, vähendades iga päise hash-katse jaoks vajalike arvutuste hulka. See meetod kasutab kaevandamiseks kasutatava SHA256 hash-funktsiooni omadust, mis jagab andmed enne nende töötlemist plokkideks. ASICBOOST säilitab ühe neist plokkidest muutumatuna mitme hashimise katse jooksul, võimaldades kaevandajal teha selle ploki jaoks ainult osa tööd mitme katse jooksul. Selline andmete jagamine võimaldab eelmiste arvutuste tulemusi taaskasutada, vähendades seega kehtiva hash'i leidmiseks vajalike arvutuste koguarvu.

ASICBOOSTi saab kasutada kahes vormis: Overt ASICBOOST ja Covert ASICBOOST. Overt ASICBOOSTi vorm on kõigile nähtav, kuna see hõlmab bloki `nVersion` välja kasutamist nonce'ina ja mitte tegeliku `Nonce` muutmist. Varjatud vorm püüab neid muudatusi varjata, kasutades Merkle'i puid. See teine meetod on aga pärast SegWit'i kasutuselevõttu muutunud vähem tõhusaks teise Merkle-puu tõttu, mis suurendab selle kasutamiseks vajalike arvutuste arvu.

Kokkuvõttes võimaldab ASICBOOST kaevuritele mitte teostada tõelist täielikku SHA256 kõigi hashing-katsete puhul, kuna osa tulemusest jääb muutumatuks, mis kiirendab kaevurite tööd.