---
name: Pautas de corrección
description: ¿Cuáles son los factores importantes que hay que tener en cuenta al corregir en Plan ₿ Network?
---

![github](assets/cover.webp)


Bienvenido a este tutorial sobre las **directrices a seguir al revisar contenidos en Plan ₿ Network**. Nos complace que comparta nuestra misión de traducir los materiales de Bitcoin al mayor número de idiomas posible, con el fin de ayudar a la gente a conocer mejor cómo funciona y cómo puede utilizarse en su vida cotidiana.


En primer lugar, contribuir al [repositorio público] de Plan ₿ Network(https://github.com/PlanB-Network/Bitcoin-educational-content) te da la oportunidad de escribir tutoriales, corregir el contenido existente o incluso proponer la adición de un nuevo idioma a la plataforma. Para saber más, únete primero a nuestro [grupo de Telegram](https://t.me/PlanBNetwork_ContentBuilder) y escribe una breve presentación sobre ti y los idiomas que puedes hablar.


El presente tutorial está dedicado a los colaboradores que desean corregir contenidos. La mayoría de ellos no saben mucho acerca de [Github](https://planb.network/en/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) o el [lenguaje Markdown](https://www.markdownguide.org/basic-syntax/) que utilizamos dentro del repositorio, por lo que es importante compartir algunas ideas sobre los factores clave que intervienen en esta tarea.


A continuación, he reunido los problemas más comunes con los que se encuentran los correctores. Siéntase libre de sugerir más, ya que puede ayudar a otros a mejorar.


Antes de entrar en materia, lo primero que hay que hacer es leer este tutorial sobre las acciones prácticas que hay que seguir en Github, bifurcando el repositorio Plan ₿ Network, confirmando cambios y enviando PR:


https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6


## ¿Qué es la corrección de pruebas?


La corrección de pruebas es el proceso de revisión final de un texto escrito, para identificar y corregir errores gramaticales, ortográficos, de puntuación y de formato. Garantiza que el texto sea claro, coherente y sin errores antes de su publicación o presentación.


Cuando realice este tipo de tareas, es importante que siga el sentido de la lengua original (EN o FR), pero asegúrese de que el texto en la lengua final sea lo más fluido posible para un hablante nativo.


Recuerde siempre que la traducción/revisión es EDUCACIÓN


De hecho, nuestro objetivo común es educar al mayor número posible de personas sobre la Bitcoin, por lo que es fundamental que el material que lean sea fluido y claro.

En este sentido, todos los colaboradores de Plan ₿ Network son educadores


## Los primeros pasos antes de corregir en Plan ₿ Network


Antes de empezar una nueva tarea de corrección, anúnciala en el [grupo de Telegram](https://t.me/PlanBNetwork_ContentBuilder) o informa a tu coordinador de Plan ₿ Network, que abrirá un [tema] dedicado (https://github.com/orgs/PlanB-Network/projects/3). Cuando reciba el enlace de la cuestión, simplemente **comente que va a empezar** con la tarea de corrección de ese contenido.


Este sistema ayuda al coordinador a seguir el progreso dentro del repositorio, y permite que el contenido sea "reclamado" por el corrector, lo que evita la duplicación de esfuerzos por parte de otra persona.

En la propia edición, encontrarás los enlaces que te redirigen al contenido a comprobar. Puedes simplemente hacer clic en ellos, o, incluso mejor, puedes volver a tu propio repositorio y trabajar directamente desde allí. ¡Veamos cómo puedes hacerlo!


En primer lugar, **recuerda SIEMPRE SINCRONIZAR tu repo, en la rama "dev "**. De esta forma, el contenido siempre estará actualizado antes de que inicies cualquier tipo de tarea, y no crearás conflictos entre el material antiguo y el nuevo. Asegúrate de hacer clic en "Sync Fork" y "Update branch".



![REVIEW](assets/en/1.webp)



Después de sincronizar con éxito, puede acceder directamente al contenido de interés y confirmar en una nueva rama, como se muestra en este [tutorial](https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6). De lo contrario, puede abrir una nueva rama donde trabajar, haciendo clic en "Ramas", como se muestra a continuación.



![REVIEW](assets/en/2.webp)



Dentro de esta nueva página, encontrarás todas las sucursales que ya has abierto bajo el título "Tus sucursales". Esta sección es muy útil porque te permite encontrar fácilmente dónde has modificado algún contenido. Si quieres abrir una nueva rama, puedes hacer clic en "Nueva rama" en la esquina superior derecha de la página.



![REVIEW](assets/en/3.webp)



A continuación, aparecerá una ventana emergente en la que deberá introducir el nombre de la nueva sucursal. En este caso, he decidido llamarla "BTC101-FR". De este modo, siempre recordaré que esta rama específica debe utilizarse para la corrección del curso BTC101 en francés, y **no la utilizaré para ninguna otra tarea**.


Te sugiero que hagas lo mismo: asegúrate de abrir una nueva rama cada vez que necesites iniciar una nueva tarea.



![REVIEW](assets/en/4.webp)



Después de crear esta nueva rama, asegúrese de hacer clic en ella desde "Sus ramas" en la página anterior y empezar a trabajar en el archivo *.md* relacionado con el contenido específico (en mi caso, haré clic en "cursos" -> "BTC101" -> "fr.md"). Todos los commits relacionados con el archivo específico tendrán que ser confirmados (guardados) dentro de la misma rama.



## ¿Lengua original o traducción?


Al revisar un contenido, es importante **comprobar siempre la versión original en inglés (o francés)** del mismo. Ten en cuenta que traducimos con herramientas de traducción automática, por lo que la traducción al idioma de destino puede no ser fluida o comprensible para el lector final.


Por tanto, siéntase libre de hacer ajustes en el texto y modificar las frases, si es necesario. Nuestro objetivo es aumentar la fluidez, pero siempre respetando el sentido original. En caso de duda sobre cómo tratar una palabra concreta, no dude en preguntar al coordinador de traducción.


Las herramientas LLM pueden traducir literalmente algunas palabras relacionadas con Bitcoin, como Lightning Network. Esto ocurre especialmente cuando se trata de palabras muy técnicas. En casos como estos, es aconsejable mantener la palabra original en inglés en su idioma de destino para mayor claridad, a menos que las normas de su idioma le impongan traducir cada una de las palabras.


En este segundo caso, **investiga siempre para ver si alguien de tu comunidad Bitcoin ya ha traducido esa palabra** y ya se utiliza ampliamente.



- Una solución podría ser **comprobar en [BitcoinWiki](https://en.Bitcoin.it/wiki/Main_Page)** en tu idioma de destino si la palabra ha sido traducida o no. Si no lo está, mantienes la palabra en inglés.



- En cualquier caso, mi consejo sería **insertar la palabra EN a pesar de todo**, añadiendo el significado correspondiente en la lengua de llegada dentro de paréntesis redondos, siguiendo el esquema EN (LANG), o viceversa. Ej. Address (indirizzo), o indirizzo (Address).



- Otra buena solución es mantener la palabra/frase original y **crear un hipervínculo** que redirija al [glosario](https://planb.network/en/resources/glossary) en planb.network. Para ello, debe insertar la palabra/frase entre corchetes y el enlace entre paréntesis, como se muestra en el siguiente ejemplo:


```
[UTXO](https://planb.network/resources/glossary/utxo)
```


En el resultado final (imagen inferior) no se visualizará el enlace completo, y la palabra pasará a ser clicable.



![REVIEW](assets/en/5.webp)



Tenga en cuenta que el enlace al glosario que tomará del sitio web contiene el código de idioma después de la palabra "red" (ejemplo: ``https://planb.network/en/resources/glossary/UTXO``-> aquí puede leer el código de idioma "en"). En este caso, **elimine el código de idioma del enlace**, como ha visto en el cuadro anterior. De este modo, el sistema llevará automáticamente al lector a su idioma designado.


El contenido del repositorio está lleno de hipervínculos como estos de arriba. Ahora que sabes lo que significan, **asegúrate de no borrar ningún enlace** insertado por el autor original.



- Otra cosa relacionada con la traducción de palabras es la siguiente. Si encuentra "Plan ₿ Network" en el texto, **déjelo en esta forma original**. No traduzca la palabra "plan" ni la palabra "red". Además, NO utilice el artículo "The" al presentar Plan ₿ Network: **considérelo como una marca**.



- Lo mismo ocurre con "₿-CERT", "BIZ SCHOOL", "TECH SCHOOL", que también deben conservarse en su forma original.


Un último apunte a este párrafo: como decíamos más arriba, utilizamos herramientas de IA para traducir los contenidos, y luego pedimos la intervención de los colaboradores para asegurarnos de que todo es fluido y está bien corregido.


Si utiliza la IA para corregir la mayor parte del texto, seguro que nos daremos cuenta, ya que estamos familiarizados con las estructuras de frases típicas que genera la IA. Si descubrimos que ha confiado únicamente en la IA para la corrección, sin aplicar cambios significativos, ¡la recompensa final en Sats puede reducirse a la mitad!



## La estructura de las cabeceras


En el lenguaje markdown, todos los encabezados (y títulos de párrafo) comienzan con el signo Hash ``#``. El número de signos Hash corresponde al nivel del encabezamiento. Por ejemplo, un encabezado de nivel tres tiene tres signos numéricos antes del texto (por ejemplo, `#### Mi Encabezado`).


En los cursos, las partes más importantes se introducen con un único signo Hash, mientras que las subpartes pueden tener de dos a cuatro signos Hash. En los tutoriales, normalmente sólo utilizamos cabeceras con dos signos Hash.



![REVIEW](assets/en/6.webp)



Asegúrese de **NUNCA suprimir los signos Hash** antes de un título, de lo contrario creará problemas con la estructura del texto.


Al mismo tiempo, **no cambies** la parte del chapterID que puedes ver en la imagen de arriba, ``<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>`` o las referencias de vídeo como ``:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::``.


Cuando insertamos ``#`` antes de un título, éste se pondrá automáticamente en negrita en la vista previa del curso, así que **evite poner los títulos en negrita durante la corrección**.


Como nota al margen, en la versión EN de los cursos, los **títulos introducidos por uno o dos ``#`` tienen todas las palabras empezando en mayúsculas**, mientras que los títulos que empiezan por tres o cuatro ``#``, no suelen seguir esta regla. Si es posible, asegúrese de que los títulos en su idioma de destino siguen esta estructura.



## La sección inicial de los cursos


Al principio de cualquier contenido, encontrará las siguientes palabras estáticas en minúsculas: "nombre", "descripción", "objetivos". El sitio web las utiliza para descodificar el propio contenido y **siempre se dejan en EN**. En consecuencia, NO las traduzca, ya que de lo contrario el contenido creará problemas de sincronización. Asegúrese de revisar sólo la parte que va después de los dos puntos, que es traducida automáticamente por la IA.



![REVIEW](assets/en/7.webp)



En esta misma sección inicial, mantén el formato tal cual. No añada nada al principio del texto. Por ejemplo, evite añadir "tt" antes de los guiones, como en la imagen siguiente



![REVIEW](assets/en/8.webp)



## Recomendaciones de formato


A continuación encontrará algunos ejemplos de cuestiones de formato a las que debe prestar atención al corregir contenidos en su lengua de destino.



- Preste atención a los signos de puntuación extraños como `\*\*`, o ``**`` que pueden representar una mala representación del símbolo de negrita. En la imagen de abajo, puedes ver que los asteriscos están sólo a la derecha de la palabra, lo que resulta extraño.



![REVIEW](assets/en/9.webp)



Así pues, compruebe siempre el texto original en inglés para ver si debe haber un texto en negrita. En este caso, basta con añadir dos asteriscos al principio de la palabra, para que se muestre correctamente en el sitio web. De hecho, en el lenguaje markdown, **para que aparezca la negrita, hay que insertar dos asteriscos ``**`` tanto antes como después de la palabra/sentencia** (véase el ejemplo siguiente).



![REVIEW](assets/en/10.webp)




- Lo mismo puede ocurrir con símbolos como $ y `` ``.

Asegúrese de comprobar el archivo del idioma original (a menudo EN o FR) para ver dónde se supone que deben estar estos símbolos. Siempre puede pedir ayuda al coordinador sobre este asunto.



- Si encuentra comillas, asegúrese de investigar en Internet para encontrar la traducción correcta en su idioma. Las comillas suelen insertarse después del símbolo ``>``.



![REVIEW](assets/en/11.webp)



## Corrección de cuestionarios


¿Sabías que también puedes corregir las preguntas de los cuestionarios de cada curso? Por ejemplo, si quieres corregir los cuestionarios de BTC101 en TI, puedes abrir una rama específica y seguir este camino: "cursos" -> "BTC101" -> "cuestionario". Allí encontrará todas las carpetas dedicadas a cada pregunta, junto con el archivo de idioma correspondiente en formato _yml_.


Una vez más, asegúrese de que se encuentra en una sucursal que abra específicamente para este fin, e informe siempre al coordinador.


Después de revisar la pregunta, asegúrese de cambiar el estado "revisado" de "falso" a "verdadero", como se muestra en la imagen siguiente.



![REVIEW](assets/en/12.webp)


## Corrección de glosarios


Al igual que los cuestionarios, también puedes corregir el glosario. El glosario original estaba escrito en francés, por lo que encontrarás frases como: "En francés, esta expresión puede traducirse por..."


En casos como éste, adapte esta frase a su lengua de destino, o al inglés.


## Otras buenas prácticas



- Si necesitas buscar palabras concretas dentro del texto, puedes pulsar ``CTRL+F`` y aparecerá la sección buscar-reemplazar. Esta parte es muy útil cuando necesitas saltar a una parte específica del texto, o necesitas reemplazar palabras/sentencias específicas en lote, sin desplazarte por todo el contenido.



![REVIEW](assets/en/13.webp)



Al utilizar la función "reemplazar todo", es importante comprobar dos veces los resultados para asegurarse de que no se han alterado también los enlaces. Por ejemplo, si desea cambiar la palabra "Bitcoin" por "Bitkoin" (lo que puede ser necesario en algunos idiomas), la función "reemplazar todo" puede actualizar eficazmente todas las instancias del texto. Sin embargo, tenga en cuenta que esta herramienta también modificará todos los enlaces que contengan esa palabra, lo que puede provocar problemas de redireccionamiento.


En el ejemplo siguiente, el corrector utilizó la función anterior para sustituir "Satoshi" por "Satoshi(Sats)", y también cambió el enlace a un tutorial que contenía la propia palabra. Como consecuencia, el enlace dejó de ser válido.


Compruebe siempre todos los hipervínculos del texto para asegurarse de que son correctos.



![REVIEW](assets/en/14.webp)




- Siguiendo con el tema, si el autor inserta un enlace que haga referencia a un curso o tutorial de Plan ₿ Network (**no** entre paréntesis), el sitio web creará automáticamente una "tarjeta" mostrando la miniatura relacionada. En consecuencia, asegúrese siempre de que **hay un espacio entre el texto y el propio enlace**, de lo contrario podría aparecer el siguiente error en el sitio web.



![REVIEW](assets/en/15.webp)





- Por último, otra buena práctica que puede aplicar cuando termine su tarea de corrección y envíe el RP es volver a la incidencia original abierta por el coordinador y comentar con "Corrección realizada". **Asegúrate de insertar también allí el enlace a tu RP**.



## Conclusión


En resumen, conocer los errores más comunes de los correctores puede ayudarte a mejorar tus habilidades a la hora de revisar contenidos. Es fácil pasar por alto aspectos como el contexto o la coherencia, y detectar estos errores puede marcar una gran diferencia.


Ten siempre en cuenta que un principiante puede leer estos cursos y tutoriales, por lo que es nuestra responsabilidad asegurarnos de que los entiende perfectamente. Como corrector, ¡eres un educador!


Gracias por leer este tutorial y ¡buen viaje!