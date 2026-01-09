---
name: Building a Lightning Wallet Frontend
goal: Learn Bitcoin programming fundamentals and development to build practical Lightning Network applications and tools.
objectives:
  - Learn tools and techniques used in professional development
  - Specialized training for Bitcoin/Lightning development
  - Build real applications, not just theory
  - Get into production deployment
---

# About This Course
Welcome to PlebDevs Frontend Course! In this comprehensive 6-lesson journey, we'll transform you from a starting developer into a proficient frontend developer with a special focus on Lightning App Development. This course builds on frontend fundamentals to create lightning network applications.

**What You'll Build**
- **HTML5** - Structure and markup for web applications
- **CSS** - Styling and responsive design
- **JavaScript** - Programming fundamentals and DOM manipulation
- **API Calls** - Connecting to external services and APIs
- **React** - Modern frontend framework for building user interfaces
- **Lightning Wallet Basics** - Integration with LNbits for Bitcoin payments
- **GitHub/Git Fundamentals** - Version control and collaboration
- **Visual Studio Code** - Professional development environment setup
- **Vercel** - Modern deployment and hosting platform

+++

# Introduction
<partId>bf4836ec-ca04-4354-832b-db50bc90d4d1</partId>

## Course overview
<chapterId>12aad4f3-b584-46cc-9a15-11270c578e4f</chapterId>

Welcome to the PlebDevs Frontend Course - your one-stop shop to learn how to build your first Lightning app! This comprehensive course will take you from an absolute beginner to a capable frontend developer focusing on Bitcoin/Lightning projects in under 6 hours.

Our instructors, **Super Testnet** and **Austin**, have put together this accelerated course to condense all the fundamentals of frontend development and fast-track your path toward developing apps on your own. Both instructors have built cutting-edge projects on Bitcoin and Lightning, conduct workshops inside of PlebLab, and learned how to code from ZERO without prior experience.

Using our exciting, hands-on teaching style, you are sure to master the principles AND have fun at the same time!

### 🚀 What You Will Learn

- **HTML5** - Structure and markup for web applications
- **CSS** - Styling and responsive design
- **JavaScript** - Programming fundamentals and DOM manipulation
- **API Calls** - Connecting to external services and APIs
- **React** - Modern frontend framework for building user interfaces
- **Lightning Wallet Basics** - Integration with LNbits for Bitcoin payments
- **GitHub/Git Fundamentals** - Version control and collaboration
- **Visual Studio Code** - Professional development environment setup
- **Vercel** - Modern deployment and hosting platform

### Course Structure


| Lesson | Topic | Description |
|--------|-------|-------------|
| **Lesson 1** | Intro to the Course | Course overview and setup |
| **Lesson 2** | Learn HTML | Building blocks of web pages |
| **Lesson 3** | Learn CSS | Styling and layout fundamentals |
| **Lesson 4** | Learn JavaScript | Programming logic and interactivity |
| **Lesson 5** | Development Environment Setup | Professional dev tools and workflow |
| **Lesson 6** | Learn React | Modern frontend framework |
| **Lesson 7** | Pleb Wallet Demo | Final project walkthrough |

### Final Project

Build a complete **Lightning Wallet Frontend** application! 

**Repository**: [pleb-wallet-frontend](https://github.com/pleb-devs/pleb-wallet-frontend)

The final project demonstrates:
- Modern React application architecture
- Lightning Network integration
- Professional UI/UX design
- Real-world Bitcoin/Lightning functionality
- Complete deployment pipeline

### Why This Course?

#### For Bitcoin Developers
- **Specialized Focus**: Unlike generic web development courses, this focuses specifically on Bitcoin/Lightning applications
- **Real-World Skills**: Learn tools and patterns used in actual Bitcoin projects
- **Community Connection**: Join a thriving ecosystem of Bitcoin developers

#### For New Developers
- **Accelerated Learning**: 6 hours to go from beginner to building real apps
- **Practical Approach**: Learn by building, not just reading
- **Expert Instruction**: Learn from developers who've built successful Bitcoin projects

Ready to build your first Lightning app? Let's start with Lesson 1! ⚡🚀 

# Introducing Frontend Development 
<partId>e48f404b-0536-4e65-8d87-4d4eadeef91f</partId>

## HTML Fundamentals & Layout Logic
<chapterId>d7997b5b-fb48-476c-a734-e4e9e2a4a16a</chapterId>

### What is HTML?

#### Definition
HTML is a markup language that instructs web browsers how to display a web page. It's not a programming language since it can't perform calculations - it simply tells browsers how to display images, text, and other content.

#### How HTML Works
1. **HTML documents are hosted on servers**
2. **When you visit a website, your browser downloads the HTML document**
3. **The browser reads the HTML and displays the content according to the instructions**

#### Basic HTML Structure
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>My Page Title</title>
    </head>
    <body>
        <h1>Hello World!</h1>
        <p>This is my first HTML page.</p>
    </body>
</html>
```

### The Box Model & Layout basics

#### What is the Box Model?
HTML uses a box model to display content. It divides content into different boxes (called elements) and displays those boxes on the page.

#### Basic Example
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
        <div class="greeting">
            Hello world!
        </div>
        <div class="info">
            This div illustrates HTML's box model
        </div>
    </body>
</html>
```

#### Visualizing Boxes
To see the box model in action, add background colors:
```html
<div style="background-color: red">
    Hello world!
</div>
<div style="background-color: yellow">
    This div illustrates HTML's box model
</div>
```

### Element Flow: Block vs. Inline Elements

#### Block Elements
- **Cover the full width of the page**
- **Force new lines before and after**
- **Examples**: `<div>`, `<p>`, `<h1>`, `<h2>`

#### Inline Elements
- **Have variable width**
- **Multiple inline elements can be on the same line**
- **Examples**: `<span>`, `<a>`, `<img>`

#### Example Comparison
```html
<!-- Block elements (stacked) -->
<div>Block element 1</div>
<div>Block element 2</div>

<!-- Inline elements (side by side) -->
<span>Inline element 1</span>
<span>Inline element 2</span>
```

## Essential HTML Components & Data
<chapterId>5570c27f-6980-4514-af32-770e5f330b59</chapterId>

### Common HTML Elements

#### Document Structure
| Element | Purpose |
|---------|---------|
| `<!DOCTYPE html>` | Declares document type |
| `<html>` | Root element |
| `<head>` | Document metadata |
| `<body>` | Visible content |
| `<meta>` | Metadata (charset, viewport) |
| `<title>` | Page title (appears in browser tab) |

#### Content Elements
| Element | Purpose | Type |
|---------|---------|------|
| `<div>` | Generic container | Block |
| `<span>` | Generic inline container | Inline |
| `<p>` | Paragraph | Block |
| `<h1>`, `<h2>` | Headers | Block |
| `<a>` | Links | Inline |
| `<img>` | Images | Inline |
| `<br>` | Line break | None |
| `<hr>` | Horizontal rule (line) | Block |

#### Form Elements
| Element | Purpose | Type |
|---------|---------|------|
| `<form>` | Form container | Block |
| `<input>` | User input field | Inline |
| `<textarea>` | Multi-line text input | Inline |
| `<button>` | Clickable button | Inline |

### Element Attributes & Metadata

#### Common Attributes
- **`style`** - Change appearance (color, font, size)
- **`class`** - Categorization and CSS/JavaScript hooks
- **`id`** - Unique identifier for anchor links
- **`name`** - Pass form data to servers
- **`data-*`** - Custom attributes

#### Attribute Examples
```html
<div class="word" style="background-color: red">Text</div>
<a href="https://google.com" id="google-link">Google</a>
<input name="username" type="text" placeholder="Enter username">
```

#### Anchor Links
Create internal page navigation:
```html
<a href="#section1">Go to Section 1</a>
<p id="section1">This is section 1</p>
```

### Working with Forms

#### Basic Form Structure
```html
<form action="/login/">
    <p><input name="username" type="text" placeholder="username"></p>
    <p><textarea name="message"></textarea></p>
    <p><button>Submit</button></p>
</form>
```

#### Form Behavior
- **Action attribute**: Where to send form data
- **Name attributes**: Identify form fields
- **Submit button**: Triggers form submission
- **URL encoding**: Data appears as `?username=value&message=value`

#### Important Note
Forms require server-side code or JavaScript to process data. Without it, forms will either do nothing or show errors.

## Practical Project: The Bitcoin Blog
<chapterId>0f7e874d-b850-43e1-ba43-bf1fe67e5bd5</chapterId>

### Building Your Bitcoin Blog

##### Project Overview
We'll create a blog post about Bitcoin using the Bitcoin whitepaper content. This will include:
- Header with title and author info
- Abstract and introduction sections
- Comment form (non-functional)
- Basic CSS styling

#### Step 1: Basic Structure
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Bitcoin Blog</title>
    </head>
    <body>
        <h1>Bitcoin: A Peer-to-Peer Electronic Cash System</h1>
        <div class="info">
            Satoshi Nakamoto<br>
            satoshin@gmx.com<br>
            www.bitcoin.org<br>
        </div>
    </body>
</html>
```

#### Step 2: Add Content
```html
<p class="abstract">
    Abstract. A purely peer-to-peer version of electronic cash would allow online payments to be sent directly from one party to another without going through a financial institution. Digital signatures provide part of the solution, but the main benefits are lost if a trusted third party is still required to prevent double-spending. We propose a solution to the double-spending problem using a peer-to-peer network...
</p>

<h2 class="introduction">I. Introduction</h2>

<p>
    Commerce on the Internet has come to rely almost exclusively on financial institutions serving as trusted third parties to process electronic payments...
</p>
```

#### Step 3: Add Comment Section
```html
<hr>
<h2 class="comments">Comments</h2>

<p>Name</p>
<p class="input_name">
    <input type="text" name="name">
</p>

<p>Comment</p>
<p>
    <textarea rows="8" name="comment" class="input_comment"></textarea>
</p>

<p>
    <button type="button" name="submit_comment">Submit</button>
</p>
```

#### Step 4: Add Basic Styling
```html
<head>
    <meta charset="UTF-8">
    <style>
        * {
            box-sizing: border-box;
            font-size: 1.15em;
            font-family: Arial, sans-serif;
        }
        html {
            max-width: 70ch;
            padding: 3em 1em;
            margin: auto;
            line-height: 1.25;
        }
        h1 {
            font-size: 2em;
        }
        h2 {
            font-size: 1.5em;
        }
        input, textarea {
            width: 100%;
            height: 1.8em;
            border: 1px solid grey;
        }
        textarea {
            height: auto;
        }
        .info {
            text-align: center;
        }
    </style>
</head>
```

#### Step 5: Add Navigation
```html
<nav>
    <a href="https://example.com/home.html">
        &larr; more articles
    </a>
</nav>
```

#### What CSS Does
- **Cascading Style Sheets** make your HTML look beautiful
- **Separates content from presentation**
- **Enables responsive design**

#### Key CSS Concepts
- **Selectors**: Target specific elements (`*`, `html`, `h1`, `.class`)
- **Properties**: What to change (`color`, `font-size`, `margin`)
- **Values**: How to change it (`red`, `2em`, `auto`)
- **Cascading**: Later rules override earlier ones

#### Box Sizing
```css
* {
    box-sizing: border-box;
}
```
This ensures borders and padding are included in element width calculations.

### Best Practices and Common Issues

#### 1. File Organization
- Use descriptive filenames (`blog.html`, not `page1.html`)
- Keep related files together
- Use lowercase for file names

#### 2. Code Structure
- Proper indentation makes code readable
- Use meaningful class names
- Add comments for complex sections

#### 3. Semantic HTML
- Use appropriate elements for their purpose
- `<h1>` for main headings, `<p>` for paragraphs
- `<nav>` for navigation, `<main>` for main content

#### 4. Testing
- Test in multiple browsers
- Use "View Page Source" to learn from other sites
- Validate your HTML

#### Common Issues and Solutions

#### 1. Elements Not Displaying
- Check for unclosed tags
- Ensure proper nesting
- Verify file saved with `.html` extension

#### 2. Styles Not Working
- Check for typos in CSS
- Ensure CSS is in `<head>` section
- Remember cascading order matters

#### 3. Forms Not Working
- Forms need server-side processing
- Use `action` attribute to specify destination
- Include `name` attributes on inputs

### Hands-on Exercises and Next Steps

#### Exercise 1: Personal Blog Post
1. Create a new HTML file
2. Write a blog post about why you're learning Bitcoin development
3. Include headers, paragraphs, and a comment form
4. Add basic styling

#### Exercise 2: Navigation Practice
1. Create multiple HTML pages
2. Link them together with navigation
3. Use anchor links for internal navigation
4. Test all links work correctly

#### Exercise 3: Form Experimentation
1. Create a contact form
2. Include different input types
3. Add placeholder text
4. Style the form elements

#### Learning Resources

#### Essential References
- **[W3Schools HTML Tutorial](https://www.w3schools.com/html/)** - Comprehensive HTML reference
- **[MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML)** - Official documentation
- **[HTML Validator](https://validator.w3.org/)** - Check your HTML

#### Search Tips
When you don't know how to do something:
1. Google: "How do I [what you want] in HTML?"
2. Include "w3schools" in your search
3. Use "View Page Source" on websites you like
4. Practice with online code editors

#### Example Searches
- "w3schools checkboxes HTML"
- "how to make left arrow HTML"
- "HTML table tutorial"
- "responsive HTML forms"

#### Next Steps

#### Immediate Actions
1. **Complete the blog project** from this lesson
2. **Experiment with different HTML elements**
3. **Practice viewing source code** on websites
4. **Start building your own pages**

#### Prepare for Next Lesson
In the next lesson, we'll dive deeper into CSS and learn how to:
- Style your HTML professionally
- Create responsive layouts
- Use CSS frameworks
- Make your Bitcoin blog look amazing

#### Building Your Portfolio
- Save all your HTML files
- Create a simple portfolio page
- Link your projects together
- Share your work on GitHub

#### Key Takeaways

1. **HTML is the foundation** of all web development
2. **Box model understanding** is crucial for layout
3. **Practice by building** real projects
4. **View source** to learn from others
5. **Google is your friend** for specific questions
6. **Start simple** and iterate

Remember: Every expert was once a beginner. The key is to start coding, make mistakes, learn from them, and keep building. Your Bitcoin blog is the first step in your journey to becoming a Lightning developer!

Happy coding! ⚡️

---

### Complete Blog Example

Here's the complete HTML for the Bitcoin blog we built in this lesson:

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Bitcoin Blog</title>
        <style>
            * {
                box-sizing: border-box;
                font-size: 1.15em;
                font-family: Arial, sans-serif;
            }
            html {
                max-width: 70ch;
                padding: 3em 1em;
                margin: auto;
                line-height: 1.25;
            }
            h1 {
                font-size: 2em;
            }
            h2 {
                font-size: 1.5em;
            }
            input, textarea {
                width: 100%;
                height: 1.8em;
                border: 1px solid grey;
            }
            textarea {
                height: auto;
            }
            .info {
                text-align: center;
            }
        </style>
    </head>
    <body>
        <nav>
            <a href="https://example.com/home.html">
                &larr; more articles
            </a>
        </nav>
        <h1>
            Bitcoin: A Peer-to-Peer Electronic Cash System
        </h1>
        <div class="info">
            Satoshi Nakamoto<br>
            satoshin@gmx.com<br>
            www.bitcoin.org<br>
        </div>
        <p class="abstract">
            Abstract. A purely peer-to-peer version of electronic cash would allow online payments to be sent directly from one party to another without going through a financial institution. Digital signatures provide part of the solution, but the main benefits are lost if a trusted third party is still required to prevent double-spending. We propose a solution to the double-spending problem using a peer-to-peer distributed timestamp server to generate computational proof of the chronological order of transactions. The system is secure as long as honest nodes collectively control more CPU power than any cooperating group of attacker nodes.
        </p>
        <h2 class="introduction">
            I. Introduction
        </h2>
        <p>
            Commerce on the Internet has come to rely almost exclusively on financial institutions serving as trusted third parties to process electronic payments. While the system works well enough for most transactions, it still suffers from the inherent weaknesses of the trust based model. Completely non-reversible transactions are not really possible, since financial institutions cannot avoid mediating disputes. The cost of mediation increases transaction costs, limiting the minimum practical transaction size and cutting off the possibility for small casual transactions, and there is a broader cost in the loss of ability to make non-reversible payments for non-reversible services. With the possibility of reversal, the need for trust spreads. Merchants must be wary of their customers, hassling them for more information than they would otherwise need. A certain percentage of fraud is accepted as unavoidable. These costs and payment uncertainties can be avoided in person by using physical currency, but no mechanism exists to make payments over a communications channel without a trusted party.
        </p>
        <p>
            What is needed is an electronic payment system based on cryptographic proof instead of trust, allowing any two willing parties to transact directly with each other without the need for a trusted third party. Transactions that are computationally impractical to reverse would protect sellers from fraud, and routine escrow mechanisms could easily be implemented to protect buyers. In this paper, we propose a solution to the double-spending problem using a peer-to-peer distributed timestamp server to generate computational proof of the chronological order of transactions. The system is secure as long as honest nodes collectively control more CPU power than any cooperating group of attacker nodes.
        </p>
        <hr>
        <h2 class="comments">
            Comments
        </h2>
        <p>
            Name
        </p>
        <p class="input_name">
            <input type="text" name="name">
        </p>
        <p>
            Comment
        </p>
        <p>
            <textarea rows="8" name="comment" class="input_comment"></textarea>
        </p>
        <p>
            <button type="button" name="submit_comment">Submit</button>
        </p>
    </body>
</html>
```

Save this as `blog.html` and open it in your browser to see your Bitcoin blog in action! 

## Learn CSS: CSS Foundations & Style Logic
<chapterId>ee807797-77f6-453c-9adc-7a28ea43d883</chapterId>

### Introduction to CSS

#### Definition
CSS (Cascading Style Sheets) is a rule-based language that describes how HTML elements should be displayed. While HTML provides the structure and content, CSS handles the presentation - colors, fonts, layout, spacing, and visual effects.

#### Why CSS Matters
- **Separates content from presentation** - Keep HTML clean and semantic
- **Enables responsive design** - Adapt to different screen sizes
- **Provides consistency** - Maintain unified styling across pages
- **Enhances user experience** - Create engaging, professional interfaces

#### CSS Rule Structure
```css
selector {
    property: value;
    property: value;
}
```

### CSS Integration Methods

#### 1. Inline Styles (Avoid)
```html
<p style="color: blue; font-size: 16px;">This is inline styling</p>
```
**Why avoid:** Hard to maintain, violates separation of concerns, poor reusability.

#### 2. Internal Styles (Limited Use)
```html
<head>
    <style>
        p {
            color: blue;
            font-size: 16px;
        }
    </style>
</head>
```

#### 3. External Stylesheets (Recommended)
```html
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```

**Benefits:**
- Clean separation of concerns
- Reusable across multiple pages
- Better organization and maintainability
- Improved performance (caching)

### CSS Properties Fundamentals

#### Understanding Properties
CSS properties are the styles you apply to elements. Each property has a specific purpose and accepts certain values.

#### Property Syntax
```css
element {
    property-name: value;
    another-property: another-value;
}
```

#### The Cascade
CSS properties are read **top to bottom** and can be overwritten:

```css
p {
    color: pink;
    color: yellow; /* This wins - yellow text */
}
```

You can use this strategically:
```css
.footer {
    margin: 1% auto; /* General margin */
    margin-bottom: 0;  /* Specific override */
}
```

#### Essential CSS Properties

| Property | Purpose | Example |
|----------|---------|---------|
| `color` | Text color | `color: #8a4fff;` |
| `font-size` | Text size | `font-size: 1.2rem;` |
| `font-family` | Font type | `font-family: monospace;` |
| `font-weight` | Text boldness | `font-weight: bold;` |
| `background-color` | Background color | `background-color: #192734;` |
| `margin` | Outer spacing | `margin: 10px;` |
| `padding` | Inner spacing | `padding: 1%;` |
| `border` | Element border | `border: 2px solid #ffbf46;` |
| `border-radius` | Rounded corners | `border-radius: 5px;` |
| `width` | Element width | `width: 100%;` |
| `height` | Element height | `height: 300px;` |

### CSS Units

#### Understanding Units
CSS units define measurements for properties like width, height, margin, and font-size.

#### Absolute Units
Fixed measurements that remain the same across devices:
- **px (pixels)** - `1px = 1/96th of 1 inch`
- Use for: borders, small fixed elements

#### Relative Units
Measurements relative to other elements or viewport:

| Unit | Description | Use Case |
|------|-------------|----------|
| `%` | Relative to parent element | Responsive widths |
| `rem` | Relative to root font size | Scalable typography |
| `em` | Relative to current font size | Component-based sizing |
| `vw` | 1% of viewport width | Full-width elements |
| `vh` | 1% of viewport height | Full-height elements |

#### Unit Examples
```css
.container {
    width: 80%;        /* 80% of parent width */
    padding: 2rem;     /* 2x root font size */
    font-size: 1.2rem; /* 1.2x root font size */
    border: 1px solid black; /* 1 pixel border */
}

.hero {
    height: 100vh;     /* Full viewport height */
    width: 100vw;      /* Full viewport width */
}
```
## Precision Styling & Selectors
<chapterId>41895064-cdc6-4aeb-bdfb-736b216b917c</chapterId>


### The Power of Selectors

#### What Are Selectors?
Selectors determine which HTML elements receive your CSS styles. They're patterns that match elements in your HTML.

#### Basic Selector Types

##### 1. Universal Selector
```css
* {
    box-sizing: border-box; /* Applies to all elements */
}
```

##### 2. Type Selector (Element Selector)
```css
p {
    color: blue; /* All paragraphs */
}

h1 {
    font-size: 2rem; /* All h1 elements */
}
```

##### 3. Class Selector (Most Important)
```css
.button {
    background-color: #ffbf46;
    padding: 10px;
}
```

HTML usage:
```html
<button class="button">Click me</button>
<div class="button">Styled div</div>
```

##### 4. ID Selector (Avoid for Styling)
```css
##header {
    background-color: red;
}
```

**Why avoid IDs:** Too specific, hard to override, poor reusability.

#### Combining Selectors

##### Descendant Selectors
```css
/* Any p inside a footer */
footer p {
    color: #8a4fff;
}

/* Any p inside an element with class balance-card */
.balance-card p {
    font-weight: bold;
}
```

##### Multiple Classes
```css
/* Element must have both classes */
.button.primary {
    background-color: blue;
}
```

#### CSS Specificity

##### How Specificity Works
When multiple rules target the same element, specificity determines which rule wins:

1. **Inline styles** (avoid) - Highest specificity
2. **IDs** (avoid for styling) - High specificity  
3. **Classes** (use these) - Medium specificity
4. **Elements** (use for general styling) - Low specificity

##### Specificity Example
```css
p {
    color: yellow; /* Specificity: 1 */
}

.text {
    color: blue; /* Specificity: 10 - This wins */
}

div p {
    color: red; /* Specificity: 2 */
}
```

#### Pseudo-Classes

##### Hover Effects
```css
.button:hover {
    cursor: pointer;
    opacity: 0.8;
}
```

##### Common Pseudo-Classes
- `:hover` - Mouse over element
- `:focus` - Element has focus
- `:active` - Element is being clicked
- `:first-child` - First child element
- `:last-child` - Last child element

### CSS Flexbox

#### What is Flexbox?
Flexbox is a modern layout method that makes it easy to align and distribute space among items in a container, even when their size is unknown or dynamic.

#### Basic Flexbox Setup
```css
.container {
    display: flex; /* Activates flexbox */
    flex-direction: row; /* Default: horizontal */
    justify-content: space-between; /* Distribute space */
    align-items: center; /* Vertical alignment */
}
```

#### Key Flexbox Properties

##### Container Properties
```css
.flex-container {
    display: flex;
    flex-direction: row | column;
    justify-content: flex-start | center | flex-end | space-between | space-around | space-evenly;
    align-items: stretch | flex-start | center | flex-end;
    flex-wrap: nowrap | wrap;
}
```

##### Item Properties
```css
.flex-item {
    flex-grow: 1; /* Grow to fill space */
    flex-shrink: 1; /* Shrink if needed */
    flex-basis: auto; /* Initial size */
}
```

#### Flexbox Examples
```css
/* Horizontal button row */
.buttons {
    display: flex;
    justify-content: space-around;
    gap: 10px;
}

/* Centered content */
.hero {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* Responsive cards */
.card-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}
```

### Responsive Design with Media Queries

#### Understanding Media Queries
Media queries allow you to apply different styles based on device characteristics like screen width, height, or orientation.

#### Basic Media Query Syntax
```css
@media (max-width: 768px) {
    /* Styles for screens 768px and smaller */
    .container {
        width: 100%;
        padding: 10px;
    }
}
```

#### Common Breakpoints
```css
/* Mobile first approach */
.container {
    width: 100%; /* Mobile default */
}

/* Tablet and up */
@media (min-width: 768px) {
    .container {
        width: 80%;
    }
}

/* Desktop and up */
@media (min-width: 1024px) {
    .container {
        width: 60%;
    }
}
```

#### Media Query Types
```css
/* Width-based */
@media (max-width: 600px) { }
@media (min-width: 600px) { }

/* Height-based */
@media (max-height: 400px) { }

/* Orientation */
@media (orientation: landscape) { }
@media (orientation: portrait) { }
```

## The Pleb Wallet & Workflow
<chapterId>40ec5e6f-17f1-4523-a203-acc8d973380b</chapterId>

### Building the Pleb Wallet Project

#### Project Overview
We'll build a complete Bitcoin wallet interface featuring:
- Responsive design (desktop and mobile)
- Modern CSS techniques
- Professional styling
- Interactive hover effects

#### Step 1: Project Setup

##### Create Project Structure
```
pleb-wallet/
├── index.html
├── index.css
└── BTCUSD.png
```

##### HTML Boilerplate
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Pleb Wallet</title>
    <link rel="stylesheet" href="index.css">
</head>
<body>
    <p>Hello world!</p>
</body>
</html>
```

##### Test CSS Connection
```css
/* index.css */
p {
    color: green;
}
```

#### Step 2: HTML Structure

```html
<body>
    <header>
        <h1>Pleb Wallet</h1>
    </header>
    
    <main>
        <div class="buttons">
            <button>Send</button>
            <button>Receive</button>
        </div>
        
        <div class="row">
            <div class="balance-card">
                <h2>Balance</h2>
                <p>897900 sats</p>
            </div>
            <div class="balance-card">
                <h2>Price</h2>
                <p>$19,364</p>
            </div>
        </div>
        
        <div class="row">
            <div class="row-item">
                <h3>Transactions</h3>
                <p class="transaction">Sent to bc1xxxxxxxxxxxxxxxx</p>
                <p class="transaction-amount">-2200 sats</p>
                <p class="transaction">Received from bc1xxxxxxxxxxxxxxxx</p>
                <p class="transaction-amount">+100 sats</p>
                <p class="transaction">Received to bc1xxxxxxxxxxxxxxxx</p>
                <p class="transaction-amount">+900000 sats</p>
                <p class="transaction">Sent to bc1xxxxxxxxxxxxxxxx</p>
                <p class="transaction-amount">-2200 sats</p>
                <p class="transaction">Received from bc1xxxxxxxxxxxxxxxx</p>
                <p class="transaction-amount">+100 sats</p>
                <p class="transaction">Received to bc1xxxxxxxxxxxxxxxx</p>
                <p class="transaction-amount">+900000 sats</p>
            </div>
            <div class="row-item">
                <img src="./BTCUSD.png" alt="Bitcoin Price Chart" />
            </div>
        </div>
    </main>
    
    <footer>
        <p>Made by plebs, for plebs.</p>
    </footer>
</body>
```

#### Step 3: Base Styles (Type Selectors)

```css
/* Global styles */
body {
    background-color: #192734;
    font-family: monospace;
    margin: 0;
    padding: 0;
}

/* Header */
header {
    border-bottom: 2px solid #ffbf46;
}

h1 {
    text-align: center;
    color: #8a4fff;
    margin: 20px 0;
}

/* Images */
img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Footer */
footer {
    border-top: 2px solid #ffbf46;
    padding: 1%;
    text-align: center;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #192734;
}

footer p {
    color: #8a4fff;
    margin: 0;
}
```

#### Step 4: Component Styles (Class Selectors)

```css
/* Button container */
.buttons {
    width: 50%;
    margin: 0 auto;
    margin-top: 3%;
    display: flex;
    justify-content: space-around;
}

/* Button styles */
.buttons button {
    background-color: #ffbf46;
    border: 2px solid #8a4fff;
    border-radius: 5px;
    padding: 10px 15px;
    font-size: 1.2rem;
    width: 100px;
    cursor: pointer;
    transition: opacity 0.3s ease;
}

.buttons button:hover {
    opacity: 0.6;
}

/* Balance cards */
.balance-card {
    background-color: #ffbf46;
    border: 2px solid #8a4fff;
    padding: 1%;
    width: 25%;
    margin-top: 3%;
    margin-bottom: 1%;
    border-radius: 5px;
}

.balance-card h2 {
    margin: 0 0 10px 0;
    color: #192734;
}

.balance-card p {
    font-size: 1.2rem;
    font-weight: bold;
    margin: 0;
    color: #192734;
}

/* Layout rows */
.row {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 0 20px;
}

/* Row items */
.row-item {
    background-color: ghostwhite;
    border: 2px solid #8a4fff;
    border-radius: 5px;
    height: 300px;
    width: 40%;
    overflow: scroll;
    padding: 10px;
}

.row-item h3 {
    margin: 0 0 15px 0;
    color: #192734;
}

.row-item p {
    margin: 5px 0;
    color: #192734;
}

/* Transaction styles */
.transaction-amount {
    border-bottom: 1px solid #ccc;
    padding-bottom: 10px;
    margin-bottom: 10px;
    font-weight: bold;
}
```

#### Step 5: Responsive Design

```css
/* Tablet breakpoint */
@media (max-width: 876px) {
    .row-item {
        width: 100%;
        height: 200px;
        margin-bottom: 20px;
    }
    
    .balance-card {
        width: 100%;
        text-align: center;
        margin-right: 2%;
        margin-left: 2%;
    }
    
    .buttons {
        width: 80%;
    }
}

/* Mobile breakpoint */
@media (max-width: 615px) {
    .row {
        flex-direction: column;
        padding: 0 10px;
    }
    
    .row-item {
        width: 100%;
        margin-top: 15px;
    }
    
    .balance-card {
        width: 80%;
        margin: 15px auto;
    }
    
    .buttons {
        width: 90%;
        margin-top: 20px;
    }
    
    .buttons button {
        width: 80px;
        font-size: 1rem;
    }
    
    /* Add padding to prevent footer overlap */
    main {
        padding-bottom: 80px;
    }
}
```

### Advanced CSS Techniques and Best Practices

#### Box Model Understanding
```css
/* Better box model */
* {
    box-sizing: border-box;
}
```

This ensures padding and borders are included in element width calculations.

#### CSS Custom Properties (Variables)
```css
:root {
    --primary-color: #8a4fff;
    --secondary-color: #ffbf46;
    --background-color: #192734;
    --text-color: white;
}

.button {
    background-color: var(--secondary-color);
    color: var(--background-color);
}
```

#### Transitions and Animations
```css
.button {
    transition: all 0.3s ease;
}

.button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}
```

#### CSS Grid (Alternative to Flexbox)
```css
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
}
```

#### CSS Organization 

#### 1. File Structure
```
styles/
├── base/
│   ├── reset.css
│   └── typography.css
├── components/
│   ├── buttons.css
│   └── cards.css
├── layout/
│   ├── header.css
│   └── footer.css
└── main.css
```

#### 2. Naming Conventions (BEM)
```css
/* Block Element Modifier */
.wallet-card { }              /* Block */
.wallet-card__title { }       /* Element */
.wallet-card--highlighted { } /* Modifier */
```

#### 3. CSS Organization Order
```css
.component {
    /* 1. Display & Layout */
    display: flex;
    position: relative;
    
    /* 2. Dimensions */
    width: 100%;
    height: 50px;
    
    /* 3. Spacing */
    margin: 10px;
    padding: 15px;
    
    /* 4. Colors & Typography */
    color: #333;
    font-size: 16px;
    
    /* 5. Borders & Shadows */
    border: 1px solid #ccc;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    
    /* 6. Transitions */
    transition: all 0.3s ease;
}
```

### Testing and Debugging

#### Browser Developer Tools
1. **Right-click → Inspect** to open DevTools
2. **Elements tab** - View and edit HTML/CSS live
3. **Console tab** - See errors and warnings
4. **Device toolbar** - Test responsive design

#### CSS Debugging Tips
```css
/* Temporary border to see element boundaries */
.debug {
    border: 1px solid red !important;
}

