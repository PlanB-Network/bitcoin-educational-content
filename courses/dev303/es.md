---
name: Aprendizaje de Rust con Bitcoin
goal: Mejore sus conocimientos de desarrollo en Rust mediante la codificación de Bitcoin
objectives: 

  - Acostúmbrese al lenguaje Rust
  - Entender por qué utilizar Rust para desarrollar Bitcoin
  - Obtenga la base del SDK de Lightning

---

# Una expedición a Rust para constructores Bitcoin

En este curso práctico, que se filmó durante un seminario organizado por Fulgur' Ventures en octubre de 2023, desarrollarás tus habilidades de Rust construyendo componentes y miniproyectos reales centrados en Bitcoin. Cubriremos los fundamentos de Rust, por qué se utiliza Rust para el desarrollo de Bitcoin (seguridad de memoria, rendimiento y concurrencia segura) y cómo empezar con el SDK de Lightning para crear funciones de pago.

A lo largo de los capítulos, practicarás los patrones básicos de Rust (propiedad, tiempos de vida, rasgos, async), trabajarás con primitivas de Bitcoin (claves, transacciones, secuencias de comandos) e integrarás progresivamente conceptos de Lightning (nodos, canales, facturas).

No es estrictamente necesario tener conocimientos previos de Rust o Bitcoin, aunque es útil estar familiarizado con la programación básica. El curso está pensado para principiantes, pero es lo bastante práctico para ingenieros que se pasen a Bitcoin.

+++

# Introducción

<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>

## Resumen del curso

<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>

**Introducción**

Bienvenido a este curso de programación para principiantes sobre SDKs. En esta formación, aprenderá los conceptos básicos de Rust, luego se centrará en Rust aplicado a la programación Bitcoin, y terminará con algunos casos de uso utilizando SDKs.

Los vídeos de la formación estarán disponibles por ahora solo en inglés y formaron parte de un seminario en directo organizado el pasado mes de octubre en la Toscana por Fulgure Venture. Esta formación se centrará únicamente en la primera semana. La segunda mitad estaba dirigida a RGB y puede encontrarse en el curso RGB.

https://planb.academy/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

Esta formación te da la oportunidad de desarrollar tus habilidades de programación en Lightning Network utilizando Rust y varios SDKs. Está diseñado para desarrolladores con una sólida formación en programación que deseen sumergirse en el desarrollo específico de Lightning Network. Aprenderá los conceptos básicos de Rust, por qué es adecuado para el desarrollo de Bitcoin y, a continuación, pasará a la implementación práctica utilizando SDK especializados.

**Sección 2: Aprende a codificar con Rust**

En esta sección, descubrirás los fundamentos de Rust a través de una serie de capítulos progresivos. Aprenderás a escribir código en Rust, a entender sus especificidades y a dominar sus características esenciales a lo largo de siete partes detalladas. Este módulo es esencial para entender por qué Rust es el lenguaje favorito para el desarrollo de Bitcoin.

**Sección 3: Rust y Bitcoin**

Aquí exploraremos en profundidad por qué Rust es una opción relevante para el desarrollo de Bitcoin. Aprenderás sobre su modelo de error, la herramienta UniFFI y los rasgos asíncronos, todos ellos elementos clave para construir software robusto y seguro.

**Sección 4: Desarrollo de LNP/BP con SDKs**

Aprenderás a desarrollar nodos LN utilizando varios SDKs como Breez SDK y Greenlight para Lipa. Verás cómo implementar aplicaciones Lightning Network utilizando librerías diseñadas para simplificar el desarrollo de Bitcoin y Lightning.

¿Listo para aumentar tus habilidades en Lightning Network con Rust? Vamos allá

# Aprenda a programar con el libro de Rust

<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>

## Introducción a Rust

<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>

<professorId>e7e63d59-ea19-4960-9446-61bd4dcc98f0</professorId>

:::video id=12a518cf-64be-43f1-b6d4-f6592a1324ea:::

### Instalación y gestión de Rust con Rustup

Al comenzar su viaje con Rust, el primer paso consiste en configurar un entorno de desarrollo adecuado. El método más recomendado para instalar Rust es Rustup, un sistema de gestión de cadenas de herramientas que gestiona la instalación y las actualizaciones en diferentes proyectos y plataformas.

Rustup sirve como algo más que un instalador, funciona como una herramienta de gestión integral para su entorno de desarrollo Rust. Con Rustup, puede instalar fácilmente objetivos de compilación adicionales para diferentes plataformas, como ARM64 para el desarrollo de Android u otras arquitecturas que pueda necesitar. La herramienta también gestiona las actualizaciones de Rust sin problemas, lo que es particularmente valioso dado que Rust lanza una nueva versión estable aproximadamente cada seis semanas. Cuando necesites actualizar a la última versión, un simple comando `rustup update` se encarga de todo automáticamente.

A la hora de instalar Rustup, conviene entender el modelo de seguridad implicado. El proceso de instalación descarga y se ejecuta un script desde el sitio web oficial de Rust a través de HTTPS, que proporciona seguridad criptográfica en la capa de transporte. Los paquetes descargados por Rustup y Cargo provienen de fuentes de confianza (crates.io y la infraestructura oficial de Rust) y se benefician del cifrado HTTPS. Aunque este enfoque es seguro para la mayoría de los escenarios de desarrollo, algunas organizaciones con políticas de seguridad estrictas pueden preferir instalar Rust a través del gestor de paquetes de su distribución de Linux, que proporciona una capa adicional de confianza a través de la propia infraestructura de firma de paquetes de la distribución. Para propósitos de aprendizaje y desarrollo general, Rustup es una herramienta bien establecida y de amplia confianza en el ecosistema Rust.

Para la mayoría de los escenarios de desarrollo, puedes instalar Rustup ejecutando el script de instalación proporcionado en el sitio web oficial de Rust. El instalador te pedirá que elijas entre diferentes opciones de toolchain (cadenas de herramientas), siendo el toolchain estable la opción recomendada para la mayoría de los usuarios. La instalación ocurre en tu directorio personal, no requiere privilegios de administrador, y configura todas las variables de entorno necesarias para su uso inmediato.

### Comprender las cadenas de herramientas (toolchains) y los componentes de Rust

El ecosistema de desarrollo de Rust consta de varios componentes clave que trabajan juntos para proporcionar un entorno de programación completo. Comprender estos componentes le ayudará a navegar por el proceso de desarrollo de Rust con mayor eficacia y a solucionar los problemas que puedan surgir.

El compilador de Rust, conocido como `rustc`, forma el núcleo de la cadena de herramientas de Rust. Aunque teóricamente podrías usar `rustc` directamente para compilar programas Rust, la mayor parte del trabajo de desarrollo se basa en Cargo, el gestor de paquetes y sistema de compilación de Rust. Cargo funciona de forma similar a npm en el ecosistema JavaScript, gestionando dependencias, coordinando compilaciones y proporcionando comandos convenientes para tareas de desarrollo comunes. Cuando ejecutas comandos como `cargo build` o `cargo run`, Cargo orquesta el proceso de compilación, maneja la resolución de dependencias y gestiona la estructura general del proyecto.

Clippy es un linter que analiza tu código y proporciona sugerencias para mejorarlo. A diferencia de los comprobadores básicos de sintaxis, Clippy entiende los modismos de Rust y puede recomendar formas más idiomáticas de realizar tareas específicas. Esta herramienta ayuda a aprender las mejores prácticas de Rust y a escribir código más fácil de mantener.

La cadena de herramientas de Rust también incluye completas herramientas de documentación y la documentación de la librería estándar, accesible a través de la página web oficial de documentación de Rust. Esta documentación sirve como referencia indispensable durante el desarrollo, proporcionando información detallada sobre las funciones, tipos y módulos de la librería estándar. La documentación incluye extensos ejemplos y explicaciones que le ayudarán a entender no solo lo que hacen las funciones, sino cómo utilizarlas eficazmente en sus programas.

Rust admite varios canales de publicación: estable, beta y nightly. El canal estable proporciona versiones probadas a fondo adecuadas para su uso en producción. El canal beta ofrece una vista previa de la próxima versión estable, utilizada principalmente para las pruebas finales antes del lanzamiento oficial. El canal nightly incluye características experimentales en desarrollo activo, que pueden ser útiles para probar nuevas capacidades de Rust, aunque estas características pueden cambiar o ser eliminadas en futuras versiones.

### Creación y gestión de proyectos Rust con Cargo

El desarrollo moderno de Rust se centra en Cargo, que agiliza la creación de proyectos, la gestión de dependencias y el proceso de compilación. En lugar de crear manualmente directorios y archivos, Cargo proporciona el comando `cargo new` para generar una estructura del proyecto completa con valores predeterminados sensibles.

Cuando creas un nuevo proyecto con `cargo new nombre_proyecto`, Cargo establece una estructura de directorios estándar, crea un archivo `main.rs` básico con un programa "¡Hola, mundo!", inicializa un repositorio Git y genera un archivo `Cargo.toml` para la configuración del proyecto. El archivo `Cargo.toml` sirve como punto central de configuración para tu proyecto, conteniendo metadatos sobre tu proyecto y listando todas las dependencias que requiere tu código.

Cargo proporciona varios comandos esenciales para el trabajo diario de desarrollo. El comando `cargo build` compila el proyecto y sus dependencias, creando archivos ejecutables en el directorio `target`. Para una rápida iteración durante el desarrollo, `cargo run` combina la compilación y la ejecución en un único paso. El comando `cargo check` realiza todas las comprobaciones de compilación sin generar el ejecutable final, lo que lo hace significativamente más rápido que una compilación completa cuando simplemente quieres verificar que tu código compila correctamente.

Al preparar el código para su despliegue en producción, la opción `--release` activa las optimizaciones y elimina las aserciones de depuración. Las compilaciones de lanzamiento se ejecutan más rápido y producen ejecutables más pequeños, pero tardan más en compilarse y eliminan información de depuración útil. El compilador aplica varias optimizaciones durante las compilaciones de lanzamiento y desactiva las comprobaciones en tiempo de ejecución, como la detección del desbordamiento de enteros, lo que mejora el rendimiento pero elimina algunas garantías de seguridad presentes en las compilaciones de depuración.

### Variables, mutabilidad y filosofía de seguridad en Rust

Rust adopta una aproximación diferente a la gestión de variables que la mayoría de los lenguajes. Por defecto, todas las variables en Rust son inmutables, lo que significa que sus valores no pueden ser cambiados después de la asignación inicial. Esta decisión de diseño tiene como objetivo evitar errores de programación comunes que surgen de cambios de estado inesperados.

Cuando declaras una variable usando `let x = 5`, esa variable se vuelve inmutable por defecto. Cualquier intento posterior de modificar su valor provocará un error de compilación. Este requisito de inmutabilidad obliga a los desarrolladores a pensar cuidadosamente cuándo son realmente necesarios los cambios de estado y hace que el comportamiento del código sea más predecible. Muchos errores de programación provienen de variables que cambian inesperadamente, y la inmutabilidad por defecto de Rust ayuda a prevenir estos problemas.

Cuando realmente necesites modificar el valor de una variable, Rust requiere una declaración explícita de mutabilidad usando la palabra clave `mut`: `let mut x = 5`. Esta declaración explícita sirve como una señal clara tanto para el compilador como para otros desarrolladores de que el valor de esta variable puede cambiar durante la ejecución del programa. El requisito de declarar explícitamente la mutabilidad anima a considerar detenidamente si la mutabilidad es realmente necesaria para cada variable.

Rust también soporta shadowing, que permite declarar una nueva variable con el mismo nombre que una variable anterior. A diferencia de la mutación, la sombra crea una variable completamente nueva que tiene el mismo nombre, ocultando así la variable anterior. Esta técnica resulta especialmente útil cuando se transforman datos a través de múltiples pasos, como el análisis sintáctico de una cadena en un número y su posterior procesamiento. Con el shadowing, puede mantener un nombre de variable consistente a lo largo del proceso de transformación mientras cambia el tipo de la variable en cada paso.

La distinción entre shadowing y mutación es importante cuando se consideran los cambios de tipo. Con shadowing, puedes cambiar tanto el valor como el tipo de una variable porque estás creando una nueva variable. Con la mutación, solo puedes cambiar el valor manteniendo el mismo tipo, ya que estás modificando una variable existente en lugar de crear una nueva.

```rust
// Shadowing: Creando nuevas variables con el mismo nombre
let amount = "100000";           // la cantidad es de tipo &str (cadena)
let amount = amount.parse::<u64>().unwrap();  // La canditad ahora es u64 (entero positivo)
let amount = amount * 100;       // La cantidad sigue siendo de tipo u64, pero con nuevo valor
// Mutación: Modificando la misma variable
let mut balance = 50000_u64;
balance = balance + amount;      // OK: Mismo tipo, Diferente valor
// balance = "vacío";            // ERROR: No se puede cambiar el tipo con mutación

// Ejemplo práctico: Procesando una entrada de cantidad de Bitcoin
let user_input = "  0.001 ";                    // &str con espacios en blanco
let user_input = user_input.trim();            // &str, espacios removidos
let satoshis: u64 = (user_input.parse::<f64>().unwrap() * 100_000_000.0) as u64;
println!("Cantidad en satoshis: {}", satoshis);  // 100000
```

### Tipos de datos y fundamentos del sistema de tipos

Rust implementa un sistema de tipos fuerte y estático donde cada valor debe tener un tipo bien definido y conocido en tiempo de compilación. Aunque esto puede parecer restrictivo comparado con lenguajes de tipado dinámico, las capacidades de inferencia de tipos de Rust significan que raramente necesitas especificar tipos explícitamente. El compilador normalmente puede determinar el tipo apropiado basándose en cómo se utiliza el valor.

Sin embargo, ciertas situaciones requieren anotaciones explícitas de tipo. Cuando se utilizan funciones genéricas como `parse()`, que pueden convertir cadenas en varios tipos numéricos, el compilador necesita saber qué tipo específico desea. En estos casos, se proporcionan anotaciones de tipo utilizando la sintaxis de dos puntos: `let adivinar: u32 = "42".parse().expect("¡No es un número!")`.

Los tipos escalares de Rust incluyen enteros, números en coma flotante, booleanos y caracteres. El sistema de tipos enteros proporciona un control preciso sobre el uso de memoria y las características de rendimiento. Los tipos enteros se nombran sistemáticamente: `i8`, `i16`, `i32`, `i64` y `i128` para los enteros con signo, y `u8`, `u16`, `u32`, `u64` y `u128` para los enteros positivos. Los números indican el ancho de bit, lo que aclara el uso de memoria y los rangos de valores.

Los tipos `isize` y `usize` merecen especial atención, ya que se adaptan a la arquitectura de destino. En sistemas de 64 bits, estos tipos tienen un ancho de 64 bits, mientras que en sistemas de 32 bits, tienen un ancho de 32 bits. Estos tipos se utilizan habitualmente para la indexación de matrices (arrays) y los desplazamientos de memoria, ya que coinciden con el tamaño natural de palabra de la arquitectura de destino, lo que permite una aritmética de punteros y operaciones de memoria eficientes.

Rust proporciona múltiples formas de escribir literales enteros, incluyendo los formatos decimal, hexadecimal (`0x`), octal (`0o`) y binario (`0b`). También puedes utilizar guiones bajos en cualquier lugar dentro de los literales numéricos para mejorar la legibilidad, como escribir `1_000_000` en lugar de `1000000`. Los guiones bajos no afectan al valor, pero pueden hacer más legibles los números grandes.

Los tipos de coma flotante en Rust son sencillos: `f32` para números de precisión simple y `f64` para números de coma flotante de doble precisión. El tipo `f64` se prefiere generalmente debido a su mayor precisión y al hecho de que los procesadores modernos a menudo pueden manejar operaciones de coma flotante de 64 bits tan eficientemente como las operaciones de 32 bits.

### Tipos compuestos y organización de datos

Además de los tipos escalares, Rust proporciona tipos compuestos que agrupan múltiples valores. Las tuplas permiten combinar valores de diferentes tipos en un único valor compuesto. Las tuplas se crean utilizando paréntesis y se puede especificar el tipo de cada elemento: `let tupla: (i32, f64, u8) = (500, 6.4, 1)`.

Las tuplas admiten la desestructuración, que permite extraer valores individuales: `let (x, y, z) = tup`. Esta sintaxis crea tres variables independientes a partir de los componentes de la tupla. También se puede acceder directamente a los elementos de la tupla utilizando la notación de puntos con el índice del elemento: `tup.0`, `tup.1`, `tup.2`.

```rust
// Creando una tupla con diferentes tipos
let transaction: (&str, u64, bool) = ("abc123", 50000, true);

// Desestructuración: extraer todos los valores a la vez
let (txid, amount, confirmed) = transaction;
println!("Transacción {} para {} sats", txid, amount);

// Notación de puntos: acceder a elementos individuales por índice
println!("Confirmed: {}", transaction.2);  // verdadero

// Ejemplo práctico: función que devuelve múltiples valores
fn parse_utxo(data: &str) -> (String, u32, u64) {
// Retorna (txid, output_index, value_in_sats)
("a]1b2c3".to_string(), 0, 100000)
}

let (txid, vout, value) = parse_utxo("raw_data");
println!("UTXO {}:{} = {} sats", txid, vout, value);
```

Las matrices en Rust difieren significativamente de las matrices o listas en muchos otros lenguajes porque tienen un tamaño fijo que se convierte en parte de su tipo. Una matriz de cinco enteros tiene el tipo `[i32; 5]`, donde el punto y coma separa el tipo de elemento de la longitud de la matriz. Esta información de tamaño a nivel de tipo permite al compilador realizar una comprobación de límites y garantiza que las funciones que reciben matrices sepan exactamente cuántos elementos esperar.

Puede inicializar matrices enumerando todos los elementos explícitamente: `[1, 2, 3, 4, 5]`, o utilizando una sintaxis abreviada para matrices con valores repetidos: `[3; 5]` crea una matriz de cinco elementos, todos con el valor de 3. Esta abreviatura es útil para inicializar buffers o crear matrices con valores por defecto.

El acceso a matrices utiliza la notación de corchetes como la mayoría de los lenguajes, pero Rust proporciona comprobación de límites tanto en tiempo de compilación como en tiempo de ejecución. Cuando accedes a una matriz con un índice constante que el compilador puede verificar, detectará accesos fuera de límites en tiempo de compilación. Para índices dinámicos determinados en tiempo de ejecución, Rust inserta comprobaciones de límites que causarán que el programa entre en pánico si intentas acceder a un índice inválido, previniendo violaciones de seguridad de memoria.

## Ownership y seguridad de la memoria en Rust

