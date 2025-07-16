---
name: be-BOP
description: Practical guide to monetizing your business with be-BOP
---

![cover-bebop](assets/cover.webp)


**be-BOP** is an e-commerce platform designed for entrepreneurs wishing to sell online and offline, in complete autonomy, while accepting payments in Bitcoin, via a bank account and in Cash. The solution is also useful for any type of organization wishing to collect donations or monetize its various activities.


The solution is simple, light and autonomous. It enables the creation of an online store, even in an environment where traditional financial services are limited or absent. Indeed, **be-BOP** has been designed to operate efficiently with or without access to banks, using Bitcoin as the payment infrastructure.


In this tutorial, we will take you step by step through :



- Create your first online store with **be-BOP**
- Personalize your showcase and your products
- Configure available payment methods
- Understand the best practices for selling effectively online with **be-BOP**


This tutorial does not require advanced technical skills. It is aimed at developers as well as artisans, merchants, cooperatives or entrepreneurs wishing to embark on digital commerce in a sovereign and resilient way.


## Prerequisites for installing be-BOP on your own server


Before you start installing be-BOP, make sure you have the following technical infrastructure. These elements are essential for the platform to function correctly:


### S3-compatible storage


be-BOP uses a storage system to manage files (such as product images). This requires access to an S3 service, such as :



- [MinIO](https://min.io/) self-hosted
- Amazon S3 (AWS)
- Scaleway Object Storage


You will need to configure a bucket and provide the following information:



- S3_BUCKET**: bucket name
- S3_ENDPOINT_URL**: access link to your S3 service
- S3_KEY_ID** and S3_KEY_SECRET: your access codes
- S3_REGION**: the region of your S3 service


### MongoDB database in ReplicaSet mode


be-BOP uses MongoDB to store store, user, product and other data.


You have two options:



- Install MongoDB locally with **ReplicaSet mode enabled**
- Use an online service like **MongoDB Atlas**


You will need the following variables:



- MONGODB_URL**: database connection address
- MONGODB_DB**: database name


## Node.js environment


be-BOP works with Node.js. Make sure you have **Node.js** version 18 or higher and **Corepack** enabled (needed to manage package managers like pnpm). The command to run is `corepack enable`


### Git LFS installed


Some resources (such as large images) are managed via Git LFS (Large File Storage). Make sure you have Git LFS installed on your machine with the `git lfs install` command. Once these prerequisites are in place, you're ready to move on to the next step: downloading and configuring be-BOP.


**Note:** A technical guide to software deployment is available in a separate tutorial.


## Creating a Super-Admin account


The very first time be-BOP is launched, a **Super Admin** account is created. This account has all the authorizations required to manage back-office functions. To create an account, follow these steps:



- Go to `yourresiteweb/admin/login`
- Create a super-admin account with a secure login and password


This account will give you access to all back-office functions. Once created, you can log in by entering your username and password.


![login](assets/fr/001.webp)


## Back-Office configuration and security


Before configuring your Interface back-office connection, you need to create a unique Hash. This provides protection against malicious actors trying to steal the connection link to your Interface admin.


To create Hash, go to `/admin/Settings`. In the section dedicated to security (e.g. "Admin Hash"), define a unique string (Hash). Once registered, the back-office URL will be modified (e.g. `/admin-yourhash/login`) to restrict access to unauthorized persons.


![hash-login](assets/fr/002.webp)


2.2. Activate maintenance mode (if necessary)


Still in /admin/Settings, (Settings > General via Interface graphics) check the "enable maintenance mode" option at the bottom of the page.


![maintenance-mode](assets/fr/003.webp)


If required, you can specify a list of authorized IPv4 addresses (separated by commas) to enable access to the front office during maintenance. The back office remains accessible to administrators.


![ip-bebop](assets/fr/004.webp)


## Communications setup


To enable be-BOP to send notifications (e.g. for orders, registrations or system messages), you need to configure at least one communication method. Two options are available: e-mail (SMTP) or Nostr.


### SMTP configuration (e-mail)


be-BOP can send e-mails via an SMTP server. You'll need valid SMTP credentials, often supplied by an e-mail service (e.g. Mailgun, Gmail, etc.).


Here's what you need to know:


SMTP_HOST: SMTP server address (e.g. smtp.mailgun.org)


SMTP_PORT: the port to use (often 587 or 465)


SMTP_USER: your username (usually an e-mail address)


SMTP_PASSWORD: your password or API key


SMTP_FROM: the e-mail address that will appear as the sender



### Nostr configuration


be-BOP enables you to send notifications via the Nostr protocol, a decentralized messaging infrastructure. To do this, you need to generate or supply a Nostr private key (NSEC). You can generate this key directly via be-BOP's Interface, in the section dedicated to Nostr. When these elements are correctly configured, be-BOP will be able to automatically send messages and alerts to your users.


## Compatible payment methods


be-BOP is compatible with several payment solutions, allowing you to offer your customers greater flexibility. Here's what you need to set up the payment method that suits you best.


### Bitcoin Onchain


be-BOP lets you accept Bitcoin payments directly on the Blockchain (On-Chain), simply and securely.


**Configuration steps:**



- Go to the **Payment Settings** menu
- Click on **Bitcoin Nodeless** to access On-Chain payment parameters.
- Complete the following fields:


| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)