/* Use background colors to understand layout */
.container {
    background-color: rgba(255, 0, 0, 0.1);
}
```

#### Common CSS Issues
1. **Specificity conflicts** - Use more specific selectors
2. **Box model confusion** - Add `box-sizing: border-box`
3. **Flexbox alignment** - Check `justify-content` vs `align-items`
4. **Mobile responsiveness** - Test on actual devices

#### Performance Optimization

#### CSS Performance Tips
1. **Minimize CSS file size**
2. **Use efficient selectors**
3. **Avoid deep nesting**
4. **Use CSS compression**
5. **Optimize images**

#### Efficient Selectors
```css
/* Good - specific and fast */
.button { }
.card__title { }

/* Avoid - too generic */
* { }
div div div p { }
```

### Practice & Resources

#### Hands-on Exercises

**Exercise 1: Customize the Pleb Wallet**
1. Change the color scheme to your preference
2. Add a new section for "Recent Activity"
3. Implement a dark/light mode toggle
4. Add animations to button hovers

**Exercise 2: Build a Bitcoin Price Dashboard**
1. Create a grid layout for multiple cryptocurrencies
2. Add price change indicators (green/red arrows)
3. Make it fully responsive
4. Add a search filter

**Exercise 3: Create a Lightning Invoice Generator**
1. Build a form with proper styling
2. Add validation styling (error states)
3. Create a QR code display area
4. Style for mobile-first design

#### Essential References
- **[CSS-Tricks](https://css-tricks.com/)** - Comprehensive CSS guide
- **[MDN CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS)** - Official documentation
- **[Can I Use](https://caniuse.com/)** - Browser compatibility checker
- **[Flexbox Froggy](https://flexboxfroggy.com/)** - Interactive Flexbox game
- **[CSS Grid Garden](https://cssgridgarden.com/)** - CSS Grid learning game

#### Advanced Learning
- **[CSS Animations](https://robots.thoughtbot.com/transitions-and-transforms)** - Transitions and transforms
- **[CSS Architecture](https://sass-lang.com/)** - SASS and CSS preprocessing
- **[CSS Frameworks](https://tailwindcss.com/)** - Tailwind CSS
- **[CSS-in-JS](https://styled-components.com/)** - Modern CSS solutions

#### Design Inspiration
- **[Dribbble](https://dribbble.com/)** - Design inspiration
- **[Behance](https://behance.net/)** - Creative portfolios
- **[Awwwards](https://awwwards.com/)** - Award-winning web design
- **[CodePen](https://codepen.io/)** - CSS experiments and demos

#### Next Steps

**Immediate Actions**
1. **Complete the Pleb Wallet project** with all responsive features
2. **Experiment with different layouts** using Flexbox and Grid
3. **Practice media queries** on various screen sizes
4. **Build your own Bitcoin-themed components**

#### Prepare for Next Lesson
In the next lesson, we'll dive into JavaScript and learn how to:
- Add interactivity to our wallet
- Make API calls to get real Bitcoin prices
- Handle user input and form validation
- Create dynamic content updates
- Connect to Lightning Network services

#### Building Your Portfolio
- Create multiple CSS projects
- Experiment with different design patterns
- Build responsive layouts
- Share your work on CodePen or GitHub

#### Key Takeaways

1. **CSS is about presentation** - Separate styling from content
2. **Selectors are powerful** - Use classes for styling, avoid IDs
3. **Flexbox simplifies layouts** - Modern solution for alignment
4. **Mobile-first is essential** - Design for smallest screens first
5. **Practice makes perfect** - Build projects to solidify knowledge
6. **Tools are your friend** - Use browser DevTools for debugging
7. **Performance matters** - Write efficient, maintainable CSS

#### Troubleshooting Common Issues

- CSS Not Loading
```html
<!-- Check file path -->
<link rel="stylesheet" href="./styles.css">
<!-- vs -->
<link rel="stylesheet" href="styles.css">
```

- Styles Not Applying
1. Check selector specificity
2. Verify HTML class names match CSS
3. Look for typos in property names
4. Ensure proper syntax (semicolons, brackets)

- Responsive Issues
1. Add viewport meta tag
2. Test on actual devices
3. Use relative units (%, rem, em)
4. Check media query syntax

- Layout Problems
1. Use browser DevTools to inspect
2. Add temporary borders to see boundaries
3. Check box model with `box-sizing`
4. Verify Flexbox container/item properties

Remember: Every expert was once a beginner. The key is consistent practice and building real projects. Your Pleb Wallet is a solid foundation - now make it your own!

Happy styling! 🎨⚡️

---

#### Complete Pleb Wallet Code

#### HTML (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Pleb Wallet</title>
    <link rel="stylesheet" href="index.css">
</head>
<body>
    <header>
        <h1>Pleb Wallet</h1>
    </header>
    
    <main>
        <div class="buttons">
            <button onclick="alert('Send!')">Send</button>
            <button onclick="alert('Receive!')">Receive</button>
        </div>
        
        <div class="row">
            <div class="balance-card">
                <h2>Balance</h2>
                <p>897900 sats</p>
            </div>
            <div class="balance-card">
                <h2>Price</h2>
                <p>$19,364</p>
            </div>
        </div>
        
        <div class="row">
            <div class="row-item">
                <h3>Transactions</h3>
                <p class="transaction">Sent to bc1xxxxxxxxxxxxxxxx</p>
                <p class="transaction-amount">-2200 sats</p>
                <p class="transaction">Received from bc1xxxxxxxxxxxxxxxx</p>
                <p class="transaction-amount">+100 sats</p>
                <p class="transaction">Received to bc1xxxxxxxxxxxxxxxx</p>
                <p class="transaction-amount">+900000 sats</p>
                <p class="transaction">Sent to bc1xxxxxxxxxxxxxxxx</p>
                <p class="transaction-amount">-2200 sats</p>
                <p class="transaction">Received from bc1xxxxxxxxxxxxxxxx</p>
                <p class="transaction-amount">+100 sats</p>
                <p class="transaction">Received to bc1xxxxxxxxxxxxxxxx</p>
                <p class="transaction-amount">+900000 sats</p>
            </div>
            <div class="row-item">
                <img src="./BTCUSD.png" alt="Bitcoin Price Chart" />
            </div>
        </div>
    </main>
    
    <footer>
        <p>Made by plebs, for plebs.</p>
    </footer>
</body>
</html>
```

#### CSS (index.css)
```css
/* Global Styles */
body {
    background-color: #192734;
    font-family: monospace;
    margin: 0;
    padding: 0;
}

/* Header */
header {
    border-bottom: 2px solid #ffbf46;
}

h1 {
    text-align: center;
    color: #8a4fff;
    margin: 20px 0;
}

/* Images */
img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Footer */
footer {
    border-top: 2px solid #ffbf46;
    padding: 1%;
    text-align: center;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #192734;
}

footer p {
    color: #8a4fff;
    margin: 0;
}

/* Button Container */
.buttons {
    width: 50%;
    margin: 0 auto;
    margin-top: 3%;
    display: flex;
    justify-content: space-around;
}

/* Button Styles */
.buttons button {
    background-color: #ffbf46;
    border: 2px solid #8a4fff;
    border-radius: 5px;
    padding: 10px 15px;
    font-size: 1.2rem;
    width: 100px;
    cursor: pointer;
    transition: opacity 0.3s ease;
}

.buttons button:hover {
    opacity: 0.6;
}

/* Balance Cards */
.balance-card {
    background-color: #ffbf46;
    border: 2px solid #8a4fff;
    padding: 1%;
    width: 25%;
    margin-top: 3%;
    margin-bottom: 1%;
    border-radius: 5px;
}

.balance-card h2 {
    margin: 0 0 10px 0;
    color: #192734;
}

.balance-card p {
    font-size: 1.2rem;
    font-weight: bold;
    margin: 0;
    color: #192734;
}

/* Layout Rows */
.row {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 0 20px;
}

/* Row Items */
.row-item {
    background-color: ghostwhite;
    border: 2px solid #8a4fff;
    border-radius: 5px;
    height: 300px;
    width: 40%;
    overflow: scroll;
    padding: 10px;
}

.row-item h3 {
    margin: 0 0 15px 0;
    color: #192734;
}

.row-item p {
    margin: 5px 0;
    color: #192734;
}

/* Transaction Styles */
.transaction-amount {
    border-bottom: 1px solid #ccc;
    padding-bottom: 10px;
    margin-bottom: 10px;
    font-weight: bold;
}

/* Responsive Design */
@media (max-width: 876px) {
    .row-item {
        width: 100%;
        height: 200px;
        margin-bottom: 20px;
    }
    
    .balance-card {
        width: 100%;
        text-align: center;
        margin-right: 2%;
        margin-left: 2%;
    }
    
    .buttons {
        width: 80%;
    }
}

@media (max-width: 615px) {
    .row {
        flex-direction: column;
        padding: 0 10px;
    }
    
    .row-item {
        width: 100%;
        margin-top: 15px;
    }
    
    .balance-card {
        width: 80%;
        margin: 15px auto;
    }
    
    .buttons {
        width: 90%;
        margin-top: 20px;
    }
    
    .buttons button {
        width: 80px;
        font-size: 1rem;
    }
    
    /* Add padding to prevent footer overlap */
    main {
        padding-bottom: 80px;
    }
}
```

Save these files in your project folder and open `index.html` in your browser to see your complete Bitcoin wallet interface! 


# Learn JavaScript: Building Your First Bitcoin Wallet
<partId>d039b767-640f-43f9-b14d-b8b73af1e41a</partId>

## Introduction to JavaScript
<chapterId>bed2fa44-e3fd-4ee0-8f9b-60fef10c4181</chapterId>

### Definition and Why JavaScript Matters
JavaScript is the **only** programming language that runs natively in web browsers. While other languages can run on servers or desktop applications, JavaScript is unique because it's built into every web browser, making it the universal language of web development.

- **Interactivity** - Make websites respond to user actions
- **Dynamic content** - Update pages without refreshing
- **API integration** - Connect to external services and databases
- **Real-time updates** - Display live data like Bitcoin prices
- **User experience** - Create smooth, app-like experiences

**JavaScript's Role in Web Development**
```
HTML (Structure) + CSS (Style) + JavaScript (Behavior) = Complete Web Application
```

### Getting Started with JavaScript

#### Browser Console
Before writing JavaScript files, let's explore the browser console - your JavaScript playground.

##### Opening Developer Tools
1. **Chrome/Brave/Edge**: Menu → More Tools → Developer Tools
2. **Firefox**: Menu → More Tools → Web Developer Tools
3. **Safari**: Develop → Show Web Inspector

##### Your First JavaScript
Navigate to `example.com` and open the console, then try:

```javascript
console.log(`Hello, World!`);
console.log(`This is my first time using JavaScript`);
console.log(`Wow, this is easy!`);
```

#### How JavaScript Executes
JavaScript runs **line by line**, from top to bottom:

```javascript
console.log(`First line`);    // Runs first
console.log(`Second line`);   // Runs second  
console.log(`Third line`);    // Runs third
```

This sequential execution is crucial to understand as we build more complex applications.

### JavaScript Fundamentals

#### Data Types

##### Numbers vs Strings
Understanding the difference between numbers and strings is critical:

```javascript
// Numbers (green in Firefox console)
console.log(Number(3));
console.log(3 + 2); // = 5 (arithmetic)

// Strings (black in Firefox console)  
console.log(String(3));
console.log(String(3) + 2); // = "32" (concatenation)
```

##### Key Differences
- **Numbers**: Can perform arithmetic operations (+, -, *, /)
- **Strings**: Text data, concatenation with +
- **Loose Typing**: JavaScript tries to guess data types, but be explicit for reliability

##### Best Practice
Always specify data types explicitly:

```javascript
// Good - explicit typing
let price = Number("16725.45");
let message = String("Bitcoin price: ");

// Avoid - relying on JavaScript's guessing
let price = "16725.45"; // Might cause unexpected behavior
``` 

#### Data Structures

##### Arrays: Ordered Lists
Arrays store multiple values in a numbered list:

```javascript
// Creating an array
var fruits = [];
fruits.push(`lemons`);
fruits.push(`apples`);  
fruits.push(`oranges`);

console.log(fruits);        // Shows entire array
console.log(fruits[0]);     // "lemons" (first item)
console.log(fruits[1]);     // "apples" (second item)
```

**Key Points:**
- Arrays are indexed starting from 0
- Use `push()` to add items
- Access items with bracket notation: `array[index]`
- Perfect for lists of transactions, prices, etc.

##### Objects: Key-Value Pairs
Objects store data as key-value pairs:

```javascript
var fruits = {};
fruits[`yellow fruit`] = `lemon`;
fruits[`red fruit`] = `apple`;
fruits[`orange fruit`] = `orange`;

console.log(fruits);                    // Shows entire object
console.log(fruits[`red fruit`]);       // "apple"
```

**Key Points:**
- Objects use keys instead of numeric indexes
- Order is not guaranteed (browsers may reorder)
- Access values with bracket notation: `object[key]`
- Great for structured data like API responses

##### Arrays vs Objects
| Arrays | Objects |
|--------|---------|
| Ordered, indexed by numbers | Unordered, indexed by keys |
| `fruits[0]` | `fruits['red fruit']` |
| Order preserved | Order not guaranteed |
| Use for lists | Use for structured data |

#### Variables: Short Names for Values

Variables let you store and reuse values throughout your code:

```javascript
// Creating and updating a variable
var message = `This is a long piece of text`;
message = message + ` and I can make it even longer`;
message = message + ` and even stretch it out to ridiculous lengths`;
message = message + ` but manage it easily through JavaScript`;

console.log(message);
console.log(message + ` and that's the way it is`);
```

##### Variable Rules
- Use `var`, `let`, or `const` to declare variables
- Variable names should be descriptive
- Use `=` to assign values
- Variables can be updated by reassigning

##### Modern Variable Declaration
```javascript
// const - cannot be reassigned (recommended for values that don't change)
const API_URL = `https://api.coinbase.com/v2/prices/BTC-USD/spot`;

// let - can be reassigned (recommended for values that change)
let bitcoinPrice = 0;
let balance = 1000;

// var - older style (avoid in modern code)
var oldStyle = `avoid this`;
```

#### Functions: Reusable Code Blocks

Functions let you write code once and use it many times:

```javascript
// Basic function
function sayHello() {
    console.log(`Look ma, I'm using a function!`);
}

// Call the function
sayHello(); // Outputs: "Look ma, I'm using a function!"
```

##### Functions with Parameters
Parameters let you pass data into functions:

```javascript
function greetUser(name, age, location) {
    console.log(`Hello ${name}! You are ${age} years old and from ${location}.`);
}

// Call with different values
greetUser("Alice", 25, "New York");
greetUser("Bob", 30, "London");
```

##### Template Literals (Backticks)
Use backticks (\`) for string interpolation:

```javascript
// Good - template literals with ${}
function greetUser(name) {
    console.log(`Hello ${name}!`);
}

// Avoid - concatenation
function greetUser(name) {
    console.log("Hello " + name + "!");
}

// Why backticks are better:
// 1. No conflicts with apostrophes: "I'm a developer"
// 2. Easy variable insertion with ${}
// 3. Multi-line strings supported
```

#### Control Flow: If/Else Statements

If statements are the core of programming logic:

```javascript
// Basic if/else
if (1 == 1) {
    console.log("I am running option 1");
} else {
    console.log("I am running option 2");
}
```

##### Comparison Operators
```javascript
// Equality (double equals for comparison)
if (price == 50000) { /* Bitcoin hit $50k! */ }

// AND operator (&&)
if (balance > 1000 && price < 20000) {
    console.log("Good time to buy!");
}

// OR operator (||)  
if (balance == 0 || price > 100000) {
    console.log("Either broke or Bitcoin mooned!");
}

