---
term: P2MS
---

P2MS significa *Pay to Multisig*, que se traduce como "pagar a múltiples firmas". Es un modelo de script estándar utilizado para establecer condiciones de gasto en un UTXO. Permite bloquear bitcoins con múltiples claves públicas. Para gastar estos bitcoins, se requiere una firma con un número predefinido de claves privadas asociadas. Por ejemplo, un `P2MS 2/3` involucra `3` claves públicas con `3` claves privadas secretas asociadas. Para gastar los bitcoins bloqueados con este script P2MS, se necesita una firma con al menos `2` de las `3` claves privadas. Este es un sistema de seguridad por umbral.

Este script fue inventado en 2011 por Gavin Andresen cuando tomó el control del mantenimiento del cliente principal de Bitcoin. Hoy en día, P2MS solo se utiliza marginalmente por algunas aplicaciones. La gran mayoría de las multisignaturas modernas utilizan otros scripts como P2SH o P2WSH. En comparación con estos, P2MS es extremadamente trivial. Las claves públicas que contiene se revelan al recibir la transacción. Usar un P2MS también es más caro que otros scripts de multisignatura.

> ► *Los P2MS a menudo se llaman "bare-multisig", que podría traducirse como "multifirma desnuda" o "multifirma cruda". A principios de 2023, los scripts P2MS estuvieron en el centro de una controversia debido a su uso indebido dentro del protocolo Stamps. Su impacto en el conjunto de UTXO fue señalado notablemente.*