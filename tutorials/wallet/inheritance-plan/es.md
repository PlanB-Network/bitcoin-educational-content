---
name: Plan de sucesión Bitcoin
description: Cómo transferir bitcoins a tus seres queridos
---

![cover](assets/cover.webp)



La transmisión de bitcoins representa un importante reto técnico que muchos titulares pasan por alto. A diferencia de los activos bancarios tradicionales, en los que una entidad financiera puede remitir los fondos a sus legítimos propietarios, Bitcoin funciona sin intermediarios. Sus seres queridos nunca podrán acceder a sus fondos sin la información técnica necesaria, independientemente de su legitimidad legal.



Este tutorial te guía a través de la creación de un plan técnico de herencia. Aprenderás cómo funcionan los mecanismos de on-chain para la transmisión automatizada, cómo documentar tus configuraciones y cómo elegir las soluciones adecuadas para garantizar que tu legado de Bitcoin siga siendo accesible para tus seres queridos.



## Por qué es esencial un plan técnico de patrimonio



Bitcoin se basa en un principio criptográfico fundamental: quien posee las claves privadas controla los fondos. Esta soberanía se convierte en una gran vulnerabilidad cuando el titular desaparece sin haber transmitido la información necesaria.



Un plan de sucesión de Bitcoin debe cumplir dos objetivos aparentemente contradictorios: permitir que sus seres queridos accedan a sus fondos cuando llegue el momento, y evitar al mismo tiempo que cualquier otra persona acceda a ellos antes de tiempo. Este delicado equilibrio se basa en las capacidades de programación nativas de Bitcoin.



La complejidad técnica añade una capa extra de dificultad. Sus herederos tendrán que manipular conceptos como frases de recuperación, descriptores de cartera o vías de derivación. Sin una preparación adecuada, incluso un heredero bienintencionado corre el riesgo de cometer errores irreversibles.



## Cómo funciona la herencia on-chain



Bitcoin utiliza su lenguaje de scripting para codificar las condiciones de gasto directamente en las transacciones. La herencia de on-chain aprovecha esta programabilidad para crear vías de recuperación alternativas que se activan automáticamente.



### Timelocks



Los bloqueos temporales son el mecanismo fundamental de la herencia de Bitcoin. Permiten bloquear fondos hasta que se cumpla una condición temporal.



**CLTV (CheckLockTimeVerify)**: Este bloqueo de tiempo absoluto comprueba que se ha alcanzado un tiempo específico (fecha o altura de bloque) antes de autorizar el gasto. Por ejemplo, "estos fondos sólo pueden gastarse después del bloque 900000" o "después del 1 de enero de 2026". La ventaja de la CLTV es que permite grandes retrasos (varios años), pero la fecha es fija y se aplica de forma idéntica a todos los UTXO de la cartera. Para mantener el control de sus fondos, debe crear periódicamente una nueva cartera con una fecha de vencimiento ampliada y transferirle sus fondos.



**CSV (CheckSequenceVerify)**: Este bloqueo temporal relativo verifica que ha transcurrido un determinado número de bloques desde que se creó la UTXO. Por ejemplo, "estos fondos sólo pueden gastarse 52560 bloques (~1 año) después de su recepción". La ventaja de CSV es que cada UTXO tiene su propio contador independiente. Cada vez que se realiza una transacción, los UTXO recién creados reinician su propio límite de tiempo. Sin embargo, el límite técnico de 65535 bloques (~15 meses como máximo) restringe los plazos posibles. Este enfoque es más natural para el uso diario, ya que tu actividad normal retrasa automáticamente los plazos.



### Múltiples vías de gasto



Una cartera de herencia combina varias vías de gasto en cada dirección:





- Vía principal** : El propietario puede gastar sus fondos en cualquier momento con su llave principal, sin restricciones de tiempo.
- Vía(s) de recuperación **: Una o varias claves alternativas pueden gastar fondos sólo después de transcurrido un tiempo establecido.



Cada transacción realizada por el propietario "refresca" la UTXO, creando nuevas salidas con temporizadores restablecidos. Este mecanismo garantiza que, mientras el propietario permanezca activo, las rutas de recuperación nunca se activen.



### Miniscript y Taproot



