---
name: Heritage
description: Una cartera Bitcoin con mecanismo de herencia integrado mediante guiones Taproot
---

![cover](assets/cover.webp)



La transmisión de bitcoins en caso de fallecimiento o incapacidad representa un gran reto para cualquier poseedor de criptoactivos. Sin un plan de sucesión adecuado, estos activos se convierten en irrecuperables para sus seres queridos.



Heritage ofrece una respuesta elegante implementando un mecanismo de interruptor de hombre muerto directamente en la blockchain Bitcoin. Esta wallet de código abierto permite configurar las condiciones de sucesión de la on-chain: si el propietario no realiza más transacciones durante un periodo definido, unas claves alternativas previamente designadas pueden liberar los fondos.



## ¿Qué es el patrimonio?



Heritage es una cartera Bitcoin que integra de forma nativa un mecanismo de herencia mediante scripts Taproot. Desarrollado bajo licencia MIT por Jérémie Rodon, este software de código abierto garantiza transparencia y durabilidad.



Heritage utiliza guiones Taproot codificados en direcciones Bitcoin. Cada UTXO integra dos tipos de condiciones de gasto:





- Vía primaria** : El propietario puede gastar sus bitcoins en cualquier momento con su clave primaria
- Vías alternativas**: Para cada heredero designado, un script combina su clave pública con un timelock



Cada transacción de propietario aplaza automáticamente la fecha de activación de las cláusulas sucesorias. En caso de inactividad prolongada (fallecimiento, incapacidad), las condiciones se activan automáticamente.



## Servicio de Patrimonio (opcional)



Heritage ofrece dos opciones de uso:



**Hágalo usted mismo (gratis)**: Sólo la aplicación de código abierto. Lo gestionas todo de forma autónoma con tu propio nodo. Esta opción ofrece acceso de copia de seguridad, herencia incorporada y control exclusivo de tus bitcoins. Sin embargo, tienes que crear tus propias alertas (calendario, recordatorios) para no olvidarte de renovar tus bitcoins, y no hay notificaciones automáticas para tus herederos.



**Utilizar el servicio (0,05% al año)** : El servicio btc-heritage.com añade funciones para simplificar la gestión:




- Recordatorios automáticos antes de que venzan los plazos
- Notificaciones automáticas a los herederos para guiarles en el proceso de recuperación
- Asistencia prioritaria
- Gestión simplificada de los descriptores



Comisión: 0,05% del importe gestionado al año, mínimo 0,5 mBTC/año. Primer año gratuito.



El servicio sigue siendo sin custodia: sus claves privadas nunca salen de su dispositivo. Heritage no puede acceder a tus fondos.



## Heritage CLI



Para los usuarios avanzados que prefieran el terminal, Heritage ofrece una herramienta de línea de comandos (CLI) para el control granular y el funcionamiento de la máquina con aire comprimido.



![Page Heritage CLI](assets/fr/03.webp)



La documentación completa de CLI está disponible en [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli). Aquí encontrarás instrucciones para descargar, conectarte al servicio, crear monederos (con Ledger o claves locales), gestionar herederos y transacciones.



Este tutorial se centra en la aplicación Desktop, más accesible para la mayoría de los usuarios.



## Heritage Desktop



Heritage Desktop es una aplicación gráfica con una interfaz intuitiva que guía al usuario en cada paso del proceso de configuración.



### Descargar



