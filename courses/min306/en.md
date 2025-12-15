---
name: Bitaxe Open Source Mining Mastery
goal: Master the complete Bitaxe ecosystem, from hardware assembly to advanced customization and performance optimization
objectives:
  - Understand the philosophy of open source Bitcoin mining hardware
  - Build Bitaxe mining devices from scratch
  - Configure and optimize mining software including AxeOS and Public Pool
  - Implement advanced performance optimizations including overclocking and benchmarking
---

# Your Bitaxe Mining Guide

Welcome to the comprehensive Bitaxe course, where you'll master the revolutionary open source Bitcoin mining hardware that's democratizing access to mining technology. This course takes you from understanding the philosophical foundations of decentralized mining to the advanced hardware customization and performance optimization techniques.

The Bitaxe project represents a paradigm shift in Bitcoin mining, breaking the monopoly of proprietary ASIC manufacturers by providing fully open source designs, firmware, and software. Through these hands-on chapters, you'll gain practical skills in hardware assembly, software configuration, PCB design, and performance optimization.

No prior mining experience is required, though basic electronics knowledge and familiarity with GitHub will be helpful. The course will transform you from a curious observer into a capable Bitaxe builder and contributor.

+++


# Introduction

<partId>6b3cd9f0-0063-40f0-a7bb-00a48f330d88</partId>

## Course overview

<chapterId>1fac9579-0e1c-48e3-9bc5-e7a2960018c8</chapterId>

Welcome to the course MIN 306 _**Bitaxe Open Source Mining Mastery**_, a comprehensive journey into the world of Bitaxe mining. This course is designed for those who want to understand, build, and optimize their own Bitaxe mining hardware while exploring the philosophical and technical foundations that make this project unique within the Bitcoin ecosystem.

### Understanding Bitaxe

The first section lays the essential groundwork: you’ll discover the origins of the Bitaxe project, its evolution, and the values of decentralization and transparency that define it. You’ll learn what a Bitaxe actually is, how it differs from proprietary ASICs, and where to find community resources to deepen your knowledge. This section provides the context needed to understand why Bitaxe represents a turning point in Bitcoin mining history.

### Software and Operations

The second section focuses on the software environment, with a detailed presentation of *AxeOS*: the open-source operating system designed specifically for Bitaxe devices. You’ll learn its main features and how to configure and interact with your device to start your first mining operation.

### Community and Collaboration

The third section highlights the collaborative aspect of the project. You’ll explore the open-source philosophy applied to both the hardware and software development of Bitaxe. Through practical exercises, you’ll learn how to contribute directly to the source code, and you’ll also discover _Public Pool_, a community platform for pooling computational power. You’ll also learn how to install it on an Umbrel node for local and sovereign integration.

### Hardware Assembly and Troubleshooting

In the fourth section, you’ll dive into the hardware itself. You’ll learn how to identify the tools needed to assemble a Bitaxe, fix soldering issues and perform a complete diagnostic using *AxeOS* and USB tools. This section emphasizes hands-on practice and a deep understanding of how hardware and software components interact.

### Advanced Customization

The fifth section is dedicated to customization. You’ll learn how to modify the PCB (printed circuit board), create a factory file, and use the _Bitaxe Web Flasher_. This section is aimed at those who want to go beyond simple assembly and truly design customized versions of their own device.

### Performance Optimization

Finally, the sixth section covers advanced optimization techniques. You’ll learn how to benchmark your Bitaxe to evaluate its performance and how to overclock it efficiently. These skills will help you get the most out of your hardware while respecting its physical limitations.

As with every course on Plan ₿ Academy, the final section includes an evaluation designed to reinforce your knowledge.

Dive right into this technical adventure — the future of Bitcoin mining is in your hands!

# Understanding Bitaxe
<partId>ba1cb4ea-6a77-54fd-916c-57285c8c2418</partId>

## The History
<chapterId>73d928e5-72f0-5c17-a7a6-8b6ece7f9a30</chapterId>
:::video id=67d2529a-b7cb-4804-b02c-e56c12c9e66e:::

The Bitaxe project represents a groundbreaking shift in Bitcoin mining hardware development, bringing open source principles to an industry dominated by proprietary solutions. This educational series explores the comprehensive history, technical innovations, and community-driven evolution of Bitaxe, providing insights into how a single engineer's vision transformed into a thriving ecosystem of decentralized mining hardware. Through examining the project's origins, challenges, and achievements, we gain valuable understanding of both the technical complexities of ASIC development and the power of open source collaboration in the Bitcoin space.

### The Origin Story: From Silk Road Discovery to Solar Mining Vision

Skot, the founder of Bitaxe, began his journey into Bitcoin at a college party where he first learned about Bitcoin through someone purchasing items on the Silk Road. This initial exposure to Bitcoin at approximately $20 per coin sparked a curiosity that would later evolve into a revolutionary mining project. The technical foundation for his future work was established during his time at university, where he had access to extensive FPGA resources in a laboratory setting. Working alongside his supervisor, Skot began experimenting with open source FPGA bitstreams for Bitcoin mining, initially with the modest goal of mining enough Bitcoin to purchase a pizza for their office.

The transition from academic experimentation to serious development occurred years later when Skot was working on solar-powered gateways for remote data collection in Africa. This professional experience with solar power systems sparked the realization that Bitcoin mining ASICs, being fundamentally low-voltage DC devices, would pair perfectly with solar panels. The concept seemed natural and elegant. However, when Skot began researching existing solutions he discovered a significant gap in the market: unlike the early days of Bitcoin mining when FPGA designs were openly available, the advent of ASICs had moved the industry toward completely proprietary, closed-source solutions.

The lack of open source mining hardware became a driving frustration for Skot, particularly given his background in open source software development and his belief that Bitcoin's open source nature should extend to its mining infrastructure. This philosophical alignment with open source principles, combined with the technical challenge of reverse-engineering proprietary ASIC designs, set the stage for what would become the Bitaxe project. The initial vision was ambitious yet practical: create a solar-powered Bitcoin miner that could operate independently without requiring a separate computer for control, making it suitable for deployment in remote locations under solar panels.

### Technical Challenges and Reverse Engineering Breakthroughs

The development of Bitaxe required overcoming substantial technical obstacles, primarily centered around the complete lack of documentation of Bitmain's ASIC chips. Skot's approach to this challenge exemplified the determination and ingenuity required for successful reverse engineering. Without access to official datasheets or technical specifications, he resorted to examining chips under microscopes, measuring pin pitches with calipers, and even scanning chips to determine their exact footprint requirements. This painstaking process resulted in multiple failed prototypes, with the first two iterations of the "day miner" failing to function properly due to incorrect footprint calculations.

The breakthrough came with the third iteration in May 2022, when Skot successfully created a working two-chip design using BM1387 chips harvested from Antminer S9 units. This achievement marked the birth of the Bitaxe name, inspired by the concept of a pickaxe for Bitcoin mining. The success of this design validated the reverse engineering approach and demonstrated that independent developers could create functional mining hardware without manufacturer support. However, the technical challenges extended beyond chip interfacing to include complex power supply design, as the ASICs required precise voltage regulation at high currents, often operating at voltages as low as 0.6 volts while drawing significant amperage.

The firmware development presented another layer of complexity, as the project required creating mining software that could run directly on an ESP32 microcontroller rather than relying on external computers running software such as CGMiner. This self-contained approach was essential to Skot's vision of deployable, independent mining units. The combination of hardware reverse engineering and embedded firmware development created a comprehensive technical challenge that required expertise across multiple disciplines, from electrical engineering and PCB design to embedded programming and network protocols.

### Community Formation and Open Source Collaboration

The transformation of Bitaxe from a solo project to a thriving community initiative represents one of the most significant aspects of its success. Initially, Skot's attempts to generate interest through Bitcoin forums and social media met with limited response and occasional skepticism. The breakthrough came when community members like SirVapesAlot recognized the potential of open source mining and established the Open Source Miners United (OSMU) Discord server. This platform provided the collaborative environment necessary for the project to flourish, attracting contributors from diverse backgrounds who shared a common interest in democratizing Bitcoin mining technology.

The community-driven development model proved remarkably effective, with key contributors like johnny9 and Ben emerging to tackle specific technical challenges. Johnny9's expertise in firmware development solved critical software implementation problems, while Ben's front-end development skills created the intuitive AxeOS dashboard that simplified device configuration and monitoring. Ben's additional contributions included establishing manufacturing capabilities and creating Public Pool, an open source mining pool optimized for Bitaxe devices. This collaborative approach demonstrated how open source principles could accelerate development beyond what any individual contributor could achieve alone.

The OSMU community also fostered an inclusive environment where newcomers could learn and contribute regardless of their initial technical expertise. Ben's own journey from soldering novice to major manufacturer exemplifies this welcoming approach to skill development. The community's commitment to education and mutual support created a virtuous cycle where experienced members mentored newcomers, who then became contributors themselves. This model proved essential for scaling the project beyond its original scope and establishing a sustainable ecosystem for continued innovation and growth.

### Vision for Decentralized Mining and Future Impact

Skot's long-term vision for Bitaxe extends far beyond creating another mining device: it is a fundamental transformation of Bitcoin's mining landscape. The ambitious goal of producing one million one-terahash miners would create an exahash of distributed mining power, representing a significant step toward mining decentralization. This vision addresses critical concerns about mining centralization, where large pools and industrial operations could potentially be subject to government pressure or regulatory capture. By distributing mining power across countless home miners, the network becomes more resilient and aligned with Bitcoin's decentralized principles.

The economic model supporting this vision relies on the unique characteristics of home mining, where infrastructure costs are essentially zero and miners can operate with minimal oversight. Unlike industrial mining operations that require massive capital investments in facilities, power infrastructure, and cooling systems, home miners can simply plug devices into existing electrical outlets and internet connections. This approach could theoretically bring significant hash rate online without the traditional barriers to entry that characterize large-scale mining operations.

The project's success has already begun influencing the broader Bitcoin mining ecosystem, with the potential to inspire other manufacturers to embrace open source development models. The financial viability demonstrated by Bitaxe manufacturers proves that open source hardware can be commercially successful while maintaining transparency and community involvement. As the project continues to evolve with new chip integrations, improved designs and expanded manufacturing partnerships, it serves as a proof of concept of how Bitcoin mining can return to its decentralized roots while embracing modern ASIC technology. The ultimate goal extends beyond mere hash rate distribution to include educational impact, bringing more people into direct contact with Bitcoin's fundamental mining process and fostering deeper understanding of the network's security model.

## What is the Bitaxe?
<chapterId>6a56af56-35ce-51af-999b-4bc7305e6464</chapterId>
:::video id=12b26c7a-74b1-4ea9-afc0-e3ef90cf5837:::

### Hardware Overview and Capabilities

The Bitaxe ecosystem encompasses multiple hardware iterations, each designed to optimize different aspects of the mining experience while maintaining the core philosophy of open-source accessibility. These devices serve not only as functional mining hardware but also as educational tools that allow users to understand the intricate relationship between ASIC chips, microcontrollers, and the Bitcoin mining process. Understanding the Bitaxe's design philosophy and technical implementation provides valuable insights into how modern mining hardware operates at both the component and system levels.


### Bitaxe Max, First-Generation Implementation

The Bitaxe Max represents the foundational implementation of the Bitaxe concept, utilizing the BM1397 ASIC chip originally developed by Bitmain for their S17 mining series. This chip integration demonstrates how open-source hardware can repurpose existing ASIC technology to create accessible mining solutions. The Bitaxe Max delivers an estimated hash rate between 300 to 400 gigahashes per second, positioning it as an educational and experimental mining platform rather than a commercial-scale solution.

The BM1397 chip's integration into the Bitaxe Max required careful consideration of power management, thermal control and communication protocols. The board's design accommodates the specific requirements of this ASIC while providing the necessary supporting circuitry for stable operation. This implementation showcases how open-source hardware development can leverage existing semiconductor technology to create new applications and learning opportunities within the mining community.

### Bitaxe Ultra, Advanced Chip Technology

