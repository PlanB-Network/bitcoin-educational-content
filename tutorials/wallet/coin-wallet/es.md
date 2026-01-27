---
name: Coin Wallet
description: Tutorial sobre Coin Wallet y formas de mejorar la privacidad y la seguridad
---

![cover](assets/cover.webp)


Este tutorial trata sobre [Coin Wallet](https://coin.space/) - una wallet criptográfica autocustodiada para dispositivos móviles, y sobre cómo aumentar la seguridad y la privacidad cuando se utilizan aplicaciones móviles wallet.



## Acerca de Coin Wallet


**Coin Wallet** es un wallet autocustodiado / no custodiado, de código abierto creado por un equipo de entusiastas de Bitcoin en 2015. Comenzó como una aplicación web, seguida de la aplicación iOS en 2017, y la aplicación Android en 2020 - disponible en Google Play, Samsung Galaxy Store, y Huawei AppGallery.


Ventajas clave:


- Arquitectura no privativa de libertad
- Totalmente [código fuente abierto](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- Diseño sencillo y limpio
- Centrado en el objetivo principal: almacenar criptomonedas de forma segura, sin funciones innecesarias
- Compatibilidad multiplataforma: móvil (iOS y Android), escritorio, web
- Soporte RBF (Replace-By-Fee) - acelera las transacciones atascadas en cualquier momento
- Hardware 2FA con llave [YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / FIDO2
- Soporte Tor integrado: dirige todo el tráfico a través de la red Tor para obtener la máxima privacidad



## 1️⃣ Instalación de Coin Wallet

Coin Wallet está disponible en las principales plataformas.



- [iOS App Store](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [Android Google Play](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [Android (Galaxy Store)](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android (Huawei AppGallery)](https://appgallery.huawei.com/app/C112183767)



- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)



- [Android APK](https://coin.space/api/v3/download/android-apk/any)



- [Todos los enlaces](https://github.com/CoinSpace/CoinSpace/releases)


También disponible para escritorio (Windows, Linux, macOS), como aplicación web y a través de Tor.


![image](assets/en/01.webp)


## 2️⃣ Creación de un Wallet y configuración del PIN


Una wallet se crea a partir de una passphrase: una secuencia aleatoria de 12 palabras separadas por espacios, generada a partir de una [lista de 2048 palabras](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts).

Coin Wallet admite frases de contraseña de 12, 15, 18, 21 o 24 palabras importadas de otros monederos.


La passphrase es la forma legible por el ser humano de la clave privada maestra. Debe guardarse de forma segura. La passphrase es todo lo que se necesita para acceder a la wallet o restaurarla. Si se pierde la passphrase, la wallet y todos los fondos se pierden permanentemente. La passphrase nunca debe compartirse. Coin Wallet no almacena claves en ningún servidor o base de datos.


**¿Es seguro un passphrase de 12 palabras?**

Con 2048 palabras posibles por posición, hay 2048¹² ≈ 10³⁹ combinaciones, lo que proporciona ~128 bits de seguridad, comparable a las claves privadas Bitcoin. Este nivel se considera suficiente.


![image](assets/en/02.webp)


Después de escribir y confirmar el passphrase, la aplicación le pedirá que establezca un **PIN** de 4 dígitos para el acceso diario. Para mayor comodidad, puedes activar la autenticación biométrica (huella dactilar o reconocimiento facial) en lugar de utilizar un PIN.


![image](assets/en/03.webp)



No hay cuenta, ni recuperación de claves, ni restablecimiento de passphrase, ni anulación de transacciones. La seguridad es responsabilidad total del usuario.


Para obtener información detallada sobre cómo guardar la frase mnemotécnica:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ Frase de contraseña + PIN. Cuándo y cómo se utilizan


**¿Cuándo se necesita la passphrase?

Sólo en estos raros casos:


- Configuración de wallet en un nuevo dispositivo
- Reinstalación de la aplicación Coin Wallet
- Borrar los datos de la aplicación/navegador (Almacenamiento local)
- Eliminación de una llave hardware de la cuenta
- Introducir el PIN incorrecto tres veces (la aplicación se bloquea por seguridad)


En el uso diario, el PIN de 4 dígitos es suficiente para desbloquear la wallet.


**Frase de contraseña + PIN: ¿Cómo funciona?

La passphrase es la verdadera clave privada maestra y funciona en cualquier dispositivo.

Como teclear 12-24 palabras cada vez sería incómodo, Coin Wallet utiliza un PIN de 4 dígitos para un acceso rápido y cotidiano en el dispositivo actual.

Un simple PIN por sí solo no es lo suficientemente seguro como para proteger directamente la clave maestra, por lo que nunca se utiliza para el cifrado. En su lugar:



- El PIN se envía al servidor y se intercambia por un token criptográfico largo.
- Este token descifra la clave maestra cifrada almacenada únicamente en el dispositivo.


Si el PIN se introduce incorrectamente tres veces, el servidor borra la token de forma permanente. La clave almacenada localmente queda inutilizada, y la única forma de recuperar la wallet es introduciendo la passphrase original.

Este diseño ofrece comodidad y una sólida protección de emergencia.



## 4️⃣ Recepción de ₿itcoin - Address Tipos y privacidad


Coin Wallet admite los tres formatos de dirección Bitcoin:



- Native SegWit (Bech32)** - empieza por **bc1q** - tarifas más bajas, recomendadas
- SegWit anidado (P2SH)** - comienza por **3**
- Legado (P2PKH)** - comienza por **1**


![image](assets/en/04.webp)


**¿Por qué cambia la dirección después de cada ingreso?

Esto es intencionado y protege la privacidad. Cada vez que se reciben monedas, Coin Wallet genera automáticamente una nueva dirección no utilizada. Si se reutilizara la misma dirección (por ejemplo, para el salario mensual), cualquiera podría sumar fácilmente todas las transacciones entrantes en un explorador de blockchain y conocer el ingreso total.


Las direcciones antiguas siguen siendo válidas para siempre -puede seguir recibiéndolas-, pero utilizar una dirección nueva cada vez es la mejor práctica de privacidad recomendada.


**Cómo recibir Bitcoin:**

1. Abrir la moneda

2. Pulse **Recibir**

3. Elija el tipo de dirección deseado (preferiblemente **bc1q** - `Native SegWit`)

4. Mostrar el código QR o copiar la dirección y enviarla al pagador


**Opcional - Mecto (para pagos en persona):**

En la misma pantalla de recepción hay un botón `Mecto`.

Cuando lo enciendas:


- Se te pedirá que introduzcas un **nombre de usuario** (gravatar)
- Su ubicación actual + dirección de recepción se comparten temporalmente con otros usuarios Coin Wallet que también tienen Mecto habilitado
- Pueden descubrirte en un pequeño mapa y enviar monedas sin teclear ni escanear


Los datos sólo son visibles para otros usuarios de Mecto y se borran automáticamente al cabo de 1 hora (o inmediatamente al apagarlo).

Mecto es completamente opcional: déjalo desactivado si prefieres la máxima privacidad.


![image](assets/en/05.webp)


## 5️⃣ Envío de ₿itcoin


Para enviar Bitcoin:


1. Abre la moneda → pulsa **Enviar**

2. Pegue la dirección o escanee el código QR

3. Introduzca el importe (o pulse **Máx**)

4. Elija la velocidad de transacción:



| Velocidad   | Tiempo de confirmación aproximado | Nivel de tarifa     |
|---------|---------------------------|---------------|
| **Lento**    | ~120 minutos              | Más bajo
| **Predeterminado** | ~60 minutos               | Medio
| **Rápido**    | ~20 minutos               | Más alto

5. Confirme con su PIN de 4 dígitos → transacción emitida


### Cómo acelerar una transacción pendiente de ₿itcoin (RBF)


Si eliges una tarifa lenta y la transacción se bloquea:


1. Ir a la pestaña **Historia**

2. Pulse la transacción pendiente

3. Grifo **Acelerar** (Sustitución por tarifa)

4. Confirmar → la transacción se retransmitirá con una tarifa más alta


La aceleración RBF es compatible actualmente con:

Bitcoin - Avalanche - Cadena inteligente Binance - Ethereum - Ethereum Classic - Polygon


Más información sobre Replace-by-fee (RBF): https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣ Exportación de claves privadas


**¿Cuándo se necesita realmente una clave privada?

(El 99 % de los usuarios nunca lo hacen: basta con la passphrase de 12 palabras)



| Situación                                      | Por qué necesita la clave privada                     |
|------------------------------------------------|--------------------------------------------------|
| Barrido de una cartera de papel antigua                   | Mover fondos a su cartera actual             |
| Importación a un firmante de hardware (por ejemplo, Coldcard) | Para firma sin conexión                              |
| Recuperación de emergencia (semilla perdida pero aplicación aún abierta) | Para rescatar monedas antes de que desaparezca la aplicación           |
| Uso de herramientas que no aceptan frases de semilla     | Algunos utilitarios de solo observación o firma             |

### Cómo exportar claves privadas en Coin Wallet


1. Abierto **Bitcoin (BTC)**

2. Desplácese hasta la parte inferior de la página y pulse **Exportar claves privadas**

3. La aplicación muestra cada dirección con saldo + su clave privada en formato **WIF** (empieza por 5, K o L) y un código QR.


Sólo aparecen las direcciones no vacías.


**Ejemplo de clave WIF**

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**Qué hacer a continuación (recomendado)**


- Abra Electrum, Sparrow, BlueWallet o cualquier hardware wallet
- Importar/barrer clave privada
- Todos los fondos se trasladan instantáneamente a una nueva dirección segura bajo su actual seed


Nunca almacene la clave privada digitalmente en texto plano. Después de barrerla, puede eliminarse de forma segura.


Para obtener una guía completa sobre claves privadas y rutas de derivación: [How to Work with Private Keys: The Ultimate Guide](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣ Detalles técnicos - BIP39, BIP32 y vías de derivación


Coin Wallet sigue estrictamente las normas oficiales Bitcoin que utilizan casi todas las carteras serias.


`BIP39` - cómo el passphrase se convierte en la clave privada maestra


- Número de palabras por defecto: 12
- Opcional passphrase/contraseña: ninguna ("")
- Entropía inicial: 128 bits (12 palabras) → 256 bits (24 palabras)
- Aplicación de código abierto: https://github.com/paulmillr/scure-bip39
- Lista de palabras: lista de 2048 palabras en inglés estándar
- Admite la importación de frases de 12, 15, 18, 21 y 24 palabras desde cualquier otro BIP39 wallet


`BIP32 + BIP44/BIP49/BIP84` - generación determinista de todas las direcciones

A partir de una llave maestra, la wallet puede generate miles de millones de direcciones en un orden estrictamente definido. Por eso, las mismas 12 palabras introducidas en Electrum, Sparrow, Trezor, Ledger, BlueWallet, etc. mostrarán exactamente las mismas direcciones y saldos.





**Rutas de derivación utilizadas en Coin Wallet para Bitcoin**

| Tipo de dirección              | Estándar | Ruta de derivación       | Comienza con | Comentario                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| SegWit nativo (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Formato moderno, tarifas más bajas           |
| SegWit anidado (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Envoltura de compatibilidad para servicios antiguos |
| Legado (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Formato más antiguo, tarifas más altas          |

Dentro de cada camino:


- `/0` - cadena externa (direcciones que muestra para recibir pagos)
- `/1` - cadena interna (cambia las direcciones que utiliza el propio wallet)


Dado que Coin Wallet sigue estas normas públicas sin ningún cambio, sus fondos seguirán siendo recuperables en cualquier otra wallet compatible incluso dentro de 10-20-30 años.


## 8️⃣ Mejorar el anonimato con Tor


**Por qué usar Tor en Coin Wallet**

Tor oculta tu dirección IP real a los nodos, intercambios y observadores de Bitcoin.

Todo el tráfico (saldos, transacciones, intercambios) pasa a través de la red Tor - sin conexiones directas, sin fugas de IP.

Esto se implementa directamente en el código fuente de la aplicación (véase [.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)).


Coin Wallet tiene una dirección .onion oculta y, desde la v6.6.3 (diciembre de 2024), **soporte Tor integrado directamente en la aplicación móvil**.


### Cómo activar Tor en Android e iOS


1. **Instala Orbot** - aplicación oficial del Proyecto Tor (gratuita)


   - Android → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)


2. **Abre Orbot → pulsa Inicio**

Seleccione **Coin Wallet** de la lista para que sólo wallet use Tor (opcional pero recomendado)

Espere hasta que diga **"Conectado "** (10-30 segundos)


3. **Abra Coin Wallet → Ajustes → Red**

Activar **Usar Tor**


4. **Comprobar estado**

Aparece un **icono morado de cebolla Tor** en la barra superior → todo el tráfico se enruta ahora a través de Tor


![image](assets/en/06.webp)


Ya está: su Coin Wallet móvil es totalmente anónimo.


¡Disfrute de la gestión privada de criptomonedas!


## 📝 Conclusión


[Coin Wallet](https://coin.space/) - uno de los verdaderos pioneros de Bitcoin wallet con una historia de desarrollo de 10 años.

Es deliberadamente sencillo y se centra en su misión principal: almacenar de forma segura tus criptomonedas.

No hay publicidad, no hay noticias, no hay suscripciones, no hay funciones sociales, no hay distracciones - sólo un wallet limpio, rápido y autocustodiado que hace exactamente lo que se supone que debe hacer.

Coin Wallet da prioridad a la sencillez y la seguridad, siempre lo ha hecho y siempre lo hará.


## 📖 Recursos


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39