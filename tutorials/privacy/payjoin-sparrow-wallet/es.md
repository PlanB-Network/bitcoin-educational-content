---
name: Payjoin - Sparrow Wallet
description: ¿Cómo hacer una transacción Payjoin en Sparrow Wallet?
---
![imagen de portada del tutorial de sparrow payjoin](assets/cover.webp)

_**ATENCIÓN:** Tras el arresto de los fundadores de Samourai Wallet y la incautación de sus servidores el pasado 24 de abril, los Payjoins Stowaway en Samourai Wallet ahora solo funcionan intercambiando manualmente los PSBT entre las partes involucradas, siempre que ambos usuarios estén conectados a su propio Dojo. En cuanto a Sparrow, los Payjoins a través de BIP78 todavía funcionan. Sin embargo, es posible que estas herramientas se reinicien en las próximas semanas. Mientras tanto, siempre puede leer este artículo para comprender el funcionamiento teórico de los payjoins._

_Estamos siguiendo de cerca la evolución de este caso así como los desarrollos relacionados con las herramientas asociadas. Ten la seguridad de que actualizaremos este tutorial a medida que estén disponibles nuevas informaciones._

_Este tutorial se proporciona únicamente con fines educativos e informativos. No respaldamos ni alentamos el uso de estas herramientas para fines criminales. Es responsabilidad de cada usuario cumplir con las leyes en su jurisdicción._

---

> *"Obliga a los espías de la cadena de bloques a replantearse todo lo que creen saber."*

Payjoin es una estructura específica de transacción de Bitcoin que mejora la privacidad del usuario durante el gasto al colaborar con el receptor del pago. Existen varias implementaciones que facilitan la configuración y automatización de PayJoin. Entre estas implementaciones, la más conocida es Stowaway desarrollada por el equipo de Samourai Wallet. Este tutorial tiene como objetivo guiarte a través del proceso de realizar una transacción Payjoin de Stowaway utilizando el software Sparrow Wallet.

## ¿Cómo funciona Stowaway?

Como se mencionó anteriormente, Samourai Wallet ofrece una herramienta PayJoin llamada "Stowaway". Es accesible a través del software Sparrow Wallet en PC o la aplicación Samourai Wallet en Android. Para realizar un Payjoin, el receptor, que también actúa como colaborador, debe utilizar un software compatible con Stowaway, es decir, Sparrow o Samourai Wallet. Estos dos software son interoperables, lo que permite transacciones Stowaway entre una billetera Sparrow y una billetera Samourai, y viceversa.

Stowaway se basa en una categoría de transacciones que Samourai se refiere como "Cahoots" (complicidad). Un Cahoots es esencialmente una transacción colaborativa entre múltiples usuarios que requiere un intercambio de información fuera de la cadena. Actualmente, Samourai ofrece dos herramientas Cahoots: Stowaway (Payjoins) y StonewallX2 (que exploraremos en un artículo futuro).

Las transacciones Cahoots implican el intercambio de transacciones parcialmente firmadas entre los usuarios. Este proceso puede ser largo y engorroso, especialmente cuando se realiza de forma remota. Sin embargo, aún se puede hacer manualmente con otro usuario, lo cual puede ser conveniente si los colaboradores están físicamente cerca. En la práctica, esto implica intercambiar manualmente cinco códigos QR que se escanean sucesivamente.

Cuando se realiza de forma remota, este proceso se vuelve demasiado complejo. Para abordar este problema, Samourai ha desarrollado un protocolo de comunicación cifrada basado en Tor, llamado "Soroban". Con Soroban, los intercambios necesarios para un Payjoin se automatizan detrás de una interfaz fácil de usar. Este es el segundo método que exploraremos en este artículo.

Estos intercambios cifrados requieren establecer una conexión y autenticación entre los participantes de Cahoots. Las comunicaciones de Soroban se basan en los Paynyms de los usuarios. Si no estás familiarizado con los Paynyms, te invito a consultar este artículo para obtener más detalles: [BIP47 - PAYNYM](https://planb.network/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093)
En resumen, un Paynym es un identificador único vinculado a tu billetera que permite diversas funcionalidades, incluido el envío de mensajes cifrados. El Paynym se presenta en forma de un identificador y una ilustración que representa a un robot. Aquí tienes un ejemplo del mío en Testnet: ![Paynym Sparrow](assets/es/1.webp)

**En resumen:**
- *Payjoin* = Estructura específica de transacción colaborativa;
- *Stowaway* = Implementación de Payjoin disponible en Samourai y Sparrow Wallet;
- *Cahoots* = Nombre dado por Samourai a todos sus tipos de transacciones colaborativas, incluido Payjoin Stowaway;
- *Soroban* = Protocolo de comunicación cifrada establecido en Tor, que permite la colaboración con otros usuarios en el contexto de una transacción Cahoots.
- *Paynym* = Identificador único de una billetera que permite la comunicación con otro usuario en Soroban, con el fin de realizar una transacción Cahoots.

[**-> Descubre más sobre las transacciones Payjoin y su utilidad**](https://planb.network/tutorials/privacy/on-chain/payjoin-848b6a23-deb2-4c5f-a27e-93e2f842140f)

## ¿Cómo establecer una conexión entre Paynyms?
Para realizar una transacción remota de Cahoots, específicamente un PayJoin (Stowaway) a través de Samourai o Sparrow, es necesario "Seguir" al usuario con el que deseas colaborar, utilizando su Paynym. En el caso de un Stowaway, esto significa seguir a la persona a la que deseas enviar bitcoins.
**Aquí está el procedimiento para establecer esta conexión:**

Primero, necesitas obtener el identificador Paynym del destinatario. Esto se puede hacer utilizando su apodo o código de pago. Para hacer esto, desde la billetera Sparrow del destinatario, selecciona la pestaña `Herramientas`, luego haz clic en `Mostrar PayNym`.
![Mostrar Paynym](assets/notext/2.webp)
![Paynym Sparrow](assets/es/1.webp)
En tu lado, abre tu billetera Sparrow y accede al mismo menú `Mostrar PayNym`. Si estás utilizando tu Paynym por primera vez, necesitarás obtener un identificador haciendo clic en `Recuperar PayNym`.
![Recuperar paynym](assets/notext/3.webp)
A continuación, ingresa el identificador Paynym de tu colaborador (ya sea su apodo `+...` o su código de pago `PM...`) en el cuadro `Buscar contacto`, luego haz clic en el botón `Agregar contacto`.
![Agregar contacto](assets/notext/4.webp)
El software te ofrecerá un botón `Enlazar contacto`. No es necesario hacer clic en este botón para nuestro tutorial. Este paso solo es necesario si planeas hacer pagos al Paynym indicado en el contexto de BIP47, que no está relacionado con nuestro tutorial.

Una vez que el Paynym del destinatario es seguido por tu Paynym, repite esta operación en la dirección opuesta para que tu destinatario también te siga. Luego puedes realizar un Payjoin.

## ¿Cómo realizar un Payjoin en Sparrow Wallet?
Si has completado estos pocos pasos preliminares, ¡finalmente estás listo para realizar la transacción de Payjoin! Para hacer esto, sigue nuestro tutorial en video:
![Tutorial de Payjoin - Sparrow Wallet](https://youtu.be/ZQxKod3e0Mg)

**Recursos externos:**
- https://docs.samourai.io/en/spend-tools#stowaway ;
- https://sparrowwallet.com/docs/spending-privately.html.
