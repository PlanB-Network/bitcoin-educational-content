---
name: Pastel Wallet
description: Tutorial sobre Cake Wallet y pagos silenciosos
---

![cover](assets/cover.webp)


Esta guía explora [**Cake Wallet**](https://cakewallet.com/): una wallet multidivisa de código abierto, sin custodia y centrada en la privacidad, disponible para Android, iOS, macOS, Linux y Windows. Nos sumergiremos en sus características de privacidad específicas de Bitcoin, recorreremos el envío/recepción de Bitcoin a través de **Pagos Silenciosos** (un protocolo de privacidad mejorado de on-chain) y echaremos un vistazo a la implementación de PayJoin v2 para transacciones asíncronas.


## características principales



- [**Pagos Silenciosos (BIP-352)**](https://bips.dev/352/) mejora los anteriores [BIP 47 códigos de pago](https://silentpayments.xyz/docs/comparing-proposals/bip47/) también llamados "PayNyms" con direcciones ocultas reutilizables. Cuando un remitente utiliza su dirección de pago silencioso, su wallet obtiene una dirección única de un solo uso utilizando diferentes claves que se combinarán en una dirección única de un solo uso Taproot. Los registros de la cadena de bloques (blockchain) muestran transacciones no relacionadas, impidiendo la vinculación de los pagos entrantes. Los pagos silenciosos ofrecen una serie de ventajas, entre las que se incluyen:
    - Direcciones reutilizables: No hay necesidad de generate una nueva dirección para cada transacción, proporcionando una mejor experiencia de usuario y una mayor privacidad
    - Aumento cero de los costes: Los pagos silenciosos no aumentan el tamaño ni el coste de las transacciones.
    - Mayor anonimato: Los observadores externos no pueden vincular las transacciones a una dirección de Silent Payment.
    - No se requiere interacción entre emisor y receptor: Las transacciones pueden realizarse sin comunicación entre las partes.
    - Direcciones únicas para cada pago: Eliminando el riesgo de reutilización accidental de direcciones.
    - No requiere servidor: Los pagos silenciosos pueden realizarse sin necesidad de un servidor dedicado.
- PayJoin v2** mitiga el análisis del grafo de transacciones fusionando las entradas de emisores y receptores en una única transacción. Cake Wallet implementa dos avances críticos:
    - Transacciones asíncronas**: El emisor y el receptor ya no necesitan estar conectados simultáneamente para completar una transacción privada.
    - Comunicación sin servidor**: Ninguna de las partes necesita ejecutar un servidor Payjoin, lo que elimina una importante barrera técnica.
- Coin Control** permite la selección manual de UTXO durante las transacciones. Esto evita la vinculación accidental de direcciones al gastar varios UTXO con orígenes diferentes.
- Compatibilidad con TOR**, lo que permite a los usuarios enrutar su tráfico de red a través de la red Tor
- RBF** (Sustituir por tasa) permite ajustar la tasa después de enviar una transacción.


## 1️⃣ Configuración de la Wallet


Cake Wallet ofrece una amplia gama de plataformas compatibles. Puedes elegir entre `Android`, `iOS / macOS` , `Linux` y `Windows`.  Para empezar, visite https://docs.cakewallet.com/get-started/ y seleccione su sistema operativo.


![image](assets/en/01.webp)


Tras la instalación, establece un `PIN` (4 ó 6 dígitos). Entonces lo verás:


1. `Crear un nuevo Wallet` (para nuevos usuarios)

2. restaurar Wallet (para carteras existentes)


![image](assets/en/02.webp)


En la siguiente pantalla podrás elegir entre una amplia gama de criptomonedas. Selecciona "Bitcoin", pulsa "Siguiente" e introduce un "nombre Wallet" para identificar el wallet. Al pulsar en "Configuración avanzada" aparecerá una serie de "Opciones de privacidad". Realice estos cambios:



- Fiat API:** seleccione `Sólo Tor` (enruta las solicitudes de precios a través de Tor)
- Swap:** seleccione `Tor Only` (anonimiza el tráfico de intercambio)


Por defecto se genera el tipo BIP-39 seed, con la opción de cambiar al tipo Electrum seed. Las vías de derivación son las siguientes:



- Electrum: `m/0'`
- BIP-39: `m/84'/0'/0`


Si quieres añadir una capa de seguridad adicional, puedes configurar una `passphrase`.  El objetivo principal de una passphrase es proporcionar protección adicional contra ataques físicos. Aunque un atacante encuentre la frase seed, no podrá acceder a su wallet sin la passphrase correcta. En otras palabras, la frase seed por sí sola representa una wallet, mientras que la frase seed más la passphrase crea una wallet completamente diferente sin conexión con la original. Esta característica también permite "monederos secretos" protegidos por la passphrase, y le da una negación plausible. En una situación coercitiva, podrías revelar la frase seed mientras mantienes activos más grandes a salvo en la wallet protegida por la passphrase.


Si ya estás ejecutando tu propio nodo, activa `Add New Custom Node` y proporciona tu `Node Address` para validar transacciones y bloques dentro de tu propia infraestructura. Una vez que haya terminado pulse en `Continue` y `Next` para crear su wallet.


![image](assets/en/03.webp)


En la siguiente pantalla, aparece una cláusula de exención de responsabilidad:


```
On the next page you will see a series of words. This is your unique and private seed and it is the ONLY way to recover your wallet in case of lass or malfunction. It is YOUR responsibility to write it down and store it in a safe place outside of the Cake Wallet app.
```


![image](assets/en/04.webp)


Para conocer las mejores prácticas para guardar su frase mnemotécnica, consulte este tutorial:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Toca `Entiendo. Muéstrame mi seed` y guarda estas palabras en un lugar seguro A continuación, pulse "Verificar seed" y después de la verificación "Abrir Wallet".


## 2️⃣ Configuración


Antes de profundizar, echemos un vistazo a la `Pantalla de inicio` y a la `Configuración`.


En la pantalla de inicio podemos ver diferentes elementos desplegados:



- el `menú hamburguesa` nos lleva a la `configuración`
- Saldo disponible
- Tarjeta Silent Payments para empezar a escanear las transacciones enviadas a su dirección de Silent Payment
- La tarjeta Payjoin `Activa` Payjoin para preservar la privacidad y ahorrar comisiones
- en la parte inferior hay accesos directos a `Wallet Overview`, `Receive`, `Swap` entre Bitcoin y otras monedas, `Send` y `Buy`


![image](assets/en/11.webp)


Tocando el icono `Menú de hamburguesa` se abre el menú de configuración. Vamos a revisar las opciones.


![image](assets/en/05.webp)


### A - Conexión y sincronización 🔗


Aquí podemos reconectar el wallet, gestionar nodos y conectarnos a nuestro propio nodo (recomendado). El `Silent Payments Scanning` nos permite personalizar el escaneo especificando `Scan from block height` o `Scan from date`.


![image](assets/en/06.webp)


Como característica `Alpha` también existe la opción de `Habilitar Tor incorporado` para enrutar el tráfico a través de la red Tor.


### B - Configuración de pagos silenciosos 🔈


Podemos activar la tarjeta de Pagos Silenciosos en la pantalla de inicio para mostrar esta función. Activar "Escanear siempre" permite a wallet monitorizar continuamente la cadena de bloques en busca de pagos silenciosos entrantes. Podemos especificar los parámetros de escaneo para personalizar el proceso de escaneo a nuestras necesidades como se ha descrito anteriormente.


![image](assets/en/07.webp)


### C - Seguridad y copia de seguridad 🗝️


Para proteger nuestra wallet, podemos crear una copia de seguridad siguiendo las instrucciones de la aplicación. Así nos aseguraremos de tener una copia segura de nuestras claves privadas, lo que nos permitirá recuperar nuestra wallet si la perdemos o nos la roban. Además, podemos ver nuestra frase y claves privadas de seed, cambiar nuestro PIN, activar la autenticación biométrica, Firmar / Verificar y configurar 2FA para una capa adicional de protección.


![image](assets/en/08.webp)


**Nota**: A partir de septiembre de 2025, se requiere que la autenticación biométrica de huellas dactilares en dispositivos Android funcione con al menos una implementación biométrica de Clase 2, para más detalles consulte [aquí](https://source.android.com/docs/security/features/biometric/measure#biometric-classes). Sin embargo, este requisito puede cambiar en el futuro.


### D - Configuración de privacidad 🔒


También podemos mejorar la seguridad de nuestra wallet utilizando Tor para encriptar nuestra conexión a Internet y salvaguardar nuestra privacidad cuando accedemos a fuentes externas. Además, podemos evitar las capturas de pantalla para mantener la confidencialidad de la información de nuestra wallet, habilitar las direcciones autogeneradas para crear nuevas en cada transacción y deshabilitar las acciones de compra/venta para evitar transacciones no autorizadas. Además podemos `Habilitar PayJoin`, que es otra característica de privacidad que revisaremos más adelante.


![image](assets/en/09.webp)


### E - Otros ajustes 🔧


Otros ajustes nos permiten gestionar la prioridad de las comisiones y establecer el nivel de comisión por defecto para nuestras transacciones. Esto nos permite controlar las tarifas de transacción asociadas a nuestros pagos silenciosos, teniendo en cuenta la utilización actual de la red.


![image](assets/en/10.webp)


## 3️⃣ Recepción de ₿itcoin mediante pagos silenciosos


Hay varias opciones y tipos de dirección disponibles para recibir Bitcoin. `Segwit (P2WPKH)` *(empezando por bc1q....)* es la opción por defecto.  Vamos a seleccionar `Pagos silenciosos` en este ejemplo.


Para recibir un pago silencioso, pulse primero el icono "Recibir" en Cake Wallet. A continuación, introduzca el importe que espera recibir. A continuación, introduzca el importe que espera recibir. Para especificar el tipo de dirección, vuelva a pulsar "Recibir" en la parte superior de la pantalla y seleccione "Pagos silenciosos" entre las opciones.


En la pantalla principal, aparecerá su código QR de Pago Silencioso reutilizable y su dirección. Como era de esperar, la dirección es bastante larga:


`sp1qq0ryu780uwragyk06prxn29830a9csnl3wvr4as6fwh73rzn28zzcqmc6ve36vadllfztaa403ty9et0rlzup7kt55qh486gxzrde6y27c8s6x5p` .


![image](assets/en/12.webp)


Ahora, utilice una BIP-352 compatible wallet (como Blue Wallet) para escanear este código QR y enviar el pago. Verás que la wallet obtiene una dirección de destino única a partir de tu dirección silenciosa.


![image](assets/en/13.webp)


## 4️⃣ Envío de ₿itcoin mediante Silent Payments


Como Blue Wallet sólo puede `Enviar` Pagos Silenciosos, utilizaremos otra BIP 352 compatible como parte receptora. Este proceso es idéntico al de una transacción normal con Bitcoin.



- Pulse `Enviar` en la pantalla de inicio
- pegando nuestra dirección reutilizable `sp1qq...` o escaneando el código QR directamente en la aplicación.
- Selecciona cuánto quieres gastar de tu saldo disponible
- Pulse "Enviar" en la parte inferior de la pantalla para confirmar la transacción


Una vez que hemos introducido la dirección `sp1qq...`, la wallet deriva automáticamente una dirección `bc1p...` Taproot correspondiente (P2TR) en segundo plano, que se utilizará para el pago silencioso.


Opcionalmente, podemos escribir una nota interna para cada transacción, ajustar la configuración de las comisiones o seleccionar determinados UTXOs para la transacción utilizando la función `Coin Control`.


![image](assets/en/14.webp)


deslice el dedo hacia la derecha para confirmar la transacción.


Una vez enviada la transacción, se le preguntará si desea añadir este contacto a su libreta de direcciones.


![image](assets/en/15.webp)


## 5️⃣ PayJoin


Repasemos en qué consiste PayJoin (https://docs.cakewallet.com/cryptos/bitcoin/#payjoin):


payjoin v2 es una característica de Bitcoin que preserva la privacidad y ahorra costes, permitiendo al emisor y al receptor de una transacción trabajar juntos para crear una única transacción. Esta transacción tiene entradas de *ambos* el remitente y el destinatario, rompiendo las técnicas de vigilancia más comunes contra Bitcoin y permitiendo un mejor escalado y ahorro de tasas en algunas circunstancias también


Para saber más sobre PayJoin también puedes visitar el siguiente tutorial.


https://planb.academy/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f

Para utilizar PayJoin ambas partes necesitan una wallet compatible con PayJoin, y el destinatario necesita tener al menos una moneda o salida en su wallet. Para empezar, sigue estos pasos:


1. Pulse sobre el "Menú Hamburguesa" y pulse sobre el botón "Privacidad"

2. Activar la opción `Usar Payjoin

3.  Pulse "Recibir" en la pantalla de inicio y aparecerá un código QR PayJoin y un botón de copia (si se selecciona Segwit)


![image](assets/en/16.webp)


## 6️⃣ Otras características


Hay varias otras características como `Swaps` multidivisa, opciones de `Compra y Venta` con diferentes conexiones de vendedores y programas específicos de Cake como `Cake Pay`, que te permite comprar tarjetas prepago o tarjetas regalo.


![image](assets/en/17.webp)


## 🎯 Conclusión


Este es nuestro análisis de Cake Wallet, que ofrece la práctica privacidad de Bitcoin gracias a funciones como Silent Payments (BIP-352) y Payjoin v2.


Los Pagos Silenciosos sustituyen las direcciones desechables por direcciones ocultas reutilizables para evitar la vinculación on-chain de las transacciones entrantes. Aunque los problemas de sincronización de las versiones anteriores han mejorado notablemente, se requieren algunos requisitos computacionales mayores para escanear y detectar los Pagos Silenciosos, lo que exige más recursos y ancho de banda.


Payjoin v2 altera el análisis de las cadenas al fusionar las entradas del remitente y el destinatario en transacciones únicas sin comisiones adicionales ni coordinación central. Esto rompe la heurística común de propiedad de las entradas, lo que supone una ventaja significativa, ya que significa que no se puede asumir que todas las entradas pertenecen al remitente.


Para los usuarios que dan prioridad al anonimato financiero, Cake Wallet es una opción viable. Incorpora protocolos de privacidad directamente en su funcionalidad principal, haciéndolos accesibles sin ninguna complejidad técnica. A medida que aumenta la vigilancia sobre las cadenas de bloques públicas, herramientas como ésta ayudan a mantener la privacidad de las transacciones donde más importa. Una implantación más amplia de estas normas en el panorama de la wallet sería un avance bienvenido.


## 📚 Recursos


https://cakewallet.com


https://docs.cakewallet.com/


https://github.com/cake-tech/cake_wallet


https://blog.cakewallet.com/


[https://silentpayments.xyz/](https://silentpayments.xyz/)


[ttps://bips.dev/352/](https://bips.dev/352/)


https://payjoin.org/