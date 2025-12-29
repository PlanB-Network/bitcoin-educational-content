---
name: Bitcoin Keeper - Plan de sucesión
description: Planifique su transmisión de bitcoins con Bitcoin Keeper
---

![cover](assets/cover.webp)



La transferencia de activos de Bitcoin es uno de los retos más subestimados por los titulares. A diferencia de una cuenta bancaria, en la que la institución financiera puede transferir los fondos a los herederos legítimos, Bitcoin depende totalmente de la posesión de claves privadas. Un heredero legal perfectamente legítimo nunca podrá acceder a los fondos sin estas claves, mientras que un individuo malintencionado en posesión de los secretos podrá gastarlos sin ninguna formalidad.



En este segundo tutorial de Bitcoin Keeper, exploramos las funciones premium dedicadas a la planificación patrimonial. La aplicación ofrece herramientas avanzadas para crear Bóvedas Mejoradas, con mecanismos de protección temporizados gracias a Miniscript, así como documentos de acompañamiento para guiar a tus seres queridos.



Esta guía asume que usted ya ha dominado los fundamentos de Bitcoin Keeper (creación de carteras, multisig clásico, la adición de teclas de hardware) como se explica en nuestro primer tutorial :



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-22cbfb8d-790f-4a6f-a92f-93a117e1e65c

