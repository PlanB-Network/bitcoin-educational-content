---
name: Seed Signer

description: Configuración de tu Seed signer
---

![cover](assets/cover.jpeg)

# Seed signer

## Material:

1. Raspberry Pi Zéro (versión 1.3)

Raspberry Pi Zero

Para una solución completamente aislada, asegúrate de usar la versión 1.3 sin capacidad de WiFi o Bluetooth, pero cualquier modelo de Raspberry Pi 2/3/4 o Zero funcionará.

Nota: Las Raspberry Pi generalmente no vienen con pines adjuntos; los pines deberán soldarse o se puede utilizar algo llamado "GPIO Hammer".
GPIO Hammer

Si no eres muy bueno soldando o simplemente no tienes una soldadora, puedes usar "GPIO Hammer" como alternativa a la soldadura.

2. Chapeau LCD WaveShare 1,3 pulgadas con pantalla de 240 × 240 píxeles

WaveShare LCD Hat

Waveshare 1.3″ 240×240 pxl LCD

Nota: Elige cuidadosamente la pantalla de Waveshare; asegúrate de comprar el modelo que tenga una resolución de 240×240 píxeles.
más información

3. Módulo de cámara compatible con Pi Zero

Cámara Raspberry Pi

Aokin / AuviPal 5MP 1080p con módulo de cámara de sensor OV5647; otras marcas con el módulo de sensor OV5647 también deberían funcionar, pero es posible que no sean compatibles con la carcasa Orange Pill.

Nota: Necesitarás un cable de cámara específicamente compatible con Raspberry Pi Zero.

4. Tarjeta MicroSD con al menos 4 GB de capacidad

Recursos adicionales: https://seedsigner.com/explainers/

## Software:

Instalación de software

1. Descarga el último archivo "seedsigner_x_x_x.img.zip"
   última versión

2. Descomprime el archivo "seedsigner_x_x_x.img.zip"

3. Utiliza Balena Etcher u otra herramienta similar para escribir el archivo de imagen .img descomprimido en una tarjeta microSD
   BALENA ETCHER

4. Instala la tarjeta microSD en SeedSigner.
   Clave pública GPG de SeedSigner
   seedsigner_pubkey.gpg

## Tutorial en video

_Guía tomada de Southerbitcoiner, creada por Cole_

### Una colección de guías en video sobre SeedSigner: una billetera de hardware de código abierto y de bricolaje

![image](assets/1.jpeg)

SeedSigner es un dispositivo de firma de Bitcoin que puedes construir desde cero. Suena difícil, pero esta serie de 4 partes debería ayudarte : Te sugiero que veas la parte 1 y 2, luego decidas si quieres usar una computadora de escritorio (mira la parte 3) o un dispositivo móvil (mira la parte 4).

Todo lo que necesitas saber estará a continuación. Otros enlaces útiles incluyen el sitio web de SeedSigner, su Github, su Keybase, la última versión y los requisitos de hardware.

### Parte 1: Cómo construir un SeedSigner:

En este video te muestro cómo descargar y verificar el software de SeedSigner, qué partes se necesitan y cómo ensamblar tu SeedSigner.

![video](https://youtu.be/mGmNKYOXtxY)

### Parte 2: Probando tu SeedSigner

Antes de usar mi SeedSigner, hice algunas pruebas para asegurarme de que no estuviera haciendo nada malicioso. Pensé que también compartiría este paso. Aquí está cómo verificar que tu SeedSigner exporta la billetera correcta (xpub), cómo verificar las tiradas de dados matemáticas de SeedSigner y cómo verificar las semillas hijas bip-85 de SeedSigner.

### Parte 3: Cómo usar SeedSigner con Sparrow Wallet (escritorio)

SeedSigner es capaz de generar semillas y firmar transacciones de bitcoin. Pero por sí solo, no es capaz de construir transacciones. Necesitas usar un "coordinador" de billetera con tu SeedSigner. Así es cómo usar Sparrow Wallet con tu SeedSigner:

![video](https://youtu.be/IQb8dh-VTOg)

### Parte 4: Cómo usar SeedSigner con Blue Wallet (móvil)

SeedSigner es capaz de generar semillas y firmar transacciones de bitcoin. Pero por sí solo, no es capaz de crear transacciones. Necesitas usar un "coordinador" de billetera con tu SeedSigner. Así es cómo usar Blue Wallet con tu SeedSigner:

¡Esos son todos los guías de SeedSigner, por ahora! Avísame si crees que me falta algo. Estos están en mi lista para posibles videos:

![video](https://youtu.be/x0Ee35Ct0r4)

> Reseña general de SeedSigner. ¿Es una buena opción como dispositivo de firma? Pros/contras?

> Cómo usar Bip-85 con SeedSigner
> Cómo ser tío Jim con SeedSigner

¿Te han resultado útiles? Considera enviar una propina para ayudar a financiar futuros videos:

https://www.southernbitcoiner.com/donate/
