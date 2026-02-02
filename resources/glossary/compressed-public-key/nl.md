---
term: Gecomprimeerde publieke sleutel
definition: Compacte vorm van een publieke sleutel die alleen de x-coördinaat en een pariteitsprefix (02 of 03) gebruikt.
---

Een publieke sleutel wordt gebruikt in scripts (direct in de vorm van een publieke sleutel of als Address) om bitcoins te ontvangen en te beveiligen. Een ruwe publieke sleutel wordt voorgesteld door een punt op een elliptische curve, bestaande uit twee coördinaten (`x, y`) van elk 256 bits. In onbewerkt formaat is een openbare sleutel dus 512 bits groot, de extra byte om het formaat te identificeren niet meegerekend. Een gecomprimeerde openbare sleutel daarentegen is een compactere vorm van openbare sleutelrepresentatie. Het gebruikt alleen de `x` coördinaat en een voorvoegsel (`02` of `03`) dat de pariteit van de `y` coördinaat aangeeft (even of oneven).


Als we dit vereenvoudigen tot het veld van reële getallen, gegeven dat de elliptische kromme symmetrisch is ten opzichte van de x-as, bestaat er voor elk punt $P$ (`x, y`) op de kromme een punt $P'$ (`x, -y`) dat ook op dezelfde kromme ligt. Dit betekent dat er voor elke `x` slechts twee mogelijke waarden van `y` zijn, positief en negatief. Bijvoorbeeld, voor een gegeven abscis `x` zijn er twee punten $P1$ en $P2$ op de elliptische kromme, met dezelfde abscis maar tegengestelde ordinaten:




Om te kiezen tussen de twee potentiële punten op de kromme, wordt een prefix die specificeert welke `y` gekozen moet worden toegevoegd aan `x`. Met deze methode kan de grootte van een openbare sleutel worden teruggebracht van 520 bits naar slechts 264 bits (8 bits van de prefix + 256 bits voor `x`). Deze weergave staat bekend als de gecomprimeerde vorm van de openbare sleutel.


In de context van cryptografie met elliptische krommen gebruiken we echter niet de reële getallen, maar een eindig veld van orde `p` (een priemgetal). In deze context wordt het "teken" van `y` bepaald door de pariteit, dat wil zeggen of `y` even of oneven is. Het voorvoegsel `0x02` geeft dan een even `y` aan, terwijl `0x03` een oneven `y` aangeeft.


Beschouw het volgende voorbeeld van een ruwe publieke sleutel (een punt op de elliptische curve) in hexadecimaal:

```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```


We kunnen het voorvoegsel, `x`, en `y` isoleren:

```plaintext
Prefix = 04
To determine the parity of `y`, we examine the last hexadecimal character of `y`:
```

Basis 16 (hexadecimaal): f

Basis 10 (decimaal): 15

y is oneven

```

The prefix for the compressed public key will be `03`. The compressed public key in hexadecimal becomes:
```

K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6

```