// NOT operator (!)
if (!userLoggedIn) {
    console.log("Please log in");
}
```

##### Real-World Example
```javascript
function checkWalletStatus(balance, price) {
    if (balance > 1000 && price < 30000) {
        console.log("Great time to stack sats!");
    } else if (balance == 0) {
        console.log("Time to buy some Bitcoin!");
    } else {
        console.log("HODL strong!");
    }
}
``` 

### Asynchronous Programming and APIs

#### Getting Data from the Internet

Modern web applications need to fetch data from external services. Here's our versatile `getData` function:

```javascript
function getData(url, apikey, content_type) {
    return new Promise(function(resolve, reject) {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && (this.status >= 200 && this.status < 300)) {
                resolve(xhttp.responseText);
            }
        }
        xhttp.open(`GET`, url, true);
        if (apikey) {
            xhttp.setRequestHeader(`X-Api-Key`, apikey);
        }
        if (content_type) {
            xhttp.setRequestHeader(`Content-Type`, content_type);
        }
        xhttp.send();
    });
}
```

#### Understanding Promises

When you request data from the internet, JavaScript returns a **Promise** - a container that will eventually hold your data:

```javascript
// This returns a Promise immediately
let dataPromise = getData(`https://api.coinbase.com/v2/prices/BTC-USD/spot`);
console.log(dataPromise); // Shows: Promise {<pending>}

// The Promise will resolve when data arrives
// Click to see: Promise {<fulfilled>: "...data..."}
```

#### Async/Await: Making Promises Easy

Instead of dealing with complex Promise syntax, use `async/await`:

```javascript
// Without await (confusing)
function getBitcoinPrice() {
    var data = getData(`https://api.coinbase.com/v2/prices/BTC-USD/spot`);
    console.log(data); // Promise object, not the actual data!
}

// With await (clear and simple)
async function getBitcoinPrice() {
    var data = await getData(`https://api.coinbase.com/v2/prices/BTC-USD/spot`);
    console.log(data); // Actual data!
}
```

##### Why JavaScript Doesn't Wait by Default

JavaScript is designed for speed. It fires off requests and immediately continues to the next line:

```javascript
function demonstrateAsyncBehavior() {
    console.log("First: Starting request");
    var data = getData("https://api.example.com/data");
    console.log("Second: This runs immediately");
    console.log("Third: Data isn't ready yet:", data);
}
```

Output:
```
First: Starting request
Second: This runs immediately  
Third: Data isn't ready yet: Promise {<pending>}
```

##### Async/Await Fixes This

```javascript
async function demonstrateAsyncBehavior() {
    console.log("First: Starting request");
    var data = await getData("https://api.example.com/data");
    console.log("Second: Data is ready:", data);
    console.log("Third: This runs after data arrives");
}
```

#### Working with JSON Data

##### What is JSON?
JSON (JavaScript Object Notation) is how computers exchange data on the web. It looks like JavaScript objects:

```json
{
    "data": {
        "base": "BTC",
        "currency": "USD", 
        "amount": "16725.45"
    }
}
```

##### Parsing JSON Responses

Raw API responses are strings. Convert them to JavaScript objects with `JSON.parse()`:

```javascript
async function getBitcoinPrice() {
    // Get raw string data
    var rawData = await getData(`https://api.coinbase.com/v2/prices/BTC-USD/spot`);
    console.log(typeof rawData); // "string"
    
    // Parse into JavaScript object
    var jsonData = JSON.parse(rawData);
    console.log(typeof jsonData); // "object"
    
    // Access nested data
    var price = jsonData.data.amount;
    console.log(`Bitcoin price: $${price}`);
}
```

##### Working with Arrays of Objects

Many APIs return arrays of objects. Here's how to work with them:

```javascript
async function getComments() {
    var data = await getData(`https://jsonplaceholder.typicode.com/posts/1/comments`);
    var comments = JSON.parse(data);
    
    console.log(comments);           // Array of comment objects
    console.log(comments[0]);        // First comment object
    console.log(comments[0].email);  // Email from first comment
    
    // Loop through all comments
    comments.forEach(function(comment) {
        console.log(`${comment.name}: ${comment.body}`);
    });
}
```

#### Best Practices for Async Functions

##### Always Use Async for Network Calls
```javascript
// Good - async function
async function fetchData() {
    const result = await getData("https://api.example.com/data");
    return result;
}

// Avoid - mixing sync and async
function fetchData() {
    return getData("https://api.example.com/data"); // Returns Promise, not data
}
```

##### Error Handling
```javascript
async function safeFetchData() {
    try {
        const data = await getData("https://api.example.com/data");
        return JSON.parse(data);
    } catch (error) {
        console.error("Failed to fetch data:", error);
        return null;
    }
}
```

## Mastering the DOM in a Functional Pleb Wallet
<chapterId>850c6fb1-a5d0-4864-ae60-f40246cc26b3</chapterId>

### DOM Manipulation: Updating Web Pages

#### What is the DOM?
The DOM (Document Object Model) represents your HTML as a JavaScript object. Every HTML element becomes a JavaScript object you can modify.

#### Query Selectors: Finding Elements

First, set up easy-to-use query functions:

```javascript
// Shorthand for document.querySelector and document.querySelectorAll
var $ = document.querySelector.bind(document);
var $$ = document.querySelectorAll.bind(document);
```

Now you can easily find and modify elements:

```javascript
// Find single elements
var header = $(`h1`);                    // First h1 element
var balanceCard = $(`.balance-card`);     // First element with class "balance-card"
var priceDisplay = $(`#price-display`);  // Element with ID "price-display"

// Find multiple elements  
var allCards = $$(`.balance-card`);       // All elements with class "balance-card"
var allParagraphs = $$(`p`);             // All paragraph elements
```

#### Updating Content

##### Changing Text Content
```javascript
// Update the Bitcoin price display
$(`.balance-card p`).innerHTML = `$16,725.45`;

// Update multiple elements
$$(`.balance-card p`)[0].innerHTML = `100 sats`;  // First balance card
$$(`.balance-card p`)[1].innerHTML = `$16,725`;   // Second balance card
```

##### Adding New Content
```javascript
// Add a new transaction to the list
var transactionList = $(`.row-item`);
transactionList.innerHTML += `
    <p class="transaction">Received payment</p>
    <p class="transaction-amount">+50 sats</p>
`;
```

#### Practical Example: Live Price Updates

```javascript
async function updateBitcoinPrice() {
    try {
        // Fetch current price
        var data = await getData(`https://api.coinbase.com/v2/prices/BTC-USD/spot`);
        var json = JSON.parse(data);
        var price = Number(json.data.amount);
        
        // Format with commas
        var formattedPrice = price.toLocaleString();
        
        // Update the display
        $$(`.balance-card p`)[1].innerHTML = `$${formattedPrice}`;
        
        console.log(`Updated Bitcoin price: $${formattedPrice}`);
    } catch (error) {
        console.error(`Failed to update price:`, error);
    }
}

// Update price immediately and then every 10 seconds
updateBitcoinPrice();
setInterval(updateBitcoinPrice, 10000);
``` 



### Building the Pleb Wallet Project

#### Project Overview
We'll transform the static wallet from lesson 2 into a fully functional Bitcoin Lightning wallet that:
- Displays real-time Bitcoin prices from Coinbase
- Shows actual wallet balance from LNbits
- Lists real transactions
- Allows sending and receiving Bitcoin payments
- Updates automatically every 10 seconds

#### Step 1: Project Setup

##### Download the CSS Wallet
Clone Austin's wallet project from lesson 2:

```bash
git clone https://github.com/AustinKelsay/learn-css
cd learn-css
```

##### Open in Browser and Editor
1. Open `index.html` in your web browser
2. Open the project folder in your text editor
3. You should see the static wallet with fake data

#### Step 2: Adding JavaScript to HTML

JavaScript goes inside `<script>` tags. Add this before the closing `</body>` tag:

```html
<footer>
    <p>Made by plebs, for plebs.</p>
</footer>

<!-- Add JavaScript here -->
<script>
    console.log(`test`);
</script>
</body>
</html>
```

**Test it works:**
1. Save the file
2. Refresh your browser
3. Open Developer Tools → Console
4. You should see "test" logged

#### Step 3: Set Up DOM Manipulation

Replace the test script with our query selectors:

```html
<script>
    // Easy DOM manipulation
    var $ = document.querySelector.bind(document);
    var $$ = document.querySelectorAll.bind(document);
    
    // Test updating the price
    $$('.balance-card p')[1].innerHTML = 'Testing...';
</script>
```

You should see the price change from "$19,364" to "Testing..."

#### Step 4: Add the getData Function

Add our HTTP request function:

```html
<script>
    function getData(url, apikey, content_type) {
        return new Promise(function(resolve, reject) {
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && (this.status >= 200 && this.status < 300)) {
                    resolve(xhttp.responseText);
                }
            }
            xhttp.open(`GET`, url, true);
            if (apikey) {
                xhttp.setRequestHeader(`X-Api-Key`, apikey);
            }
            if (content_type) {
                xhttp.setRequestHeader(`Content-Type`, content_type);
            }
            xhttp.send();
        });
    }
</script>
```

#### Step 5: Real Bitcoin Prices

Create a function to fetch Bitcoin prices from Coinbase:

```html
<script>
    async function getBitcoinPrice() {
        var data = await getData(`https://api.coinbase.com/v2/prices/BTC-USD/spot`);
        var json = JSON.parse(data);
        var price = json.data.amount;
        return price;
    }
</script>
```

#### Step 6: Update the Display

Create the main app function that updates our wallet:

```html
<script>
    var $ = document.querySelector.bind(document);
    var $$ = document.querySelectorAll.bind(document);
    
    async function app() {
        // Get Bitcoin price
        var price = await getBitcoinPrice();
        var formattedPrice = Number(price).toLocaleString();
        
        // Update the display
        $$('.balance-card p')[1].innerHTML = `$${formattedPrice}`;
        
        // Update again in 10 seconds
        setTimeout(function() {
            app();
        }, 10000);
    }
    
    // Start the app
    app();
</script>
```

**Important:** Put this script **after** the getBitcoinPrice function, or move all scripts to the bottom of the page.

#### Step 7: Setting Up LNbits Wallet

##### Create an LNbits Wallet
1. Go to [demo.lnbits.com](https://demo.lnbits.com) (updated from legend.lnbits.com)
2. Click "Create new wallet"
3. Give it a name like "Pleb Wallet"
4. Save your wallet - you now have a Bitcoin Lightning wallet!

##### Get Your API Keys
In your LNbits wallet:
1. Click on "API docs"
2. Copy your **Admin key** (the longer one)
3. This key lets your JavaScript app access your wallet

##### Understanding the API
LNbits provides several endpoints:
- `/api/v1/wallet` - Get wallet balance
- `/api/v1/payments` - Get transaction list
- We'll use GET requests to read data

#### Step 8: Add LNbits Integration

##### Wallet Balance Function
```html
<script>
    async function getLnbitsBalance() {
        var apiKey = 'YOUR_ADMIN_KEY_HERE'; // Replace with your actual key
        var data = await getData(
            'https://demo.lnbits.com/api/v1/wallet', 
            apiKey
        );
        var json = JSON.parse(data);
        var balance = Number(json.balance) / 1000; // Convert millisats to sats
        return balance;
    }
</script>
```

##### Transactions Function
```html
<script>
    async function getLnbitsTransactions() {
        var apiKey = 'YOUR_ADMIN_KEY_HERE'; // Replace with your actual key
        var data = await getData(
            'https://demo.lnbits.com/api/v1/payments', 
            apiKey, 
            'application/json'
        );
        var json = JSON.parse(data);
        return json;
    }
</script>
```

#### Step 9: Complete Wallet App

Update your main app function to handle everything:

```html
<script>
    async function app() {
        try {
            // Update Bitcoin price
            var price = await getBitcoinPrice();
            var formattedPrice = Number(price).toLocaleString();
            $$('.balance-card p')[1].innerHTML = `$${formattedPrice}`;
            
            // Update wallet balance
            var balance = await getLnbitsBalance();
            $$('.balance-card p')[0].innerHTML = `${balance} sats`;
            
            // Update transactions
            var transactions = await getLnbitsTransactions();
            updateTransactionsList(transactions);
            
        } catch (error) {
            console.error('App update failed:', error);
        }
        
        // Update again in 10 seconds
        setTimeout(function() {
            app();
        }, 10000);
    }
    
    function updateTransactionsList(transactions) {
        var transactionContainer = $('.row-item');
        
        // Reset transactions list but keep header
        transactionContainer.innerHTML = '<h3>Transactions</h3>';
        
        transactions.forEach(function(tx) {
            var amount = Math.floor(Number(tx.amount) / 1000); // Convert to sats
            
            // Only show completed transactions
            if (!tx.pending) {
                if (amount > 0) {
                    // Incoming payment
                    transactionContainer.innerHTML += `
                        <p class="transaction" data-checking-id="${tx.checking_id}">
                            Received with ${tx.bolt11.substring(0, 25)}...
                        </p>
                        <p class="transaction-amount">+${amount} sats</p>
                    `;
                } else if (amount < 0 && tx.preimage !== "0000000000000000000000000000000000000000000000000000000000000000") {
                    // Outgoing payment (only if actually paid)
                    transactionContainer.innerHTML += `
                        <p class="transaction" data-checking-id="${tx.checking_id}">
                            Sent with ${tx.bolt11.substring(0, 25)}...
                        </p>
                        <p class="transaction-amount">${amount} sats</p>
                    `;
                }
            }
        });
    }
    
    // Start the app
    app();
</script>
```

#### Step 10: Add Send/Receive Functionality

##### Create Input Forms
Add these divs after your buttons in the HTML:

```html
<div class="buttons">
    <button>Send</button>
    <button>Receive</button>
</div>

<!-- Add these new divs -->
<div style="background-color: white; padding: 20px; display: none;" align="center" class="paste_invoice">
    <p style="font-family: Helvetica, sans-serif; font-size: 1.25em;">Paste an invoice</p>
    <p><input class="invoice_to_pay" style="font-size: 1.15em;"></p>
    <p><button type="button" onclick="submitInvoiceToPay($('.invoice_to_pay').value)" style="font-size: 1.15em;">Submit</button></p>
</div>

<div style="background-color: white; padding: 20px; display: none;" align="center" class="create_invoice">
    <p style="font-family: Helvetica, sans-serif; font-size: 1.25em;">Enter an amount</p>
    <p><input class="amount_of_new_invoice" style="font-size: 1.15em;"></p>
    <p><button type="button" onclick="getInvoice($('.amount_of_new_invoice').value)" style="font-size: 1.15em;">Submit</button></p>
</div>
```

##### Button Click Handlers
```html
<script>
    // Send button functionality
    $$('button')[0].onclick = function() {
        var pasteDiv = $('.paste_invoice');
        if (pasteDiv.style.display !== 'block') {
            pasteDiv.style.display = 'block';
        } else {
            pasteDiv.style.display = 'none';
        }
        $('.invoice_to_pay').value = '';
    }
    
    // Receive button functionality
    $$('button')[1].onclick = function() {
        var createDiv = $('.create_invoice');
        if (createDiv.style.display !== 'block') {
            createDiv.style.display = 'block';
        } else {
            createDiv.style.display = 'none';
        }
        $('.amount_of_new_invoice').value = '';
    }
</script>
```

##### POST Function for Sending Data
```html
<script>
    function postJson(url, apikey, content_type, json) {
        return new Promise(function(resolve, reject) {
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && (this.status >= 200 && this.status < 300)) {
                    resolve(xhttp.responseText);
                }
            }
            xhttp.open('POST', url, true);
            if (apikey) {
                xhttp.setRequestHeader('X-Api-Key', apikey);
            }
            if (content_type) {
                xhttp.setRequestHeader('Content-Type', content_type);
            }
            xhttp.send(json);
        });
    }
</script>
```

##### Invoice Creation Function
```html
<script>
    async function getInvoice(amount) {
        var apiKey = 'YOUR_ADMIN_KEY_HERE'; // Replace with your key
        
        var requestData = {
            out: false,
            amount: amount,
            memo: "LNBits"
        };
        
        var response = await postJson(
            'https://demo.lnbits.com/api/v1/payments',
            apiKey,
            'application/json',
            JSON.stringify(requestData)
        );
        
        var responseData = JSON.parse(response);
        $('.create_invoice').innerHTML += responseData.payment_request;
    }
</script>
```

##### Payment Function
```html
<script>
    async function submitInvoiceToPay(invoice) {
        if (!confirm(`Are you sure you want to pay this invoice? ${invoice}`)) {
            return;
        }
        
        var apiKey = 'YOUR_ADMIN_KEY_HERE'; // Replace with your key
        
        var requestData = {
            out: true,
            bolt11: invoice
        };
        
        var response = await postJson(
            'https://demo.lnbits.com/api/v1/payments',
            apiKey,
            'application/json',
            JSON.stringify(requestData)
        );
        
        var responseData = JSON.parse(response);
        $('.paste_invoice').innerHTML += JSON.stringify(responseData);
    }
</script>
```

#### Step 11: Testing Your Wallet

##### Test Receiving
1. Click "Receive"
2. Enter an amount (like 10)
3. Click "Submit"
4. You'll get a Lightning invoice
5. Pay it with a Lightning wallet app
6. Watch your balance update!

##### Test Sending
1. Create an invoice in another Lightning wallet
2. Click "Send" in your web wallet
3. Paste the invoice
4. Click "Submit"
5. Confirm the payment
6. Watch the transaction appear!

#### Understanding Lightning Network Basics

##### Millisatoshis vs Satoshis
- Lightning Network uses **millisatoshis** (1/1000 of a satoshi)
- We convert to satoshis for display: `amount / 1000`
- This allows for more precise micropayments

##### Preimages and Payment Proofs
- Lightning payments use cryptographic proofs called **preimages**
- A preimage of all zeros means the payment failed
- Non-zero preimages prove the payment was completed
- This is how we determine if outgoing payments succeeded

##### Invoice Format
Lightning invoices (bolt11) contain:
- Payment amount
- Destination
- Payment hash
- Expiry time
- Description

#### Common Issues and Solutions

##### CORS Errors
If you get CORS errors, LNbits might be blocking requests:
- Use the demo server: demo.lnbits.com
- Some browsers are more restrictive than others
- Try Firefox or Chrome

##### API Key Issues
- Make sure you're using the **Admin** key, not the Invoice key
- Copy the entire key without extra spaces
- Replace 'YOUR_ADMIN_KEY_HERE' with your actual key

##### Function Order
JavaScript functions must be defined before they're called:
```html
<!-- Define first -->
<script>
    function getData() { /* ... */ }
</script>

<!-- Use second -->
<script>
    async function app() {
        var data = await getData(); // This works
    }
</script>
``` 

### Advanced JavaScript Techniques

#### Array Methods for Processing Data

Lightning wallets often work with arrays of transactions. Here are essential array methods:

```javascript
// Filter transactions by type
var incomingTxs = transactions.filter(function(tx) {
    return Number(tx.amount) > 0;
});

var outgoingTxs = transactions.filter(function(tx) {
    return Number(tx.amount) < 0;
});

// Transform data with map
var transactionAmounts = transactions.map(function(tx) {
    return Math.floor(Number(tx.amount) / 1000); // Convert to sats
});

// Sum all transaction amounts
var totalAmount = transactionAmounts.reduce(function(sum, amount) {
    return sum + amount;
}, 0);

// Find specific transactions
var largeTx = transactions.find(function(tx) {
    return Math.abs(Number(tx.amount)) > 100000; // Over 100 sats
});
```

#### Error Handling Best Practices

Always handle potential errors when working with APIs:

```javascript
async function safeGetBitcoinPrice() {
    try {
        var data = await getData(`https://api.coinbase.com/v2/prices/BTC-USD/spot`);
        var json = JSON.parse(data);
        
        if (json && json.data && json.data.amount) {
            return Number(json.data.amount);
        } else {
            throw new Error('Invalid price data received');
        }
    } catch (error) {
        console.error('Failed to get Bitcoin price:', error);
        return 0; // Default fallback value
    }
}
```

#### Performance Optimization

##### Debouncing API Calls
Avoid overwhelming APIs with too many requests:

```javascript
var updateTimeout;

function scheduleUpdate() {
    // Cancel previous update if still pending
    if (updateTimeout) {
        clearTimeout(updateTimeout);
    }
    
    // Schedule new update
    updateTimeout = setTimeout(function() {
        app();
    }, 10000);
}
```

##### Efficient DOM Updates
Batch DOM changes to improve performance:

```javascript
function updateTransactionsList(transactions) {
    var html = '<h3>Transactions</h3>';
    
    // Build HTML string first
    transactions.forEach(function(tx) {
        if (!tx.pending) {
            var amount = Math.floor(Number(tx.amount) / 1000);
            html += `<p class="transaction">${tx.description}</p>`;
            html += `<p class="transaction-amount">${amount} sats</p>`;
        }
    });
    
    // Single DOM update
    $('.row-item').innerHTML = html;
}
```

### Practice & Resources of Javascript

#### Exercise 1: Enhanced Price Display
Extend the Bitcoin price functionality:

1. **Add Price Change Indicator**
   ```javascript
   var previousPrice = 0;
   
   async function updatePriceWithIndicator() {
       var currentPrice = await getBitcoinPrice();
       var priceElement = $$('.balance-card p')[1];
       
       if (currentPrice > previousPrice) {
           priceElement.style.color = 'green';
           priceElement.innerHTML = `$${currentPrice.toLocaleString()} ↗`;
       } else if (currentPrice < previousPrice) {
           priceElement.style.color = 'red';
           priceElement.innerHTML = `$${currentPrice.toLocaleString()} ↘`;
       }
       
       previousPrice = currentPrice;
   }
   ```

2. **Add Multiple Currencies**
   - Fetch EUR and GBP prices
   - Display all three currencies
   - Let users switch between them

3. **Price History Graph**
   - Store last 10 price updates
   - Display a simple ASCII graph
   - Use local storage to persist data

#### Exercise 2: Transaction Analytics
Add analytics to your wallet:

1. **Transaction Summary**
   ```javascript
   function calculateTransactionStats(transactions) {
       var stats = {
           totalReceived: 0,
           totalSent: 0,
           transactionCount: 0,
           averageAmount: 0
       };
       
       transactions.forEach(function(tx) {
           if (!tx.pending) {
               var amount = Math.floor(Number(tx.amount) / 1000);
               if (amount > 0) {
                   stats.totalReceived += amount;
               } else {
                   stats.totalSent += Math.abs(amount);
               }
               stats.transactionCount++;
           }
       });
       
       stats.averageAmount = stats.transactionCount > 0 ? 
           (stats.totalReceived + stats.totalSent) / stats.transactionCount : 0;
       
       return stats;
   }
   ```

2. **Transaction Filtering**
   - Add buttons to filter by sent/received
   - Add date range filters
   - Search transactions by amount

3. **Export Functionality**
   - Export transactions as CSV
   - Generate transaction reports
   - Create backup of wallet data

#### Exercise 3: User Experience Improvements

1. **Loading States**
   ```javascript
   function showLoading(message) {
       $('.loading-indicator').innerHTML = message || 'Loading...';
       $('.loading-indicator').style.display = 'block';
   }
   
   function hideLoading() {
       $('.loading-indicator').style.display = 'none';
   }
   ```

2. **Notifications System**
   - Show success/error messages
   - Auto-hide notifications after 3 seconds
   - Different styles for different message types

3. **Responsive Improvements**
   - Make forms work better on mobile
   - Add touch-friendly buttons
   - Optimize for different screen sizes

#### Exercise 4: Security Enhancements

1. **Input Validation**
   ```javascript
   function validateAmount(amount) {
       var num = Number(amount);
       if (isNaN(num) || num <= 0) {
           throw new Error('Amount must be a positive number');
       }
       if (num > 1000000) {
           throw new Error('Amount too large');
       }
       return num;
   }
   ```

2. **API Key Management**
   - Store API keys securely
   - Add key validation
   - Handle expired keys gracefully

3. **Rate Limiting**
   - Limit API calls per minute
   - Show user when rate limited
   - Queue requests during high traffic

#### Learning Resources

**Essential JavaScript References**
- **[MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)** - Comprehensive official documentation
- **[W3Schools JavaScript Tutorial](https://www.w3schools.com/js/)** - Beginner-friendly tutorials with examples
- **[JavaScript.info](https://javascript.info/)** - Modern JavaScript tutorial
- **[Can I Use](https://caniuse.com/)** - Check browser compatibility

**API and Async Programming**
- **[Promises and Async/Await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises)** - Deep dive into asynchronous JavaScript
- **[Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)** - Modern alternative to XMLHttpRequest
- **[JSON Working Group](https://www.json.org/)** - Official JSON specification

**Bitcoin and Lightning Development**
- **[LNbits Documentation](https://lnbits.com/)** - Complete LNbits API reference
- **[Lightning Network Basics](https://github.com/lightningnetwork/lnd/blob/master/docs/INSTALL.md)** - Understanding Lightning Network
- **[Bitcoin Developer Guide](https://developer.bitcoin.org/)** - Official Bitcoin development resources
- **[Lightning Address](https://lightningaddress.com/)** - Human-readable Lightning addresses

**DOM Manipulation and Web APIs**
- **[DOM Manipulation Guide](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)** - Complete DOM reference
- **[Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)** - Local and session storage
- **[Progressive Web Apps](https://web.dev/progressive-web-apps/)** - Making web apps feel native

**Advanced JavaScript**
- **[Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)** - Complete array method reference
- **[JavaScript Modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)** - Organizing code into modules
- **[Error Handling](https://javascript.info/try-catch)** - Comprehensive error handling guide

### Debugging and Troubleshooting

#### Browser Developer Tools

##### Console Tab
- **View errors and warnings** - Red errors, yellow warnings
- **Test code snippets** - Run JavaScript directly in console
- **Monitor network requests** - See all API calls
- **Debug variables** - Type variable names to see their values

##### Network Tab
- **Monitor API calls** - See all requests to external services
- **Check response data** - Verify API responses are correct
- **Identify slow requests** - Find performance bottlenecks
- **Debug CORS issues** - See cross-origin request problems

##### Elements Tab
- **Inspect HTML structure** - See generated DOM
- **Modify CSS live** - Test styling changes
- **View element properties** - Check classes, IDs, attributes

#### Common JavaScript Errors

##### ReferenceError: function is not defined
```javascript
// Problem: Function called before definition
app(); // Error: app is not defined

