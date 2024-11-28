## Workflow

### 1. Configure your local environment

- You must have your own fork of the [Plan B Network repository on GitHub](https://github.com/PlanB-Network/bitcoin-educational-content).
- Sync the main branch (`dev`) of your fork with the source repository.
- Update your local clone.

### 2. Create a new branch

- Ensure you are on the `dev` branch.
- Create a new branch with a descriptive name (e.g., `tuto-green-wallet-loic`).
- Publish this branch on your online fork.

### 3. Add the tutorial documents

- Locate the appropriate folder in the local repository (e.g., `tutorials/wallet`).
- Create a dedicated directory for the tutorial with a clear name (e.g., `sparrow-wallet`). Note that this folder name will also determine the URL path for your tutorial. It must be lowercase, without special characters (except dashes), and without spaces.
- Add the following elements to this directory:
    - A subfolder named `assets` containing:
        - Two `.webp` images:
            - `logo.webp`: The tutorial logo (square format with a background). This logo should represent the software or tool presented. If the tutorial is not specific to a single tool (e.g., a general tutorial on generating a mnemonic phrase), you are free to choose a visual to act as the logo (e.g., a generic icon).
            - `cover.webp`: A cover image displayed at the beginning of the tutorial.
        - A subfolder named with the tutorial's original language code. For example, if the tutorial is written in English, this subfolder should be named `en`. Place all tutorial visuals (diagrams, images, screenshots, etc.) here.
    - A `tutorial.yml` file containing metadata (professor, tags, category, difficulty level, etc.).
    - A Markdown file for the tutorial content, named according to the language code (e.g., `fr.md`, `en.md`, etc.).

### 4. Complete the YAML file

- Complete the `tutorial.yml` file using the following template:

```yaml
id: 

builder: 

tags:
  - 
  - 
  - 

category: 

level: 

credits:
  professor: 

# Proofreading metadata

original_language:
proofreading:
  - language: 
    last_contribution_date:
    urgency:
    contributors_id:
      - 
    reward:
```

- Required fields:
    - **id**: A UUID (_Universally Unique Identifier_) for uniquely identifying the tutorial.
    - **builder**: The name of the company or organization behind the tool presented in the tutorial [from the builders list](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/builders).
    - **tags**: 2 or 3 relevant keywords related to the tutorial content, chosen [from Paolo's tag list](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/docs/50-planb-tags.md).
    - **category**: The subcategory corresponding to the tutorial's content, based on the Plan B site structure (e.g., for wallets: `desktop`, `hardware`, `mobile`, `backup`).
    - **level**: The tutorial difficulty level, selected from the following:
        - `beginner`
        - `intermediate`
        - `advanced`
        - `expert`
    - **professor**: Your `contributor_id` (BIP39 words) as displayed on [your professor profile](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/professors).
    - **original_language**: The original language of the tutorial (e.g., `fr`, `en`, etc.).
    - **proofreading**: Information about the proofreading process. Complete the initial part, as proofreading your own tutorial counts as the first review.
        - **language**: Proofreading language code (e.g., `fr`, `en`, etc.).
        - **last_contribution_date**: Today's date.
        - **urgency**: Leave blank.
        - **contributors_id**: Your GitHub ID.
        - **reward**: Leave blank.
- Example of a completed `tutorial.yml` file for a tutorial on the Blockstream Green wallet:

```yaml
id: e84edaa9-fb65-48c1-a357-8a5f27996143

builder: Blockstream

tags:
  - wallets
  - software
  - keys

category: mobile

level: beginner

credits:
  professor: pretty-private

# Proofreading metadata

original_language: fr
proofreading:
  - language: fr
    last_contribution_date: 2024-11-20
    urgency:
    contributors_id:
      - LoicPandul
    reward:
```

### 5. Write the content

- Complete the Markdown file properties with:
    - The title (`name`).
    - A short description (`description`).
- Add the cover image at the top of the tutorial using Markdown syntax (replace "green" with the presented tool name):

```markdown
![cover-green](assets/cover.webp)
```

- Write the tutorial content in Markdown:
    - Use well-structured headings (`##`), lists, and paragraphs.
    - Insert visuals using Markdown syntax:

```markdown
![image-name](assets/en/001.webp)
```

- Place diagrams and images in the language subfolder within `assets`.

### 6. Save and submit the tutorial

- Save your changes locally, creating a commit with a descriptive message.
- Push the changes to your GitHub fork.
- Once complete, create a Pull Request (PR) on GitHub to propose integrating your changes.
- Add a title and brief description for the PR. Mention the corresponding issue number in your PR comment.

### 7. Review and merge

- Wait for validation or feedback from an admin.
- If needed, make additional changes and push new commits.
- Once the PR is merged, you can delete your working branch.

For more detailed information on the process of proposing a new tutorial, you can also refer to this detailed guide, and more broadly, to all the tutorials in the "contribution" section: https://planb.network/tutorials/others/write-tutorials

## Content creation standards

- **Supported formatting on the platform**:
    - Classic Markdown: lists, links, images, quotes, bold, italics, etc.
    - LaTeX (block only, not inline): Delimited by `$$`.
    - Inline code: Single backtick syntax.
    - Code blocks: Triple backtick syntax (\`\`\`), e.g.:

```python
  print("Hello, Bitcoin!")
```

- **Illustrations and diagrams**:
    - All images must be in WebP format. Use this free tool to convert them if needed: [ImagesConverter](https://github.com/LoicPandul/ImagesConverter).
    - Name visuals sequentially with 2 or 3 digits (e.g., `001.webp`, `002.webp`).
    - When creating a tutorial on a smartphone or hardware wallet, it’s better to use mockups for the images. You can either ask the design team to do it for you in advance or do it yourself.
    - Use only visuals you created yourself or those that are free to use under the original license.
    - Ensure visuals are relevant and of sufficient quality.

- **Compliance with the graphic charter**:
    - Use the [Rubik font](https://fonts.google.com/specimen/Rubik) for visuals.
    - Follow Plan B Network's color codes:
        - Orange: `#FF5C00`
        - Black: `#000000`
        - White: `#FFFFFF`

- **Clarity and accessibility**:
    - Avoid complex technical words without explanation, especially for beginner tutorials.
    - Tailor your content to the indicated level (`beginner`, `intermediate`, etc.).

## Suggested tools

- For Markdown file editing:
    - **Obsidian** (Free, not open-source)
    - **Mark Text** (Free, open-source)
    - **Zettlr** (Free, open-source)
    - **Typora** (Paid, ~€15, not open-source)

- For Git:
    - **Git** (Free, open-source)
    - **GitHub Desktop** (Free, open-source)
    - **Sourcetree** (Free, not open-source)

- For YAML file editing:
    - **Visual Studio Code** (Free, open-source)
    - **Sublime Text** (Free with limitations, not open-source)

- For creating diagrams and visuals:
    - **Canva** (Free with paid options, not open-source)
    - **Inkscape** (Free, open-source)
    - **Penpot** (Free, open-source)