**Miniscript** es un lenguaje estructurado desarrollado por Andrew Poelstra, Pieter Wuille y Sanket Kanjalkar que facilita la escritura y el análisis de scripts Bitcoin complejos. Permite componer condiciones de gasto legibles y verificables, esenciales para las configuraciones de herencia que implican múltiples claves y relojes.



**Taproot** (activado en noviembre de 2021) mejora significativamente la herencia de on-chain. Gracias a su estructura de árbol (MAST), solo se revela en la blockchain la condición de gasto utilizada. Si el propietario gasta sus fondos normalmente, las condiciones de herencia permanecen invisibles. Esta confidencialidad también reduce los costes de transacción en el caso de rutas complejas.



## La importancia crítica de los descriptores



Para las carteras heredadas, la frase de recuperación (seed) no basta para restablecer el acceso a los fondos. El **descriptor** se convierte en el elemento crítico.



Un descriptor es una cadena que describe exhaustivamente la estructura de una cartera: las claves públicas implicadas, las condiciones de gasto, las vías de derivación y los calendarios configurados. He aquí un ejemplo simplificado:



```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```



Este descriptor dice: "o bien la clave maestra puede gastar inmediatamente, o bien la clave de recuperación puede gastar después de 52560 bloques".



Desgranemos este ejemplo:




