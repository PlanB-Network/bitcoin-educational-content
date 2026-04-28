---
term: Diskret logaritm
definition: Svårlöst matematiskt problem som utgör grunden för Bitcoins kryptografiska säkerhet.
---

Den diskreta logaritmen är ett matematiskt problem som används i vissa kryptografiska algoritmer med publik nyckel. Om man i en cyklisk grupp av ordning $q$, med en generator $g$, har en ekvation av formen $g^x = h$, så kallas $x$ den diskreta logaritmen av $h$ med avseende på basen $g$, modulo $q$. Enkelt uttryckt handlar det om att bestämma exponenten $x$ när $g$, $h$ och $q$ är kända. Den diskreta logaritmen är alltså inversen av exponentialen i en ändlig cyklisk grupp. För stora värden på $q$ anses det dock vara algoritmiskt svårt att lösa problemet med den diskreta logaritmen. Denna egenskap utnyttjas för att garantera säkerheten i många kryptografiska protokoll, t.ex. Diffie-Hellman-protokollet för nyckeln Exchange.


Den diskreta logaritmen används också inom kryptografi med elliptiska kurvor (ECC), bland annat i ECDSA (*Elliptic Curve Digital Signature Algorithm*). I samband med elliptiska kurvor utvidgas problemet med den diskreta logaritmen till att hitta en skalär $k$ så att $k \cdot G = K$, där $G$ och $K$ är punkter på kurvan och $\cdot$ representerar punktmultiplikationsoperationen. I samband med Bitcoin kan skript använda antingen ECDSA eller Schnorr-protokollet för att låsa UTXO:er. Båda förlitar sig på att det är omöjligt att beräkna den diskreta logaritmen.