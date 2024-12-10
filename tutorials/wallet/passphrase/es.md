---
name: Frase de paso BIP39
description: Entendiendo cómo funciona una frase de paso
---
![cover](assets/cover.webp)

## ¿Qué es una frase de paso BIP39?

Las carteras HD se generan típicamente a partir de una frase mnemotécnica que consiste en 12 o 24 palabras. Esta frase es muy importante porque permite la restauración de todas las claves de una cartera en caso de que su medio físico (como una cartera de hardware, por ejemplo) se pierda. Sin embargo, constituye un único punto de fallo porque si se ve comprometida, un atacante podría robar todos los bitcoins.

![PASSPHRASE BIP39](assets/notext/01.webp)

Aquí es donde entra en juego la frase de paso. Es una contraseña opcional que puedes elegir libremente, la cual se añade a la frase mnemotécnica en el proceso de derivación de claves para mejorar la seguridad de la cartera.

![PASSPHRASE BIP39](assets/notext/02.webp)

Ten cuidado de no confundir la frase de paso con el código PIN de tu cartera de hardware o la contraseña utilizada para desbloquear el acceso a tu cartera en tu computadora. A diferencia de todos estos elementos, la frase de paso juega un papel en la derivación de las claves de tu cartera. **Esto significa que sin ella, nunca podrás recuperar tus bitcoins.**

La frase de paso trabaja en conjunto con la frase mnemotécnica, alterando la semilla de la cual se generan las claves. Así, incluso si alguien obtiene tu frase de 12 o 24 palabras, sin la frase de paso, no pueden acceder a tus fondos. **Usar una frase de paso crea esencialmente una nueva cartera con claves distintas. Modificar (incluso ligeramente) la frase de paso generará una cartera diferente.**

## ¿Por qué deberías usar una frase de paso?

La frase de paso es arbitraria y puede ser cualquier combinación de caracteres elegida por el usuario. Usar una frase de paso ofrece varias ventajas. Primero, reduce todos los riesgos asociados con el compromiso de la frase mnemotécnica al requerir un segundo factor para acceder a los fondos (robo, acceso a tu hogar, etc.).

Luego, puede ser utilizada estratégicamente para crear una cartera señuelo, para lidiar con coacciones físicas para robar tus fondos como el infame "*ataque del destornillador de 5 dólares*". En este escenario, la idea es tener una cartera sin frase de paso que contenga solo una pequeña cantidad de bitcoins, suficiente para satisfacer a un potencial agresor, mientras se tiene una cartera oculta. Esta última utiliza la misma frase mnemotécnica pero está asegurada con una frase de paso adicional.

Finalmente, usar una frase de paso es interesante cuando se desea controlar la aleatoriedad de la generación de la semilla de la cartera HD.

## ¿Cómo elegir una buena frase de paso?
Para que la frase de paso sea efectiva, debe ser suficientemente larga y aleatoria. Al igual que con una contraseña fuerte, recomiendo elegir una frase de paso que sea lo más larga y aleatoria posible, con una variedad de letras, números y símbolos para hacer cualquier ataque de fuerza bruta imposible.

También es importante guardar adecuadamente esta frase de paso, de la misma manera que la frase mnemotécnica. **Perderla significa perder el acceso a tus bitcoins**. Aconsejo enérgicamente en contra de memorizarla únicamente en tu cabeza, ya que esto aumenta irrazonablemente el riesgo de pérdida. Lo ideal es anotarla en un medio físico (papel o metal) separado de la frase mnemotécnica. Este respaldo debe obviamente ser almacenado en una ubicación diferente de donde se guarda tu frase mnemotécnica para prevenir que ambos sean comprometidos simultáneamente.

## Tutoriales

Para configurar una frase de paso en un dispositivo Ledger (Stax, Flex, o Nano), puedes consultar este tutorial:

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49