The Bitaxe Ultra represents the evolution of the Bitaxe platform, incorporating the more advanced BM1366 ASIC chip from Bitmain's S19 series. This newer chip technology brings improved efficiency and performance characteristics to the Bitaxe platform while maintaining the same fundamental design philosophy. The upgrade to the BM1366 chip demonstrates the platform's adaptability and the community's commitment to incorporating technological advances into open-source mining solutions.

The transition from the BM1397 to the BM1366 chip required modifications to the board's power delivery systems, thermal management, and control algorithms. These changes illustrate the iterative nature of hardware development and the importance of maintaining compatibility while advancing performance. The Bitaxe Ultra's implementation provides users with access to more recent ASIC technology while preserving the educational and experimental nature of the platform.

### Microcontroller and Communication Systems

At the heart of every Bitaxe device lies an ESP microcontroller that serves as the primary interface between the user and the ASIC chip. This microcontroller runs specialized software developed by the Open Source Miners United (OSMU) community, enabling precise control over the ASIC's operation parameters. The communication between the microcontroller and ASIC occurs through carefully designed serial communication lines that are etched directly onto the printed circuit board as visible traces.

The microcontroller's role extends beyond simple ASIC control: it includes power management, temperature monitoring and user interface functions. Through the integrated display screen, users can monitor critical operational parameters such as temperature, hash rate, IP address, and other relevant mining statistics. This real-time feedback system provides valuable insights into the device's performance and helps users optimize their mining operations while learning about the underlying hardware behavior.

### Power Management and Safety Considerations

The Bitaxe platform operates on a strict 5-volt power requirement, making proper power supply selection critical for device longevity and safety. The power management system on the Bitaxe boards includes sophisticated circuitry designed to regulate voltage delivery to the ASIC chip while monitoring power consumption across different operational modes. This power management capability allows the device to operate efficiently across a range of internal frequencies and voltages, typically consuming between 5 to 25 watts depending on configuration.

Understanding the power requirements becomes crucial when considering that incorrect voltage application can permanently damage the device. The relationship between frequency, voltage, power consumption, and hash rate demonstrates fundamental principles of ASIC operation that apply across all mining hardware. Users can experiment with different power settings to understand the efficiency trade-offs inherent in mining operations, gaining practical experience with concepts that apply to larger-scale mining implementations.

### Solo Mining Focus and Network Participation

The Bitaxe platform specifically targets solo mining applications, where individual miners attempt to solve Bitcoin blocks independently rather than participating in large mining pools. While the hash rate of Bitaxe devices makes successful block discovery statistically unlikely, this approach serves important educational and philosophical purposes within the Bitcoin community. Solo mining with Bitaxe devices helps users understand the fundamental mechanics of Bitcoin's proof-of-work system while contributing to network decentralization.

The emphasis on solo mining reflects the OSMU community's commitment to encouraging individual participation in Bitcoin's security model. By providing accessible hardware that can operate independently, the Bitaxe platform enables users to run their own mining operations without relying on pool infrastructure. This approach fosters a deeper understanding of Bitcoin's consensus mechanism while supporting the network's decentralized nature through increased miner diversity.

### Hardware Evolution and Production Improvements

The Bitaxe platform continues to evolve through community feedback and production optimization, with newer versions incorporating improvements that enhance manufacturability and user experience. Version updates typically focus on production efficiency rather than fundamental performance changes, ensuring that existing users don't face obsolescence pressure. Features like the transition from micro-USB to USB-C connectors and improved power connection systems reflect the community's attention to practical usability improvements.

This evolutionary approach demonstrates the benefits of open-source hardware development, where community input drives incremental improvements that benefit all users. The philosophy of "if it hashes, it hashes" emphasizes the platform's focus on functionality over constant upgrades, encouraging users to maintain and operate their devices rather than pursuing the latest versions. This approach supports sustainable hardware practices while maintaining the educational value of Bitaxe.

## Where can I learn more?
<chapterId>706f2fff-fa1c-5d8e-b14c-ece6e42c016f</chapterId>
:::video id=90088397-3a16-485f-bbd2-89cdbb844e4a:::

The Bitaxe project represents a comprehensive open-source mining initiative that extends far beyond a single device. Understanding where to find reliable information, technical resources, and community support is crucial for anyone looking to engage with this ecosystem. This chapter provides a complete guide to the essential platforms and resources that form the foundation of the Bitaxe and Open Source Miners United (OSMU) community.

### Bitaxe.org, the Central Hub

The Bitaxe.org website serves as the primary gateway to all project-related information and resources. This centralized platform functions as your first point of reference whenever you need to learn about Bitaxe devices or explore other projects within the OSMU community. The website's design prioritizes accessibility and organization, presenting visitors with carefully curated links that connect to various specialized resources throughout the ecosystem.

The importance of this central hub cannot be overstated, as it eliminates the confusion that often accompanies decentralized open-source projects. Rather than searching through multiple platforms or relying on potentially outdated information from unofficial sources, users can trust Bitaxe.org to provide current, verified links to all essential resources. This approach ensures that both newcomers and experienced community members can efficiently locate the specific information they need for their projects.

### Technical Resources and Development Materials

The hardware design files repository on GitHub represents one of the most valuable resources for anyone interested in understanding or building Bitaxe devices. This public repository contains comprehensive documentation that covers every aspect of the hardware design process, from initial concepts to final manufacturing specifications. The repository includes detailed images, project goals, feature descriptions, and built-in component explanations that provide both technical depth and practical guidance.

For those interested in manufacturing their own devices, the repository includes specific documentation files such as building.md, which provides step-by-step instructions for the entire production process. This documentation covers the software tools required for PCB design, the procedures for sending files to manufacturers, and the steps involved in receiving and validating manufactured PCBs. This level of detail ensures that individuals or small organizations can successfully navigate the manufacturing process without extensive prior experience in hardware production.

The ESP-Miner repository serves as the central location for all firmware-related code and documentation. This GitHub repository contains every line of code written for the Bitaxe firmware, along with comprehensive documentation that explains system requirements, hardware specifications, and configuration options. The repository structure is designed to accommodate both users who prefer pre-compiled binary files and developers who want to build the firmware from source code.

The documentation within this repository includes detailed sections on hardware requirements, pre-configuration options, and recommended values for various settings. This information proves to be invaluable for users who want to customize their devices or troubleshoot specific issues. Additionally, the repository includes information about newer developments, such as Raspberry Pi integration, ensuring that the documentation remains current with ongoing project evolution.

### Device Management and Maintenance Tools

The Bitaxe web flasher represents a practical solution for device maintenance and updates. This web-based tool allows users to flash firmware to their devices without requiring specialized software or complex command-line procedures. The flasher supports multiple device variants, including the Bitaxe Ultra with various port versions and the older Bitaxe Max models. Users can choose between updating existing firmware through the web interface or performing complete factory resets using USB connections.

This tool addresses one of the most common challenges faced by hardware enthusiasts: maintaining and updating device firmware. By providing a user-friendly web interface, the flasher eliminates many of the technical barriers that might otherwise prevent users from keeping their devices current with the latest firmware releases. The tool's design prioritizes simplicity while maintaining the flexibility needed for different device configurations and update scenarios.

### Community Platforms and Communication Channels

The Discord server represents the heart of real-time community interaction and support within the Bitaxe ecosystem. The server's organization reflects the diverse interests and needs of community members, with carefully structured channels that facilitate focused discussions on specific topics. New members encounter a verification process that requires reading and accepting community rules, ensuring that all participants understand the expectations for respectful and productive interaction.

The server's channel structure includes general discussion areas covering topics such as solar power integration, mining pools, and Bitcoin-related discussions. More specialized sections focus on specific devices, including dedicated channels for the Bitaxe Ultra, Hex, and Supra variants. The firmware channel provides a focused space for technical discussions about software development and troubleshooting, while the official releases channel ensures that community members receive timely notifications about new developments.

It also features a subscriber area that provides additional benefits for community members who choose to support the project financially. This tiered approach allows the community to offer enhanced services while maintaining open access to essential information and support channels. The help channel serves as a dedicated space for troubleshooting and technical assistance, ensuring that users can receive prompt support when encountering difficulties.


The Open Source Miners United wiki (osmu.wiki) provides comprehensive documentation that complements the real-time discussions occurring on Discord. Unlike chat-based platforms, the wiki offers structured, searchable documentation that covers all aspects of the Bitaxe project and related initiatives. The way it is organized mirrors the project's structure, with dedicated sections for different device series and comprehensive setup guides.

The wiki's open-source nature allows community members to contribute directly to the documentation. Users can edit pages, submit corrections, and add new information through GitHub integration, ensuring that the knowledge base remains current and transparent. This collaborative approach leverages the collective expertise of the community while maintaining quality control through a review process for submitted changes.

The wiki includes practical resources such as PDF setup guides that provide step-by-step instructions for device configuration and use. These guides serve as valuable references for both new users and experienced community members who need quick access to specific procedures or configuration details.

### Purchasing and Vendor Information

The Bitaxe legit list addresses a critical need within the open-source hardware community: identifying trustworthy vendors and avoiding fraudulent sellers. This curated list includes verified resellers and manufacturers who meet specific criteria for legitimacy and community support. Each listing includes direct links to vendor websites, regional information, and company descriptions that help users make informed purchasing decisions.

Importantly, the list indicates whether each vendor contributes back to the OSMU community, either financially or through other forms of support. This transparency helps community members understand which vendors actively support the project's development and sustainability. The list also serves as a protective measure against common scams, such as unauthorized pre-orders for unreleased products, which have historically caused problems within the community.

The emphasis on non-affiliate links demonstrates the community's commitment to providing unbiased vendor recommendations. Users can trust that the recommendations are based on vendor legitimacy and community contribution rather than financial incentives, ensuring that purchasing decisions support both individual needs and community sustainability.


# Software and Operations
<partId>04b302a9-42ba-5ad4-834c-6979950c2948</partId>

## What is AxeOS?
<chapterId>a0cdf10d-e007-58e2-a17b-b588fd393b5e</chapterId>
:::video id=de7bcbf2-f9ac-4057-ad40-29dc223b4798:::

AxeOS is a firmware and web interface for Bitaxe mining devices, providing users with complete control and monitoring capabilities through an intuitive browser-based dashboard. This system transforms the complex task of ASIC management into an accessible experience, allowing miners to monitor performance, adjust settings, and manage multiple devices from a single interface. Understanding AxeOS is essential for maximizing your Bitaxe device's potential and maintaining optimal mining operations.

### Dashboard Overview and Core Metrics

The AxeOS dashboard serves as your primary window into your Bitaxe device's performance, presenting critical mining metrics in an organized, real-time format. When you navigate to your Bitaxe device's IP address, you're immediately presented with four key performance indicators that define your mining operation's current state. The hash rate display shows the actual computational speed your ASIC chip is producing as it processes the current block template, providing immediate feedback on your device's core functionality.

Adjacent to the hash rate, the shares counter tracks every valid solution your Bitaxe device submits to the mining pool, incrementing with each successful submission and serving as a direct measure of your device's contribution to the pool's mining efforts. The efficiency metric provides crucial insight into your device's power performance by calculating the ratio of hash rate to power consumption, helping you optimize your operation's profitability. The best difficulty indicator preserves a record of the highest difficulty share your device has ever found, maintaining this achievement even through reboots and updates, only resetting when you perform a complete factory flash.

The dashboard's expandable menu system, controlled by a toggle button, provides access to all AxeOS functionality while maintaining a clean interface. The live hash rate graph represents one of its most valuable features, displaying real-time performance data that becomes more accurate and informative the longer you maintain your session. The power, heat, and performance sections provide comprehensive monitoring of your device's operational status, including input voltage warnings that alert you to potential power supply issues while ensuring continued operation within safe parameters.

### Advanced Monitoring and System Information

The monitoring capabilities of AxeOS extend far beyond basic hash rate tracking, providing detailed insights into every aspect of your Bitaxe device's operation. The power section displays calculated power consumption derived from onboard integrated circuits, input voltage measurements from your power supply connection, and requested ASIC voltage levels. When voltage drops occur, AxeOS immediately presents warning notifications, though these typically don't affect mining operations and simply indicate potential power supply optimization opportunities.

