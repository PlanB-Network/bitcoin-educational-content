---
term: CÓDIGO DE PAGO REUTILIZABLE

---
En BIP47, un código de pago reutilizable es un identificador estático generado a partir de un monedero Bitcoin que permite una transacción de notificación y la derivación de direcciones únicas. Esto evita la reutilización de direcciones, que conlleva una pérdida de privacidad, sin tener que derivar y transmitir manualmente nuevas direcciones no utilizadas para cada pago. En BIP47, los códigos de pago reutilizables se construyen de la siguiente manera:


- El byte 0 corresponde a la versión;
- El byte 1 es un campo de bits para añadir información en caso de uso específico;
- El byte 2 indica la paridad del `y` de la clave pública;
- Del byte 3 al byte 34, encontrará el valor `x` de la clave pública;
- Del byte 35 al byte 66, está el código de cadena asociado a la clave pública;
- Del byte 67 al byte 79, el relleno es cero.

Generalmente se añade una parte legible por el ser humano (HRP) al principio del código de pago y una suma de comprobación al final, y luego se codifica en base58. La construcción de un código de pago es, por tanto, bastante similar a la de una clave extendida. Aquí está, por ejemplo, mi propio código de pago BIP47 en base58:

```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```

En la implementación PayNym de BIP47, los códigos de pago también pueden expresarse en forma de identificadores asociados a la imagen de un robot. Aquí está el mío, por ejemplo:

```text
+throbbingpond8B1
```

El uso de códigos de pago con la implementación PayNym está disponible actualmente en Sparrow Wallet en PC y en Samourai Wallet en móvil.