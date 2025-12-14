---
name: Ashigaru Terminal
description: Usa Ashigaru en el escritorio para hacer coinjoins
---

![cover](assets/cover.webp)



Ashigaru Terminal es la adaptación del equipo Ashigaru de Sparrow Server, que implementa el protocolo Whirlpool coinjoin. Este software es una continuación del trabajo iniciado por Samourai Wallet, en particular sobre Whirlpool GUI, cuyos principios fundamentales adopta: autocustodia y preservación de la confidencialidad.



Este software es un fork de Sparrow Server, modificado y optimizado para su plena integración con el ecosistema Whirlpool, el protocolo ZeroLink coinjoin desarrollado originalmente por los equipos Samourai.



Ashigaru Terminal opera desde una interfaz TUI minimalista y puede desplegarse en un ordenador personal o en un servidor dedicado. Le permite interactuar directamente con Whirlpool para iniciar "*Tx0*", gestionar cuentas "*Deposit*", "*Premix*", "*Postmix*" y "*Badbank*", y realizar remezclas automáticas para reforzar la confidencialidad de sus piezas.



En resumen, Ashigaru Terminal le será especialmente útil si desea crear coinjoins utilizando Whirlpool.



En este primer tutorial, te llevaré a través de la instalación y el funcionamiento de Ashigaru Terminal. Un segundo tutorial, más avanzado, estará dedicado a la creación de coinjoins.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. Instalar terminal Ashigaru