![video](https://youtu.be/tCld_-n2d30)



## Planes de suscripción Bitcoin Keeper



Bitcoin Keeper funciona con un modelo freemium con tres niveles de suscripción que ofrecen una funcionalidad progresiva. Para acceder a los planes, ve a la pestaña **Más** y, a continuación, toca tu plan actual (por defecto es "Pleb") para abrir la pantalla **Gestionar suscripción**.



![Plans d'abonnement](assets/fr/01.webp)



El plan **Pleb** (gratuito) proporciona acceso a lo esencial: creación ilimitada de monederos de una o varias claves, compatibilidad con los principales monederos hardware (Coldcard, Trezor, Ledger, Jade, Tapsigner...), control de monedas, etiquetado y conexión a un servidor Electrum personal. Este plan es suficiente para un uso estándar e incluso para configuraciones clásicas de multi-sig.



El plan **Hodler** (9,99 €/mes, con 1 mes gratis si se paga anualmente) incluye todas las funciones de Pleb y añade copias de seguridad cifradas en la nube (iCloud o Google Drive) para restaurar tus cajas fuertes en cualquier dispositivo, Server Key para añadir políticas de gasto automáticas y 2FA por encima de cierto umbral, y Canary Wallets para detectar accesos no autorizados a tus claves.



El plan **Manos de Diamante** (29,99 euros/mes, con 1 mes gratis si se paga anualmente) es el paquete completo para la planificación de la herencia. Incluye todo el plan Hodler y desbloquea la Llave de Herencia (activación diferida), la Llave de Emergencia (llave de emergencia para recuperación en caso de pérdida), las herramientas y documentos de Planificación de Herencias, y una llamada de soporte con el equipo Concierge para validar su configuración. Esta es la oferta para los bitcoiners que desean transmitir su herencia a lo largo de varias generaciones.



Punto importante: los almacenes que hayas creado seguirán siendo accesibles aunque vuelvas al plan gratuito. Tus configuraciones se basan en estándares abiertos (BSMS, Miniscript) y funcionan independientemente de tu suscripción.



## Documentos sucesorios



Una vez que haya activado su suscripción a Diamond Hands, acceda a la sección **Documentos de sucesión** desde la pestaña Más. Bitcoin Keeper ofrece cinco modelos de documentos para estructurar su plan de sucesión, así como una sección de consejos:



![Documents d'héritage](assets/fr/02.webp)





- Plantilla de palabras semilla**: una plantilla para anotar de forma ordenada sus frases de recuperación
- Contactos de confianza**: una plantilla para enumerar los datos de contacto de las personas de confianza implicadas en su plan (notario, abogado, herederos, guardianes de llaves)
- Clave compartida adicional**: documento en el que se detalla la información técnica de cada clave: Código PIN, ruta de derivación, ubicación física, tipo de dispositivo y cualquier otra información útil para identificar y utilizar la clave
- Instrucciones de recuperación**: instrucciones paso a paso para que el heredero o beneficiario recupere los fondos
- Carta al abogado**: una carta precumplimentada que puede adaptarse para su abogado o notario



La sección **Consejos para la herencia** ofrece consejos prácticos para asegurar las llaves a los herederos y optimizar su plan de sucesión.



Personalice estos documentos para adaptarlos a su situación y guárdelos en un lugar seguro, separados de las propias llaves.



## Configuración de la copia de seguridad en la nube



Antes de crear tu almacén heredado, activa la copia de seguridad en la nube para proteger tus archivos de configuración. En la pestaña Más, pulsa **Copia de seguridad en la nube personal**.



![Configuration Cloud Backup](assets/fr/03.webp)



Elija una contraseña segura para encriptar sus copias de seguridad. Esta contraseña sólo protege los archivos de configuración de wallet (no tus claves privadas). Confirma la contraseña y pulsa **Confirmar**. Sus copias de seguridad se almacenarán en su iCloud o Google Drive dependiendo de su dispositivo. Pulsa **Hacer copia de seguridad ahora** para iniciar tu primera copia de seguridad.



## Importe sus llaves hardware



Para nuestro ejemplo, crearemos una caja fuerte 2-de-3 con dos claves adicionales (Herencia y Emergencia). Empecemos importando todas las claves necesarias en la pestaña **Claves**.



![Import des clés hardware](assets/fr/04.webp)



Pulse **Añadir llave**, luego seleccione **Añadir llave de un hardware** para conectar un hardware wallet. Bitcoin Keeper es compatible con muchos dispositivos: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner y Specter Solutions.



En nuestra configuración, importamos :




- 2 llaves **Coldcard** (MK4SP y MK4)
- 2 llaves **Tapsigner** (Metro y Genesis)



Para añadir una Coldcard, selecciónela de la lista y siga las instrucciones en pantalla para exportar la clave pública mediante código QR, archivo, USB o NFC. Para más detalles sobre cómo utilizar una Coldcard o Tapsigner, consulte nuestros tutoriales dedicados:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59


Una vez importadas todas tus claves, las encontrarás en la pestaña Claves con sus nombres personalizados.



## Crear el legado wallet



Pasemos a la creación del baúl. En la pestaña **Monederos**, pulsa **Añadir Wallet**, selecciona **Bitcoin Wallet** y, a continuación, **Crear Wallet**.



![Création du wallet](assets/fr/05.webp)



Elija el tipo de wallet. Para nuestro plan heredado, seleccione **2 de 3 multi-llave**. En la parte inferior de la pantalla, active **Opciones de seguridad mejoradas** y pulse **Proceder**.



![Options de sécurité avancées](assets/fr/06.webp)



En la ventana emergente Opciones de seguridad mejoradas, marque :




- Clave de herencia**: una clave adicional que se añadirá al quórum tras un periodo de tiempo determinado
- Llave de emergencia**: una llave con control total diferido para recuperar fondos en caso de pérdida de la llave



Pulse **Guardar cambios**. A continuación, seleccione las 3 teclas que compondrán su wallet de entre las importadas (por ejemplo, Seed Key, Coldcard MK4SP y Tapsigner Metro).



## Fijación de plazos especiales



La siguiente pantalla le permite configurar la Llave de Emergencia y la Llave de Herencia. Aquí se definen los retrasos que rigen la activación de estas llaves especiales.



![Configuration des délais](assets/fr/07.webp)



Para la **Llave de Emergencia**, seleccione la llave hardware que servirá como último respaldo (aquí Coldcard MK4) y elija el plazo de activación (en nuestro ejemplo: 2 años). A diferencia de la Llave de Herencia, la Llave de Emergencia no se añade al quórum: le permite **pasar por alto el multisig** por completo, y le da un control total sobre los fondos una vez expirado el plazo. Es su solución de último recurso: si se pierden o destruyen varias claves, esta única clave le permite recuperarlo todo. Por tanto, debe protegerse con el máximo rigor.



Para la **Llave de Herencia**, seleccione la llave destinada al heredero (aquí Coldcard MK4SP) y elija la demora (en nuestro ejemplo: 1 año). Después de un año sin movimiento, esta llave **se añadirá al quórum de firmas**. En la práctica, su wallet 2-de-3 se convertirá en una wallet 2-de-4 una vez transcurrido este plazo, lo que permitirá al heredero participar en la firma junto con las llaves existentes.



### ¿Cómo funcionan los relojes programadores?



La Bitcoin Keeper utiliza **timelocks absolutos** (CLTV - CheckLockTimeVerify), posibles gracias a Miniscript. A diferencia de los timelocks relativos (CSV), que comienzan cuando se recibe cada UTXO, los timelocks absolutos funcionan con una **fecha de caducidad fija** definida cuando se crea el wallet.



En concreto, si crea una wallet hoy con una Clave de Herencia de 1 año, la fecha de activación será "hoy + 1 año". Todos los fondos depositados en esta wallet, sea cual sea su fecha de depósito, serán accesibles a través de la Clave de Herencia en esa misma fecha.



La ventaja de los relojes absolutos es que permiten plazos superiores a 15 meses (el límite de los relojes CSV relativos), lo que explica que Bitcoin Keeper pueda ofrecer opciones como 2 años.



### El mecanismo de actualización



Para evitar la activación de claves especiales durante tu vida, debes "refrescar" periódicamente tu wallet. Con los relojes absolutos, esto implica **recrear la wallet con una nueva fecha de caducidad** en el futuro y transferir tus fondos a esta nueva wallet.



Bitcoin Keeper simplifica este proceso con una función de actualización integrada. La aplicación se encarga automáticamente de la complejidad en segundo plano: usted sólo tiene que seguir los pasos guiados, sin tener que crear manualmente una nueva wallet ni transferir los fondos usted mismo. Planifique esta operación periódicamente, con suficiente antelación al vencimiento del plazo más corto configurado. Por ejemplo, con una Clave de Herencia de 1 año, actualícela cada 9-10 meses para mantener un margen de seguridad.



## Guardar y exportar la configuración



Una vez creada la wallet, la aplicación le recuerda que debe guardar el fichero de configuración. **Este paso es crítico**: sin este archivo, sus herederos no podrán reconstituir la wallet multisig.



![Export de la configuration](assets/fr/08.webp)



Pulse **Copia de seguridad del archivo de recuperación Wallet**. Están disponibles varias opciones de exportación:




- Exportación a PDF**: genera un documento completo con toda la información de wallet
- Mostrar QR**: muestra un código QR para importar la configuración en otro dispositivo
- Airdrop / Exportación de archivos**: exporta el archivo a través de las opciones de uso compartido
- NFC**: compartir mediante NFC con un dispositivo compatible



Multiplica las copias: una en tu notaría, otra en la caja fuerte de un banco y otra en versión digital encriptada. Tu nueva wallet aparece ahora en la pestaña Carteras con las etiquetas "Multi-llave", "2 de 3", "Llave heredada" y "Llave de emergencia".



## Crear un canario Wallet



La Wallet canaria es un sistema de alerta temprana. La idea: cada llave utilizada en una wallet multi-llave puede utilizarse también en otra wallet de llave única. Depositando una pequeña suma en esta wallet "canaria", cualquier movimiento no autorizado señala un compromiso de la llave.



![Canary Wallets](assets/fr/09.webp)



Hay dos formas de configurar una Wallet Canary. Desde la pestaña **Más**, pulsa **Canary Wallets** en la sección "Keys and Wallets". La pantalla explica el principio: si alguien accede a una de tus llaves y encuentra fondos en la llave única wallet asociada, intentará eliminarlos, lo que te alertará.



![Configuration Canary depuis une clé](assets/fr/10.webp)



También puede configurar el Canary directamente desde una tecla. En la pestaña **Llaves**, seleccione una llave (por ejemplo, Tapsigner Genesis), pulse el icono **Configuración** (engranaje) y, a continuación, **Canario Wallet**. El canario wallet asociado se abre, listo para recibir algunos satoshis de vigilancia.



Deposite una pequeña suma (unos miles de satoshis) en cada Canary Wallet. Si estos fondos se mueven sin su acuerdo, retire inmediatamente la llave comprometida de sus cajas fuertes multisig.



## Buenas prácticas



**Prueba tu configuración** con una pequeña cantidad de dinero antes de poner una gran suma. Envía unos miles de satoshis a la cámara acorazada y luego prueba un gasto saliente para comprobar que dominas el proceso de firma con cada dispositivo. Prueba también a importar el archivo de configuración en otro teléfono para asegurarte de que la copia de seguridad funciona.



**Distribuya las claves de forma inteligente**. Para los Tapsigners, entréguelas en un sobre cerrado con el PIN comunicado por separado (por ejemplo, en la carta de instrucciones de recuperación guardada en otro lugar). Para los monederos hardware clásicos, guarde el dispositivo con un tercero de confianza y la seed en papel o metal con usted u otro tercero. Anote la huella de cada clave y su nombre en el archivo de configuración para evitar confusiones.



**Planifique pruebas periódicas** (simulacros de incendio). Anualmente, compruebe que puede reconstruir la caja fuerte a partir de copias de seguridad en un teléfono en blanco. Pruebe las alertas Canary comprobando los saldos. Simule escenarios de pérdida ("¿y si pierdo la Coldcard?") para confirmar que las combinaciones de teclas restantes son suficientes.



**No olvides la actualización**. Si has configurado tu Clave de Herencia a 1 año, actualízate cada 9-10 meses. Es el precio que pagas por la transmisión automática sin intervención de terceros.



**Mantener el plan actualizado**. Cualquier cambio (sustitución de una clave, modificación de herederos, cambio de plazo) debe reflejarse en todas las copias de seguridad y documentos. Regenere los PDF después de cada modificación y redistribuya las nuevas versiones.



## Límites y consideraciones



A pesar de la potencia de estas herramientas, es importante reconocer sus limitaciones para gestionarlas con la mayor eficacia posible.



La **complejidad** de una caja fuerte multisig con temporizadores puede ser un riesgo en sí mismo: mala configuración, malentendido por parte de los herederos, pérdida de un elemento crítico entre los muchos componentes. Bitcoin Keeper simplifica al máximo la experiencia, pero sigue siendo una operación técnica. Despliegue este plan sólo si el importe a proteger lo justifica. Para importes pequeños, puede bastar un plan más sencillo.



Merece la pena reflexionar sobre la **dependencia de la aplicación**. Aunque el código es abierto y se basa en estándares abiertos (Miniscript, BSMS), ciertas funcionalidades dependen del ecosistema Keeper. Conserve una copia de la aplicación (Android APK o iOS IPA) y documente en sus cartas a los herederos la posibilidad de utilizar otros monederos compatibles con Miniscript (como Liana) para recuperar los fondos.



Los intermediarios de confianza** introducen un riesgo humano. ¿Qué ocurre si un pariente malintencionado utiliza la llave que se le ha confiado antes de la fecha límite? ¿O si el abogado extravía sus documentos? Elija a estas personas con cuidado, explíqueles claramente sus responsabilidades y tenga un plan B. Las carteras canarias, las copias de seguridad redundantes y la propia estructura de multisig siguen siendo su mejor protección contra estos riesgos.



## Conclusión



Bitcoin Keeper, con su plan Manos de Diamante, ofrece una completa caja de herramientas para la planificación patrimonial: Bóvedas mejoradas con llaves temporizadas, documentos de acompañamiento, Carteras Canarias y asistencia personalizada.



Es algo más que una cuestión técnica: se trata de diseñar la arquitectura de tu herencia, distribuir inteligentemente las claves y los conocimientos, y poner a prueba el sistema con regularidad. Un plan de herencia Bitcoin bien diseñado transforma tus satoshis en un legado real y transferible.