function app() {
    console.log("Hello");
}

// Solution: Define functions first, call them after
function app() {
    console.log("Hello");
}
app(); // Works!
```

##### TypeError: Cannot read property of undefined
```javascript
// Problem: Accessing property on undefined object
var json = JSON.parse(data);
console.log(json.data.amount); // Error if json.data is undefined

// Solution: Check if objects exist
if (json && json.data && json.data.amount) {
    console.log(json.data.amount);
}
```

##### SyntaxError: Unexpected token
```javascript
// Problem: Missing quotes, brackets, or semicolons
var message = Hello World; // Error: missing quotes

// Solution: Check syntax carefully
var message = "Hello World"; // Correct
```

#### API-Related Issues

##### CORS (Cross-Origin Resource Sharing) Errors
```
Access to XMLHttpRequest at 'https://api.example.com' from origin 'file://' has been blocked by CORS policy
```

**Solutions:**
- Use APIs that support CORS (like Coinbase)
- Use LNbits demo server instead of local instances
- Serve your HTML from a web server instead of opening files directly

##### API Key Issues
```
Error 401: Unauthorized
```

**Solutions:**
- Verify you're using the Admin key, not the Invoice key
- Check for extra spaces when copying keys
- Ensure key hasn't expired or been revoked

##### Rate Limiting
```
Error 429: Too Many Requests
```

**Solutions:**
- Increase interval between requests
- Implement exponential backoff
- Cache responses when possible

#### Performance Issues

##### Slow API Responses
- Check Network tab for slow requests
- Implement loading indicators
- Add timeout handling
- Cache frequently requested data

##### Memory Leaks
```javascript
// Problem: Creating intervals without clearing them
setInterval(function() {
    updatePrice();
}, 1000);

// Solution: Store reference and clear when needed
var priceInterval = setInterval(function() {
    updatePrice();
}, 1000);

// Clear when page unloads
window.addEventListener('beforeunload', function() {
    clearInterval(priceInterval);
});
```

### Best Practices Summary

#### Code Organization
1. **Functions first, calls second** - Define all functions before calling them
2. **One function, one purpose** - Keep functions focused and small
3. **Use descriptive names** - `getBitcoinPrice()` not `getPrice()`
4. **Comment complex logic** - Explain why, not what

#### Error Handling
1. **Always use try/catch with async functions**
2. **Provide fallback values** - Don't let errors break the app
3. **Log errors for debugging** - Use `console.error()`
4. **Show user-friendly error messages**

#### Performance
1. **Minimize DOM manipulation** - Batch updates when possible
2. **Cache API responses** - Don't fetch same data repeatedly
3. **Use appropriate intervals** - 10 seconds for prices, not 1 second
4. **Clean up resources** - Clear intervals and timeouts

#### Security
1. **Validate all user input** - Check amounts, formats, lengths
2. **Use HTTPS APIs only** - Never send sensitive data over HTTP
3. **Keep API keys secure** - Don't expose in client-side code in production
4. **Handle expired sessions** - Gracefully handle auth failures

#### Next Steps

**Immediate Actions**
1. **Complete the full wallet** with send/receive functionality
2. **Test with real Lightning payments** using small amounts
3. **Add error handling** to all API calls
4. **Implement loading states** for better UX

**Prepare for Advanced Topics**
In future lessons, you'll learn:
- **React** - Building more complex UIs with components
- **State management** - Managing application data efficiently
- **Modern JavaScript** - ES6+ features and modules
- **Build tools** - Webpack, npm, and development workflows
- **Testing** - Writing tests for your JavaScript code

**Building Your Portfolio**
- **Enhance the wallet** with additional features
- **Create new Bitcoin tools** - Price trackers, converters, etc.
- **Contribute to open source** - Help improve LNbits or other projects
- **Share your work** - Deploy to GitHub Pages or Vercel

#### Key Takeaways

1. **JavaScript is essential** - The only language that runs in browsers
2. **Async/await simplifies promises** - Use it for all API calls
3. **DOM manipulation enables interactivity** - Update pages without refreshing
4. **APIs connect your app to the world** - Fetch real data from services
5. **Error handling is crucial** - Always expect and handle failures
6. **Practice builds understanding** - Build projects to solidify knowledge
7. **Bitcoin development is accessible** - You can build Lightning apps today
8. **User experience matters** - Loading states and error messages improve apps

#### Complete Pleb Wallet Code

#### HTML (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Pleb Wallet</title>
    <link rel="stylesheet" href="index.css">
</head>
<body>
    <header>
        <h1>Pleb Wallet</h1>
    </header>
    
    <main>
        <div class="buttons">
            <button>Send</button>
            <button>Receive</button>
        </div>
        
        <div style="background-color: white; padding: 20px; display: none;" align="center" class="paste_invoice">
            <p style="font-family: Helvetica, sans-serif; font-size: 1.25em;">Paste an invoice</p>
            <p><input class="invoice_to_pay" style="font-size: 1.15em;"></p>
            <p><button type="button" onclick="submitInvoiceToPay($('.invoice_to_pay').value)" style="font-size: 1.15em;">Submit</button></p>
        </div>
        
        <div style="background-color: white; padding: 20px; display: none;" align="center" class="create_invoice">
            <p style="font-family: Helvetica, sans-serif; font-size: 1.25em;">Enter an amount</p>
            <p><input class="amount_of_new_invoice" style="font-size: 1.15em;"></p>
            <p><button type="button" onclick="getInvoice($('.amount_of_new_invoice').value)" style="font-size: 1.15em;">Submit</button></p>
        </div>
        
        <div class="row">
            <div class="balance-card">
                <h2>Balance</h2>
                <p>0 sats</p>
            </div>
            <div class="balance-card">
                <h2>Price</h2>
                <p>Loading...</p>
            </div>
        </div>
        
        <div class="row">
            <div class="row-item">
                <h3>Transactions</h3>
            </div>
            <div class="row-item">
                <img src="./BTCUSD.png" alt="Bitcoin Price Chart" />
            </div>
        </div>
    </main>
    
    <footer>
        <p>Made by plebs, for plebs.</p>
    </footer>

    <!-- JavaScript -->
    <script>
        // HTTP request functions
        function getData(url, apikey, content_type) {
            return new Promise(function(resolve, reject) {
                var xhttp = new XMLHttpRequest();
                xhttp.onreadystatechange = function() {
                    if (this.readyState == 4 && (this.status >= 200 && this.status < 300)) {
                        resolve(xhttp.responseText);
                    }
                }
                xhttp.open("GET", url, true);
                if (apikey) {
                    xhttp.setRequestHeader("X-Api-Key", apikey);
                }
                if (content_type) {
                    xhttp.setRequestHeader("Content-Type", content_type);
                }
                xhttp.send();
            });
        }

        function postJson(url, apikey, content_type, json) {
            return new Promise(function(resolve, reject) {
                var xhttp = new XMLHttpRequest();
                xhttp.onreadystatechange = function() {
                    if (this.readyState == 4 && (this.status >= 200 && this.status < 300)) {
                        resolve(xhttp.responseText);
                    }
                }
                xhttp.open("POST", url, true);
                if (apikey) {
                    xhttp.setRequestHeader("X-Api-Key", apikey);
                }
                if (content_type) {
                    xhttp.setRequestHeader("Content-Type", content_type);
                }
                xhttp.send(json);
            });
        }
    </script>

    <script>
        // API functions
        async function getBitcoinPrice() {
            var data = await getData("https://api.coinbase.com/v2/prices/BTC-USD/spot");
            var json = JSON.parse(data);
            var price = json.data.amount;
            return price;
        }

        async function getLnbitsBalance() {
            var apiKey = "YOUR_ADMIN_KEY_HERE"; // Replace with your actual key
            var data = await getData("https://demo.lnbits.com/api/v1/wallet", apiKey);
            var json = JSON.parse(data);
            var balance = Number(json.balance) / 1000;
            return balance;
        }

        async function getLnbitsTransactions() {
            var apiKey = "YOUR_ADMIN_KEY_HERE"; // Replace with your actual key
            var data = await getData("https://demo.lnbits.com/api/v1/payments", apiKey, "application/json");
            var json = JSON.parse(data);
            return json;
        }
    </script>

    <script>
        // DOM manipulation and main app
        var $ = document.querySelector.bind(document);
        var $$ = document.querySelectorAll.bind(document);

        async function app() {
            try {
                // Update balance
                var balance = await getLnbitsBalance();
                $$('.balance-card p')[0].innerHTML = balance + ' sats';

                // Update price
                var price = await getBitcoinPrice();
                var formattedPrice = Number(price).toLocaleString();
                $$('.balance-card p')[1].innerHTML = '$' + formattedPrice;

                // Update transactions
                var transactions = await getLnbitsTransactions();
                $('.row-item').innerHTML = '<h3>Transactions</h3>';
                
                transactions.forEach(function(tx) {
                    var amount = Math.floor(Number(tx.amount) / 1000);
                    
                    if (amount > 0 && !tx.pending) {
                        $('.row-item').innerHTML += `
                            <p class="transaction" data-checking-id="${tx.checking_id}">
                                Received with ${tx.bolt11.substring(0, 25)}...
                            </p>
                            <p class="transaction-amount">+${amount} sats</p>
                        `;
                    }
                    
                    if (amount < 0 && tx.preimage !== "0000000000000000000000000000000000000000000000000000000000000000") {
                        $('.row-item').innerHTML += `
                            <p class="transaction" data-checking-id="${tx.checking_id}">
                                Sent with ${tx.bolt11.substring(0, 25)}...
                            </p>
                            <p class="transaction-amount">${amount} sats</p>
                        `;
                    }
                });

            } catch (error) {
                console.error('App update failed:', error);
            }

            setTimeout(function() { app(); }, 10000);
        }

        // Button handlers
        $$('button')[0].onclick = function() {
            var pasteDiv = $('.paste_invoice');
            pasteDiv.style.display = pasteDiv.style.display !== 'block' ? 'block' : 'none';
            $('.invoice_to_pay').value = '';
        }

        $$('button')[1].onclick = function() {
            var createDiv = $('.create_invoice');
            createDiv.style.display = createDiv.style.display !== 'block' ? 'block' : 'none';
            $('.amount_of_new_invoice').value = '';
        }

        // Payment functions
        async function submitInvoiceToPay(invoice) {
            if (!confirm(`Are you sure you want to pay this invoice? ${invoice}`)) return;
            
            var apiKey = "YOUR_ADMIN_KEY_HERE";
            var json = { out: true, bolt11: invoice };
            
            var response = await postJson(
                "https://demo.lnbits.com/api/v1/payments",
                apiKey,
                "application/json",
                JSON.stringify(json)
            );
            
            $('.paste_invoice').innerHTML += JSON.stringify(JSON.parse(response));
        }

        async function getInvoice(amount) {
            var apiKey = "YOUR_ADMIN_KEY_HERE";
            var json = { out: false, amount: amount, memo: "LNBits" };
            
            var response = await postJson(
                "https://demo.lnbits.com/api/v1/payments",
                apiKey,
                "application/json",
                JSON.stringify(json)
            );
            
            var responseData = JSON.parse(response);
            $('.create_invoice').innerHTML += responseData.payment_request;
        }

        // Start the app
        app();
    </script>
</body>
</html>
```

Remember to replace `"YOUR_ADMIN_KEY_HERE"` with your actual LNbits admin key!

Congratulations! You've built your first Bitcoin Lightning wallet with JavaScript. You now understand the fundamentals of web development and can create interactive Bitcoin applications. Keep building, keep learning, and welcome to the Bitcoin developer community! ⚡️🧡

---

#### What's Next?

In the next lesson, we'll dive into **React** - a powerful library that makes building complex user interfaces much easier. We'll refactor our wallet using modern development practices and add advanced features like:

- Component-based architecture
- State management
- Modern JavaScript (ES6+)
- Professional development workflow
- Deployment to production

The journey from here only gets more exciting! 🚀 

# Learn Development Environments: Setting Up Your Professional Workflow
<partId>5674be06-4861-408e-80ec-50182ce394a6</partId>

## The Local Ecosystem
<chapterId>dc9223b2-ac06-4288-a934-4a9846f146fc</chapterId>

### Why Development Environments Matter

Real developers don't just write code in isolation. They work within ecosystems of tools, services, and processes that enable:

- **Collaboration** - Multiple developers working on the same codebase
- **Version control** - Tracking changes, rolling back mistakes, branching features
- **Quality assurance** - Linting, testing, code review processes
- **Deployment** - Getting code from development to production seamlessly
- **Maintenance** - Updating dependencies, fixing bugs, adding features

#### Three Essential Environments
Modern development typically involves three key environments:

1. **Local Environment** - Your computer where you write and test code
2. **Remote Repository** - GitHub where code is stored and shared
3. **Production Environment** - Live servers where users access your application

Each serves a specific purpose and they work together to create a professional development workflow. 

### Installing Essential Tools: Node js, visual code and more 

##### Node.js: The JavaScript Runtime
Node.js allows JavaScript to run outside of browsers and provides the foundation for modern web development tools.

