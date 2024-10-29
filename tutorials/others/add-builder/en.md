---
name: Adding a Builder
description: How to propose the addition of a new builder on PlanB Network?
---
![builder](assets/cover.webp)

PlanB's mission is to provide top-tier educational resources on Bitcoin, in as many languages as possible. All content published on the site is open-source and hosted on GitHub, which allows anyone to participate in enriching the platform.

Do you want to add a new Bitcoin "builder" to the PlanB Network site and give visibility to your company or software, but don't know how? This tutorial is for you!
![builder](assets/01.webp)
- First, you need to have a GitHub account. If you don't know how to create an account, we have made a detailed tutorial to guide you.

https://planb.network/tutorials/others/create-github-account


- Go to [the GitHub repository of PlanB dedicated to data](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/builders) in the `resources/builder/` section:
![builder](assets/02.webp)
- Click on the top right on the `Add file` button, then on `Create new file`:
![builder](assets/03.webp)
- If you have never contributed to the contents of PlanB Network before, you will need to create your fork of the original repository. Forking a repository means creating a copy of that repository on your own GitHub account, which allows you to work on the project without affecting the original repository. Click on the `Fork this repository` button:
![builder](assets/04.webp)
- You will then arrive at the GitHub editing page:
![builder](assets/05.webp)
- Create a folder for your company. To do this, in the `Name your file...` box, write the name of your company in lowercase with dashes instead of spaces. For example, if your company is called "Bitcoin Baguette", you should write `bitcoin-baguette`:
![builder](assets/06.webp)
- To validate the creation of the folder, simply add a slash after your name in the same box, for example: `bitcoin-baguette/`. Adding a slash automatically creates a folder rather than a file:
![builder](assets/07.webp)
- In this folder, you will create a first YAML file named `builder.yml`:
![builder](assets/08.webp)
- Fill this file with information about your company using this template:

```yaml
name:

address_line_1:
address_line_2:
address_line_3: 

language:
  - 

links:
  website:
  twitter:
  Github:
  youtube:
  nostr:

tags:
  - 
  - 

category:
```

Here's what to fill in for each key:
- `name`: The name of your company (mandatory);
- `address` : The location of your business (optional);
- `language` : The countries your business operates in or the languages supported (optional);
- `links` : The various official links of your business (optional);
- `tags` : 2 terms that qualify your business (mandatory);
- `category` : The category that best describes the field in which your business operates among the following choices:
	- `wallet`,
	- `infrastructure`,
	- `exchange`,
	- `education`,
	- `service`,
	- `communities`,
	- `conference`,
	- `privacy`,
	- `investment`,
	- `node`,
	- `mining`,
	- `news`,
	- `manufacturer`.

For example, your YAML file could look like this:

```yaml
name: Bitcoin Baguette

address_line_1: Paris, France
address_line_2:
address_line_3: 

language:
  - fr
  - en

links:
  website: https://bitcoin-baguette.com
  twitter: https://twitter.com/bitcoinbaguette
  Github:
  youtube:
  nostr:

tags:
  - bitcoin
  - education

category: education
```

