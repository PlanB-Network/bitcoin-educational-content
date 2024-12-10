---
name: GnuPG
description: Cómo verificar la integridad y autenticidad del software?
---
![cover](assets/cover.webp)

Al descargar software, es muy importante asegurarse de que no ha sido alterado y que efectivamente proviene de la fuente oficial. Esto es especialmente cierto para el software relacionado con Bitcoin, como el software de billetera, que te permite asegurar las claves que dan acceso a tus fondos. En este tutorial, veremos cómo verificar la integridad y autenticidad del software antes de instalarlo. Usaremos Sparrow Wallet como ejemplo, un software de billetera favorito entre los bitcoiners, pero el procedimiento será el mismo para cualquier otro software.

Verificar la integridad implica asegurarse de que el archivo descargado no ha sido modificado comparando su huella digital (es decir, su hash) con la proporcionada por el desarrollador oficial. Si coinciden, significa que el archivo es idéntico al original y no ha sido corrompido o modificado por un atacante.

Verificar la autenticidad, por otro lado, asegura que el archivo efectivamente proviene del desarrollador oficial y no de un impostor. Esto se hace verificando una firma digital. Esta firma prueba que el software fue firmado con la clave privada legítima del desarrollador.

Si estas comprobaciones no se realizan, existe el riesgo de instalar malware que podría contener código modificado. Este código podría robar información como tus claves privadas o bloquear el acceso a tus archivos. Este tipo de ataque es bastante común, especialmente en el contexto del software de código abierto donde se pueden distribuir versiones falsificadas.

Para realizar esta verificación, usaremos dos herramientas: funciones de hashing para verificar la integridad, y GnuPG, una herramienta de código abierto que implementa el protocolo PGP, para verificar la autenticidad.

## Prerrequisitos

Si estás en **Linux**, GPG está preinstalado en la mayoría de las distribuciones. Si no, puedes instalarlo con el siguiente comando:

```bash
sudo apt install gnupg
```

Para **macOS**, si aún no has instalado el gestor de paquetes Homebrew, hazlo con los siguientes comandos:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
```

```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Luego instala GPG con este comando:

```bash
brew install gnupg
```
Para **Windows**, si no tienes GPG, puedes instalar el software [Gpg4win](https://www.gpg4win.org/).
![GnuPG](assets/notext/01.webp)

## Descargando Documentos

Para comenzar, necesitaremos varios documentos. Visita el sitio oficial de [Sparrow Wallet en la sección "*Download*"](https://sparrowwallet.com/download/). Si deseas verificar otro software, ve al sitio web de ese software.

![GnuPG](assets/notext/02.webp)

También puedes ir [al repositorio de GitHub del proyecto](https://github.com/sparrowwallet/sparrow/releases).

![GnuPG](assets/notext/03.webp)

Descarga el instalador del software correspondiente a tu sistema operativo.

![GnuPG](assets/notext/04.webp)

También necesitarás el hash del archivo, a menudo llamado "*SHA256SUMS*" o "*MANIFEST*".

![GnuPG](assets/notext/05.webp)

Descarga la firma PGP del archivo también. Este es el documento en formato `.asc`.

![GnuPG](assets/notext/06.webp)
Asegúrate de colocar todos estos archivos en la misma carpeta para los siguientes pasos.
Finalmente, necesitarás la llave pública del desarrollador, la cual usaremos para verificar la firma PGP. Esta llave a menudo está disponible ya sea en el sitio web del software, en el repositorio de GitHub del proyecto, a veces en las redes sociales del desarrollador, o en sitios especializados como Keybase. En el caso de Sparrow Wallet, puedes encontrar la llave pública del desarrollador Craig Raw [en Keybase](https://keybase.io/craigraw). Para descargarla directamente desde el terminal, ejecuta el comando:

```bash
curl https://keybase.io/craigraw/pgp_keys.asc | gpg --import
```

![GnuPG](assets/notext/07.webp)

## Verificando la Firma

El proceso de verificación de la firma es el mismo en **Windows**, **macOS** y **Linux**. Normalmente, ya habrás importado la llave pública durante el paso anterior, pero si no, hazlo con el comando:

```bash
gpg --import [ruta de la llave]
```

Reemplaza `[ruta de la llave]` con la ubicación del archivo de la llave pública del desarrollador.

![GnuPG](assets/notext/08.webp)

Verifica la firma con el siguiente comando:

```bash
gpg --verify [archivo.asc]
```

Reemplaza `[archivo.asc]` con la ruta del archivo de la firma. En el caso de Sparrow, este archivo se llama "*sparrow-2.0.0-manifest.txt.asc*" para la versión 2.0.0.

![GnuPG](assets/notext/09.webp)

Si la firma es válida, GPG te lo indicará. Entonces puedes pasar al siguiente paso, ya que esto confirma la autenticidad del archivo.

![GnuPG](assets/notext/10.webp)

## Verificando el Hash
Ahora que la autenticidad del software ha sido confirmada, también es necesario verificar su integridad. Compararemos el hash del software con el hash proporcionado por el desarrollador. Si ambos coinciden, garantiza que el código del software no ha sido alterado.

En **Windows**, abre un terminal y ejecuta el siguiente comando:

```bash
CertUtil -hashfile [ruta del archivo] SHA256 | findstr /v "hash"
```

Reemplaza `[ruta del archivo]` con la ubicación del instalador.

![GnuPG](assets/notext/11.webp)

El terminal devolverá el hash del software descargado.

![GnuPG](assets/notext/12.webp)

Ten en cuenta que, para algunos softwares, puede ser necesario usar una función de hash diferente a SHA256. En este caso, simplemente reemplaza el nombre de la función de hash en el comando.

Luego compara el resultado con el valor correspondiente en el archivo "*sparrow-2.0.0-manifest.txt*".

![GnuPG](assets/notext/13.webp)

En mi caso, vemos que los dos hashes coinciden perfectamente.

En **macOS** y **Linux**, el proceso de verificación del hash es automatizado. No es necesario verificar manualmente la coincidencia entre los dos hashes como en Windows.

Simplemente ejecuta este comando en **macOS**:

```bash
shasum --check [nombre del archivo] --ignore-missing
```

Reemplaza `[nombre del archivo]` con el nombre del instalador. Por ejemplo, para Sparrow Wallet:

```bash
shasum --check sparrow-2.0.0-manifest.txt --ignore-missing
```

Si los hashes coinciden, deberías ver la siguiente salida:

```bash
Sparrow-2.0.0.dmg: OK
```
En **Linux**, el comando es similar:
```bash
sha256sum --check [nombre del archivo] --ignore-missing
```

Y si los hashes coinciden, deberías ver la siguiente salida:

```bash
sparrow_2.0.0-1_amd64.deb: OK
```

Ahora puedes estar seguro de que el software que has descargado es auténtico e íntegro. Puedes proceder con su instalación en tu máquina.

Si encontraste útil este tutorial, agradecería mucho un pulgar arriba abajo. No dudes en compartir este artículo en tus redes sociales. ¡Muchas gracias!

También recomiendo revisar este otro tutorial sobre VeraCrypt, un software que te permite cifrar y descifrar dispositivos de almacenamiento.

https://planb.network/tutorials/others/general/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5