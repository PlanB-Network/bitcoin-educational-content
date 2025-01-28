---
name: Guarda tu frase mnemotécnica
description: Descubra las mejores prácticas para proteger su monedero Bitcoin
---
![cover](assets/cover.webp)

Cuando crea un nuevo monedero Bitcoin, ya sea a través de un monedero software o hardware, recibe una frase mnemotécnica compuesta por 12 o 24 palabras. Esta frase es muy importante, ya que es la fuente de derivación de todas las claves privadas que aseguran sus Bitcoins. Por lo tanto, debe salvaguardarse cuidadosamente para garantizar la recuperación de sus fondos en caso de rotura, robo o pérdida del soporte de su monedero.

En este tutorial, exploraremos las mejores prácticas para guardar tu frase mnemotécnica de forma segura, para que no pierdas el acceso a tus bitcoins.

## Conciencia del riesgo

La mnemotecnia te da acceso total y sin restricciones a todos tus bitcoins. Cualquiera que posea esta frase puede robar tus fondos, incluso sin acceso físico al soporte que aloja tu monedero.

Esto significa, por ejemplo, que si utilizas un monedero Bitcoin en un Ledger, cualquiera con acceso a tu frase mnemotécnica puede robar todos tus bitcoins, incluso sin tener acceso al propio Ledger. Esta es la razón por la que **nunca debes compartir tu frase mnemotécnica**, sea cual sea la situación.

Esta frase es, por tanto, la información única que te permite restaurar el acceso a tus bitcoins en caso de pérdida, robo o daño del soporte del monedero. Tomemos de nuevo el ejemplo de Ledger: si pierdes el dispositivo, puedes recuperar tus fondos introduciendo tu frase mnemotécnica en un nuevo Ledger o en cualquier otro monedero compatible, ya sea software o hardware.

Por eso es importante guardar esta frase con el máximo cuidado y mantenerla en un lugar seguro, como detallaremos en las siguientes secciones.

**Tu frase mnemotécnica se expone así a dos riesgos principales: robo y pérdida**

El robo puede producirse de dos formas principales:


- Alguien ha accedido físicamente a tu copia de seguridad, por ejemplo durante un robo o a través de un amigo;
- Ha compartido voluntaria o involuntariamente su condena con otra persona.

Para evitar el robo físico de la copia de seguridad de tu frase mnemotécnica, es importante que la guardes en un lugar seguro. Veremos este punto en detalle en las siguientes secciones.

Cuando se trate de intentos de robo a distancia, recuerda siempre no compartir nunca tu frase mnemotécnica, sea cual sea la situación. Los intentos de suplantación de identidad son habituales: correos electrónicos fraudulentos, sitios web que imitan a los de los monederos oficiales o solicitudes directas a través de diversos canales de comunicación. Si alguien te pide tu frase mnemotécnica, es una estafa, ¡incluso en caso de emergencia! Es habitual que los ladrones se hagan pasar por empleados del fabricante de tu monedero físico, pero ten en cuenta que estas empresas nunca te pedirán tu frase de contraseña, sea cual sea la situación. Así que mantente muy atento a cualquier comunicación que recibas, ya sea por correo electrónico, teléfono, correo postal, redes sociales o incluso en persona.

Cuando necesites introducir tu frase en un monedero hardware o software para restaurar el acceso a tu monedero tras un problema con el soporte inicial, tómate tu tiempo para comprobar la autenticidad e integridad del hardware o software que estás utilizando. No se deje llevar por el pánico y proceda metódicamente.

Además, ten cuidado al manejar tu frase mnemotécnica. Asegúrate de que no te observan otras personas o una cámara.

En cuanto al riesgo de pérdida, puede producirse por tres motivos principales: la pérdida del soporte de copia de seguridad, su degradación o un error en su clasificación. En los siguientes apartados veremos cómo evitar o minimizar estos tres riesgos.

## El apoyo

Para guardar tu frase de recuperación, tienes que escribirla en un soporte físico, como papel o metal. Nunca utilices un soporte digital: no la guardes en un archivo de texto, no le hagas una foto ni la almacenes en un gestor de contraseñas. Estos métodos aumentan considerablemente la superficie de ataque en comparación con los soportes físicos. Por tanto, la regla es clara: utiliza papel, cartón o metal para guardar tu frase.

Aunque escribir su frase en un simple papel ya es una buena práctica, optar por un soporte metálico, como el acero inoxidable, ofrece una seguridad añadida. Este tipo de soporte protege tu frase mnemotécnica de los riesgos de incendio, inundación o derrumbe que pueden afectar al lugar de almacenamiento.