Temperature monitoring focuses on ASIC chip thermal management, with readings taken from strategic locations on the device to provide accurate thermal data with appropriate offsets for chip-level accuracy. The frequency and voltage displays offer real-time feedback on your ASIC tuning parameters, with the measured voltage representing the most accurate reading available, taken directly at the ASIC chip location. This precision enables fine-tuning of performance parameters while maintaining safe operating conditions.

The connection status section provides immediate visibility into your mining pool configuration, displaying the current stratum URL, port, and user identification. For devices connected to public pools, AxeOS generates convenient quick links that transport you directly to your pool's web interface, where you can access detailed statistics, device listings, and historical performance data. This integration streamlines the monitoring process by connecting device-level and pool-level information in a seamless workflow.

### Swarm Management and Multi-Device Control

The Swarm functionality represents AxeOS's solution to the complexity of managing multiple Bitaxe devices across a network, eliminating the need to remember and navigate to numerous IP addresses. This centralized management system allows you to add devices by simply entering their IP addresses, automatically detecting active Bitaxe miners and incorporating them into a unified control dashboard. Once configured, Swarm provides comprehensive control over your entire mining operation from a single interface.

Through the Swarm interface, you can perform critical management tasks across multiple devices simultaneously or individually, including pool configuration changes, device restarts, frequency adjustments, and performance monitoring. This centralized approach significantly reduces the administrative overhead of managing large mining operations while ensuring consistent configuration across all devices. The system maintains individual device identity while providing collective management capabilities, striking an optimal balance between granular control and operational efficiency.

The Swarm dashboard presents each managed device with its current status, performance metrics, and quick-access controls, enabling rapid response to performance issues or configuration changes. This functionality proves particularly valuable for miners operating multiple devices in different locations or those who frequently adjust mining parameters based on market conditions or pool performance.

### Configuration Management and System Settings

The Settings section of AxeOS provides comprehensive control over every configurable aspect of your Bitaxe device, from network connectivity to mining parameters and hardware optimization. Network configuration begins with Wi-Fi setup, where you specify your network name and password, with AxeOS recommending single-word network names without spaces to ensure reliable connectivity. The system handles the complete wireless configuration process, enabling remote management and monitoring capabilities.

Mining configuration centers on stratum settings, where you specify your chosen mining pool's URL without protocol prefixes or port numbers, which are handled in separate fields. The stratum user field accommodates various pool requirements, supporting both Bitcoin addresses for solo mining and username systems for pool mining, with the ability to append device identifiers for multi-device operations. The recently added stratum password functionality supports pools requiring authentication, though most public pools operate without this requirement.

Hardware optimization through frequency and core voltage adjustment represents AxeOS's most powerful performance tuning capability. Depending on your device version and browser, these settings may appear as dropdown menus with preset configurations or as open fields allowing custom values. The default settings of 485 MHz frequency and 1200 mV core voltage provide stable operation for initial testing, while advanced users can optimize these parameters for maximum performance or efficiency based on their specific requirements and operating conditions.

### System Maintenance and Advanced Features

AxeOS includes sophisticated system maintenance capabilities designed to keep your Bitaxe device operating at peak performance while providing diagnostic information for troubleshooting and optimization. The update system streamlines firmware management by displaying the latest available release directly in the interface and providing direct download links to official firmware files. This integration eliminates the need to manually navigate GitHub repositories or manage file downloads, simplifying the update process to a few clicks.

The update interface accepts properly named firmware files, specifically esp-miner.bin and www.bin, ensuring compatibility and preventing installation errors. For users experiencing difficulties with the standard update process, AxeOS provides references to comprehensive factory flash procedures that can restore devices to original functionality. This dual approach accommodates both routine updates and recovery scenarios.

The logging system provides real-time insight into device operations, displaying detailed information about ASIC chip models, system uptime, Wi-Fi connectivity status, available memory, firmware versions, and board revisions. These logs prove invaluable for developers and advanced users seeking to understand device behavior, diagnose issues, or optimize performance. The real-time log viewer presents live operational data, including nonce processing, difficulty calculations, and mining submission parameters, offering unprecedented visibility into the mining process itself.

Additional system features include screen orientation control for devices used in custom enclosures, fan polarity inversion for specialized cooling configurations, and automatic fan control that adjusts cooling based on ASIC temperature. Manual fan speed control provides precise cooling management when automatic systems don't meet specific requirements. All configuration changes require saving and device restart to take effect, ensuring stable operation and preventing partial configuration states that could impact mining performance.


# Community and Collaboration
<partId>eed1ce48-6752-5744-91f7-91e4e20ff6b2</partId>

## Open-Source Contribution Overview
<chapterId>715d026e-cebc-536e-a34e-728f5653b999</chapterId>
:::video id=7298ba19-28d2-4a7c-ac0b-44ad0c4770cf:::

### GitHub and Its Role in Software Development

GitHub represents a fundamental shift in how software development projects are managed and shared across the global programming community. As a cloud-based platform that hosts software development projects using Git, a distributed version control system, GitHub enables developers to collaborate seamlessly on projects regardless of their physical location. The platform serves as both a technical tool and a social network for programmers, allowing them to track changes, merge updates, maintain different versions of their code, and contribute to open-source initiatives like the BitX project from Open Source Miners United.

The power of GitHub lies in its ability to simplify the complex process of collaborative development. When multiple developers work on the same project, GitHub provides the infrastructure to manage contributions, review changes, handle project issues, and maintain comprehensive documentation. This collaborative approach has made GitHub an essential component of modern software development workflows, transforming how both individual developers and large organizations approach project management and code sharing.

### Navigating the GitHub Interface and Repository Structure

Understanding the GitHub interface begins with recognizing the key elements that make up any repository page. The top navigation bar contains several critical sections including Code, Issues, Pull Requests, Discussions, Actions, Projects, Security, and Insights. Each section serves a specific purpose in the project management ecosystem, with the Code section displaying the actual files and folders that comprise the project.

The repository structure itself reflects the organizational approach of the project maintainers. Some repositories contain just a single file, perhaps a simple shell script, while others like the BitX hardware project contain numerous files organized into directories and subdirectories. The repository name appears prominently and serves as both an identifier and a brief description of the project's purpose. Essential interactive elements include the Watch button for receiving notifications about repository updates, the Fork button for creating personal copies of the repository, and the Star button which functions as a community endorsement system similar to a "thumbs up" feature.

The About section provides crucial project information in a condensed format, including a one-line description, licensing information, and key project details. For the BitX project, this section identifies it as "open source ASIC Bitcoin miner hardware" and specifies the GPL 3.0 license. Understanding licensing is particularly important because GitHub operates as an open-source platform where public repositories are accessible to the entire community but the content can only be used and distributed according to each license's compliance rules.

### Working with Branches and Project Versions

The concept of branches represents one of GitHub's most powerful features for managing different versions and development tracks within a single project. A branch essentially creates a copy or modified version of the main codebase, allowing developers to work on specific features, bug fixes, or experimental changes without affecting the primary development line. The master branch typically serves as the default and most stable version of the project, while additional branches accommodate different iterations, testing phases, or entirely different product variants.

In the BitX hardware project, multiple branches exist to manage different hardware versions and configurations. For example, the Ultra v2 branch contains files specific to that hardware iteration, while the Super 401 branch focuses on implementations using the S21 ASIC chip for improved efficiency. Each branch may be several commits ahead or behind the master branch, indicating the extent of changes and development activity. When examining different branches, users will notice completely different file structures, documentation, and even visual representations, reflecting the unique requirements and specifications of each hardware variant.

The branch system prevents confusion among contributors and users by clearly separating different development tracks. Rather than mixing experimental features with stable releases, or combining different hardware versions in a single location, branches provide clean separation while maintaining the ability to merge successful changes back into the main development line when appropriate. This organizational approach ensures that users can easily locate the specific version they need while developers can work on improvements without disrupting the primary project.

### Contributing Through Issues

The Issues section serves as the primary communication channel between users and project maintainers for reporting problems, suggesting improvements, and documenting bugs. However, it's crucial to understand that the Issues section is specifically designed for legitimate technical problems rather than general questions or support requests. When users encounter actual malfunctions, unexpected behavior, or identify potential improvements, creating a well-documented issue helps the entire community by bringing attention to problems that may affect multiple users.

Effective issue reporting requires detailed documentation of the problem, including the circumstances that led to the issue, steps to reproduce the problem, and any relevant technical details. The BitX project demonstrates this principle through various closed issues that show the resolution process, from initial problem identification through community discussion to final resolution. Some issues result in hardware improvements, such as the addition of mounting holes to increase cooling options, while others may be resolved through user education or software updates.

The distinction between Issues and Discussions is important for maintaining organized community interaction. While Issues focus on specific technical problems, the Discussions section provides a forum-like environment for questions, ideas, and general community engagement. Although the Discord server has become the primary communication channel for the BitX community, the GitHub Discussions section remains available for more formal or searchable conversations that benefit from permanent documentation and easy reference.

### Understanding Pull Requests

Pull requests represent the mechanism through which external contributors propose changes to a project repository. When someone identifies an improvement, bug fix, or new feature that would benefit the project, they can create a pull request to submit their changes for review and potential integration into the main codebase. This process ensures that all modifications undergo review before becoming part of the official project, maintaining code quality and project coherence while enabling community contributions.

The pull request workflow typically begins when a contributor forks the repository, creates their own copy where they can make changes, and then submits those changes back to the original project through a pull request. Project maintainers can then review the proposed changes, discuss modifications with the contributor, and ultimately decide whether to merge the changes into the main project. This collaborative review process helps maintain project standards while encouraging community participation and improvement.

Understanding tags and releases adds another layer to project management and version control. Tags serve as markers in the development timeline, identifying specific points that represent particular versions or milestones. In hardware projects like BitX, tags often correspond to specific model numbers or hardware revisions, providing clear reference points for users seeking particular versions. Releases, more commonly used in software projects, represent formal distributions of completed features and bug fixes, often accompanied by detailed release notes and downloadable packages.

The GitHub ecosystem creates a comprehensive environment for open-source collaboration that extends far beyond simple file sharing. By understanding these various components and their proper usage, contributors can effectively participate in projects, help improve software and hardware designs, and benefit from the collective knowledge and effort of the global development community. Whether reporting issues, suggesting improvements, or contributing code, GitHub provides the tools and structure necessary for meaningful collaboration in the open-source world.

## Open-Source Contribution Hands-on
<chapterId>84d033f5-7182-584f-b1a5-697172bc7a1c</chapterId>
:::video id=7d318fd0-6f0b-422a-9f30-2c470b56951d:::

Building upon the foundation of creating issues and exploring open source projects, this chapter focuses on the practical aspects of making direct contributions through pull requests and repository management. Understanding how to fork repositories, make changes, and submit pull requests represents a crucial skill set for any developer looking to contribute meaningfully to open source projects, whether they involve software development or hardware design.

The process of contributing code changes follows a standardized workflow that ensures project integrity while allowing for collaborative development. This workflow involves creating your own copy of a project repository, making modifications in a controlled environment, and then proposing those changes back to the original project through a formal review process. While the examples in this chapter focus primarily on software contributions, the same principles and procedures apply equally to hardware projects involving PCB designs, schematics, and other technical documentation.

### Understanding Forks and Repository Structure

The foundation of contributing to any open source project begins with creating a fork, which serves as your personal copy of the original repository. When you navigate to a GitHub repository and click the "fork" button, you create an independent copy under your own GitHub account that maintains a clear connection to the original source. This forked repository appears in your account with a clear indication of its origin, displaying text such as "forked from [original-owner]/[repository-name]" beneath the repository title.

Your forked repository operates independently from the original, allowing you to make changes without affecting the main project. However, it maintains awareness of updates to the original repository through GitHub's synchronization features. When the original repository receives updates that your fork lacks, GitHub displays status information such as "This branch is X commits behind" or "X commits ahead," providing clear visibility into the relationship between your fork and the upstream repository. You can synchronize your fork with the original repository at any time by clicking the "Sync fork" button, which pulls in the latest changes from the upstream source.

