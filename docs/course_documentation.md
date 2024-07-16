# Introduction 

A course is a structured educational content designed to extensively teach a specific subject matter. In this documentation, we outline the required formatting that all courses must respect -- adhering to these formatting guidelines ensures consistency and clarity across all courses.

The name of folder for any course represents its unique identifier known as the course ID. It is essential that the course ID follows specific rules which are detailed in this [documentation page](./course-id-rules.md). 

This folder has a specific structure that is extensively detailed in the next section. 
# Course Folder Structure

Any course folder should be placed in the `courses/` folder and respect the following strucure:

```
courses/
  └── btc101/
	  ├── assets/
	  │   ├── en/
	  │   │   ├── image1.webp     - English version of image1
	  │   │   └── image2.webp     - English version of image2
	  │   ├── es/
	  │   │   ├── image1.webp     - Spanish version of image1
	  │   │   └── image2.webp     - Spanish version of image2
	  │   ├── thumbnail.webp      - BTC101's thumbnail
	  │   └── ..                  - Indicates additional language-specific folders
	  ├── course.yaml             - English version of the main documentation file
	  ├── en.md                   - English version of the main documentation file
	  ├── es.md                   - Spanish version of the btc101 course
	  └── ..                      - Indicates language-specific course files
```

Here we used the course BTC101 as an example. This folder "btc101" contains : 
- a [yaml file](#yaml-course-file) which describes the course 
- several language specific [markdown files](#markdown-course-files) that contains the written courses
- an [assets folder](#assets-course-folder) that contains all the images used in the course
- a question folder (not implemented yet)
- an exam folder (not implemented yet)
- an exercice folder (not implemented yet)
- a teachable folder (not implemented yet)

**NB.** If you are writting a paid course, you will have to additionnaly read this [section](#Paid-course) to add specific metadata specific to this type of content. 

## Yaml course file

Here again we'll used the file present in the btc101 folder as an example: 

```yaml
level: beginner
hours: 20

professors:
  - rabbit-hole

contributors:
  - another-satoshi
```

This [yaml file](./format_guidelines.md#yaml-format-guidelines) must contains all the relevant metadata of the course which are defined via the used of the following properties:
- `level`: you can set the difficulty to the following values `beginner`, `intermediate`, `advanced`, `developer`
- `hours`: an evaluation of the number of hours that would be needed to complete the course
- `professors`: a list of all professors that have participated in this course, by using the associated [PlanB-UID](./planb-uid.md) (see [professor documentation page](./professor_documentation.md))
- `contributors`: a list of all contributors that have participated in the maintenance of the course folder, by using the associated [PlanB-UID](./planb-uid.md)

## Markdown course files

Markdown files contain the written course and must be placed in the course folder. Additionnaly,  because it is a language-specific, the language code used will reflect the language used in the file. These files MUST respect precise formatting rules to be properly rendered on our website (cf. [course formatting section](#Course formatting rules)). You can either read our [tutorial](008%20DB%20x%20PBN/PlanB%20Network.md) on our website or our [documentation page](./content-translation-process.md), if you want to learn more about the translation process. 

Let's start describing a markdown course file. 
Here again we'll used the beginning of btc101's `es.md` file as an example: 

```md
---
name: El recorrido de Bitcoin
goal: Descubrir Bitcoin y sus fundamentos con su propuesta de valor monetario, los mineros, las transacciones y las carteras.
objectives:
  - Tener una comprensión general de la tecnología Bitcoin
  - Comprender cómo comprar y asegurar sus bitcoins
  - Tener una comprensión general de la tecnología Blockchain
  - Estar familiarizado con el concepto de la Red Lightning
  - Comprender el impacto geopolítico y social que representa Bitcoin
---

# Tu primera aventura en Bitcoin

En este curso, te explicaré Bitcoin en 21 capítulos para que puedas entender esta tecnología de manera simple y efectiva. El curso es accesible para todos y explora la industria en su conjunto: mineros, carteras, plataformas de compra/venta, etc. […]

+++

# Introducción

## Un salto hacia lo desconocido
<chapterId>father-loop-frog</chapterId>

### Bienvenido a un nuevo paradigma monetario y tecnológico.

Bitcoin es una innovación significativa que va más allá de ser simplemente una "moneda de internet". Es una revolución tanto tecnológica como monetaria, capaz de cuestionar nuestra relación con el dinero y la sociedad. Bitcoin es una moneda "neutral" y "descentralizada", lo que significa que no está bajo el control de ninguna entidad o institución. Es una innovación significativa que va más allá de ser simplemente una divisa. Para comprender bien este famoso bitcoin, es importante entender que bitcoin (llamado BTC) es tanto un protocolo informático (Bitcoin) como una unidad monetaria (bitcoin). […]

### Un currículo completo pero accesible

En el marco de este curso, discutiremos los aspectos monetarios de Bitcoin, incluyendo cómo comprar y vender bitcoins, cómo mantenerlos seguros en carteras digitales y cómo utilizarlos para realizar transacciones. También examinaremos el papel de los mineros, que son esenciales para la creación de nuevos bitcoins y la seguridad de la red Bitcoin. Además, nos centraremos en el futuro de Bitcoin y cómo la tecnología de la Red Lightning puede mejorar las transacciones de Bitcoin.

![image](assets/es/chapter0/4.webp) 

[…]

```

The markdown course file is divided in 3 parts. The first two parts would be used to build the presentation page of the course (see this [example](https://planb.network/es/courses/btc101))
1. The **Course Header** which contains language-specific metadata and is delimited by `---` and must contains the following properties:
	- `name`: define the name of the course 
	- `goal`: define the main goal of the course
	- `objectives`:  define a list of skills that would be developped 
	- NB. the yaml properties MUST NOT be translated and MUST remained in English 
2. The **Course Description** which is composed of a title defined by the heading (`#`) and a short paragraph to present the course. 
3. The **Course Content** which is the proper written course using the [markdown syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax). 
	- The first-level heading will be interpreted as a part of the lecture, a second-level as a chapter and third-level as a sub-chapter. 
	- Note that this structure is used to create the outline of the course and that each chapter is rendered on a single page, so try to evaluate a user-friendly (not too short and not too long) length for your chapter. 
	- On the other hand parts  (resp. subchapters) are used as way to better group similar chapters (resp. split paragraphes on slightly different matter) and could be used to better reflect the intentions of the course 
### Course formatting rules

rules for course format:
- 1 course is composed of at least 2 parts and 2 chapters per part
	- parts are identified by `#`
	- chapters are identified by `##`
	- subpart, identied by `###` are optional but they will be displayed on the syllabus course
	- subsubpart, identified by `####` are optional but *not* displayed on the syllabus course
- each chapter is composed a unique ID (see [chapter ID section](#Chapter ID))
- a course contains a header part, delimited by `---`
- a course contains an introduction part, delimited by `+++`
- if a chapter is provided or written by another teacher, you can mention it via the htlm tag `<professor>contributor-id</professor>`. Note that the professor must be present in the [professor folder](./professor-documentation.md)

#### Chapter ID

The **Chapter ID** is a unique identifier for each chapter. This ID is a simply three words from the BIP39 wordlist. You can either generate these ids by yourself by following this [tutorial](./how-to-generate-a-bip39-id.md) or ask to one the PlanB reviewers to do it for you. This ID will allow you to link your chapter with questions present in the [question folder](#question-folder) of your course, but also let you re-order your chapters after the first publication without breaking our database for PlanB Network website. 

## Assets course folder

The `/assets` subfolder contains all the images used in the course.  In order to facilitate the maintaining and the potential translation of the images you will used 2 types of folders: 
1. a folder for images without any text, called `no-txt/` 
2. a folder per language for images with text written on it. Theses folder will be named by the language code assigned to the corresponding language (eg. `en` or `es` for english or spanish respectively)
	- Altough you are free to structure language-specfic folders, the structure MUST remain the same between two different language. This rule makes it manageable to automatically update the image path in the corresponding markdown file. 
	- If you create a course, you can simply create image with text in english, then in a second time we can start the [image translation process](how-to-translate-image.md)

Additionnaly the `assets/` folder must be is a `thumbnail.webp` file that will be used as the course's thumbnail, like the one used for the [btc101 course](https://planb.network/en/courses/btc101).  


## Optional folders within course folder

### Question folder 

### Exam folder 

### Exercice folder 
### Teachable folder

# Paid Course