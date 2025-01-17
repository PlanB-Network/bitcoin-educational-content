---
name: Los fundamentos de GitHub
description: Entendiendo los fundamentos de Git y GitHub
---

![cover](assets/cover.webp)

La misión de PlanB es proporcionar recursos educativos de primer nivel sobre Bitcoin, disponibles en tantos idiomas como sea posible. Todo el contenido publicado en el sitio es de código abierto y alojado en GitHub, ofreciendo a cualquier persona la oportunidad de contribuir al enriquecimiento de la plataforma. Las contribuciones pueden tomar varias formas: corregir y revisar textos existentes, traducir a otros idiomas, actualizar información o crear nuevos tutoriales aún no disponibles en nuestro sitio.

Si deseas contribuir a la Red PlanB, necesitarás usar Git y GitHub. Si estas herramientas te son desconocidas o si su funcionamiento te parece oscuro, ¡no te preocupes, este artículo es para ti! Revisaremos juntos los fundamentos de Git y GitHub, así como el argot técnico asociado, para permitirte utilizar estas herramientas de manera efectiva después.

## ¿Qué es Git?

Git es un sistema de control de versiones, diseñado específicamente para gestionar proyectos de software. Creado en 2005 por Linus Torvalds, Git rápidamente se convirtió en el estándar en la industria del desarrollo de software para el control de versiones. Pero, ¿qué significa exactamente eso?
![git](assets/1.webp)
En su núcleo, Git permite a los desarrolladores rastrear los cambios realizados en el código fuente de un proyecto a lo largo del tiempo. Esto significa que con cada cambio en el código, Git registra una nueva versión del proyecto. Si ocurre un error o si una característica experimental no funciona como se esperaba, es posible revertir a un estado anterior del código, como una especie de máquina del tiempo para archivos.

Una de las características clave de Git es la gestión de ramas. Una rama es una especie de línea paralela donde los desarrolladores pueden trabajar independientemente del resto del proyecto. Esto facilita enormemente la adición de nuevas características o la corrección de errores sin perturbar el código principal. Una vez que las modificaciones son probadas y validadas, pueden fusionarse con la rama principal.

Una de las peculiaridades de Git es su capacidad para operar de manera distribuida. Cada desarrollador tiene una copia completa del proyecto en el disco duro de su propio ordenador, lo que les permite trabajar sin conexión y fusionar los cambios más tarde cuando esté disponible una conexión a Internet. Esto reduce el riesgo de conflictos y permite que varios desarrolladores trabajen simultáneamente en el mismo proyecto sin estorbarse mutuamente.
Inicialmente, Git fue diseñado principalmente para proyectos de desarrollo de software. Sin embargo, también se puede utilizar para gestionar proyectos de escritura de contenido. En lugar de colaborar en código, colaboramos en texto. Y es precisamente este método el que la Red PlanB ha adoptado para gestionar su contenido. Git facilita la colaboración en la escritura de cursos y tutoriales, ya que permite un seguimiento preciso de los cambios, una gestión eficiente de versiones y también habilita la revisión y mejora del contenido por otros colaboradores.
## ¿Qué es GitHub?

GitHub es una plataforma de gestión y alojamiento de código fuente basada en el sistema de control de versiones Git del que acabamos de hablar. Lanzado en 2008, GitHub rápidamente ganó popularidad y se ha convertido en una referencia esencial para desarrolladores en todo el mundo. Pero, ¿en qué se diferencia GitHub de Git y por qué es tan crucial en nuestro método de producción de contenido?
![github](assets/2.webp)
Primero, es importante entender que GitHub está construido sobre Git (del cual hablamos en la sección anterior). Mientras que Git es la herramienta que rastrea los cambios en el código, GitHub es el servicio en línea que aloja, comparte y gestiona este código.