**Installation:**
1. Visit [nodejs.org](https://nodejs.org/en/download/)
2. Download the LTS (Long Term Support) version for your operating system
3. Run the installer with default settings
4. Verify installation by opening terminal/command prompt and running:
   ```bash
   node --version
   npm --version
   ```

**What Node.js Provides:**
- **Runtime environment** - Execute JavaScript outside browsers
- **npm (Node Package Manager)** - Install and manage code libraries
- **Build tools** - Compile, bundle, and optimize your code
- **Development servers** - Run your applications locally

##### Visual Studio Code: Your Code Editor
Visual Studio Code is a free, powerful code editor that's become the industry standard for web development.

**Installation:**
1. Visit [code.visualstudio.com](https://code.visualstudio.com/download)
2. Download for your operating system (Mac, Windows, Linux)
3. Install with default settings
4. Launch Visual Studio Code

**Adding VS Code to PATH (Command Line Access):**
This allows you to open VS Code from the terminal with the `code` command.

1. Open Visual Studio Code
2. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
3. Type "shell command" and select "Shell Command: Install 'code' command in PATH"
4. Follow the prompts to install

**Test it works:**
```bash
code --version
```

#### Essential Visual Studio Code Extensions

Extensions supercharge VS Code with additional functionality. Install these essential extensions:

##### ESLint - JavaScript Code Quality
**What it does:** Analyzes your JavaScript code and highlights errors, warnings, and style issues in real-time.

**Why you need it:**
- Catches syntax errors before you run your code
- Enforces consistent code style
- Provides live documentation for functions and methods
- Helps you learn JavaScript best practices

**Installation:**
1. Open VS Code Extensions panel (Ctrl+Shift+X)
2. Search for "ESLint"
3. Click Install on the official ESLint extension

##### Prettier - Code Formatter
**What it does:** Automatically formats your code to follow consistent style rules.

**Why you need it:**
- Consistent indentation and spacing
- Automatic formatting on save
- Reduces time spent on code formatting
- Makes code more readable and professional

**Installation:**
1. Search for "Prettier - Code formatter" in Extensions
2. Install the official Prettier extension
3. Configure to format on save:
   - Go to Settings (Cmd+, or Ctrl+,)
   - Search for "format on save"
   - Check the "Editor: Format On Save" option

#### Visual Studio Code Interface Overview

##### Key Areas
- **Explorer** (left sidebar) - File and folder navigation
- **Search** - Find and replace across your project
- **Source Control** - Git integration for version control
- **Extensions** - Install and manage extensions
- **Editor** - Where you write your code
- **Terminal** - Integrated command line
- **Problems** - View errors and warnings
- **Output** - See build results and logs

##### Essential Shortcuts
```
Cmd+P / Ctrl+P     - Quick file open
Cmd+Shift+P        - Command palette
Cmd+`             - Toggle terminal
Cmd+B             - Toggle sidebar
Cmd+S             - Save file
Cmd+Z             - Undo
Cmd+Shift+Z       - Redo
```

##### Integrated Terminal
The integrated terminal is one of VS Code's most powerful features:
- Access command line without leaving your editor
- Run build commands, start development servers
- Execute Git commands
- Install packages with npm

**Opening Terminal:**
- View → Terminal
- Or use shortcut: Ctrl+` (backtick)

#### Code Intelligence Features

##### IntelliSense
VS Code provides intelligent code completion:
- **Auto-completion** - Suggests functions, variables, and methods
- **Parameter hints** - Shows function parameters as you type
- **Type information** - Displays data types and documentation
- **Error highlighting** - Red squiggles under syntax errors

##### Live Documentation
Hover over functions to see:
- Function signatures
- Parameter descriptions
- Return types
- Usage examples

Example with console.log:
```javascript
console.log() // Hover to see: "(method) Console.log(...data: any[]): void"
```

### First Steps with Projects in Your Environment

##### Opening Projects 
Three ways to open projects in VS Code:
1. **File → Open Folder** - Browse and select your project folder
2. **Command line** - `code /path/to/your/project`
3. **Drag and drop** - Drag project folder onto VS Code icon

##### Project Structure
VS Code automatically recognizes project types:
- **package.json** - Identifies Node.js projects
- **.git folder** - Shows Git repository status
- **Language-specific files** - Enables appropriate extensions and features

#### Customizing Your Environment

##### Themes and Appearance
1. **Command Palette** → "Preferences: Color Theme"
2. Popular themes: Dark+, One Dark Pro, Dracula
3. Install additional themes from Extensions marketplace

##### Settings Sync
Sync your VS Code settings across devices:
1. Sign in with GitHub account
2. Enable Settings Sync
3. Your extensions, settings, and themes sync automatically

##### Workspace Settings
Configure settings per project by creating `.vscode/settings.json`:
```json
{
  "editor.tabSize": 2,
  "editor.insertSpaces": true,
  "editor.formatOnSave": true,
  "emmet.includeLanguages": {
    "javascript": "javascriptreact"
  }
}
``` 

## Version Control Basics (Git)
<chapterId>59aef5f2-0fe7-4008-83d3-752f22f4b609</chapterId>

### Git and GitHub: Version Control and Collaboration

##### Git: The Version Control System
Git is a **protocol** - a set of rules for tracking changes in code. Think of it as a sophisticated "Save" system that:
- **Tracks every change** made to your code
- **Enables collaboration** without conflicts
- **Allows experimentation** with branches
- **Provides backup and recovery** for your work
- **Shows detailed history** of who changed what when

Git was created in the early 2000s to solve the problem of multiple developers working on the same codebase. Without version control, this was chaos:
- Files getting overwritten
- No way to roll back changes
- Impossible to track who made what changes
- No way to experiment safely

##### GitHub: The Platform
GitHub is a **website and cloud service** built on top of Git. It provides:
- **Remote repositories** - Store your Git repositories in the cloud
- **Visual interface** - Web-based UI for Git operations
- **Collaboration tools** - Issues, pull requests, project management
- **Backup and sharing** - Your code is safe and accessible anywhere
- **Portfolio building** - Showcase your work and contributions

**Analogy:** If Git is the engine, GitHub is the car that makes it accessible and user-friendly.

#### Why Every Developer Uses GitHub

##### 1. Proof of Work
GitHub acts as your developer portfolio:
- **Green squares** show daily coding activity
- **Repositories** showcase your projects
- **Contribution history** proves consistent work
- **Employers look at GitHub** profiles when hiring

##### 2. Collaboration and Open Source
- **99% of professional developers** use Git/GitHub
- **All major projects** are on GitHub (Bitcoin, Linux, React, etc.)
- **Contributing to open source** builds reputation and skills
- **Learning from others** by reading real codebases

##### 3. Backup and Accessibility
- **Never lose your work** - everything is backed up in the cloud
- **Access from anywhere** - work on any computer
- **Share easily** - send links to your projects
- **Version history** - see how your code evolved

### Essential Git Terminology

Understanding these terms is crucial for working with Git and GitHub:

##### Repository (Repo)
A **folder that contains your code** and is tracked by Git. Think of it as a project folder with superpowers.
```bash
my-bitcoin-wallet/     # This is a repository
├── index.html
├── style.css
├── script.js
└── .git/             # Hidden folder that makes it a Git repo
```

##### Commit
A **saved snapshot** of your code at a specific point in time. Each commit has:
- **Unique ID** (hash) - like a fingerprint
- **Message** - description of what changed
- **Timestamp** - when it was made
- **Author** - who made the changes

```bash
## Example commit history
commit a1b2c3d "Add Bitcoin price display feature"
commit e4f5g6h "Fix wallet balance calculation bug"  
commit i7j8k9l "Initial project setup"
```

##### Staging
**Preparing commits** before they're saved. It's like putting items in a shopping cart before checkout:
- **Working directory** - files you're editing
- **Staging area** - files ready to be committed  
- **Repository** - committed files in Git history

##### Push
**Uploading your local commits** to GitHub (remote repository). Your changes go from your computer to the cloud.

##### Pull
**Downloading changes** from GitHub to your local machine. Get updates from the remote repository.

##### Branch
A **separate version** of your code where you can experiment without affecting the main version.
- **main/master branch** - the primary, stable version
- **feature branches** - experimental work
- **merge** - combining branches back together

##### Pull Request (PR)
A **request to merge** your branch into the main branch. It includes:
- **Description** of changes made
- **Code review** process
- **Discussion** between team members
- **Approval** before merging

##### Clone
**Downloading a complete copy** of a repository from GitHub to your computer.

##### Fork
**Creating your own copy** of someone else's repository. Useful for:
- Contributing to open source projects
- Experimenting with existing code
- Creating your own version of a project

### Installing and Configuring Git

##### Installation
**Mac:** Git comes pre-installed, but you can update it:
```bash
## Check if Git is installed
git --version

## Install via Homebrew (if you have it)
brew install git
```

**Windows:** Download from [git-scm.com](https://git-scm.com/download/win)

**Linux:** 
```bash
## Ubuntu/Debian
sudo apt install git

## CentOS/RHEL
sudo yum install git
```

##### First-Time Setup
Configure Git with your identity (use the same email as your GitHub account):

```bash
## Set your name (appears in commit history)
git config --global user.name "Your Name"

## Set your email (must match GitHub account)
git config --global user.email "your.email@example.com"

## Verify configuration
git config --global --list
```

#### Creating Your GitHub Account

1. **Visit [github.com](https://github.com)**
2. **Sign up** with a professional username (employers will see this)
3. **Choose a plan** - Free plan is perfect for learning
4. **Verify your email** - important for security
5. **Complete your profile** - add a photo and bio

##### Profile Tips
- **Use your real name** or professional username
- **Add a profile picture** - makes you more memorable
- **Write a bio** - mention you're learning Bitcoin development
- **Pin your best repositories** - showcase your top projects

#### Your First Repository

##### Creating a Repository on GitHub
1. **Click "New repository"** (green button on GitHub)
2. **Name your repository** - use descriptive names like "bitcoin-price-tracker"
3. **Add description** - explain what the project does
4. **Make it public** - show off your work
5. **Initialize with README** - creates a starting file
6. **Click "Create repository"**

##### Cloning to Your Computer
```bash
## Navigate to where you want the project
cd ~/Desktop

## Clone the repository (replace with your URL)
git clone https://github.com/yourusername/your-repo-name.git

## Enter the project directory
cd your-repo-name

## Open in VS Code
code .
```

### The Daily Git Workflow
This is what you'll do every time you make changes:

```bash
## 1. Check what files have changed
git status

## 2. Add files to staging area
git add .                 # Add all changes
git add filename.js       # Add specific file

## 3. Commit your changes with a message
git commit -m "Add Bitcoin price fetching feature"

## 4. Push to GitHub
git push origin main
```

##### Understanding Git Status
Git status shows three types of files:
- **Red files** - modified but not staged
- **Green files** - staged and ready to commit
- **Clean working tree** - no changes to commit

```bash
## Example git status output
On branch main
Changes not staged for commit:
  modified:   index.html        # Red - needs staging
  modified:   script.js         # Red - needs staging

Changes to be committed:
  modified:   style.css         # Green - staged and ready
```

##### Writing Good Commit Messages
Commit messages should be:
- **Clear and descriptive** - explain what changed
- **Present tense** - "Add feature" not "Added feature"  
- **Specific** - "Fix wallet balance display bug" not "Fix stuff"

```bash
## Good commit messages
git commit -m "Add real-time Bitcoin price updates"
git commit -m "Fix wallet balance calculation error"
git commit -m "Improve mobile responsive design"

## Poor commit messages
git commit -m "stuff"
git commit -m "changes"
git commit -m "idk"
```

#### Working with Remotes

##### Understanding Remote Repositories
- **Local repository** - Git repo on your computer
- **Remote repository** - Git repo on GitHub
- **Origin** - default name for your main remote repository

##### Remote Commands
```bash
## View your remotes
git remote -v

## Add a remote (usually done automatically when cloning)
git remote add origin https://github.com/username/repo.git

## Push to remote
git push origin main       # Push main branch
git push                   # Push current branch (if upstream is set)

## Pull from remote
git pull origin main       # Pull main branch
git pull                   # Pull current branch
```

#### Branching and Merging

##### Why Use Branches?
Branches let you:
- **Experiment safely** - try new features without breaking main code
- **Work on multiple features** simultaneously
- **Collaborate effectively** - different people work on different branches
- **Review code** before it goes to production

##### Basic Branching
```bash
## Create and switch to a new branch
git checkout -b feature/bitcoin-price-display

## Switch between branches
git checkout main                    # Switch to main
git checkout feature/bitcoin-price-display  # Switch to feature branch

## See all branches
git branch

## Delete a branch (after merging)
git branch -d feature/bitcoin-price-display
```

##### Merging Branches
```bash
## Switch to main branch
git checkout main

## Merge feature branch into main
git merge feature/bitcoin-price-display

## Push merged changes
git push origin main
```

#### GitHub Web Interface

##### Repository Navigation
- **Code tab** - browse files and folders
- **Issues tab** - track bugs and feature requests
- **Pull requests tab** - code review and merging
- **Actions tab** - automated workflows (CI/CD)
- **Settings tab** - repository configuration

##### Viewing Commit History
Click on "commits" to see:
- **Commit messages** and timestamps
- **File changes** (green additions, red deletions)
- **Author information**
- **Commit hashes** for referencing specific versions

##### Understanding Pull Requests
Pull requests are where professional development happens:
1. **Create feature branch** and make changes
2. **Push branch to GitHub**
3. **Open pull request** to merge into main
4. **Code review** - team members review changes
5. **Discussion** - suggest improvements
6. **Approve and merge** - changes go to main branch

#### GitHub as Your Portfolio

##### Contribution Graph
The green squares on your profile show:
- **Daily activity** - commits, pull requests, issues
- **Consistency** - regular contributions over time
- **Intensity** - darker green = more activity

**Goal:** Get into the habit of making at least one commit per day when working on projects.

##### Showcasing Your Work
- **Pin repositories** - highlight your best 6 projects
- **Write good READMEs** - explain what your project does
- **Use descriptive names** - "bitcoin-lightning-wallet" not "project1"
- **Add screenshots** - show your projects in action
- **Include live demos** - link to deployed versions

#### README Best Practices
A good README includes:
```markdown
    ## Project Name
    Brief description of what it does

    ### Features
    - List key features
    - What makes it special

    ### Demo
    [Live Demo](https://your-app.vercel.app)

    ### Screenshots
    ![App Screenshot](screenshot.png)

    ### Installation
    Steps to run locally

    ### Technologies Used
    - HTML, CSS, JavaScript
    - React, Node.js
    - LNbits, Bitcoin APIs

    ### What I Learned
    - New skills gained
    - Challenges overcome
``` 

## Moving to React Architecture
<chapterId>68055299-b666-47de-925b-91783cca4ca6</chapterId>

### Introduction to React

React is a **JavaScript library for building user interfaces**, particularly web applications. It was created by Facebook (now Meta) and has become the most popular way to build modern web applications.

#### Why React Matters
- **Industry standard** - Most companies use React for frontend development
- **Component-based** - Build UIs as reusable pieces
- **Easier to manage** - Organizes complex applications
- **Better developer experience** - Powerful tools and debugging
- **Job market** - High demand for React developers

#### React vs Vanilla JavaScript
In previous lessons, we built applications with HTML, CSS, and JavaScript separately. This works for small projects but becomes difficult as applications grow:

**Vanilla JavaScript challenges:**
- **Code scattered** across multiple files
- **Hard to reuse** UI components
- **Manual DOM manipulation** is error-prone
- **State management** becomes complex
- **Testing and debugging** is difficult

**React solutions:**
- **Everything in one place** - HTML, CSS, and JavaScript together
- **Reusable components** - Write once, use everywhere
- **Automatic updates** - React handles DOM changes
- **Predictable state** - Easier to understand and debug
- **Rich ecosystem** - Tools, libraries, and community support

### React Fundamentals

#### Components: The Building Blocks
React applications are built from **components** - reusable pieces of UI that combine HTML, CSS, and JavaScript:

```jsx
// A simple React component
function BitcoinPrice() {
    return (
        <div className="price-display">
            <h2>Bitcoin Price</h2>
            <p>$45,000</p>
        </div>
    );
}
```

**Key concepts:**
- **Functions that return HTML** - Components are JavaScript functions
- **JSX syntax** - Write HTML-like code in JavaScript
- **Reusable** - Use the same component multiple times
- **Composable** - Combine components to build complex UIs

#### JSX: HTML in JavaScript
JSX lets you write HTML-like syntax directly in JavaScript:

```jsx
// JSX (what you write)
const greeting = <h1>Hello, Bitcoin developers!</h1>;

// What it becomes (JavaScript)
const greeting = React.createElement('h1', null, 'Hello, Bitcoin developers!');
```

**JSX differences from HTML:**
- `className` instead of `class` (class is a JavaScript keyword)
- `onClick` instead of `onclick` (camelCase event handlers)
- Curly braces `{}` for JavaScript expressions
- Self-closing tags must have `/` (like `<img />`)

##### State: Making Components Dynamic
State allows components to remember and change data:

```jsx
import { useState } from 'react';

function BitcoinPrice() {
    const [price, setPrice] = useState(0);
    
    // This function updates the price
    const updatePrice = (newPrice) => {
        setPrice(newPrice);
    };
    
    return (
        <div>
            <h2>Bitcoin Price: ${price}</h2>
            <button onClick={() => updatePrice(50000)}>
                Update Price
            </button>
        </div>
    );
}
```

**State concepts:**
- **useState hook** - React's way to add state to components
- **Current value** - `price` holds the current state
- **Setter function** - `setPrice` updates the state
- **Re-rendering** - React automatically updates the UI when state changes

##### Effects: Handling Side Effects
Effects let you perform operations like API calls, timers, and cleanup:

```jsx
import { useState, useEffect } from 'react';

function BitcoinPrice() {
    const [price, setPrice] = useState(0);
    
    useEffect(() => {
        // This runs after the component mounts
        fetchBitcoinPrice().then(setPrice);
        
        // Set up interval to update price every 10 seconds
        const interval = setInterval(() => {
            fetchBitcoinPrice().then(setPrice);
        }, 10000);
        
        // Cleanup function (runs when component unmounts)
        return () => clearInterval(interval);
    }, []); // Empty dependency array = run once on mount
    
    return <div>Bitcoin Price: ${price}</div>;
}
```

**Effect concepts:**
- **useEffect hook** - Perform side effects in components
- **Dependencies array** - Control when effects run
- **Cleanup function** - Prevent memory leaks
- **Lifecycle events** - React automatically manages when effects run

### Creating Your First React App

#### Using Create React App
Create React App is a tool that sets up a complete React development environment with one command:

```bash
## Navigate to your projects folder
cd ~/Desktop

## Create a new React app
npx create-react-app pleb-wallet-react

## Enter the project directory
cd pleb-wallet-react

## Open in VS Code
code .
```

**What this creates:**
- **Complete project structure** - All necessary files and folders
- **Development server** - Live reload as you make changes
- **Build system** - Compiles and optimizes your code
- **Testing setup** - Framework for writing tests
- **Git repository** - Version control ready to go

#### Project Structure Overview
```
pleb-wallet-react/
├── public/
│   ├── index.html          # Main HTML file
│   └── favicon.ico         # Website icon
├── src/
│   ├── App.js              # Main App component
│   ├── App.css             # App styles
│   ├── index.js            # Entry point
│   └── index.css           # Global styles
├── package.json            # Project configuration
├── package-lock.json       # Dependency lock file
└── node_modules/           # Installed packages
```

##### Understanding package.json
The `package.json` file is your project's configuration center:

```json
{
  "name": "pleb-wallet-react",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

**Key sections:**
- **dependencies** - External packages your project uses
- **scripts** - Commands you can run (`npm start`, `npm build`, etc.)
- **name/version** - Project identification

##### Understanding node_modules
The `node_modules` folder contains all the code libraries your project depends on:
- **Massive folder** - Can contain thousands of files
- **Don't edit manually** - Managed by npm
- **Can be regenerated** - Delete and run `npm install` to recreate
- **Not in Git** - Too large for version control

##### Starting Your Development Server
```bash
# Start the development server
<partId>de47af6c-e9be-4456-96b6-d41f0cdd9a83</partId>
npm start
```

This opens your React app in the browser at `http://localhost:3000` with:
- **Live reload** - Changes appear instantly
- **Error display** - Syntax errors shown in browser
- **Hot module replacement** - Updates without full page refresh

#### React App Architecture

##### How React Apps Work
React apps follow a specific architecture:

1. **index.html** - Contains a single `<div id="root"></div>`
2. **index.js** - JavaScript entry point that injects React into the HTML
3. **App.js** - Main component that contains your entire application
4. **Components** - Smaller pieces that make up your app

##### Entry Point: index.js
```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
```

**What this does:**
- **Finds the root div** in index.html
- **Creates React root** - Tells React where to inject components
- **Renders App component** - Your main application component

##### Main Component: App.js
```jsx
import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Pleb Wallet</h1>
        <p>Your Bitcoin Lightning Wallet</p>
      </header>
    </div>
  );
}

export default App;
```

**Component structure:**
- **Import React** - Required for JSX
- **Import CSS** - Component-specific styles
- **Function component** - Returns JSX
- **Export default** - Makes component available to other files

#### Building a Bitcoin Price Component

Let's build a real component that fetches Bitcoin prices:

##### Step 1: Create the Component
```jsx
// BitcoinPrice.js
import React, { useState, useEffect } from 'react';

function BitcoinPrice() {
    const [price, setPrice] = useState(0);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchBitcoinPrice();
        const interval = setInterval(fetchBitcoinPrice, 10000);
        return () => clearInterval(interval);
    }, []);

    const fetchBitcoinPrice = async () => {
        try {
            const response = await fetch('https://api.coinbase.com/v2/prices/BTC-USD/spot');
            const data = await response.json();
            setPrice(Number(data.data.amount));
            setLoading(false);
        } catch (error) {
            console.error('Failed to fetch Bitcoin price:', error);
            setLoading(false);
        }
    };

    if (loading) {
        return <div>Loading Bitcoin price...</div>;
    }

    return (
        <div className="bitcoin-price">
            <h2>Bitcoin Price</h2>
            <p>${price.toLocaleString()}</p>
        </div>
    );
}

export default BitcoinPrice;
```

##### Step 2: Use the Component in App.js
```jsx
import React from 'react';
import BitcoinPrice from './BitcoinPrice';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Pleb Wallet</h1>
        <BitcoinPrice />
      </header>
    </div>
  );
}

export default App;
```

##### Step 3: Add Styling
```css
/* App.css */
.bitcoin-price {
    background: #f7931a;
    color: white;
    padding: 20px;
    border-radius: 10px;
    margin: 20px 0;
    text-align: center;
}

.bitcoin-price h2 {
    margin: 0 0 10px 0;
}

.bitcoin-price p {
    font-size: 2em;
    font-weight: bold;
    margin: 0;
}
```

#### Package Management with NPM

##### What is NPM?
NPM (Node Package Manager) is the world's largest software registry containing over 2 million packages:
- **Free and open source** - Anyone can publish packages
- **Quality packages** - Battle-tested by millions of developers
- **Easy installation** - One command to add functionality
- **Dependency management** - Automatically handles package dependencies

##### Installing Packages
```bash
## Install a package for your project
npm install axios                  # API client
npm install react-qr-code          # QR code generator

## Install development-only packages
npm install --save-dev eslint      # Code linting (dev only)

## Install packages globally (available system-wide)
npm install -g create-react-app    # Global CLI tools
```

##### Package.json Updates
When you install packages, `package.json` automatically updates:

```json
{
  "dependencies": {
    "axios": "^1.6.0",
    "react": "^18.2.0",
    "react-qr-code": "^2.0.11"
  }
}
```

##### Using Installed Packages
```jsx
// Import and use installed packages
import axios from 'axios';
import QRCode from 'react-qr-code';

function PaymentRequest() {
    const [invoice, setInvoice] = useState('');

    const fetchInvoice = async () => {
        const response = await axios.get('/api/invoice');
        setInvoice(response.data.payment_request);
    };

    return (
        <div>
            <button onClick={fetchInvoice}>Generate Invoice</button>
            {invoice && <QRCode value={invoice} />}
        </div>
    );
}
```

##### Package Security and Quality
When choosing packages, consider:
- **Download count** - More downloads usually mean better quality
- **Recent updates** - Active maintenance is important
- **GitHub stars** - Community approval indicator
- **Documentation** - Good docs mean easier integration
- **Bundle size** - Smaller packages = faster loading

##### Common Useful Packages
```bash
## API and HTTP requests
npm install axios

## Date manipulation
npm install date-fns

## QR code generation
npm install react-qr-code

## Bitcoin utilities
npm install bitcoin-price-api

## UI component libraries
npm install @mui/material           # Material-UI
npm install react-bootstrap         # Bootstrap components

## State management
npm install zustand                 # Simple state management
```

#### React Development Workflow

##### Daily Development Process
1. **Start development server** - `npm start`
2. **Edit components** - Make changes in VS Code
3. **See changes live** - Browser updates automatically
4. **Test functionality** - Click around, test features
5. **Commit changes** - `git add`, `git commit`, `git push`

##### Hot Reloading
React's development server provides hot reloading:
- **Save file** → Browser updates instantly
- **Syntax errors** → Show in browser overlay
- **State preserved** → No need to recreate app state
- **Fast iteration** → See changes immediately

### Debugging React Apps

##### Browser Developer Tools
React provides additional debugging tools:
- **Install React Developer Tools** browser extension
- **Components tab** - Inspect React component tree
- **Profiler tab** - Analyze performance
- **State inspection** - See component state and props

##### Common Debugging Techniques
```jsx
function BitcoinPrice() {
    const [price, setPrice] = useState(0);
    
    // Console logging for debugging
    console.log('Current price:', price);
    
    useEffect(() => {
        console.log('Component mounted');
        fetchPrice();
        
        return () => {
            console.log('Component unmounting');
        };
    }, []);
    
    const fetchPrice = async () => {
        try {
            const data = await fetch('/api/price');
            console.log('API response:', data);
            setPrice(data.price);
        } catch (error) {
            console.error('API error:', error);
        }
    };
    
    return <div>Price: ${price}</div>;
}
``` 

## Deploying to Production with Vercel
<chapterId>fe8fe942-0ae7-4f1b-8667-01ace11f3481</chapterId>

### What is Production Deployment?

**Production deployment** means making your application available to real users on the internet. Up until now, your app only runs on your computer (`localhost:3000`). Deployment puts it on a real URL that anyone can visit.

#### Why Vercel?

Vercel is a deployment platform specifically designed for frontend applications:
- **Free tier** - Perfect for learning and small projects
- **Automatic deployments** - Connects directly to GitHub
- **Global CDN** - Fast loading worldwide
- **HTTPS by default** - Secure connections
- **Custom domains** - Use your own domain name
- **Zero configuration** - Works out of the box with React

#### Setting Up Vercel

##### Creating Your Account
1. **Visit [vercel.com](https://vercel.com)**
2. **Sign up with GitHub** - This connects your repositories automatically
3. **Complete profile** - Add your name and details
4. **Choose hobby plan** - Free tier is perfect for learning

##### Connecting Your Repository
Once your React app is pushed to GitHub:

1. **Click "New Project"** on Vercel dashboard
2. **Import from GitHub** - Vercel lists your repositories
3. **Select your React app** repository
4. **Configure project** - Vercel automatically detects it's a React app
5. **Click "Deploy"** - Your app starts building

##### Automatic Configuration
Vercel automatically detects:
- **Framework** - Identifies Create React App
- **Build command** - `npm run build`
- **Output directory** - `build/`
- **Node.js version** - Uses latest stable version

### Understanding the Deployment Process

#### What Happens During Deployment
1. **Code checkout** - Vercel downloads your GitHub repository
2. **Install dependencies** - Runs `npm install`
3. **Build application** - Runs `npm run build`
4. **Optimize assets** - Compresses images, minifies code
5. **Deploy to CDN** - Distributes globally for fast access
6. **Generate URL** - Creates your live application URL

##### Build Process Details
```bash
## What `npm run build` does:
✅ Compiles JSX to JavaScript
✅ Bundles all components into optimized files
✅ Minifies CSS and JavaScript
✅ Optimizes images and assets
✅ Generates service worker for caching
✅ Creates production-ready files in build/ folder
```

### Live Deployment Workflow

##### The Complete Workflow
This is the professional development cycle you'll use:

```bash
## 1. Make changes locally
code .                          # Edit in VS Code
npm start                       # Test locally

## 2. Commit changes
git add .
git commit -m "Add new feature"
git push origin main

## 3. Automatic deployment
## Vercel detects the GitHub push
## Automatically builds and deploys
## New version is live in ~30 seconds
```

##### Watching Deployments
In your Vercel dashboard, you can:
- **See build progress** - Real-time deployment logs
- **View deployment history** - Every version ever deployed
- **Rollback if needed** - Instantly revert to previous version
- **Preview branches** - Test feature branches before merging

##### Environment Variables
For sensitive data like API keys:

```bash
## In Vercel dashboard → Settings → Environment Variables
REACT_APP_API_KEY=your_secret_key_here
REACT_APP_LNBITS_URL=https://demo.lnbits.com
```

**Using environment variables in React:**
```jsx
const apiKey = process.env.REACT_APP_API_KEY;
const lnbitsUrl = process.env.REACT_APP_LNBITS_URL;
```

**Important:** Only variables starting with `REACT_APP_` are included in the build.

#### Custom Domains

##### Adding Your Own Domain
Once you're ready for a professional presence:

1. **Buy a domain** - From providers like Namecheap, GoDaddy
2. **Add to Vercel** - Project Settings → Domains
3. **Configure DNS** - Point your domain to Vercel
4. **Automatic HTTPS** - Vercel provides SSL certificates

Example: `your-bitcoin-wallet.com` instead of `random-name.vercel.app`

#### Project: Complete Development to Deployment

Let's build and deploy a complete Bitcoin price tracker:

##### Step 1: Create React App
```bash
## Create new React app
npx create-react-app bitcoin-price-tracker
cd bitcoin-price-tracker

## Install additional packages
npm install axios

## Open in VS Code
code .
```

##### Step 2: Build Bitcoin Price Component
```jsx
// src/BitcoinPrice.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './BitcoinPrice.css';

function BitcoinPrice() {
    const [price, setPrice] = useState(0);
    const [previousPrice, setPreviousPrice] = useState(0);
    const [loading, setLoading] = useState(true);
    const [lastUpdated, setLastUpdated] = useState(null);

    useEffect(() => {
        fetchPrice();
        const interval = setInterval(fetchPrice, 30000); // Update every 30 seconds
        return () => clearInterval(interval);
    }, []);

    const fetchPrice = async () => {
        try {
            const response = await axios.get('https://api.coinbase.com/v2/prices/BTC-USD/spot');
            const newPrice = Number(response.data.data.amount);
            
            setPreviousPrice(price);
            setPrice(newPrice);
            setLastUpdated(new Date());
            setLoading(false);
        } catch (error) {
            console.error('Error fetching price:', error);
            setLoading(false);
        }
    };

    const getPriceDirection = () => {
        if (price > previousPrice) return 'up';
        if (price < previousPrice) return 'down';
        return 'same';
    };

    const formatPrice = (price) => {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            minimumFractionDigits: 2,
            maximumFractionDigits: 2,
        }).format(price);
    };

    if (loading) {
        return (
            <div className="bitcoin-price loading">
                <div className="spinner"></div>
                <p>Loading Bitcoin price...</p>
            </div>
        );
    }

    return (
        <div className={`bitcoin-price ${getPriceDirection()}`}>
            <h1>₿ Bitcoin Price</h1>
            <div className="price-display">
                <span className="price">{formatPrice(price)}</span>
                <span className="direction">
                    {getPriceDirection() === 'up' && '↗'}
                    {getPriceDirection() === 'down' && '↘'}
                    {getPriceDirection() === 'same' && '→'}
                </span>
            </div>
            {lastUpdated && (
                <p className="last-updated">
                    Last updated: {lastUpdated.toLocaleTimeString()}
                </p>
            )}
            <button onClick={fetchPrice} className="refresh-btn">
                Refresh Price
            </button>
        </div>
    );
}

export default BitcoinPrice;
```

##### Step 3: Add Styling
```css
/* src/BitcoinPrice.css */
.bitcoin-price {
    max-width: 600px;
    margin: 2rem auto;
    padding: 2rem;
    border-radius: 12px;
    background: linear-gradient(135deg, #f7931a, #ff6b35);
    color: white;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

.bitcoin-price.up {
    background: linear-gradient(135deg, #00d4aa, #00a085);
}

.bitcoin-price.down {
    background: linear-gradient(135deg, #ff4757, #ff3742);
}

.bitcoin-price h1 {
    margin: 0 0 1rem 0;
    font-size: 2rem;
    font-weight: 300;
}

.price-display {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    margin: 1.5rem 0;
}

.price {
    font-size: 3rem;
    font-weight: bold;
    letter-spacing: -2px;
}

.direction {
    font-size: 2rem;
    animation: pulse 2s infinite;
}

.last-updated {
    margin: 1rem 0;
    opacity: 0.8;
    font-size: 0.9rem;
}

.refresh-btn {
    background: rgba(255, 255, 255, 0.2);
    border: 2px solid rgba(255, 255, 255, 0.3);
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 25px;
    cursor: pointer;
    font-size: 1rem;
    transition: all 0.3s ease;
}

.refresh-btn:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: translateY(-2px);
}

.loading {
    background: linear-gradient(135deg, #667eea, #764ba2);
}

.spinner {
    width: 40px;
    height: 40px;
    border: 4px solid rgba(255, 255, 255, 0.3);
    border-top: 4px solid white;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin: 0 auto 1rem auto;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
}

@media (max-width: 768px) {
    .bitcoin-price {
        margin: 1rem;
        padding: 1.5rem;
    }
    
    .price {
        font-size: 2.5rem;
    }
    
    .bitcoin-price h1 {
        font-size: 1.5rem;
    }
}
```

##### Step 4: Update App.js
```jsx
// src/App.js
import React from 'react';
import BitcoinPrice from './BitcoinPrice';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <BitcoinPrice />
        <footer>
          <p>Made with ❤️ by a Bitcoin pleb</p>
          <p>Data from Coinbase API</p>
        </footer>
      </header>
    </div>
  );
}

export default App;
```

##### Step 5: Push to GitHub
```bash
## Initialize Git (if not already done)
git init
git add .
git commit -m "Initial Bitcoin price tracker"

## Create repository on GitHub and push
git remote add origin https://github.com/yourusername/bitcoin-price-tracker.git
git branch -M main
git push -u origin main
```

##### Step 6: Deploy to Vercel
1. **Go to Vercel dashboard**
2. **Click "New Project"**
3. **Import your GitHub repository**
4. **Click "Deploy"**
5. **Wait for deployment to complete**
6. **Visit your live URL!**

#### Continuous Deployment

##### What is Continuous Deployment?
Once connected to GitHub, every push to your main branch automatically triggers a new deployment:

```bash
## Make a change
echo "Added new feature" >> README.md

## Commit and push
git add .
git commit -m "Update documentation"
git push origin main

# Vercel automatically:
<partId>cc2212b1-604c-479a-9b3e-2572bcb929eb</partId>
# 1. Detects the push
<partId>a8c1192c-4737-4212-b6dd-d6ec999e8d67</partId>
# 2. Starts building
<partId>134a9452-fde4-4a06-a820-1e00c4f78605</partId>
# 3. Deploys new version
<partId>39915c97-1fcd-4625-9ef4-e990b4825e2a</partId>
# 4. Updates live URL
<partId>db8ef232-4c24-4dd4-9f40-b1b6a7f329e0</partId>
```

##### Branch Previews
Vercel also creates preview deployments for feature branches:
```bash
## Create feature branch
git checkout -b feature/add-charts

## Make changes and push
git add .
git commit -m "Add price charts"
git push origin feature/add-charts

## Vercel creates a preview URL just for this branch
## Perfect for testing before merging to main
```

### Hands-on Exercises

#### Exercise 1: Complete Development Environment Setup
Set up your professional development environment:

1. **Install all required tools:**
   - Node.js and npm
   - Visual Studio Code
   - Git
   - Essential VS Code extensions (ESLint, Prettier)

2. **Create GitHub account and profile:**
   - Professional username
   - Profile picture and bio
   - Pin your best repositories

3. **Test your setup:**
   - Create a new React app
   - Open in VS Code
   - Start development server
   - Make changes and see live updates

#### Exercise 2: Git Workflow Practice
Master the basic Git workflow:

1. **Create a new repository:**
   - Initialize locally with `git init`
   - Create on GitHub
   - Connect local to remote
   - Push initial commit

2. **Practice daily workflow:**
   - Make changes to files
   - Use `git status` to check changes
   - Stage with `git add`
   - Commit with descriptive messages
   - Push to GitHub

3. **Experiment with branches:**
   - Create feature branch
   - Make changes on branch
   - Switch between branches
   - Merge feature into main

#### Exercise 3: React Component Building
Build a collection of Bitcoin-related React components:

1. **Bitcoin News Component:**
   ```jsx
   // Fetch from a crypto news API
   // Display latest Bitcoin headlines
   // Add refresh functionality
   // Include loading states
   ```

2. **Satoshi Quote Generator:**
   ```jsx
   // Array of famous Satoshi quotes
   // Random quote on button click
   // Tweet quote functionality
   // Copy to clipboard feature
   ```

3. **Block Height Tracker:**
   ```jsx
   // Fetch current Bitcoin block height
   // Show time since last block
   // Display mining difficulty
   // Real-time updates
   ```

#### Exercise 4: Full-Stack Bitcoin App
Create a comprehensive Bitcoin dashboard:

1. **Plan your application:**
   - Sketch UI layout
   - List required components
   - Identify data sources
   - Plan user interactions

2. **Build components:**
   - Price display with charts
   - News feed
   - Calculator (USD ↔ BTC)
   - Lightning network stats

3. **Add advanced features:**
   - Local storage for favorites
   - Dark/light theme toggle
   - Responsive design
   - Progressive Web App features

4. **Deploy and share:**
   - Push to GitHub
   - Deploy to Vercel
   - Add custom domain
   - Share with the Bitcoin community

#### Exercise 5: Open Source Contribution
Contribute to the Bitcoin development community:

1. **Find a project:**
   - Browse Bitcoin-related repositories
   - Look for "good first issue" labels
   - Read contribution guidelines
   - Fork the repository

2. **Make your contribution:**
   - Fix a bug or add a feature
   - Write good commit messages
   - Test your changes thoroughly
   - Submit a pull request

3. **Engage with maintainers:**
   - Respond to feedback professionally
   - Make requested changes
   - Learn from code review
   - Celebrate when merged!

#### Learning Resources

**Official Documentation**
- **[React Documentation](https://react.dev/)** - Official React docs with interactive examples
- **[Create React App](https://create-react-app.dev/)** - Complete setup and configuration guide
- **[Node.js Documentation](https://nodejs.org/docs/)** - Node.js and npm reference
- **[Git Documentation](https://git-scm.com/doc)** - Complete Git command reference
- **[GitHub Guides](https://guides.github.com/)** - Step-by-step GitHub tutorials
- **[Vercel Documentation](https://vercel.com/docs)** - Deployment and hosting guide

**Development Tools**
- **[Visual Studio Code](https://code.visualstudio.com/docs)** - Editor documentation and tutorials
- **[React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/)** - Browser extension for debugging
- **[Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)** - Quick Git command reference
- **[npm Documentation](https://docs.npmjs.com/)** - Package management guide

**Bitcoin Development Resources**
- **[Bitcoin Developer Documentation](https://developer.bitcoin.org/)** - Official Bitcoin development guide
- **[Lightning Network Resources](https://lightning.network/lightning-network-paper.pdf)** - Lightning Network whitepaper
- **[LNbits Documentation](https://lnbits.com/)** - Lightning wallet and account system
- **[Bitcoin APIs](https://bitcoinbook.info/wp-content/themes/bitcoinbook/assets/appendix-bitcoin-apis.html)** - List of Bitcoin APIs

**React Learning Path**
- **[React Tutorial](https://react.dev/learn)** - Interactive tutorial from React team
- **[React Hooks Guide](https://react.dev/reference/react)** - Complete hooks reference
- **[React Patterns](https://reactpatterns.com/)** - Common React patterns and best practices
- **[React Performance](https://kentcdodds.com/blog/fix-the-slow-render-before-you-fix-the-re-render)** - Optimization techniques

**Project Ideas and Inspiration**
- **[GitHub Explore](https://github.com/explore)** - Discover trending repositories
- **[Awesome Bitcoin](https://github.com/igorbarinov/awesome-bitcoin)** - Curated Bitcoin resources
- **[React Projects](https://github.com/topics/react-projects)** - Example React applications
- **[Bitcoin Development Examples](https://github.com/bitcoinbook/bitcoinbook)** - Mastering Bitcoin code examples

### Best Practices and Tips

#### Development Environment
1. **Keep tools updated** - Regularly update Node.js, VS Code, and extensions
2. **Use consistent formatting** - Let Prettier handle code formatting
3. **Learn keyboard shortcuts** - Speed up your development workflow
4. **Organize your workspace** - Keep projects organized in folders
5. **Use meaningful names** - For files, functions, and variables

#### Git and GitHub
1. **Commit frequently** - Small, focused commits are easier to understand
2. **Write clear commit messages** - Explain what and why, not how
3. **Use branches for features** - Keep main branch stable
4. **Review before pushing** - Use `git diff` to check changes
5. **Keep README updated** - Document your project clearly

#### React Development
1. **Component naming** - Use PascalCase for component names
2. **File organization** - One component per file, group related files
3. **State management** - Keep state as local as possible
4. **Effect cleanup** - Always clean up intervals, subscriptions
5. **Error boundaries** - Handle errors gracefully
6. **Performance** - Use React DevTools to identify bottlenecks

#### Code Quality
1. **Use TypeScript** - Add type safety as you advance
2. **Write tests** - Start with simple unit tests
3. **Handle errors** - Always include try/catch for async operations
4. **Validate inputs** - Check user inputs and API responses
5. **Document complex logic** - Add comments for future self

#### Security Considerations
1. **Never commit secrets** - Use environment variables
2. **Validate API responses** - Don't trust external data
3. **Use HTTPS** - Always use secure connections
4. **Keep dependencies updated** - Regularly update packages
5. **Follow security advisories** - Subscribe to security notifications

#### Next Steps and Career Development

#### Immediate Next Steps
1. **Complete the course project** - Build and deploy your Bitcoin wallet
2. **Practice daily** - Code a little bit every day
3. **Join communities** - Bitcoin development Discord/Telegram groups
4. **Read code** - Study open source Bitcoin projects
5. **Document learning** - Write about what you build

#### Advanced Topics to Explore
- **TypeScript** - Add static typing to JavaScript
- **Testing** - Jest, React Testing Library
- **State Management** - Redux, Zustand, Context API
- **Styling Solutions** - Styled Components, Tailwind CSS
- **Build Tools** - Webpack, Vite, custom configurations
- **Backend Development** - Node.js, Express, databases
- **Blockchain Integration** - Web3, Bitcoin libraries

#### Building Your Portfolio
1. **GitHub presence** - Maintain consistent green squares
2. **Project documentation** - Write excellent READMEs
3. **Live demos** - Deploy projects for others to see
4. **Blog about learning** - Share your journey
5. **Contribute to open source** - Build reputation in community

#### Career Opportunities
- **Frontend Developer** - Focus on user interfaces
- **Full-Stack Developer** - Frontend + backend skills
- **Bitcoin Developer** - Specialize in Bitcoin/Lightning
- **DevOps Engineer** - Focus on deployment and infrastructure
- **Technical Writer** - Document Bitcoin technology
- **Open Source Maintainer** - Lead Bitcoin projects

#### Continuing Education
- **Advanced React patterns** - Compound components, render props
- **Performance optimization** - Code splitting, lazy loading
- **Accessibility** - Making apps usable for everyone
- **Progressive Web Apps** - Native app-like experiences
- **Server-side rendering** - Next.js, Gatsby
- **Mobile development** - React Native

#### Key Takeaways

1. **Professional development requires proper tooling** - VS Code, Git, Node.js are industry standards
2. **Version control is essential** - Git and GitHub are used by every professional developer
3. **React simplifies complex applications** - Component-based architecture scales better than vanilla JavaScript
4. **Deployment should be automatic** - Continuous deployment from GitHub to production
5. **Package management saves time** - npm ecosystem provides solutions for common problems
6. **Practice builds understanding** - Set up your environment and build projects daily
7. **Community involvement accelerates learning** - Contribute to open source and engage with developers
8. **Portfolio building starts now** - Every project you build showcases your skills

Congratulations! You've learned to set up a professional development environment and understand the modern web development workflow. You can now build React applications, manage code with Git, and deploy to production. These are the exact same tools and processes used by developers at major tech companies.

The next lesson will dive deeper into React and build a complete Lightning wallet application. Keep practicing, keep building, and welcome to the professional development community! 🚀

---

#### What's Next?

In future lessons, you'll learn:
- **Advanced React patterns** - Custom hooks, context, performance optimization
- **Lightning Network integration** - Building real Bitcoin applications
- **Backend development** - APIs, databases, authentication
- **Production best practices** - Testing, monitoring, scaling
- **Career preparation** - Portfolio building, interview skills, job hunting

The journey continues, and you're well-equipped for what comes next! ⚡️🧡 

# Building the Pleb Wallet Frontend
<partId>65ca5d69-60a4-4906-a293-ff87567f2299</partId>

## The React Paradigm Shift
<chapterId>9cb5b0d7-401b-4758-a1e6-03af4707f9b7</chapterId>

### The Problem with Vanilla JavaScript
Our previous wallet worked, but it had limitations:
- **Scattered code** - HTML, CSS, and JavaScript in separate files
- **Manual DOM manipulation** - Tedious and error-prone updates
- **Difficult state management** - Hard to keep UI in sync with data
- **Poor reusability** - Copying code instead of reusing components
- **Complex debugging** - Hard to trace problems across files

#### The React Solution
React solves these problems with:
- **Component-based architecture** - Everything in logical, reusable pieces
- **Declarative programming** - Describe what UI should look like, React handles how
- **Automatic updates** - React updates DOM when data changes
- **Developer tools** - Excellent debugging and development experience
- **Industry adoption** - Used by Facebook, Netflix, Airbnb, and most Bitcoin companies

#### Understanding the Virtual DOM
React's secret weapon is the Virtual DOM - a JavaScript representation of your actual webpage:

```javascript
// Instead of directly manipulating DOM like this:
document.getElementById('price').innerHTML = '$45000';

// React does this:
const [price, setPrice] = useState(45000);
return <div>Price: ${price}</div>; // React handles DOM updates
```

**How it works:**
1. **Virtual representation** - React creates a virtual copy of your DOM in memory
2. **Efficient diffing** - When data changes, React compares virtual DOM snapshots
3. **Minimal updates** - Only changes what actually needs updating
4. **Better performance** - Especially important for real-time Bitcoin price updates

#### Why This Matters for Our Wallet
Imagine our wallet updating the Bitcoin price every 5 seconds:
- **Without React** - Re-render entire page, slow and inefficient
- **With React** - Update only the price display, smooth and fast

### React Components: The Building Blocks

#### What Are Components?
Components are **reusable pieces of UI** that combine HTML, CSS, and JavaScript:

```jsx
// A simple Bitcoin price component
function BitcoinPrice() {
    const [price, setPrice] = useState(0);
    
    return (
        <div className="price-display">
            <h2>Bitcoin Price</h2>
            <p>${price.toLocaleString()}</p>
        </div>
    );
}
```

#### Component Benefits
- **Reusability** - Write once, use everywhere
- **Modularity** - Each component has a single responsibility
- **Testability** - Easy to test individual pieces
- **Maintainability** - Changes are isolated to specific components

#### Functional vs Class Components

##### Class Components (Legacy - Don't Use)
```jsx
class BitcoinPrice extends React.Component {
    constructor(props) {
        super(props);
        this.state = { price: 0 };
    }
    
    render() {
        return <div>Price: ${this.state.price}</div>;
    }
}
```

##### Functional Components (Modern - Use This)
```jsx
function BitcoinPrice() {
    const [price, setPrice] = useState(0);
    return <div>Price: ${price}</div>;
}
```

**Why functional components:**
- **Simpler syntax** - Less boilerplate code
- **Hooks support** - Modern React features
- **Better performance** - Easier for React to optimize
- **Industry standard** - What everyone uses now

### Component Hierarchy and Architecture

#### Building Component Trees
React applications are built as **trees of components**:

```
App
├── Header
├── Buttons
├── BalanceCards
│   ├── BalanceCard (Balance)
│   └── BalanceCard (Price)
└── MainContent
    ├── Transactions
    └── Chart
```

#### Planning Our Wallet Structure
For our Lightning wallet, we'll create:
- **App** - Main component that holds everything
- **Buttons** - Send/Receive functionality
- **BalanceCards** - Display balance and Bitcoin price
- **Transactions** - List of Lightning payments
- **Chart** - Real-time price visualization
- **PaymentsModal** - Send/receive Lightning payments

## React Syntax & Data Flow
<chapterId>8741a311-7a6c-4268-b9fe-e2b1d64a59d1</chapterId>

### JSX: HTML in JavaScript

JSX lets you write HTML-like syntax directly in JavaScript:

```jsx
// JSX (what you write)
const greeting = <h1>Hello, Bitcoin developers!</h1>;

// JavaScript (what it becomes)
const greeting = React.createElement('h1', null, 'Hello, Bitcoin developers!');
```

#### JSX Differences from HTML
```jsx
// className instead of class
<div className="wallet-container">

// camelCase event handlers
<button onClick={handleClick}>

// Self-closing tags need /
<img src="bitcoin.png" />

// JavaScript expressions in {}
<p>Price: ${price}</p>
```

### Props: Passing Data Between Components

#### What Are Props?
Props (properties) are how we pass data from parent to child components:

```jsx
// Parent component
function App() {
    const [price, setPrice] = useState(50000);
    return <PriceDisplay price={price} />;
}

// Child component
function PriceDisplay({ price }) {
    return <div>Bitcoin: ${price}</div>;
}
```

#### Props Flow Rules
- **One-way flow** - Data only flows down (parent → child)
- **Read-only** - Child components cannot modify props
- **Any data type** - Strings, numbers, objects, arrays, functions

#### Prop Destructuring
```jsx
// Method 1: Props object
function Header(props) {
    return <h1>{props.title}</h1>;
}

// Method 2: Destructuring (preferred)
function Header({ title }) {
    return <h1>{title}</h1>;
}
```

### React Hooks: Powerful State Management

#### useState Hook: Managing Component State
State allows components to remember and change data:

```jsx
import { useState } from 'react';

function BitcoinPrice() {
    // [currentValue, setterFunction] = useState(initialValue)
    const [price, setPrice] = useState(0);
    const [loading, setLoading] = useState(true);
    
    const updatePrice = () => {
        setPrice(50000);
        setLoading(false);
    };
    
    return (
        <div>
            {loading ? 'Loading...' : `Price: $${price}`}
            <button onClick={updatePrice}>Update Price</button>
        </div>
    );
}
```

**State Rules:**
- **Always use setter function** - Never modify state directly
- **State updates trigger re-renders** - UI automatically updates
- **State is local** - Each component instance has its own state

#### useEffect Hook: Side Effects and Lifecycle

useEffect handles operations that happen **outside** of rendering:

```jsx
import { useState, useEffect } from 'react';

function BitcoinPrice() {
    const [price, setPrice] = useState(0);
    
    useEffect(() => {
        // This runs after component mounts
        fetchBitcoinPrice().then(setPrice);
        
        // Set up interval for real-time updates
        const interval = setInterval(() => {
            fetchBitcoinPrice().then(setPrice);
        }, 5000);
        
        // Cleanup function (prevents memory leaks)
        return () => clearInterval(interval);
    }, []); // Empty array = run once on mount
    
    return <div>Price: ${price}</div>;
}
```

#### useEffect Dependency Array
Controls **when** the effect runs:

```jsx
// No dependency array - runs on every render
useEffect(() => {
    console.log('Runs every render');
});

// Empty array - runs once on mount
useEffect(() => {
    console.log('Runs once on mount');
}, []);

// With dependencies - runs when dependencies change
useEffect(() => {
    console.log('Runs when price changes');
}, [price]);
```

## Building Our Lightning Wallet in React
<chapterId>409ef049-7b10-4dd1-97a3-45ac12fad6c7</chapterId>

### Project Setup & Environment
Starting from our Create React App foundation:

```bash
## Navigate to your project
cd pleb-wallet-react

## Install additional dependencies
npm install axios react-modal react-linechart

## Start development server
npm start
```

#### App.js - Main Component Structure
```jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Buttons from './components/Buttons';
import Transactions from './components/Transactions';
import Chart from './components/Chart';
import PaymentsModal from './components/PaymentsModal';
import './App.css';

function App() {
    // State for Bitcoin price and wallet data
    const [price, setPrice] = useState(null);
    const [balance, setBalance] = useState(null);
    const [transactions, setTransactions] = useState([]);
    const [chartData, setChartData] = useState(null);
    const [modalState, setModalState] = useState({
        type: "",
        open: false,
    });

    // API functions
    const getPrice = () => {
        axios
            .get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
            .then((res) => {
                setPrice(res.data.data.amount);
                updateChartData(res.data.data.amount);
            })
            .catch((err) => console.log(err));
    };

    const getWalletBalance = () => {
        const headers = {
            "X-Api-Key": "your-api-key-here",
        };
        axios
            .get("https://legend.lnbits.com/api/v1/wallet", { headers })
            .then((res) => {
                setBalance(res.data.balance / 1000); // Convert from millisats
            })
            .catch((err) => console.log(err));
    };

    const getTransactions = () => {
        const headers = {
            "X-Api-Key": "your-api-key-here",
        };
        axios
            .get("https://legend.lnbits.com/api/v1/payments", { headers })
            .then((res) => {
                setTransactions(res.data);
            })
            .catch((err) => console.log(err));
    };

    const updateChartData = (currentPrice) => {
        const timestamp = Date.now();
        setChartData((prevState) => {
            if (!prevState) {
                return [{
                    x: timestamp,
                    y: Number(currentPrice),
                }];
            }
            
            // Don't add duplicate data points
            if (prevState[prevState.length - 1].y === Number(currentPrice)) {
                return prevState;
            }
            
            return [
                ...prevState,
                {
                    x: timestamp,
                    y: Number(currentPrice),
                }
            ];
        });
    };

    // Initial data fetch
    useEffect(() => {
        getPrice();
        getWalletBalance();
        getTransactions();
    }, []);

    // Real-time updates every 5 seconds
    useEffect(() => {
        const interval = setInterval(() => {
            getPrice();
            getWalletBalance();
            getTransactions();
        }, 5000);
        
        return () => clearInterval(interval);
    }, []);

    return (
        <div className="App">
            <header>
                <h1>pleb wallet</h1>
            </header>
            
            <Buttons modalState={modalState} setModalState={setModalState} />
            
            <div className="row">
                <div className="balance-card">
                    <h2>Balance</h2>
                    <p>{balance} sats</p>
                </div>
                <div className="balance-card">
                    <h2>Price</h2>
                    <p>${price}</p>
                </div>
            </div>
            
            <div className="row">
                <div className="row-item">
                    <Transactions transactions={transactions} />
                </div>
                <div className="row-item">
                    <Chart chartData={chartData} />
                </div>
            </div>
            
            <PaymentsModal 
                modalState={modalState} 
                setModalState={setModalState} 
            />
            
            <footer>
                <p>Made by plebs, for plebs.</p>
            </footer>
        </div>
    );
}

export default App;
```

#### Buttons Component
```jsx
import React from "react";
import "./Buttons.css";

const Buttons = ({ modalState, setModalState }) => {
    const handleSendClick = () => {
        setModalState({ open: true, type: "send" });
    };

    const handleReceiveClick = () => {
        setModalState({ open: true, type: "receive" });
    };

    return (
        <div className="buttons">
            <button className="button" onClick={handleSendClick}>
                Send
            </button>
            <button className="button" onClick={handleReceiveClick}>
                Receive
            </button>
        </div>
    );
};

export default Buttons;
```

#### Transactions Component
```jsx
import React from "react";
import "./Transactions.css";

const Transactions = ({ transactions }) => {
    const parseTx = (tx) => {
        const date = new Date(tx.time * 1000);
        const formattedDate = date.toLocaleDateString("en-US");
        
        // Skip pending transactions
        if (tx.pending) return null;

        if (tx.amount > 0) {
            return (
                <div key={tx.checking_id} className="tx-item">
                    <p>Received from {tx.bolt11.substring(0, 25)}...</p>
                    <p>+{tx.amount / 1000} sats</p>
                    <p className="transaction-date">{formattedDate}</p>
                </div>
            );
        }

        if (tx.amount < 0) {
            return (
                <div key={tx.checking_id} className="tx-item">
                    <p>Sent with {tx.bolt11.substring(0, 25)}...</p>
                    <p>{tx.amount / 1000} sats</p>
                    <p className="transaction-date">{formattedDate}</p>
                </div>
            );
        }
    };

    return (
        <div>
            <h3>Transactions</h3>
            {transactions.map((transaction) => parseTx(transaction))}
        </div>
    );
};

export default Transactions;
```

#### Chart Component
```jsx
import React from "react";
import LineChart from "react-linechart";
import "../../node_modules/react-linechart/dist/styles.css";
import "./Chart.css";

const Chart = ({ chartData }) => {
    if (!chartData || !chartData.length) return null;

    const data = [
        {
            color: "steelblue",
            points: chartData,
        },
    ];

    return (
        <div className="chart-container">
            {chartData.length <= 1 ? (
                <p>Loading chart...</p>
            ) : (
                <LineChart
                    xLabel="Time"
                    height={300}
                    width={550}
                    data={data}
                    onPointHover={(obj) => `price: $${obj.y}<br />time: ${obj.x}`}
                    ticks={4}
                    hideYLabel={true}
                    hideXLabel={true}
                    xDisplay={(timestamp) =>
                        new Date(timestamp).toLocaleTimeString("en-US")
                    }
                />
            )}
        </div>
    );
};

export default Chart;
```

#### PaymentsModal Component
```jsx
import React, { useState } from "react";
import Modal from "react-modal";
import axios from "axios";
import "./PaymentsModal.css";

const customStyles = {
    content: {
        top: "20%",
        left: "40%",
        right: "40%",
        bottom: "auto",
    },
};

const PaymentsModal = ({ modalState, setModalState }) => {
    const [formData, setFormData] = useState({
        amount: 0,
        invoiceToPay: "",
    });
    const [invoice, setInvoice] = useState("");
    const [paymentInfo, setPaymentInfo] = useState({
        paymentHash: "",
        checkingId: "",
    });

    const handleSend = (e) => {
        e.preventDefault();
        const headers = {
            "X-Api-Key": "your-api-key-here",
        };
        const data = {
            bolt11: formData.invoiceToPay,
            out: true,
        };
        
        axios
            .post("https://legend.lnbits.com/api/v1/payments", data, { headers })
            .then((res) =>
                setPaymentInfo({
                    paymentHash: res.data.payment_hash,
                    checkingId: res.data.checking_id,
                })
            )
            .catch((err) => console.log(err));
    };

    const handleReceive = (e) => {
        e.preventDefault();
        const headers = {
            "X-Api-Key": "your-api-key-here",
        };
        const data = {
            amount: formData.amount,
            out: false,
            memo: "LNBits",
        };
        
        axios
            .post("https://legend.lnbits.com/api/v1/payments", data, { headers })
            .then((res) => setInvoice(res.data.payment_request))
            .catch((err) => console.log(err));
    };

    const clearForms = () => {
        setModalState({ type: "", open: false });
        setInvoice("");
        setPaymentInfo({ paymentHash: "", checkingId: "" });
        setFormData({ amount: 0, invoiceToPay: "" });
    };

    return (
        <Modal
            isOpen={modalState.open}
            style={customStyles}
            contentLabel="Payments Modal"
            appElement={document.getElementById("root")}
        >
            <p className="close-button" onClick={clearForms}>
                X
            </p>
            
            {modalState.type === "send" && (
                <form>
                    <label>Paste an invoice</label>
                    <input
                        type="text"
                        value={formData.invoiceToPay}
                        onChange={(e) =>
                            setFormData({ ...formData, invoiceToPay: e.target.value })
                        }
                    />
                    <button className="button" onClick={handleSend}>
                        Submit
                    </button>
                </form>
            )}
            
            {modalState.type === "receive" && (
                <form>
                    <label>Enter amount</label>
                    <input
                        type="number"
                        min="0"
                        value={formData.amount}
                        onChange={(e) =>
                            setFormData({ ...formData, amount: e.target.value })
                        }
                    />
                    <button className="button" onClick={handleReceive}>
                        Submit
                    </button>
                </form>
            )}
            
            {invoice && (
                <section>
                    <h3>Invoice created</h3>
                    <p>{invoice}</p>
                </section>
            )}
            
            {paymentInfo.paymentHash && (
                <section>
                    <h3>Payment sent</h3>
                    <p>Payment hash: {paymentInfo.paymentHash}</p>
                    <p>Checking id: {paymentInfo.checkingId}</p>
                </section>
            )}
        </Modal>
    );
};

export default PaymentsModal;
```

### Understanding Callback Functions

#### What Are Callbacks?
A callback is a **function passed into another function** to be called at the appropriate time:

```jsx
// Higher-order function that accepts a callback
function fetchData(callback) {
    // Simulate API call
    setTimeout(() => {
        const data = { price: 50000 };
        callback(data); // Call the callback with data
    }, 1000);
}

// Using the callback
fetchData((data) => {
    console.log('Price received:', data.price);
});
```

#### Why Callbacks Matter
Callbacks handle **timing and asynchronous operations**:
- **API calls** - Don't know when they'll complete
- **User interactions** - Don't know when users will click
- **Timers** - Need to run code at specific times

#### Callbacks in React
```jsx
// Event handler callback
<button onClick={(e) => handleClick(e)}>

// useEffect callback
useEffect(() => {
    // This function is a callback
    fetchData();
}, []);

// Array method callbacks
transactions.map((tx) => <div key={tx.id}>{tx.amount}</div>)
```

### Package Management with NPM

#### Installing Packages
```bash
## Install a package for your project
npm install axios                  # HTTP client
npm install react-modal            # Modal dialogs
npm install react-linechart        # Charts
```

#### Using Installed Packages
```jsx
// Import and use packages
import axios from 'axios';
import Modal from 'react-modal';
import LineChart from 'react-linechart';

// Use them in your components
const response = await axios.get('/api/data');
```

#### Managing Dependencies
```json
// package.json automatically updated
{
  "dependencies": {
    "axios": "^1.6.0",
    "react": "^18.2.0",
    "react-modal": "^3.16.1",
    "react-linechart": "^1.3.1"
  }
}
```

### Styling in React

#### CSS Modules and Component Styling
Each component has its own CSS file:

```css
/* Buttons.css */
.buttons {
    width: 50%;
    margin: 0 auto;
    margin-top: 3%;
    display: flex;
    justify-content: space-around;
}

.button {
    background-color: #ffbf46;
    border: 2px solid #8a4fff;
    border-radius: 5px;
    padding: 5px;
    font-size: 1.2rem;
    font-family: monospace;
    font-weight: bold;
    width: 100px;
}

.button:hover {
    cursor: pointer;
    opacity: 0.6;
}
```

#### Responsive Design
```css
/* Mobile-first responsive design */
@media (max-width: 876px) {
    .row-item {
        width: 100%;
        height: 200px;
    }

    .balance-card {
        width: 100%;
        text-align: center;
        margin-right: 2%;
        margin-left: 2%;
    }
}

@media (max-width: 615px) {
    .row {
        flex-direction: column;
    }

    .balance-card {
        width: 80%;
        margin: 0 auto;
        margin-top: 1%;
    }
}
```

### Lightning Network Integration

#### LNbits API Integration
Our wallet integrates with LNbits for Lightning functionality:

```jsx
// Wallet configuration
const LNBITS_URL = "https://legend.lnbits.com";
const API_KEY = "your-api-key-here"; // Store securely in production

// API headers
const headers = {
    "X-Api-Key": API_KEY,
};

// Get wallet balance
const getBalance = async () => {
    const response = await axios.get(`${LNBITS_URL}/api/v1/wallet`, { headers });
    return response.data.balance / 1000; // Convert from millisats
};

// Create Lightning invoice
const createInvoice = async (amount, memo) => {
    const data = { amount, out: false, memo };
    const response = await axios.post(`${LNBITS_URL}/api/v1/payments`, data, { headers });
    return response.data.payment_request;
};

// Pay Lightning invoice
const payInvoice = async (bolt11) => {
    const data = { bolt11, out: true };
    const response = await axios.post(`${LNBITS_URL}/api/v1/payments`, data, { headers });
    return response.data;
};
```

#### Real-time Updates
```jsx
// Update wallet data every 5 seconds
useEffect(() => {
    const interval = setInterval(() => {
        getPrice();
        getWalletBalance();
        getTransactions();
    }, 5000);
    
    return () => clearInterval(interval);
}, []);
```



## Deployment of Our Lightning Wallet & Career Path
<chapterId>8a5b9a90-6580-4ca6-a747-81b2546b465b</chapterId>

### Deployment and Production

#### Building for Production
```bash
## Create optimized production build
npm run build

## This creates a 'build' folder with optimized files
```

#### Environment Variables
Store sensitive data like API keys:

```bash
## .env file (never commit to Git)
REACT_APP_LNBITS_URL=https://legend.lnbits.com
REACT_APP_API_KEY=your-secret-key
```

```jsx
// Use in your app
const apiKey = process.env.REACT_APP_API_KEY;
const lnbitsUrl = process.env.REACT_APP_LNBITS_URL;
```

#### Deployment to Vercel
```bash
## Push to GitHub
git add .
git commit -m "Complete React wallet implementation"
git push origin main

## Vercel automatically builds and deploys
```

### Hands-on Exercises

#### Exercise 1: Component Creation Practice
Create additional wallet components:

1. **WalletStats Component**
   ```jsx
   // Display wallet statistics
   - Total transactions
   - Average transaction amount
   - Wallet age
   - Favorite payment memo
   ```

2. **QRCode Component**
   ```jsx
   // Generate QR codes for Lightning invoices
   npm install qrcode.react
   // Display QR code in PaymentsModal
   ```

3. **Settings Component**
   ```jsx
   // Wallet settings
   - Currency display (sats/BTC/USD)
   - Update frequency
   - Theme selection
   ```

#### Exercise 2: Advanced State Management
Enhance the wallet with more sophisticated state:

1. **Local Storage Persistence**
   ```jsx
   // Save settings to localStorage
   useEffect(() => {
       const savedSettings = localStorage.getItem('walletSettings');
       if (savedSettings) {
           setSettings(JSON.parse(savedSettings));
       }
   }, []);
   ```

2. **Error Handling**
   ```jsx
   // Add error states and retry logic
   const [error, setError] = useState(null);
   const [retryCount, setRetryCount] = useState(0);
   ```

3. **Loading States**
   ```jsx
   // Better loading indicators
   const [loading, setLoading] = useState({
       price: false,
       balance: false,
       transactions: false
   });
   ```

#### Exercise 3: Enhanced Features
Add new wallet capabilities:

1. **Transaction Filtering**
   ```jsx
   // Filter transactions by:
   - Date range
   - Amount range
   - Payment type (sent/received)
   ```

2. **Export Functionality**
   ```jsx
   // Export transaction history
   - CSV format
   - JSON format
   - PDF reports
   ```

3. **Multiple Wallets**
   ```jsx
   // Support multiple LNbits wallets
   - Wallet switching
   - Combined balance view
   - Wallet comparison
   ```

#### Exercise 4: Performance Optimization
Optimize your React wallet:

1. **Memoization**
   ```jsx
   import { useMemo, useCallback } from 'react';
   
   // Memoize expensive calculations
   const expensiveValue = useMemo(() => {
       return calculateComplexStats(transactions);
   }, [transactions]);
   ```

2. **Component Optimization**
   ```jsx
   import { memo } from 'react';
   
   // Prevent unnecessary re-renders
   const TransactionItem = memo(({ transaction }) => {
       return <div>{transaction.amount}</div>;
   });
   ```

3. **Code Splitting**
   ```jsx
   import { lazy, Suspense } from 'react';
   
   // Lazy load heavy components
   const Chart = lazy(() => import('./components/Chart'));
   ```

### Common React Patterns and Best Practices

#### State Management Best Practices
```jsx
// ✅ Good: Keep state as local as possible
function TransactionList({ transactions }) {
    const [filter, setFilter] = useState('all');
    // Filter only affects this component
}

// ❌ Avoid: Lifting state unnecessarily
function App() {
    const [filter, setFilter] = useState('all'); // Too high in tree
}
```

#### Effect Dependencies
```jsx
// ✅ Good: Include all dependencies
useEffect(() => {
    fetchTransactions(walletId, currency);
}, [walletId, currency]);

// ❌ Avoid: Missing dependencies
useEffect(() => {
    fetchTransactions(walletId, currency);
}, []); // Missing walletId, currency
```

#### Component Organization
```jsx
// ✅ Good: Single responsibility
function BitcoinPrice({ price }) {
    return <div>Bitcoin: ${price}</div>;
}

// ❌ Avoid: Too many responsibilities
function WalletDashboard() {
    // 500 lines of code doing everything
}
```

#### Error Boundaries
```jsx
class ErrorBoundary extends React.Component {
    constructor(props) {
        super(props);
        this.state = { hasError: false };
    }

    static getDerivedStateFromError(error) {
        return { hasError: true };
    }

    render() {
        if (this.state.hasError) {
            return <h1>Something went wrong with the wallet.</h1>;
        }

        return this.props.children;
    }
}

// Wrap your app
<ErrorBoundary>
    <App />
</ErrorBoundary>
```

### Testing Your React Wallet

#### Basic Component Testing
```jsx
import { render, screen } from '@testing-library/react';
import BitcoinPrice from './BitcoinPrice';

test('displays bitcoin price', () => {
    render(<BitcoinPrice price={50000} />);
    expect(screen.getByText('Bitcoin: $50000')).toBeInTheDocument();
});
```

#### Testing Hooks
```jsx
import { renderHook, act } from '@testing-library/react';
import { useState } from 'react';

test('wallet balance updates correctly', () => {
    const { result } = renderHook(() => useState(0));
    
    act(() => {
        result.current[1](1000); // setBalance(1000)
    });
    
    expect(result.current[0]).toBe(1000);
});
```

#### Integration Testing
```jsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import App from './App';

test('can create lightning invoice', async () => {
    render(<App />);
    
    fireEvent.click(screen.getByText('Receive'));
    fireEvent.change(screen.getByLabelText('Enter amount'), {
        target: { value: '1000' }
    });
    fireEvent.click(screen.getByText('Submit'));
    
    await waitFor(() => {
        expect(screen.getByText('Invoice created')).toBeInTheDocument();
    });
});
```

### The Bitcoin Developer Journey

#### Learning Resources & Advanced Topics

**React Documentation**
- **[React.dev](https://react.dev/)** - Official React documentation with interactive examples
- **[React Hooks Reference](https://react.dev/reference/react)** - Complete hooks documentation
- **[React Patterns](https://reactpatterns.com/)** - Common patterns and best practices

**React Learning Paths**
- **[React Tutorial](https://react.dev/learn)** - Step-by-step interactive tutorial
- **[FreeCodeCamp React Course](https://www.freecodecamp.org/learn/front-end-development-libraries/)** - Comprehensive free course
- **[React TypeScript Cheatsheet](https://react-typescript-cheatsheet.netlify.app/)** - For adding TypeScript

**Lightning Development**
- **[LNbits Documentation](https://lnbits.com/)** - Lightning wallet and account system
- **[Lightning Network Paper](https://lightning.network/lightning-network-paper.pdf)** - Understanding Lightning Network
- **[Bitcoin Development Guide](https://developer.bitcoin.org/)** - Official Bitcoin development resources

**Development Tools**
- **[React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/)** - Browser extension for debugging
- **[Axios Documentation](https://axios-http.com/)** - HTTP client for API calls
- **[React Modal](https://reactcommunity.org/react-modal/)** - Modal component documentation

#### Immediate Next Steps
1. **Complete the wallet project** - Implement all features from the lesson
2. **Deploy to production** - Get your wallet live on the internet
3. **Add error handling** - Make your wallet robust and user-friendly
4. **Implement testing** - Add unit and integration tests
5. **Share your work** - Show the Bitcoin community what you built

#### Advanced React Topics
- **Context API** - Global state management
- **React Router** - Multi-page applications
- **Server-Side Rendering** - Next.js framework
- **React Native** - Mobile app development
- **Performance Optimization** - Profiling and optimization techniques

#### Lightning Development Path
- **Watchtower Implementation** - Lightning security features
- **Multi-signature Wallets** - Enhanced security
- **Lightning Service Provider** - Channel management
- **BTCPay Server Integration** - Merchant payment processing
- **Lightning Node Management** - Running your own node

#### Career Development
- **Build Portfolio Projects** - Create multiple Lightning applications
- **Contribute to Open Source** - Lightning protocol implementations
- **Join Bitcoin Companies** - Companies building on Lightning
- **Start Your Own Project** - Lightning-powered business ideas
- **Teach Others** - Share knowledge with the Bitcoin community

#### Key Takeaways

1. **React transforms development** - Component-based architecture scales much better than vanilla JavaScript
2. **State management is crucial** - useState and useEffect are the foundation of dynamic React apps
3. **Component hierarchy matters** - Plan your component tree before building
4. **Props flow down only** - Data flows from parent to child components
5. **Hooks enable powerful features** - Modern React is built on functional components and hooks
6. **Lightning integration is straightforward** - LNbits makes Lightning development accessible
7. **Real-time updates enhance UX** - Users expect live data in Bitcoin applications
8. **Package management saves time** - npm ecosystem provides solutions for common needs
9. **Testing ensures reliability** - Critical for handling real Bitcoin transactions
10. **Deployment should be automatic** - Continuous deployment from GitHub to production

Congratulations! You've built a fully functional Lightning wallet using React. You now understand modern frontend development and can build sophisticated Bitcoin applications. The skills you've learned here are directly applicable to working at Bitcoin companies and building your own Lightning-powered projects.

This React wallet is just the beginning. You can now extend it with advanced features, integrate with other Lightning services, or use these skills to build entirely new Bitcoin applications. Welcome to the world of Bitcoin development! ⚡️🧡

---

#### What's Next?

In the final lesson (Lesson 6), you'll learn:
- **Advanced React patterns** - Context API, custom hooks, performance optimization
- **Production deployment strategies** - Environment variables, monitoring, scaling
- **Security best practices** - Protecting user funds and data
- **Lightning Network deep dive** - Advanced Lightning concepts and implementations
- **Career guidance** - Building your portfolio and finding Bitcoin development opportunities

The journey to becoming a Bitcoin developer continues! 🚀 

## Designing for Lightning: Architecture & Setup
<chapterId>3f282c6a-37b8-4532-80cf-98471f074101</chapterId>

### Why React for Lightning Development

#### The Evolution from Vanilla JavaScript
Our previous wallet worked, but had significant limitations:
- **Scattered architecture** - Logic spread across multiple files
- **Manual DOM updates** - Tedious and error-prone element manipulation
- **State synchronization issues** - Keeping UI in sync with changing data
- **Code duplication** - Repeating similar functionality
- **Debugging difficulties** - Hard to trace data flow and component interactions

#### React's Lightning-Powered Solution
React solves these problems with:
- **Component-based architecture** - Logical, reusable pieces of functionality
- **Automatic UI updates** - React handles DOM changes when data changes
- **Predictable data flow** - Props flow down, events flow up
- **Developer experience** - Excellent debugging tools and development workflow
- **Industry adoption** - Used by major Bitcoin companies like Coinbase, Kraken, and Lightning Labs

### React Component Hierarchy Planning

#### Understanding the Wallet Structure
Before building, let's plan our component tree:

```
App (Main wallet container)
├── Header (Wallet title)
├── Buttons (Send/Receive actions)
├── BalanceCards (Balance and Price display)
├── MainContent
│   ├── Transactions (Payment history)
│   └── Chart (Real-time Bitcoin price chart)
└── PaymentsModal (Send/Receive forms)
```

#### Data Flow Architecture
Understanding how data flows through our wallet:
- **App component** - Holds all state (price, balance, transactions, chart data)
- **Child components** - Receive data via props, send events via callbacks
- **State updates** - Trigger automatic re-renders throughout the component tree
- **API integration** - Centralized in App component, shared via props

### Building the React Lightning Wallet

#### Project Setup and Initial Structure

Starting with our Create React App foundation:

```bash
## Navigate to your project
cd pleb-wallet-frontend

## Install required dependencies
npm install axios react-modal react-linechart

## Start development server
npm start
```

#### App.js - The Heart of Our Wallet

Our main App component will manage all wallet state and functionality:

```jsx
import React, { useEffect, useState } from "react";
import axios from "axios";
import Buttons from "./components/Buttons";
import Transactions from "./components/Transactions";
import Chart from "./components/Chart";
import PaymentsModal from "./components/PaymentsModal";
import "./App.css";

function App() {
  // State for Bitcoin price and wallet data
  const [price, setPrice] = useState(null);
  const [balance, setBalance] = useState(null);
  const [transactions, setTransactions] = useState([]);
  const [chartData, setChartData] = useState(null);
  const [modalState, setModalState] = useState({
    type: "",
    open: false,
  });

  // API function to get Bitcoin price
  const getPrice = () => {
    axios
      .get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
      .then((res) => {
        setPrice(res.data.data.amount);
        updateChartData(res.data.data.amount);
      })
      .catch((err) => console.log(err));
  };

  // API function to get wallet balance from LNbits
  const getWalletBalance = () => {
    const headers = {
      "X-Api-Key": "your-api-key-here", // Replace with your LNbits API key
    };
    axios
      .get("https://legend.lnbits.com/api/v1/wallet", { headers })
      .then((res) => {
        setBalance(res.data.balance / 1000); // Convert from millisats
      })
      .catch((err) => console.log(err));
  };

  // API function to get transaction history
  const getTransactions = () => {
    const headers = {
      "X-Api-Key": "your-api-key-here", // Replace with your LNbits API key
    };
    axios
      .get("https://legend.lnbits.com/api/v1/payments", { headers })
      .then((res) => {
        setTransactions(res.data);
      })
      .catch((err) => console.log(err));
  };

  // Function to update chart data with new price points
  const updateChartData = (currentPrice) => {
    const timestamp = Date.now();
    setChartData((prevState) => {
      // If no previous data, create initial point
      if (!prevState) {
        return [{
          x: timestamp,
          y: Number(currentPrice),
        }];
      }
      
      // Don't add duplicate data points
      if (
        prevState[prevState.length - 1].x === timestamp ||
        prevState[prevState.length - 1].y === Number(currentPrice)
      ) {
        return prevState;
      }
      
      // Add new data point to existing array
      return [
        ...prevState,
        {
          x: timestamp,
          y: Number(currentPrice),
        }
      ];
    });
  };

  // Initial data fetch on component mount
  useEffect(() => {
    getPrice();
    getWalletBalance();
    getTransactions();
  }, []);

  // Set up real-time updates every 5 seconds
  useEffect(() => {
    const interval = setInterval(() => {
      getPrice();
      getWalletBalance();
      getTransactions();
    }, 5000);
    
    // Cleanup interval on component unmount
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="App">
      <header>
        <h1>pleb wallet</h1>
      </header>
      
      <Buttons modalState={modalState} setModalState={setModalState} />
      
      <div className="row">
        <div className="balance-card">
          <h2>Balance</h2>
          <p>{balance} sats</p>
        </div>
        <div className="balance-card">
          <h2>Price</h2>
          <p>${price}</p>
        </div>
      </div>
      
      <div className="row">
        <div className="row-item">
          <Transactions transactions={transactions} />
        </div>
        <div className="row-item">
          <Chart chartData={chartData} />
        </div>
      </div>
      
      <PaymentsModal 
        modalState={modalState} 
        setModalState={setModalState} 
      />
      
      <footer>
        <p>Made by plebs, for plebs.</p>
      </footer>
    </div>
  );
}

export default App;
```

#### Understanding React Hooks in Practice

##### useState for State Management
Each piece of dynamic data gets its own state:

```jsx
// Bitcoin price from Coinbase API
const [price, setPrice] = useState(null);

// Wallet balance from LNbits
const [balance, setBalance] = useState(null);

// Transaction history array
const [transactions, setTransactions] = useState([]);

// Chart data points for price visualization
const [chartData, setChartData] = useState(null);

// Modal state for send/receive dialogs
const [modalState, setModalState] = useState({
  type: "",
  open: false,
});
```

##### useEffect for Side Effects
Managing when and how our effects run:

```jsx
// Run once on component mount
useEffect(() => {
  getPrice();
  getWalletBalance();
  getTransactions();
}, []); // Empty dependency array = run once

// Run repeatedly every 5 seconds
useEffect(() => {
  const interval = setInterval(() => {
    getPrice();
    getWalletBalance();
    getTransactions();
  }, 5000);
  
  // Cleanup function prevents memory leaks
  return () => clearInterval(interval);
}, []); // Empty dependency = set up once, cleanup on unmount
```

#### Building the Buttons Component

Creating reusable UI components with clear responsibilities:

```jsx
// components/Buttons.js
import React from "react";
import "./Buttons.css";

const Buttons = ({ modalState, setModalState }) => {
  const handleSendClick = () => {
    setModalState({ open: true, type: "send" });
  };

  const handleReceiveClick = () => {
    setModalState({ open: true, type: "receive" });
  };

  return (
    <div className="buttons">
      <button className="button" onClick={handleSendClick}>
        Send
      </button>
      <button className="button" onClick={handleReceiveClick}>
        Receive
      </button>
    </div>
  );
};

export default Buttons;
```

##### Buttons Component Styles
```css
/* components/Buttons.css */
.buttons {
  width: 50%;
  margin: 0 auto;
  margin-top: 3%;
  display: flex;
  justify-content: space-around;
}

.button {
  background-color: #ffbf46;
  border: 2px solid #8a4fff;
  border-radius: 5px;
  padding: 5px;
  font-size: 1.2rem;
  font-family: monospace;
  font-weight: bold;
  width: 100px;
}

.button:hover {
  cursor: pointer;
  opacity: 0.6;
}
```

#### Building the Transactions Component

Displaying and parsing Lightning transaction data:

```jsx
// components/Transactions.js
import React from "react";
import "./Transactions.css";

const Transactions = ({ transactions }) => {
  const parseTx = (tx) => {
    const date = new Date(tx.time * 1000);
    const formattedDate = date.toLocaleDateString("en-US");
    
    // Skip pending transactions
    if (tx.pending) return null;

    // Handle received payments
    if (tx.amount > 0) {
      return (
        <div key={tx.checking_id} className="tx-item">
          <p>Received from {tx.bolt11.substring(0, 25)}...</p>
          <p>+{tx.amount / 1000} sats</p>
          <p className="transaction-date">{formattedDate}</p>
        </div>
      );
    }

    // Handle sent payments
    if (tx.amount < 0) {
      return (
        <div key={tx.checking_id} className="tx-item">
          <p>Sent with {tx.bolt11.substring(0, 25)}...</p>
          <p>{tx.amount / 1000} sats</p>
          <p className="transaction-date">{formattedDate}</p>
        </div>
      );
    }
  };

  return (
    <div>
      <h3>Transactions</h3>
      {transactions.map((transaction) => parseTx(transaction))}
    </div>
  );
};

export default Transactions;
```

#### Building the Chart Component

Real-time Bitcoin price visualization:

```jsx
// components/Chart.js
import React from "react";
import LineChart from "react-linechart";
import "../../node_modules/react-linechart/dist/styles.css";
import "./Chart.css";

const Chart = ({ chartData }) => {
  // Don't render if no data
  if (!chartData || !chartData.length) return null;

  const data = [
    {
      color: "steelblue",
      points: chartData,
    },
  ];

  return (
    <div className="chart-container">
      {chartData.length <= 1 ? (
        <p>Loading chart...</p>
      ) : (
        <LineChart
          xLabel="Time"
          height={300}
          width={550}
          data={data}
          onPointHover={(obj) => `price: $${obj.y}<br />time: ${obj.x}`}
          ticks={4}
          hideYLabel={true}
          hideXLabel={true}
          xDisplay={(timestamp) =>
            new Date(timestamp).toLocaleTimeString("en-US")
          }
        />
      )}
    </div>
  );
};

export default Chart;
```

#### Building the PaymentsModal Component

Complex modal for Lightning payments:

```jsx
// components/PaymentsModal.js
import React, { useState } from "react";
import Modal from "react-modal";
import axios from "axios";
import "./PaymentsModal.css";

const customStyles = {
  content: {
    top: "20%",
    left: "40%",
    right: "40%",
    bottom: "auto",
  },
};

const PaymentsModal = ({ modalState, setModalState }) => {
  // Form data for sending/receiving
  const [formData, setFormData] = useState({
    amount: 0,
    invoiceToPay: "",
  });
  
  // Generated invoice for receiving
  const [invoice, setInvoice] = useState("");
  
  // Payment confirmation data
  const [paymentInfo, setPaymentInfo] = useState({
    paymentHash: "",
    checkingId: "",
  });

  // Handle sending Lightning payments
  const handleSend = (e) => {
    e.preventDefault();
    
    const headers = {
      "X-Api-Key": "your-api-key-here",
    };
    const data = {
      bolt11: formData.invoiceToPay,
      out: true,
    };
    
    axios
      .post("https://legend.lnbits.com/api/v1/payments", data, { headers })
      .then((res) =>
        setPaymentInfo({
          paymentHash: res.data.payment_hash,
          checkingId: res.data.checking_id,
        })
      )
      .catch((err) => console.log(err));
  };

  // Handle creating Lightning invoices
  const handleReceive = (e) => {
    e.preventDefault();
    
    const headers = {
      "X-Api-Key": "your-api-key-here",
    };
    const data = {
      amount: formData.amount,
      out: false,
      memo: "LNBits",
    };
    
    axios
      .post("https://legend.lnbits.com/api/v1/payments", data, { headers })
      .then((res) => setInvoice(res.data.payment_request))
      .catch((err) => console.log(err));
  };

  // Clear all form state when modal closes
  const clearForms = () => {
    setModalState({ type: "", open: false });
    setInvoice("");
    setPaymentInfo({ paymentHash: "", checkingId: "" });
    setFormData({ amount: 0, invoiceToPay: "" });
  };

  return (
    <Modal
      isOpen={modalState.open}
      style={customStyles}
      contentLabel="Payments Modal"
      appElement={document.getElementById("root")}
    >
      <p className="close-button" onClick={clearForms}>
        X
      </p>
      
      {/* Send payment form */}
      {modalState.type === "send" && (
        <form>
          <label>Paste an invoice</label>
          <input
            type="text"
            value={formData.invoiceToPay}
            onChange={(e) =>
              setFormData({ ...formData, invoiceToPay: e.target.value })
            }
          />
          <button className="button" onClick={handleSend}>
            Submit
          </button>
        </form>
      )}
      
      {/* Receive payment form */}
      {modalState.type === "receive" && (
        <form>
          <label>Enter amount</label>
          <input
            type="number"
            min="0"
            value={formData.amount}
            onChange={(e) =>
              setFormData({ ...formData, amount: e.target.value })
            }
          />
          <button className="button" onClick={handleReceive}>
            Submit
          </button>
        </form>
      )}
      
      {/* Display generated invoice */}
      {invoice && (
        <section>
          <h3>Invoice created</h3>
          <p>{invoice}</p>
        </section>
      )}
      
      {/* Display payment confirmation */}
      {paymentInfo.paymentHash && (
        <section>
          <h3>Payment sent</h3>
          <p>Payment hash: {paymentInfo.paymentHash}</p>
          <p>Checking id: {paymentInfo.checkingId}</p>
        </section>
      )}
    </Modal>
  );
};

export default PaymentsModal;
```

### Advanced React Concepts

#### Callback Functions and Event Handling

Understanding how React components communicate:

```jsx
// Parent component passes callback to child
<Buttons 
  modalState={modalState} 
  setModalState={setModalState}  // This is a callback
/>

// Child component calls the callback
const handleSendClick = () => {
  setModalState({ open: true, type: "send" });  // Calling parent's callback
};
```

#### State Updates and Functional Updates

Complex state updates using previous state:

```jsx
// Functional update for complex state changes
setChartData((prevState) => {
  if (!prevState) {
    return [{ x: timestamp, y: Number(currentPrice) }];
  }
  
  return [
    ...prevState,  // Spread operator to copy existing data
    { x: timestamp, y: Number(currentPrice) }  // Add new data point
  ];
});
```

#### Prop Destructuring and Component Props

Clean ways to handle props in components:

```jsx
// Method 1: Props object
function Transactions(props) {
  return <div>{props.transactions.map(...)}</div>;
}

// Method 2: Destructuring (preferred)
function Transactions({ transactions }) {
  return <div>{transactions.map(...)}</div>;
}

// Method 3: Multiple props destructuring
function PaymentsModal({ modalState, setModalState }) {
  // Clean access to multiple props
}
```

#### Package Management with NPM

#### Installing and Managing Dependencies

```bash
## Install a package and save to package.json
npm install axios
npm install react-modal
npm install react-linechart

## Install development dependencies
npm install --save-dev eslint

## Install specific version
npm install react@18.2.0

## Update packages
npm update

## Check for vulnerabilities
npm audit
```

#### Understanding package.json

```json
{
  "name": "pleb-wallet-frontend",
  "version": "1.0.0",
  "dependencies": {
    "axios": "^1.6.0",
    "react": "^18.2.0",
    "react-modal": "^3.16.1",
    "react-linechart": "^1.3.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test"
  }
}
```

## Lightning Network Integration Deep Dive
<chapterId>330b4bc6-b62c-40f7-a844-b032d8411242</chapterId>

### LNbits API Integration

Complete API integration for Lightning functionality:

```jsx
// Configuration constants
const LNBITS_URL = "https://legend.lnbits.com";
const API_KEY = process.env.REACT_APP_API_KEY; // Use environment variables

// Helper function for API headers
const getHeaders = () => ({
  "X-Api-Key": API_KEY,
  "Content-Type": "application/json"
});

// Get wallet balance
const getWalletBalance = async () => {
  try {
    const response = await axios.get(
      `${LNBITS_URL}/api/v1/wallet`, 
      { headers: getHeaders() }
    );
    return response.data.balance / 1000; // Convert from millisats
  } catch (error) {
    console.error("Error fetching balance:", error);
    throw error;
  }
};

// Create Lightning invoice
const createInvoice = async (amount, memo = "LNbits") => {
  try {
    const data = { amount, out: false, memo };
    const response = await axios.post(
      `${LNBITS_URL}/api/v1/payments`, 
      data, 
      { headers: getHeaders() }
    );
    return response.data.payment_request;
  } catch (error) {
    console.error("Error creating invoice:", error);
    throw error;
  }
};

// Pay Lightning invoice
const payInvoice = async (bolt11) => {
  try {
    const data = { bolt11, out: true };
    const response = await axios.post(
      `${LNBITS_URL}/api/v1/payments`, 
      data, 
      { headers: getHeaders() }
    );
    return response.data;
  } catch (error) {
    console.error("Error paying invoice:", error);
    throw error;
  }
};
```

#### Error Handling and User Feedback

Implementing robust error handling:

```jsx
const [error, setError] = useState(null);
const [loading, setLoading] = useState(false);

const handlePayment = async (invoice) => {
  setLoading(true);
  setError(null);
  
  try {
    const result = await payInvoice(invoice);
    setPaymentInfo(result);
  } catch (error) {
    setError("Payment failed: " + error.message);
  } finally {
    setLoading(false);
  }
};

// In your JSX
{error && (
  <div className="error-message">
    {error}
  </div>
)}

{loading && (
  <div className="loading-spinner">
    Processing payment...
  </div>
)}
```

### Styling and Responsive Design

#### Complete App.css Styles

```css
/* App.css */
body {
  background-color: #192734;
  font-family: monospace;
}

header {
  border-bottom: 2px solid #ffbf46;
}

h1 {
  text-align: center;
  color: #8a4fff;
}

footer {
  border-top: 2px solid #ffbf46;
  padding: 1%;
  text-align: center;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
}

footer p {
  color: #8a4fff;
}

.balance-card {
  background-color: #ffbf46;
  border: 2px solid #8a4fff;
  padding: 1%;
  width: 25%;
  margin-top: 3%;
  margin-bottom: 1%;
  border-radius: 5px;
}

.balance-card p {
  font-size: 1.2rem;
  font-weight: bold;
}

.row {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.row-item {
  background-color: ghostwhite;
  border: 2px solid #8a4fff;
  border-radius: 5px;
  height: 300px;
  width: 40%;
  overflow: scroll;
}

/* Responsive design for mobile */
@media (max-width: 876px) {
  .row-item {
    width: 100%;
    height: 200px;
  }

  .balance-card {
    width: 100%;
    text-align: center;
    margin-right: 2%;
    margin-left: 2%;
  }
}

@media (max-width: 615px) {
  .row {
    flex-direction: column;
  }

  .row-item {
    margin-top: 1%;
  }

  .balance-card {
    width: 80%;
    margin: 0 auto;
    margin-top: 1%;
  }
}
```

#### Component-Specific Styling

Each component has its own CSS file for better organization:

```css
/* components/PaymentsModal.css */
form {
  margin: 2% auto;
  display: flex;
  flex-direction: column;
  text-align: center;
}

form input {
  margin: 10px 0;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

form .button {
  margin: 10% auto;
}

section h3 {
  text-align: center;
}

section p {
  word-wrap: break-word;
}

.close-button {
  cursor: pointer;
  text-align: end;
  font-weight: bold;
  font-size: 1.2rem;
}
```

### Testing Your React Wallet

#### Manual Testing Checklist

Before deploying, test all functionality:

1. **Initial Load**
   - [ ] Bitcoin price displays correctly
   - [ ] Wallet balance loads from LNbits
   - [ ] Transaction history appears
   - [ ] Chart initializes properly

2. **Real-time Updates**
   - [ ] Price updates every 5 seconds
   - [ ] Balance reflects new transactions
   - [ ] Chart adds new data points
   - [ ] No duplicate API calls

3. **Send Functionality**
   - [ ] Modal opens when Send clicked
   - [ ] Can paste Lightning invoice
   - [ ] Payment processes successfully
   - [ ] Payment confirmation displays
   - [ ] Balance updates after payment

4. **Receive Functionality**
   - [ ] Modal opens when Receive clicked
   - [ ] Can enter amount
   - [ ] Invoice generates correctly
   - [ ] QR code displays (if implemented)
   - [ ] Invoice can be paid externally

#### Debugging React Applications

Using React Developer Tools:

```jsx
// Add console logs for debugging
useEffect(() => {
  console.log('Price updated:', price);
  console.log('Chart data:', chartData);
}, [price, chartData]);

// Debug state changes
const handleSend = (e) => {
  console.log('Send clicked with data:', formData);
  // ... rest of function
};
```

### Environment Variables and Security

#### Securing API Keys

Never commit API keys to Git. Use environment variables:

```bash
## Create .env file in project root
REACT_APP_LNBITS_URL=https://legend.lnbits.com
REACT_APP_API_KEY=your-secret-api-key-here
```

```jsx
// Use in your React app
const apiKey = process.env.REACT_APP_API_KEY;
const lnbitsUrl = process.env.REACT_APP_LNBITS_URL;

if (!apiKey) {
  console.error('API key not found. Please set REACT_APP_API_KEY in .env file');
}
```

```gitignore
## Add to .gitignore
.env
.env.local
.env.development.local
.env.test.local
.env.production.local
```

## Deployment, Exercises & Career
<chapterId>eaac757d-c2f4-4a69-a6bc-d227e875a770</chapterId>

### Building for Production

```bash
## Create optimized production build
npm run build

## This creates a 'build' folder with:
## - Minified JavaScript
## - Optimized CSS
## - Compressed assets
## - Service worker for caching
```

#### Deployment to Vercel

```bash
## Push to GitHub
git add .
git commit -m "Complete React Lightning wallet"
git push origin main

## Vercel automatically:
## 1. Detects the push
## 2. Runs npm run build
## 3. Deploys to production URL
## 4. Provides preview deployments
```

#### Environment Variables in Production

Set environment variables in Vercel dashboard:
1. Go to your project settings
2. Add environment variables
3. Redeploy to apply changes

#### Hands-on Exercises

#### Exercise 1: Enhanced Error Handling
Add comprehensive error handling to your wallet:

```jsx
// Add error states
const [errors, setErrors] = useState({
  price: null,
  balance: null,
  transactions: null,
  payment: null
});

// Enhanced error handling in API calls
const getPrice = async () => {
  try {
    setErrors(prev => ({ ...prev, price: null }));
    const response = await axios.get("https://api.coinbase.com/v2/prices/BTC-USD/spot");
    setPrice(response.data.data.amount);
    updateChartData(response.data.data.amount);
  } catch (error) {
    setErrors(prev => ({ 
      ...prev, 
      price: "Failed to fetch Bitcoin price" 
    }));
  }
};

// Display errors in UI
{errors.price && (
  <div className="error-message">
    {errors.price}
  </div>
)}
```

#### Exercise 2: Loading States
Add loading indicators for better UX:

```jsx
const [loading, setLoading] = useState({
  price: false,
  balance: false,
  transactions: false,
  payment: false
});

// Loading spinner component
const LoadingSpinner = () => (
  <div className="loading-spinner">
    <div className="spinner"></div>
    <p>Loading...</p>
  </div>
);

// Use in components
{loading.balance ? (
  <LoadingSpinner />
) : (
  <p>{balance} sats</p>
)}
```

#### Exercise 3: QR Code Integration
Add QR codes for Lightning invoices:

```bash
npm install qrcode.react
```

```jsx
import QRCode from 'qrcode.react';

// In PaymentsModal component
{invoice && (
  <section>
    <h3>Invoice created</h3>
    <QRCode value={invoice} size={256} />
    <p>{invoice}</p>
  </section>
)}
```

#### Exercise 4: Local Storage Persistence
Save wallet settings to localStorage:

```jsx
// Save settings to localStorage
useEffect(() => {
  const settings = {
    currency: 'sats',
    updateInterval: 5000,
    theme: 'dark'
  };
  localStorage.setItem('walletSettings', JSON.stringify(settings));
}, []);

// Load settings from localStorage
useEffect(() => {
  const savedSettings = localStorage.getItem('walletSettings');
  if (savedSettings) {
    const settings = JSON.parse(savedSettings);
    // Apply settings to your app
  }
}, []);
```

#### Exercise 5: Multiple Wallet Support
Extend to support multiple LNbits wallets:

```jsx
const [wallets, setWallets] = useState([]);
const [activeWallet, setActiveWallet] = useState(0);

const addWallet = (apiKey, name) => {
  setWallets(prev => [...prev, { apiKey, name, balance: 0 }]);
};

const switchWallet = (index) => {
  setActiveWallet(index);
  // Fetch data for new wallet
};
```

### Advanced React Patterns

#### Custom Hooks
Create reusable logic with custom hooks:

```jsx
// Custom hook for API calls
function useApi(url, headers) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchData = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.get(url, { headers });
      setData(response.data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return { data, loading, error, fetchData };
}

// Use in components
function App() {
  const { data: balance, loading, error, fetchData } = useApi(
    'https://legend.lnbits.com/api/v1/wallet',
    { 'X-Api-Key': apiKey }
  );

  useEffect(() => {
    fetchData();
  }, []);
}
```

#### Context API for Global State
For larger applications, use Context API:

```jsx
// Create context
const WalletContext = createContext();

// Provider component
export function WalletProvider({ children }) {
  const [balance, setBalance] = useState(0);
  const [transactions, setTransactions] = useState([]);

  const value = {
    balance,
    setBalance,
    transactions,
    setTransactions
  };

  return (
    <WalletContext.Provider value={value}>
      {children}
    </WalletContext.Provider>
  );
}

// Use context in components
function BalanceCard() {
  const { balance } = useContext(WalletContext);
  return <p>{balance} sats</p>;
}
```

#### Memoization for Performance
Optimize expensive operations:

```jsx
import { useMemo, useCallback } from 'react';

function TransactionList({ transactions }) {
  // Memoize expensive calculations
  const totalSpent = useMemo(() => {
    return transactions
      .filter(tx => tx.amount < 0)
      .reduce((total, tx) => total + Math.abs(tx.amount), 0);
  }, [transactions]);

  // Memoize callback functions
  const handleTransactionClick = useCallback((txId) => {
    console.log('Transaction clicked:', txId);
  }, []);

  return (
    <div>
      <p>Total spent: {totalSpent} sats</p>
      {transactions.map(tx => (
        <div key={tx.id} onClick={() => handleTransactionClick(tx.id)}>
          {tx.amount} sats
        </div>
      ))}
    </div>
  );
}
```

### Performance Optimization

#### Code Splitting
Split your app into smaller chunks:

```jsx
import { lazy, Suspense } from 'react';

// Lazy load heavy components
const Chart = lazy(() => import('./components/Chart'));
const PaymentsModal = lazy(() => import('./components/PaymentsModal'));

function App() {
  return (
    <div>
      <Suspense fallback={<div>Loading chart...</div>}>
        <Chart chartData={chartData} />
      </Suspense>
      
      <Suspense fallback={<div>Loading modal...</div>}>
        <PaymentsModal modalState={modalState} />
      </Suspense>
    </div>
  );
}
```

#### React.memo for Component Optimization
Prevent unnecessary re-renders:

```jsx
import { memo } from 'react';

// Only re-render when props actually change
const TransactionItem = memo(({ transaction, onClick }) => {
  return (
    <div onClick={() => onClick(transaction.id)}>
      <p>{transaction.amount} sats</p>
      <p>{transaction.date}</p>
    </div>
  );
});

// Custom comparison function
const TransactionItem = memo(({ transaction }) => {
  return <div>{transaction.amount}</div>;
}, (prevProps, nextProps) => {
  // Only re-render if amount changed
  return prevProps.transaction.amount === nextProps.transaction.amount;
});
```

### Learning Resources

#### Official React Documentation
- **[React.dev](https://react.dev/)** - Official documentation with interactive examples
- **[React Hooks Reference](https://react.dev/reference/react)** - Complete hooks documentation
- **[React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/)** - Browser debugging extension

#### Lightning Development Resources
- **[LNbits Documentation](https://lnbits.com/)** - Lightning wallet and account system
- **[Lightning Network Specification](https://github.com/lightning/bolts)** - Technical specifications
- **[Bitcoin Development Guide](https://developer.bitcoin.org/)** - Bitcoin development resources

#### React Learning Paths
- **[FreeCodeCamp React Course](https://www.freecodecamp.org/learn/front-end-development-libraries/)** - Comprehensive free course
- **[React Tutorial](https://react.dev/learn)** - Step-by-step interactive tutorial
- **[React Patterns](https://reactpatterns.com/)** - Common patterns and best practices

#### Package Documentation
- **[Axios Documentation](https://axios-http.com/)** - HTTP client for API calls
- **[React Modal](https://reactcommunity.org/react-modal/)** - Accessible modal dialogs
- **[React LineChart](https://www.npmjs.com/package/react-linechart)** - Line chart visualization

### Career and Next Steps

#### Building Your Portfolio
1. **Deploy your wallet** - Get it live and share the URL
2. **Add unique features** - Multi-signature, watchtowers, channel management
3. **Write about your experience** - Blog posts, tutorials, documentation
4. **Contribute to open source** - Lightning protocol implementations
5. **Join the community** - Bitcoin developer meetups, conferences

#### Advanced Lightning Development
- **BTCPay Server Integration** - Merchant payment processing
- **Lightning Node Management** - Channel opening, closing, rebalancing
- **Watchtower Implementation** - Security services for offline nodes
- **LNURL Integration** - Lightning authentication and payments
- **Multi-signature Wallets** - Enhanced security features

#### React Ecosystem Expansion
- **Next.js** - Server-side rendering and full-stack React
- **React Native** - Mobile app development
- **TypeScript** - Type safety for larger applications
- **Testing** - Jest, React Testing Library, Cypress
- **State Management** - Redux, Zustand, Jotai

#### Bitcoin Company Opportunities
Companies building on Lightning and Bitcoin:
- **Lightning Labs** - Lightning protocol development
- **Blockstream** - Bitcoin infrastructure
- **River Financial** - Bitcoin financial services
- **Strike** - Lightning payments
- **Fountain** - Lightning-powered podcasting
- **Zap** - Lightning wallet and services

#### Key Takeaways

1. **React revolutionizes development** - Component-based architecture scales infinitely better than vanilla JavaScript
2. **State management is everything** - useState and useEffect are the foundation of dynamic React applications
3. **Component hierarchy planning matters** - Design your component tree before writing code
4. **Props flow down, events flow up** - Understanding data flow prevents bugs and confusion
5. **Hooks enable modern React** - Functional components with hooks are cleaner and more powerful
6. **Real-time updates enhance UX** - Users expect live data in Bitcoin applications
7. **Package management accelerates development** - NPM ecosystem provides solutions for most needs
8. **Error handling builds trust** - Robust error handling is crucial for financial applications
9. **Performance optimization matters** - Memoization and code splitting improve user experience
10. **Security is paramount** - Proper environment variable handling protects user funds

#### Final Project Checklist

- [ ] **Bitcoin price display** - Real-time price from Coinbase API
- [ ] **Wallet balance** - Live balance from LNbits wallet
- [ ] **Transaction history** - List of sent and received payments
- [ ] **Send functionality** - Pay Lightning invoices
- [ ] **Receive functionality** - Generate Lightning invoices
- [ ] **Real-time chart** - Bitcoin price visualization
- [ ] **Responsive design** - Works on desktop and mobile
- [ ] **Error handling** - Graceful error messages
- [ ] **Loading states** - User feedback during operations
- [ ] **Environment variables** - Secure API key handling
- [ ] **Production deployment** - Live on Vercel
- [ ] **Clean code** - Well-organized components and styles

Congratulations! 🎉 You've built a fully functional Lightning wallet using React. You now have the skills to build sophisticated Bitcoin applications and join the growing ecosystem of Lightning developers.

This wallet is just the beginning. You can extend it with advanced features, integrate with other Lightning services, or use these skills to build entirely new Bitcoin applications. The Lightning Network needs more developers, and you're now equipped to contribute to this revolutionary technology.

Welcome to the Bitcoin developer community! ⚡️🧡

---

#### Additional Resources
- **Slides:** [Pleb Wallet Demo Presentation](https://docs.google.com/presentation/d/1CXdnCi_I0R-lPi1XKnvDN0QL3atSlurWApvfEXf1n2M/edit?usp=sharing)
- **Repository:** [Pleb Wallet React Code Examples](https://github.com/AustinKelsay/pleb-wallet-react)


#### What's Next?

You've completed the PlebDevs Frontend Course! Consider these next steps:

- **Build more Lightning apps** - Explore different use cases
- **Learn backend development** - Complete the full stack
- **Join Bitcoin development** - Contribute to open source projects
- **Start your own project** - Build the Lightning app you wish existed
- **Teach others** - Share your knowledge with the community

The journey to becoming a Bitcoin developer continues! 🚀 

# Final part 
<partId>cc9688e4-46ee-473c-9729-6b7bd4a82feb</partId>

## Reviews & Ratings
<chapterId>032e4dcd-d029-492b-a623-7842fd7f6774</chapterId>



<isCourseReview>true</isCourseReview>


## Final examination
<chapterId>3e64a633-9c5c-41e1-8918-77594c6dce40</chapterId>


<isCourseExam>true</isCourseExam>


## Conclusion
<chapterId>3a689fc8-354b-4a27-a2ff-bf709b106249</chapterId>




<isCourseConclusion>true</isCourseConclusion>