Vaya a [btc-heritage.com](https://btc-heritage.com) y haga clic en "Descargar aplicación".



![Page d'accueil Heritage](assets/fr/01.webp)



Elija la versión correspondiente a su sistema operativo (Linux 64bits o Windows 64bits). Los binarios no están firmados digitalmente, lo que puede provocar advertencias de seguridad.



![Page de téléchargement](assets/fr/02.webp)



### Instalación en Linux



En Linux, la aplicación se distribuye en formato AppImage. Antes de poder ejecutarla, es necesario instalar la dependencia `libfuse2`:



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



A continuación, haz que el archivo sea ejecutable y ejecútalo:



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### Primer lanzamiento



En el primer inicio, el asistente de incorporación le ofrece tres opciones:



![Onboarding initial](assets/fr/05.webp)





- Crear una Wallet con plan de patrimonio**: Crear una nueva wallet con plan de patrimonio
- Heredar bitcoins**: Recupera bitcoins como heredero
- Explorar por mí mismo**: Explorar funciones sin ayuda



Seleccione "Configurar un Wallet heredado" para crear su primer wallet.



### Conexión de red Bitcoin



Elija cómo conectarse a la red Bitcoin:



![Choix connexion](assets/fr/06.webp)





- Utilizar el Servicio de Patrimonio**: Infraestructura gestionada, más sencilla para los herederos
- Utilizar mi propio nodo**: Conéctese a su propio nodo Bitcoin Core o Electrum



Para este tutorial, vamos a utilizar nuestro propio nodo.



### Gestión de claves privadas



Seleccione cómo gestionar sus claves privadas:



![Gestion des clés](assets/fr/07.webp)





- Con un herraje Ledger** : Máxima seguridad con hardware wallet (recomendado)
- Almacenamiento local con contraseña**: Llaves almacenadas localmente con protección por contraseña
- Restauración de un wallet existente** : Restaurar desde una seed existente



### Configuración de nodos



Si utiliza su propio nodo, la aplicación le guiará a través de su configuración. Asegúrese de que su nodo Bitcoin o Electrum está :




- Instalado y en funcionamiento
- Sincronizado con la red Bitcoin
- Configurado para aceptar conexiones RPC (para Bitcoin Core)



![Configuration nœud](assets/fr/08.webp)



Haga clic en "Mi nodo Bitcoin está en marcha" cuando su nodo esté listo.



### Panel de estado



Pulse "Estado" en la esquina superior derecha y, a continuación, "Abrir configuración" para acceder a los parámetros de conexión.



![Panneau Status](assets/fr/09.webp)



Establezca la URL de su servidor Electrum (por ejemplo, `umbrel.local:50001` si utiliza Umbrel).



![Configuration Electrum](assets/fr/10.webp)



### Creación de wallet



Una vez establecida la conexión, haga clic en "Crear Wallet" en la pestaña WALLETS.



![Créer wallet](assets/fr/11.webp)



Una ventana emergente explica la arquitectura dividida de Heritage :



![Architecture split](assets/fr/12.webp)



1. **Proveedor de claves (Offline)**: Gestiona sus claves privadas y firma las transacciones. Puede ser un software Ledger o wallet.


2. **Wallet en línea**: Gestiona la sincronización con la red Bitcoin, la creación de direcciones y la difusión de transacciones.



Rellene el formulario de creación :



![Formulaire création wallet](assets/fr/13.webp)





- Nombre Wallet**: Un nombre único para identificar su wallet
- Proveedor de claves**: Elija Almacenamiento Local de Claves para este tutorial
- Nuevo/Restaurar**: Seleccione "Nuevo" para generate un nuevo seed
- Número de palabras**: 24 palabras recomendadas para máxima seguridad



Introduzca una contraseña segura y elija las opciones para Online Wallet :



![Options Online Wallet](assets/fr/14.webp)





- Nodo local**: Utiliza su propio nodo central Electrum o Bitcoin
- Servicio Heritage**: Utiliza el servicio Heritage (recomendado para las funciones de notificación)



Haga clic en "Crear Wallet" para finalizar la creación.



### Interface de wallet



Su wallet ya está creada. La interfaz muestra :



![Interface wallet](assets/fr/15.webp)





- Saldo
- Botones SEND y RECEIVE
- Historial de transacciones
- Historia de la configuración del patrimonio
- Direcciones wallet



### Crear herederos



Vaya a la pestaña "HEREDEROS" para crear sus herederos.



![Page Heirs](assets/fr/16.webp)



La ventana emergente de información lo explica:




- Los herederos son claves públicas Bitcoin asociadas a individuos
- Cada heredero tiene su propia frase mnemotécnica
- El primer heredero debe ser un "Backup" para ti (en caso de pérdida de tu wallet principal)



#### Creación del heredero de la copia de seguridad



Haz clic en "Crear heredero" y nómbralo "Copia de seguridad".



![Création héritier Backup](assets/fr/17.webp)



La ventana emergente explica por qué una frase de 12 palabras sin passphrase es segura para los herederos:


1. **Sin acceso inmediato**: Las llaves herederas no pueden acceder a los fondos hasta que haya expirado el bloqueo temporal


2. **Detección de compromiso**: Si alguien accede a la frase, puede actualizar la configuración del Patrimonio


3. **Accesibilidad a largo plazo**: Un passphrase podría caer en el olvido al cabo de muchos años



Configurar el heredero :



![Configuration héritier](assets/fr/18.webp)





- Proveedor de claves** : Almacenamiento local de claves
- Nuevo**: Generar un nuevo seed
- Número de palabras**: 12 palabras



Finalizar la creación :



![Finalisation héritier](assets/fr/19.webp)





- Tipo de heredero**: Clave pública ampliada
- Exportar a servicio**: Opcional, permite la notificación automática a los herederos



El heredero de la copia de seguridad ya está creado:



![Héritier créé](assets/fr/20.webp)



#### Guardar la frase mnemotécnica del heredero



Haga clic en el heredero de copia de seguridad y luego en "Mostrar Mnemonic" :



![Afficher mnemonic](assets/fr/21.webp)



**IMPORTANTE: Anote estas 12 palabras y guárdelas en un lugar seguro. Esta es la clave para recuperar los fondos.



![Phrase mnémotechnique](assets/fr/22.webp)



#### Eliminación de seed de la aplicación



Una vez escrita la frase, acceda a los parámetros del heredero (icono de rueda dentada):



![Paramètres héritier](assets/fr/23.webp)



Utilice "Eliminar semilla heredera" para eliminar la clave privada de la aplicación. Confirme que ha guardado la frase.



![Strip Heir Seed](assets/fr/24.webp)



Se trata de una medida de seguridad: sólo la clave pública permanece en la aplicación, suficiente para configurar la herencia.



#### Creación de un segundo heredero



Repita el proceso para crear un segundo heredero (por ejemplo, "Satoshi"). Ahora tendrás dos herederos:



![Deux héritiers](assets/fr/25.webp)





- Copia de seguridad**: Tu llave personal de emergencia
- Satoshi**: Un heredero designado



### Configuración del patrimonio



Vuelva a su wallet y haga clic en el icono Configuración:



![Paramètres wallet](assets/fr/26.webp)



En la sección "Configuración del patrimonio", haga clic en "Crear":



![Heritage Configuration](assets/fr/27.webp)



Establece límites de tiempo para cada heredero:



![Configuration délais](assets/fr/28.webp)





- Respaldo**: 180 días (6 meses) - Fecha de vencimiento: 2026-06-18
- Satoshi**: 455 días (15 meses) - Fecha de vencimiento: 2027-03-20



**Importante**: Cada heredero debe tener un retraso mayor que el anterior. El primer heredero (Backup) tendrá acceso a los fondos en primer lugar.



Configure también :



![Configuration finale](assets/fr/29.webp)





- Fecha de referencia**: Fecha de inicio del cálculo de los plazos de entrega
- Plazo mínimo de vencimiento**: Plazo mínimo tras una transacción (se recomiendan 10 días)



Haga clic en "Crear" para validar la configuración.



La configuración del Patrimonio está ahora activa:



![Configuration active](assets/fr/30.webp)



Muestra ambos herederos con sus respectivos plazos y fechas de expiración.



### Guardar descriptores



**Importante**: Guarde sus descriptores wallet. Sin ellos, incluso con la frase mnemotécnica, la recuperación de fondos es imposible.



Haga clic en "Descriptores de copia de seguridad" :



![Bouton Backup](assets/fr/31.webp)



Guarde el archivo JSON que contiene sus descriptores Bitcoin:



![Backup descripteurs](assets/fr/32.webp)



Este archivo debe transmitirse a sus herederos, junto con sus respectivas frases mnemotécnicas.



### Recibir bitcoins



Haga clic en "RECIBIR" para generate una dirección de recepción:



![Recevoir bitcoins](assets/fr/33.webp)



¡Enhorabuena! Su Heritage Wallet está listo para recibir bitcoins. Cada dirección generada incorpora automáticamente tus condiciones Heritage.



Tras recibir una transacción, se actualiza su saldo:



![Solde mis à jour](assets/fr/34.webp)



El historial muestra la transacción y la configuración de Patrimonio asociada.



---

## Recuperación por un heredero



Una vez transcurrido el plazo establecido, el heredero puede reclamar los fondos.



### Requisitos previos



El heredero necesita :


1. Su frase mnemotécnica de 12 palabras


2. El archivo de copia de seguridad del descriptor original de wallet (JSON)



### Creación de un heredero Wallet



En la pestaña "HERENCIAS", una ventana emergente le recuerda estos requisitos previos:



![Page Heir Wallets](assets/fr/35.webp)



**Por favor, tenga en cuenta**: Sin el archivo de copia de seguridad del descriptor, el acceso a los fondos es IMPOSIBLE, incluso con la frase mnemotécnica correcta.



Haga clic en "Crear heredero Wallet" :



![Créer Heir Wallet](assets/fr/36.webp)



Rellene el formulario:



![Formulaire Heir Wallet](assets/fr/37.webp)





- Nombre del heredero Wallet**: Un nombre para identificar a este heredero wallet
- Proveedor de claves** : Almacenamiento local de claves
- Restaurar**: Seleccione esta opción para introducir una frase existente



Introduzca las 12 palabras de la frase mnemotécnica del heredero y configure el Proveedor de Herencia:



![Entrée mnemonic](assets/fr/38.webp)





- Proveedor de Patrimonio**: "Local" para utilizar su propio nodo con el archivo de copia de seguridad



Cargue el archivo de copia de seguridad JSON y haga clic en "Crear heredero Wallet" :



![Chargement backup](assets/fr/39.webp)



### Interface Heredero Wallet



Se crea el heredero Wallet. Inicialmente, si el bloqueo temporal aún no ha expirado, no hay herencia disponible:



![Pas d'héritage disponible](assets/fr/40.webp)



Una vez transcurrido el plazo y sincronizados los fondos con la red Bitcoin, aparecen en la lista de herencias:



![Héritage disponible](assets/fr/41.webp)



La interfaz muestra :




- Tipo de llave y huella dactilar
- Total fondos heredables
- Importe gastable actual (0 sat si el bloqueo temporal aún no ha expirado)
- Fechas de vencimiento y expiración



Cuando llega la fecha de vencimiento, el botón "Gastar" transfiere los bitcoins a una wallet personal.



---

## Buenas prácticas



### Guardar descriptores



Los descriptores wallet son esenciales para reconstruir sus direcciones Heritage. **Sin los descriptores, incluso con su frase mnemotécnica, no podrá encontrar sus fondos.



### Seguridad de las llaves





- Utiliza una Ledger para la llave principal si es posible
- Nunca guarde las sentencias de los herederos en el mismo lugar que las suyas
- Difundir información en múltiples medios y lugares



### Documentación para sus seres queridos



Escriba instrucciones claras que expliquen cada paso del proceso de recuperación. Puede que sus herederos no estén familiarizados con Bitcoin en el momento crítico.



## Alternativas



Existen otras soluciones para gestionar la transmisión de tus bitcoins, como Liana y Bitcoin Keeper. Encontrarás nuestros tutoriales a continuación:



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Conclusión



Heritage le permite planificar su sucesión de Bitcoin de forma soberana a través de la aplicación Desktop. La puesta en práctica requiere considerar detenidamente los plazos adecuados y asegurar los secretos. No olvide transmitirlo a sus herederos:




- Su frase mnemotécnica de 12 palabras
- El archivo de copia de seguridad del descriptor
- Instrucciones de recuperación



## Recursos





- [Sitio web oficial de Heritage](https://btc-heritage.com)
- [Documentación CLI](https://btc-heritage.com/heritage-cli)
- [Herencia GitHub CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)