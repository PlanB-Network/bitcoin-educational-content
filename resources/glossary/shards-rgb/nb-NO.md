---
term: Shards (rgb)
definition: Separat gren i DAG-grafen som sporer historikken til en RGB-kontrakts overganger.
---

I forbindelse med RGB-protokollen representerer en Shard en distinkt gren i den acykliske rettede grafen (DAG) som sporer historien til en Contracts tilstandsoverganger. Den utgjør en sammenhengende delmengde av settet med overganger, som for eksempel tilsvarer sekvensen av operasjoner som kreves for å attestere gyldigheten til en bestemt eiendel siden Genesis. Denne mekanismen gjør det mulig å isolere spesifikke segmenter av den samlede historikken, slik at det blir enklere å verifisere på klientsiden.