<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>

:::video id=8ed76bae-7c30-4aac-9f28-bb4cbb9180e4:::

### Entendiendo el enfoque único de Rust para la gestión de memoria

Este capítulo cubre uno de los conceptos más importantes de Rust. Mientras que los conceptos anteriores pueden haber parecido familiares a los programadores que vienen de otros lenguajes, esta propiedad es el enfoque de Rust para resolver la seguridad de memoria sin recolección de basura (garbage collector).

Rust se diseñó con el objetivo fundamental de evitar los errores relacionados con la memoria que afectan a lenguajes de bajo nivel como C y C++. Entre estos problemas se incluyen los errores de uso después de la liberación, por los que se accede a la memoria después de haberla liberado, y los desbordamientos de búfer, por los que los programas escriben fuera de los límites de la memoria asignada. Las soluciones tradicionales a estos problemas han implicado compromisos que Rust pretende eliminar. Los lenguajes de alto nivel como Java y Go resuelven la seguridad de la memoria mediante el garbage collector, en la que un proceso automático identifica y libera periódicamente la memoria no utilizada. Sin embargo, los garbage collector introducen una sobrecarga de rendimiento y pueden causar pausas impredecibles durante la ejecución del programa, lo que los hace inadecuados para la programación de sistemas en los que un rendimiento constante es fundamental.

Rust consigue la seguridad de memoria principalmente mediante el análisis estático realizado en tiempo de compilación. El compilador examina el código fuente y puede determinar si la mayoría de las operaciones de memoria son seguras sin necesidad de recurrir a la recolección de basura. Para los casos que no pueden verificarse estáticamente, como el acceso a matrices con índices calculados en tiempo de ejecución, Rust inserta comprobaciones de límites que provocan el pánico en lugar de permitir comportamientos indefinidos. Este enfoque difiere fundamentalmente de los analizadores estáticos disponibles para C y C++, que se adaptaron a lenguajes no diseñados originalmente para un análisis estático exhaustivo. La sintaxis y las reglas del lenguaje de Rust se diseñaron desde cero para permitir una amplia verificación en tiempo de compilación, garantizando que una vez que un programa se compila correctamente, se ejecute de forma segura o entre en pánico de forma predecible en lugar de mostrar un comportamiento indefinido.

### El sistema Ownership: Reglas y principios

La piedra angular de las garantías de seguridad de memoria de Rust es el sistema de propiedad, que gobierna cómo se gestiona la memoria a lo largo de la ejecución de un programa. Ownership se basa en tres reglas fundamentales que el compilador aplica en todo momento:

1. Cada valor en Rust tiene un propietario (una variable que contiene el valor)

2. solo puede haber un propietario a la vez

3. Cuando el propietario sale del ámbito de aplicación, se elimina el valor


Los ámbitos en Rust se definen normalmente mediante llaves, ya sea en cuerpos de funciones, bloques condicionales o bloques de ámbito creados explícitamente. Cuando se declara una variable dentro de un ámbito, ese ámbito se convierte en el propietario del valor de la variable. La variable permanece accesible y válida durante todo el tiempo de vida del ámbito, pero tan pronto como la ejecución abandona el ámbito, todas las variables de propiedad se limpian automáticamente a través de un proceso llamado dropping.

Esta limpieza automática se implementa a través del mecanismo drop de Rust, donde el lenguaje implícitamente llama a una función drop en variables que salen de ámbito. Para los tipos básicos, esto significa simplemente que la memoria se marca como disponible para su reutilización. Para tipos más complejos que gestionan recursos, las implementaciones de drop personalizadas pueden realizar operaciones de limpieza adicionales, como cerrar gestores de archivos o liberar conexiones de red. Este patrón, tomado de RAII (Resource Acquisition Is Initialization) de C++, garantiza que los recursos siempre se liberen correctamente sin necesidad de que el programador introduzca código de limpieza explícito.

### Traslado de Ownership y disposición de la memoria

Para entender cómo se transfiere la propiedad entre variables es necesario examinar la diferencia entre tipos simples y tipos complejos en términos de disposición de memoria y comportamiento de copia. Los tipos simples como enteros, booleanos y números de punto flotante tienen un tamaño fijo y conocido en tiempo de compilación y pueden ser copiados eficientemente. Cuando asignas una variable entera a otra, Rust crea una copia completa e independiente del valor, permitiendo que ambas variables existan simultáneamente sin problemas de propiedad.

Los tipos complejos como las cadenas presentan un reto diferente porque gestionan memoria asignada dinámicamente. Una cadena en Rust consta de tres componentes almacenados en la pila: un puntero a los datos de caracteres asignados al montón, la longitud actual de la cadena y la capacidad total del búfer asignado. Esta estructura permite que las cadenas crezcan y se encojan eficientemente manteniendo el conocimiento de sus límites. Cuando se asigna una variable "String" a otra, Rust se enfrenta a una elección: podría copiar solo la estructura basada en la pila (creando dos punteros a los mismos datos de la pila) o realizar una copia profunda de todos los datos de la pila.

El comportamiento por defecto de Rust es mover la propiedad en lugar de copiar, transfiriendo los datos del montón de la variable origen a la variable destino e invalidando la fuente. Este enfoque evita el peligroso escenario en el que múltiples variables podrían modificar la misma memoria del montón o en el que la misma memoria podría ser liberada múltiples veces cuando las variables salen del ámbito. La operación de movimiento es eficiente porque solo copia la pequeña estructura basada en la pila, no los datos de la pila potencialmente grandes, al tiempo que mantiene la seguridad de la memoria garantizando la propiedad única.

### Referencias y préstamos

Aunque los movimientos de propiedad proporcionan seguridad, pueden ser restrictivos cuando se necesita utilizar un valor en varios lugares sin transferir la propiedad. Rust soluciona esto mediante el préstamo, que permite a las funciones y variables acceder temporalmente a los datos sin tomar la propiedad. Una referencia, creada usando el operador ampersand, proporciona acceso de solo lectura a un valor mientras deja la propiedad con la variable original.

Las referencias permiten a las funciones operar con datos sin consumirlos, lo que hace posible utilizar el mismo valor varias veces a lo largo de un programa. Cuando pasas una referencia a una función, estás prestando los datos temporalmente, y la función debe devolver la referencia antes de que el propietario original pueda recuperar el control total. Esta metáfora del préstamo refleja la naturaleza temporal del acceso: del mismo modo que prestas un libro a un amigo sin perder la propiedad, las referencias permiten un acceso temporal sin perder la relación de propiedad original.

Las referencias mutables amplían este concepto para permitir la modificación de datos prestados, pero con restricciones estrictas para mantener la seguridad. Rust solo permite una referencia mutable a un dato en un momento dado, lo que evita las carreras de datos en las que varias partes de un programa pueden modificar simultáneamente la misma memoria. Además, no se pueden tener simultáneamente referencias mutables e inmutables a los mismos datos, ya que esto podría llevar a situaciones en las que el código asume que los datos son estables mientras otro código los está modificando activamente. Estas reglas se aplican en tiempo de compilación, lo que elimina clases enteras de errores de concurrencia que afectan a otros lenguajes de programación de sistemas.

```rust
fn main() {
let mut wallet_balance: u64 = 100_000; // 100,000 satoshis

// Préstamo inmutable: leer el balance
let balance_ref = &wallet_balance;
println!("Balance actual: {} sats", balance_ref);
// balance_ref queda fuera del alcance aquí

// Préstamo mutable: actualizar el balance
let balance_mut = &mut wallet_balance;
*balance_mut += 50_000; // Pago recibido
println!("Después del depósito: {} sats", balance_mut);
// balance_mut queda fuera del alcance aquí

// Función que toma prestado de forma inmutable
fn display_balance(balance: &u64) {
println!("Balance check: {} sats", balance);
}

// Función que toma prestado de forma mutable
fn deduct_fee(balance: &mut u64, fee: u64) {
*balance -= fee;
}

display_balance(&wallet_balance);
deduct_fee(&mut wallet_balance, 1_000);
println!("Después de la tarifa: {} sats", wallet_balance); // 149,000
}
```

### Tipos de cadenas y segmentos (slices)

Rust distingue entre literales de cadena y el tipo String, reflejando diferentes estrategias de gestión de memoria y casos de uso. Los literales de cadena se incrustan directamente en el binario compilado y tienen el tipo &str (string slice), que representa una vista en datos de cadena inmutables. Estos literales son eficientes porque no requieren asignación en tiempo de ejecución, pero no pueden modificarse ya que forman parte del código del programa.

El tipo String, por el contrario, gestiona la memoria asignada dinámicamente y puede crecer, decrecer y modificarse en tiempo de ejecución. Puede crear una cadena a partir de un literal utilizando String::from() o métodos similares, que asignan memoria al montón y copian el contenido del literal. Esta distinción permite a Rust optimizar tanto el rendimiento (usando literales cuando es posible) como la flexibilidad (usando String cuando se necesita modificar).

Los segmentos de cadena (&str) proporcionan una potente abstracción para trabajar con porciones de cadenas sin copiar datos. Una segmento (slice) contiene un puntero al inicio de los datos de la cadena y una longitud, lo que permite hacer referencia a subcadenas de forma eficaz. La sintaxis de los segmentos utiliza rangos (por ejemplo, &s[0..5]) para especificar a qué parte de la cadena se va a hacer referencia. Dado que los segmentos son referencias, están sujetos a reglas de préstamo que impiden que la cadena subyacente se modifique mientras existan segmentos. Esta aplicación en tiempo de compilación evita errores comunes como el acceso a memoria no válida después de que la cadena original haya sido liberada o modificada.

### Matrices, vectores y segmentos genéricos

El concepto de segmento se extiende más allá de las cadenas a cualquier secuencia de elementos, proporcionando una forma unificada de trabajar tanto con matrices de tamaño fijo como con vectores dinámicos. Las matrices en Rust tienen su longitud codificada en su tipo (por ejemplo, [i32; 5] para una matriz de cinco enteros de 32 bits), lo que las hace adecuadas para situaciones que requieren garantías de tamaño en tiempo de compilación. Las funciones que aceptan matrices pueden imponer requisitos de longitud exacta, útiles para operaciones como las funciones criptográficas que necesitan entradas de tamaño preciso.

Los segmentos (&[T]) ofrecen una alternativa más flexible, ya que representan una vista de cualquier secuencia contigua de elementos, independientemente del almacenamiento subyacente. Se pueden crear segmentos a partir de matrices, vectores u otras segmentos, y el mismo segmento puede hacer referencia a diferentes porciones de datos a lo largo de su vida. Esta flexibilidad hace que los segmentos sean ideales para funciones que necesitan procesar secuencias sin preocuparse por el mecanismo de almacenamiento específico o el tamaño exacto.

La relación entre los tipos propios (String, Vec<T>) y sus homólogos prestados (&str, &[T]) sigue un patrón consistente en Rust. Los tipos propios gestionan su memoria y pueden modificarse, mientras que los segmentos proporcionan un acceso de lectura eficiente a porciones de esos datos. Los tipos propios gestionan su memoria y pueden ser modificados, mientras que los segmentos proporcionan un acceso eficiente de solo lectura a porciones de esos datos. Este diseño permite APIs que son a la vez flexibles (aceptando varios tipos de entrada a través de segmentos) y eficientes (evitando copias innecesarias), mientras se mantienen las garantías de seguridad de Rust a través del sistema de préstamo.

## Estructuras, construcción de tipos de datos complejos

<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>

:::video id=c78a543f-1462-43a1-9845-889d310d31a4:::

Las estructuras en Rust sirven como base para la creación de tipos de datos complejos, similares a las clases en otros lenguajes de programación. Permiten agrupar datos relacionados en una única unidad cohesiva que puede contener múltiples campos de diferentes tipos. La sintaxis para definir una estructura sigue un patrón sencillo: se utiliza la palabra clave `struct` seguida del nombre de la estructura, luego se definen los campos entre llaves utilizando una sintaxis de dos puntos para especificar el tipo de cada campo.

Rust sigue unas convenciones de nomenclatura específicas para las estructuras que el compilador aplicará mediante advertencias. Los nombres de las estructuras deben usar CamelCase (también conocido como PascalCase), mientras que los nombres de los campos dentro de la estructura deben usar snake_case con guiones bajos. Esta convención ayuda a mantener la consistencia entre las bases de código de Rust y hace que el código sea más legible para otros desarrolladores.

Para crear instancias de estructuras es necesario especificar los valores de todos los campos utilizando el nombre de la estructura seguido de llaves que contengan las asignaciones de los campos. Una vez que tienes una instancia de estructura, puedes acceder y modificar campos individuales usando la notación de puntos, siempre que la instancia esté declarada como mutable. Esta notación de puntos funciona de forma consistente en Rust, a diferencia de lenguajes como C++ donde se pueden utilizar diferentes operadores para punteros y objetos directos.

### Funciones del constructor y atajos de campo

Rust no tiene constructores incorporados como algunos lenguajes orientados a objetos, pero puedes crear funciones que devuelvan instancias de estructuras para servir al mismo propósito. Estas funciones constructoras típicamente toman parámetros para algunos o todos los campos y pueden establecer valores por defecto para otros. Cuando se escriben estas funciones, Rust proporciona una abreviatura conveniente: si un parámetro tiene el mismo nombre que un campo de estructura, puede simplemente escribir el nombre del campo una vez en lugar de repetirlo en el formato `field: value`.

Las instancias de estructura también pueden crearse copiando valores de instancias existentes mediante la sintaxis de actualización de estructura. Esta característica le permite crear una nueva instancia especificando solo los campos que desea cambiar, con todos los demás campos copiados de una instancia existente. Sin embargo, esta operación sigue las reglas de propiedad de Rust, lo que significa que los tipos no copiados se moverán de la instancia fuente, haciendo potencialmente inutilizables partes de la instancia original después. El compilador rastrea estos movimientos parciales de forma inteligente, permitiéndote continuar usando los campos que no fueron movidos mientras previene el acceso a los campos movidos.

### Estructuras de tupla y estructuras unitarias

Rust soporta estructuras de tupla, que son estructuras con campos sin nombre a los que se accede por índice en lugar de por nombre. Son útiles para tipos envolventes simples o cuando necesitas una estructura pero no necesitas campos con nombre. Para acceder a los campos de una estructura de tupla se utiliza la notación con puntos seguida del índice del campo, por ejemplo `.0` para el primer campo, `.1` para el segundo, etcétera. Este método es adecuado para estructuras que contienen un único valor o unos pocos valores estrechamente relacionados, en las que los nombres pueden ser redundantes.

Las estructuras unitarias representan la forma más simple de estructuras: no contienen ningún dato. Aunque esto puede parecer inútil inicialmente, las estructuras unitarias se vuelven valiosas cuando se trabaja con el sistema de rasgos de Rust, ya que pueden implementar comportamientos sin almacenar ningún dato. Estas estructuras vacías sirven como marcadores o marcadores de posición en patrones más avanzados de Rust.

### Métodos y funciones asociadas

Las estructuras adquieren funcionalidad adicional cuando se añade comportamiento a través de bloques de implementación. Utilizando la palabra clave `impl` seguida del nombre de la estructura, puedes definir métodos que operen sobre instancias de tu estructura. Los métodos son funciones que toman `self` como primer parámetro, que puede ser un valor propio (`self`), una referencia inmutable (`&self`), o una referencia mutable (`&mut self`), dependiendo de lo que el método necesite hacer con la instancia.

La elección del tipo de parámetro `self` determina el comportamiento del método con respecto a la propiedad. Los métodos que toman `&self` pueden leer de la instancia sin tomar la propiedad, lo que los hace adecuados para operaciones que no modifican la estructura. Los métodos que toman `&mut self` pueden modificar la instancia mientras que permiten que la persona que llama conserve la propiedad. Los métodos que toman `self` por valor consumen la instancia, lo que es apropiado para operaciones que transforman la estructura en otra cosa o cuando el método representa la operación final sobre esa instancia.

Las funciones asociadas son funciones definidas dentro de un bloque de implementación que no toman `self` como parámetro. Son similares a los métodos estáticos de otros lenguajes y se suelen utilizar como constructores o funciones de utilidad relacionadas con el tipo. Las funciones asociadas se llaman utilizando la sintaxis de dos puntos dobles (`Tipo::nombre_funcion()`), que las distingue claramente de los métodos llamados sobre instancias.

```rust
// Definir una estructura para una factura lightning
struct Invoice {
payment_hash: String,
amount_msat: u64,
description: String,
expiry_secs: u32,
}
impl Invoice {
// Asociar la función (constructor) - sin el parámetro self
fn new(payment_hash: String, amount_msat: u64, description: String) -> Self {
Invoice {
payment_hash,
amount_msat,
description,
expiry_secs: 3600, // por defecto 1 hora
}
}

// Método con &self - acceso de solo lectura
fn amount_sats(&self) -> u64 {
self.amount_msat / 1000
}

// Método con &mut self - Puede modificar la instancia
fn extend_expiry(&mut self, additional_secs: u32) {
self.expiry_secs += additional_secs;
}

// Método con self - consume la instancia
fn into_payment_request(self) -> String {
format!("lnbc{}n1p{}", self.amount_msat, self.payment_hash)
}
}

fn main() {
// Utilice la función asociada para crear una instancia
let mut invoice = Invoice::new(
"abc123".to_string(),
100_000_000, // 100,000 sats en milisats
"Pago de café".to_string(),
);

println!("Amount: {} sats", invoice.amount_sats());
invoice.extend_expiry(1800); // agregar 30 minutos

let request = invoice.into_payment_request();
// La factura ya está consumida y ya no se puede utilizar.
println!("Payment request: {}", request);
}
```

#### Enumeraciones: Modelado de opciones y variantes

Las enumeraciones en Rust tienen más capacidades que las enumeraciones en muchos otros lenguajes. Aunque pueden representar simples conjuntos de constantes con nombre, las enumeraciones de Rust también pueden contener datos dentro de cada variante, lo que las hace adecuadas para modelar situaciones en las que un valor puede ser uno de varios tipos o estados diferentes. Cada variante de enum puede contener diferentes tipos y cantidades de datos, desde ningún dato hasta estructuras complejas con campos con nombre.

La posibilidad de adjuntar datos a las variantes enum elimina muchos errores de programación habituales en otros lenguajes. En lugar de mantener variables separadas para un indicador de tipo y los datos asociados, que pueden ser fácilmente incoherentes, las enumeraciones de Rust agrupan la información de tipo con los propios datos. Este diseño garantiza que los datos siempre coincidan con la variante, evitando desajustes que podrían provocar errores en tiempo de ejecución.

