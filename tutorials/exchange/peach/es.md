---
name: Peach
description: Guía completa para usar Peach e intercambiar Bitcoin P2P
---
![cover](assets/cover.webp)

![peach](https://youtu.be/ziwhv9KqVkM)

## Introducción

Los intercambios P2P (peer-to-peer) son esenciales para preservar la confidencialidad y la autonomía financiera de los usuarios. Permiten transacciones directas entre particulares sin necesidad de verificar la identidad, lo que es crucial para quienes valoran la privacidad. Para profundizar en los conceptos teóricos, consulte el curso BTC204:

https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. ¿Qué es Peach?

Peach es una plataforma de intercambio P2P que permite a los usuarios comprar y vender Bitcoin sin KYC. Ofrece una interfaz intuitiva y funciones de seguridad avanzadas. En comparación con otras soluciones como Bisq, HodlHodl y Robosat, Peach destaca por su facilidad de uso y sus bajas comisiones.

### 2. Privacidad y recopilación de datos

**¿Qué información recopila Peach?**

Peach se esfuerza por almacenar el mínimo absoluto de datos sobre sus usuarios. He aquí un resumen de los datos almacenados en sus servidores:

- Un hash de su identificador único de aplicación (AdID)
- Un hash de sus datos de pago
- Tus conversaciones encriptadas
- Datos de las transacciones para garantizar que los usuarios anónimos no superan el límite de negociación (tipos de métodos de pago utilizados, importes de compra y venta)
- Direcciones utilizadas para enviar y recibir desde la cuenta de custodia
- Datos de uso (Firebase y Google Analytics), sólo con su consentimiento

Como recordatorio, un hash son datos convertidos en irreconocibles, de forma similar al cifrado. Los mismos datos siempre producirán el mismo hash, lo que permite detectar duplicados sin conocer los datos originales.

*Para más información sobre hashing, puedes seguir este curso:*

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**¿Quién puede ver mis datos de pago?**

- Sólo tu contraparte puede ver tus datos de pago
- Los datos se transmiten a través de servidores Peach, pero totalmente encriptados de extremo a extremo
- En caso de litigio, los datos de pago y el historial de conversaciones serán visibles para el mediador Peach asignado

## Instalación y configuración

### 1. Instalar la aplicación Peach

![Installation de Peach](assets/fr/01.webp)


- Descarga la aplicación desde [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/).
- Sigue las instrucciones de instalación de tu dispositivo.
- Durante la instalación, se te pedirá que elijas si deseas compartir ciertos datos para mejorar la aplicación Peach (imagen 1)
- En la siguiente pantalla (imagen 2), tienes dos opciones:
 - Si eres un nuevo usuario, haz clic en "Nuevo usuario" para crear un nuevo perfil
 - Si ya tienes una cuenta, utiliza "Restaurar" para restaurar tu perfil existente
- Si tienes un código de referencia, puedes introducirlo aquí.
- Para restaurar una cuenta existente (imagen 3), necesitarás:
 - Tu archivo de copia de seguridad
 - La contraseña para descifrar este archivo

### 2. Vista general de las pantallas principales

La aplicación Peach está organizada en torno a cuatro pantallas principales accesibles desde la barra de navegación inferior:

![Navigation dans l'application](assets/fr/02.webp)

- **Inicio**: La pantalla principal para comprar y vender Bitcoin. Aquí es donde puedes crear nuevas transacciones y acceder a las ofertas disponibles.
- **Monedero**: Tu monedero Bitcoin integrado que te permite:
 - Comprobar tu saldo
 - Recibir Bitcoin
 - Enviar Bitcoin
 - Consultar el historial de transacciones
- **Comercios**: Tu centro de gestión comercial donde encontrarás:
 - Tus transacciones actuales
 - Un historial completo de tus intercambios
 - El estado de cada transacción
- **Configuración**: El centro de configuración de tu cuenta para:
 - Gestionar tus medios de pago
 - Configurar tus copias de seguridad
 - Personalizar tus preferencias
 - Acceso a ayuda y apoyo

### 3. Configura tus métodos de pago

![Accès aux paramètres de paiement](assets/fr/03.webp)

Acceda a los métodos de pago a través de la pestaña Configuración (imagen 8)

**Pagos en línea**

![Configuration des paiements en ligne](assets/fr/04.webp)


- Haz clic en el botón para añadir un nuevo método de pago
- Elige tu moneda
- Selecciona tu forma de pago preferida

*Tipos de métodos de pago disponibles:*

***Transferencias bancarias disponibles:***

- SEPA (estándar o instantánea)
- Introduce tus datos bancarios SEPA

***Se aceptan monederos electrónicos :***

- Varias opciones disponibles en función de tu país (Revolut, Paypal, Wise, Strike, etc.)
- Sigue las instrucciones para añadir tus datos de acceso

***La tarjeta de regalo que se puede utilizar:***

- Amazon
- Introduce el país de emisión de la tarjeta y otra información necesaria

***Opciones de pago nacionales:***

Sistemas de pago específicos de cada país:

- Satispay (Italia)
- MB Way (Portugal)
- Bizum (España)
- Faster Payments (Reino Unido)

***Pagos en persona:***

![Configuration des paiements en personne](assets/fr/05.webp)

- Selecciona "Meetup"
- A continuación, selecciona tu reunión de la lista

### Instrucciones de uso

- Puedes configurar varios métodos de pago simultáneamente
- Cuantos más métodos añadas, mayor será la gama de ofertas a las que tendrás acceso
- Comprueba que tus datos son correctos antes de inscribirte
- Puedes cambiar o eliminar tus métodos de pago en cualquier momento

**Nota de seguridad**: Tu información de pago está encriptada y sólo se comparte con tu socio de intercambio durante una transacción.

### 4. Cómo asegurar tu billetera

**Entender tu cuenta Peach**

Una cuenta Peach no es una cuenta tradicional de nombre de usuario y contraseña. Es un archivo almacenado localmente en tu teléfono, lo que significa que Peach no necesita almacenar tus datos ni conocer tu identidad: tú tienes el control. Este archivo contiene todos tus datos, desde las claves de tu monedero Bitcoin hasta tus detalles de pago.

Este enfoque garantiza una mayor confidencialidad, pero también implica una mayor responsabilidad. Perder tu teléfono sin una copia de seguridad significa perder el acceso a tu cuenta Peach y a tus fondos. Así que es crucial hacer una copia de seguridad de este archivo y protegerlo con una contraseña segura.

**Crea tus copias de seguridad**

![Accéder aux sauvegardes](assets/fr/13.webp)

- Accede a los ajustes desde la pestaña situada en la parte inferior derecha de la pantalla de inicio
- Selecciona la opción "copias de seguridad" en el menú de configuración

![Processus de sauvegarde](assets/fr/06.webp)

Existen dos tipos de copias de seguridad:

**Guardar archivo de cuenta (imagen 14)**

- Haz clic en "Crear nueva copia de seguridad"
- Crea una contraseña segura para cifrar tu archivo de copia de seguridad
- Guarda este archivo en un lugar seguro

La copia de seguridad de archivos restaura toda tu cuenta de Peach, incluyendo:

- Tu cartera
- Tus formas de pago
- Historial de conversaciones
- Datos de pago
- Historial de transacciones con datos de la contraparte

**Guardando la frase de recuperación (imagen 15)**

- Sigue las instrucciones para visualizar tu frase de recuperación
- Escribe cuidadosamente las palabras en el orden correcto
- Guarda esta copia de seguridad en un lugar seguro, idealmente distinto del archivo de la cuenta

La frase de recuperación sólo recupera:

- Acceso a tu cuenta
- Tus fondos en bitcoin

Perderás:

- Historial de conversaciones
- Datos de pago
- Información sobre la contraparte en el historial de transacciones

Para una seguridad óptima, te recomendamos que realices ambos tipos de copia de seguridad.

## Compra y venta de Bitcoin

### 1. Cómo comprar Bitcoin

![Création et vue des offres](assets/fr/07.webp)


- En la pantalla de inicio, pulsa el botón "Comprar" (imagen 16)
- Configura tu compra según tus preferencias (imagen 17)
- Consulta la lista de ofertas disponibles (imagen 18)

![Sélection et confirmation d'achat](assets/fr/08.webp)


- Selecciona la oferta que más te convenga (imagen 19)
- Realiza el pago mediante el método acordado
- Confirma el pago en la aplicación y evalúa la transacción (imagen 20)

![Réception des Bitcoin](assets/fr/09.webp)


- Seguimiento del estado de tu transacción
- Comprobar confirmación de recepción de Bitcoin
- Los fondos estarán disponibles en tu cartera Peach

### 2. Cómo vender Bitcoin

![Création d'un ordre de vente](assets/fr/10.webp)


- Configure tu oferta de venta (imagen 24)
- Solventa la transacción enviando el Bitcoin a la dirección facilitada (imagen 25)
- Espera la confirmación de la transacción (imagen 26)
- Tu oferta es ahora visible para los compradores (imagen 27)

![Attente du paiement](assets/fr/11.webp)


- Supervisa el estado de tu oferta
- Espera la confirmación del pago por parte del comprador
- Comprueba los detalles de la transacción

![Finalisation de la vente](assets/fr/12.webp)


- Comprueba el estado del pago
- Confirma la recepción del pago
- Evalúa la transacción
- El Bitcoin se entrega automáticamente al comprador

**Consejos para una transacción exitosa**

- Responde rápidamente a los mensajes de tu contraparte
- Comprueba cuidadosamente los datos de pago
- No dudes en recurrir al servicio de mediación si tienes un problema

**Nota de seguridad**: No confirmes nunca la recepción de un pago hasta que hayas comprobado que se ha recibido en tu cuenta.

## Ventajas e inconvenientes

### Beneficios de Peach

- **No se requiere KYC**: Preserva la confidencialidad del usuario.
- **Sin acceso a datos bancarios**: Peach no tiene acceso a tus datos bancarios ni a tu identidad.
- **Interfaz intuitiva**: Fácil de usar para usuarios intermedios.
- **Código abierto**: El código fuente es público y verificable por la comunidad.

### Desventajas de Peach

- **Liquidez limitada**: Menor volumen de negociación que plataformas más consolidadas.
- **Riesgo reglamentario**: La aplicación está gestionada por una empresa suiza. Por tanto, está sujeta a la normativa suiza, que podría evolucionar y potencialmente censurar la aplicación.

## Recursos útiles

- Vídeo explicativo en francés: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Guía de inicio rápido: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)
