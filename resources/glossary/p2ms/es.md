---
term: P2MS

definition: Script multifirma que bloquea bitcoins con múltiples claves públicas que requieren un umbral de firmas.
---
P2MS son las siglas de *Pay to Multisig*, que se traduce como "pagar a múltiples firmas". Es un modelo de escritura estándar utilizado para establecer condiciones de gasto en un UTXO. Permite el bloqueo de bitcoins con múltiples claves públicas. Para gastar estos bitcoins, se requiere una firma con un número predefinido de claves privadas asociadas. Por ejemplo, un `P2MS 2/3` implica `3` claves públicas con `3` claves privadas secretas asociadas. Para gastar los bitcoins bloqueados con este script P2MS, se necesita una firma con al menos `2` de las `3` claves privadas. Se trata de un sistema de seguridad de umbral.

Este script fue inventado en 2011 por Gavin Andresen cuando se hizo cargo del mantenimiento del cliente principal de Bitcoin. Hoy en día, P2MS solo es utilizado marginalmente por algunas aplicaciones. La gran mayoría de las multifirmas modernas utilizan otros scripts como P2SH o P2WSH. Comparado con éstos, P2MS es extremadamente trivial. Las claves públicas que lo componen se revelan al recibir la transacción. Utilizar un P2MS también es más caro que otros scripts de multifirma.