Las variantes de los enum pueden contener datos de varias formas: sin datos para indicadores simples, datos tipo tupla para campos sin nombre o datos tipo estructura con campos con nombre. Incluso se pueden mezclar estos estilos dentro de un mismo enum, eligiendo la forma más adecuada para cada variante. Esta flexibilidad hace que los enums sean adecuados para modelar conceptos de dominio complejos en los que distintos casos requieren información diferente.

#### El tipo de opción: Gestionar las ausencias con seguridad

Uno de los enums más importantes de Rust es `Option<T>`, que representa valores que pueden o no estar presentes. Este enum tiene dos variantes: `Some(T)` que contiene un valor de tipo T, y `None` que representa la ausencia de un valor. El tipo Option sirve como solución de Rust a los problemas de punteros nulos que afectan a muchos otros lenguajes, obligando a los desarrolladores a manejar explícitamente los casos en los que pueden faltar valores.

El uso de los tipos Option hace que su código sea más robusto porque el compilador requiere que usted maneje tanto la presencia como la ausencia de valores. No puede utilizar accidentalmente un valor potencialmente ausente sin comprobar primero si existe. Este manejo explícito evita excepciones de puntero nulo y errores de ejecución similares que son fuentes comunes de errores en otros lenguajes de programación.

El tipo Option se integra con el sistema de concordancia de patrones de Rust, permitiéndole manejar ambos casos. Métodos como `unwrap_or()` proporcionan formas convenientes de extraer valores con valores por defecto, mientras que métodos como `map()` y `and_then()` permiten patrones de programación funcional para trabajar con valores opcionales.

### Coincidencia de patrones con expresiones coincidentes

La concordancia de patrones mediante expresiones `match` proporciona una forma de trabajar con enums y otros tipos de datos. Una expresión de coincidencia examina un valor y ejecuta código diferente en función del patrón con el que coincida el valor. Cada patrón puede desestructurar el valor coincidente, vinculando partes del mismo a variables que pueden utilizarse en el bloque de código correspondiente.

Las expresiones de coincidencia deben ser exhaustivas, lo que significa que deben tratar todos los casos posibles para el tipo de coincidencia. Este requisito evita errores que podrían producirse si algunos casos quedaran accidentalmente sin tratar. Si no desea tratar todos los casos explícitamente, puede utilizar el patrón comodín (`_`) para capturar todos los casos restantes, o vincular los casos no tratados a una variable si necesita acceder al valor.

La construcción `if let` proporciona una alternativa más concisa a match cuando solo le interesa un patrón específico. Esta sintaxis es particularmente útil cuando se trabaja con tipos Option o cuando se desea ejecutar código solo si un valor coincide con una variante particular de un enum. La construcción `if let` puede incluir una cláusula `else` para los casos en los que el patrón no coincida, lo que la convierte en una forma simplificada de manejar escenarios de coincidencia de patrones simples.

#### Colecciones: Gestión de grupos de datos

La biblioteca estándar de Rust proporciona varios tipos de colecciones para gestionar grupos de datos relacionados. Estas colecciones son genéricas, es decir, pueden almacenar elementos de cualquier tipo, y gestionan la memoria automáticamente. Las colecciones más utilizadas son los vectores para listas ordenadas, los mapas hash para asociaciones clave-valor y las cadenas para datos de texto.

#### Vectores: Matrices dinámicas

Los vectores representan matrices ampliables que pueden cambiar de tamaño durante la ejecución del programa. A diferencia de las matrices de tamaño fijo, los vectores asignan memoria en el montón y pueden ampliarse o reducirse según sea necesario. La creación de un vector suele requerir una anotación de tipo explícita cuando se comienza con un vector vacío, ya que el compilador necesita saber qué tipo de elementos contendrá el vector.

Los vectores proporcionan múltiples formas de acceder a los elementos, cada una con diferentes características de seguridad. La notación de índice (`vec[0]`) proporciona acceso directo pero entrará en pánico si el índice está fuera de los límites. El método `get()` devuelve una `Option`, permitiéndote manejar el acceso fuera de los límites con elegancia. La elección entre estos enfoques depende de si puedes garantizar que el índice es válido o si necesitas manejar posibles fallos.

Las reglas de préstamo de Rust se aplican a los vectores, evitando problemas comunes de seguridad de memoria. Si mantienes una referencia a un elemento del vector, no puedes modificar el vector hasta que esa referencia salga del ámbito. Esto evita situaciones en las que las referencias pueden apuntar a memoria desasignada después de operaciones vectoriales como introducir nuevos elementos o borrar el vector.

#### Mapas Hash: Almacenamiento clave-valor

Los mapas Hash proporcionan un almacenamiento clave-valor eficiente que permite buscar rápidamente valores en función de sus claves asociadas. Tanto las claves como los valores pueden ser de cualquier tipo, aunque las claves deben implementar los rasgos necesarios para hash y comparación de igualdad. Los mapas Hash se apropian de los valores insertados a menos que éstos implementen el rasgo "Copy".

Los mapas Hash ofrecen varios métodos para insertar y actualizar valores. El método básico `insert()` sobrescribirá los valores existentes, mientras que `entry()` proporciona una lógica de inserción más flexible. La entrada API permite insertar valores solo si no existen ya, o actualizar valores existentes basándose en su estado actual. Este API es útil para patrones como el recuento de ocurrencias o el mantenimiento de totales en ejecución.

Cuando se recuperan valores de mapas hash, el método `get()` devuelve una `Option` ya que la clave solicitada podría no existir. Puedes utilizar métodos como `copied()` para convertir de `Option<&T>` a `Option<T>` para los tipos Copy, y `unwrap_or()` para proporcionar valores por defecto cuando faltan claves.

### Manejo de cadenas y Unicode

Las cadenas en Rust están codificadas en UTF-8, lo que proporciona soporte completo para Unicode pero introduce complejidad en comparación con las cadenas simples de ASCII. El tipo `String` representa datos de texto propios y ampliables, mientras que los segmentos de cadena (`&str`) proporcionan vistas prestadas de los datos de cadena. Puede convertir entre estos tipos según sea necesario, con trozos de cadena a menudo utilizados para parámetros de función que aceptan tanto cadenas propias como literales de cadena.

La manipulación de cadenas incluye métodos para añadir texto, formatear múltiples valores juntos y extraer subcadenas. El método `push_str()` añade trozos de cadena sin tomar propiedad, mientras que la macro `format!` proporciona una forma flexible de construir cadenas a partir de múltiples componentes. Cuando trabaje con índices de cadenas, debe tener cuidado de respetar los límites de caracteres UTF-8 para evitar pánicos en tiempo de ejecución.

Para un procesamiento seguro carácter a carácter, las cadenas proporcionan métodos iteradores como `chars()` para valores escalares Unicode y `bytes()` para acceso a bytes sin procesar. Estos iteradores manejan correctamente la codificación UTF-8, asegurando que no se dividan accidentalmente caracteres multibyte. Este enfoque es más seguro y fiable que la indexación manual, especialmente cuando se trabaja con texto internacional que puede contener caracteres Unicode complejos.

## Sistema de gestión de errores de dos categorías de Rust

<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>

:::video id=0f2f6f68-52ca-474f-a64f-ba61cdc92821:::

Rust adopta un enfoque fundamentalmente diferente para el manejo de errores en comparación con la mayoría de los lenguajes de programación. Mientras que muchos lenguajes se basan principalmente en excepciones, Rust distingue entre dos categorías distintas de errores y proporciona mecanismos específicos para manejar cada tipo. Este capítulo explora el completo sistema de manejo de errores de Rust, cubriendo tanto los errores irrecuperables que terminan la ejecución del programa como los errores recuperables que permiten que los programas continúen ejecutándose con gracia.

### Errores irrecuperables y pánico

Los errores irrecuperables representan situaciones en las que el programa ha entrado en un estado inconsistente o inesperado del que no puede recuperarse con seguridad. Esto incluye escenarios como acceder a un array fuera de los límites, intentar operaciones que violan la seguridad de la memoria, o encontrar condiciones que indican errores lógicos fundamentales del programa. Cuando estos errores ocurren, la respuesta apropiada es terminar el programa inmediatamente en lugar de arriesgarse a más corrupción o comportamiento indefinido.

En Rust, los errores irrecuperables desencadenan un pánico, que hace que el programa se bloquee de forma controlada. Antes de terminar, Rust realiza un proceso llamado desenrollado, en el que recorre la pila de llamadas para proporcionar un seguimiento detallado de la pila que muestra exactamente dónde se produjo el pánico. Este proceso de desenrollado ayuda a los desarrolladores a identificar el origen del problema durante la depuración. Para aplicaciones de rendimiento crítico o sistemas embebidos, puede desactivar el desenrollado y configurar Rust para abortar inmediatamente cuando se produce un pánico, aunque esto sacrifica la información de depuración para una terminación más rápida.

Puede provocar un pánico explícitamente utilizando la macro `panic!` con un mensaje personalizado. Cuando ocurre un pánico, verás una salida indicando qué hebra entró en pánico y el mensaje asociado. Establecer la variable de entorno `RUST_BACKTRACE` proporciona información de depuración adicional, mostrando la pila de llamadas completa que condujo al pánico. Por ejemplo, si se intenta acceder al elemento 99 de un vector que contiene solo tres elementos, provocará un pánico con el mensaje "index out of bounds", junto con un backtrace que muestra la secuencia exacta de llamadas a funciones que provocaron el error.

### Errores recuperables con resultado

Los errores recuperables representan condiciones de fallo esperadas que los programas pueden manejar con elegancia sin terminar. Algunos ejemplos son el intento de abrir un archivo que no existe, fallos en la conexión de red o entradas de usuario no válidas. Para estas situaciones, Rust proporciona el enum `Result`, que representa explícitamente las operaciones que pueden fallar y obliga a los desarrolladores a manejar tanto los casos de éxito como de fracaso.

El enum `Result` se define con dos variantes: `Ok(T)` para operaciones con éxito que contienen un valor de tipo `T`, y `Err(E)` para fallos que contienen un error de tipo `E`. Este diseño utiliza el sistema de tipos de Rust para asegurar que los fallos potenciales no pueden ser ignorados. Las funciones que pueden fallar devuelven un `Resultado`, y el código de llamada debe manejar explícitamente tanto el caso de éxito como el de error, normalmente utilizando la concordancia de patrones con expresiones `match`.

Consideremos la función `File::open`, que devuelve un `Resultado<File, std::io::Error>`. Al abrir un fichero, recibes un objeto `File` si la operación se realiza correctamente o un `std::io::Error` si la operación falla. Puedes comparar estos resultados para manejar cada caso de forma apropiada. En el caso de éxito, puede continuar con las operaciones de archivo, mientras que en el caso de error, puede intentar crear el archivo, intentar un enfoque alternativo, o propagar el error al código de llamada. Este manejo explícito asegura que su programa tome decisiones conscientes sobre la recuperación de errores en lugar de bloquearse inesperadamente.

### Patrones y atajos para el tratamiento de errores

Mientras que la concordancia explícita de patrones proporciona un control completo sobre el manejo de errores, Rust ofrece varios métodos convenientes para el manejo de patrones de error comunes. El método `unwrap` extrae el valor de éxito de un `Result` pero entra en pánico si se produce un error, por lo que es útil para la creación rápida de prototipos o situaciones en las que está seguro de que una operación tendrá éxito. El método `expect` funciona de forma similar pero te permite proporcionar un mensaje de pánico personalizado, facilitando la depuración cuando las cosas van mal.

Para una gestión de errores más flexible, métodos como `unwrap_or_else` permiten proporcionar un cierre que se ejecuta cuando se produce un error, permitiendo una lógica de recuperación personalizada. Puedes encadenar estas operaciones para manejar escenarios complejos, como intentar abrir un archivo y crearlo si no existe, con diferentes estrategias de gestión de errores para cada paso.

El operador de signo de interrogación (`?`) proporciona una sintaxis concisa para la propagación de errores, que es común en los programas Rust. Cuando se añade `?` a un `Resultado`, automáticamente desenvuelve los valores correctos y devuelve los errores inmediatamente desde la función actual. Este operador solo puede usarse en funciones que devuelvan tipos `Result`, asegurando que los errores puedan propagarse adecuadamente por la pila de llamadas. El operador `?` hace que el código de gestión de errores sea mucho más legible, ya que elimina las expresiones de coincidencia prolijas y mantiene la semántica explícita de propagación de errores.

```rust
use std::fs::File;
use std::io::{self, Read};

// Tipo de error personalizado para operaciones de billetera
#[derive(Debug)]
enum WalletError {
FileNotFound,
InvalidFormat,
InsufficientFunds,
}

// Función que devuelve el resultado en caso de errores recuperables
fn load_wallet_balance(path: &str) -> Result<u64, WalletError> {
// Simular la lectura de un archivo
let balance_str = "150000"; // Normalmente leería desde el archivo
balance_str
.parse::<u64>()
.map_err(|_| WalletError::InvalidFormat)
}

// Usando el operador ? para una propogración de eror limpia
fn send_payment(amount: u64) -> Result<String, WalletError> {
let balance = load_wallet_balance("wallet.dat")?; // Propaga el error si falla
if balance < amount {
return Err(WalletError::InsufficientFunds);
}

Ok(format!("Enviar {} sats, restantes: {}", amount, balance - amount))
}

fn main() {
// Manejar el resultado explícitamente
match send_payment(50_000) {
Ok(msg) => println!("Éxito: {}", msg),
Err(WalletError::InsufficientFunds) => println!("Error: Fondos insuficientes"),
Err(WalletError::FileNotFound) => println!("Error: Archivo de wallet no encontrado"),
Err(WalletError::InvalidFormat) => println!("Error: archivo de billetera dañado"),
}

// O utiliza unwrap_or_else para una alternativa personalizada
let result = send_payment(200_000)
.unwrap_or_else(|e| format!("Payment failed: {:?}", e));
println!("{}", result);
}
```

### Propagación de errores y diseño de funciones

La propagación de errores es un concepto fundamental en el manejo de errores de Rust, que permite a las funciones pasar errores a la pila de llamadas en lugar de manejarlos localmente. Cuando diseñes funciones que puedan fallar, deberías devolver tipos `Result` para dar a los que llaman la flexibilidad de decidir cómo manejar los errores. Este enfoque promueve el manejo componible de errores donde cada función en la cadena de llamada puede manejar los errores localmente o pasarlos a código de nivel superior que tiene más contexto para tomar decisiones de recuperación.

El operador interrogación simplifica la propagación de errores. En lugar de escribir verborreicas expresiones de coincidencia para cada operación potencialmente fallida, puedes encadenar operaciones con operadores `?`, creando código legible que maneja la ruta de éxito mientras propaga automáticamente cualquier error que se produzca. Este patrón es tan común que muchas funciones de Rust están diseñadas específicamente para trabajar bien con el operador `?`, permitiendo un manejo fluido de los errores en toda su base de código.

Al decidir entre entrar en pánico o devolver errores, considere si el código de llamada puede recuperarse razonablemente del fallo. Si un fallo representa un error de programación o un estado irrecuperable del sistema, es apropiado entrar en pánico. Sin embargo, si el fallo es una condición esperada que el código de llamada podría manejar de manera diferente dependiendo del contexto, devolver un `Result` proporciona una mejor flexibilidad y composibilidad.

### Buenas prácticas y consideraciones de diseño

El manejo efectivo de errores en Rust requiere una consideración cuidadosa de cuándo entrar en pánico y cuándo devolver errores. Usa pánicos para situaciones que representen errores de programación o estados que nunca deberían ocurrir en programas correctos, como acceder a datos codificados que sabes que son válidos. Por ejemplo, el análisis de una cadena de direcciones IP codificada que se ha verificado que es correcta puede utilizar con seguridad `expect` con un mensaje descriptivo que explique por qué la operación nunca debería fallar.

Para las entradas controladas por el usuario o las interacciones con sistemas externos, prefiera siempre devolver tipos `Result` en lugar de entrar en pánico. Los usuarios cometen errores, los archivos se borran y las conexiones de red fallan - estas son condiciones normales que los programas bien diseñados deben manejar con gracia. Al devolver errores en estas situaciones, permites que el código de llamada implemente estrategias de recuperación apropiadas, ya sea pidiendo al usuario una entrada diferente, volviendo a los valores por defecto o mostrando mensajes de error útiles.

Considere la posibilidad de crear tipos personalizados que impongan la validación en el momento de la construcción para evitar que los estados no válidos se propaguen a través de su programa. Por ejemplo, si su programa requiere números dentro de un rango específico, cree un tipo envolvente que valide la entrada durante la construcción y no proporcione ninguna forma de crear instancias no válidas. Este enfoque utiliza el sistema de tipos de Rust para eliminar clases enteras de errores al hacer que los estados no válidos sean irrepresentables, reduciendo la necesidad de comprobación de errores en tiempo de ejecución en toda la base de código.

## Funciones de programación funcional, cierres y punteros inteligentes

<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>

:::video id=5514da77-5b71-4763-96b8-49eb21291c2b:::

Aunque Rust no es un lenguaje de programación funcional puro, incorpora características inspiradas en paradigmas de programación funcional. Estas características permiten a los desarrolladores escribir código conciso aprovechando conceptos como cierres e iteradores. Rust incluye estos elementos funcionales para proporcionar herramientas flexibles de procesamiento de datos y mecanismos de devolución de llamada.

Las características de programación funcional de Rust mantienen los principios básicos del lenguaje de seguridad de memoria y abstracciones de coste cero. Cuando se utilizan cierres e iteradores, no se sacrifica rendimiento por expresividad: el compilador de Rust optimiza estas construcciones para producir código máquina eficiente comparable a los enfoques tradicionales basados en bucles.

### Comprender los cierres

Los cierres en Rust son funciones anónimas que pueden capturar variables de su entorno. En otros lenguajes de programación, a menudo se denominan funciones lambda. La característica clave de los cierres es su capacidad para "cerrar" su entorno, lo que significa que pueden acceder y utilizar variables que existen en el ámbito en el que se define el cierre.

La sintaxis de los cierres utiliza caracteres de tubo (`|`) en lugar de paréntesis para definir los parámetros. Para un cierre sin parámetros, se escribe `||`, y para cierres con parámetros, se enumeran entre los tubos como `|x, y|`. Si el cuerpo del cierre consiste en una única expresión, puedes omitir las llaves, haciendo la sintaxis muy concisa.

