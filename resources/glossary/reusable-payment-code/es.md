---
term: CÓDIGO DE PAGO REUTILIZABLE
---

En BIP47, un código de pago reutilizable es un identificador estático generado desde una cartera de Bitcoin que permite una transacción de notificación y la derivación de direcciones únicas. Esto evita la reutilización de direcciones, lo que conduce a una pérdida de privacidad, sin tener que derivar y transmitir manualmente direcciones nuevas y sin usar para cada pago. En BIP47, los códigos de pago reutilizables se construyen de la siguiente manera:
* El byte 0 corresponde a la versión;
* El byte 1 es un campo de bits para agregar información en caso de uso específico;
* El byte 2 indica la paridad de la `y` de la clave pública;
* Desde el byte 3 hasta el byte 34, encontrarás el valor `x` de la clave pública;
* Desde el byte 35 hasta el byte 66, está el código de cadena asociado con la clave pública;
* Desde el byte 67 hasta el byte 79, hay un relleno de ceros.

Generalmente se agrega una Parte Legible por Humanos (HRP) al principio del código de pago y un checksum al final, y luego se codifica en base58. La construcción de un código de pago es así bastante similar a la de una clave extendida. Aquí está mi propio código de pago BIP47 en base58 como ejemplo:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

En la implementación de PayNym de BIP47, los códigos de pago también pueden expresarse en forma de identificadores asociados con la imagen de un robot. Aquí está el mío, por ejemplo:

```text
+throbbingpond8B1
```

El uso de códigos de pago con la implementación de PayNym está actualmente disponible en Sparrow Wallet en PC y en Samourai Wallet en móvil.