The relationship between your fork and the original repository becomes particularly important when you begin making changes. As you implement modifications and commit them to your fork, GitHub tracks these differences and displays them as commits ahead of the original repository. This tracking system enables the pull request process, where you can propose your changes for inclusion in the main project while maintaining a clear history of what has been modified.

### Setting Up Your Development Environment

Creating an effective development environment requires careful attention to both general development tools and project-specific requirements. Visual Studio Code serves as an excellent integrated development environment (IDE) for most open source contributions, providing essential features for code editing, version control integration, and project management. The first critical component involves installing and configuring the Git extension, which enables seamless integration with GitHub repositories directly from your development environment.

Modern versions of Visual Studio Code typically include Git support by default, but you must authenticate with your GitHub account to enable full functionality. This authentication process involves signing into GitHub through the IDE, which then allows you to clone repositories, commit changes, and push updates directly from your development environment. The GitHub integration appears as an icon in the left sidebar, providing access to repository cloning, branch management, and synchronization features without requiring command-line operations.

For projects involving embedded systems or specific hardware platforms, additional tools become necessary. The ESP-IDF extension represents a crucial component for projects targeting ESP32 microcontrollers, requiring specific version compatibility to ensure proper functionality. The installation process involves selecting the appropriate ESP-IDF version, configuring tool paths, and setting up the development container environment. Version 5.1.3 currently represents the recommended configuration for many ESP32-based projects, though these requirements may evolve as projects update their dependencies and toolchains.

### Making Changes and Managing Commits

Once your development environment is properly configured, the process of making meaningful contributions begins with downloading or cloning your forked repository to your local machine. You can accomplish this either by downloading a ZIP file of the repository contents or by using Visual Studio Code's integrated cloning functionality, which provides a more streamlined workflow for ongoing development. The cloning process creates a local copy of your repository that remains synchronized with your GitHub fork, enabling you to work offline while maintaining version control capabilities.

When working with the local repository, you gain access to the complete project structure, including source code files, configuration files, documentation, and any hardware design files. Most firmware projects utilize programming languages such as C for core functionality, with additional components written in TypeScript for user interfaces or Java for specific utilities. Understanding the project structure helps you identify the appropriate files to modify and ensures that your changes align with the project's architectural patterns and coding standards.

The commit process represents a fundamental aspect of version control that requires careful attention to both technical accuracy and communication clarity. Before making any changes, you should thoroughly understand the existing code and test any modifications in your local environment. The cardinal rule of open source contribution emphasizes never publishing untested code, as this can introduce bugs or security vulnerabilities that affect the entire project community. Additionally, you must never commit sensitive information such as passwords, API tokens, or personal credentials to public repositories, as this information becomes permanently accessible to anyone with repository access.

### Creating and Managing Pull Requests

The culmination of your contribution effort involves creating a pull request, which serves as a formal proposal to merge your changes into the original project repository. This process begins in your GitHub fork, where you can review the differences between your repository and the upstream source. GitHub's interface clearly displays the number of commits ahead or behind, providing immediate visibility into the scope of your proposed changes. Before creating a pull request, you should ensure your fork is synchronized with the latest upstream changes to minimize potential conflicts.

Creating an effective pull request requires more than simply submitting your code changes. The pull request description serves as your opportunity to communicate the purpose, scope, and impact of your modifications to the project maintainers and community. A well-written description explains what problems your changes address, how you implemented the solution, and any potential implications for other parts of the project. This documentation becomes particularly important for complex changes that might not be immediately obvious from examining the code differences alone.

The review process represents a collaborative aspect of open source development where project maintainers and experienced contributors evaluate your proposed changes. You can request specific reviewers who have expertise in the areas your changes affect, ensuring that knowledgeable community members examine your work. The review process may involve multiple iterations, with reviewers providing feedback, requesting modifications, or asking for additional testing. This collaborative refinement process helps maintain code quality while providing valuable learning opportunities for contributors at all experience levels.

Understanding that not all pull requests receive acceptance helps set appropriate expectations for the contribution process. Project maintainers may decline pull requests for various reasons, including misalignment with project goals, insufficient testing, or the existence of alternative solutions already in development. Rather than viewing rejection as failure, it should be considered as an opportunity to learn from feedback, refine the approach, and potentially contribute alternative solutions that better meet the project's needs. The open source community thrives on this iterative process of proposal, review, and refinement that ultimately drives projects forward through collective effort and shared expertise.


## What's Public-Pool?
<chapterId>b461bf94-4a90-5bb8-ba3f-976d5d57be0d</chapterId>

:::video id=d4652496-1ed4-4415-8048-0b6871b9ed51:::

Public Pool represents a revolutionary approach to Bitcoin mining that addresses many of the concerns miners have with traditional mining pools. As a fully open-source solo Bitcoin mining pool, Public Pool fundamentally changes the reward distribution model that miners have become accustomed to. Unlike conventional mining pools where participants share rewards when any miner in the pool finds a block, Public Pool operates on a solo mining principle where individual miners retain 100% of their block rewards when they successfully mine a block.

The most compelling feature of Public Pool is its zero-fee structure. When miners successfully find a block using Public Pool, they receive the complete block reward along with all associated transaction fees, without any deductions for pool operation costs. This stands in stark contrast to traditional mining pools that typically charge fees ranging from 1-3% of mining rewards. The zero-fee model makes Public Pool particularly attractive for miners who want to maximize their potential returns while maintaining full control over their mining operations.

To understand Public Pool's unique position, it's important to grasp the fundamental difference between solo mining and pooled mining. True solo mining means you mine independently and receive the full block reward (currently 3.125 BTC + fees) if you find a block, but the probability is proportional to your hash rate versus the entire network—creating extreme variance that can span months or years between rewards. Traditional pools combine hash power to find blocks more frequently, distributing rewards proportionally and providing steady, predictable income. For miners with significant capital invested in hardware and operating costs, pure solo mining is typically impractical regardless of its philosophical advantages—the variance makes it nearly impossible to cover electricity costs and recover investments. This economic reality means most miners will choose pooled mining for practical financial reasons. Public Pool operates as a solo mining pool, meaning you still face the variance of solo mining (you only get rewarded when you personally find a block), but you benefit from the pool's infrastructure and transparent, zero-fee operation.

### The Open Source Advantage and Technical Implementation

Public Pool's commitment to open-source development provides miners with unprecedented transparency and control over their mining operations. The entire codebase is available on GitHub, allowing miners to examine exactly how the software operates, modify it according to their needs, and even contribute to its development. This transparency addresses a significant concern in the mining community regarding the unknown configurations and practices of traditional mining pools.

The software architecture includes both the core mining pool functionality and a separate user interface repository, both of which are freely available for download and modification. Miners can run Public Pool in various configurations, including Docker containers, making it adaptable to different hardware setups and technical preferences. The comprehensive documentation provided in the GitHub repositories offers detailed installation guides, configuration options, and modification instructions, making it accessible to miners with varying levels of technical expertise.

Connecting to Public Pool requires minimal configuration compared to traditional mining setups. Miners simply need to configure their mining devices with the Stratum connection details and provide their Bitcoin address as the username. An optional worker name can be added after a dot separator for organizational purposes.

### Community Features and Sustainability Model

Public Pool incorporates several innovative features that strengthen the Bitcoin mining community while maintaining its zero-fee operation. The platform displays comprehensive statistics including the total hash rate of connected miners, which was typically ranged between 1 to 2 PetaHash per second in 2024 and around 40 PH/s in November 2025, and provides detailed information about connected mining devices. Particularly noteworthy is the platform's emphasis on open-source mining hardware, with devices marked by stars indicating fully open-source designs, complete with links to their respective GitHub repositories.

The sustainability of Public Pool's zero-fee operation relies on a creative affiliate program partnership with mining hardware vendors. When miners purchase equipment from partner companies using the discount code "SOLO", fifty percent of the affiliate earnings support Public Pool's operational costs, while the remaining fifty percent is distributed as rewards to miners who achieve the highest difficulty shares each month. This model creates a symbiotic relationship where miners receive discounts on equipment purchases, vendors gain customers, and Public Pool maintains its operations without charging direct fees.

### Decentralization Philosophy and Best Practices

While Public Pool offers an excellent alternative to traditional mining pools, it's important to understand its role within the broader context of Bitcoin decentralization. The platform serves as a stepping stone toward the ultimate goal of individual miners operating their own mining pools. Running your own mining pool represents the highest level of decentralization, as it eliminates dependence on any third-party infrastructure or software, regardless of how transparent or well-intentioned that third party may be.

Public Pool's open-source nature makes it an ideal learning platform for miners who want to understand pool operations before implementing their own solutions. The availability of installation guides for multiple operating systems and the comprehensive documentation provide miners with the knowledge needed to transition from using Public Pool to operating their own mining infrastructure. This educational aspect aligns with Bitcoin's fundamental principles of self-sovereignty and decentralization, empowering individual miners to take complete control of their mining operations while contributing to the overall security and decentralization of the Bitcoin network.

The platform's user interface provides miners with detailed monitoring capabilities, including worker status, hash rate statistics, and performance metrics. These features help miners optimize their operations while learning about pool management principles that they can later apply to their own mining pool implementations.

## How to install Public-Pool on Umbrel
<chapterId>7f6d0307-7715-5581-89ea-f13cf8754f9a</chapterId>

:::video id=3a4fe0a9-bbf5-458a-8ec1-52c3b83afd87:::

Running your own Bitcoin mining pool at home has become increasingly accessible with modern hardware and simplified software solutions. This chapter explores the practical implementation of a home-based public pool using affordable mini PC hardware and streamlined node management software. By the end of this guide, you'll understand the hardware requirements, software setup process, and basic configuration needed to establish your own mining pool infrastructure.

### Hardware Requirements and Setup

The foundation of any home mining pool setup begins with selecting appropriate hardware that balances performance, cost, and energy efficiency. A mini PC represents an ideal solution for this application, offering sufficient processing power while maintaining a compact footprint and reasonable power consumption. The recommended configuration includes an Intel N100 processor, which provides adequate computational resources for pool operations, paired with at least one terabyte of NVMe storage to accommodate the Bitcoin blockchain and associated data.

The storage requirement is particularly critical since running a mining pool necessitates maintaining a fully synchronized Bitcoin node. The one terabyte NVMe drive ensures fast read/write operations essential for blockchain synchronization and ongoing transaction processing. Additionally, sufficient RAM allocation supports smooth operation of both the underlying Linux operating system and the node management software that will coordinate pool activities.

### Software Architecture and Node Management

The software stack for a home mining pool builds upon a Linux foundation, providing the stability and security necessary for Bitcoin operations. On top of this base system, specialized node management software like Umbrel creates an intuitive interface for managing Bitcoin infrastructure. This approach abstracts much of the complexity traditionally associated with running Bitcoin nodes, making pool operation accessible to users without extensive technical backgrounds.

Umbrel serves as a comprehensive node management platform that handles Bitcoin Core installation, synchronization, and ongoing maintenance through a web-based interface. The platform's app store model allows for easy installation of additional services, including mining pool software, through simple point-and-click operations. This architecture ensures that users can focus on pool operation rather than system administration, while still maintaining full control over their Bitcoin infrastructure.

### Public Pool Installation and Configuration

Installing public pool software through the Umbrel platform demonstrates the streamlined nature of modern Bitcoin infrastructure deployment. The process begins with accessing the Umbrel app store through the web interface, where a simple search for "public pool" reveals the available mining pool software. Installation requires only a few clicks: selecting the application, confirming installation, and waiting for the automated setup process to complete.

The installation process automatically configures the necessary connections between the public pool software and the underlying Bitcoin node. This integration ensures that the pool can validate transactions, construct block templates, and distribute work to connected miners without requiring manual configuration of complex networking parameters. Once installation completes, the pool interface becomes immediately accessible through the local network, providing real-time monitoring and management capabilities.

### Connecting Miners and Network Considerations

Connecting mining hardware to your newly established pool requires configuring the miner's pool settings to point to your local infrastructure. This involves replacing the default pool address with your local IP address and the appropriate port number assigned during the public pool installation. The configuration change redirects your mining hardware's computational efforts from external pools to your home-based infrastructure, allowing you to retain full control over mining operations and potential rewards.

