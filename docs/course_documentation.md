# Introduction 

- a course is defined as an education content which purpose is to teach extensivily a specific subject and that **must** respect the following formatting
- the root folder defined the *course ID* which must respect some rules (cf. [course ID rules](./course_ID_rules.md))


# Course Folder Structure

Any course folder should be placed in the `courses/` folder and respect the following strucure:

```

btc101/                                                                                                                                   
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
- a [yaml file](#Yaml course file) which describes the course 
- several language specific [markdown files](#Markdown course files) that contains the written courses
- an [assets folder](#Assets course folder) that contains all the images used in the course

## Yaml course file

needs to be written

## Markdown course files

needs to be written

## Assets course folder

Within the "assets" subfolder,  there are language-specific subfolders ("en" for English and "es" for Spanish) that hold different versions of image 1 and 2 in each language. Note that although the author can freely strucutre the subfolder `assets/`, it is more convenient to structure language-specific folders identically, as it makes it easier to change image path in the corresponding language-specific markdown file. Additionnaly the `assets/` folder must be is a `thumbnail.webp` file that will be used as the course's thumbnail, like the one used for the [btc101 course](https://planb.network/en/courses/btc101).  

Then several files would be present in the course folder, 

Then the files that contains the written course must be placed in the course folder and because it is a language-specific, the language code used will reflect the language used in the file. These files must also respect some precise formatting to be properly rendered on our website (cf. [course formatting section](#Course formatting))

You can either read our [tutorial](planb.network) on our website or our [documentation page](./content-translation-process.md), if you want to learn more about the translation process. 