Consideremos este ejemplo práctico de una empresa de camisetas que regala camisetas exclusivas en función de las preferencias de los clientes. Si un cliente ha especificado un color favorito, recibe ese color; de lo contrario, recibe el color más surtido por defecto. Usando cierres, esta lógica se convierte en: `user_preference.unwrap_or_else(|| self.most_stocked())`. El cierre `|| self.most_stocked()` proporciona el valor por defecto solo cuando es necesario, y puede acceder a `self` desde su entorno.

### Inferencia y flexibilidad del tipo de cierre

Una de las características más convenientes de Rust con los cierres es la inferencia automática de tipos. A diferencia de las funciones normales, en las que hay que especificar explícitamente los tipos de los parámetros y los tipos de retorno, los cierres a menudo pueden inferir estos tipos a partir del contexto. El compilador analiza cómo se utiliza el cierre y determina los tipos apropiados automáticamente. Sin embargo, una vez que un cierre es llamado con tipos específicos, esos tipos se vuelven fijos para esa instancia de cierre.

Puedes almacenar cierres en variables como cualquier otro valor, lo que los convierte en ciudadanos de primera clase en el lenguaje. Cuando asignas un cierre a una variable, puedes llamarlo más tarde usando paréntesis: `let mi_cierre = |x| x + 1; let resultado = mi_cierre(5);`. Esta flexibilidad te permite pasar cierres como argumentos a funciones, devolverlos de funciones y usarlos en estructuras de datos.

Si el compilador no puede deducir los tipos o si desea ser explícito, puede anotar los parámetros de cierre y los tipos de retorno utilizando una sintaxis similar a la de las funciones: `|x: i32| -> i32 { x + 1 }`. Esta tipificación explícita es a veces necesaria en situaciones complejas en las que el compilador necesita información adicional para resolver los tipos correctamente.

### Captura de variables de entorno

Los cierres pueden capturar variables de su entorno de tres formas diferentes: por referencia inmutable, por referencia mutable, o tomando propiedad. El compilador Rust determina automáticamente el método de captura más restrictivo que satisfaga las necesidades de tu closure, siguiendo el principio de mínimo privilegio.

Cuando un cierre solo necesita leer un valor, lo captura por referencia inmutable. Esto permite que la variable original siga siendo accesible después de que se defina y llame al cierre. Por ejemplo, un cierre que imprime una lista tomará prestada la lista de forma inmutable, permitiéndole continuar utilizando la lista después de que el cierre se ejecute.

Si un cierre necesita modificar una variable capturada, debe capturar por referencia mutable. En este caso, tanto la variable capturada como el propio cierre deben ser declarados como mutables. El cierre puede entonces modificar la variable capturada, pero las reglas de préstamo se siguen aplicando - no se pueden tener otras referencias a esa variable mientras exista el cierre mutable.

El método de captura más restrictivo es la toma de propiedad, que mueve las variables capturadas al cierre. Esto es necesario cuando el cierre puede sobrepasar el ámbito en el que se definieron originalmente las variables, como cuando se generan subprocesos. Puedes forzar la captura de propiedad utilizando la palabra clave `move` antes de los parámetros de cierre: `move |x| { /* cuerpo del cierre */ }`. Esto es esencial para la seguridad de los hilos, ya que los hilos no pueden tomar prestado de forma segura de otros hilos que podrían terminar y soltar sus variables.

### Rasgos de cierre y tipos de función

Rust representa los cierres mediante un sistema de rasgos con tres rasgos clave: `FnOnce`, `FnMut` y `Fn`. Estos rasgos forman una jerarquía que describe cómo se puede llamar a los cierres y lo que pueden hacer con las variables capturadas.

`FnOnce` es el rasgo más básico que implementan todos los cierres. Representa cierres que pueden ser llamados al menos una vez. Algunos cierres, particularmente aquellos que mueven valores capturados o los consumen de alguna manera, solo pueden ser llamados una vez porque destruyen o mueven sus datos capturados durante la ejecución.

`FnMut` representa cierres que pueden ser llamados múltiples veces y pueden mutar su entorno capturado. Estos cierres capturan variables por referencia mutable y pueden modificarlas a través de múltiples llamadas. Las reglas de préstamo aseguran que cuando un cierre `FnMut` está activo, tiene acceso mutable exclusivo a sus variables capturadas.

`Fn` es el rasgo más restrictivo, representando cierres que pueden ser llamados múltiples veces sin mutar su entorno capturado. Estos cierres solo capturan por referencia inmutable y pueden ser llamados concurrentemente sin violar las garantías de seguridad de Rust. Si un cierre implementa `Fn`, automáticamente implementa también `FnMut` y `FnOnce`, ya que ser invocable múltiples veces sin mutación implica ser invocable con mutación y ser invocable una vez.

### Trabajar con iteradores

Los iteradores en Rust proporcionan una forma de procesar secuencias de datos. Son perezosos, lo que significa que no realizan ningún trabajo hasta que los consumes llamando a métodos que realmente iteran a través de los datos. Esta evaluación perezosa permite un encadenamiento eficiente de operaciones sin crear colecciones intermedias.

El rasgo `Iterator` define la funcionalidad básica con un tipo asociado `Item` que representa lo que el iterador produce, y un método `next` que devuelve `Option<Self::Item>`. Cuando `next` devuelve `None`, el iterador se agota. Este diseño permite a los iteradores representar tanto secuencias finitas como potencialmente infinitas de forma segura.

Puede crear iteradores a partir de colecciones utilizando métodos como `iter()` para la iteración de préstamo, `iter_mut()` para la iteración de préstamo mutable y `into_iter()` para la iteración de consumo. La elección entre estos métodos depende de si necesitas modificar elementos y de si quieres consumir la colección original.

### Adaptadores y consumidores de iteradores

Los adaptadores de iteradores son métodos que transforman un iterador en otro, permitiendo encadenar operaciones. Los adaptadores más comunes son `map` para transformar cada elemento, `filter` para seleccionar elementos basándose en un predicado, y `enumerate` para añadir índices. Estos adaptadores son perezosos - no hacen ningún trabajo hasta que se consumen.

El método `map` aplica un cierre a cada elemento, transformándolo en otra cosa. Por ejemplo, `numbers.iter().map(|x| x * 2)` crea un iterador que duplica cada número. El método `filter` mantiene solo los elementos para los que el cierre del predicado devuelve verdadero: `numbers.iter().filter(|&x| x > 10)` mantiene solo los números mayores que diez.

Los métodos consumidores realmente iteran a través de los datos y producen un resultado final. El método `collect` consume un iterador y crea una colección a partir de él. A menudo es necesario especificar el tipo de colección: `let vec: Vec<_> = iterator.collect()`. Otros consumidores son `sum` para sumar elementos numéricos, `fold` para acumular valores con una operación personalizada, y `for_each` para ejecutar efectos secundarios en cada elemento.

### Iteradores avanzados

Otras operaciones de iteración son `zip` para combinar dos iteradores elemento a elemento, `chain` para concatenar iteradores y `filter_map` para combinar filtrado y mapeado en una sola operación. El método `zip` crea pares a partir de los elementos correspondientes de dos iteradores: `a.iter().zip(b.iter())` produce las tuplas `(a[0], b[0]), (a[1], b[1]), ...`.

El método `fold` es útil para acumular valores. Toma un valor inicial y un cierre que combina el acumulador con cada elemento: `numbers.iter().fold(0, |acc, x| acc + x)` suma todos los números. Este patrón puede implementar muchas otras operaciones como encontrar valores máximos, construir cadenas o crear estructuras de datos complejas.

Las cadenas de iteradores permiten expresar de forma concisa transformaciones de datos complejas. Por ejemplo, el procesamiento de datos de audio podría implicar: `coefficients.iter().zip(buffer.iter()).map(|(c, b)| c * b).sum::<i32>() >> 12`. Esto multiplica los coeficientes correspondientes y los valores del buffer, suma los resultados y desplaza el valor final, todo en una única expresión legible.

```rust
fn main() {
// Ejemplo UTXOs: (txid_suffix, amount_sats)
let utxos = vec![
("a1b2", 50_000u64),
("c3d4", 15_000),
("e5f6", 100_000),
("g7h8", 3_000),
("i9j0", 75_000),
];

// Uso de cierres e iteradores para procesar UTXO

// 1. Filtrar UTXO por encima del umbral de polvo (10,000 sats)
let spendable: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000)
.collect();
println!("Spendable UTXOs: {:?}", spendable);

// 2. Calcular el balance total con fold
let total_balance: u64 = utxos
.iter()
.map(|(_, amount)| amount)
.fold(0, |acc, amount| acc + amount);
println!("Total balance: {} sats", total_balance);

// 3. Encontrar UTXOs necesarios para cubrir un pago de 120,000 sats
let target = 120_000u64;
let mut accumulated = 0u64;
let selected: Vec<_> = utxos
.iter()
.filter(|(_, amount)| *amount >= 10_000) // Saltar polvo
.take_while(|(_, amount)| {
if accumulated >= target {
false
} else {
accumulated += amount;
true
}
})
.collect();
println!("Selected for payment: {:?}", selected);

// 4. Transformar al formato de visualización usando el mapa y recopilar
let display_strings: Vec<String> = utxos
.iter()
.map(|(txid, amount)| format!("{}...:{} sats", txid, amount))
.collect();
println!("Display: {:?}", display_strings);
}
```

### Introducción a los punteros inteligentes

Los punteros inteligentes son estructuras de datos que actúan como los punteros tradicionales, pero proporcionan capacidades adicionales y gestión automática de la memoria. A diferencia de las referencias simples, los punteros inteligentes son propietarios de los datos a los que apuntan y pueden implementar comportamientos personalizados para la asignación, desasignación y patrones de acceso a la memoria. Son herramientas esenciales para gestionar los datos asignados al montón e implementar patrones de propiedad complejos que van más allá del sistema de propiedad básico de Rust.

El aspecto "inteligente" proviene de su capacidad para gestionar automáticamente tareas de gestión de memoria que, de otro modo, requerirían intervención manual. Cuando un puntero inteligente sale de su ámbito, puede liberar automáticamente la memoria asociada, disminuir el número de referencias o realizar otras operaciones de limpieza. Esta automatización ayuda a evitar las fugas de memoria y los errores de uso después de la liberación, a la vez que proporciona más flexibilidad que la asignación solo en pila.

Los punteros inteligentes suelen implementar dos rasgos clave: `Deref` y `Drop`. El rasgo `Deref` permite utilizar el puntero inteligente como si fuera una referencia a los datos contenidos. El rasgo `Drop` permite una lógica de limpieza personalizada cuando se destruye el puntero inteligente. Juntos, estos rasgos permiten a los punteros inteligentes gestionar la memoria automáticamente.

### El puntero inteligente de Box

`Box<T>` es el puntero inteligente más simple, que proporciona asignación al montón para cualquier tipo `T`. Cuando se crea un `Box`, el valor contenido se almacena en el montón en lugar de en la pila, y la propia `Box` (que es solo un puntero) se almacena en la pila. Esta indirección es útil cuando necesitas almacenar grandes cantidades de datos sin moverlos, cuando necesitas un tipo con un tamaño desconocido en tiempo de compilación, o cuando quieres transferir la propiedad de los datos del montón eficientemente.

Crear una `Caja` es sencillo: `let valor_caja = Box::new(42);` asigna un entero en el heap. El `Box` gestiona automáticamente esta memoria - cuando el `Box` sale del ámbito, automáticamente desasigna la memoria del heap. Esta limpieza automática evita fugas de memoria sin necesidad de gestión manual.

Uno de los usos más importantes de `Box` es permitir estructuras de datos recursivas. Consideremos una lista enlazada en la que cada nodo contiene un valor y un puntero al siguiente nodo. Sin `Box`, no se puede definir una estructura de este tipo porque el compilador no puede determinar el tamaño de un tipo que se contiene a sí mismo. Usando `Box<Node>` para el siguiente puntero, se rompe el problema del tamaño recursivo porque `Box` tiene un tamaño fijo y conocido independientemente de lo que contenga.

### Aplicación del rasgo Deref

El rasgo `Deref` permite desreferenciar un tipo utilizando el operador `*`, haciendo que los punteros inteligentes se comporten como referencias a los datos que contienen. Cuando implementas `Deref` para un puntero inteligente, habilitas la desreferencia automática que hace que el puntero inteligente sea transparente de usar. Esto significa que puedes llamar a métodos del tipo contenido directamente a través del puntero inteligente sin desreferenciación explícita.

El rasgo `Deref` define un tipo asociado `Target` que especifica qué tipo de referencia debe producir la operación de dereferencia. El rasgo requiere la implementación de un método `deref` que devuelva una referencia al tipo objetivo. Para `Box<T>`, la implementación devuelve una referencia al valor `T` contenido.

Rust realiza la coerción automática deref, lo que significa que el compilador puede insertar automáticamente llamadas a `deref` cuando sea necesario para hacer los tipos compatibles. Esta es la razón por la que puedes pasar una `String` a una función que espera una `&str` - el compilador automáticamente derefiere la `String` para obtener un trozo de cadena. Esta coerción puede encadenar múltiples niveles, por lo que una `Box<String>` puede convertirse automáticamente en una `&str` a través de múltiples operaciones deref.

### Implantación de caída personalizada

El rasgo `Drop` te permite especificar código de limpieza personalizado que se ejecuta cuando un valor sale del ámbito. Esto es particularmente importante para punteros inteligentes que gestionan recursos más allá de la simple memoria, como manejadores de ficheros, conexiones de red o recuentos de referencias. El rasgo `Drop` tiene un único método, `drop`, que toma una referencia mutable a `self` y realiza la limpieza.

La mayoría de los tipos no necesitan implementaciones personalizadas de `Drop` porque Rust gestiona automáticamente la eliminación de sus campos. Sin embargo, los punteros inteligentes a menudo necesitan una lógica personalizada para limpiar adecuadamente los recursos que gestionan. Por ejemplo, un puntero inteligente con contador de referencias necesita decrementar el contador de referencias y potencialmente desasignar datos compartidos cuando la última referencia es eliminada.

También puedes soltar explícitamente un valor antes de que salga del ámbito usando `std::mem::drop()`. Esta función toma posesión de un valor y lo suelta inmediatamente, lo que puede ser útil para liberar recursos antes de tiempo o asegurar que la limpieza se realiza en un punto específico del programa. La función drop explícita es solo una función de identidad que toma la propiedad - el trabajo real ocurre cuando el valor se suelta al final de la función.

Esta base de cierres, iteradores y punteros inteligentes proporciona a los desarrolladores de Rust herramientas para escribir código expresivo, seguro y eficiente. Estas características trabajan juntas para permitir patrones de programación comunes, manteniendo las garantías básicas de Rust de seguridad de memoria y rendimiento.

## Recuento de referencias y mutabilidad interior

<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>

:::video id=44c681d1-d154-4240-b3e8-15590cbfcbd2:::

### Recuento de referencias con RC

El contador de referencia representa otro tipo fundamental de puntero inteligente en Rust, diseñado específicamente para permitir escenarios de propiedad múltiple. A diferencia de Box, que sigue las reglas tradicionales de propiedad única en las que una entidad es propietaria de los datos, RC (Reference Counter) permite que varias partes de su código compartan la propiedad de los mismos datos simultáneamente. Este modelo de propiedad compartida funciona mediante un mecanismo de recuento que rastrea cuántas referencias existen a un dato concreto.

El sistema de recuento de referencias funciona manteniendo un contador interno que aumenta cada vez que se clona una RC y disminuye cuando se abandona una RC. La memoria solo se libera cuando este contador llega a cero, asegurando que los datos siguen siendo válidos mientras exista alguna referencia. Este enfoque evita la desasignación prematura a la vez que permite patrones flexibles de compartición de datos que serían imposibles con la simple propiedad de Box.

Un ejemplo práctico de la utilidad de RC es la creación de estructuras de datos compartidas, como las listas enlazadas, en las que varias listas pueden hacer referencia a la misma porción de cola. Considere la posibilidad de crear dos listas separadas que hagan referencia a una subsecuencia común. Con la propiedad Box, esto es imposible porque al mover la porción compartida a la primera lista se transfiere la propiedad, impidiendo su uso en la segunda lista. RC resuelve esto permitiéndole clonar la referencia en lugar de los datos subyacentes, haciendo posible la estructura compartida mientras se mantiene la seguridad de la memoria.

Cuando clonas un RC, no estás duplicando los datos internos, independientemente de su tamaño o complejidad. En su lugar, se crea otra referencia a la misma posición de memoria y se incrementa el contador de referencias. Esto hace que la clonación de instancias RC sea eficiente incluso para grandes estructuras de datos, ya que solo se copia la referencia en sí, mientras que los datos subyacentes permanecen en su lugar.

### Mutabilidad interior con RefCell

RefCell introduce la mutabilidad interior, que permite mutar datos aunque solo se tenga una referencia inmutable a ellos. Esta capacidad cambia fundamentalmente el modo en que se aplican las normas de préstamo de Rust, ya que traslada las comprobaciones del tiempo de compilación al tiempo de ejecución. Mientras que las referencias normales dependen del compilador para verificar la seguridad del préstamo, RefCell realiza estas comprobaciones durante la ejecución del programa, proporcionando una mayor flexibilidad a costa de posibles pánicos en tiempo de ejecución.

El principio básico de RefCell consiste en mantener las mismas reglas de préstamo que Rust aplica normalmente en tiempo de compilación, pero comprobándolas dinámicamente. En cualquier momento, puede tener una referencia mutable o cualquier número de referencias inmutables a los datos dentro de una RefCell. Si su código intenta violar estas reglas creando simultáneamente referencias en conflicto, el programa entrará en pánico en lugar de producir un comportamiento indefinido.

Esta comprobación en tiempo de ejecución permite ciertos patrones de programación que el compilador podría rechazar incluso cuando son realmente seguros. El análisis estático del compilador no siempre puede demostrar que los patrones de préstamo complejos son correctos, lo que le lleva a pecar de precavido. RefCell le permite anular estas restricciones conservadoras cuando confía en la corrección de su código, pero esta confianza conlleva la responsabilidad de garantizar un uso adecuado para evitar bloqueos en tiempo de ejecución.

Un caso de uso común para RefCell implica objetos simulados en escenarios de pruebas. Cuando se implementa un rasgo que solo proporciona acceso inmutable a sí mismo, pero la implementación simulada necesita realizar un seguimiento interno de los cambios de estado, RefCell permite este patrón. Puede envolver el estado interno en una RefCell, permitiendo que el simulacro mute sus datos de seguimiento incluso a través de una interfaz inmutable.

### Combinación de RC y RefCell para un estado mutable compartido