Para instalar Ashigaru Terminal, necesitará el Navegador Tor, ya que los binarios sólo se distribuyen a través de la red Tor. Si aún no lo ha hecho, [instálelo en su máquina](https://www.torproject.org/download/).



### 1.1. descargar Ashigaru Terminal



Desde el Navegador Tor, vaya a [la página de versiones de su repositorio Git](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) para descargar la última versión de Ashigaru Terminal para su sistema operativo.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



Descargue los 2 archivos siguientes para su sistema operativo:




- El binario (`ashigaru_terminal_v1.0.0_amd64.deb` para Debian/Ubuntu, `.dmg` para macOS o `.zip` para Windows) ;
- El archivo hashes firmado: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2. Compruebe la terminal Ashigaru



Antes de ejecutar el software en tu dispositivo, debes comprobar su autenticidad e integridad. Este es un paso importante, ya que evita que instales una versión fraudulenta que podría comprometer tus bitcoins o infectar tu máquina.



Abra una nueva pestaña del navegador y vaya a [Keybase verification tool](https://keybase.io/verify). Pegue el contenido del archivo `.txt` que acaba de descargar en el campo correspondiente y haga clic en el botón `Verify`.



![Image](assets/fr/02.webp)



Para diversificar sus fuentes de verificación, también puede comparar el mensaje con el disponible en el sitio clearnet [ashigaru.rs](https://ashigaru.rs/download/), en la sección `/download`.



![Image](assets/fr/03.webp)



Si la firma es válida, Keybase mostrará un mensaje confirmando que el archivo ha sido firmado por los desarrolladores de Ashigaru.



![Image](assets/fr/04.webp)



También puede hacer clic en el perfil `ashigarudev` mostrado por Keybase y comprobar que su huella digital de clave coincide exactamente : `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



Si aparece un error en esta fase, la firma no es válida. En este caso, **no instale el software descargado**. Vuelva a empezar desde el principio o pida ayuda a la comunidad antes de continuar.



Keybase te ha proporcionado el hash autenticado de la aplicación. Ahora comprobaremos que el hash del archivo `.deb`, `.zip` o `.dmg` que has descargado coincide con el validado en Keybase. Para ello, dirígete a [ARCHIVO HASH ONLINE](https://hash-file.online/).



Pulsa el botón `BROWSE...` y selecciona el archivo `.deb`, `.zip` o `.dmg` descargado en el paso 1.1. A continuación, seleccione la función hash `SHA-256` y haga clic en `CALCULAR HASH` para generate el hash de su archivo.



![Image](assets/fr/06.webp)



El sitio mostrará el hash del software. Compárelo con el hash que verificó en Keybase.io. Si ambos coinciden perfectamente, la comprobación de autenticidad e integridad se ha realizado correctamente. Ya puede utilizar el software.



![Image](assets/fr/07.webp)



### 1.3 Lanzamiento de la Terminal Ashigaru





- Debian / Ubuntu



Para instalar el software, ejecute el comando :



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



Modifique el orden según la versión descargada.



A continuación, compruebe la instalación:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



A continuación, inicie el software:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- Windows**



Haga clic con el botón derecho del ratón en el archivo `.zip` que ha descargado y comprobado y, a continuación, seleccione `Extraer todo...` para extraer su contenido.



Una vez finalizada la extracción, haz doble clic en el archivo `Ashigaru-terminal.exe` para iniciar el software.



![Image](assets/fr/08.webp)



## 2. Primeros pasos con Ashigaru Terminal



Ashigaru Terminal es un programa TUI (*Text-based User Interface*), es decir, una interfaz minimalista que se ejecuta directamente en el terminal. Usted interactúa con él usando menús y atajos de teclado, pero sin ningún entorno gráfico clásico real.



![Image](assets/fr/09.webp)



Es fácil de usar: utiliza las flechas del teclado para navegar por los menús y pulsa la tecla "Intro" para validar una acción o confirmar una elección.



## 3. Conectando su nodo a la Terminal Ashigaru



Por defecto, Ashigaru Terminal se conecta a un servidor Electrum público. Esto obviamente presenta riesgos en términos de confidencialidad y soberanía. Así que vamos a configurarlo para que se conecte directamente a su propio Electrum Server.



Para ello, abra el menú `Preferencias > Servidor`.



![Image](assets/fr/10.webp)



Haga clic en el botón `< Editar >`.



![Image](assets/fr/11.webp)



Seleccione "Private Electrum Server" y haga clic en "Continue".



![Image](assets/fr/12.webp)



Introduzca la URL y el puerto de su servidor. Puede especificar una dirección Tor en `.onion`. A continuación, haga clic en `< Test >` para verificar la conexión.



![Image](assets/fr/13.webp)



Si la conexión tiene éxito, aparecerá el mensaje `Success`, junto con los detalles de su servidor.



![Image](assets/fr/14.webp)



Si aún no tienes un nodo Bitcoin, te recomiendo que sigas este curso:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*En mi caso, para este tutorial, voy a desconectarme de mi servidor Electrs porque estoy trabajando en testnet. Sin embargo, el funcionamiento sigue siendo estrictamente idéntico en mainnet.*



## 4. Crear una cartera en Ashigaru Terminal



Ahora que el software está correctamente configurado, podemos añadir una cartera Bitcoin.



Tienes dos opciones:




- Puede crear un nuevo wallet desde cero y utilizarlo exclusivamente en el Terminal Ashigaru. En este caso, deberá abrir este software cada vez que desee interactuar con su wallet;
- Alternativamente, puede importar su actual Ashigaru wallet directamente desde su teléfono al Terminal Ashigaru. La desventaja de este método es que reduce ligeramente la seguridad de su configuración, ya que su wallet está expuesto a dos entornos de riesgo en lugar de uno. Por otro lado, ofrece la ventaja de poder dejar Ashigaru Terminal funcionando continuamente para mezclar sus monedas, mientras le permite gastarlas remotamente a través de la aplicación móvil Ashigaru.



En este tutorial, optaremos por el segundo método. Sin embargo, si prefiere crear una cartera completamente nueva, el procedimiento sigue siendo el mismo: la única diferencia será durante la creación, cuando tendrá que guardar su nueva frase mnemotécnica y su nuevo passphrase.



Tenga en cuenta también que Ashigaru Terminal no permite gastar directamente sus bitcoins. Puede sincronizar la misma billetera en Ashigaru Terminal y en la aplicación Ashigaru (lo que haré en este tutorial), o en Sparrow Wallet.



Si aún no tienes una wallet en la aplicación Ashigaru, puedes seguir el tutorial dedicado :



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Vaya al menú "Monederos".



![Image](assets/fr/15.webp)



A continuación seleccione `Crear / restaurar wallet...`. La opción `Abrir Wallet...` le permite acceder posteriormente a una cartera ya guardada en Ashigaru Terminal.



![Image](assets/fr/16.webp)



Dale un nombre a tu cartera.



![Image](assets/fr/17.webp)



A continuación, elija el tipo de cartera `Hot Wallet`.






![Image](assets/fr/18.webp)



Es en esta fase cuando el procedimiento difiere en función de su elección inicial:




- Si desea crear una nueva cartera desde cero, haga clic en `<Generar nueva Wallet>`, defina una passphrase BIP39 y, a continuación, guarde cuidadosamente su frase mnemotécnica y su passphrase en un soporte físico ;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- Si desea utilizar el mismo wallet que su aplicación Ashigaru, introduzca las 12 palabras de su frase mnemotécnica y su passphrase BIP39 directamente en los campos correspondientes. Escriba las palabras en minúsculas, enteras, en orden, separadas por un espacio, sin números ni caracteres adicionales.



Una vez completado este paso, haga clic en `< Siguiente >`.



*Nota*: Si no puede hacer clic en este botón, su frase mnemotécnica no es válida. Compruebe cuidadosamente que ninguna de las palabras sea incorrecta o esté mal escrita.



![Image](assets/fr/19.webp)



A continuación, tendrá que establecer una contraseña. Ésta se utilizará para desbloquear su Terminal Ashigaru wallet y protegerlo contra el acceso físico no autorizado. No interviene en la derivación criptográfica de tus claves: en otras palabras, incluso sin esta contraseña, cualquiera con tu frase mnemotécnica y tu passphrase podrá restaurar tu wallet y acceder a tus bitcoins.



Elija una contraseña larga, compleja y aleatoria. Guarda una copia en un lugar seguro: lo ideal sería en un soporte físico o en un gestor de contraseñas seguro.



Haz clic en `< OK >` cuando hayas terminado.



![Image](assets/fr/20.webp)



## 5. Utilizar la cartera



A continuación, puede elegir a qué cuenta desea acceder. Por el momento, no hemos iniciado ninguna mezcla, así que accederemos a la cuenta `Deposit`.



![Image](assets/fr/21.webp)



El funcionamiento es entonces idéntico al de Sparrow, ya que Ashigaru Terminal es un fork de Sparrow Server. Encontrará los mismos menús:



![Image](assets/fr/22.webp)





- transacciones": permite consultar el historial de transacciones vinculadas a esta cuenta. En mi caso, algunas de ellas ya aparecen, pues había realizado algunas con la aplicación Ashigaru en este mismo wallet.



![Image](assets/fr/23.webp)





- receive`: genera una nueva dirección de recibo en blanco para depositar satss en la cuenta de depósito.



![Image](assets/fr/24.webp)





- direcciones`: muestra una lista de todas sus direcciones, ya pertenezcan a la cadena interna o externa de su cuenta.



![Image](assets/fr/25.webp)





- `UTXOs`: lista todos los UTXOs disponibles.



![Image](assets/fr/26.webp)





- `Settings`: da acceso al *descriptor* de su cartera. También puede consultar su seed, ajustar el *Límite de diferencia* o cambiar la fecha de creación de su cartera.



![Image](assets/fr/27.webp)



Ahora ya sabes cómo instalar y usar Ashigaru Terminal. En el próximo tutorial, veremos cómo realizar coinjoins con este software y cómo gestionar los fondos en "*Postmix*".
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