![builder](assets/09.webp)
- Once you have finished making changes to this file, save them by clicking on the `Commit changes...` button:
![builder](assets/10.webp)
- Add a title for your changes, along with a short description:
![builder](assets/11.webp)
- Click on the green `Propose changes` button:
![builder](assets/12.webp)
- You will then arrive at a page summarizing all your changes:
![builder](assets/13.webp)
- Click on your GitHub profile picture at the top right, then on `Your Repositories`:
![builder](assets/14.webp)
- Select your fork of the PlanB Network repository:
![builder](assets/15.webp)
- You should see a notification at the top of the window with your new branch. It's probably called `patch-1`. Click on it:
![builder](assets/16.webp)
- You are now on your working branch (**make sure you are on the same branch as your previous modifications, this is important!**):
![builder](assets/17.webp)
- Go back to the `resources/builders/` folder and select the folder of your business that you just created in the previous commit:
![builder](assets/18.webp)
- In the folder of your business, click on the `Add file` button, then on `Create new file`:
![builder](assets/19.webp)
- Name this new folder `assets` and confirm its creation by putting a slash `/` at the end:
![builder](assets/20.webp)
- In this `assets` folder, create a file named `.gitkeep`:
![builder](assets/21.webp)
- Click on the `Commit changes...` button:
![builder](assets/22.webp)
- Leave the commit title as default, and make sure the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`: ![builder](assets/23.webp)
- Go back to the `assets` folder:
![builder](assets/24.webp)
- Click on the `Add file` button, then on `Upload files`:
![builder](assets/25.webp)
- A new page will open. Drag and drop an image of your company or your software into the area. This image will be displayed on the PlanB Network site:
![builder](assets/26.webp)
- It can be the logo or an icon:
![builder](assets/27.webp)
- Once the image is uploaded, verify that the `Commit directly to the patch-1 branch` box is checked, then click on `Commit changes`:
![builder](assets/28.webp)
- Be careful, your image must be square, must be named `logo`, and must be in `.webp` format. The full file name should therefore be: `logo.webp`:
![builder](assets/29.webp)
- Go back to your `assets` folder and click on the `.gitkeep` intermediate file:
![builder](assets/30.webp)
- Once on the file, click on the three small dots at the top right then on `Delete file`:
![builder](assets/31.webp)
- Verify that you are still on the same working branch, then click on the `Commit changes` button:
![builder](assets/32.webp)
- Add a title and a description to your commit, then click on `Commit changes`:
![builder](assets/33.webp)
- Go back to your company's folder:
![builder](assets/34.webp)
- Click on the `Add file` button, then on `Create new file`:
![builder](assets/35.webp)
- Create a new YAML file by naming it with the indicator of your native language. This file will be used for the description of the builder. For example, if I want to write my description in English, I will name this file `en.yml`:
![builder](assets/36.webp)
- Fill out this YAML file using this template:
```yaml
description: |
 
contributors:
 - 
```

- For the `contributors` key, you can add your contributor identifier to PlanB Network if you have one. If you don't, leave this field empty.
- For the `description` key, you simply need to add a short paragraph that describes your company or your software. The description must be in the same language as the file name. You do not need to translate this description into all the languages supported on the site, as the PlanB teams will do so using their model. For example, here is what your file could look like:
```yaml
description: |
Founded in 2017, Bitcoin Baguette is a Paris-based association dedicated to organizing Bitcoin meetups and technical workshops. We bring together enthusiasts, experts, and curious minds to explore and discuss the intricacies of Bitcoin technology. Our events provide a platform for knowledge sharing, networking, and fostering a deeper understanding of Bitcoin's inner workings. Join us at Bitcoin Baguette to be a part of Paris's Bitcoin community and stay updated with the latest advancements in the field.

contributors:
- 
```
![builder](assets/37.webp)
- Click on the `Commit changes` button:
![builder](assets/38.webp)
- Ensure the `Commit directly to the patch-1 branch` box is checked, add a title, then click on `Commit changes`:
![builder](assets/39.webp)
- Your company folder should now look like this:
![builder](assets/40.webp)
- If everything is to your satisfaction, return to the root of your fork:
![builder](assets/41.webp)
- You should see a message indicating that your branch has undergone changes. Click on the `Compare & pull request` button:
![builder](assets/42.webp)
- Add a clear title and description to your PR:
![builder](assets/43.webp)
- Click on the `Create pull request` button:
![builder](assets/44.webp)
Congratulations! Your PR has been successfully created. An administrator will now review it and, if everything is in order, integrate it into the main repository of PlanB Network. You should see your builder profile appear on the website a few days later.

Be sure to follow the progress of your PR. An administrator may leave a comment asking for additional information. As long as your PR is not validated, you can consult it in the `Pull requests` tab on the PlanB Network GitHub repository:
![builder](assets/45.webp)
Thank you very much for your valuable contribution! :)