**Tip:** To obtain your extended public key (Zpub), you can consult the advanced settings of your Bitcoin wallet (Sparrow wallet, BlueWallet, Specter, etc.). Make sure your wallet is **not read-only** if you intend to use transaction history.


### Lightning Network


be-BOP can also accept instant Bitcoin payments thanks to Lightning Network. Two configuration options are currently available:


**Phoenixd**


Go to the `Payment Settings` menu, click on `Phoenixd`


![phoenixd](assets/fr/006.webp)


You'll then need to enter **the password or token authentication** that connects you to your Phoenixd instance, a backend developed by Acinq that lets you manage Lightning payments with your own node, but without the complexity of managing payment channels.


**Swiss Bitcoin Pay**


If you don't want to manage a Lightning node yourself, **Swiss Bitcoin Pay** is a ready-to-use, easy-to-configure solution that's ideal for starting to accept Lightning payments without a complex infrastructure.


Configuration steps :



- In the "Payment Settings" menu, click on `Swiss Bitcoin Pay`
- Log in to your Swiss Bitcoin Pay account (or create one if you don't already have one).
- Enter the API Key supplied by Swiss Bitcoin Pay, then click on "Save"


Once set up, be-BOP will automatically generate Lightning invoices for your customers, and you'll receive payments directly into your Swiss Bitcoin Pay account. This solution is ideal for users who want to avoid the technical complexity of a personal node while accepting fast, low-cost payments.


![swissbtcpay](assets/fr/007.webp)


### PayPal


In addition to Bitcoin, be-BOP also lets you accept cash payments via PayPal, a well-known and widely used international solution.


Configuration steps :



- Go to the `Payment Settings` menu
- Click on `PayPal
- In your Paypal account (developer section), enter the `Client ID` and the `Secret`
- Select the currency of your choice (e.g. **USD**, **EUR**, **XOF**, etc.)
- Click on `save


![paypal](assets/fr/008.webp)


**Note:** You must have a PayPal business account to generate these identifiers. You can obtain them via the [developer] portal (https://developer.paypal.com)


### SumUp


The software now integrates the **SumUp** payment solution, enabling you to accept credit card payments simply, securely and efficiently. To benefit from this functionality, an initial configuration is required. Here are the steps to follow, numbered for a clear and progressive implementation:



- Start by entering your **API Key**, a confidential key supplied by SumUp when you created your developer account. It establishes a secure connection between your SumUp account and the software.
- Fill in the `Merchant Code` field with the unique code that identifies your business within the SumUp platform. This code is essential for associating transactions with your business.
- In the `Currency` field, choose the main currency you use for your transactions (e.g. **EUR**, **USD**, **CDF**, etc.).
- Once all fields have been filled in correctly, click on the `Save` button to save your settings. The system will then establish the link with your SumUp account, and your software will be ready to accept payments.


![payment-sumup](assets/fr/009.webp)


After this configuration, **SumUp** integration will be active and operational, allowing you to quickly cash out and track your transactions directly from the software.


### Stripe


be-BOP also offers full integration with **Stripe**, one of the most popular online payment platforms. Stripe allows you to accept online payments via credit card, digital wallet and several other payment methods. Here's how to activate it:



- Enter the **secret key** provided in the Stripe dashboard.
- Complete the **Public Key** field, also provided by Stripe.
- Select the **principal currency**.
- Save the configuration, then click `Save`.


![payment-stripe](assets/fr/010.webp)


⚠️ **Please note:** It is essential to know the VAT regime applicable to your activity (e.g.: sale under VAT in the seller's country, exemption under justification, or sale at the VAT rate of the buyer's country) in order to correctly configure the invoicing options in **be-BOP**.


## Currency configuration


**be-BOP** offers advanced currency management and is adapted to multi-currency environments and specific accounting requirements. To ensure consistency in financial operations and reporting, it is essential to properly configure the different currencies used in the system. Here are the steps to follow for this configuration:



- Select the **main currency** (`Main currency`)
- Select `Secondary currency
- Define **reference currency** (`Price reference currency`)
- Indicate `Accounting currency


Once all currencies have been correctly configured, the software ensures automatic and accurate conversion of multi-currency transactions, while maintaining rigorous accounting consistency.


![settings-currencies](assets/fr/011.webp)


## Configuration of recovery access via email or Nostr


Still in `/admin/settings`, via the **ARM** module, make sure that the super-admin account includes an **email address** or a **recovery pub**, thus facilitating the procedure if you forget your password.


![settings-users](assets/fr/012.webp)


## Language settings


The software offers multi-language capability to adapt to an international audience and enhance the user experience. To activate the multilingual functionality, it is important to configure the available languages and define a **default language**.


![settings-languages](assets/fr/13.webp)


## Interface and Identity configuration in be-BOP


**be-BOP** provides designers with all the tools they need to design a website. The first step is to open the `/Admin > Merch > Layout` section in the settings. Start by configuring the **Top Bar**, the **Navbar** and the **Footer**.


### Le Top Bar


The **Top Bar** configuration lets you personalize your software's visual identity by displaying key information right from the first line of the Interface. This reinforces brand recognition and provides a clear context for users.


#### Configuration steps :



- In the `Brand name` field, enter the name of your company, organization or product. This name will appear at the top of the Interface and will represent your main visual identity.
- Indicate the website title**: the title chosen should summarize the purpose of the platform. This title can appear in the header or in the browser tab.
- Add Website description**: this is where you enter a brief description of your initiative. This description helps contextualize the tool for users and can also be used for SEO purposes.


Once this information has been entered, the **Top Bar** will display a clear, professional and coherent presentation of your solution.


#### Links in the Top Bar


The Top Bar's `Links` section lets you add shortcuts to important pages in your application or on external sites. These links are displayed directly in the Top Bar, offering your users fast, structured access.


#### Configuration steps :



- Enter link name (Text)**: in the `Text` field, enter the name or label of the link as it will appear (e.g. Home, Contact, Help...).
- Indicate link address (Url)**: in the `Url` field, enter the full address of the target page (internal or external).
- Add other links if necessary**: each configuration line lets you add an additional link using the `Text` and `Url` fields.
- Save links**: once all links have been entered, click on the "Add top bar link" button to save them.


This configuration allows you to offer clear, fluid and accessible navigation through the different sections of your website or to complementary resources.


![settings-topbar](assets/fr/014.webp)


### La Nav Bar


The **Navbar** section lets you configure your be-BOP's main navigation menu, usually located on the side or top of the Interface. This menu guides users to the application's various pages and functions. Link configuration is simple and intuitive. Here's how it works:



- Enter link name (`Text`)**: on the configuration line, start by filling in the `Text` field. This corresponds to the name of the link displayed in the navigation bar (examples: *Dashboard*, *Users*, *Settings*...).
- Enter the link address (`Url`)**: next to the `Text` field, you'll find the `Url` field. In this field, enter the address of the page to which the link should redirect. This can be an internal route or a link to an external page.
- Add multiple links if required**: below the first line, new `Text` and `Url` fields are available for adding as many links as required. Each line represents an additional navigation link.
- Save links**: once you've entered all the elements, click on the `Add nav bar link` button to save and display the results in the navigation bar.


This configuration allows efficient structuring of access to different parts of the software, improving ergonomics and the user experience.


![navbar](assets/fr/015.webp)


### The Footer


The **Footer** section lets you customize the footer of your software, adding useful information or links. Before configuring the links, start by activating a specific option:



- Enable display of the "Powered by be-BOP "** label: activate the `Display Powered by be-BOP` button to display this label in the footer.
- Enter the name of the link (`Text`)**: fill in the `Text` field, which corresponds to the wording of the link in the footer (examples: *Terms*, *Privacy*, *Contact*...).
- Indicate link address (`Url`)**: in the `Url` field, enter the address of the target page (internal or external).
- Add more links if required**: use the additional lines to create as many links as you like.
- Save links**: click on the "Add footer link" button to save links.


![footer](assets/fr/016.webp)


### Visual personalization


**⚠️ Don't forget to set the logos for the light and dark themes, as well as the favicon, via** `Admin > Merch > Pictures`.


Here's how to customize the look and feel of your site:


#### Go to Pictures section


Menu `Admin` > `Merch` > `Pictures`.


#### Add a new image


Click on `New Picture`.


#### Select a local file


Click on `Choose Files`, then select an image from your hard disk.


#### Select the file to import


Double-click on the image to be imported (light logo, dark logo or favicon).


#### Naming the image


Fill in the `Name of the picture` field.


#### Add image


Click `Add` to finalize the import.


![pictures](assets/fr/017.webp)


### Seller Identity Setup


#### Identity settings


Accessible via `Admin > Identity` (or `Settings > Identity`), this section lets you configure your company's administrative and legal information.


#### Legal information



- Business name**: official company name.
- Business ID**: legal identifier or registration number (RCCM, SIRET...).


#### Business address



- Street**: postal address (street, number...).
- Country**: country.
- State**: province or region.
- City**: city.
- ZIP code**: postal code.


#### Contact information



- Email**: professional email address.
- Phone**: company phone number.


#### Bank account



- Account holder name**: name of the account holder.
- Account holder Address**: holder's address.
- IBAN**: International Bank Account Number.
- BIC**: SWIFT/BIC code.


![bank-account](assets/fr/019.webp)


#### Billing



- Click on `Fill with main shop informations` to pre-fill the data.
- Very-top-right issuer information**: field for legal/tax information visible on invoices.
- Click `Update` to save changes.


**Note:** you can also enter additional information to be displayed on the invoice, according to your needs.


![vat](assets/fr/019.webp)


![issuer-info](assets/fr/020.webp)


#### Physical store address


For those with a physical store, add a specific full address in `Admin > Settings > Identity` or a dedicated section. This will enable it to be displayed on official documents and in the footer if necessary.


![seller-id](assets/fr/021.webp)


## Product Management


### Creating a new product


Go to `Admin > Merch > Products` to add or modify a product. Fill in the following fields:


#### Basic information



- Product Name**: name of the product (e.g. *BOP T-shirt limited edition*).
- Slug**: URL identifier without spaces (e.g. `tshirt-bop-edition-limitee`).
- Alias** *(optional)*: useful for quick addition to the basket via a dedicated field.


![product-config](assets/fr/028.webp)


#### Pricing



- Price Amount**: product price (e.g. `25.00`).
- Price Currency**: currency (EUR, USD, BTC, etc.).
- Special products** :
  - this is a free product.
  - this is a pay-what-you-want product.


#### Product options



- Single product (`standalone`)**: only one addition possible per order (e.g. donation, admission ticket).
- Product with variations** :
  - Don't check `Standalone`.
  - Check `Product has light variations (no stock difference)`.
  - Add :
    - Name** (e.g. *Size*),
    - Values** (e.g.: S, M, L, XL),
    - Price differences** if applicable (e.g.: `+2 USD` for XL).


![product-details](assets/fr/029.webp)


## Stock management


### Advanced options when creating a product (Stock, Delivery, Tickets, etc.)


#### Product with limited stock


If your product is not available in unlimited quantities, check `The product has a limited stock`. This activates automatic tracking of remaining quantities. Once this box is checked, a field appears to indicate the **available stock**.


The system manages :



- Reserved stock** → products in baskets not yet paid for
- Stock sold** → products already purchased


**Basket reservation time**: When a customer adds a product to his basket, it is "reserved" for a limited time. You can modify this time in: `Admin > Config > Cart reservation` (value in minutes)


#### Product to be delivered?


Check `The product has a physical component that will be shipped to the customer's Address`. This is useful for all products to be sent physically (books, t-shirts, etc.)


#### Other options



- Ticket**: tick if the product is a ticket for an event
- Booking**: check if this is a reservation slot (e.g.: session, appointment)


![product-options](assets/fr/030.webp)


### Action Settings (bottom)


This section determines **where** and **how** the product can be viewed and purchased:


| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Check only the channels you wish to use.


## Creation and customization of CMS pages and widgets


### Mandatory CMS pages


Go to `Admin > Merch > CMS`. You'll see a list of existing pages and can add new ones with **Add CMS page**.


CMS pages are important for :



- Inform your visitors (e.g. terms of use)
- Comply with the law (e.g. privacy policy)
- Explain certain store features (e.g. IP collection, 0% VAT)


You can add other pages as required:



- About us / Who we are
- Support us / Donations
- FAQ
- Contact
- etc.


**Tip: Click on each link or icon to modify the **content**, **title**, or **seo visibility** of each page.


### Layout and graphic elements


Go to : `Admin > Merch > Layout`. You can customize the visual elements of your site:


![product-options](assets/fr/032.webp)


#### Top Bar



- Modify or delete links (EX: HOME, ABOUT US,...)
- Navigation between key sections of the site


#### Navbar (main navigation bar)



- Present in the grey area below the top bar
- Contains quick access to : `Config`, `Payment Settings`, `Transaction`, `Node Management`, `Widgets`, etc.
- Directors only


#### Footer



- Editable from `Admin > Merch > Layout`
- Contains: contact information, useful links, legal notices..


#### Customize visuals


Go to: `Admin > Merch > Pictures`


You can :



- Change the **main logo**
- Modify or add layout **images**


#### Site description


Also modifiable in `Pictures`, it allows you to display a **summary or slogan** in the header or footer, depending on the theme.


**Note:** this allows you to adjust the appearance to your brand identity (educational, commercial or community).


### Integrating widgets into CMS pages


Widgets** enrich your CMS pages with dynamic or visual elements.


#### Widget creation


Go to: `Admin > Widgets`


Examples of available widgets:



- Challenges**: challenges or missions
- Tags**: categories or keywords
- Sliders**: image carousels
- Specifications** : Specifications tables
- Forms**: forms (contact, feedback, etc.)
- Countdowns**: timers
- Galleries**: image galleries
- Leaderboards**: user rankings


![widgets](assets/fr/033.webp)


#### Integration into CMS pages


Use **shortcodes** in the content of your CMS pages:


| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Current parameters** :



- `slug`: unique widget identifier
- `display=img-1`: product-specific image
- `width`, `height`, `fit`: image dimensions and style
- autoplay=3000`: time in ms between two slides


**Advantages** :



- Easy to insert (copy and paste)
- Dynamic: any modification to the widget is automatically reflected
- No developer required


## Order management and reporting


### Order tracking


To view and manage past orders, go to: `Admin > Transaction > Orders`


Here you will find the **complete list of orders** placed on your site.


![orders](assets/fr/034.webp)


#### Visualization and search


The Interface allows you to search and filter orders according to several criteria:



- order Number: order number
- product alias: product identifier or name
- payment Mean": payment method used (card, crypto, etc.)
- `Email`: customer email


These filters facilitate quick searches and targeted management.


#### Details of each order


By clicking on an order, you can access a complete file containing :



- Products ordered
- Customer information
- Delivery address (if applicable)
- Any notes associated with the order


#### Possible actions on an order


You can :



- Confirm order (if pending)
- Cancel an order (in the event of a problem or customer request)
- Add **labels** (for internal organization)
- Consult / add **internal notes**


**Note:** this section is essential for good logistics and customer relations.


### Reporting and export


To access sales and payment statistics :

administrator > Settings > Reporting


![reporting](assets/fr/035.webp)


Here you'll find an overview of your business, in the form of **monthly and yearly reports**.


#### Report content


The reports are divided into sections:



- Order Detail**: number of orders, status (confirmed, cancelled, pending), evolution
- Product Detail**: products sold, quantities, popular products
- Payment Detail**: amounts collected, breakdown by payment method


#### Data export


Each section includes a **Export CSV** button, which allows you to :



- Download data in CSV format
- Open them in Excel, Google Sheets, etc.
- Archiving for administrative or accounting use
- Use them for internal reports


**Note:** ideal for performance tracking, accounting and presentations.


## Nostr Messaging configuration (optional)


![nostr-config](assets/fr/036.webp)


The platform supports the **Nostr** protocol for certain advanced functions:



- Decentralized notifications
- Login without password
- Interface light administration


### Generating and adding the Nostr private key


Go to :

admin > Node Management > Nostr



- Click on **Create nsec** if you don't have one.
- The system can generate it automatically.
- Alternatively, you can use an existing key (e.g. from Damus or Amethyst).


Next:



- Copy the `nsec` key
- Add it to your `.env.local` (or `.env`) file: ```env NOSTR_PRIVATE_KEY=YourNsecIciKey


### Features activated with Nostr


Once configured, several functions are available:


**Notifications via Nostr**



- Send alerts for orders, payments or system events
- For administrators or users


**Interface light administration**



- Accessible via a Nostr client
- Enables fast, mobile-friendly management


**Connexion without password**



- Login by secure link (sent via Nostr)
- Greater user safety and fluidity


## Design and theme customization


To adapt the appearance of your store to your graphic charter, go to: `Admin > Merch > Theme`


Here you'll find all the options for **creating** and **configuring** a custom theme.


### Creating a theme


![theme](assets/fr/037.webp)


When creating or modifying a theme, you can define :



- Colors**: for buttons, backgrounds, text, links, etc.
- Fonts**: choice of typefaces for titles, paragraphs, menus
- Graphic styles**: borders, margins, spacing, block shapes


### Customizable sections


Each part of the site can be adjusted independently:



- Header**: top navigation bar
- Body**: main content
- Footer** : bottom of page


**Note:** this granularity ensures consistency between the site's visuals and your brand's identity.


### Theme activation


Once the theme is configured :



- Click on **Save**
- Activate it as the store's **main theme**


**Note:** the active theme is the one that will be visible to visitors.


## Configuring e-mail templates


The platform lets you personalize the emails sent automatically to users. Go to: `Admin > Settings > Templates`


![emails-templates](assets/fr/038.webp)


### Creating / editing templates


Each email (order confirmation, forgotten password, etc.) has :



- Subject**: the subject of the email (e.g. "Your order has been validated")
- HTML Body**: HTML content displayed in the email


**Note:** you can insert text, images, links, etc., as required.


### Using dynamic variables


To make emails dynamic, insert variables such as :



- `{orderNumber}}` : replaced by the actual order number
- `{invoiceLink}}` : link to the invoice
- `{websiteLink}}`: URL of your website


**Note:** these tags are automatically replaced when sent.


### Advanced tips



- Create emails that are **responsive** for easy reading on mobile devices
- Add **action buttons** (pay, download, track order)
- Test your emails by sending them to yourself before publication


## Configuring specific tags and widgets


### Tag management


Tags can be used to structure and enrich your content. To access them: `Admin > Widgets > Tag`


![tags-config](assets/fr/039.webp)


### Creating a tag


Complete the following fields:



- Tag Name**: tag name displayed
- Slug**: unique identifier (no spaces or accents)
- Tag Family**: groups tags by category


![targsconfig](assets/fr/040.webp)


#### Available families :



- creators`: authors or producers
- retailers: salespeople or points of sale
- `Temporal`: periods or dates
- events: associated events


### Optional fields


These fields can be used to enrich a tag as if it were a content page:



- Title
- Subtitle
- Short** content
- Full content** (in French)
- CTAs** (action buttons)


### Using tags


Tags can be :



- Allocated to products
- Integrated into CMS pages with a tag: [Tag=slug?display=var-1]


## Configuration of downloadable files


To offer downloadable documents to your customers: `Admin > Merch > Files`


### Adding a file


1. Click on **New file**

2. Inform :


   - File name** (e.g. *Installation guide*)
   - File to upload** (PDF, image, Word...)


**Note:** once added, the platform automatically generates a **permanent link**.


### Using the link


This link can then be inserted into :



- CMS** page (as text link or button)
- A **e-mail client** (via a template)
- A **product sheet** (e.g. manual download)


It's ideal for providing *user manuals, technical guides, product sheets...* without the need for external hosting.


## Nostr-bot


The platform offers advanced integration with the **Nostr** protocol, via an automated bot.


Go to : node Management > Nostr


### Main features


#### Relay management



- Add or remove **relays** used by the bot
- Optimize the **reach** and **reliability** of sent messages


#### Automatic introduction message



- Activate an automatic message on **first user interaction**
- Ideal for :
  - Presenting your service
  - Send a useful link (e.g. FAQ, contact, order)


#### Certification of your `npub



- Add a **logo** and a **public name**
- Link to a **verified web domain**
- Enhances the credibility and recognition of your Nostr identity


### Nostr-bot use cases



- Sending **order confirmations** to you
- Automatic response to **events (e.g. new order)**
- Creating a **decentralized customer interaction**


## Overloading translation labels


be-BOP is multilingual (FR, EN, ES...), but you can adapt the translations to your needs.


To do this, go to: `Settings > Language`


### Loading and editing


Translation files are in JSON. You can :



- Download** language files
- Modify** existing texts
- Add** your own translations


Link to original files :

[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations](https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)


**Example:** replace `Add to cart` by `Ajouter au panier` or `Acheter`.


## Teamwork & Point of Sale (POS)


### User and access rights management


#### Creating roles


Go to: `Admin > Settings > ARM`


Click on **Create a role** to create a role (e.g. `Super Admin`, `POS`, `Ticket checker`).


Each role contains :



- write access**: write access
- read access**: read access
- forbidden access**: sections interdites


#### User creation


In the same menu `Admin > Settings > ARM`, add a user with :



- login
- alias
- email recovery
- (optional) `recovery npub` for connection via Nostr


Assign a previously defined role.


![pos-users](assets/fr/045.webp)


Read-only** users will see menus in *italic* and will not be able to modify content.


## Point of Sale (POS) configuration


### Assigning the POS role


To give a user access to the POS, assign the role `Point of Sale (POS)` in: `Admin > Config > ARM`


He can connect via the secure URL: `/pos` or `/pos/touch`


### POS-specific features


Be-BOP offers a Interface dedicated to physical sales (store, event, etc.).


#### Quick addition via alias


In `/cart`, a field allows you to add a product:



- By scanning a **bar code** (ISBN, EAN13)
- By entering a **product alias** manually


**Note:** the product is automatically added to the basket.


#### Means of payment


POS supports :



- Species
- Credit card
- Lightning Network (crypto)
- Others according to configuration


Two advanced options are available:



- VAT exemption** : applicable on justification (NGOs, foreigners...)
- Gift discount**: exceptional discount with compulsory comment


#### Client-side display


The URL `/pos/session` is intended for a **secondary screen** (HDMI, tablet...):


Poster:



- Products in progress
- Total amount
- Method of payment
- Discounts applied


**Note:** the customer follows the order live, while the seller records it on `/pos`.


### POS summary


| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Thank you for following this tutorial carefully.