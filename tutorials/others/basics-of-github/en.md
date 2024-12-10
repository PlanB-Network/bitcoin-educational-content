---
name: The Basics of GitHub
description: Understanding the basics of Git and GitHub
---

![cover](assets/cover.webp)

PlanB's mission is to provide top-tier educational resources on Bitcoin, available in as many languages as possible. All content published on the site is open-source and hosted on GitHub, offering anyone the opportunity to contribute to the enrichment of the platform. Contributions can take various forms: correcting and proofreading existing texts, translating into other languages, updating information, or creating new tutorials not yet available on our site.

If you wish to contribute to the PlanB Network, you will need to use Git and GitHub. If these tools are unfamiliar to you or if their operation seems obscure, don't panic, this article is for you! We will review together the fundamentals of Git and GitHub, as well as the associated technical jargon, to enable you to effectively use these tools afterward.

## What is Git?

Git is a version control system, specifically designed to manage software projects. Created in 2005 by Linus Torvalds, Git has quickly become the standard in the software development industry for version control. But what does that exactly mean?
![git](assets/1.webp)
At its core, Git allows developers to track changes made to a project's source code over time. This means that with every change in the code, Git records a new version of the project. If an error occurs or if an experimental feature does not work as expected, it is possible to revert to a previous state of the code, like a kind of time machine for files.

One of the key features of Git is branch management. A branch is a kind of parallel line where developers can work independently from the rest of the project. This greatly facilitates the addition of new features or the correction of bugs without disturbing the main code. Once the modifications are tested and validated, they can be merged with the main branch.

One of the peculiarities of Git is its ability to operate in a distributed manner. Each developer has a complete copy of the project on their own computer's hard drive, allowing them to work offline and merge changes later when an Internet connection is available. This reduces the risk of conflicts and allows multiple developers to work simultaneously on the same project without stepping on each other's toes.
Initially, Git was primarily designed for software development projects. However, it can also be used to manage content writing projects. Instead of collaborating on code, we collaborate on text. And it is precisely this method that PlanB Network has adopted to manage its content! Git facilitates collaboration on writing courses and tutorials, as it allows for precise tracking of changes, efficient version management, and also enables the review and improvement of content by other contributors.
## What is GitHub?

GitHub is a source code management and hosting platform based on the Git version control system we just discussed. Launched in 2008, GitHub quickly gained popularity and has become an essential reference for developers worldwide. But how does GitHub differ from Git, and why is it so crucial in our content production method?
![github](assets/2.webp)
First, it's important to understand that GitHub is built on Git (which we discussed in the previous section). While Git is the tool that tracks code changes, GitHub is the online service that hosts, shares, and manages this code.

Imagine Git as a kind of logbook that each developer uses on their own computer to record all the changes in their project. GitHub, on the other hand, is like a public library where all these logbooks can be shared, compared, and combined.

The fundamental difference between Git and GitHub lies in their function: Git is the tool used locally by each developer to manage their code versions, while GitHub is the online platform that hosts these versions and facilitates collaboration.

GitHub is much more than just a code hosting service. It's a collaboration platform that allows developers to work together efficiently. And indeed, PlanB Network uses this platform to host not only all the code that powers the website but also, and this is what interests us, all the content (tutorials, training, resources...).

## Some Technical Terms

On Git and GitHub, you will encounter commands and features whose names may seem complex. In this last part, I provide simple definitions to understand the technical terms you might come across when using Git and GitHub:

- **Fetch origin:** Command that retrieves recent information and changes from a remote repository without merging them with your local work. It updates your local repository with new branches and commits present in the remote repository.

- **Pull origin:** Command that retrieves updates from a remote repository and immediately integrates them into your local branch to synchronize it. This combines the steps of fetch and merge into a single command.
- **Sync Fork:** A feature on GitHub that allows you to update your fork of a project with the latest changes from the source repository. This ensures that your copy of the project stays up-to-date with the main development.
- **Push origin:** Command used to send your local changes to a remote repository.

- **Pull Request:** A request sent by a contributor to indicate that they have pushed changes to a branch in a remote repository and wish for these changes to be reviewed and potentially merged into the main branch of the repository.

- **Commit:** Saving your changes. A commit is like an instant snapshot of your work at a given moment, which allows keeping a history of changes. Each commit includes a descriptive message explaining what has been modified.

- **Branch:** A parallel version of the repository, allowing you to work on changes without affecting the main branch (often called "main" or "master"). Branches facilitate the development of new features and the correction of bugs without the risk of disrupting stable code.

- **Merge:** Merging consists of integrating the changes from one branch into another. It is used, for example, to add the changes from a working branch onto the main branch, which allows adding the various contributions.

- **Fork:** Forking a repository means creating a copy of that repository on your own GitHub account, which allows you to work on the project without affecting the original repository. The fork can either go its own way and become a different project from the original, or it can regularly synchronize with the original project to contribute to it.

- **Clone:** Cloning a repository means making a local copy on your computer, which gives you access to all the files and the history. This allows you to work on the project directly locally.

- **Repository:** Storage space for a project on GitHub. A repository contains all the project files as well as the history of all the changes that have been made to it. It is the basis of storage and collaboration on GitHub.

- **Issue:** A tool for tracking tasks and bugs on GitHub. Issues allow for reporting problems, proposing improvements, or discussing new features. Each issue can be assigned, labeled, and commented on.

This list is obviously not exhaustive. There are many other technical terms specific to Git and GitHub. However, those mentioned here are the main ones you will frequently encounter.

After reading this article, it is possible that some aspects of Git and GitHub are still unclear to you. I encourage you to start using these tools yourself. Practice is often the best way to understand how the machine works! And to get started, you can discover these 2 other tutorials:
**[Create your GitHub account](https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c)**
**[Setting Up Your Local Environment to Contribute to PlanB Network](https://planb.network/tutorials/others/contribution/github-desktop-work-environment-5862003b-9d76-47f5-a9e0-5ec74256a8ba)**