Network configuration plays a crucial role in pool accessibility and functionality. Local network setup typically involves standard IP addressing, but users may encounter variations in DNS resolution depending on their router configuration. Some routers provide local DNS services that create friendly names for local services, while others require direct IP address access. For broader accessibility beyond the local network, port forwarding configuration on the router may be necessary, though this introduces additional security considerations that require careful evaluation of the associated risks and benefits.

The successful establishment of a home mining pool represents a significant step toward decentralized Bitcoin infrastructure, providing both educational value and practical mining capabilities while maintaining complete control over your Bitcoin operations.

# Hardware Assembly and Troubleshooting
<partId>f6987088-5ba4-52e2-b2d0-aa122080940c</partId>

## What tools to use?
<chapterId>733935b5-0171-5a22-838c-e192df6f7ccf</chapterId>

:::video id=bddd0e47-7b43-4685-ba2e-bf3a8ff653c9:::

In the world of surface-mount device (SMD) soldering, particularly when working with Bitaxe projects, having the right tools makes the difference between frustration and success. This comprehensive guide covers the essential equipment needed to tackle SMD soldering projects effectively, from basic hand tools to specialized equipment that will elevate your soldering capabilities.

If you want to refer to some documentation about the schematics, check this [GitHub repo](https://github.com/skot/bitaxe-doc/tree/main). 

### Basic Hand Tools and Precision Instruments

The foundation of any SMD soldering setup begins with quality tweezers, which serve as your primary component placement tools. Two types of tweezers prove most valuable in this work: standard straight-tip tweezers and those with a slight bend at the tip. The straight-tip variety handles most SMD components found in typical Bitaxe kits, while the bent-tip tweezers excel when working with extremely small components that require precise positioning. These tools often come included with repair kits, such as iFixit sets designed for phone repairs, making them readily accessible to most hobbyists.

Complementing the tweezers, a good pair of scissors becomes indispensable for cutting electrical tape, which serves multiple purposes in electronics projects. Electrical tape provides essential insulation for cables and components, and having quality tape readily available streamlines the soldering process. These basic supplies can be sourced from hardware stores or online retailers without requiring specialized electronics suppliers.

### Solder Paste Application and Management

The application of solder paste represents one of the most critical aspects of SMD soldering, and the right tools make this process both accurate and enjoyable. Small, non-sharp syringes filled with solder paste provide exceptional control over paste placement. This method allows for precise application of the exact amount of solder paste needed for each joint, and most people quickly develop the proper technique for controlling pressure and flow rate through hands-on practice.

The choice of solder paste itself significantly impacts soldering success. ChipQuik TS391SNL50 stands out as an exceptional solder paste for Bitaxe projects and general SMD work. This paste maintains proper consistency and melting characteristics, avoiding the problems associated with cheaper alternatives that have excessively low melting points. Low-quality solder pastes can create issues where previously soldered joints become fluid again when heating adjacent areas, leading to component displacement and poor connections. While quality solder paste represents a higher initial investment, the improved results and reduced frustration justify the expense.

### Problem-Solving and Cleanup Tools

Even experienced solderers encounter issues that require correction, making desoldering equipment essential for any complete toolkit. A desoldering rig, essentially a heated vacuum tool, removes excess solder and corrects bridged connections between component pins. These tools work most effectively when combined with flux, which improves solder flow and helps the desoldering process work more efficiently.

Flux comes in various forms, including solid and liquid varieties, and serves multiple purposes beyond desoldering assistance. When solder paste begins to lose its effectiveness during extended work sessions, applying additional flux restores proper flow characteristics and ensures reliable connections. A small spoon-like tool, often found in precision repair kits, facilitates accurate flux application to specific areas without contaminating surrounding components.

Board cleanup represents the final step in professional-quality work, requiring isopropanol alcohol and a dedicated cleaning brush. An old toothbrush works perfectly for this purpose, and a squeeze bottle containing isopropanol allows controlled application of cleaning solution. This combination removes flux residue and paste remnants, leaving boards with a clean, professional appearance that also facilitates inspection of solder joints.

### Specialized Equipment and Advanced Tools

For projects involving complex integrated circuits, particularly ASICs, stencils transform the soldering process from tedious hand-placement to efficient, accurate paste application. These precision-cut templates ensure consistent paste thickness and placement, dramatically reducing the time required for complex components while improving reliability. The investment in quality stencils pays dividends in both time savings and improved results.

Thermal management becomes crucial when working with power components, making thermal paste or thermal grease essential supplies. These materials ensure proper heat transfer between heat sinks and integrated circuits, preventing thermal damage and ensuring reliable operation. Quality thermal interface materials represent a small investment that protects much more expensive components.

The heart of any SMD soldering setup is the hot air rework station, which provides the controlled heat necessary for surface-mount work. While budget stations in the $30-50 range can perform adequately, they often lack the reliability and precision of higher-end equipment. These entry-level stations typically operate effectively at 355°C and include automatic temperature reduction when the handpiece is returned to its holder. However, their reliability can be inconsistent, with some units failing prematurely. For serious work, investing in higher-quality equipment from specialized electronics suppliers provides better long-term value through improved reliability and more precise temperature control.

The combination of these tools creates a complete SMD soldering capability that extends far beyond Bitaxe projects to general electronics work. Understanding each tool's role and selecting quality equipment appropriate to your skill level and project requirements ensures successful outcomes and an enjoyable soldering experience.


## Fix solder issues
<chapterId>96663744-b4f7-5154-930f-a68ba7954603</chapterId>

:::video id=9286c0dc-acd6-44d9-b34e-59cfb2da9748:::


The Bitaxe transceiver kit presents unique challenges during assembly that require careful attention to component orientation, solder bridge prevention, and proper heat management. Understanding these common issues and their solutions is essential for successful kit construction and avoiding costly component damage. This chapter examines the most frequent soldering problems encountered during Bitaxe assembly and provides practical techniques for identifying and resolving them.

### Component Orientation and Identification

Proper component orientation represents one of the most critical aspects of successful Bitaxe assembly, particularly with MOSFETs Q1 and Q2. These components feature distinctive orientation markers that must be carefully observed during installation. Each MOSFET contains a small dot marking that corresponds to specific pad arrangements on the circuit board. The key to correct orientation lies in understanding the physical structure of these components, which feature four pins arranged with one large pad and three smaller pads that have no connection to the large pad.

When installing Q1 and Q2, examine both the component and the circuit board carefully. The board layout clearly shows the intended orientation through its pad configuration, with four pins positioned to match the MOSFET structure. Before soldering any large component, always verify orientation by comparing the component's physical markers with the board's pad arrangement. This simple verification step prevents the frustration of desoldering and reinstalling incorrectly oriented components.

The consequences of incorrect orientation extend beyond simple functionality issues. Wrongly oriented MOSFETs can create circuit malfunctions that are difficult to diagnose and may require complete component replacement. Taking time to verify orientation before applying heat ensures proper circuit operation and prevents unnecessary troubleshooting later in the assembly process.

### Managing Solder Bridges and Excess Solder

Solder bridges represent another common challenge in Bitaxe assembly, particularly around fine-pitch components like U10. These unwanted connections between adjacent pins can cause circuit malfunctions and require careful removal techniques. The most effective approach involves using desoldering wick, a copper braided material that absorbs excess solder when heated. This technique requires patience and proper tool selection to avoid damaging delicate components.

When addressing solder bridges on integrated circuits, employ a PCB holder or articulated clamp to securely hold the component while working. Apply gentle heat to the affected area and carefully draw the desoldering wick across the bridged connections. The copper braid naturally absorbs the excess solder, separating the unwanted connections. This process may require multiple attempts, but persistence yields clean, properly separated connections.

Prevention remains the best approach to solder bridge management. Using appropriate amounts of solder paste and maintaining steady hand control during component placement significantly reduces bridge formation. When bridges do occur, address them immediately rather than hoping they won't affect circuit operation. Even seemingly minor bridges can cause significant functionality problems that are difficult to diagnose once the board is fully assembled.

### Critical Components and Special Considerations

The buck converter U9 deserves particular attention due to its critical role in converting 5 volts to 1.2 volts for the ASIC chip. This component presents unique challenges due to its five small connections and tendency toward failure. Proper installation requires precise solder paste application and careful heat management. Insufficient solder paste under U9 can result in poor connections that prevent proper voltage conversion, while excess paste can create bridges that cause circuit malfunction.

U9 produces distinctive audio signatures when experiencing solder bridge issues, generating high-frequency noise that differs from normal ASIC operation. This auditory diagnostic technique can help identify problems, though it requires good high-frequency hearing to detect. When audio diagnosis isn't possible, visual inspection becomes essential. Examine all connections carefully, looking for bridges or insufficient solder coverage.

If U9 fails to output the required 1.2 volts despite appearing properly soldered, consider insufficient solder paste as the likely cause. Remove the component, apply a small amount of additional solder paste, and reinstall. In cases where individual pins lack adequate solder coverage, carefully apply small amounts of solder paste to specific locations using tweezers. The solder paste will naturally flow under the component when heated, creating proper connections through capillary action.

### Heat Management and Component Protection

Proper heat management protects sensitive components from thermal damage while ensuring reliable solder joints. Components like the crystal oscillator Y1 and U1 are particularly sensitive to prolonged heat exposure and require careful temperature control. Maintain soldering iron temperature at 350 degrees Celsius, but minimize heat application time to prevent component damage. Quick, efficient soldering techniques protect these sensitive components while achieving reliable connections.

The ASIC chip requires special handling techniques due to its complex pin structure and sensitivity to mechanical stress. When using stencils for solder paste application, ensure even coverage across all pins to prevent uneven component seating. If excessive solder paste causes the ASIC to sit unevenly, allow the assembly to cool completely before making corrections. Apply gentle pressure only to the component's labeled edges, never to the central die area, while reheating to achieve proper seating.

Component U8 presents unique challenges due to its numerous pins and potential for bent leads. When pins become bent during handling, use a PCB holder or articulated clamp to secure the component and carefully straighten the affected pins. Work slowly and patiently to avoid breaking the delicate leads. Understanding that certain pin groups on U8 are internally connected can simplify troubleshooting, as bridges between these specific pins don't affect circuit operation. However, bridges between other pins require careful removal to ensure proper functionality.

## How to debug your Bitaxe using AxeOS
<chapterId>603f5c0d-4b7c-51e1-9bad-318a8b8e9db7</chapterId>
:::video id=d23d748b-510e-4748-9617-b875da757031:::

When working with Bitaxe mining devices, hardware failures can manifest in various ways that may not be immediately obvious. Understanding how to systematically diagnose these issues using the AxeOS operating system can save significant time and prevent unnecessary component replacements. This chapter explores the diagnostic techniques and troubleshooting methodologies that experienced technicians use to identify specific hardware problems through software analysis.

### Understanding Power Consumption Indicators

The first and most critical diagnostic indicator in AxeOS is power consumption monitoring. Normal Bitaxe devices, including the Bitaxe Ultra and Bitaxe Supra models, typically consume between 10 to 17 watts during standard operation. This baseline measurement serves as your primary health indicator for the entire system. When power consumption drops significantly below this range, particularly below 3 watts, it signals a fundamental problem with the ASIC chip or its supporting circuitry.

Low power consumption scenarios require immediate attention because they indicate that the mining chip is either completely non-functional or operating in a severely degraded state. This measurement alone can help you quickly differentiate between performance issues and complete hardware failures. The power reading in AxeOS provides real-time feedback that allows you to monitor the effectiveness of any repair attempts you make to the device.

### Analyzing ASIC Voltage Measurements

The ASIC voltage measurement feature in AxeOS provides crucial diagnostic information that helps pinpoint the exact nature of hardware problems. When examining voltage readings, you need to understand the relationship between measured voltage and requested voltage to properly diagnose issues. The system displays both the voltage being delivered to the ASIC chip and the voltage that the chip is requesting from the power management system.

When you observe an ASIC voltage measurement of exactly 1.2 volts combined with power consumption below 3 watts, this specific combination indicates either a soldering problem with the ASIC chip or a completely failed ASIC. This voltage reading suggests that power is reaching the chip location, but the chip itself is not functioning properly. Physical inspection of the ASIC die can reveal cracks or other visible damage that would explain this behavior pattern.

A different diagnostic scenario emerges when you see low power consumption paired with very low requested voltage readings, such as 100 millivolts or 0.5 volts. This pattern indicates that the ASIC chip is not receiving adequate voltage supply, which typically points to problems with the U9 buck converter component. The buck converter is responsible for providing the precise voltage regulation that ASIC chips require for proper operation.

### Interpreting Log Data and ASIC Communication

The AxeOS logging system provides valuable insight into whether your ASIC chip is communicating with the control system. When you access the logs through the "show logs" function, the presence of "ASIC results" entries confirms that the chip is not only powered but also actively processing work and returning results. This communication indicates that the ASIC is properly soldered and maintaining its connection to the control circuitry.

The absence of ASIC results in the logs, particularly when combined with other symptoms, helps narrow down the problem to specific components or connection issues. This diagnostic approach allows you to distinguish between chips that are completely non-responsive and those that may have intermittent connection problems. The log analysis becomes particularly valuable when troubleshooting complex issues where multiple symptoms might suggest different root causes.

### Systematic Troubleshooting Approach

When diagnosing Bitaxe hardware issues, following a systematic approach prevents overlooking critical problems and ensures efficient repair processes. Begin by documenting the power consumption and voltage readings, then correlate these measurements with the log data to build a complete picture of the system's behavior. This methodical approach helps identify whether problems stem from the ASIC chip itself, the power delivery system, or the communication pathways between components.

For cases where the U9 buck converter appears to be the problem, physical inspection and potential resoldering may be necessary. The U9 component is particularly susceptible to soldering issues, especially in first-time assembly situations. When voltage regulation problems are suspected, using a multimeter to verify that 1.2 volts is actually present at the ASIC pins provides definitive confirmation of power delivery issues. If voltage is present at the pins but the ASIC still doesn't function, and physical inspection reveals no damage, replacing the ASIC chip becomes the next logical step. Should problems persist even after ASIC replacement, the U2 component, which drives the ASIC chip, may require attention as the final element in the troubleshooting sequence.

## How to debug using USB?
<chapterId>f3182763-e1ef-5460-8bc0-f2ea53e3a410</chapterId>

:::video id=fe1b4b48-5f8a-4fd7-9417-ca03a36bce9f:::


When troubleshooting Bitaxe mining devices, having direct access to the device's internal logging system provides invaluable insights that web-based interfaces cannot offer. This chapter explores how to establish a direct USB serial connection to your Bitaxe device using the ESP-IDF framework, enabling real-time monitoring of system logs, boot sequences, and error messages. This debugging approach is particularly crucial when dealing with devices that experience frequent reboots or hardware failures, as it captures all diagnostic information that might be lost during system restarts.

The debugging process requires Visual Studio Code with the ESP-IDF extension, though any compatible IDE can be used. This method works with all Bitaxe variants that include a USB port, including the Bitaxe Ultra 204 and other models in the series. The direct serial connection bypasses potential web interface limitations and provides unfiltered access to the device's internal state information.

### Setting Up Serial Communication

Establishing communication with your Bitaxe device begins with connecting the USB cable and opening the ESP-IDF terminal within your development environment. The command `idf.py monitor` initiates the connection process, automatically scanning available COM ports to establish UART communication with the ESP32 chip on your Bitaxe device. The system typically cycles through available ports (COM3, COM4, COM16, etc.) until it finds the correct connection.

Once connected, the terminal displays the complete boot sequence and ongoing operational logs. The initial connection process may take several moments as the system identifies the correct communication port. If automatic port detection fails, you can manually specify the COM port through the IDE's port selection interface. This direct communication channel remains active throughout the device's operation, providing continuous access to system diagnostics and performance metrics.

### Interpreting Boot Sequence and Normal Operation Logs

The boot sequence provides critical information about your Bitaxe device's hardware configuration and initialization process. Normal startup logs begin with ESP-IDF version information, followed by the distinctive "Welcome to the Bitaxe. Hack the planet" message that confirms successful firmware loading. The system then displays ASIC frequency configuration, device model identification, and board version details.

A properly functioning device will show successful I2C initialization and ASIC voltage regulation set to 1.2 volts. The logs display GPIO status information and Wi-Fi initialization sequences, followed by DHCP server configuration and IP address assignment. One of the most crucial indicators is the ASIC chip detection message, which should report "detected one ASIC chip" for a single-chip device. This confirmation validates that the mining hardware is properly connected and communicating with the ESP32 controller.

The operational logs reveal multiple concurrent tasks running on the device, including stratum API communication, main task coordination, ASIC task management, and stratum task processing. These different task identifiers help isolate issues to specific system components. Normal operation includes pool connection establishment, difficulty adjustment messages, job queuing and dequeuing, and nonce generation reporting. Successful mining operations display ASIC results with difficulty calculations and mining submit confirmations when shares meet the required threshold.

### Identifying Hardware Failures and Error Patterns

Hardware failures manifest in the logs through specific error patterns that indicate which components are malfunctioning. The most common failure mode involves I2C communication errors with specific integrated circuits on the Bitaxe board. For example, DS4432U communication failures appear as "ESP_ERROR_CHECK failed" messages with timeout indicators, pointing to voltage regulation issues or soldering problems affecting the U10 component responsible for display communication.

These error messages include detailed debugging information such as the specific source file (main_ds4432u.c), the failing function call, and the processor core handling the task. The backtrace information provides additional context for advanced troubleshooting. Similar error patterns can occur with the EMC2101 temperature and fan control chip, each generating distinctive log signatures that help identify the failing component.

Physical hardware issues often present as repeated error cycles followed by system reboots. If your device produces audible noise during operation, this typically indicates soldering problems such as bridges between component pins or inadequate solder joints. While these mechanical issues may not always generate specific log entries, they create unstable operating conditions that manifest as frequent crashes and restart cycles in the monitoring output.

### Advanced Troubleshooting Strategies

Serial monitoring provides several advantages over web-based debugging interfaces, particularly for intermittent failures or devices experiencing frequent reboots. The continuous log capture ensures that no diagnostic information is lost during system restarts, unlike web interfaces that may lose data during disconnection events. This comprehensive logging capability makes it possible to identify patterns in failures and correlate specific error conditions with hardware or environmental factors.

When analyzing problematic devices, focus on the sequence of events leading to failures rather than isolated error messages. Successful ASIC communication should show regular job processing, nonce generation, and share submission cycles. Missing ASIC results in the logs indicate communication failures between the ESP32 and the mining chip, often caused by power supply issues, damaged traces, or component failures.

For systematic troubleshooting, document error patterns and component-specific failures before seeking community support. The detailed error logs, including specific chip identifiers and failure modes, enable experienced users to provide targeted repair guidance, such as component replacement procedures or soldering corrections. This methodical approach to hardware debugging significantly improves repair success rates and reduces troubleshooting time for complex issues.

# Advanced Customization
<partId>8d333102-ecb5-5f05-bfb5-03a27b2d0d70</partId>

## Modify the PCB
<chapterId>ca08d2a4-2b34-575b-aecc-7482a03c190e</chapterId>

:::video id=30fb0010-f560-4e96-a05b-c21dc172746e:::

KiCad represents one of the most powerful open-source tools available for printed circuit board (PCB) design and routing. This professional-grade software enables engineers and hobbyists to create complex electronic designs by placing components on virtual boards and routing the intricate traces that connect these components together. What makes KiCad particularly valuable for educational and development purposes is its complete open-source nature, allowing users to modify, customize, and learn from existing designs without licensing restrictions.

The Bitaxe project exemplifies the power of open-source hardware development, providing a complete PCB design that users can examine, modify, and customize according to their specific needs. This accessibility creates an excellent learning environment where students and practitioners can explore real-world PCB designs while developing their understanding of electronic systems. The ability to customize visual elements like logos provides an approachable entry point for users who may be intimidated by the technical complexity of electronic design.

### Setting Up Your KiCad Environment

Before beginning any customization work, proper setup of your development environment is essential. The Bitaxe repository must be downloaded to your local machine, typically accomplished through GitHub's ZIP download functionality. This repository contains all the necessary project files, including the KiCad project files, component libraries, and design documentation required for successful modification.

KiCad installation should be completed using the official distribution from the KiCad website, ensuring compatibility with the project files and access to the latest features. Once both the repository and KiCad are properly installed, opening the project requires navigating to the Bitaxe Ultra KiCad project file within the downloaded repository structure. This project file serves as the central hub that links all associated design files, component libraries, and configuration settings.

The initial view of a complex PCB design can appear overwhelming, with numerous components, traces, and layers creating a dense visual landscape. However, KiCad's 3D viewer functionality provides an invaluable tool for understanding the physical layout and spatial relationships within the design. This three-dimensional perspective transforms the abstract schematic representation into a realistic visualization of the final manufactured product, making it easier to comprehend component placement and overall design aesthetics.

### Logo Customization Process

Customizing logos on PCB designs represents one of the most accessible modifications for users new to KiCad, requiring minimal technical knowledge while providing immediate visual results. The process begins with the image converter tool, which transforms standard image files into footprint formats compatible with PCB design software. This conversion process requires careful attention to sizing parameters, typically measured in millimeters to ensure proper scaling on the final manufactured board.

The image converter workflow involves several critical steps that determine the final appearance and placement of custom logos. Source image selection should prioritize high-contrast designs that will translate well to the silkscreen printing process used in PCB manufacturing. Size specification becomes crucial, as logos must be large enough to remain legible after manufacturing while not interfering with component placement or functionality. The choice between front and back silkscreen layers affects both visibility and manufacturing considerations.

Footprint library management represents a fundamental aspect of KiCad customization, requiring users to understand how the software organizes and accesses design elements. Adding custom logos involves creating new footprint libraries or modifying existing ones, then properly linking these libraries within the project structure. This process ensures that custom elements remain accessible across different design sessions and can be easily shared with other team members or collaborators.

### Advanced Design Exploration and Understanding

Beyond simple logo customization, KiCad provides powerful tools for exploring and understanding complex PCB designs. The layer management system allows users to selectively view different aspects of the design, from component placement and routing to manufacturing specifications and assembly information. This layered approach enables detailed analysis of specific design elements without visual clutter from unrelated components.

Trace routing analysis represents one of the most educational aspects of PCB exploration, revealing how electrical connections flow between components and subsystems. By following individual traces or groups of related signals, users can develop understanding of circuit functionality and design decisions. For example, examining power distribution networks reveals how voltage regulation and filtering components work together to provide clean, stable power to sensitive electronic components.

The relationship between schematic design and physical layout becomes apparent through careful examination of component placement and routing decisions. Understanding why specific components are positioned in particular locations, how thermal considerations influence layout decisions, and how signal integrity requirements drive routing choices provides valuable insights into professional PCB design practices. This knowledge proves invaluable for users developing their own designs or modifying existing ones for specific applications.

KiCad's comprehensive design rule checking and verification tools ensure that modifications maintain electrical and manufacturing compatibility. These automated systems help prevent common design errors while educating users about industry standards and best practices. The integration of 3D visualization with electrical design data creates a powerful learning environment where theoretical concepts become tangible through visual representation and interactive exploration.

## How to create a factory file?
<chapterId>e9da631c-e6d1-50c1-bb59-bc8455c29d3e</chapterId>

:::video id=07f980bf-6052-4ed4-bf7b-75e8aba585df:::

Building custom firmware for ESP-based mining devices requires careful attention to configuration, dependencies, and the proper build process. This comprehensive guide walks through the complete process of creating both standard firmware binaries and factory files that include pre-configured settings, making deployment more efficient and reducing setup time for end users.

Note that this chapter is quite technical and can be simply skimmed through for if you are curious about it.

### Setting Up the Development Environment

To start some ESP-Miner firmware development you should with establishing the proper development environment in Visual Studio Code, ideally on a linux distribution. The ESP-IDF extension serves as the cornerstone of this setup, providing the necessary tools and framework integration for ESP32 development. When installing the ESP-IDF extension for the first time, users encounter a setup guide that facilitates the configuration process.

A critical consideration in the setup process involves selecting the appropriate ESP-IDF version. While version 5.1.3 was previously recommended, practical experience has revealed that this version can cause build issues that complicate the development process. The recommended approach now involves using ESP-IDF version 5.3 Beta 1, which has proven to resolve these building complications and ensures that Bitaxe devices function properly. The installation process requires selecting the Express installation option and specifically choosing version 5.3 Beta 1 from the available options.

The development environment setup extends beyond the ESP-IDF installation to include proper terminal configuration. Visual Studio Code provides multiple methods for accessing ESP-IDF functionality, including the command palette option to open an ESP-IDF terminal or using the dedicated terminal icon located in the interface. This specialized terminal environment ensures that all ESP-IDF commands function correctly and provides access to the complete toolchain.

### Configuring the ESP-Miner Settings

The configuration file represents the heart of the ESP-Miner customization process, containing all the essential parameters that define how the device will operate in its target environment. This configuration encompasses network settings, mining pool connections, and hardware-specific parameters that must be tailored to the specific deployment scenario.

Network configuration forms the primary component of the setup process, requiring the specification of Wi-Fi credentials including the SSID and password. Rather than using placeholder values like "test," production configurations should include the actual network credentials that the device will use in its operational environment. The configuration also accommodates various mining pool setups, supporting both private pool configurations with specific IP addresses and public pools like public-pool.io with their corresponding port settings.

Mining-specific configuration parameters include the stratum user setting, which typically corresponds to the Bitcoin address where mining rewards should be directed. Additional hardware parameters such as frequency settings, voltage configurations, and ASIC type specifications must align with the target hardware platform. The GitHub repository provides pre-configured examples for different hardware variants, such as the BM1368 configuration designed for Super devices and BM1366 settings for Ultra variants. Board version specifications, such as setting the port version to 401 for newer hardware revisions, ensure compatibility with the target device's specific characteristics.

### Building the Web Interface and Core Firmware

The ESP-Miner project incorporates a sophisticated web interface that requires separate compilation before the main firmware build process can commence. This web interface, referred to as the AxeOS firmware, provides users with a comprehensive management interface for monitoring and controlling their mining devices.

The web interface build process begins by navigating to the HTTP server directory within the main repository structure, specifically the AxeOS subdirectory. This location contains the Node.js-based web application that requires dependency installation through the npm install command. The build system assumes that Node.js is properly installed on the development system, as this represents a fundamental requirement for the web interface compilation process.

Following the dependency installation, the npm run build command compiles the web interface components, creating the necessary files that will be embedded into the ESP32 firmware. This compilation process generates optimized web assets that provide the user interface functionality while maintaining efficient memory usage on the constrained ESP32 platform. The successful completion of this build step is essential before proceeding to the main firmware compilation, as the ESP-Miner firmware incorporates these web interface components as integral functionality.

### Creating Factory Files with Embedded Configuration

The creation of factory files represents an advanced deployment strategy that embeds configuration settings directly into the firmware binary, eliminating the need for manual configuration during device setup. This approach proves particularly valuable for large-scale deployments or situations where consistent configuration across multiple devices is essential.

The factory file creation process begins with generating a configuration binary from the CSV configuration file using the ESP-IDF's NVS partition generator tool. This tool, located within the ESP-IDF components directory under nvs-flash/nvs-partition-generator, converts the human-readable configuration into a binary format suitable for direct flash memory storage. The nvs-partition-gen.py script processes the config.csv file and generates a config.binary file that targets the 0x6000 memory address space.

The final assembly of factory files utilizes specialized merge scripts that combine the core firmware binaries with the configuration data. The repository provides multiple merge options, including a standard merge script for basic factory files and a configuration-inclusive merge script for comprehensive factory files. The merge-bin-with-config.sh script creates factory files that include both the firmware functionality and the pre-configured settings, resulting in a complete deployment package. This approach enables the creation of device-specific factory files, such as versions tailored for Bitaxe Ultra devices with specific board revisions, while maintaining the flexibility to generate generic factory files without embedded configurations for scenarios requiring manual setup flexibility.

The completed factory files provide deployment teams with ready-to-flash binaries that include all necessary firmware components and configuration settings, streamlining the device provisioning process and ensuring consistent operational parameters across deployed mining devices.

## How to use the Bitaxe Web Flasher?
<chapterId>8c3e2d4c-c038-53ec-93cb-cc30a29e4394</chapterId>

:::video id=291757b9-f459-48f6-8766-56387f907859:::

The Bitaxe Web Installer represents a streamlined approach to firmware management for Bitaxe devices, providing users with multiple installation options through a web-based interface. This comprehensive tool eliminates the complexity traditionally associated with firmware updates and fresh installations, making device management accessible to users regardless of their technical expertise. Understanding the proper use of this installer is crucial for maintaining optimal device performance and avoiding common pitfalls that can render devices temporarily inoperable.

### Accessing and Browser Compatibility Requirements

The Bitaxe Web Installer is accessible through the dedicated URL [https://bitaxeorg.github.io/bitaxe-web-flasher/](https://bitaxeorg.github.io/bitaxe-web-flasher/) (the one presented in the video in now deprecated), serving as the central hub for all firmware installation activities. However, successful operation of this web-based tool requires browser compatibility, as the installer relies on specific web technologies that are not universally supported across all browsers. Chrome stands as the primary recommended browser for the installer, providing full compatibility with all features and functions. While other Chromium-based browsers may offer similar functionality, popular alternatives like Brave and Firefox lack the necessary web serial API support, making them incompatible with the installer's core operations.

This browser limitation stems from the installer's reliance on direct serial communication with Bitaxe devices through the web interface. The web serial API, which enables this communication, remains a relatively new web standard that has not yet achieved universal browser adoption. Users attempting to access the installer through unsupported browsers will encounter connection failures and inability to communicate with their devices, necessitating a switch to a compatible browser before proceeding with any installation activities.

### Power Requirements and Device Preparation

Bitaxe devices exhibit different power requirements depending on their specific model and version, making proper power management essential for successful firmware installation. Devices running version 204 or below can operate solely through USB power, drawing sufficient current from the connected computer to maintain operation during the flashing process. This simplified power arrangement makes these earlier versions particularly convenient for firmware updates, as users need only connect a single USB cable to begin the installation process.

However, devices running version 205 and above require external power sources in addition to the USB connection, reflecting changes in power consumption and circuit design in newer hardware revisions. These devices cannot draw adequate power through USB alone, necessitating connection to their standard power supplies during firmware installation. Failure to provide adequate power to these newer devices will result in installation failures and potential corruption of the firmware update process.

The physical connection process requires specific timing and button manipulation to ensure proper communication between the installer and the device. Users must press and hold the boot button on their Bitaxe device before connecting the USB-C cable to their computer. This sequence places the device into bootloader mode, enabling the installer to communicate directly with the device's firmware storage. Connecting the USB cable before engaging the boot button will result in normal device operation rather than the bootloader mode required for firmware installation, preventing the installer from establishing the necessary communication channel.

### Installation Options and Their Applications

The Bitaxe Web Installer provides four distinct installation options, each designed for specific use cases and device configurations. The Bitaxe Superboard version 4.0.1 represents the most current firmware for Super model devices, with version 4.0.2 scheduled for future release. This option includes both factory and update variants, providing flexibility in installation approach based on user needs and device status.

Factory installations represent complete firmware replacements that mirror the original manufacturing process, including comprehensive self-test procedures that verify device functionality across all systems. When users select a factory installation, the installer performs a complete erasure of existing firmware and configuration data, replacing it with a fresh, clean installation identical to what would be applied during manufacturing. This process includes automated self-testing that validates proper hardware operation, requiring users to reboot their devices upon completion before normal operation can resume. Factory installations prove particularly valuable when devices experience persistent issues or when users desire to return their devices to original factory specifications.

Update installations provide a more conservative approach, preserving existing configuration data while updating only the core firmware components. This option proves ideal for users who have customized their device settings and wish to maintain their personal configurations while benefiting from firmware improvements and bug fixes. The update process targets only the firmware components that require modification, leaving user-specific settings, WiFi credentials, and Bitcoin addresses intact throughout the installation process.

### Critical Installation Considerations and Data Protection

The distinction between factory and update installations carries significant implications for device configuration and user data preservation. Factory installations perform complete device erasure, removing all user-configured settings including WiFi credentials, Bitcoin addresses, and any personalized device parameters. Following a factory installation, users must reconnect to the device's default WiFi network and reconfigure all personal settings from scratch, essentially treating the device as if it were brand new from the manufacturer.

Update installations require careful attention to the erase device option presented during the installation process. The installer will prompt users with the question "Do you want to erase the device before installing Bitaxe Flasher?" accompanied by a warning that all data on the device will be lost. Users performing update installations must decline this option by clicking "Next" rather than confirming the erase operation. Accepting the erase option during an update installation will remove the device's configuration file, potentially rendering the device non-functional until proper configuration is restored. While this situation does not permanently damage the device, it creates unnecessary complications and requires additional configuration steps to restore normal operation.

The installation process itself proceeds automatically once users have made their selections and confirmed their choices. The installer handles all technical aspects of firmware transfer and verification, providing progress indicators and status updates throughout the process. This automated approach eliminates the need for users to understand complex firmware installation procedures while ensuring reliable and consistent results across different device models and firmware versions.

## How to create and order the PCB?
<chapterId>566f5e06-9ec9-55c0-84f6-101d6ca4c2ff</chapterId>

:::video id=9a56ad84-d9cf-4f85-ab98-301fb3101228:::

This chapter focuses on the practical process of generating manufacturing files from KiCad projects and ordering professional PCBs from online manufacturers. Using the Bitaxe project as our example, we'll walk through the complete workflow from file generation to placing an order with a PCB manufacturer.

### Understanding the PCB Manufacturing Process

The journey from a completed KiCad design to a physical PCB involves several critical steps that bridge the gap between digital design and physical manufacturing. When working with complex projects like the Bitaxe, the PCB editor in KiCad provides a comprehensive view of your design, displaying all components and their interconnections through colored traces. The red and blue lines you see represent the electrical connections between different integrated circuits and components on the board. KiCad's 3D viewer feature allows you to visualize how the final assembled board will appear, providing valuable insight into component placement and potential mechanical conflicts.

The manufacturing process requires specific file formats that PCB manufacturers can interpret and use to fabricate your boards. These files contain precise information about copper layers, drill holes, component placement, and other manufacturing specifications. Understanding this workflow is essential whether you're working with the standard Bitaxe design or creating modifications such as adding custom logos, changing component values, or adjusting the board layout to meet specific requirements.

### Generating Gerber Files for Manufacturing

Gerber files serve as the industry standard for communicating PCB design information to manufacturers. These files contain all the necessary data for fabricating your PCB, including copper layer patterns, solder mask definitions, and drill hole locations. To generate these files in KiCad, navigate to the PCB editor and access the fabrication outputs through the Files menu. The software automatically configures the appropriate settings for standard manufacturing processes, including the proper output directory structure typically organized as "manufacturing files/gerbers."

The generation process creates multiple Gerber files, each representing different aspects of your PCB design. These files work together to provide manufacturers with complete fabrication instructions. Once generated, these files must be compressed into a ZIP archive, as this is the standard format expected by most PCB manufacturers. The ZIP file contains all necessary manufacturing data and ensures that no files are lost or corrupted during the upload process to the manufacturer's website.

It's worth noting that many open-source projects, including the Bitaxe, often include pre-generated manufacturing files in their repositories. However, understanding how to generate these files yourself is crucial when making design modifications or working with different board versions. This knowledge becomes particularly valuable when customizing designs or troubleshooting manufacturing issues.

### Selecting PCB Manufacturers and Understanding Options

The PCB manufacturing landscape offers several reputable options, with JLCPCB and PCBWay being among the most popular choices for hobbyists and professionals alike. Both manufacturers provide similar services with competitive pricing and reliable quality, though each has specific advantages depending on your project requirements. JLCPCB often attracts first-time users with promotional pricing and user-friendly interfaces, while PCBWay may offer different material options or specialized services.

When uploading your Gerber files to a manufacturer's website, the system automatically analyzes your design and presents various manufacturing options. The default settings provided by these platforms are typically suitable for most standard designs, and it's generally recommended to maintain these settings unless you have specific requirements. Key parameters include PCB thickness, copper weight, surface finish, and minimum quantities. Most manufacturers require minimum orders of five boards, which actually works well for hobbyist projects where having spare boards or sharing with friends is beneficial.

Color options represent one of the few aesthetic choices available during the manufacturing process. While green remains the traditional and most cost-effective option, manufacturers typically offer alternatives including blue, red, yellow, purple, and black. The color choice is purely aesthetic and doesn't affect the electrical performance of your PCB, though some colors may have slight cost implications or longer manufacturing times.

### Advanced Manufacturing Considerations and Assembly Options

Beyond basic PCB fabrication, modern manufacturers offer additional services that can significantly streamline your project completion. Stencils represent one of the most valuable add-on services, particularly for designs with fine-pitch components like the ASIC chips found in Bitcoin mining projects. A stencil is essentially a precision-cut aluminum template with openings that correspond exactly to the solder pad locations on your PCB. This tool enables consistent and accurate application of solder paste, dramatically improving assembly quality and reducing the likelihood of soldering errors.

Stencil options typically include single stencils with both top and bottom patterns, or separate stencils for each side of the board. For most projects, a combined stencil proves more convenient and cost-effective. The stencil thickness is carefully calculated to deposit the appropriate amount of solder paste for your specific component types and pad sizes. Using a stencil transforms what could be a tedious and error-prone manual process into a quick and professional assembly step.

While some manufacturers offer partial or complete assembly services, these options require careful consideration for complex projects like the Bitaxe. Component availability, cost implications, and the educational value of self-assembly all factor into this decision. Many specialized components required for Bitcoin mining projects may not be readily available through standard PCB assembly services, making component sourcing and manual assembly the more practical approach. Future episodes in this series will cover component sourcing strategies and assembly techniques to help you successfully complete your Bitaxe project from bare PCB to functional device.

The manufacturing and assembly process represents a crucial bridge between digital design and physical implementation. Understanding these workflows empowers you to take control of your projects, reduce costs, and gain valuable hands-on experience with professional manufacturing processes. Whether you're building a single prototype or planning a small production run, mastering these skills opens up new possibilities for bringing your electronic designs to life.

# Performance Optimization
<partId>87b8790f-b7a9-5286-a7f8-328176ef7cb5</partId>

## Benchmark your Bitaxe
<chapterId>7259a4b1-93c1-5956-87d3-baaee58115af</chapterId>

:::video id=2491a783-9750-4ea5-a40c-1d1d611784d5:::

The pursuit of optimal mining performance requires a systematic approach to hardware configuration that balances hashrate, efficiency, and thermal management. The Bitaxe offer numerous configuration parameters that can significantly impact performance, but manually testing every combination of settings would be impractical and time-consuming. This chapter explores how to leverage automated benchmarking tools to scientifically optimize your Bitaxe's performance while maintaining safe operating conditions.

### Understanding Bitaxe Performance Metrics and Baseline Configuration

Before diving into optimization techniques, it's essential to understand the key performance indicators that define your Bitaxe's operational efficiency. The primary metrics include hashrate measured in terahash per second, power efficiency expressed in joules per terahash, ASIC frequency in megahertz, and core voltage in volts. A well-configured Bitaxe might achieve approximately 1.1 terahash with an efficiency of around 17 joules per terahash, operating at 550 megahertz with a measured ASIC voltage of 1.14 volts. These baseline numbers provide a reference point for understanding the potential improvements available through systematic optimization.

The relationship between these metrics is complex and interdependent. Higher frequencies typically increase hashrate but also increase power consumption and heat generation. Similarly, voltage adjustments affect both performance and thermal characteristics. The challenge lies in finding the optimal balance that maximizes either hashrate or efficiency while maintaining stable operation within safe temperature limits. This optimization process requires methodical testing across multiple parameter combinations, making automated tools invaluable for achieving optimal results.

### The Bitaxe Hashrate Benchmark Tool Architecture

The [Bitaxe Hashrate Benchmark](https://github.com/mrv777/Bitaxe-Hashrate-Benchmark/) tool represents a sophisticated Python-based solution originally developed by WhiteCookie and subsequently enhanced by mrv777. This open-source tool, distributed under the GPLv3 license, automates the complex process of testing multiple configuration combinations to identify optimal settings for your specific hardware. The tool's primary strength lies in its systematic approach to parameter testing, incrementally adjusting frequency and voltage settings while continuously monitoring performance metrics and thermal conditions.

The benchmarking process typically requires 30 to 40 minutes to complete, during which the tool methodically tests various combinations of ASIC frequency and voltage settings. The tool begins with conservative baseline settings, typically starting at 1.15 volts and 500 megahertz, then incrementally increases these parameters while monitoring hashrate, temperature, and stability. Importantly, the tool prioritizes safe operation over maximum performance, automatically backing down from settings that cause excessive heat generation or instability. This conservative approach ensures that the optimization process doesn't compromise hardware longevity or reliability.

### Installation and Setup Requirements

Implementing the Bitaxe Hashrate Benchmark tool requires several prerequisite software components on your local computer. The primary requirements include Python for executing the benchmarking scripts, Git for repository management, and optionally Visual Studio Code for enhanced development environment capabilities. While the tool can be operated from command line interfaces, using an integrated development environment like VS Code provides better visibility into the benchmarking process and results analysis.

The installation process follows standard Python development practices, beginning with cloning the repository from GitHub to your local machine. Once the repository is downloaded, you'll need to create a virtual environment to isolate the tool's dependencies from your system's Python installation. This isolation prevents potential conflicts with other Python applications and ensures consistent operation. After activating the virtual environment, you'll install the required dependencies using the provided requirements file, which automatically configures all necessary libraries and modules for proper tool operation.

### Executing Benchmarks and Interpreting Results

Running the benchmark requires executing a single Python command that includes your Bitaxe's IP address as a parameter. The tool automatically connects to your miner's web interface and begins the systematic testing process. During execution, the tool provides detailed logging information showing the current test iteration, applied voltage and frequency settings, resulting hashrate, input voltage, temperature readings, and thermal data from critical components like the buck converter. This real-time feedback allows you to monitor the benchmarking progress and understand how different settings affect your miner's performance.

The tool's intelligent thermal management becomes evident when temperatures approach the 66-degree Celsius safety threshold. Rather than pushing beyond safe operating limits, the benchmark automatically reduces settings to maintain thermal stability. This conservative approach ensures that the optimization process prioritizes long-term hardware reliability over short-term performance gains. Upon completion, the tool generates comprehensive results in JSON format, ranking the top five configurations for both maximum hashrate and optimal efficiency. These results provide clear guidance for selecting the configuration that best matches your operational priorities, whether focused on maximum output or energy efficiency.

The benchmarking tool also offers customization options for advanced users who want to modify the testing parameters. Command-line arguments allow you to specify custom starting voltages and frequencies, enabling more targeted optimization for specific use cases. For instance, if you already know your hardware performs well at higher frequencies, you can start the benchmark at elevated settings rather than beginning from the conservative defaults. This flexibility makes the tool valuable for both novice users seeking automated optimization and experienced miners who want to fine-tune specific performance characteristics.

## Overclock your Bitaxe
<chapterId>6b48c0c6-51c3-51a3-b317-850a374ae61e</chapterId>

:::video id=46c7a442-cd72-477c-8c91-b2c489ada1e6:::

Overclocking a Bitaxe device requires careful consideration of both hardware limitations and cooling requirements. While many users prefer to underclock their devices for quieter operation, understanding proper overclocking techniques is essential for those seeking maximum performance without damaging their hardware. The process involves increasing the frequency and potentially adjusting voltage settings beyond factory specifications, which inherently increases heat generation and stress on components.

The foundation of successful overclocking lies in adequate cooling infrastructure. Before attempting any frequency modifications, you must ensure your Bitaxe has proper heat dissipation capabilities. A Bitaxe Gamma with a quality heatsink and fan provides the necessary thermal management for safe overclocking. Devices with small heatsinks and inadequate fans should not be overclocked, as poor cooling performance will lead to thermal throttling and potential hardware damage. The relationship between heat and component longevity is critical to understand—excessive heat creates stress that degrades electronic components over time, significantly reducing the operational lifespan of your device.

### Strategic Heatsink Placement

The most critical component requiring additional cooling is the buck converter, a small black component located on the backside of the Bitaxe near the large coil. This device converts the incoming 5V power supply down to the appropriate voltage for the ASIC chip, typically around 1.2V. The buck converter, often referred to as the TPS, generates significant heat during operation and represents a thermal bottleneck that limits overclocking potential. Installing a small adhesive heatsink on this component not only enables higher overclocking headroom but also improves overall efficiency by reducing thermal losses.

Additional heatsink placement can benefit other high-current areas of the board. The voltage regulation circuitry experiences substantial electrical stress as power flows from the input section down through various board traces to supply the ASIC chip. Many experienced overclockers install heatsinks on the front of the Bitaxe in these high-current areas to further improve thermal dissipation. While not strictly necessary for moderate overclocking, these additional cooling measures become important when pushing frequencies to extreme levels.

### Cooling System Considerations and Limitations

The ESP32 controller, visible as the silvery component on the board, typically does not require additional cooling. This component generates minimal heat independently and only becomes warm due to thermal transfer from surrounding components. Installing heatsinks near the ESP32 can potentially interfere with the adjacent Wi-Fi antenna, degrading wireless connectivity and signal quality. Focus cooling efforts on the power regulation components and ASIC area rather than the control circuitry.

Dual fan configurations present both opportunities and limitations. While adding a second fan to blow air across the back of the Bitaxe can improve cooling performance, the device's firmware can only control one fan properly. The Bitaxe has two fan headers but only one fan controller, meaning that connecting two fans will confuse the firmware as it receives conflicting RPM signals. This configuration will function but may result in unpredictable fan control behavior.

### Baseline Performance Assessment

Before attempting any overclocking modifications, establish baseline performance metrics by running your Bitaxe at stock settings for several hours. Monitor the ASIC temperature, voltage regulator temperature, and fan speed percentage through the web interface. Optimal operating temperatures should maintain the ASIC below 60°C and the voltage regulator below 60°C under normal conditions. If your device already operates above 65°C on the ASIC or 70-80°C on the voltage regulator at stock settings, additional cooling hardware is mandatory before proceeding with overclocking.

The systematic approach to frequency increases involves incremental steps using the predefined frequency options in the settings menu. Begin by selecting the next available frequency step above your current setting while maintaining the default core voltage. This conservative approach allows you to evaluate thermal and stability impacts before making additional changes. Allow the device to operate at each new frequency setting for at least 30 minutes to one hour, monitoring temperature trends and hash rate stability throughout the evaluation period.

### Advanced Custom Configuration

Access to custom frequency and voltage settings requires enabling the advanced overclocking interface by appending "?OC" to the device's web interface URL. This unlocks manual input fields for precise frequency and voltage control, accompanied by appropriate warnings about the risks of operating outside designed parameters. The custom interface enables fine-tuning beyond the standard frequency steps, allowing experienced users to optimize performance for their specific cooling configurations.

When using custom settings, maintain conservative increment sizes of 10-15 MHz per adjustment step. This methodical approach prevents sudden thermal spikes and allows for proper stability testing at each frequency level. Some advanced users achieve frequencies around 700 MHz with core voltages adjusted to 1.175V or similar values, but these extreme settings require extensive cooling modifications and careful monitoring. The voltage regulator can operate at temperatures up to 100°C without immediate damage, but higher temperatures reduce efficiency and long-term reliability. Successful overclocking requires patience, systematic testing, and continuous monitoring to achieve stable performance improvements while preserving hardware integrity.

# Final Section
<partId>33367393-17a7-58d4-8359-79fffc6221fb</partId>

## Evaluate this course
<chapterId>785f8b92-c8a6-5a65-aa39-e9753a7edf51</chapterId>
<isCourseReview>true</isCourseReview>

## Conclusion
<chapterId>758baee6-2404-56fb-b534-6a39e441ae29</chapterId>
<isCourseConclusion>true</isCourseConclusion>

