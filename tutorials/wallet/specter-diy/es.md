---
name: Specter DIY
description: Guía de instalación de Specter DIY
---

![cover](assets/cover.webp)


## Specter-DIY


> Los Cypherpunks escriben código. Sabemos que alguien tiene que escribir software para defender la privacidad, y como no podemos conseguir privacidad a menos que todos lo hagamos, vamos a escribirlo.

*Manifiesto de un Cypherpunk - Eric Hughes - 9 de marzo de 1993*


La idea del proyecto es construir un wallet de hardware a partir de componentes disponibles en el mercado.

Aunque tenemos una placa de extensión que lo pone todo en un bonito formato y te ayuda a evitar cualquier soldadura, seguiremos apoyando y manteniendo la compatibilidad con los componentes estándar.


![image](assets/fr/01.webp)


También queremos que el proyecto sea flexible, de modo que pueda funcionar con cualquier otro conjunto de componentes con cambios mínimos. Quizás quieras hacer un wallet de hardware en una arquitectura diferente (¿RISC-V?), con un módem de audio como canal de comunicación - deberías poder hacerlo. Debería ser fácil añadir o cambiar la funcionalidad de Specter e intentamos abstraer los módulos lógicos tanto como podemos.


Los códigos QR son una forma predeterminada para que Specter se comunique con el host. Los códigos QR son bastante convenientes y permiten al usuario estar en control de la transmisión de datos - cada código QR tiene una capacidad muy limitada y la comunicación ocurre unidireccionalmente. Y es airgapped - usted no necesita conectar el wallet al ordenador en cualquier momento.


Para el almacenamiento de secretos, admitimos el modo agnóstico (wallet olvida todos los secretos cuando se apaga), el modo temerario (almacena los secretos en la memoria flash del microcontrolador de la aplicación) y la integración de secure element está próxima.


