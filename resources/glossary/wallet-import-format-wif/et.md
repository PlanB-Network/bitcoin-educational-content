---
term: Wallet import format (WIF)

definition: Bitcoini privaatvõtme Base58Check kodeerimismeetod, et hõlbustada selle importimist või eksportimist rahakottide vahel.
---
Meetod Bitcoini privaatvõtme kodeerimiseks nii, et seda saaks hõlpsamini importida või eksportida erinevate rahakottide vahel. WIF põhineb `Base58Check` kodeeringul, mis sisaldab teavet versiooni kohta, vastava avaliku võtme pakkimist ja kontrollsummat vigade tuvastamiseks trükkimisel. WIFi privaatvõti algab tihendamata võtmete puhul märkidega `5` või tihendatud võtmete puhul märkidega `K` ja `L` ning sisaldab kõiki algse privaatvõtme rekonstrueerimiseks vajalikke märke. WIF-vorming pakub standardiseeritud vahendit privaatvõtme edastamiseks erinevate rahakoti tarkvarade vahel.