La combinación de RC y RefCell crea un patrón de estado mutable compartido, en el que varios propietarios pueden modificar los mismos datos. RC proporciona la capacidad de propiedad compartida, mientras que RefCell permite la mutación a través de referencias inmutables. Esta combinación es útil en escenarios como estructuras de grafos, cachés o cualquier situación en la que varias partes del programa necesiten acceso de lectura y escritura a datos compartidos.

Cuando se envuelve una RefCell dentro de una RC, se crea una estructura que puede ser clonada y distribuida por todo el programa, con cada clon proporcionando acceso a los mismos datos mutables subyacentes. Todos los propietarios pueden modificar los datos utilizando el método borrow_mut de RefCell, pero deben respetar las reglas de préstamo en tiempo de ejecución. Este patrón permite escenarios complejos de compartición de datos al tiempo que mantiene las garantías de seguridad de Rust mediante comprobaciones en tiempo de ejecución.

Sin embargo, esta flexibilidad conlleva importantes advertencias en relación con las fugas de memoria y los ciclos de referencia. Cuando se utiliza RC con RefCell, es posible crear accidentalmente referencias circulares en las que las estructuras de datos se referencian a sí mismas, ya sea directamente o a través de una cadena de referencias. Estos ciclos impiden que el recuento de referencias llegue nunca a cero, provocando fugas de memoria porque los datos parecen tener siempre referencias activas incluso cuando ya no son accesibles desde el resto del programa.

La solución a los ciclos de referencia pasa por utilizar referencias débiles, que no contribuyen al recuento de referencias utilizado para las decisiones de gestión de memoria. Las referencias débiles permiten mantener conexiones entre estructuras de datos sin mantenerlas vivas, lo que rompe posibles ciclos al tiempo que preserva la capacidad de acceder a los datos relacionados cuando aún existen.

```rust
use std::rc::Rc;
use std::cell::RefCell;

// Simular un estado de canal al que varios componentes necesitan acceder y modificar
#[derive(Debug)]
struct ChannelState {
channel_id: String,
local_balance_msat: u64,
remote_balance_msat: u64,
is_active: bool,
}

fn main() {
// Rc<RefCell<T>> Permite múltiples propietarios con mutabilidad interior.
let channel = Rc::new(RefCell::new(ChannelState {
channel_id: "abc123".to_string(),
local_balance_msat: 1_000_000_000,  // 1M sats in msats
remote_balance_msat: 500_000_000,
is_active: true,
}));

// Clonar Rc para compartir la propiedad (barato: solo incrementa el contador)
let channel_for_ui = Rc::clone(&channel);
let channel_for_router = Rc::clone(&channel);

// El recuento de referencias ahora es 3
println!("Recuento de referencia: {}", Rc::strong_count(&channel));

// El componente UI lee el estado (préstamo inmutable)
{
let state = channel_for_ui.borrow();
println!("UI muestra balance: {} msats", state.local_balance_msat);
} // el préstamo termina aquí

// El enrutador actualiza el estado después de un pago (préstamo mutable)
{
let mut state = channel_for_router.borrow_mut();
state.local_balance_msat -= 100_000_000; // 100k sats enviados
state.remote_balance_msat += 100_000_000;
println!("Saldos actualizados del enrutador");
} // El préstamo mutable termina aquí

// La referencia original aún puede leer el estado actualizado
let state = channel.borrow();
println!("New local balance: {} msats", state.local_balance_msat);

// ADVERTENCIA: ¡Esto podría generar pánico en tiempo de ejecución!
// let borrow1 = channel.borrow();
// let borrow2 = channel.borrow_mut(); // PÁNICO: ya se tomó prestado
}
```

### Fundamentos de seguridad de subprocesos y concurrencia

La aproximación de Rust a la concurrencia se centra en prevenir las carreras de datos y los problemas de seguridad de memoria en tiempo de compilación. El sistema de tipos refuerza la seguridad de los hilos a través de rasgos como `Send` y `Sync`, que marcan los tipos como seguros para la transferencia entre hilos o seguros para el acceso concurrente respectivamente. Esta verificación en tiempo de compilación detecta muchos errores de concurrencia que solo aparecerían en tiempo de ejecución en otros lenguajes de programación de sistemas.

La creación de hilos en Rust sigue un patrón sencillo utilizando thread::spawn, que toma un closure para ejecutar en el nuevo hilo y devuelve un handle para gestionar el ciclo de vida del hilo. El hilo generado se ejecuta simultáneamente con el hilo principal, y se puede utilizar el método join en el manejador para esperar la finalización. Sin una unión explícita, los subprocesos generados pueden terminar cuando el subproceso principal salga, cortando potencialmente el trabajo incompleto.

La palabra clave move es crucial cuando se trabaja con subprocesos porque los cierres pasados a subprocesos generados a menudo necesitan poseer sus datos en lugar de tomarlos prestados. Dado que los subprocesos generados pueden sobrevivir al ámbito que los creó, tomarlos prestados del ámbito padre crea violaciones potenciales del tiempo de vida. Mover los datos al cierre de la hebra transfiere la propiedad, asegurando que los datos permanezcan válidos durante toda la vida de la hebra mientras se previene el acceso desde el ámbito original.

El paso de mensajes proporciona una alternativa a la concurrencia de estados compartidos a través de canales que permiten a los hilos comunicarse enviando datos en lugar de compartir memoria. La biblioteca estándar de Rust proporciona canales MPSC (Multiple Producer Single Consumer), en los que varios subprocesos pueden enviar mensajes a un único subproceso receptor. Este patrón elimina muchos problemas de sincronización al evitar por completo el estado mutable compartido, confiando en cambio en el intercambio de mensajes para la coordinación.

### Concurrencia de estados compartidos con Mutex y Arc

Cuando el paso de mensajes no es adecuado, Rust proporciona concurrencia de estado compartido tradicional a través de Mutex (exclusión mutua) combinado con Arc (contador de referencia atómica). Mutex asegura que solo un hilo puede acceder a los datos protegidos a la vez requiriendo que los hilos adquieran un bloqueo antes de acceder a los datos. El bloqueo se libera automáticamente cuando el objeto guardián devuelto por la operación de bloqueo sale del ámbito, lo que evita los habituales escenarios de punto muerto causados por desbloqueos olvidados.

Arc es el equivalente seguro de RC, ya que utiliza operaciones atómicas para gestionar el recuento de referencias de forma segura en varios subprocesos. Mientras que RC funciona perfectamente para escenarios de un solo hilo, su recuento de referencias no atómico crea condiciones de carrera cuando se accede desde múltiples hilos. Los contadores atómicos de Arc garantizan que las modificaciones en el recuento de referencias se produzcan de forma segura incluso bajo acceso concurrente, por lo que es adecuado para compartir datos a través de los límites de los subprocesos.

La combinación de Arc y Mutex crea un patrón para el estado mutable compartido en programas concurrentes. Al envolver un Mutex en un Arc, se puede clonar el Arc para distribuir el acceso al mismo mutex entre varios subprocesos, pudiendo cada subproceso adquirir el bloqueo y modificar los datos protegidos de forma segura. Este patrón proporciona la flexibilidad del estado compartido a la vez que mantiene las garantías de seguridad de Rust mediante la verificación en tiempo de compilación y el bloqueo en tiempo de ejecución.

Los rasgos Send y Sync funcionan en segundo plano para garantizar la seguridad de los subprocesos en tiempo de compilación. Send indica que un tipo puede transferirse de forma segura a otro subproceso, mientras que Sync indica que las referencias a un tipo pueden compartirse de forma segura entre subprocesos. La mayoría de los tipos implementan automáticamente estos rasgos cuando sus componentes son seguros para subprocesos, pero algunos tipos como RC y RefCell no los implementan explícitamente porque no están diseñados para el acceso concurrente. Esta implementación automática de rasgos evita la introducción accidental de violaciones de la seguridad de hilos, al tiempo que permite que los tipos seguros funcionen sin problemas en contextos concurrentes.

## Comprender las macros de Rust

<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>

:::video id=5e96914d-df02-4781-ae54-b06008952301:::

### Introducción a las macros en Rust

Las macros en Rust son una característica de metaprogramación que permite a los desarrolladores escribir código que genera otro código en tiempo de compilación. A diferencia de las funciones, que se invocan en tiempo de ejecución, las macros se expanden al principio del proceso de compilación, antes de la comprobación de tipos y etapas posteriores. Esta distinción fundamental hace que las macros sean especialmente útiles para reducir la repetición de código y crear lenguajes específicos de dominio dentro de los programas Rust.

El indicador más reconocible de una llamada a macro es el signo de exclamación (!) que sigue al nombre de la macro. Por ejemplo, cuando se utiliza `println!("¡Hola, mundo!")`, no se está llamando a una función sino invocando una macro. Esta macro se expande en un código más complejo que maneja las operaciones de formato y salida. El signo de exclamación sirve de indicación visual a los desarrolladores de que se está generando código en tiempo de compilación en lugar de una llamada a una función estándar.

Rust proporciona tres tipos distintos de macros, cada uno de los cuales sirve a diferentes propósitos en el ecosistema del lenguaje:

- **Macros de tipo función**: Se parecen a las llamadas a funciones, pero operan en tiempo de compilación (por ejemplo, `vec!`, `println!`)
- **Macros derivadas**: Implementación automática de rasgos para tipos (por ejemplo, `#[derive(Debug, Clone)]`)
- **Macros de tipo atributo**: Modifican el comportamiento de los elementos de código a los que se aplican (por ejemplo, `#[test]`, `#[tokio::main]`)

La comprensión de estos diferentes tipos de macros es esencial para una programación eficaz de Rust, ya que cada una aborda casos de uso y patrones de programación específicos.

### Tipos de macros y sus aplicaciones

Las macros de tipo función representan el tipo de macro más comúnmente encontrado en la programación Rust. Estas macros utilizan una sintaxis similar a la de las llamadas a funciones, pero realizan una concordancia de patrones en su entrada para generate código apropiado. La macro `vec!` es un ejemplo común de esta categoría, permitiendo a los desarrolladores crear e inicializar vectores con una sintaxis concisa. Cuando escribes `vec![1, 2, 3, 4]`, la macro expande esto en código que crea un nuevo vector, empuja cada elemento individualmente, y devuelve el vector completado.

Las macros derivadas proporcionan implementaciones automáticas de rasgos para tipos personalizados, reduciendo significativamente el código repetitivo. Cuando añades `#[derive(Debug)]` a una definición struct o enum, estás indicando al compilador que genere una implementación completa del rasgo Debug para ese tipo. Esta implementación generada maneja la lógica de formateo necesaria para mostrar el contenido del tipo en un formato legible por humanos. El mecanismo de derivación soporta numerosos rasgos estándar de la biblioteca, incluyendo Clone, PartialEq, lo que lo convierte en una herramienta comúnmente utilizada para reducir el boilerplate.

Las macros de tipo atributo modifican el comportamiento de los elementos de código que anotan, proporcionando una forma de añadir metadatos o alterar el comportamiento de compilación. Estas macros aparecen como atributos situados sobre definiciones de tipos, funciones u otras construcciones de código. Por ejemplo, el atributo `#[non_exhaustive]` de un enum indica que podrían añadirse variantes adicionales en futuras versiones, lo que requiere que las expresiones de coincidencia incluyan un caso por defecto. Este mecanismo garantiza la compatibilidad futura al tiempo que proporciona una documentación clara del potencial de evolución del tipo.

### Creación de macros personalizadas similares a funciones

Escribir macros personalizadas similares a funciones implica comprender la sintaxis de coincidencia de patrones de Rust para las definiciones de macros. La definición de macros utiliza un enfoque declarativo en el que se especifican patrones que coinciden con diferentes formas de entrada y las correspondientes plantillas de generación de código. Cada macro puede contener múltiples ramas, permitiéndole manejar varios patrones de entrada y generar el código apropiado para cada caso.

Considere la posibilidad de crear una macro vectorial personalizada que demuestre los principios fundamentales de la construcción de macros. La definición de la macro comienza con `macro_rules!` seguido por el nombre de la macro y una serie de ramas de coincidencia de patrones. Cada rama consiste en un patrón que coincide con una sintaxis de entrada específica y una plantilla de código que genera el código Rust correspondiente. Por ejemplo, una rama simple puede coincidir con paréntesis vacíos `[]` y generar el código para crear un vector vacío, mientras que otra rama coincide con una sola expresión y genera código para crear un vector con un elemento.

Las macros resultan especialmente útiles cuando se implementan patrones de argumentos variables utilizando la sintaxis de repetición. El patrón `$($x:expr),*` coincide con cero o más expresiones separadas por comas, permitiendo a la macro manejar un número arbitrario de argumentos. La plantilla de generación de código correspondiente utiliza `$(vec.push($x);)*` para iterar sobre todas las expresiones coincidentes y generar sentencias push individuales para cada una. Este mecanismo de repetición permite a las macros escribir manualmente código que sería imposible o extremadamente prolijo.

```rust
// Una macro para crear un HashMap con datos relacionados a Bitcoin
macro_rules! btc_map {
// Caso vacío
() => {
std::collections::HashMap::new()
};
// Key-value pairs case
($($key:expr => $value:expr),+ $(,)?) => {
{
let mut map = std::collections::HashMap::new();
$(
map.insert($key, $value);
)+
map
}
};
}

// Una macro para registrar con contexto (simulando un patrón similar a una derivación)
macro_rules! log_payment {
($level:ident, $($arg:tt)*) => {
println!(
"[{}] [PAYMENT] {}",
stringify!($level).to_uppercase(),
format!($($arg)*)
)
};
}

fn main() {
// Usando la macro btc_map!
let fee_rates = btc_map! {
"high_priority" => 50_u64,    // sats/vbyte
"medium" => 25_u64,
"low" => 10_u64,
};

println!("Tarifas: {:?}", fee_rates);

// Usando la macro log_payment!
log_payment!(info, "Enviando {} sats a {}", 100_000, "bc1q...");
log_payment!(warn, "Tarifa {} sats/vB está por encima del promedio", 75);
log_payment!(error, "Pago fallido: fondos insuficientes");

// Comparación del uso de la macro vec! estándar
let utxos = vec![50_000_u64, 30_000, 20_000];
let total: u64 = utxos.iter().sum();
println!("Total UTXOs: {} sats", total);
}
```

El proceso de compilación transforma las llamadas a macros en código expandido antes de que se produzcan la comprobación de tipos y la optimización. Cuando el compilador encuentra una invocación a una macro, compara la entrada con los patrones definidos y sustituye la llamada a la macro por el código generado. A continuación, este código expandido se somete a los procesos de compilación normales, incluida la comprobación de tipos y la optimización. Herramientas como `cargo expand` permiten a los desarrolladores inspeccionar el código generado, lo que ofrece valiosas posibilidades de depuración cuando se desarrollan macros complejas.

### Conceptos avanzados de macros y depuración

El desarrollo de macros requiere comprender la distinción entre la ejecución en tiempo de compilación y en tiempo de ejecución. Las macros se ejecutan durante la compilación, generando código que se ejecutará en tiempo de ejecución. Esta separación temporal significa que la lógica de las macros no puede depender de valores en tiempo de ejecución, pero también permite optimizaciones en las que los cálculos complejos pueden realizarse una vez durante la compilación en lugar de repetidamente durante la ejecución.

El sistema de concordancia de patrones de las macros admite varios especificadores de fragmentos que definen qué tipo de elementos de código pueden concordar. El especificador `expr` concuerda con expresiones, `ty` concuerda con tipos, `ident` concuerda con identificadores, y varios otros proporcionan un control detallado sobre la validación de la entrada. Estos especificadores garantizan que las macros reciban entradas sintácticamente válidas y proporcionan mensajes de error claros cuando se encuentra una sintaxis no válida.

La depuración de macros presenta retos únicos debido a su naturaleza en tiempo de compilación. El comando `cargo expand` es útil para el desarrollo de macros, ya que muestra el código completamente expandido generado por las invocaciones de macros. Esta herramienta permite a los desarrolladores verificar que sus macros generan el código previsto e identificar problemas en la lógica de expansión. Cuando el código generado por la macro contiene errores, la salida expandida ayuda a determinar si el problema reside en la definición de la macro o en la estructura del código generado.

Las macros complejas pueden implementar patrones recursivos, en los que una macro se llama a sí misma con argumentos modificados para gestionar la generación de código anidado o iterativo. Sin embargo, las macros recursivas requieren un diseño cuidadoso para evitar la expansión infinita y los problemas de rendimiento de la compilación. La naturaleza de la expansión de macros en tiempo de compilación significa que incluso las implementaciones de macros ineficientes solo afectan a la velocidad de compilación, no al rendimiento en tiempo de ejecución, pero las macros excesivamente complejas pueden ralentizar considerablemente el proceso de compilación.

# Rust Y Bitcoin

<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>

## Por qué Rust para el desarrollo de Bitcoin

<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>

:::video id=f59c4951-e109-4c70-b7da-41721e50ab04:::

