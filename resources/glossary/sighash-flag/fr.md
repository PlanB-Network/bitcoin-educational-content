---
term: SIGHASH FLAG
---

Paramètre dans une transaction Bitcoin permettant de déterminer les composants d'une transaction (inputs et outputs) couvertes par la signature associée, qui deviennent donc immuables. Le SigHash Flag est un octet ajouté à la signature numérique de chaque entrée. Le choix du SigHash Flag affecte donc directement les parties de la transaction qui sont figées par la signature et celles qui peuvent encore être encore modifiées par la suite. Ce mécanisme assure que les signatures engagent les données de transaction de manière précise et sécurisée, selon l'intention du signataire. Trois principaux SigHash Flags existent :

-`SIGHASH_ALL` (`0x01`) : La signature s'applique à tous les inputs et outputs de la transaction, les verrouillant ainsi intégralement ;

-`SIGHASH_NONE` (`0x02`) : La signature s'applique à tous les inputs, mais à aucun output, permettant la modification des outputs après la signature ;

-`SIGHASH_SINGLE` (`0x03`) : La signature couvre tous les inputs et seulement un output correspondant à l'index de l'input signé.

En complément de ces trois SigHash Flags, le modificateur `SIGHASH_ANYONECANPAY` (`0x80`) peut être combiné avec chacun des types précédents. Quand ce modificateur est utilisé, seule une partie des inputs est signée, laissant les autres ouverts à modification. Voici les combinaisons existantes avec le modificateur :

-`SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`) : La signature s'applique à un seul input tout en couvrant tous les outputs de la transaction ;

-`SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`) : La signature couvre un seul input, sans engager aucun output ;

-`SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`) : La signature s'applique à un seul input et uniquement à l'output ayant le même index que cet input.

> ► *Un synonyme parfois utilisé de « SigHash » est « Signature Hash Types ».*