Imagina Git como una especie de libro de registro que cada desarrollador usa en su propio ordenador para registrar todos los cambios en su proyecto. GitHub, por otro lado, es como una biblioteca pública donde todos estos libros de registro pueden ser compartidos, comparados y combinados.
La diferencia fundamental entre Git y GitHub radica en su función: Git es la herramienta utilizada localmente por cada desarrollador para gestionar sus versiones de código, mientras que GitHub es la plataforma en línea que aloja estas versiones y facilita la colaboración.
GitHub es mucho más que un simple servicio de alojamiento de código. Es una plataforma de colaboración que permite a los desarrolladores trabajar juntos de manera eficiente. Y de hecho, PlanB Network utiliza esta plataforma para alojar no solo todo el código que impulsa el sitio web, sino también, y esto es lo que nos interesa, todo el contenido (tutoriales, formación, recursos...).

## Algunos Términos Técnicos

En Git y GitHub, te encontrarás con comandos y características cuyos nombres pueden parecer complejos. En esta última parte, proporciono definiciones simples para entender los términos técnicos que podrías encontrar al usar Git y GitHub:

- **Fetch origin:** Comando que recupera información reciente y cambios de un repositorio remoto sin fusionarlos con tu trabajo local. Actualiza tu repositorio local con nuevas ramas y commits presentes en el repositorio remoto.

- **Pull origin:** Comando que recupera actualizaciones de un repositorio remoto e inmediatamente las integra en tu rama local para sincronizarla. Esto combina los pasos de fetch y merge en un solo comando.
- **Sync Fork:** Una característica en GitHub que te permite actualizar tu bifurcación de un proyecto con los últimos cambios del repositorio fuente. Esto asegura que tu copia del proyecto se mantenga actualizada con el desarrollo principal.
- **Push origin:** Comando utilizado para enviar tus cambios locales a un repositorio remoto.

- **Pull Request:** Una solicitud enviada por un colaborador para indicar que han enviado cambios a una rama en un repositorio remoto y desean que estos cambios sean revisados y potencialmente fusionados en la rama principal del repositorio.

- **Commit:** Guardar tus cambios. Un commit es como una instantánea instantánea de tu trabajo en un momento dado, lo que permite mantener un historial de cambios. Cada commit incluye un mensaje descriptivo explicando qué ha sido modificado.

- **Branch:** Una versión paralela del repositorio, que te permite trabajar en cambios sin afectar la rama principal (a menudo llamada "main" o "master"). Las ramas facilitan el desarrollo de nuevas características y la corrección de errores sin el riesgo de interrumpir el código estable.

- **Merge:** Fusionar consiste en integrar los cambios de una rama en otra. Se utiliza, por ejemplo, para añadir los cambios de una rama de trabajo a la rama principal, lo que permite agregar las diversas contribuciones.

- **Fork:** Bifurcar un repositorio significa crear una copia de ese repositorio en tu propia cuenta de GitHub, lo que te permite trabajar en el proyecto sin afectar el repositorio original. La bifurcación puede tomar su propio camino y convertirse en un proyecto diferente del original, o puede sincronizarse regularmente con el proyecto original para contribuir a él.

- **Clone:** Clonar un repositorio significa hacer una copia local en tu computadora, lo que te da acceso a todos los archivos y el historial. Esto te permite trabajar directamente en el proyecto localmente.

- **Repository:** Espacio de almacenamiento para un proyecto en GitHub. Un repositorio contiene todos los archivos del proyecto así como el historial de todos los cambios que se han realizado en él. Es la base del almacenamiento y la colaboración en GitHub.

- **Issue:** Una herramienta para rastrear tareas y errores en GitHub. Los issues permiten reportar problemas, proponer mejoras o discutir nuevas características. Cada issue puede ser asignado, etiquetado y comentado.

Esta lista obviamente no es exhaustiva. Hay muchos otros términos técnicos específicos para Git y GitHub. Sin embargo, los mencionados aquí son los principales con los que te encontrarás frecuentemente.
Después de leer este artículo, es posible que algunos aspectos de Git y GitHub todavía no te sean claros. Te animo a que empieces a utilizar estas herramientas por ti mismo. ¡La práctica es a menudo la mejor manera de entender cómo funciona la máquina! Y para comenzar, puedes descubrir estos otros 2 tutoriales:
**[Crea tu cuenta de GitHub](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Configurando Tu Entorno Local para Contribuir a PlanB Network](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**