La elección de Rust para el desarrollo de Bitcoin y Lightning no es casual. El desarrollo de Bitcoin conlleva responsabilidades únicas que lo distinguen del desarrollo de software típico. Al trabajar con Bitcoin, los desarrolladores suelen manejar fondos de usuarios en un entorno en el que los errores pueden ser irreversibles. A diferencia de los sistemas financieros tradicionales con protecciones normativas y mecanismos de devolución de cargos, la naturaleza descentralizada de Bitcoin significa que una vez que se emite una [transacción](https://planb.academy/resources/glossary/transaction-tx), no hay ninguna autoridad a la que recurrir para recuperar los fondos. Esta realidad exige un mayor nivel de responsabilidad y precisión en el desarrollo de software.

La filosofía de "avanzar rápido y romper cosas", que funciona en muchos sectores tecnológicos, no es aplicable al desarrollo de Bitcoin. En su lugar, el ecosistema requiere lenguajes y herramientas que ayuden a los desarrolladores a crear software robusto y seguro en el que los fallos se eviten o se gestionen con elegancia. Esta es la razón por la que muchos proyectos destacados de Bitcoin han gravitado hacia Rust, incluido el kit de desarrollo de Bitcoin (BDK), Lightning Development Kit (LDK) y BreezSDK.

Rust ofrece tres propiedades esenciales que lo hacen especialmente adecuado para el desarrollo de Bitcoin: un sistema estático de tipos fuertes, herramientas modernas y ricas, y compatibilidad entre plataformas. Cada una de estas características contribuye a la capacidad del lenguaje para ayudar a los desarrolladores a escribir código más seguro y fiable para el manejo de operaciones con [criptomonedas](https://planb.academy/resources/glossary/cryptocurrency).

### Sistema estático de tipo fuerte de Rust

El sistema de tipos de Rust proporciona características de tipado estático y fuerte que trabajan conjuntamente para detectar errores antes de que puedan afectar a los usuarios. La naturaleza estática significa que la comprobación de tipos se produce en tiempo de compilación, lo que obliga a los desarrolladores a resolver los desajustes de tipos incluso antes de que el programa pueda construirse. Esto contrasta con los lenguajes de tipado dinámico, en los que los errores de tipado solo aparecen durante el tiempo de ejecución, potencialmente después de que el software se haya desplegado y esté gestionando fondos de usuarios reales.

La fuerza del sistema de tipos de Rust se refiere a su expresividad y rigor a la hora de modelar problemas. A diferencia de lenguajes con sistemas de tipos más débiles como C, donde los desarrolladores están limitados a tipos básicos como números y estructuras, Rust permite un modelado de tipos rico que puede representar conceptos de dominio complejos con precisión. Por ejemplo, se pueden crear tipos que distingan entre diferentes tipos de listas o que obliguen a que ciertas operaciones solo se realicen sobre tipos de objetos específicos.

Lo que hace que el sistema de tipos de Rust sea relevante para el desarrollo de Bitcoin es su enfoque de la seguridad de la memoria. El mismo sistema de tipos que modela la lógica de negocio también gestiona la propiedad de la memoria y el control de acceso compartido. Esta doble responsabilidad significa que las clases comunes de vulnerabilidades, como las fugas de memoria, los errores doble-libre y las condiciones de carrera, son eliminadas completamente por el compilador. El sistema de tipos aplica estas garantías de seguridad mediante conceptos como propiedad, préstamo y recuento de referencias, lo que hace extremadamente difícil introducir errores relacionados con la memoria que puedan comprometer la seguridad o la estabilidad.

```rust
// Ejemplo: Manejo de cantidades de Bitcoin con seguridad de tipos
// Uso de nuevos tipos para evitar mezclar satoshis y otros valores

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct Satoshis(u64);

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
struct FeeRate(u64); // sats por vbyte

impl Satoshis {
fn from_btc(btc: f64) -> Self {
Satoshis((btc * 100_000_000.0) as u64)
}

fn as_btc(&self) -> f64 {
self.0 as f64 / 100_000_000.0
}
}

// Calcular la tarifa según el tamaño de la transacción: el sistema de tipos garantiza que no podamos mezclar valores
fn calculate_fee(tx_size_vbytes: u32, rate: FeeRate) -> Satoshis {
Satoshis(tx_size_vbytes as u64 * rate.0)
}

fn main() {
let payment = Satoshis::from_btc(0.001); // 100,000 sats
let fee_rate = FeeRate(25);              // 25 sats/vbyte
let tx_size = 250_u32;                   // vbytes

let fee = calculate_fee(tx_size, fee_rate);
println!("Payment: {:?} ({} BTC)", payment, payment.as_btc());
println!("Fee: {:?}", fee);

// Esto NO se compilaría; la seguridad de tipos evita la mezcla de valores:
// let bad_fee = calculate_fee(tx_size, payment); // ERROR: se esperaba FeeRate, se encontraron Satoshis
}
```

### Herramientas modernas y compatibilidad multiplataforma

El ecosistema de herramientas de Rust proporciona a los desarrolladores herramientas que ayudan a la productividad y a la calidad del código. El propio compilador de Rust está diseñado no solo para traducir código a formato binario, sino también para servir como herramienta educativa que ayude a los desarrolladores a aprender y mejorar. Cuando se producen errores de compilación, el compilador ofrece explicaciones detalladas de lo que ha fallado y a menudo sugiere soluciones específicas. Este enfoque es especialmente valioso para los desarrolladores que se inician en Rust, ya que el compilador enseña buenas prácticas y ayuda a evitar errores comunes.

El lenguaje incluye Cargo, un gestor de paquetes unificado que se ocupa de la gestión de dependencias, la construcción, las pruebas y la generación de documentación. Esta estandarización elimina la fragmentación observada en lenguajes más antiguos, como C++, donde múltiples herramientas competidoras crean incoherencias entre proyectos. Cargo también es compatible con extensiones como rustfmt para el formateo del código y Clippy para el análisis estático, lo que garantiza que el código siga unas pautas de estilo coherentes y detecte posibles problemas antes de que se conviertan en tales.

Las capacidades multiplataforma de Rust van más allá de los sistemas operativos tradicionales e incluyen plataformas móviles como Android e iOS, así como WebAssembly para aplicaciones basadas en navegador. Esta compatibilidad multiplataforma es útil para aplicaciones Bitcoin que deben ejecutarse en distintos entornos. Por ejemplo, proyectos como Mutiny Wallet aprovechan la compilación WebAssembly de Rust para crear [carteras](https://planb.academy/resources/glossary/wallet) Lightning que se ejecutan directamente en navegadores web, algo que sería poco práctico solo con las tecnologías web tradicionales.

### Tipos de error y sus consecuencias

Un tratamiento eficaz de los errores empieza por comprender las distintas categorías de errores que pueden producirse durante la ejecución de un programa. Consideremos una sencilla aplicación de enrutamiento que calcula rutas entre puntos geográficos. Este ejemplo ilustra tres tipos fundamentales de errores que los desarrolladores deben abordar: errores de entrada no válidos, errores de recursos en tiempo de ejecución y errores lógicos.

Los errores de entrada no válida se producen cuando una función recibe parámetros que no cumplen sus requisitos. Por ejemplo, si un sistema de coordenadas geográficas utiliza enteros con signo para la longitud, pero recibe un valor negativo cuando solo son válidos los valores positivos, la función no puede proceder de forma significativa. Estos errores representan una violación del contrato entre quien llama y la función, y la respuesta apropiada suele ser rechazar la entrada y devolver una indicación de error.

Los errores de recursos en tiempo de ejecución se producen cuando las dependencias externas no están disponibles o son inaccesibles. La lectura de un archivo de mapa puede fallar porque el archivo no existe, la aplicación carece de los permisos adecuados o el dispositivo de almacenamiento no está disponible. Estos errores son externos a la lógica del programa y a menudo requieren correcciones del entorno en lugar de cambios en el código. Sin embargo, las aplicaciones robustas deben anticipar y manejar estos escenarios con elegancia.

Los errores lógicos representan fallos en la implementación del programa o malentendidos sobre cómo interactúan los componentes. Si un algoritmo de enrutamiento devuelve una ruta vacía cuando se le dan puntos de inicio y final válidos, esto indica un fallo lógico que debe corregirse en el propio código. A diferencia de los otros tipos de error, los errores lógicos suelen requerir depuración y modificación del código para resolverse.

### Estrategias para una gestión sólida de los errores

Construir software fiable requiere estrategias proactivas que minimicen las oportunidades de error y gestionen con elegancia los errores inevitables. La primera estrategia consiste en limitar los posibles errores mediante un cuidadoso diseño de tipos. Eligiendo tipos que solo puedan representar valores válidos, los desarrolladores pueden eliminar clases enteras de errores de entrada no válidos. Por ejemplo, el uso de enteros sin signo para valores que no pueden ser negativos evita errores de valor negativo en tiempo de compilación.

Las aserciones proporcionan otra capa de protección al comprobar explícitamente que las condiciones esperadas se cumplen durante la ejecución del programa. Estas comprobaciones tienen múltiples propósitos: detectan errores durante las pruebas, hacen que los programas fallen antes de tiempo cuando surgen problemas (lo que facilita la depuración) y sirven como documentación ejecutable que describe las suposiciones del programador. Cuando una aserción falla, indica que se ha violado una suposición fundamental sobre el estado del programa, lo que suele apuntar a un error lógico que hay que investigar.

El principio de abstracción por capas ayuda a gestionar la complejidad garantizando que los errores se gestionen en los niveles adecuados del sistema. Los detalles de implementación internos, incluidos los tipos de error específicos de las bibliotecas de nivel inferior, no deben propagarse más allá de los límites del subsistema. En su lugar, cada capa debe traducir los errores en términos que tengan sentido en ese nivel de abstracción. Por ejemplo, una aplicación wallet que utilice una biblioteca Bitcoin debe traducir los errores de análisis de descriptor de bajo nivel en mensajes de alto nivel como "configuración de wallet no válida" que proporcionen información procesable a los usuarios o al código de llamada.

Este enfoque de la gestión de errores, combinado con el sistema de tipos y las herramientas de Rust, ayuda a detectar posibles problemas en una fase temprana del proceso de desarrollo, antes de que puedan afectar a los usuarios o comprometer la seguridad de las aplicaciones Bitcoin.

## Modelo de error

<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>

:::video id=9fac0184-8443-4c36-8afd-8acb21fb43c3:::

Rust ofrece un enfoque integral de la gestión de errores que equilibra la seguridad con la practicidad. Aunque los conceptos generales del modelo de error se aplican a todos los lenguajes de programación, Rust ofrece herramientas y patrones específicos que hacen que la gestión de errores sea explícita y manejable. Entender estos mecanismos es crucial para escribir aplicaciones Rust robustas que puedan manejar con gracia situaciones inesperadas manteniendo el rendimiento y la seguridad.

### El pánico y sus usos adecuados

El mecanismo de pánico de Rust representa la forma más directa de manejar errores irrecuperables. Cuando se llama a la macro `¡pánico!`, el programa detiene inmediatamente la ejecución, abortando o desenrollando dependiendo de su configuración. La macro panic acepta un mensaje de cadena que describe lo que ha ido mal, proporcionando contexto para la depuración. Además, métodos como `unwrap()` y `expect()` en los tipos Result y Option sirven como atajos para entrar en pánico cuando estos tipos contienen valores de error o None respectivamente. El método `expect()` permite proporcionar un mensaje personalizado, haciéndolo ligeramente más informativo que `unwrap()` cuando se depuran fallos.

A pesar de su simplicidad, el pánico debe utilizarse con criterio en el código de producción. Hay varios escenarios en los que panic no solo es aceptable, sino recomendable. Cuando se escriben ejemplos o prototipos, panic proporciona una forma limpia de centrarse en la funcionalidad principal sin saturar el código con un manejo exhaustivo de errores. En entornos de pruebas, panic es a menudo el comportamiento deseado cuando las aserciones fallan, ya que indica claramente que ha ocurrido algo inesperado. La comunidad Rust también reconoce situaciones en las que los desarrolladores tienen más conocimientos que el compilador, como cuando se analizan direcciones IP codificadas que se sabe que son válidas.

Sin embargo, la aparente seguridad de los pánicos "verificados por el compilador" puede ser engañosa. Considera un escenario donde codificas una dirección IP y usas `expect()` porque sabes que es válida. Con el tiempo, a medida que el código evoluciona, ese valor codificado puede ser refactorizado en una constante, y más tarde esa constante puede ser cambiada a algo como "localhost" para una mejor experiencia de usuario. De repente, tu pánico "seguro" se convierte en un fallo en tiempo de ejecución. Esta evolución demuestra por qué generalmente es mejor evitar los pánicos en el código de producción y en su lugar devolver tipos de error apropiados que puedan ser manejados con gracia.

Una notable excepción a la regla de "evitar el pánico" involucra las operaciones mutex. Cuando llamas a `lock()` sobre un mutex, devuelve un Resultado porque el bloqueo puede fallar si otro hilo entra en pánico mientras mantiene el mutex. Esto crea una situación confusa en la que tu código local recibe un error por algo que ocurrió en un contexto completamente diferente. Dado que usted no puede razonablemente manejar un error que se originó por el pánico de otro hilo, muchos desarrolladores consideran aceptable desenvolver bloqueos mutex, especialmente si usted mantiene una base de código libre de pánico en otro lugar.

### Trabajar con tipos de resultados y opciones

El tipo Result forma la columna vertebral del sistema de gestión de errores de Rust. Como un enum que puede contener un `Ok(valor)` o un `Err(error)`, Resultado le obliga a reconocer explícitamente que las operaciones pueden fallar. El tipo Opción tiene un propósito similar para los casos en los que un valor puede simplemente estar ausente, conteniendo `Algo(valor)` o `Nada`. Aunque Option no proporciona información detallada sobre el error, es perfecto para situaciones en las que la ausencia de un valor es significativa y esperada.

Tanto Result como Option proporcionan varios métodos de utilidad que hacen que la gestión de errores sea más ergonómica. El método `unwrap_or()` devuelve el valor contenido si está presente, o un valor por defecto si hay un error o None. Este patrón es particularmente útil cuando se tiene una alternativa razonable, como analizar la entrada del usuario con un valor por defecto razonable cuando el análisis falla. El método `unwrap_or_default()` funciona de forma similar pero utiliza el valor por defecto del tipo en lugar de pedirle que especifique uno. Aunque estos métodos técnicamente no manejan errores en el sentido tradicional, proporcionan una forma de degradar la funcionalidad cuando ocurren problemas.

El operador interrogación (`?`) es una sintaxis concisa para la propagación de errores. Cuando se aplica a un Resultado u Opción, extrae el valor de éxito si está presente, o devuelve inmediatamente el error de la función actual si hay un problema. Este operador elimina los verborreicos patrones de comprobación de errores comunes en lenguajes como Go, donde hay que comprobar y devolver manualmente los errores en cada paso. El operador de signo de interrogación esencialmente proporciona azúcar sintáctico para devoluciones tempranas, permitiéndole escribir código limpio y lineal que se centra en el camino feliz mientras maneja automáticamente la propagación de errores.

### Patrones avanzados de gestión de errores

El método `map()` en los tipos Result y Option permite una gestión de errores de estilo funcional que puede hacer que el código sea más expresivo y componible. Cuando se llama a `map()` en un Resultado, la función proporcionada se aplica al valor de éxito si está presente, mientras que los errores se propagan automáticamente sin modificación. Este patrón es útil cuando se encadenan operaciones, ya que puede centrarse en la transformación de valores sin manejar repetidamente los casos de error. El método `map_err()` proporciona la funcionalidad inversa, permitiéndole transformar los tipos de error sin modificar los valores de éxito.

La transformación de errores es crucial cuando se crean aplicaciones en capas en las que distintos componentes necesitan diferentes tipos de error. Considere una función que analiza la entrada del usuario y necesita convertir errores de análisis de bajo nivel en errores específicos del dominio. Usando `map_err()`, puedes traducir fácilmente un error genérico "formato de número no válido" en un error más contextual "edad no válida" que tenga sentido dentro del dominio de tu aplicación. Esta transformación tiene lugar justo en el punto en el que se produce el error, lo que hace que el código sea más legible y fácil de mantener que los bloques try-catch tradicionales, en los que la gestión de errores está separada de las operaciones que pueden fallar.

La combinación del operador de signo de interrogación con la asignación de errores crea patrones de gestión de errores concisos. Puede encadenar operaciones, transformar errores según sea necesario y propagarlos por la pila de llamadas con un mínimo de repeticiones. Este enfoque mantiene la gestión de errores cerca de las operaciones que pueden fallar a la vez que mantiene una separación limpia entre las rutas de éxito y de error.

```rust
use std::fmt;

// Tipos de errores en capas para una aplicación de wallet
#[derive(Debug)]
enum NetworkError {
ConnectionFailed(String),
Timeout,
}

#[derive(Debug)]
enum WalletError {
Network(NetworkError),
InvalidAddress(String),
InsufficientFunds { required: u64, available: u64 },
}

// Implementar Display para mensajes fáciles de usar
impl fmt::Display for WalletError {
fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
match self {
WalletError::Network(e) => write!(f, "Network error: {:?}", e),
WalletError::InvalidAddress(addr) => write!(f, "Invalid address: {}", addr),
WalletError::InsufficientFunds { required, available } =>
write!(f, "Need {} sats but only have {} available", required, available),
}
}
}

// Convertir de error de nivel inferior a error de dominio
impl From<NetworkError> for WalletError {
fn from(err: NetworkError) -> Self {
WalletError::Network(err)
}
}

// Llamada de red simulada
fn fetch_balance(address: &str) -> Result<u64, NetworkError> {
if address.starts_with("bc1") {
Ok(500_000) // 500k sats
} else {
Err(NetworkError::ConnectionFailed("Invalid endpoint".into()))
}
}

// Función de nivel superior que utiliza ? con conversión automática de errores
fn send_payment(from: &str, amount: u64) -> Result<String, WalletError> {
let balance = fetch_balance(from)?; // NetworkError se convierte automáticamente en WalletError

if balance < amount {
return Err(WalletError::InsufficientFunds {
required: amount,
available: balance,
});
}

Ok(format!("Sent {} sats", amount))
}

fn main() {
match send_payment("bc1qtest...", 100_000) {
Ok(msg) => println!("Success: {}", msg),
Err(e) => println!("Failed: {}", e), // Mensaje fácil de usar
}
}
```

### Bibliotecas externas y ecosistemas de gestión de errores

El ecosistema Rust incluye varias bibliotecas populares que amplían las capacidades de gestión de errores de la biblioteca estándar. La librería `anyhow` proporciona una aproximación simplificada al manejo de errores ofreciendo un tipo de error universal que puede convertir automáticamente desde cualquier tipo de error que implemente el rasgo estándar Error. Esta conversión automática permite utilizar el operador de signo de interrogación con distintos tipos de error sin necesidad de conversión manual, lo que la hace especialmente útil para aplicaciones en las que no es necesario distinguir mediante programación entre distintos tipos de error.

Mientras que `anyhow` sobresale en la simplificación de la gestión de errores para aplicaciones donde los errores se muestran principalmente a los usuarios, tiene limitaciones en el desarrollo de bibliotecas. Dado que `anyhow` esencialmente convierte todos los errores en mensajes de cadena, los consumidores de su biblioteca no pueden responder fácilmente mediante programación a diferentes condiciones de error. Esta limitación hace que `anyhow` sea más adecuado para aplicaciones de usuario final que para bibliotecas que necesitan proporcionar información estructurada de errores a sus consumidores.

Los enfoques de gestión de errores más avanzados implican la creación de tipos de error personalizados que modelen los modos de fallo específicos de su aplicación o biblioteca. Un modelo de error bien diseñado puede distinguir entre entradas no válidas (que el usuario puede corregir), errores de ejecución (que pueden reintentarse) y fallos permanentes (que indican bugs o condiciones irrecuperables). Este enfoque estructurado permite a los consumidores de su código tomar decisiones inteligentes sobre cómo responder a los diferentes tipos de fallos, ya sea reintentando operaciones, pidiendo a los usuarios una entrada diferente, o informando de errores a los desarrolladores.

## UniFFI, puente entre bibliotecas Rust y varios idiomas

<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>

:::video id=b1a0f5f6-fc29-4b83-9c09-0b24711654e2:::

### Introducción a UniFFI y al desarrollo multiplataforma

UniFFI es una herramienta para hacer accesibles las bibliotecas Rust en múltiples lenguajes de programación y plataformas. Desarrollada por Mozilla, esta herramienta aborda un reto fundamental en el desarrollo de software moderno: cómo aprovechar las ventajas de rendimiento y seguridad de Rust manteniendo al mismo tiempo la compatibilidad con diversos ecosistemas de desarrollo. La herramienta genera automáticamente enlaces de lenguaje para las bibliotecas Rust, eliminando la necesidad de que los desarrolladores creen manualmente el código de interfaz para cada lenguaje de destino.

El principal problema que resuelve UniFFI se deriva de la naturaleza de Rust como lenguaje compilado. Cuando el código de Rust se compila, produce una salida binaria con una interfaz de función externa (FFI) que presenta una interfaz de bajo nivel que puede ser difícil de usar directamente desde lenguajes de alto nivel como Python, Swift o Kotlin. Tradicionalmente, cada desarrollador de bibliotecas tendría que escribir código de vinculación personalizado para cada lenguaje de destino, creando una barrera significativa para la adopción multiplataforma. UniFFI elimina esta redundancia proporcionando un enfoque estandarizado para generar estos enlaces automáticamente.

La filosofía de diseño de la herramienta se centra en permitir que los desarrolladores de Rust se centren en su lógica empresarial principal y, al mismo tiempo, hacer que sus bibliotecas sean accesibles para los desarrolladores que trabajan en otros lenguajes. Un desarrollador de iOS que utilice Swift, por ejemplo, puede consumir una biblioteca Rust a través de enlaces generados por UniFFI que presentan una interfaz Swift completamente nativa, sin indicación alguna de que la implementación subyacente está escrita en Rust. Esta integración perfecta permite a los equipos aprovechar las ventajas de rendimiento de Rust sin necesidad de que todos los miembros del equipo aprendan Rust.

### Comprender la arquitectura y el flujo de trabajo de UniFFI

UniFFI funciona mediante un flujo de trabajo bien definido que transforma las bibliotecas Rust en paquetes compatibles con varios idiomas. El proceso comienza con la creación de un archivo de Lenguaje de Definición Unificado (UDL), que sirve como especificación de interfaz que describe qué partes de su biblioteca Rust deben exponerse a otros lenguajes. Este archivo UDL actúa como un contrato entre su implementación de Rust y los enlaces de lenguaje generados.

La arquitectura sigue una clara separación de intereses. Los desarrolladores mantienen su biblioteca Rust con modismos y patrones estándar de Rust y, a continuación, crean un archivo UDL independiente que asigna la interfaz pública al sistema de tipos de UniFFI. El generador de enlaces UniFFI procesa tanto la biblioteca Rust como la especificación UDL para producir enlaces de lenguaje nativo para las plataformas de destino solicitadas. Estas vinculaciones generadas gestionan todo el complejo proceso de intercambio de datos entre el tiempo de ejecución en el idioma externo y el código Rust.

En tiempo de ejecución, la arquitectura crea un enfoque por capas en el que el código de la aplicación escrito en el lenguaje de destino (como Kotlin para Android) interactúa con el código de enlace generado que parece completamente nativo de ese lenguaje. Esta capa de enlace se encarga de la traducción entre los tipos específicos del lenguaje y los tipos de Rust, gestiona la memoria de forma segura a través de las fronteras del lenguaje y proporciona una gestión de errores que sigue las convenciones del lenguaje de destino. La lógica de negocio subyacente de Rust permanece inalterada y ajena a las interfaces de múltiples idiomas construidas sobre ella.

### Trabajar con UDL: Definición de interfaz y asignación de tipos

El Lenguaje Unificado de Definición sirve como piedra angular de la funcionalidad de UniFFI, proporcionando una forma declarativa de especificar qué partes de una biblioteca Rust deben exponerse y cómo deben presentarse en los lenguajes de destino. Los archivos UDL deben contener al menos un espacio de nombres, que actúa como contenedor de funciones que pueden invocarse directamente sin necesidad de instanciar objetos. Estas funciones de espacio de nombres suelen manejar operaciones sencillas que toman valores como parámetros y devuelven resultados.

UDL admite un amplio conjunto de tipos incorporados que se asignan de forma natural a los tipos Rust correspondientes. Los tipos básicos incluyen primitivos estándar como booleanos, varios tamaños de enteros (u8, u32, etc.), números de punto flotante y cadenas. Los tipos más complejos incluyen vectores, mapas hash y conceptos específicos de Rust como los tipos Option (representados con una sintaxis de signo de interrogación) y los tipos Resultado para la gestión de errores. El sistema de tipos también admite enumeraciones, tanto enumeraciones simples basadas en valores como enumeraciones complejas que contienen datos asociados, lo que permite un modelado de datos que se traduce a través de las fronteras del lenguaje.

Los structs en Rust se traducen a diccionarios en UDL, manteniendo una correspondencia casi uno a uno mientras se adaptan a las convenciones sintácticas de UDL. Cuando los structs de Rust tienen métodos asociados, pueden exponerse como interfaces en UDL, que se generan como clases con métodos en lenguajes de destino orientados a objetos como Kotlin o Swift. Esta asignación conserva los patrones de diseño orientado a objetos que los desarrolladores esperan en estos lenguajes, al tiempo que mantiene la estructura y el comportamiento de la implementación Rust subyacente.

```rust
// Ejemplo de archivo UDL para una biblioteca de billetera Bitcoin (wallet.udl)
namespace wallet {
// Funciones de espacio de nombres: llamadas directamente sin objeto
string generate_mnemonic();
Wallet create_wallet(string mnemonic);
};

// Diccionario (struct): se convierte en clase de datos en Kotlin y en estructura en Swift
dictionary Balance {
u64 confirmed_sats;
u64 pending_sats;
};

// Interfaz (clase con métodos) - se convierte en clase con métodos
interface Wallet {
// Constructor
constructor(string mnemonic);

// Métodos
Balance get_balance();
string get_new_address();
string send_to_address(string address, u64 amount_sats);
};

// Enumeración con datos: se asigna a una clase sellada (Kotlin) o una enumeración con valores asociados (Swift)
[Enum]
interface TransactionStatus {
Pending(u32 confirmations_needed);
Confirmed(u32 block_height);
Failed(string reason);
};

// Enumeración de error para tipos de resultados
[Error]
enum WalletError {
"InsufficientFunds",
"InvalidAddress",
"NetworkError",
};

// Función que puede fallar: lanza una excepción en el idioma de destino
interface Wallet {
[Throws=WalletError]
string send_to_address(string address, u64 amount_sats);
};
```

La implementación correspondiente de Rust definiría estos tipos e implementaría el atributo `uniffi::export` a los bindings de generate para Kotlin, Swift, Python y otros lenguajes soportados.

### Gestión de errores y funciones avanzadas

UniFFI proporciona una gestión de errores que preserva el modelo de errores basado en resultados de Rust y lo traduce adecuadamente a los idiomas de destino. Las funciones que devuelven tipos Result en Rust pueden marcarse con la palabra clave "throws" en UDL, especificando qué tipos de error pueden producir. Estos errores deben definirse como enums de error en el archivo UDL y deben implementar el rasgo Error estándar de Rust en el código Rust subyacente. La caja thiserror proporciona una macro conveniente para implementar este rasgo, reduciendo significativamente el código repetitivo.

La traducción de la gestión de errores demuestra el enfoque de UniFFI basado en el lenguaje. En Kotlin, las funciones marcadas como throw en UDL generate son métodos que lanzan excepciones siguiendo las convenciones Java/Kotlin. Los enlaces de Python utilizan de forma similar el modelo de excepciones de Python. Esta traducción garantiza que la gestión de errores resulte natural e idiomática en cada idioma de destino, al tiempo que preserva el significado semántico de los tipos de error originales de Rust.

Las interfaces de devolución de llamada representan otra característica avanzada que permite la comunicación bidireccional entre las bibliotecas Rust y las aplicaciones consumidoras. Cuando una biblioteca de Rust necesita devolver una llamada al código de la aplicación, los desarrolladores pueden definir rasgos en Rust y marcarlos como interfaces de devolución de llamada en UDL. La aplicación consumidora implementa estas interfaces en su lenguaje nativo, y UniFFI se encarga del complejo marshaling necesario para invocar estas llamadas de retorno desde el código Rust. Este patrón requiere una cuidadosa consideración de la seguridad de los hilos, ya que las retrollamadas pueden cruzar los límites de los hilos, necesitando límites de envío y sincronización en el lado de Rust.

### Aplicaciones reales y limitaciones actuales

UniFFI ha sido adoptado en la comunidad de desarrollo de criptomonedas y [blockchain](https://planb.academy/resources/glossary/blockchain), con importantes proyectos como BDK (Bitcoin Development Kit), LDK (Lightning Development Kit) y varias implementaciones de wallet que lo utilizan para proporcionar SDK móviles. Estos proyectos demuestran el uso de UniFFI en entornos de producción.

El examen de los archivos UDL reales de estos proyectos revela patrones y mejores prácticas que han surgido del uso práctico. El archivo UDL de BDK, por ejemplo, muestra cómo modelos de dominio complejos con múltiples enums, structs e interfaces pueden mapearse eficazmente para crear SDK móviles completos. La coherencia de la sintaxis UDL en diferentes proyectos significa que los desarrolladores familiarizados con una biblioteca compatible con UniFFI pueden entender y trabajar rápidamente con otras, creando un efecto de red que beneficia a todo el ecosistema.

Sin embargo, UniFFI tiene notables limitaciones que los desarrolladores deben tener en cuenta. La más significativa es la falta de soporte para interfaces asíncronas. Todos los enlaces generados son síncronos, por lo que los desarrolladores deben gestionar las operaciones asíncronas en su código Rust y presentar interfaces síncronas a las aplicaciones consumidoras. Además, la ubicación de la documentación presenta un desafío: la documentación escrita en el código de Rust no se transfiere a los enlaces generados, mientras que la documentación de los archivos UDL no está disponible para los consumidores directos de la biblioteca Rust. Aunque se están realizando esfuerzos para solucionar estas limitaciones mediante el análisis sintáctico y la generación automáticos, siguen siendo consideraciones a tener en cuenta en las implementaciones actuales. Por último, UniFFI genera enlaces lingüísticos, pero no se encarga del empaquetado y la distribución específicos para cada plataforma, por lo que los desarrolladores deben ocuparse de los pasos finales de creación de paquetes distribuibles para cada plataforma de destino.

# Desarrollo de LNP/BP con SDK

<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>

## Nodo LN en SDK

<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>

:::video id=94b9bee6-154e-4b9c-a8ce-5e2d9e9656a2:::

### Comprender la arquitectura modular de LDK

El kit de desarrollo Lightning (LDK) adopta un enfoque diferente para la implementación de [Lightning Network](https://planb.academy/resources/glossary/lightning-network) en comparación con el software de [nodos](https://planb.academy/resources/glossary/node) tradicional como CLightning o LND. Mientras que los nodos Lightning convencionales funcionan como aplicaciones daemon completas que se ejecutan continuamente en una máquina, LDK funciona como una biblioteca Rust modular que proporciona componentes primitivos para crear soluciones Lightning personalizadas. Esta distinción arquitectónica hace que LDK sea flexible, permitiendo a los desarrolladores ensamblar la funcionalidad Lightning de forma que sirva a los requisitos específicos de su proyecto.

La filosofía básica de LDK se centra en la modularidad y la adaptabilidad. En lugar de proporcionar una solución monolítica, LDK ofrece componentes individuales que pueden combinarse, personalizarse o sustituirse por completo. Cada componente viene con implementaciones predeterminadas que funcionan de inmediato, pero los desarrolladores conservan la libertad de sustituir sus propias implementaciones cuando sea necesario. Por ejemplo, LDK incluye implementaciones predeterminadas para la supervisión de blockchain, la firma de transacciones y la comunicación de red, pero cualquiera de ellas puede sustituirse por soluciones personalizadas adaptadas a casos de uso o entornos específicos.

Este diseño modular permite a LDK funcionar en diversas plataformas y escenarios que supondrían un reto para los nodos Lightning tradicionales. Las aplicaciones móviles, los navegadores web, los dispositivos integrados y el hardware especializado pueden aprovechar los componentes de LDK de forma que se adapten a sus limitaciones y requisitos exclusivos. La arquitectura de la biblioteca garantiza que los desarrolladores puedan crear aplicaciones compatibles con Lightning sin estar sujetos a patrones operativos predeterminados o dependencias del sistema.

### Casos de uso de LDK y flexibilidad de la plataforma

La flexibilidad arquitectónica de LDK abre numerosos casos de uso que van mucho más allá de las implantaciones tradicionales de nodos Lightning. El desarrollo móvil de wallet representa una de las aplicaciones más atractivas, donde LDK permite la creación de carteras Lightning no custodiadas similares a Phoenix wallet. Estas implementaciones móviles pueden mantener el control del usuario sobre las [claves privadas](https://planb.academy/resources/glossary/private-key) a la vez que se sincronizan con los proveedores de servicios Lightning (LSP) cuando se conectan, lo que permite una recepción de pagos y una gestión de canales fluidas incluso con conectividad intermitente.

La integración del módulo de seguridad de hardware (HSM) muestra otro potente caso de uso de LDK. Al extraer solo los componentes de firma y verificación de transacciones, los desarrolladores pueden crear dispositivos de firma conscientes de Lightning que entienden el contexto y las implicaciones de las transacciones Lightning. Esta capacidad va más allá de la simple firma de transacciones e incluye un análisis inteligente del reenvío de pagos, las operaciones de [canal](https://planb.academy/resources/glossary/payment-channel) y las decisiones críticas para la seguridad. El HSM puede evaluar si una transacción representa un pago legítimo, una operación de enrutamiento o un intento potencialmente malicioso, proporcionando a los usuarios información de seguridad significativa.

Las aplicaciones Lightning basadas en Web se benefician significativamente de la filosofía de diseño sin llamadas al sistema de LDK. Dado que los entornos WebAssembly carecen de acceso directo a recursos del sistema como sistemas de archivos, sockets de red o fuentes de entropía, el enfoque puro de LDK permite que la funcionalidad Lightning funcione sin problemas en entornos de navegador. Los desarrolladores pueden implementar capas de red personalizadas mediante WebSockets y proporcionar fuentes de persistencia y aleatoriedad compatibles con navegadores, manteniendo al mismo tiempo la plena conformidad con el protocolo Lightning.

### Componentes básicos y arquitectura basada en eventos

La arquitectura interna de LDK gira en torno a varios componentes clave que trabajan juntos a través de un sistema basado en eventos. El sistema de gestión de pares gestiona todas las comunicaciones con otros nodos Lightning, implementando el protocolo de ruido para el cifrado y gestionando las estructuras de mensajes para el cumplimiento del protocolo Lightning. Este componente funciona independientemente del mecanismo de transporte subyacente, lo que permite a los desarrolladores implementar la conexión en red a través de sockets TCP, WebSockets, conexiones serie USB o cualquier otro canal de comunicación bidireccional.

El gestor de canales actúa como coordinador central de las operaciones del canal Lightning y colabora estrechamente con el gestor de pares para ejecutar las operaciones de apertura, cierre y pago del canal. Cuando un desarrollador inicia la apertura de un canal, el gestor de canales crea los mensajes de protocolo necesarios y se coordina con el gestor de pares para gestionar el proceso de negociación de varios pasos. Esta separación de preocupaciones permite una abstracción limpia entre la lógica del protocolo Lightning y los detalles de comunicación de la red.

El sistema de eventos de LDK proporciona notificaciones asíncronas para todas las operaciones y cambios de estado significativos. Los eventos cubren todo el espectro de operaciones de Lightning, desde conexiones y desconexiones de pares hasta éxitos y fracasos de pagos, cambios de estado de canales y confirmaciones de blockchain. Este enfoque basado en eventos permite a las aplicaciones responder adecuadamente a la actividad de la red Lightning, manteniendo una separación limpia entre la funcionalidad central de LDK y la lógica específica de la aplicación. Los desarrolladores pueden implementar controladores de eventos personalizados que actualicen las interfaces de usuario, activen notificaciones o inicien acciones de seguimiento basadas en eventos de la red Lightning.

### Blockchain Integración y gestión de datos

La integración de datos Blockchain representa una de las capas de abstracción de LDK, diseñada para acomodar desde nodos Bitcoin completos hasta clientes móviles ligeros. LDK admite dos modos principales de interacción con la cadena de bloques, cada uno optimizado para diferentes limitaciones de recursos y requisitos operativos. El modo de bloque completo permite a las aplicaciones con acceso a los datos completos de la cadena de bloques pasar bloques enteros a LDK, lo que permite una supervisión exhaustiva de las transacciones y una respuesta inmediata a los eventos relevantes de la cadena de bloques.

Para entornos con recursos limitados, LDK ofrece un enfoque basado en filtrado que reduce los requisitos de ancho de banda y almacenamiento. En este modo, LDK comunica sus intereses de supervisión a través de interfaces abstractas, solicitando la vigilancia de ID de transacciones específicas, [UTXO](https://planb.academy/resources/glossary/utxo) o patrones de secuencias de comandos. La capa de aplicación puede entonces implementar esta vigilancia utilizando servidores Electrum, exploradores de bloques u otras fuentes de datos ligeras de blockchain. Este enfoque permite que las wallets móviles y las aplicaciones web mantengan la funcionalidad Lightning sin requerir una sincronización completa de la blockchain.

La capa de persistencia en LDK sigue los mismos principios de abstracción, proporcionando a las aplicaciones blobs de datos binarios que deben ser almacenados y recuperados de forma fiable. LDK maneja toda la complejidad de serializar y deserializar estados de canales de Lightning, datos de chismes de red y otra información crítica. Las aplicaciones solo tienen que implementar mecanismos de almacenamiento fiables, ya sea mediante sistemas de archivos locales, servicios de almacenamiento en la nube o sistemas de bases de datos especializados. Este diseño garantiza que la gestión de estados de Lightning siga siendo sólida, al tiempo que permite a las aplicaciones elegir soluciones de almacenamiento que se ajusten a sus requisitos operativos y modelos de seguridad.

### Funciones avanzadas y modelos de integración

Las capacidades de LDK se extienden a funciones de Lightning Network como los pagos multitrayectoria, la optimización de rutas y la gestión de cotilleos de red. El sistema de enrutamiento mantiene una visión completa de la topología de Lightning Network mediante la participación en el protocolo de cotilleo, lo que permite encontrar rutas inteligentes para los pagos. Las aplicaciones pueden influir en las decisiones de enrutamiento a través de parámetros de configuración e incluso implementar una lógica de enrutamiento personalizada para casos de uso especializados.

El sistema de vinculación de lenguajes de la biblioteca permite la integración de LDK a través de múltiples entornos de programación, soportando Java, Kotlin, Swift, TypeScript, JavaScript y C++. Esta compatibilidad entre plataformas permite que las aplicaciones móviles escritas en lenguajes nativos incorporen la funcionalidad de Lightning manteniendo unas características de rendimiento óptimas. El sistema de vinculación conserva la arquitectura basada en eventos y el diseño modular de LDK en todos los lenguajes compatibles, lo que garantiza experiencias coherentes para los desarrolladores independientemente de la plataforma de destino.

La estimación de comisiones y la emisión de transacciones representan áreas adicionales en las que LDK ofrece flexibilidad. Las aplicaciones pueden aplicar estrategias personalizadas de estimación de comisiones que tengan en cuenta sus pautas operativas específicas y los requisitos de los usuarios. Del mismo modo, la difusión de transacciones puede personalizarse para trabajar con varias interfaces de red Bitcoin, desde conexiones directas a nodos completos hasta servicios de difusión de terceros. Esta flexibilidad garantiza que las aplicaciones basadas en LDK puedan optimizar sus interacciones de blockchain para sus casos de uso particulares, manteniendo al mismo tiempo el cumplimiento del protocolo Lightning y las normas de seguridad.

## Breez sdk

<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>

:::video id=68d1f253-6210-4eab-8329-b676e5772eac:::

### El reto del desarrollo de Lightning

Desarrollar aplicaciones que integren pagos Lightning supone una barrera importante para la mayoría de los desarrolladores. Para crear una aplicación con funciones de pago Lightning, los desarrolladores deben convertirse en expertos en Lightning y comprender conceptos complejos como la gestión de canales, el equilibrio de liquidez y la topología de la red. Este requisito de conocimientos crea un problema fundamental para la adopción de Lightning: aunque la red Lightning en sí es operativa y los pagos son fiables, la complejidad técnica impide una integración generalizada en las aplicaciones cotidianas.

El principal reto radica en la brecha existente entre lo que necesitan los desarrolladores y lo que quieren ofrecer. Los desarrolladores suelen trabajar con plazos ajustados y prefieren soluciones sencillas que les permitan centrarse en la funcionalidad principal de su aplicación en lugar de convertirse en expertos en infraestructura de pagos. Cuando la integración de Lightning es difícil, los desarrolladores gravitan naturalmente hacia las soluciones de custodia porque ofrecen el camino de menor resistencia. Sin embargo, esta tendencia hacia los servicios de custodia socava la propuesta de valor fundamental de Bitcoin de soberanía financiera sin custodia.

### La visión de Breez, Lightning por todas partes

Breez surgió de una visión simple pero ambiciosa: conseguir que todo el mundo se conecte a la red Lightning a través de interfaces intuitivas para la economía Lightning. El enfoque de la empresa reconoce que, aunque la red Lightning funciona bien técnicamente, necesita desesperadamente la adopción de los usuarios para alcanzar todo su potencial. Este reto de adopción va más allá de los usuarios individuales para abarcar todo el ecosistema de aplicaciones y servicios que podrían beneficiarse de la integración de Lightning.

La aplicación original Breez demostró esta visión proporcionando a los usuarios un nodo Lightning no custodial que funcionaba directamente en sus teléfonos móviles. Esta aplicación mostraba las capacidades de Lightning, como la transmisión de micropagos a podcasters y la funcionalidad de punto de venta. Sin embargo, la aplicación Breez también reveló una limitación arquitectónica crítica: el ecosistema de aplicaciones móviles no facilita la comunicación entre aplicaciones, lo que obliga a los desarrolladores a crear todas las funciones relacionadas con Lightning en una única aplicación en lugar de permitir que las aplicaciones especializadas aprovechen la infraestructura compartida de Lightning.

Los aprendizajes de la empresa a partir de la aplicación Breez condujeron a una idea crucial: el futuro de la adopción de Lightning depende de ganarse a los desarrolladores. Si la integración de Lightning sin custodia se convierte en la opción más sencilla para los desarrolladores, se convertirá en la opción por defecto. Este enfoque también ofrece ventajas normativas, ya que el software sin custodia se enfrenta a menos obstáculos normativos que los servicios de custodia, lo que facilita a los desarrolladores el envío de sus aplicaciones a todo el mundo.

### Arquitectura del SDK de Breez

El SDK Breez proporciona un enfoque alternativo para integrar la funcionalidad Lightning en las aplicaciones. En lugar de requerir que cada aplicación ejecute su propio nodo Lightning, el SDK proporciona una arquitectura que mantiene los principios de no custodia al tiempo que simplifica la experiencia del desarrollador. En esencia, el SDK proporciona a cada usuario final su propio nodo Lightning personal que se ejecuta en la infraestructura Greenlight, el servicio de alojamiento de nodos Lightning basado en la nube de Blockstream.

Esta arquitectura resuelve simultáneamente varios problemas críticos. Los usuarios no tienen que preocuparse por la gestión de la base de datos, el tiempo de actividad del servidor o el mantenimiento de la infraestructura, preocupaciones que resultarían abrumadoras para los consumidores típicos. Sin embargo, a diferencia de las soluciones de custodia tradicionales, Greenlight nunca tiene acceso a las claves de los usuarios. El nodo Lightning en la nube no puede realizar ninguna operación sin una aplicación conectada activamente que pueda firmar transacciones y mensajes. Este diseño mantiene las ventajas de seguridad de la autocustodia al tiempo que elimina la complejidad operativa.

El SDK también admite la interoperabilidad. Múltiples aplicaciones pueden conectarse al nodo Lightning del mismo usuario utilizando la misma frase seed, lo que permite a los usuarios mantener un único saldo Lightning a través de diferentes aplicaciones especializadas. Por ejemplo, un usuario puede tener tanto una aplicación general Lightning wallet como una aplicación especializada en podcasting, ambas accediendo a los mismos fondos y canales Lightning. Esta arquitectura permite el desarrollo de aplicaciones centradas y especializadas, manteniendo al mismo tiempo una infraestructura financiera unificada.

### Proveedores de servicios Lightning y liquidez justo a tiempo

Un componente fundamental del SDK Breez es su integración con los proveedores de servicios Lightning (LSP), que funcionan de forma análoga a los proveedores de servicios de Internet pero para la red Lightning. Los LSP resuelven uno de los retos más complejos de Lightning: la gestión de la liquidez. En los canales Lightning, los fondos solo pueden fluir en las direcciones donde existe liquidez, de forma similar a las cuentas de un ábaco que solo pueden moverse donde hay espacio.

El SDK implementa canales "justo a tiempo" a través de los PSL, gestionando automáticamente la liquidez sin intervención del usuario. Cuando un usuario necesita recibir un pago pero carece de suficiente liquidez entrante, el PSL abre automáticamente un nuevo canal Lightning en el momento en que llega el pago. Este proceso se produce sin problemas en segundo plano, garantizando que los usuarios siempre puedan recibir pagos sin entender la mecánica subyacente del canal.

Esta integración LSP va más allá de la simple gestión de liquidez. El SDK incluye una completa funcionalidad Lightning desde el primer momento: servicios de vigilancia integrados para la seguridad, interoperabilidad on-chain a través de swaps submarinos, rampas de entrada fiat a través de servicios como MoonPay y compatibilidad con protocolos LNURL. El sistema también proporciona copias de seguridad y recuperación sin fisuras, garantizando que los usuarios nunca pierdan el acceso a sus fondos, incluso si los proveedores de infraestructura cambian o dejan de estar disponibles.

### Experiencia en implantación y desarrollo

El SDK Breez prioriza la experiencia del desarrollador a través de su enfoque integral y con pilas incluidas. El SDK proporciona bindings para múltiples lenguajes de programación, incluidos Rust, Swift, Kotlin, Python, Go, React Native, Flutter y C#, lo que permite a los desarrolladores integrar pagos Lightning utilizando sus herramientas de desarrollo preferidas. La arquitectura se abstrae de la complejidad de Lightning a través de API, al tiempo que mantiene la seguridad de la red Lightning.

Los componentes clave trabajan juntos para proporcionar esta experiencia simplificada. El analizador de entradas gestiona automáticamente los distintos formatos de pago, determinando si una cadena representa una [factura](https://planb.academy/resources/glossary/invoice-lightning), LNURL u otro método de pago y dirigiéndola a la función de gestión adecuada. El firmante integrado gestiona todas las operaciones criptográficas en segundo plano, mientras que el intercambiador maneja las interacciones on-chain de forma transparente. Este diseño permite a los desarrolladores centrarse en la propuesta de valor única de su aplicación en lugar de convertirse en expertos en infraestructura Lightning.

La arquitectura sin confianza del SDK garantiza que, aunque Greenlight pueda observar los estados de los canales y la información de enrutamiento, no puede acceder a los fondos de los usuarios ni realizar operaciones no autorizadas. Los usuarios mantienen el control total sobre sus claves privadas, que nunca salen de sus dispositivos. Este enfoque representa un compromiso cuidadosamente estudiado entre la simplicidad operativa y la privacidad, proporcionando una vía práctica para la adopción generalizada de Lightning y preservando al mismo tiempo los principios básicos de soberanía financiera de Bitcoin.

## LDK frente a Breez SDK

<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>

:::video id=c3dec3df-1416-4761-b7c8-e1d66d27e390:::

### Comprender las limitaciones de Lightning Development Kit (LDK)

El kit de desarrollo Lightning es una colección de bibliotecas Rust diseñadas para proporcionar a los desarrolladores flexibilidad a la hora de crear aplicaciones Lightning Network. Sin embargo, esta flexibilidad conlleva importantes retos de implementación que se pusieron de manifiesto durante el desarrollo real en Lipa. La naturaleza de bajo nivel de LDK obliga a los desarrolladores a gestionar numerosas tareas complejas de forma independiente, desde la sincronización de grafos de red hasta la optimización del enrutamiento de pagos. Aunque este enfoque ofrece un control total sobre la implementación de Lightning, requiere importantes recursos de desarrollo y profundos conocimientos técnicos para lograr una fiabilidad lista para la producción.

Una de las características más críticas que faltaban en LDK era la compatibilidad con LNURL, una norma ampliamente adoptada que simplifica las interacciones Lightning Network para los usuarios finales. Además, la ausencia de salidas de anclaje planteaba graves problemas operativos, sobre todo en entornos con tarifas elevadas. Las salidas Anchor resuelven un problema fundamental de los cierres forzosos de canales Lightning: cuando las tarifas de red aumentan drásticamente, los canales con tarifas predefinidas pueden resultar imposibles de cerrar unilateralmente porque la tarifa preestablecida se vuelve insuficiente para la confirmación de la transacción. Esta limitación resulta especialmente problemática para las aplicaciones móviles wallet, en las que los usuarios pueden abandonar la wallet sin coordinar el cierre cooperativo de canales, lo que deja los fondos potencialmente varados durante los picos de las tarifas.

La relativa inmadurez de la LDK también se manifestó en un enrutamiento de pagos poco fiable, un problema crítico para cualquier aplicación Lightning. A pesar de ser una implementación técnicamente sólida, el amplio alcance del LDK como solución genérica dificultaba la rápida resolución de problemas específicos. El equipo de desarrollo tuvo que dedicar un tiempo considerable a solucionar problemas de enrutamiento y a implementar funciones que, idealmente, deberían gestionarse a nivel de biblioteca, lo que, en última instancia, afectó a la velocidad de desarrollo y a la calidad de la experiencia del usuario.

### Descubra las ventajas de Breez SDK y Greenlight

La transición al SDK Breez representó un cambio en el enfoque arquitectónico, pasando de un nodo Lightning autogestionado a una solución basada en la nube impulsada por el servicio Greenlight de Blockstream. Este cambio abordó de inmediato varios puntos críticos experimentados con la implementación de LDK. La mejora más significativa se produjo en la fiabilidad de los pagos, debido principalmente a la capacidad de Greenlight para mantener un gráfico de red siempre actualizado. A diferencia de las implementaciones móviles tradicionales de Lightning, que deben sincronizar la información de red cuando se inicia la aplicación, los nodos de Greenlight se ejecutan continuamente en la nube, manteniendo el conocimiento de la red en tiempo real y proporcionando al instante datos completos del gráfico cuando los usuarios se conectan.

Esta arquitectura aprovecha la implementación Core Lightning (CLN) probada en combate, que lleva años enrutando pagos con éxito como una de las implementaciones originales de Lightning Network. La experiencia acumulada y la fiabilidad demostrada de CLN proporcionaron mejoras de estabilidad inmediatas con respecto al proyecto LDK más joven. Cuando los usuarios activan su wallet impulsado por Greenlight, heredan al instante todo el conocimiento de la red y las capacidades de enrutamiento de un nodo Lightning en funcionamiento continuo, lo que elimina los retrasos de sincronización y las incertidumbres de enrutamiento que plagaban la implementación anterior.

La filosofía de diseño basada en opiniones del SDK de Breez resultó útil para el desarrollo de wallets. En lugar de proporcionar un kit de herramientas Lightning genérico, Breez se centra específicamente en aplicaciones wallet de usuario final, lo que permite al equipo de desarrollo concentrar sus esfuerzos en crear soluciones integrales para este caso de uso específico. Este enfoque específico permitió a Breez integrar servicios esenciales directamente en el SDK, incluida la funcionalidad Lightning Service Provider (LSP) que permite a los usuarios recibir pagos inmediatamente después de la instalación de wallet, sin necesidad de procedimientos manuales de apertura de canales.

### Funciones completas y mejoras de la experiencia de usuario

El enfoque integrado del SDK de Breez va más allá de la funcionalidad básica de Lightning, incorporando funciones que mejoran la experiencia del usuario. La integración LSP incorporada elimina la barrera tradicional de exigir a los usuarios que entiendan la gestión de canales, lo que permite la recepción inmediata de pagos para las nuevas instalaciones de wallet. Este proceso de incorporación ayuda a la adopción generalizada, ya que los usuarios pueden empezar a recibir pagos Lightning sin conocimientos técnicos ni procedimientos de configuración.

La funcionalidad de intercambio en cadena proporciona otra capa de optimización de la experiencia del usuario al permitir la presentación de un saldo unificado a los usuarios. En lugar de obligar a los usuarios a entender la distinción entre Lightning y on-chain Bitcoin, el servicio de intercambio permite la conversión automática entre estas capas según sea necesario. Cuando los usuarios necesitan realizar pagos de on-chain, el sistema puede intercambiar sin problemas fondos de Lightning a on-chain Bitcoin entre bastidores, manteniendo la ilusión de un saldo único y líquido a la vez que gestiona la complejidad técnica internamente.

La compatibilidad del SDK con las reservas de canal cero resuelve un importante problema de experiencia de usuario en las implementaciones tradicionales de Lightning. Las reservas de canal normalmente impiden a los usuarios gastar todo el saldo mostrado, lo que crea confusión cuando los pagos fallan a pesar de que aparentemente hay fondos suficientes. Al eliminar estas reservas, Breez permite a los usuarios gastar todo el saldo mostrado, aunque esto requiere que el PSL acepte un riesgo adicional. Esta solución de compromiso ejemplifica el enfoque centrado en el usuario de Breez, en el que la complejidad técnica y el riesgo son absorbidos por los proveedores de servicios para crear experiencias de usuario intuitivas.

Funciones adicionales como la compatibilidad con LNURL, los servicios de tipo de cambio y la sincronización multidispositivo demuestran aún más el enfoque integral del SDK para el desarrollo de wallets. La arquitectura basada en la nube permite a los usuarios acceder a su nodo Lightning desde varios dispositivos o aplicaciones, y Breez gestiona la sincronización de estados entre estos distintos puntos de acceso. Entre los futuros elementos de la hoja de ruta se incluyen la funcionalidad "spend-all" para el drenaje completo de wallet, el empalme para la gestión dinámica de canales y un mercado de LSP competidores para introducir una competencia sana en la prestación de servicios.

### Evaluación de las ventajas y desventajas y de los problemas de centralización

La transición a Breez SDK y Greenlight introduce importantes compensaciones de centralización que deben considerarse cuidadosamente en el contexto de los principios de descentralización de Bitcoin. La arquitectura basada en la nube significa que los nodos Lightning de los usuarios operan en la infraestructura de Blockstream, creando dependencias tanto del funcionamiento continuado de Greenlight como del desarrollo en curso de Breez. Esta centralización va más allá de la mera comodidad, ya que puede afectar a la capacidad de los usuarios para recuperar fondos si los servicios dejan de estar disponibles o si se produce la censura.

Los escenarios de recuperación presentan retos particulares en esta arquitectura. Aunque los usuarios conservan el control de sus claves privadas, acceder a los fondos sin la infraestructura de Greenlight requeriría conocimientos técnicos para poner en marcha nodos Core Lightning independientes y restaurar los estados de los canales. Para los usuarios individuales, este proceso de recuperación probablemente resultaría prohibitivamente complejo, e incluso los proveedores de wallet se enfrentarían a importantes dificultades para migrar bases enteras de usuarios a una infraestructura alternativa si se interrumpieran los servicios de Greenlight.

Las consideraciones de privacidad también cambian con este cambio arquitectónico. El enrutamiento basado en la nube significa que Greenlight puede obtener visibilidad de los destinos de los pagos, mientras que las anteriores arquitecturas basadas únicamente en LSP limitaban la fuga de información a los importes y los plazos de los pagos. La generación de factura en la nube amplía aún más la exposición potencial de la información, ya que las facturas no utilizadas que antes permanecían privadas en los dispositivos de los usuarios ahora pasan a través de la infraestructura de Blockstream.

A pesar de estas preocupaciones sobre la centralización, los beneficios prácticos a menudo superan los riesgos teóricos para muchos casos de uso. La mayor fiabilidad, el amplio conjunto de funciones y la experiencia de usuario superior permiten a los desarrolladores de wallets centrarse en las innovaciones de la capa de aplicación en lugar de en la gestión de la infraestructura de Lightning. Esta división del trabajo refleja la maduración de un ecosistema en el que los proveedores de servicios especializados se encargan de los retos técnicos complejos, lo que permite a los desarrolladores de aplicaciones concentrarse en la experiencia del usuario y la lógica empresarial. La clave reside en entender claramente estas compensaciones y tomar decisiones informadas basadas en los requisitos de casos de uso específicos y los niveles de tolerancia al riesgo.

# Sección final

<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>

## Opiniones y valoraciones

<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusión

<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>

<isCourseConclusion>true</isCourseConclusion>