Nos centramos principalmente en la configuración multifirma con otros monederos hardware, pero wallet también puede funcionar como firmante único. Intentamos hacerlo compatible con Bitcoin Core siempre que podemos - PSBT para transacciones sin firma, descriptores wallet para importar/exportar monederos multifirma. Para facilitar la comunicación con Bitcoin Core también estamos trabajando en [Specter Desktop app](https://github.com/cryptoadvance/specter-desktop) - un pequeño servidor python flask que habla con tu nodo Bitcoin Core.


La mayor parte del firmware está escrito en MicroPython, lo que hace que el código sea fácil de auditar y cambiar. Utilizamos la biblioteca [secp256k1](https://github.com/bitcoin-core/secp256k1) de Bitcoin Core para los cálculos de curvas elípticas y la biblioteca [LittlevGL](https://lvgl.io/) para la interfaz gráfica de usuario.


## Descargo de responsabilidad


El proyecto ha madurado significativamente, hasta el punto de que el nivel de seguridad de Specter-DIY es ahora comparable al de los monederos de hardware comerciales del mercado. Hemos implementado un cargador de arranque seguro que verifica las actualizaciones de firmware, por lo que puedes estar seguro de que sólo el firmware firmado se puede cargar en el dispositivo después de la configuración inicial. Sin embargo, a diferencia de los dispositivos de firma comerciales, el cargador de arranque tiene que ser instalado manualmente por el usuario y no viene configurado de fábrica por el proveedor del dispositivo. Por lo tanto, preste especial atención durante la instalación inicial del firmware y asegúrese de verificar las firmas PGP y de flashear el firmware desde un ordenador seguro.


Si algo no funciona, abre una incidencia aquí o haz una pregunta en nuestro [grupo de Telegram](https://t.me/+VEinVSYkW5TUl5Ai).


## Lista de la compra de Specter-DIY


Aquí describimos qué comprar, y en la siguiente parte del montaje explicamos cómo montarlo y algunas notas sobre la placa: puentes de alimentación, puertos USB, etc.


### Tablón de anuncios


La parte principal del dispositivo es la placa de desarrollo:



- Placa de desarrollo STM32F469I-DISCO (por ejemplo, de [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) o [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- Cable mini**USB
- Cable MicroUSB estándar para comunicación a través de USB


Opcional pero recomendado:


- [Waveshare QR code scanner](https://www.waveshare.com/barcode-scanner-module.htm) con cabezales de pines largos como [estos](https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) o [estos](https://www.amazon.com/gp/product/B015KA0RRU/) para conectar el escáner a la placa (se necesitan 4 cabezales de pines).


Actualmente estamos trabajando en una placa de ampliación que incluye una ranura para tarjetas inteligentes, un escáner de códigos QR, una batería y una carcasa impresa en 3D, pero no incluye la parte principal, la placa de detección, que hay que pedir por separado. De este modo, los ataques a la cadena de suministro no suponen un problema, ya que los componentes críticos para la seguridad se compran en una tienda de electrónica cualquiera.


Puede empezar a utilizar Specter incluso sin ningún componente adicional, pero podrá comunicarse con él a través de USB o de la ranura para tarjetas SD incorporada. El uso de Specter a través de USB significa que no es airgapped por lo que se pierde una propiedad de seguridad importante.


### Escáner QR


Para el escáner de códigos QR tiene varias opciones.


**Opción 1. Recomendado. Recomendado.** Resonablemente buen escáner de Waveshare (40$)


[Waveshare escáner](https://www.waveshare.com/barcode-scanner-module.htm) - usted tendrá que encontrar una manera de cómo montar bien, tal vez el uso de algún tipo de Arduino Prototipo escudo y algunos ducktape.


No es necesario soldar, pero si tienes conocimientos de soldadura puedes hacer que la wallet sea mucho más bonita ;)


**Opción 2.** Muy buen escáner de Mikroe pero bastante caro (150$):


[Código de barras](https://www.mikroe.com/barcode-click) + [Adaptador](https://www.mikroe.com/arduino-uno-click-shield)


**Opción 3.** Cualquier otro escáner QR


Puedes encontrar algunos escáneres baratos en China. Su calidad no suele ser muy buena, pero puedes arriesgarte. Tal vez incluso ESPcamera haría el trabajo. Sólo tienes que conectar la alimentación, UART (pines D0 y D1), y el gatillo a D5.


**Opción 4.** Sin escáner.


Entonces sólo puedes usar Specter con USB / Tarjeta SD.


A menos que construyas tu propio módulo de comunicación que utilice otra cosa en lugar de códigos QR - audiomodem, bluetooth o cualquier otra cosa. Tan pronto como se puede activar y enviar los datos a través de serie se puede hacer lo que quiera.


### Componentes opcionales


Si añades un pequeño powerbank o un cargador/reforzador de batería y alimentación, tu wallet se convierte en un dispositivo totalmente autónomo ;)



## Montaje de Specter-DIY



![video](https://youtu.be/1H7FqG_FmCw)


### Conexión del escáner de código de barras Waveshare


El firmware de wallet configurará el escáner por usted en la primera ejecución, por lo que no se requiere ninguna preconfiguración manual.


Así es como se conecta el escáner a la placa:


![image](assets/fr/02.webp)


Para mayor comodidad se puede comprar un escudo Arduino Protype y soldar y montar todo en él (es decir, [este](https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))


### Gestión de la energía


En la parte superior de la placa hay un jumper que define donde tomará la alimentación. Puedes cambiar la posición del puente y seleccionar que la fuente de alimentación sea uno de los puertos USB o el pin VIN y conectar allí una batería externa (debería ser de 5V).


### Recinto para bricolaje


Consulta la carpeta [enclosures](https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures).


### Sé creativo


Monta tu propio Specter-DIY y envíanos las fotos (haz un pull request o ponte en contacto con nosotros).


¡Echa un vistazo a la [Galería](https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md) con espectros reunidos por la comunidad!




## Instalación del código compilado


Con el cargador de arranque seguro la instalación inicial del firmware es ligeramente diferente. Las actualizaciones son más sencillas y no requieren conectar el hardware wallet al ordenador.


![video](https://youtu.be/eF4cgK_L6T4)


### Flasheo del firmware inicial


**Nota** Si no quieres usar los binarios de las versiones consulta la [documentación del gestor de arranque](https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md) que explica cómo compilarlo y configurarlo para que use tus claves públicas en lugar de las nuestras.



- Si está actualizando desde versiones inferiores a `1.4.0` o cargando el firmware por primera vez, utilice el archivo `initial_firmware_<version>.bin` de la página [releases](https://github.com/cryptoadvance/specter-diy/releases).
 - Verifique la firma del archivo `sha256.signed.txt` con la [clave PGP de Stepan](https://stepansnigirev.com/ss-specter-release.asc)
 - Verifica el hash del `initial_firmware_<version>.bin` con el hash almacenado en el `sha256.signed.txt`
- Si estás actualizando desde un gestor de arranque vacío o ves el mensaje de error del gestor de arranque que indica que el firmware no es válido, consulta la siguiente sección - Flashing signed Specter firmware.
- Asegúrese de que el puente de alimentación de su tarjeta de localización está en la posición STLK
- Conecte la tarjeta de localización al ordenador mediante el cable **miniUSB** situado en la parte superior de la tarjeta.
    - La placa debería aparecer como un disco extraíble llamado `DIS_F469NI`.
- Copie el archivo `initial_firmware_<version>.bin` en la raíz del sistema de archivos `DIS_F469NI`.
- Cuando la placa termine de flashear el firmware, se reiniciará y pasará al gestor de arranque. El bootloader comprobará el firmware y arrancará en el firmware principal. Si ves un mensaje de error que no se encuentra el firmware - sigue las instrucciones de actualización y carga el firmware a través de la tarjeta SD.
- Ahora puedes cambiar el puente de alimentación donde quieras y alimentar la placa desde el powerbank o la batería.


El flasheo del firmware inicial a través de copiar y pegar el archivo `.bin` a veces falla - a menudo debido al cable, o si se conecta el dispositivo a través de un concentrador USB. En este caso puedes intentarlo unas cuantas veces más (normalmente funciona en 2-3 intentos).


Si siempre falla, puedes utilizar la herramienta de código abierto [stlink](https://github.com/stlink-org/stlink/releases/latest). Instálela y escriba en su terminal `st-flash write <ruta/a/inicial_firmare.bin> 0x8000000`. Suele funcionar de forma mucho más fiable.


### Actualización del firmware



- Descargue el archivo `specter_upgrade_<version>.bin` de [releases](https://github.com/cryptoadvance/specter-diy/releases).
- Copie este binario en la raíz de la tarjeta SD (con formato FAT, 32 GB como máximo)
 - Asegúrese de que sólo hay un archivo `specter_upgrade***.bin` en el directorio raíz
- Inserte la tarjeta SD en la ranura SD de la placa de localización y encienda la placa
- Bootloader flasheará el firmware y te notificará cuando haya terminado.
- Reinicia la placa - ahora verás la interfaz Specter-DIY, te sugerirá que selecciones tu código PIN


Cada vez que salga una nueva versión sólo tienes que descargar el `specter_upgrade_<version>.bin` de las versiones, soltarlo en la tarjeta SD y actualizar el dispositivo como en el paso anterior. Bootloader se asegurará de que sólo firmware firmado se puede cargar en la placa.


### Cómo averiguar la versión del firmware


Ve al menú `Configuración del dispositivo` - mostrará el número de versión bajo el título de la pantalla.


## Utilice Specter-DIY wallet



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Seguridad de Specter-DIY


### Hardware


La pantalla está controlada por la MCU de la aplicación.


La integración del elemento seguro aún no ha llegado - por el momento los secretos también se almacenan en la MCU principal. Pero puedes usar el wallet sin almacenar el secreto - necesitas introducir tu frase de recuperación cada vez. ¿Por qué recordar largo passphrase si se puede recordar toda la mnemotécnica?


El dispositivo utiliza flash externa para almacenar algunos archivos (QSPI), pero todos los archivos de usuario son firmados por el wallet y comprobados cuando se cargan.


La funcionalidad de escaneo QR está en un microcontrolador separado, por lo que todo el procesamiento de imágenes ocurre fuera de la MCU de seguridad crítica. Por el momento, el USB y la tarjeta SD siguen siendo gestionados por la MCU principal, así que no utilices la tarjeta SD y el USB si quieres reducir la superficie de ataque.


### Protección mediante PIN (autenticación de usuarios)


Durante el primer arranque se genera un secreto único en la MCU principal. Este secreto permite verificar que el dispositivo no ha sido sustituido por uno malicioso - al introducir el código PIN aparece una lista de palabras que permanecerán iguales mientras esté el secreto.


Su código PIN junto con este secreto único se utilizan para generate una clave de descifrado para sus claves Bitcoin (si las almacena). Así que si el atacante sería capaz de eludir la pantalla de PIN, el descifrado seguirá fallando.


Si has bloqueado el firmware (TODO: añade el link de las instrucciones aquí) esto bloqueará efectivamente el secreto también, así que si el atacante flashea un firmware diferente a la placa el secreto se borra y serás capaz de reconocerlo cuando empieces a introducir el código PIN - la secuencia de palabras será diferente.


### Generación de la frase de recuperación


Esta es una de las partes más importantes de la wallet - para generate la clave de forma segura. Para hacerlo bien utilizamos múltiples fuentes de entropía:



- TRNG del microcontrolador. Propietario, certificado y probablemente bueno pero no confiamos en él
- Pantalla táctil. Cada vez que tocas la pantalla medimos la posición y el momento en que se ha producido ese toque (en ticks del microcontrolador a 180MHz).
- Micrófonos incorporados - todavía no. La placa tiene dos micrófonos, por lo que el hardware wallet puede escucharte y mezclar estos datos al fondo de entropía.


Toda esta entropía se combina y se convierte en tu frase de recuperación. La entropía resultante es siempre mejor que cualquiera de las fuentes individuales.


### Lógica de alto nivel - monederos


Specter funciona como un almacén de claves. Contiene claves privadas HD que pueden estar involucradas en carteras. Los monederos se definen por sus descriptores. También soportamos miniscriptores.


Cada wallet pertenece a una red determinada. Esto significa que si ha importado un wallet en `testnet`, no estará disponible en `mainnet` o `regtest`: tendrá que cambiar a esta red e importar el wallet por separado.


### Verificación de transacciones


Las siguientes normas se aplican a las transacciones que firmará wallet:



- si se encuentran entradas mezcladas de distintos monederos se avisa al usuario ([ataque](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- las salidas de cambio muestran el nombre del wallet al que se envían
- para utilizar un multisig o un minisig primero hay que importar el wallet añadiendo el descriptor wallet (a través de QR, USB o tarjeta SD)


## Apoyo a los descriptores


Todos los descriptores normales de Bitcoin funcionan. Aparte de eso tenemos algunas extensiones:


### Varias ramas en los descriptores


Para ahorrar algo de espacio en los códigos QR permitimos añadir descriptores con múltiples ramas de una sola vez. Si desea utilizar `wpkh(xpub/0/*)` para direcciones de recepción y `wpkh(xpub/1/*)` para direcciones de cambio, puede combinarlos en un único descriptor: `wpkh(xpub/{0,1}/*)` - el wallet tratará el primer índice de la parte del conjunto `{}` como la rama para direcciones de recepción y la segunda como direcciones de cambio.


También se pueden especificar más de dos ramas, y los índices de rama pueden ser diferentes para distintos cosignatarios, por lo que este descriptor es muy raro pero totalmente válido:


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


Aquí, para recibir la dirección número 17, wallet utilizará el script de `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))`.


El único requisito es que el número de índices de todos los conjuntos sea el mismo (3 en el caso anterior).


### Derivaciones por defecto


Si el descriptor contiene claves públicas maestras pero no contiene derivaciones comodín, se añadirá la derivación por defecto `/{0,1}/*` a todas las claves extendidas del descriptor. Si al menos uno de los xpubs tiene una derivación comodín, el descriptor no se modificará.


El descriptor `wpkh(xpub)` se convertirá en `wpkh(xpub/{0,1}/*)`.


### Miniscript


Specter admite miniscript, pero no admite la compilación de política a miniscript (porque es demasiado costosa). Realizamos algunas comprobaciones en el miniscipt, de modo que sólo se permiten scripts `B` en el nivel superior y todos los argumentos de los subminiscripts tienen que tener propiedades de acuerdo con las [spec](http://bitcoin.sipa.be/miniscript/).


Puede utilizar [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) para generate un descriptor de una política y luego importarlo a la wallet.


Por ejemplo, una política "puedo gastar ahora, o dentro de 100 días puede gastar mi mujer" puede convertirse en wallet de la siguiente manera:


Política: `o(9@pk(xpubA),and(older(14400),pk(B)))` (mi clave es 9 veces más probable)


Miniscript: `or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400)))`


Descriptor: `wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400))))`


Como aquí no tenemos ninguna derivación comodín las derivaciones por defecto de `/{0,1}/*` se añadirán a los xpubs.



---

Licencia MIT


Copyright (c) 2019 cryptoadvance


---