Para quienes busquen una opción económica para respaldar su frase sobre metal, [el método DIY del "*SAFU Ninja*"](https://jlopp.github.io/metal-bitcoin-storage-reviews/reviews/safu-ninja/) es una solución excelente. Basta con comprar en las tiendas arandelas metálicas, un tornillo y una tuerca. Luego grabas las palabras de tu frase en cada arandela, asegurándote de numerarlas, y las ensamblas en el tornillo con la tuerca. Este método de bajo coste ya ofrece una buena resistencia.

![SEED](assets/fr/01.webp)

Crédito de la imagen: [*SAFU Ninja Review*, Jameson Lopp](https://jlopp.github.io/metal-bitcoin-storage-reviews/reviews/safu-ninja/).

Si prefieres invertir en un dispositivo completo de soporte metálico, te recomiendo que eches un vistazo a [las pruebas de resistencia de Jameson Lopp](https://jlopp.github.io/metal-bitcoin-storage-reviews/), que evalúan la mayoría de las soluciones disponibles en el mercado. Le aconsejo que opte por soportes de una sola pieza, como una placa metálica para grabar, estampar o perforar. Por lo general, estos dispositivos ofrecen una resistencia mucho mayor que los sistemas que utilizan letras independientes para ensamblar.

Si opta por una cartera de papel, tiene varias opciones: una simple hoja de papel en blanco, la cartera de cartón que suele venir con su cartera de ferretería, o nuestra plantilla descargable que puede imprimir [haciendo clic aquí](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/wallet-backup-sheet/assets/mnemonic-sheet.pdf).

![SEED](assets/fr/02.webp)

## Copia de seguridad

Ahora que has elegido tu soporte físico, ¡es hora de escribir tu frase de recuperación! Para evitar perder tus bitcoins, sigue estas buenas prácticas.

En primer lugar, asegúrate de que no estás siendo observado, ni por otras personas ni por cámaras, mientras escribes tu frase.

Después, tómate tu tiempo para escribir cada palabra de forma clara y legible. Es posible que tengas que releer tu frase dentro de unos años, o que otra persona tenga que hacerlo como parte de una herencia. Por tanto, es esencial escribir con cuidado.

En teoría, es posible escribir sólo las 4 primeras letras de cada palabra, porque en la lista de 2048 palabras de la BIP39, no hay dos palabras que compartan las mismas 4 primeras letras en el mismo orden. Sin embargo, si tu soporte tiene espacio suficiente, te recomiendo que guardes cada palabra en su totalidad. Esto puede ser útil en caso de degradación parcial del soporte. Por ejemplo, si sólo anota `accu` para la palabra `acuse` y desaparece la letra `u`, es posible que tenga que elegir entre `accuse`, `access`, `accident` o `account`. En cambio, con la palabra completa, aunque falte una letra, sigue siendo fácil reconocer la palabra correcta.

También es esencial escribir las palabras en el orden correcto. Si tienes tus 24 palabras pero no sabes su secuencia exacta, será imposible recuperar tu cartera. Numerar las palabras es igual de importante: si el soporte se estropea o las palabras se desorganizan, numerarlas te permitirá volver a ponerlas fácilmente en el orden correcto.

![SEED](assets/fr/03.webp)

Además, es importante entender que, teóricamente, la frase mnemotécnica por sí sola no siempre es suficiente para recuperar el acceso a tus bitcoins. También necesitas conocer las rutas de derivación utilizadas para generar las claves. Si utilizas un monedero SingleSig con una ruta estándar, será relativamente sencillo recuperar tus claves. Sin embargo, con una ruta no estándar, esto podría llegar a ser imposible, incluso en posesión de la frase mnemotécnica. Para evitar este problema, te recomiendo encarecidamente que anotes, en tu soporte, la ruta de derivación de la cuenta que estás utilizando. Puede encontrar esta información en la configuración del software de su monedero. Por ejemplo, para un monedero Taproot estándar, la ruta de derivación por defecto será :

```txt
m / 86' / 0' / 0' /
```

![SEED](assets/fr/04.webp)

Si utilizas un monedero multisig o un monedero con scripts complejos que incluyen claves de recuperación, como los que ofrece el software Liana, es esencial que guardes tus **Descriptores de Scriptores de Salida**. Estos descriptores contienen toda la información que necesitas, además de las frases de recuperación, para recuperar el acceso a tus bitcoins.

También puedes enriquecer tu copia de seguridad con información adicional relacionada con el soporte de tu monedero. Por ejemplo, anota el código PIN utilizado para desbloquear tu monedero hardware, o las palabras antiphishing si utilizas una COLDCARD.

![SEED](assets/fr/05.webp)

Por otro lado, si utilizas una frase de contraseña, asegúrate de no escribirla en el mismo soporte que tu frase mnemotécnica. La finalidad de la frase de contraseña es proteger tu cartera en caso de robo. Para saber más sobre cómo utilizar una frase de contraseña, echa un vistazo a este tutorial complementario:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Una vez que hayas guardado tu frase mnemotécnica en un soporte físico, es muy recomendable que realices una prueba de recuperación mientras tu monedero recién creado aún está vacío. Esta prueba consiste en anotar una información de ejemplo, borrar deliberadamente el monedero vacío y, a continuación, intentar restaurarlo utilizando únicamente la copia de seguridad física de la frase mnemotécnica. Esto le permitirá comprobar que su copia de seguridad está completa y libre de errores de entrada. También le permitirá familiarizarse con el proceso de recuperación. De este modo, si necesitas recuperarla en el futuro, estarás mejor preparado y evitarás el estrés de un primer intento en una situación real. Para saber más sobre cómo realizar esta prueba, consulta este otro tutorial :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895
Por último, está la cuestión del número de copias de seguridad. Esta elección depende totalmente de su situación personal. Limitar el número de copias, por ejemplo escribiendo su frase mnemotécnica una sola vez en un soporte, reduce el riesgo de robo, pero aumenta el riesgo de pérdida. A la inversa, hacer varias copias reduce el riesgo de pérdida, pero aumenta el riesgo de robo. Así que depende de ti encontrar el equilibrio adecuado para tus necesidades y determinar el número de copias que consideras más apropiado.

## Almacenamiento

Ahora que ya has hecho una copia de seguridad de tu frase mnemotécnica, es el momento de elegir una ubicación de almacenamiento adecuada. Esto dependerá de tu estrategia de seguridad. En cualquier caso, elige un lugar fuera de la vista, donde sea improbable que alguien tropiece con él, pero accesible para comprobaciones periódicas. Asegúrate también de que está protegido de la intemperie, para evitar daños en el sustrato.

También le desaconsejaría almacenar su mnemónica en lugares donde no sea soberano, como una caja de seguridad en una notaría o un banco. Estas opciones pueden parecer seguras, pero implican que dependes de un tercero para acceder a tu copia de seguridad, lo que va en contra de los principios fundamentales de Bitcoin.

Para mayor seguridad, le recomiendo que utilice una bolsa de plástico a prueba de manipulaciones o un sistema de cierre similar. Así podrá comprobar que nadie ha tenido acceso a su frase. Por ejemplo, si guarda su frase en casa y recibe visitas, puede ser imposible saber si alguien la ha visto, memorizado o fotografiado. Una funda a prueba de manipulaciones simplifica este tipo de verificación: si está intacta, puede estar seguro de que su frase ha permanecido secreta. Estas fundas totalmente opacas están disponibles en Internet o en tiendas especializadas en Bitcoin.

![SEED](assets/fr/06.webp)

Por último, cuando guarde su frase en un sobre a prueba de manipulaciones, no olvide anotar el identificador único del sobre. Esto le permitirá verificar su autenticidad durante los controles.

## Gestión del tiempo

Ahora que su frase está cuidadosamente almacenada, es importante establecer un control regular. Compruebe periódicamente que la frase sigue en su lugar de almacenamiento y que no se ha abierto el sobre opaco.

Durante estas comprobaciones, también puede abrir el sobre para examinar el estado del sustrato. Asegúrese de que no está dañado y de que la frase sigue siendo perfectamente legible. Si observas algún signo de deterioro, lo mejor es crear una nueva copia a partir de tu monedero físico. Compruebe que esta nueva copia es funcional y, a continuación, destruya limpiamente la copia dañada para evitar cualquier riesgo de fuga.

Por último, la gestión de frases mnemotécnicas también plantea la cuestión de la herencia. Este tema se tratará con detalle en un futuro tutorial.

## Ir más lejos

Para ir un paso más allá y reforzar aún más tu estrategia de seguridad, te recomiendo que aprendas el funcionamiento técnico de tu monedero Bitcoin. Al comprender cómo interactúan los distintos elementos, así como su importancia e implicaciones, podrás afinar tu estrategia de seguridad con plena conciencia de los riesgos que conlleva. En particular, si comprende a nivel técnico lo que permite la frase mnemotécnica, podrá ajustar la forma en que la registra, almacena y gestiona con el tiempo.

Por eso le invito a realizar el curso de formación gratuito CYP201 ofrecido por Plan ₿ Network. Este curso de formación explica en detalle todo el funcionamiento de los monederos Bitcoin, lo que le permite dominar los aspectos técnicos esenciales para asegurar eficazmente sus fondos :

https://planb.network/courses/cyp201
Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar verde a continuación. No dudes en compartir este artículo en tus redes sociales. ¡Muchas gracias!