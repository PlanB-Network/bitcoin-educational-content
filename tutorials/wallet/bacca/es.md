---
name: Bacca
description: Configuración de un Ledger sin el software Ledger Live
---
![cover](assets/cover.webp)

Si utilizas un Ledger, probablemente te habrás dado cuenta de que tienes que pasar por el software Ledger Live, al menos para la configuración inicial del dispositivo, para comprobar su autenticidad e instalar la aplicación Bitcoin en él. Sin embargo, después de esta configuración, muchos bitcoiners prefieren utilizar software especializado de gestión de monederos Bitcoin como Sparrow o Liana en lugar de Ledger Live. Aunque Ledger produce excelentes monederos hardware que incluyen rápidamente las últimas funciones de Bitcoin, su software no está necesariamente adaptado a las necesidades específicas de los bitcoiners. De hecho, Ledger Live incluye muchas funciones diseñadas para altcoins, mientras que las opciones dedicadas a la gestión de monederos Bitcoin son limitadas. Pero el problema con Sparrow y Liana (por el momento), es que no permiten instalar la aplicación Bitcoin en el Ledger.

Para evitar la necesidad de utilizar Ledger Live durante la configuración inicial de su Ledger, puede utilizar la herramienta Bacca, (o "Instalador de Ledger"). Este software le permite instalar y actualizar la aplicación Bitcoin, verificar la autenticidad de su Ledger, e incluso actualizar posteriormente el firmware del dispositivo. Bacca fue creado por Antoine Poinsot (Darosior), desarrollador de Bitcoin Core en Chaincode Labs, cofundador [de Revault y Liana](https://wizardsardine.com/), y Pythcoiner.

En este tutorial, te mostraré cómo utilizar esta herramienta, para que puedas prescindir definitivamente del software Ledger Live y seguir disfrutando de los dispositivos Ledger. Funciona en todos los dispositivos: Nano S Classic, Nano S Plus, Nano X, Flex y Stax.

---
*Tenga en cuenta que esta herramienta es bastante nueva, y sus desarrolladores especifican que aún está **en fase de pruebas**. Recomiendan utilizarla sólo con fines de prueba, y no para un dispositivo destinado a alojar un monedero Bitcoin real, aunque es posible hacerlo. En este sentido, recomiendo seguir las recomendaciones de los desarrolladores de esta herramienta, que se especifican [en el README de su repositorio de GitHub](https://github.com/darosior/ledger_installer).*

---
## Requisitos previos

En tu ordenador, necesitarás dos herramientas para utilizar Bacca:


- Git ;
- Óxido.

Si ya los has instalado, puedes saltarte este paso.

**Linux:**

En una distribución Linux, Git suele estar preinstalado. Para comprobar si Git está instalado en su sistema, puede escribir el siguiente comando en el terminal :

```bash
git --version
```

Si no tienes Git instalado en tu sistema, aquí tienes el comando para instalarlo en un sistema Debian :

```bash
sudo apt install git
```

Por último, para instalar su entorno de desarrollo Rust, utilice el comando :

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

**Windows:**

Para instalar Git, visita [el sitio web oficial del proyecto](https://git-scm.com/). Descarga el software y sigue las instrucciones de instalación.

![BACCA](assets/fr/01.webp)

Proceda del mismo modo para instalar Rust desde [el sitio web oficial](https://www.rust-lang.org/tools/install).

![BACCA](assets/fr/02.webp)

**MacOS:**

Si Git aún no está instalado en tu sistema, abre un terminal y ejecuta el siguiente comando para instalarlo:

```bash
git --version
```

Si Git no está instalado en tu sistema, se abrirá una ventana ofreciéndote instalar Xcode, que incluye Git. Simplemente sigue las instrucciones en pantalla para proceder con la instalación.

Para instalar Rust, ejecute el siguiente comando:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## Instalación de Bacca

Abra un terminal y vaya a la carpeta donde desea guardar el software, a continuación, ejecute el siguiente comando:

```bash
git clone https://github.com/darosior/ledger_installer.git
```

Navegue hasta el directorio del software:

```bash
cd ledger_installer
```

A continuación, utiliza Cargo para compilar el proyecto y ejecutar la interfaz gráfica de Bacca:

```bash
cargo run -p ledger_manager_gui
```

Ahora tiene acceso a la interfaz del software.

![BACCA](assets/fr/03.webp)

## Configuración del Libro Mayor

Antes de empezar, si su Ledger es nuevo, asegúrese de haber configurado el código PIN y guardado la frase de recuperación. No necesita Ledger Live para estos pasos iniciales. Simplemente conecta tu Ledger a través del cable USB para encenderlo. Si no estás seguro de cómo proceder con estos dos pasos, puedes consultar el principio del tutorial específico para tu modelo:

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Uso de Bacca

Conecte su Ledger a su ordenador y desbloquéelo utilizando el código PIN que haya establecido. Bacca debería detectar automáticamente su Ledger.

![BACCA](assets/fr/04.webp)

Para confirmar la autenticidad de su Ledger, haga clic en el botón "*Comprobar*". Tendrás que autorizar la conexión en tu dispositivo Ledger para continuar.

![BACCA](assets/fr/05.webp)

Bacca le informará entonces de si su Ledger es auténtico. Si no lo es, esto indica que el dispositivo ha sido comprometido, o que es una falsificación. En este caso, deja de usarlo inmediatamente.

![BACCA](assets/fr/06.webp)

En el menú "*Aplicaciones*" puede consultar la lista de aplicaciones ya instaladas en su Ledger.

![BACCA](assets/fr/07.webp)

Para instalar la aplicación Bitcoin, haga clic en "*Instalar*" y, a continuación, autorice la instalación en su Ledger.

![BACCA](assets/fr/08.webp)

La aplicación está bien instalada.

![BACCA](assets/fr/09.webp)

Si no tiene instalada la última versión de la aplicación Bitcoin, Bacca mostrará un botón "*Actualizar*" en lugar de la indicación "*Latest*". Simplemente haga clic en este botón para actualizar la aplicación.

![BACCA](assets/fr/10.webp)

Ahora que tu Ledger está correctamente configurado con la última versión de la aplicación Bitcoin, estás listo para importar y utilizar tu monedero en software de gestión como Sparrow o Liana, ¡sin tener que pasar por Ledger Live!

Si este tutorial te ha resultado útil, te agradecería que dejaras un pulgar verde a continuación. No dudes en compartir este artículo en tus redes sociales. ¡Muchas gracias!

También te recomiendo que eches un vistazo a este tutorial sobre GnuPG, que explica cómo comprobar la integridad y autenticidad de tu software antes de instalarlo. Se trata de una práctica importante, especialmente cuando se instala software de gestión de carteras como Liana o Sparrow :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

