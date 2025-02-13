---
name: Melocotón
description: Guía completa para usar Peach e intercambiar bitcoins P2P
---
![cover](assets/cover.webp)

![peach](https://youtu.be/ziwhv9KqVkM)

## Introducción

Los intercambios P2P (peer-to-peer) son esenciales para preservar la confidencialidad y la autonomía financiera de los usuarios. Permiten transacciones directas entre particulares sin necesidad de verificar la identidad, lo que es crucial para quienes valoran la privacidad. Para profundizar en los conceptos teóricos, consulte el curso BTC204:

https://planb.network/courses/btc204
### 1. ¿Qué es el melocotón?

Peach es una plataforma de intercambio P2P que permite a los usuarios comprar y vender bitcoins sin KYC. Ofrece una interfaz intuitiva y funciones de seguridad avanzadas. En comparación con otras soluciones como Bisq, HodlHodl y Robosat, Peach destaca por su facilidad de uso y sus bajas comisiones.

### 2. Privacidad y recogida de datos

**¿Qué información recopila Peach?

Peach se esfuerza por almacenar el mínimo absoluto de datos sobre sus usuarios. He aquí un resumen de los datos almacenados en sus servidores:


- Un hash de su identificador único de aplicación (AdID)
- Un hash de sus datos de pago
- Tus conversaciones encriptadas
- Datos de las transacciones para garantizar que los usuarios anónimos no superan el límite de negociación (tipos de métodos de pago utilizados, importes de compra y venta)
- Direcciones utilizadas para enviar y recibir desde la cuenta de custodia
- Datos de uso (Firebase y Google Analytics), sólo con su consentimiento

Como recordatorio, un hash son datos convertidos en irreconocibles, de forma similar al cifrado. Los mismos datos siempre producirán el mismo hash, lo que permite detectar duplicados sin conocer los datos originales.

*Para más información sobre hashing, puedes seguir este curso:*

https://planb.network/courses/cyp201
**¿Quién puede ver mis datos de pago?


- Sólo su contraparte puede ver sus datos de pago
- Los datos se transmiten a través de servidores Peach, pero totalmente encriptados de extremo a extremo
- En caso de litigio, los datos de pago y el historial de conversaciones serán visibles para el mediador Peach asignado

## Instalación y configuración

### 1. Instalar la aplicación Peach

![Installation de Peach](assets/fr/01.webp)


- Descargue la aplicación desde [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/).
- Sigue las instrucciones de instalación de tu dispositivo.
- Durante la instalación, se le pedirá que elija si desea compartir ciertos datos para mejorar la aplicación Peach (imagen 1)
- En la siguiente pantalla (imagen 2), tiene dos opciones:
 - Si es un nuevo usuario, haga clic en "Nuevo usuario" para crear un nuevo perfil
 - Si ya tiene una cuenta, utilice "Restaurar" para restaurar su perfil existente
- Si tiene un código de referencia, puede introducirlo aquí.
- Para restaurar una cuenta existente (imagen 3), necesitarás :
 - Su archivo de copia de seguridad
 - La contraseña para descifrar este archivo

### 2. Vista general de las pantallas principales

La aplicación Peach está organizada en torno a cuatro pantallas principales accesibles desde la barra de navegación inferior:

![Navigation dans l'application](assets/fr/02.webp)


- Inicio** : La pantalla principal para comprar y vender bitcoins. Aquí es donde puedes crear nuevas transacciones y acceder a las ofertas disponibles.
- Monedero**: Tu monedero bitcoin integrado que te permite :
 - Compruebe su saldo
 - Recibir bitcoins
 - Enviar bitcoins
 - Consultar el historial de transacciones
- Comercios** : Su centro de gestión comercial donde encontrará :
 - Sus transacciones actuales
 - Un historial completo de sus intercambios
 - El estado de cada transacción
- Configuración** : El centro de configuración de su cuenta para :
 - Gestione sus medios de pago
 - Configura tus copias de seguridad
 - Personaliza tus preferencias
 - Acceso a ayuda y apoyo

### 3. Configure sus métodos de pago

![Accès aux paramètres de paiement](assets/fr/03.webp)

Acceda a los métodos de pago a través de la pestaña Configuración (imagen 8)

**Pagos en línea

![Configuration des paiements en ligne](assets/fr/04.webp)


- Haga clic en el botón para añadir un nuevo método de pago
- Elija su moneda
- Seleccione su forma de pago preferida

*Tipos de métodos de pago disponibles:*

***Transferencias bancarias disponibles: ***


- SEPA (estándar o instantánea)
- Introduzca sus datos bancarios SEPA

***Se aceptan monederos electrónicos :***


- Varias opciones disponibles en función de su país (Revolut, Paypal, Wise, Strike, etc.)
- Siga las instrucciones para añadir sus datos de acceso

***La tarjeta regalo que se puede utilizar :***


- Amazon
- Introduzca el país de emisión de la tarjeta y otra información necesaria

***Opciones de pago nacionales:***

Sistemas de pago específicos de cada país :


- Satispay (Italia)
- MB Way (Portugal)
- Bizum (España)
- Pagos más rápidos (Reino Unido)

***Pagos en persona:***

![Configuration des paiements en personne](assets/fr/05.webp)


- Seleccione "Meetup
- A continuación, seleccione su reunión de la lista

### Instrucciones de uso


- Puede configurar varios métodos de pago simultáneamente
- Cuantos más métodos añada, mayor será la gama de ofertas a las que tendrá acceso
- Compruebe que sus datos son correctos antes de inscribirse
- Puede cambiar o eliminar sus métodos de pago en cualquier momento

**Nota de seguridad**: Su información de pago está encriptada y sólo se comparte con su socio de intercambio durante una transacción.

### 4. Cómo asegurar su cartera

**Entender su cuenta Peach

Una cuenta Peach no es una cuenta tradicional de nombre de usuario y contraseña. Es un archivo almacenado localmente en tu teléfono, lo que significa que Peach no necesita almacenar tus datos ni conocer tu identidad: tú tienes el control. Este archivo contiene todos tus datos, desde las claves de tu monedero bitcoin hasta tus detalles de pago.

Este enfoque garantiza una mayor confidencialidad, pero también implica una mayor responsabilidad. Perder tu teléfono sin una copia de seguridad significa perder el acceso a tu cuenta Peach y a tus fondos. Así que es crucial hacer una copia de seguridad de este archivo y protegerlo con una contraseña segura.

**Crea tus copias de seguridad**

![Accéder aux sauvegardes](assets/fr/13.webp)


- Accede a los ajustes desde la pestaña situada en la parte inferior derecha de la pantalla de inicio
- Seleccione la opción "copias de seguridad" en el menú de configuración

![Processus de sauvegarde](assets/fr/06.webp)

Existen dos tipos de copias de seguridad:

**Guardar archivo de cuenta (imagen 14)**


- Haga clic en "Crear nueva copia de seguridad"
- Crea una contraseña segura para cifrar tu archivo de copia de seguridad
- Guarde este archivo en un lugar seguro

La copia de seguridad de archivos restaura toda tu cuenta de Peach, incluidos los archivos :


- Su cartera
- Sus formas de pago
- Historia de la conversación
- Datos de pago
- Historial de transacciones con datos de la contraparte

**Guardando la frase de recuperación (imagen 15)**


- Siga las instrucciones para visualizar su frase de recuperación
- Escribe cuidadosamente las palabras en el orden correcto
- Guarde esta copia de seguridad en un lugar seguro, idealmente distinto del archivo de la cuenta

La frase de recuperación sólo recupera :


- Acceso a su cuenta
- Sus fondos en bitcoin

Perderás :


- Historia de la conversación
- Datos de pago
- Información sobre la contraparte en el historial de transacciones

Para una seguridad óptima, le recomendamos que realice ambos tipos de copia de seguridad.

## Compra y venta de bitcoins

### 1. Cómo comprar Bitcoins

![Création et vue des offres](assets/fr/07.webp)


- En la pantalla de inicio, pulse el botón "Comprar" (imagen 16)
- Configura tu compra según tus preferencias (imagen 17)
- Consultar la lista de ofertas disponibles (imagen 18)

![Sélection et confirmation d'achat](assets/fr/08.webp)


- Seleccione la oferta que más le convenga (imagen 19)
- Realizar el pago mediante el método acordado
- Confirme el pago en la aplicación y evalúe la transacción (imagen 20)

![Réception des bitcoins](assets/fr/09.webp)


- Seguimiento del estado de su transacción
- Comprobar confirmación de recepción de bitcoins
- Los fondos estarán disponibles en su cartera Peach

### 2. Cómo vender Bitcoins

![Création d'un ordre de vente](assets/fr/10.webp)


- Configure su oferta de venta (imagen 24)
- Financie la transacción enviando los bitcoins a la dirección facilitada (imagen 25)
- Espere la confirmación de la transacción (imagen 26)
- Su oferta es ahora visible para los compradores (imagen 27)

![Attente du paiement](assets/fr/11.webp)


- Supervise el estado de su oferta
- Esperar la confirmación del pago por parte del comprador
- Comprobar los detalles de la transacción

![Finalisation de la vente](assets/fr/12.webp)


- Comprobar el estado del pago
- Confirmar la recepción del pago
- Evaluar la transacción
- Los bitcoins se entregan automáticamente al comprador

**Consejos para una transacción con éxito**


- Responda rápidamente a los mensajes de su contraparte
- Compruebe cuidadosamente los datos de pago
- No dude en recurrir al servicio de mediación si tiene un problema

**Nota de seguridad**: No confirme nunca la recepción de un pago hasta que haya comprobado que se ha recibido en su cuenta.

## Ventajas e inconvenientes

### Beneficios del melocotón


- No se requiere KYC**: Preserva la confidencialidad del usuario.
- Sin acceso a datos bancarios**: Peach no tiene acceso a tus datos bancarios ni a tu identidad.
- Interfaz intuitiva**: Fácil de usar para usuarios intermedios.
- Código abierto** : El código fuente es público y verificable por la comunidad.

### Desventajas del melocotón


- Liquidez limitada**: Menor volumen de negociación que plataformas más consolidadas.
- Riesgo reglamentario** : La aplicación está gestionada por una empresa suiza. Por tanto, está sujeta a la normativa suiza, que podría evolucionar y potencialmente censurar la aplicación.

## Recursos útiles


- Vídeo explicativo en francés: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Guía de inicio rápido: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)