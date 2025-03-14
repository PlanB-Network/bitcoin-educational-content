---
name: Sellado de tiempo de certificados y diplomas en Plan ₿ Network
description: Comprende cómo Plan ₿ Network emite pruebas verificables para tu certificado y diplomas
---

![cover](assets/cover.webp)

Si estás leyendo esto, hay una alta probabilidad de que hayas recibido un Certificado Bitcoin o un diploma de finalización por alguno de los cursos que realizaste en Plan ₿ Network, ¡así que felicitaciones por este logro!

En este tutorial, vamos a ver cómo Plan ₿ Network emite pruebas verificables para tu Certificado Bitcoin o cualquier Diploma de Finalización de Curso. Luego, en una segunda parte, veremos cómo verificar la autenticidad de estas pruebas.

# Mecanismo de prueba de Plan ₿ Network

En Plan ₿ Network, te ofrecemos un certificado y diplomas que están firmados criptográficamente por nosotros y sellados en tiempo en la Timechain (es decir, la blockchain de Bitcoin). Para lograr esto, tuvimos que idear un mecanismo de prueba que se basa en 2 operaciones criptográficas:

1. Una firma GPG en un archivo de texto que sintetiza tus logros
2. El sellado de tiempo de este archivo firmado a través de [opentimestamps](https://opentimestamps.org/).

Básicamente, la primera operación te permite verificar quién emite el certificado (o diploma) mientras que la segunda te permite verificar cuándo fue emitido.
Creemos que este sencillo mecanismo de prueba nos permite emitir certificados y diplomas con pruebas indiscutibles que cualquiera puede verificar por sí mismo.

![image](./assets/proof-mechanism.webp)

Nota que gracias a este mecanismo de prueba, cualquier intento de alterar incluso el más mínimo detalle de tu certificado o diploma creará un hash sha256 completamente diferente del archivo firmado, lo que revelaría instantáneamente la manipulación porque la firma y el sellado de tiempo ya no serían válidos. Además, si alguien intenta falsificar maliciosamente algunos certificados o diplomas en nombre de Plan ₿ Network, una simple verificación de la firma revelaría el fraude.

## ¿Cómo funciona la firma GPG?

La firma GPG se obtiene con el uso de un software de código abierto llamado GNU Private Guard. Este software permite a cualquiera crear fácilmente claves privadas, firmar y verificar firmas, y también cifrar y descifrar archivos. Para el alcance de este tutorial, ten en cuenta que Plan ₿ Network utiliza GPG para crear su clave privada/pública y para firmar cualquier Certificado Bitcoin o Diploma de Finalización de Curso.

Por otro lado, si alguien quiere verificar la autenticidad de un archivo firmado, puede usar GPG para importar la clave pública del emisor y verificar. En la segunda parte del tutorial veremos cómo hacerlo con un terminal.

Para aquellos que tienen curiosidad y quieren aprender más sobre este fantástico software, pueden referirse a ["The GNU Privacy Handbook"](https://www.gnupg.org/gph/en/manual/x135.html)

## ¿Cómo funciona el sellado de tiempo?

Cualquiera puede usar OpenTimestamps para sellar un archivo en tiempo, y obtener una prueba verificable de la existencia del archivo. En otras palabras, no te proporciona una prueba de cuándo se creó el archivo, sino una prueba de existencia no más tarde de un cierto momento.
OpenTimestamps es capaz de ofrecer este servicio de forma gratuita gracias a una manera altamente eficiente de almacenar dicha prueba en la Blockchain de Bitcoin. Utiliza el hash sha256 del archivo como un identificador único de tu archivo y construye un árbol de Merkle con otros hashes de archivos enviados por otros usuarios y solo ancla el hash de la estructura del Árbol de Merkle en una Transacción OpReturn.
Una vez que esta transacción esté en algún bloque, cualquiera con el archivo inicial y el archivo `.ots` asociado a él puede verificar la autenticidad del sellado de tiempo. En la segunda parte del tutorial veremos cómo verificar tu Certificado de Bitcoin o cualquier Diploma de Finalización de Curso con un terminal y con una interfaz gráfica a través del sitio web de OpenTimestamps.

# Cómo verificar un Certificado de Plan ₿ Network o Diploma

## Paso 1. Descarga tu Certificado o Diploma

Inicia sesión en tu panel de control personal de PBN.

![image](./assets/login.webp)

Ve a la página de Credenciales haciendo clic en el menú del lado izquierdo, y selecciona tu sesión de examen o tu Diploma de Finalización de Curso.

![image](./assets/credential.webp)

Descarga el archivo zip.

![image](./assets/download.webp)

Extrae el contenido haciendo clic derecho en el archivo `.zip` y seleccionando "Extraer". Encontrarás tres archivos diferentes dentro:

- Archivo de texto firmado (por ejemplo, certificate.txt)
- Archivo de Open Timestamp (OTS) (por ejemplo, certificate.txt.ots)
- Certificado en PDF (por ejemplo, certificate.pdf)

## Paso 2: Verificando la Firma del Archivo de Texto

Primero abre un terminal en la carpeta donde están los archivos (haciendo clic derecho en la ventana de la carpeta y clic en "Abrir en Terminal"). Luego sigue las instrucciones a continuación

1. Importa la clave pública PGP de Plan ₿ Network con el siguiente comando:

```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/planb-network-pk.asc | gpg --import
```

Deberías ver un mensaje como el siguiente si importaste la clave PGP con éxito

```
gpg: key 8F12D0C63B1A606E: public key "PlanB Network (used for PBN platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```

NOTA: si ves que 1 clave es procesada y 0 importada, lo más probable es que ya hayas importado la misma clave previamente y está bien.

2. Verifica la firma del certificado o diploma con el siguiente comando:

```bash
gpg --verify certificate.txt
```

Este comando debería mostrarte detalles sobre la firma, incluyendo:

- Quién lo firmó (Plan ₿ Network)
- Cuándo fue firmado
- Si la firma es válida

Este es un ejemplo del resultado:

```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "PlanB Network (used for PBN platform) <admin@planb.network>" [unknown]
```

Si ves un mensaje como "BAD signature", eso significa que el archivo ha sido alterado.

## Paso 3: Verificando el Open Timestamp

### Verificación a través de una Interfaz Gráfica

1. Visita el sitio web de OpenTimestamps: https://opentimestamps.org/
2. Haz clic en la pestaña "Stamp & Verify".
3. Arrastra y suelta el archivo OTS (por ejemplo, `certificate.txt.ots`) en el área designada.
4. Arrastra y suelta el archivo con sello de tiempo (por ejemplo, `certificate.txt`) en el área designada.
5. El sitio web verificará automáticamente el sello de tiempo abierto y mostrará el resultado.

Si ves un mensaje como el siguiente tu sello de tiempo es válido:
![cover](assets/opentimestamp_wegui_verified.webp)

### Método CLI

NOTA: este procedimiento **requerirá que se ejecute un nodo local de Bitcoin**

1. Instala el cliente de OpenTimestamps desde el repositorio oficial: https://github.com/opentimestamps/opentimestamps-client ejecutando el siguiente comando:

```
pip install opentimestamps-client
```

2. Navega al directorio que contiene los archivos del certificado extraídos.

3. Ejecuta el siguiente comando para verificar el timestamp abierto:

```
ots verify certificate.txt.ots
```

Este comando:

- Verificará el timestamp contra la blockchain de Bitcoin
- Te mostrará cuándo exactamente fue timestamped el archivo
- Confirmará la autenticidad del timestamp

### Resultados finales

Nota que la verificación es exitosa si se muestran **ambos** mensajes siguientes:

1. La firma GPG se reporta como **"Buena firma de Plan ₿ Network"**
2. La verificación de OpenTimestamps muestra un timestamp específico de un bloque de Bitcoin e informa **"¡Éxito! El bloque de Bitcoin [altura del bloque] atestigua que los datos existían a partir de [timestamp]"**

Ahora que sabes cómo Plan ₿ Network emite prueba verificable para cualquier Certificado de Bitcoin y Diploma de Finalización de Curso, puedes verificar fácilmente la integridad de este.

