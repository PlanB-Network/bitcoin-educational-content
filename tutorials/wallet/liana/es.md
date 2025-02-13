---
name: Liana
description: Crear y utilizar un monedero en Liana
---
![cover](assets/cover.webp)

En este tutorial, explicaremos paso a paso cómo utilizar la aplicación Liana en un ordenador. Entre otras cosas, aprenderás a configurar un plan de sucesión automatizado, a recibir y enviar bitcoins en situaciones normales y a recuperar fondos de una cartera existente tras un periodo determinado.

En enero de 2025, los monederos hardware compatibles con Liana eran: BitBox02, Blockstream Jade, Blockstream Jade Plus, COLDCARD MK4, COLDCARD Q, Ledger Nano S, Ledger Nano S Plus, Ledger Nano X, Ledger Flex, Specter DIY.

Si desea recuperar fondos de un monedero Liana existente, lea la presentación a continuación y vaya directamente a la sección "Recuperación de bitcoins".

## Presentación del software Liana

Liana es un paquete de software de código abierto diseñado para la creación y gestión de carteras avanzadas, en particular como parte de un sistema de herencia automatizado o un sólido mecanismo de copia de seguridad. El proyecto ha sido desarrollado desde 2022 por Wizardsardine, una empresa cofundada por Kévin Loaec y Antoine Poinsot. En el sitio web oficial, Liana se presenta como "una cartera sencilla para la conservación personal, con funcionalidades de recuperación y herencia". El programa funciona en ordenadores (Linux, MacOS, Windows) y su código fuente (abierto) está disponible [en GitHub](https://github.com/wizardsardine/liana).

Liana se basa en la programabilidad de Bitcoin para crear un monedero avanzado. En particular, aprovecha los bloqueos temporales (*timelocks*), que permiten gastar fondos sólo una vez transcurrido un periodo de tiempo determinado, y que intervienen en la recuperación de Bitcoins. Un monedero Liana se compone, por tanto, de varias rutas de gasto:


- Una vía principal de gasto, siempre disponible;
- Al menos una ruta de recuperación, que se vuelve accesible después de cierto tiempo.

El diagrama siguiente ilustra el funcionamiento de una cartera con dos vías de gasto:

![Schéma explicatif](assets/fr/01.webp)

Esta operación permite establecer varias configuraciones, entre ellas :


- Un plan de sucesión (o herencia), que permite a los herederos recuperar los fondos en caso de fallecimiento del usuario. Para más información sobre este tema, recomendamos la lectura de la [parte 4](https://planb.network/courses/btc102/233c88d3-2e8e-5eba-ac06-efe67a209038) del curso BTC102.
- Una copia de seguridad reforzada con un tiempo de recuperación, dando al usuario la posibilidad de utilizar su monedero sin tener que guardar la frase secreta correspondiente y arriesgarse a que se la roben, durante un robo por ejemplo.
- Una red de seguridad para las personas que se inician en Bitcoin: gestionarán su propio monedero, y su "tutor" (un familiar, por ejemplo) se reservará el derecho a recuperar sus fondos tras un periodo determinado.
- Un esquema de firma multiparte (*multisig*) con requisitos reducidos en el tiempo, para hacer frente a la desaparición de uno o más de los participantes, como los socios de una empresa.

El gran punto fuerte de Liana es que introduce una forma normalizada de garantizar la recuperación de los fondos en caso de pérdida de la clave principal, utilizada para los gastos corrientes. Esto representa una enorme innovación para la custodia limpia de fondos, que está plagada de riesgos, sobre todo si no se está bien informado sobre el tema. Por tanto, Liana podría animar incluso a los usuarios más reacios al riesgo a dejar de utilizar un custodio (como una plataforma de intercambio) para guardar sus fondos y recuperar la propiedad de su dinero, en consonancia con el espíritu cypherpunk de Bitcoin.

Por supuesto, Liana tiene sus inconvenientes. El primero es que tienes que actualizar tu monedero regularmente haciendo una transacción en la blockchain de Bitcoin. Esto puede ser un engorro (dependiendo de la frecuencia con la que utilices el software) y costoso (dependiendo del nivel de comisiones del momento), pero es el precio que pagas por una seguridad extra.

Un segundo punto negativo puede ser la confidencialidad. Cuando involucras a otra persona en la configuración, ésta tiene conocimiento de todas tus direcciones y, por tanto, puede controlar tu actividad. Sin embargo, esto no será un problema si optas por una copia de seguridad reforzada, o por un plan de sucesión en el que tu heredero no tenga conocimiento inmediato de los detalles de la cartera.

## Preparación

En este tutorial, estableceremos un plan de sucesión. Utilizaremos :


- Un Ledger Nano S Plus, para los gastos cotidianos;

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

- Un Blockstream Jade, utilizado para recuperar fondos;

https://planb.network/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3

- Dos soportes de almacenamiento (memorias USB) para guardar el descriptor de la cartera;
- Una carta de sucesión, con instrucciones para recuperar los fondos;
- Una bolsa sellada numerada, para garantizar que el dispositivo de recuperación (el Jade) no se ha utilizado.

## Instalación y configuración

Visita el sitio web oficial de Wizardsardine y descarga Liana en https://wizardsardine.com/liana/. También puedes descargar la última versión [del repositorio de GitHub](https://github.com/wizardsardine/liana/releases), donde podrás comprobar la autenticidad del software. La versión utilizada en este tutorial es la 0.9.

![Télécharger Liana](assets/fr/02.webp)

Para saber cómo verificar manualmente la autenticidad e integridad del software antes de instalarlo, le recomendamos que consulte este tutorial :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Instale el software en su máquina y ejecútelo. Elige la opción "*Crear un nuevo monedero Liana*" para configurar tu monedero.

![Accueil Liana](assets/fr/03.webp)

Elige tu tipo de cartera. Si desea configurar una copia de seguridad mejorada con tiempo de recuperación, puede seleccionar la opción "*Construya la suya propia*" y optar por el esquema predeterminado. Esto funcionará de forma muy parecida, salvo que no necesitarás conservar la frase de recuperación de la cartera de hardware.

Ignoramos aquí el caso del *Expanding multisig*, que establece una configuración más compleja.

Para los propósitos de este tutorial, vamos a utilizar la herencia simple.

![Choisir type de portefeuille](assets/fr/04.webp)

A continuación, una rápida explicación.

![Rapide explication](assets/fr/05.webp)

Una vez hayas leído la explicación, podrás configurar las claves de tu monedero Liana. Este es un paso crucial, ya que determina las características de gasto de tu cuenta.

![Configurer clés](assets/fr/06.webp)

En primer lugar, en el menú "Configuración avanzada", puede decidir el "tipo de descriptor", es decir, la forma en que se escribirá el contrato en la cadena. Puede elegir entre dos tipos: P2WSH (SegWit) o Taproot. En ambos casos, la semántica de las condiciones de gasto será la misma. Mientras que P2WSH hace que el contrato sea más fácil de entender, Taproot es superior porque oculta las condiciones no utilizadas y ahorra costes durante la recuperación.

Esta elección es opcional: en caso de duda, deje la opción por defecto (P2WSH en el caso de la versión 0.9, pero está sujeta a cambios).

![Choisir le type de descripteur](assets/fr/07.webp)

A continuación, configure su clave primaria (*clave primaria*). Esta clave (o, mejor dicho, este conjunto de claves) se utilizará para el gasto actual de fondos, que no está sujeto a ninguna condición temporal. Haciendo clic en "*Set*", puede seleccionar el correspondiente *signing device*. En nuestro caso, hemos elegido el monedero físico Ledger Nano S Plus.

Autoriza a compartir la clave pública extendida del dispositivo. Dale a esta clave un nombre significativo (en este caso, "Nano S+"). Ten en cuenta que todas las aplicaciones instaladas en el dispositivo seguirán funcionando con normalidad.

![Configurer clé principale](assets/fr/08.webp)

A continuación, fije la demora de reembolso, es decir, el tiempo tras el cual los fondos pueden ser gastados por la *clave hereditaria*. Este retraso se define en términos de bloques, con cada bloque separado por una media de 10 minutos. Puede oscilar entre 10 minutos (1 bloque) y unos 15 meses (65.535 bloques). Este límite superior es una limitación del protocolo Bitcoin, ya que el tiempo de bloqueo está codificado en 16 bits.

Salvo circunstancias especiales, opte por el plazo más largo: 15 meses o 65.535 bloques. Así ahorrará costes. No obstante, le recomendamos que realice el procedimiento de actualización (descrito en el apartado "Actualización de la cartera") una vez al año, siempre en la misma época del año, para "ritualizar" esta práctica y evitar olvidos.

Aquí, hemos establecido un tiempo de recuperación de una hora (6 bloques) para realizar nuestras pruebas.

![Configurer temps de verrouillage](assets/fr/09.webp)

Por último, configura tu llave patrimonial. Esta clave (o mejor dicho, conjunto de claves) se utilizará para recuperar fondos en caso de desaparición. Haga clic en "*Configurar*", elija el dispositivo de firma y valide la compartición de la clave pública extendida en él.

Para este tutorial, hemos elegido Jade. Dale a la llave un nombre evocador (aquí "Jade"). Al igual que con el primer dispositivo, las cuentas convencionales seguirán funcionando.

![Configurer clé de succession](assets/fr/10.webp)

Una vez realizadas todas estas acciones, compruebe que todo está en orden y haga clic en "*Continuar*" para confirmar sus elecciones.

![Confirmer clés](assets/fr/11.webp)

El siguiente paso es guardar el descriptor de su cartera. Esta es la información que necesita para encontrar los fondos de su cuenta. Contrariamente a la frase mnemotécnica, el descriptor no le permite gastar fondos, por lo que revelarlo sólo planteará un problema de confidencialidad (la persona conocerá todas sus transacciones).

Guarde dos copias del descriptor en soportes electrónicos, como memorias USB. Asegúrate de imprimir también dos copias en papel, para poder acceder a ellas en caso de que se dañen los soportes electrónicos. Cada copia de seguridad debe estar asociada a un dispositivo de firma.

![Sauvegarder descripteur](assets/fr/12.webp)

Nuestro descriptor (que se analiza al final del tutorial) es el siguiente:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

El último paso en la configuración inicial de la cartera es verificar el descriptor en cada una de las carteras de hardware que sirven como dispositivos de firma.

![Enregistrer descripteur](assets/fr/13.webp)

Haga lo mismo para cada dispositivo de firma. Deberá comprobar y confirmar que el descriptor se ha añadido a cada cartera de hardware.

![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)

La información de tu monedero ya está registrada, y todo lo que queda es configurar cómo quieres conectarte a la red Bitcoin. Puedes elegir utilizar tu propio nodo (local o remoto) o utilizar la infraestructura de WizardSardine. En este último caso, tendrás que vincular una dirección de correo electrónico a tu monedero, lo que te permitirá recuperar el descriptor. WizardSardine tendrá acceso a todas sus transacciones. Por lo tanto, se sugiere la primera opción.

![Sélectionner connexion réseau](assets/fr/15.webp)

Hemos elegido utilizar nuestro propio nodo. Puedes utilizar un nodo existente, o instalar un *nodo podado* en tu máquina. Si no tienes acceso a ningún otro nodo, instala tu propio nodo en tu máquina, lo que te llevará algún tiempo (del orden de varios días).

![Choisir type de nœud](assets/fr/16.webp)

Para este tutorial, hemos utilizado un servidor Electrum existente (público). Pero ¡cuidado! Tenía acceso a toda nuestra actividad con la cartera Liana. Así que usa tu propio nodo si quieres proteger tu privacidad.

![Connexion serveur Electrum public](assets/fr/17.webp)

Una vez completada la configuración del nodo, se abrirá la pantalla principal, mostrando tu monedero Liana recién creado.

Aproveche para guardar la unidad de recuperación en un lugar seguro. Debe guardarse en un lugar estratégico, para que pueda ser encontrada por tus herederos en caso de fallecimiento.

Para mayor seguridad, puedes colocar los componentes utilizados para la recuperación en una bolsa sellada (*bolsa a prueba de manipulaciones*) y anotar su número de serie en algún lugar. Así te aseguras de que nadie ha accedido a él y de que tu dispositivo sigue siendo válido.

En nuestro ejemplo, hemos reunido los siguientes elementos:


- Blockstream Jade como dispositivo de firma del patrimonio;
- Un cable USB para conectar y recargar el dispositivo;
- Una copia de seguridad en papel de la sentencia en caso de mal funcionamiento o daños en el dispositivo (tenga en cuenta que el soporte también puede ser metálico y, por tanto, estar protegido de la intemperie, como es el caso de las cápsulas Cryptosteel, por ejemplo);
- La llave USB que contiene el descriptor de la cartera ;
- Una copia de seguridad en papel del descriptor, en caso de mal funcionamiento o daños en la llave USB (esta copia de seguridad no se ha fotografiado aquí);
- Una carta de sucesión en la que se describan los pasos a seguir para recuperar los fondos.

![Éléments de récupération](assets/fr/18.webp)

¡Y ponemos estos artículos bajo precinto!

![Sachet scellé récupération](assets/fr/19.webp)

## Recepción de fondos

La pantalla principal de Liana muestra su saldo y las transacciones (pasadas y actuales) vinculadas a su cartera. En nuestro caso, el saldo es cero, lo cual es normal.

![Écran principal](assets/fr/20.webp)

Para recibir fondos, vaya a la pestaña "*Recibir*" y haga clic en "*Generar dirección*". En la pantalla aparecerá una nueva dirección. Es más larga que en las carteras convencionales: es una dirección vinculada a un contrato independiente (P2WSH o Taproot).

![Générer nouvelle adresse](assets/fr/21.webp)

Debe verificar esta dirección en su cartera de hardware haciendo clic en "*Verificar en dispositivo de hardware*".

![Vérifier adresse portefeuille matériel](assets/fr/22.webp)

Una vez enviados los fondos, la transacción aparece en la pantalla principal (primero como no confirmada y luego como confirmada). En este caso, hemos enviado 50.000 satoshis (algo más de 50 dólares en el momento de la transferencia) para esta prueba. Huelga decir que la cantidad transferida en su caso tendrá que ser un orden de magnitud superior a este valor, debido a las comisiones de transacción.

![Vérifier solde](assets/fr/23.webp)

Puedes comprobar el estado de expiración de tus fondos yendo a la pestaña "*Coins*". Esta pestaña le muestra las diferentes monedas (UTXO) de su monedero. Aquí podemos ver que la moneda de 50.000 satoshis creada por nuestra transacción expira el mismo día (dentro de una hora).

![Obtenir informations pièce](assets/fr/24.webp)

Para comprender mejor el modelo de representación UTXO utilizado en Bitcoin, puede consultar la primera parte del curso sobre confidencialidad en Bitcoin escrito por Loïc Morel :

https://planb.network/courses/btc204
## Gastos corrientes

El gasto corriente es la situación normal para usar Liana. El envío de bitcoins con la llave maestra funciona como en todos los monederos Bitcoin clásicos como Electrum o Sparrow.

Para realizar un cargo, vaya a la pestaña "*Enviar*" e introduzca la información esencial: la dirección BTC del destinatario, el importe a enviar y la tarifa de cargo deseada. También se puede añadir una descripción (guardada localmente) para mayor comodidad. En nuestro ejemplo, enviamos 10.000 satoshis a un tal Bob, por una tasa de cargo de 4 sat/ov, o 0,67$ en el momento de la transacción.

Liana también ofrece "control de monedas": usted indica qué moneda (UTXO) desea gastar. Aquí, hemos elegido la moneda de 50.000 satoshis creada anteriormente.

![Envoyer fonds clé principale](assets/fr/25.webp)

A continuación, firma la transacción con tu dispositivo de firma vinculado a la llave maestra haciendo clic en "*Firmar*". Tendrás que verificar y confirmar la transacción en tu monedero físico. En este caso, hemos utilizado el Nano S Plus para firmar la transacción.

![Signer transaction clé principale](assets/fr/26.webp)

Por último, difunda la transacción a través de la red haciendo clic en "*Difundir*". Ten en cuenta que el envío de fondos restablecerá el tiempo de recuperación de las monedas usadas.

![Diffuser transaction clé principale](assets/fr/27.webp)

La transacción aparecerá en la pantalla principal y su saldo se actualizará.

![Solde après dépense](assets/fr/28.webp)

## Actualización de la cartera

Como se ha explicado anteriormente, el monedero Liana requiere que actualices tus fondos regularmente realizando una transacción en la blockchain. Si no lo haces, tus fondos pueden ser recuperados por tu heredero (o por tu segundo dispositivo en el caso de una copia de seguridad mejorada). Esta situación no es extremadamente peligrosa, pero anula el propósito de establecer este mecanismo: mantener el control de tus bitcoins sin recurrir a un tercero de confianza, beneficiándote al mismo tiempo de una red de seguridad.

Aparecerá un aviso antes de que sus fondos (o parte de ellos) caduquen y puedan gastarse con la clave de recuperación. Le indicará que su "vía de recuperación" (*vía de recuperación*) estará pronto disponible. Dada la brevedad de nuestro plazo de recuperación (una hora), este mensaje se muestra directamente en nuestro caso.

![Avertissement chemin récupération](assets/fr/29.webp)

Cuando se acerque la fecha límite, aparecerá un botón pidiéndole que actualice los fondos correspondientes.

![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)

Para actualizar sus monedas, vaya a la pestaña "*Monedas*" y haga clic en "*Refrescar moneda*" en la casilla correspondiente. Si tiene varias monedas, debe actualizarlas una a una, y a intervalos relativamente cortos, por razones de confidencialidad. Para mantener los costes bajos, puede consolidar sus fondos enviando toda la cartera a una nueva dirección receptora, pero esto afectará a su confidencialidad.

![Actualiser pièce](assets/fr/31.webp)

Indique la tasa de comisión deseada para la transacción. Como se trata de una transferencia a ti mismo, puedes establecer una tasa de comisión bastante baja, sobre todo si lo haces varios días antes del vencimiento.

![Transfert à soi-même](assets/fr/32.webp)

La transacción (etiquetada como "*autotransferencia*") sólo será visible en la pestaña "*Transacciones*".

![Transactions après auto-transfert](assets/fr/33.webp)

Una vez confirmado, ¡tu moneda está a salvo! Puedes estar tranquilo hasta la próxima fecha de caducidad.

## Recuperación del bitcoin

A la hora de recuperar fondos de la cartera Liana, puede encontrarse con una de estas dos situaciones. Puede que tenga acceso al ordenador en el que está instalado el software, en cuyo caso todo lo que tiene que hacer es abrirlo (lo que ocurrirá en el caso del modelo de copia de seguridad mejorado). Sin embargo, puede que no tengas acceso a este ordenador, por lo que empezaremos desde cero. Ten en cuenta que el procedimiento de recuperación es el mismo en ambos casos.

Para empezar, descarga Liana desde [el sitio web oficial de Wizardsardine](https://wizardsardine.com/liana/), o desde [el repositorio de GitHub](https://github.com/wizardsardine/liana/releases), donde podrás comprobar la autenticidad del software. Instala el software y ejecútalo. La versión utilizada en nuestro caso es la 0.9, por lo que el aspecto visual puede haber cambiado. En la pantalla de bienvenida, selecciona la opción "Añadir un monedero Liana existente".

![Ajouter portefeuille existant](assets/fr/34.webp)

Configura cómo quieres conectarte a la red. Puedes elegir usar tu propio nodo (local o remoto) o usar la infraestructura de WizardSardine. En este último caso, necesitarás la dirección de correo electrónico utilizada por el creador de la cartera, para que los fondos puedan ser localizados automáticamente. Si no tienes esta información, elige la primera opción.

![Sélectionner connexion réseau](assets/fr/35.webp)

Si utiliza su propio nodo, importe el descriptor de la cartera. Se trata de una descripción técnica de la cuenta, que le permite recuperar los fondos depositados en ella. En nuestro caso, es la siguiente información:

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

![Importer descripteur](assets/fr/36.webp)

A continuación, Liana le pedirá que introduzca una frase mnemotécnica. Si tienes un dispositivo de firma (monedero hardware) que funciona, sáltate esta parte. Si su dispositivo ha desaparecido o está dañado, pero dispone de las 12 o 24 palabras correspondientes, puede seguir utilizando esta opción. Para mayor seguridad (si la cantidad a recuperar es elevada), le sugerimos que obtenga un nuevo monedero físico y utilice la frase mnemotécnica para restaurar las claves en él.

En nuestro caso, utilizamos el monedero físico Blockstream Jade como dispositivo de recuperación y elegimos omitir ("*Skip*") este paso.

![Passer phrase mnémotechnique](assets/fr/37.webp)

Compruebe y guarde el descriptor en su dispositivo de firma seleccionándolo en la pantalla. Si tu monedero físico no aparece, comprueba que está conectado y desbloqueado. Compruebe y confirme que esta información se ha añadido a su dispositivo.

![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)

Configure su nodo. Puedes utilizar un nodo existente o instalar un *nodo podado* en tu máquina. En nuestro caso, hemos utilizado un nodo existente.

![Choisir type de nœud](assets/fr/39.webp)

Para este tutorial, utilizamos un servidor público de Electrum. Sin embargo, tenía acceso a toda nuestra actividad con la cartera Liana. Si quieres proteger tu privacidad, es mejor que utilices tu propio nodo.

![Connexion serveur Electrum public](assets/fr/17.webp)

Una vez que hayas configurado tu nodo, accederás a la pantalla principal del monedero, donde podrás ver el saldo y las transacciones anteriores vinculadas a la cuenta. También puedes ver si se pueden recuperar fondos. Aquí vemos que se puede recuperar una moneda.

![Accueil Liana récupération](assets/fr/40.webp)

Para recuperar los fondos de la cartera, vaya a Configuración ("*Configuración*") en la parte inferior izquierda y haga clic en "*Recuperación*".

![Récupération dans paramètres](assets/fr/41.webp)

Gaste la moneda en el monedero marcando la casilla correspondiente. Indique la dirección BTC a la que desea enviar los fondos, así como la tarifa de la comisión de transacción. A continuación, haga clic en "*Siguiente*".

![Récupération des pièces](assets/fr/42.webp)

Firme la transacción haciendo clic en "*Firmar*" y validando la transacción en su monedero físico.

![Signer transaction clé de récupération](assets/fr/43.webp)

A continuación, difúndelo por la red haciendo clic en "*Difundir*".

![Diffuser transaction clé de récupération](assets/fr/44.webp)

La transacción debería aparecer en la pantalla principal. Una vez confirmada, ¡la recuperación se ha completado!

![Écran principal après récupération](assets/fr/45.webp)

## Vídeos

Si quiere saber más sobre Liana, hay algunos vídeos que le darán una idea más clara de cómo funciona. Aquí tienes un vídeo de presentación de Liana con Kévin Loaec y Antoine Poinsot :

![Vidéo de présentation avec Kévin Loaec et Antoine Poinsot](https://youtu.be/siuLmQo1lM8)

Y aquí tienes un tutorial sobre el uso de Liana, con Antoine Poinsot :

![Vidéo-tutoriel avec Antoine Poinsot](https://youtu.be/JrG4WMVPZDQ)

Las manipulaciones mostradas en este último son similares a las presentadas en este tutorial.

## Bonificación: análisis de descriptores

El descriptor es una cadena de caracteres legible por el ser humano que describe exhaustivamente un conjunto de direcciones. Combina una serie de informaciones esenciales para recuperar las partes (UTXO) de una cartera avanzada. La forma de escribir el descriptor se basa en [Miniscript syntax](https://bitbox.swiss/blog/understanding-bitcoin-miniscript-part-2/), el lenguaje de scripting desarrollado por Andrew Poelstra, Pieter Wuille y Sanket Kanjalkar en 2019.

Para entender mejor por qué es importante esta cadena de caracteres, analicemos el descriptor de nuestro ejemplo, que es :

```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```

De este descriptor puede extraerse la siguiente información:


- `wsh` (abreviatura de *witness script hash*): Este es el tipo de salida transaccional creada. Si hubiéramos optado por utilizar Taproot, el identificador habría sido `tr`.
- o_d`: Es un operador lógico que indica que *debe cumplirse una de las dos* condiciones siguientes para que el gasto sea aceptado (la `_d` indica una sintaxis particular).
- `pk` (abreviatura de *clave pública*): Este operador comprueba una firma dada contra la siguiente clave pública, y da la respuesta como un booleano (TRUE o FALSE).
- `[3689a8e7/48'/0'/0'/2']`: Este elemento incluye la *huella digital* de la clave maestra para el monedero hardware principal (en este caso el Nano S Plus), y la ruta de derivación a la clave privada extendida vinculada (de la que derivan todas las demás claves privadas).
- `xpub6FKY ... WQa`: Esta es la clave pública extendida vinculada a la cartera principal de hardware (aquí el Nano S Plus)
- `/<0;1>/*`: Son las vías de derivación para la obtención de claves y direcciones simples: `0` para la recepción, `1` para operaciones internas (*cambio*), con un "comodín" (`*`) que permite la derivación secuencial de varias direcciones de forma configurable, similar a la gestión de "gap limit" del software clásico de carteras.
- y_v`: Es un operador lógico que indica que *deben cumplirse las dos condiciones siguientes* para que el gasto sea aceptado (la `_v` indica una sintaxis particular).
- `v:pkh` (abreviatura de *verify: public key hash*): Este operador verifica una firma y clave pública dadas contra el hash de clave pública (*hash*) que sigue. Se trata esencialmente de la misma comprobación que para los scripts P2PKH y P2WPKH.
- `[42e629dd/48'/0'/0'/2']`: Se trata del mismo elemento anterior (formado por la traza y la ruta de derivación), salvo que se indica la traza de la clave maestra de la cartera de recuperación hardware (en este caso la Jade).
- `xpub6DpQ ... WQd`: Esta es la clave pública extendida vinculada a la cartera de recuperación de hardware (aquí el Jade).
- `older(6)` : Este operador comprueba que la salida transaccional creada debe tener una antigüedad estrictamente superior a 6 bloques para poder ser gastada.

El último dato (`8alrve5h`) es la suma de comprobación del descriptor, y corresponde al identificador de la cartera.

Los guiones creados por esta cartera tendrán la siguiente forma:

```plaintext
<primary_key> CHECKSIG IFDUP NOTIF DUP HASH160 <recovery_key_hash> EQUALVERIFY CHECKSIGVERIFY <locktime> CHECKSEQUENCEVERIFY ENDIF
```

Dado que la seguridad de tu monedero Bitcoin también depende de que entiendas cómo funciona, te sugiero que estudies en profundidad los mecanismos de los monederos deterministas y jerárquicos realizando este curso de formación gratuito sobre Plan ₿ Network :

https://planb.network/courses/cyp201