- `wsh()` : Witness Script Hash, indica el tipo de dirección (P2WSH)
- or_d()`: condición "o" con una rama por defecto
- pk([huella/ruta]xpub...)`: La clave pública maestra con su huella digital y ruta de derivación
- and_v()`: condición "and" que combina la clave de recuperación con el bloqueo de tiempo
- `older(52560)`: El bloqueo temporal relativo de 52560 bloques



**Sin el descriptor, incluso con todas las frases de recuperación, sus herederos no podrán reconstruir la cartera.** Una cartera estándar sólo puede restaurarse a partir de seed porque sigue rutas de derivación estandarizadas (BIP44, BIP84). Una cartera heredada, en cambio, utiliza rutas de derivación personalizadas que no se pueden adivinar. La copia de seguridad del descriptor (o el archivo de configuración exportado por su software) debe acompañar a las frases de recuperación en su plan de herencia.



## Componentes documentales de un plan de sucesión



Más allá de los mecanismos técnicos, un plan de legado eficaz se apoya en tres pilares de documentación.



### La carta de herencia



Esta carta personal es el punto de entrada a su plan. Escrita para sus herederos, explica el contexto y las precauciones que deben tomarse.



Su carta debe incluir normas de seguridad explícitas:




- No se precipite, tómese su tiempo para aprender antes de mover fondos
- Nunca comunique una frase de recuperación completa a una sola persona
- No introduzca nunca una frase de recuperación en un programa informático o un ordenador no verificados
- Cuidado con las estafas y las personas que ofrecen ayuda no solicitada
- Pide consejo al menos a dos personas de confianza antes de tomar una decisión



Esta carta también contiene los datos de contacto de su notario y la ubicación de su testamento. Nunca debe contener frases de recuperación ni contraseñas.



### El directorio de contactos de confianza



Ningún heredero debe enfrentarse solo a la recuperación de bitcoins. Este directorio enumera a las personas que pueden prestar asistencia técnica o jurídica.



Para cada contacto, documente: nombre completo, relación con usted, papel en el plan, nivel de confianza, habilidades para Bitcoin y datos de contacto completos. La regla básica: tus herederos siempre deben consultar al menos a dos personas distintas antes de tomar cualquier decisión importante.



### Inventario de activos de Bitcoin



Esta sección mapea todos tus bitcoins con la información técnica necesaria para recuperarlos.



Para cada cartera, documente :




- Tipo de cartera**: hardware, software, configuración (single-sig, multisig, legacy)
- Ubicación del dispositivo**: ubicación física del hardware de wallet
- Descriptor/ubicación del archivo de configuración**: crítico para carteras avanzadas
- Localización de la frase de recuperación**: separada del descriptor
- Códigos de acceso**: donde se almacenan los PIN y las contraseñas
- Retrasos configurados**: cuando se activan las vías de recuperación



## Soluciones técnicas disponibles



Varios paquetes de software aplican mecanismos de herencia on-chain. Cada uno tiene sus propias características técnicas.



### Liana



Liana es un software de escritorio (Linux, macOS, Windows) que utiliza Miniscript para crear carteras con rutas de recuperación temporizadas. El proyecto está desarrollado por Wizardsardine, cofundada por Antoine Poinsot (colaborador principal de Bitcoin).



**Arquitectura técnica**: Liana crea carteras P2WSH (SegWit nativo) por defecto, con soporte Taproot disponible dependiendo de la compatibilidad de su hardware wallet. La arquitectura se basa en una ruta principal y una o más rutas de recuperación. El descriptor generado codifica todas las condiciones y debe guardarse.



**Temporizadores utilizados**: Liana utiliza timelocks relativos (CSV), limitados a 65535 bloques (~15 meses). Para mantener el control, debes realizar una transacción de refresco antes de que expire el timelock.



**Integración de hardware wallet**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY, y otros dispositivos son compatibles para firmar transacciones.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper



Bitcoin Keeper es una aplicación móvil (iOS, Android) que combina multisig y relojes a través de sus "Bóvedas mejoradas". El enfoque móvil con guía integrada la hace accesible a los usuarios menos técnicos.



**Arquitectura técnica**: Las Bóvedas Mejoradas utilizan Miniscript para crear configuraciones multisig donde las llaves adicionales se activan tras retardos definidos. La Llave de Herencia se añade al quórum existente, mientras que la Llave de Emergencia puede saltarse la multisig completamente.



**Temporizadores utilizados**: Bitcoin Keeper utiliza timelocks absolutos (CLTV), lo que permite plazos superiores a 15 meses. La fecha de activación se fija en el momento de la creación de wallet y se aplica a todos los UTXO. La aplicación incorpora una función de "revaulting" que gestiona automáticamente la actualización: el usuario simplemente sigue los pasos guiados, sin tener que crear manualmente una nueva wallet.



**Características adicionales**: Documentos de herencia integrados, Canary Wallets para detectar compromiso de claves y recordatorios de actualización.



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Patrimonio



Heritage es una aplicación de escritorio que utiliza scripts Taproot para codificar las condiciones de herencia. El uso de Taproot ofrece una mayor confidencialidad, ya que las rutas no utilizadas permanecen invisibles en la blockchain.



**Arquitectura técnica**: Cada dirección de Herencia integra una vía principal y vías alternativas para cada heredero, con plazos progresivos. La estructura jerárquica permite definir un respaldo personal a 6 meses y herederos familiares a 12-15 meses.



**Modos de uso**: Versión autónoma con su propio nodo (gratuita) o servicio gestionado que añade recordatorios y notificaciones a los herederos (0,05%/año).



https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## El proceso de recuperación del heredero



Comprender el proceso de recuperación ayuda a preparar un plan eficaz. He aquí los pasos técnicos que deberá seguir un heredero.



### Requisitos de recuperación



El heredero necesita :


1. **El descriptor o archivo de configuración** de la cartera original (formato JSON o texto, según el software)


2. **Su frase de recuperación** (la asociada a su clave de herencia, normalmente 12 o 24 palabras)


3. **Software compatible** (Liana, Bitcoin Keeper, Heritage o Sparrow/Specter para descriptores estándar)


4. **Una conexión a un nodo Bitcoin** para comprobar el estado del timelock y difundir la transacción



### Pasos de la recuperación



1. **Instalar el software** en un dispositivo seguro y configurar la conexión a la red Bitcoin (nodo personal o servidor Electrum)


2. **Importar el descriptor** para reconstruir la estructura de la cartera. El software generate automáticamente todas las direcciones utilizadas


3. **Restaurar clave de herencia** de la frase de recuperación. El software comprobará que esta clave corresponde a una de las claves autorizadas en el descriptor


4. **Sincronizar cartera** para descubrir todos los UTXO y sus condiciones de gasto


5. **Comprobar la expiración del bloqueo de tiempo**: el software indicará para cada UTXO si la ruta de recuperación está activa


6. **Crear la transacción de recuperación** a una dirección controlada únicamente por el heredero (idealmente un nuevo wallet único)


7. **Firmar y difundir** la transacción en la red Bitcoin



Si el bloqueo temporal aún no ha expirado, el heredero tendrá que esperar. El software mostrará la fecha o el bloque a partir del cual será posible la recuperación. Durante este periodo de espera, los fondos permanecen seguros en la blockchain.



### Puntos a vigilar para el heredero



El heredero debe prestar especial atención a :




- Comprobar la autenticidad del software descargado** (sumas de comprobación, firmas)
- Nunca compartas tu frase de recuperación** con nadie que te ofrezca ayuda
- Consulta al menos a dos personas de confianza** antes de llevar a cabo la recuperación
- Transferir los fondos a una cartera simple** que controle completamente tras la recuperación



## Buenas prácticas



### Separación de la información



Nunca almacene toda la información en un mismo lugar. El descriptor debe estar separado de las frases de recuperación, que a su vez están separadas de los códigos PIN. Esta distribución complica el acceso a un atacante al tiempo que sigue siendo reconstituible por sus herederos legítimos.



### Pruebas de recuperación



Antes de depositar fondos importantes, pruebe todo el proceso de recuperación con una pequeña cantidad. Verifique que puede restaurar la cartera a partir del descriptor y las frases de recuperación en un dispositivo en blanco. Documente los pasos para sus herederos.



### Mantenimiento Timelock



Planifique la renovación de sus marcas de tiempo mucho antes de que caduquen. Para un reloj de 12 meses, realice una transacción cada 9-10 meses. Los programas informáticos suelen ofrecer recordatorios o funciones de actualización automática.



### Actualización del plan



La configuración de su Bitcoin evoluciona. Cada cambio significativo (nueva cartera, modificación de plazos, adición de heredero) debe reflejarse en su documentación. Establezca una rutina de revisión anual.



## Elección del enfoque



La elección entre las distintas soluciones depende de su perfil técnico y de sus necesidades específicas.



**Liana** es adecuado para usuarios de sobremesa que prefieren un software de código abierto con control total a través de su propio nodo. La configuración sigue siendo accesible gracias a la interfaz guiada. Los calendarios relativos (CSV) simplifican el mantenimiento, ya que su actividad normal retrasa automáticamente los plazos. Limitación: retraso máximo de unos 15 meses (65535 bloques).



**Bitcoin Keeper** se dirige a usuarios de móviles que buscan una interfaz intuitiva con documentos de acompañamiento integrados. La aplicación ofrece dos tipos de clave especial: la Clave de Herencia (que se suma al quórum) y la Clave de Emergencia (que lo omite por completo). Las llaves absolutas (CLTV) permiten plazos superiores a 15 meses, con una función de revalidación integrada que simplifica la renovación. El plan Diamond Hands desbloquea funciones heredadas avanzadas.



**La herencia** está dirigida a usuarios técnicos que aprecian la confidencialidad de Taproot y la herencia jerárquica con retardos progresivos. La estructura de árbol de Taproot oculta las condiciones de herencia durante las transacciones normales, revelando únicamente la condición utilizada durante la recuperación.



Las tres soluciones tienen algo en común: requieren un refresco periódico para evitar la activación prematura de las rutas de recuperación. Esta limitación es a la vez el precio y la garantía del legado no fiable de on-chain. Programe recordatorios periódicos y convierta este mantenimiento en parte de su rutina de gestión de Bitcoin.



## Conclusión



Un plan técnico heredado de Bitcoin combina mecanismos criptográficos (timelocks, Miniscript, Taproot) con una documentación rigurosa. Los monederos avanzados permiten transmitir tus bitcoins automáticamente tras un periodo de inactividad, sin intervención de terceros.



Los elementos críticos que debes transmitir a tus herederos son: el descriptor o archivo de configuración, su frase de recuperación, instrucciones detalladas de recuperación y datos de contacto de personas competentes que puedan ayudarles.



Empiece por elegir una solución técnica adaptada a su perfil, pruébela con una pequeña cantidad y, a continuación, documente el conjunto en un plan estructurado. La complejidad inicial garantiza que tus activos Bitcoin pasarán a ser de total confianza.



## Recursos



### Modelo de plan de sucesión





- [Plantilla del plan de sucesión Bitcoin (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Plantilla de documentación Plan ₿ Network



### Referencias técnicas





- [BIP-65 : OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Especificación de relojes absolutos (CLTV)
- [BIP-112 : OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Especificación de relojes relativos (CSV)
- [Miniscript Reference](https://bitcoin.sipa.be/miniscript/) - Documentación oficial de Miniscript por Pieter Wuille



### Sitios web oficiales de soluciones





- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper](https://bitcoinkeeper.app/) - Bithyve
- [Herencia Wallet](https://btc-heritage.com/) - Crypto7