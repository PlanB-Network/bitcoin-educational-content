# Introduction

A course is a structured educational content designed to extensively teach a specific subject matter. In this documentation, we outline the required formatting that all courses must respect -- adhering to these formatting guidelines ensures consistency and clarity across all courses as well as it allows a smoother and more efficient translation and proofreading process.

The name of folder for any course represents its unique identifier known as the course ID. It is essential that the course ID follows specific rules which are detailed in this [documentation page](./course-id-rules.md).

This folder has a specific structure that is extensively detailed in the next section.

You can find complete specifications about courses in the [PBN Template Repo](/PBN-template-repo/courses/) folder with full examples of folder and files structure and extensive comments inside all files to understand how to properly format your course.

# Course Folder Structure

Any course folder should be placed in the `courses/` folder and respect the following structure:

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
	  ├── en.md                   - English version of the btc101 course content
	  ├── es.md                   - Spanish version of the btc101 course content
	  └── ..                      - Indicates language-specific course files
```

As an example, we use here a course named BTC101. The folder "btc101", named after the course, contains:

- a [yaml file](#yaml-course-file) which describes the course
- several language specific [markdown files](#markdown-course-files) that contain the written courses
- an [assets folder](#assets-course-folder) that contains all the images used in the course
- a quizz folder (optional) containing quiz to make a knowledge self-assessment during the course
- an exam folder (not implemented yet)
- an exercise folder (not implemented yet)
- a teachable folder (not implemented yet)

**NB.** If you are writing a paid course, you will have to additionally read this [section](#Paid-course) to add some needed metadata specific to this type of content.

## Yaml course file

We'll used the file present in the btc101 folder as an example:

```yaml
level: beginner
hours: 20

professors:
  - rabbit-hole

contributors:
  - another-satoshi
```

This yaml file must contains all the relevant metadata of the course which are defined in [the course yml template](/docs/PBN-template-repo/courses/topic101/course.yml).

## Markdown course files

Markdown files contain the written course and must be placed in the course folder. Additionally, since it is language-specific, the language code used to name it will reflect the language used in the file. These files MUST respect precise formatting rules to be properly rendered on our website. You can find full examples in [the course md template](/docs/PBN-template-repo/courses/topic101/en.md).

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

The markdown course file is divided in 3 parts. The first two parts would be used to build the presentation page of the course (see this [example](https://planb.network/es/courses/btc101)):

1. The **Course Header** which contains language-specific metadata and is delimited by `---` and must contain the following properties:
   - `name`: define the name of the course
   - `goal`: define the main goal of the course
   - `objectives`: define a list of skills that would be developped
   - NOTE: the yaml properties MUST NOT be translated and MUST remain in English
2. The **Course Description** which is composed of a title defined by the heading (`#`) and a short paragraph to present the course.
3. The **Course Content** which is the proper written course using the [markdown syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
   - The first-level heading will be interpreted as a part of the lecture, the second-level as a chapter and the third-level as a sub-chapter.
   - Note that this structure is used to create the outline of the course and that each chapter is rendered on a single page, so try to evaluate a user-friendly (not too short and not too long) length for your chapter.
   - On the other hand, parts (resp. subchapters) are used as way to better group similar chapters (resp. split paragraphs on slightly different matter) and could be used to better reflect the intentions of the course
   - For further detail on the formatting, please look at the next paragraph [Course formatting rules](#course-formatting-rules).

### Course formatting rules

These are the rules for properly formatting course content:

- 1 course is composed of at least 2 parts and 2 chapters per part
  - parts are identified by first level heading `#`
  - chapters are identified by second level heading`##`
  - sub-part, identified by third level heading `###` are optional but they will be displayed on the syllabus course
  - sub-sub-part, identified by forth level heading `####` are optional but _not_ displayed on the syllabus course
- each chapter has a unique ID (see [chapter ID section](#Chapter ID))
- a course contains a header part, delimited by `---`
- a course contains an introduction part, delimited by `+++`
- if a chapter is provided or written by another teacher, you can mention it via the html tag `<professor>contributor-id</professor>`. Note that the professor must be present in the [professor folder](../professors/)

#### Chapter ID

The **Chapter ID** is a unique identifier for each chapter. This ID is a simply three words from the BIP39 wordlist. You can either generate these ids by yourself by following this [tutorial](./how-to-generate-a-bip39-id.md) or ask to one the PlanB reviewers to do it for you. This ID will allow you to link your chapter with questions present in the [quizz folder](#quizz-folder) of your course, but also let you re-order your chapters after the first publication without breaking our database for PlanB Network website.

## Assets course folder

The `/assets` subfolder contains all the images used in the course. In order to facilitate the maintenance and the potential translation of the images you will use 2 types of folders:

1. a folder for images without any text, called `no-txt/`
2. a folder per language for images with overlay. This folder will be named by the language code assigned to the corresponding language (eg. `en` or `es` for English or Spanish respectively)
   - Although you are free to structure language-specific folders, the structure MUST remain the same between two different language. This rule makes it easier to automatically update the image path in the corresponding markdown file.
   - If you create a course, you can simply create image with text in English and later on start the [image translation process](how-to-translate-image.md)

Additionally in the `assets/` folder a `thumbnail.webp` file is required, it will be used as the course's thumbnail, like the one used for the [btc101 course](https://planb.network/courses/2b7dc507-81e3-4b70-88e6-41ed44239966).

## Optional folders within course folder

### Quizz folder

TBD

# Paid Course

TBD
