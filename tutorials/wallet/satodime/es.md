---
name: Satodime
description: Descubra cómo utilizar el Satodime con la aplicación móvil
---
![cover](assets/cover.webp)



Esta guía te lleva a través de la instalación, configuración y uso de la aplicación móvil Satodime. Aprenderá a tomar posesión de su tarjeta, crear cajas fuertes, añadir fondos, desprecintar y recuperar sus claves privadas. Los apéndices ofrecen recursos, buenas prácticas y explicaciones técnicas.



## Introducción



**Satodime**, desarrollado por **[Satochip](https://satochip.io/fr/)**, es una tarjeta portadora segura para almacenar Bitcoin de forma tangible y sencilla. Actúa como una Hardware Wallet autocustodiada, donde tienes control total sobre tus claves privadas sin depender de terceros. De código abierto y con certificación EAL6+, admite hasta tres cajas fuertes independientes.



### Antecedentes del producto



Satodime, una **carte au porteur, pertenece a quien la posea físicamente**, sin necesidad de registro o identificación previa. Responde a la necesidad de almacenamiento seguro y portátil Bitcoin, permitiendo a cualquiera que posea la tarjeta utilizarla o transferir bitcoins escaneándola a través de la aplicación móvil para tomar posesión o desprecintar cajas fuertes. A diferencia de un billete de papel, utiliza un chip seguro para Seal las claves privadas, que se revelan sólo después de desprecintar, lo que hace que la tarjeta sea similar al dinero en efectivo, donde Ownership se determina por la posesión física. Ideal para regalar bitcoins, facilita la transferencia segura de bitcoins de mano en mano, mientras que la aplicación móvil aprovecha la NFC para una interacción accesible con el smartphone.





- Seguridad**: Claves privadas generadas y almacenadas en el chip a prueba de manipulaciones; estado visible (sellado, sin sellar, vacío).
- Características**: Compra bitcoins directamente a través de la app (socio de Paybis); gestiona Mainnet y Testnet.
- Código abierto**: Código bajo licencia AGPLv3, verificable en GitHub.



### Evolución continua



La aplicación evoluciona regularmente. Consulte el sitio web de Satochip o las tiendas para ver las actualizaciones. Por ejemplo, pueden añadirse nuevas blockchains o funcionalidades de compra. Consulta el [Satochip GitHub](https://github.com/Toporin/Satodime-Applet) para ver los desarrollos en curso.



## 1. Requisitos previos



Antes de empezar a utilizar **Satodime**, asegúrese de que dispone de los siguientes elementos:





- Smartphone compatible**: Dispositivo Android o iOS con NFC activado.
- Tarjeta Satodime**: Nueva o no inicializada.
- Conexión a Internet**: Para descargar la aplicación.
- Conocimientos básicos**: Comprensión de las claves privadas/públicas y los riesgos de pérdida (irreversibles).
- Soporte seguro**: Un lugar seguro para grabar las claves privadas una vez desprecintadas (papel, metal; nunca digital).



## 2. Instalación





- Descargar la solicitud** :
 - [App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Google Play Store](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - Compruebe el promotor (Satochip) para evitar fraudes.
 - Satodime es **de código abierto**. Código fuente : [GitHub de Satochip](https://github.com/Toporin/Satodime-Applet).





- Instala e inicia la aplicación**: Activa NFC en tu teléfono si es necesario.



![image](assets/fr/01.webp)



## 3. Configuración inicial



### 3.1 Inicie la aplicación y escanee



Abre la aplicación y sigue el asistente. Coloca la tarjeta Satodime en el lector NFC de tu teléfono (normalmente en la parte trasera). Mantenla pulsada durante toda la operación para garantizar una conexión estable.





- Si NFC no funciona, comprueba la configuración de tu teléfono.
- Un brindis confirma el éxito: "Lectura con éxito".



![image](assets/fr/02.webp)



Por regla general, **todas las operaciones siguientes requerirán la confirmación por escáner de la tarjeta Satodime**



### 3.2 Toma de posesión de la tarjeta (*Ownership*)



Para el primer uso, conviértete en el propietario de la tarjeta para asegurarla:





- Haz clic en "*Take Ownership*" en la aplicación.
- Confirme la operación: se genera una clave de propietario única.
- Vuelve a escanear el mapa para aplicar los cambios.
- Advertencia**: Este paso es irreversible. Consulte [el artículo *Ownership*](https://satochip.io/satodime-Ownership-explained/).



![image](assets/fr/03.webp)




## 4. Crear una caja fuerte



Satodime admite hasta 3 cajas fuertes. Crea una para almacenar Bitcoin :





- Seleccione una caja fuerte vacía (por ejemplo, Caja fuerte 01).
- Elija Blockchain (Bitcoin).
- Haz clic en "*Crear & Seal*".
- Escanea la tarjeta a generate y Seal la clave privada (desconocida hasta que se desprecinte).
- Enhorabuena: Su caja fuerte ya está sellada y lista para recibir fondos.



![image](assets/fr/04.webp)



![image](assets/fr/05.webp)



## 5. Añadir fondos



Una vez sellada, carga la caja fuerte con bitcoins:





- Selecciona la caja fuerte.
- Haga clic en "*Añadir fondos*".
- Copie el Address público o escanee el código QR.
- Enviar fondos desde otro Wallet.
- Compruebe el saldo después de la confirmación en la Blockchain.
- Opción de compra: Haga clic en "*Comprar*" para comprar directamente a través de Paybis (Visa, Mastercard, etc.). Tasas aplicables.



![image](assets/fr/06.webp)



## 6. Desprecintar una caja fuerte



Para acceder a la clave privada y transferir los fondos a otro lugar, desprecinte la caja fuerte:





- Seleccione la caja fuerte sellada.
- Haga clic en "Desprecintar".
- Confirme la advertencia: esta operación es irreversible.
- Escanee la tarjeta para desprecintarla.
- La caja fuerte está configurada como "*Sin sellar*"; ahora se puede ver/exportar la clave privada.
- Advertencia**: Una vez desprecintada, la clave privada es accesible. Si alguien se apodera de tu smartphone, puede acceder a esta clave y recuperar así los fondos de tu caja fuerte (irreversible).



![image](assets/fr/07.webp)



## 7. Recuperar la clave privada



Una vez desprecintada, exporte la llave para utilizarla en otra Wallet :





- Asegúrate de que estás en un entorno seguro.
- Haz clic en "*Mostrar clave privada*".
- Elige el formato: Legacy, SegWit, WIF, etc.
- Copia la clave o escanea el código QR.
- Seguridad**: Nunca compartas tu clave privada. Almacénala sin conexión.
- Importarlo a un programa informático Wallet compatible con la gestión de fondos (por ejemplo, Sparrow wallet o Electrum).



![image](assets/fr/08.webp)





## 8. Restablecer maletero



Al restablecer la caja fuerte se borra irreversiblemente la clave privada asociada. En otras palabras, si no has asegurado una copia de tu clave privada, o la has importado a otro Wallet, reiniciar la caja fuerte provocará la pérdida irreversible de los fondos que contenga.



![image](assets/fr/09.webp)



Al restablecer el baúl, la ranura queda vacía y lista para un nuevo baúl.



## 9. Transferencia Ownership



Para, por ejemplo, ofrecer bitcoins a través de Satodime, debe :




- Toma Ownership de la tarjeta,
- Crea una caja fuerte Bitcoin,
- Traslade a Satss allí,
- Transferir tarjeta Ownership: la siguiente persona que escanee la tarjeta se convierte en su propietario,
- Entrega la tarjeta Satodime a la persona que elijas e invítala a descargar la aplicación y a escanear la tarjeta para tomar Ownership de ella, y acceder así a los bitcoins "almacenados" en ella.



![image](assets/fr/10.webp)




## ANEXOS



### A1. Buenas prácticas



Para utilizar **Satodime** de forma segura :





- Asegure la tarjeta**: Trátela como dinero en efectivo; pérdida = fondos perdidos si no es el propietario.
- Copia de seguridad de las claves**: Tras desprecintar, grabar las claves privadas en un soporte físico seguro. Nunca digital.
- Comprobar estado**: Escanea siempre para confirmar la tarjeta Ownership y el estado sellado/no sellado de las cajas fuertes.
- Confidencialidad**: Utilizar direcciones nuevas; evitar los intercambios centralizados para las transferencias.
- Actualizaciones**: Mantén la app actualizada a través de las tiendas.
- Recuperación**: Si se pierde la tarjeta pero se tiene, los fondos están en la Blockchain; utilice la clave privada si no está sellada.



### A2. Recursos adicionales



Específico para Satodime :




- [producto Satodime](https://satochip.io/fr/product/satodime/)
- [Guía móvil](https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)



[Plan ₿ Network](https://planb.network/) para tutoriales sobre autocustodia, claves privadas, etc.



**Guarda tu frase de recuperación** :



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Tutorial sobre el Satochip (primer producto de la marca) :**



https://planb.network/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**Tutoriales para sembradores:**



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3. Acerca de Satochip



**Enlaces oficiales** :




- [Sitio Satochip](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- Soporte: info@satochip.io



**Satochip** es una empresa belga que desarrolla soluciones de hardware y software para gestionar y almacenar bitcoins y otras criptomonedas. Su producto estrella, la Satochip Hardware Wallet, es una tarjeta NFC equipada con una secure element con certificación EAL6+. Complementada por la Seedkeeper, un gestor de frases y secretos Mnemonic, y la Satodime, una tarjeta al portador, Satochip ofrece una gama completa adaptada a las necesidades de los usuarios. Sus dispositivos, basados en software de código abierto, pretenden democratizar la seguridad en la Bitcoin.