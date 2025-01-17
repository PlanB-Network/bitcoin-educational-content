---
term: ENTÊTE DE BLOC
---

L'entête de bloc est une structure de données servant de composant principal dans la construction d'un bloc Bitcoin. Chaque bloc est composé d'un entête et d'une liste de transactions. L'entête de bloc contient les informations cruciales qui permettent d'assurer l'intégrité et la validité d'un bloc au sein de la blockchain. L'entête de bloc contient 80 octets de métadonnées et se compose des éléments suivants :
* La version du bloc ;
* L'empreinte du bloc précédent ;
* La racine de l'arbre de Merkle des transactions ;
* L'horodatage du bloc ;
* La cible de difficulté ;
* Le nonce.

Par exemple, voici l'entête du bloc n° 785 530 au format hexadécimal, miné par Foundry USA le 15 avril 2023 :

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Si l'on décompose cet entête, on peut reconnaitre :
* La version : 

```text
00e0ff3f
```

* L'empreinte précédente :

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```

* La racine de Merkle :

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```

* L'horodatage :

```text
bcb13a64
```

* La cible :

```text
b2e00517
```

* Le nonce : 

```text
43f09a40
```

Pour être valide, un bloc doit disposer d'un entête qui, une fois haché avec `SHA256d`, produit une empreinte inférieure ou égale à la cible de difficulté.

> ► *En anglais, on parle d'un « Block Header ».*

