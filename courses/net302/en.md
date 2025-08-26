---
name: IP networks from theory to practice
goal: Master the fundamentals of IP networks to better configure and troubleshoot them.
objectives: 

  - Understand the architecture and operation of the TCP/IP protocol
  - Explain the differences, advantages and constraints of IPv4 and IPv6
  - Identify and distinguish between different types of IP address
  - Configure and verify IP addressing on Unix/Linux systems
  - Use the main diagnostic tools to analyze and solve network problems

---

# Essential Skills for Navigating the IP World

Dive into the heart of the IP world and equip yourself with the knowledge to understand and efficiently manage your networks. In this course, you'll learn everything you need to know about computer networks in a clear and practical way.

You will learn how networks and IP addressing work, how to distinguish between IPv4 and IPv6, how to identify and use the different address categories, and how to grasp the full importance of the TCP/IP protocol and the links it forges between IP addresses, physical addresses and DNS names.

NET 302 is aimed mostly at students, Linux users or simply the curious who want to understand the basics of networking and strengthen their autonomy in managing, troubleshooting and optimizing infrastructures.

Join us and turn your knowledge into real operational expertise!

___

This NET 302 course is an adaptation of the course *Network Basics: TCP/IP, IPv4 and IPv6*, written in French by Philippe Pierre and published on [IT-Connect](https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/), under the Creative Commons Attribution-NonCommercial 4.0 International license ([CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)).


Substantial changes have been made to the original version by Loïc Morel: the text has been entirely rewritten, expanded and enriched to provide updated, in-depth content, while preserving the educational spirit of Philippe Pierre's original work. The diagrams have also been revised.

+++


# Introduction

<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>


## Course overview

<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>

This course provides a complete introduction to the fundamentals of IP networks. It is structured into four main sections, each covering an essential aspect for understanding, configuring and diagnosing issues in a computer network.

### TCP/IP protocol

In this first part, we'll lay the groundwork by exploring the concept of networking and the history of the TCP/IP protocol. We'll study its main components: IP, TCP, along with a brief look at the IPv5 QoS protocol. We'll also cover service primitives to better understand the logic of data exchange.

### IPv4 addressing

We will then move on to a module dedicated to IPv4 addressing. You'll learn how IPv4 is used in practice, its different address types (private, public, broadcast, etc.), the fundamental role of DNS, as well as how Ethernet addresses and the ARP protocol work. You will also discover NAT (Network Address Translation) and the basics of network configuration.

### IPv6 addressing

The third part focuses on IPv6 addressing, which is necessary to address the limitations of IPv4. We'll go through its standards and definitions, address assignment within a local network, address block management and the relationship between IPv6 and DNS.

### Network diagnostic tools

Finally, we'll conclude with a presentation of the main network diagnostics tools. These will enable you to analyze, control and troubleshout malfunctions. This part will be structured by layers: Network Access, Network, Transport and Upper layers.

By the end of this course, you'll have the fundamental knowledge to efficiently administer a network infrastructure and diagnose potential issues.

Ready to dive into the world of computer networks? Let's go!

**NOTE**: The descriptions are based on a GNU/Linux CentOS 7 system. However, network configurations are largely the same when comparing a Debian to a CentOS system. So, we won't make any distinction. When there is one, we'll prefix it with a specific logo.

**N.B.**: If you come across any unfamiliar terms during the course, please consult [the glossary](https://planb.network/resources/glossary) for definitions.


# TCP/IP protocols

<partId>53fd4b73-cdf1-4865-ba29-1ac8ec3e9e9a</partId>


## What is a network?

<chapterId>7370904f-f8f5-4ad4-a63a-5931d94c3b3b</chapterId>


In this first module, we'll take an in-depth look at the TCP/IP protocol, the cornerstone of modern digital communications. We will discuss its origins, its fundamental principles, and the addressing system it uses, which is essential for ensuring the flow of information between connected devices.

We'll also detail the main components that structure this model, and explain how they interact to form an operational, reliable and scalable network. But first, it's essential to go back to the concept of a network.

Etymologically, a network refers to a set of points linked to one another, forming an interconnected structure. In telecommunications and computing, this definition translates into a group of devices (computers, routers, switches, access points, etc.) capable of exchanging data via physical or wireless media. A network thus enables the continuous or intermittent flow of information, depending on requirements, on the protocols in use and on the nature of the deployed architecture.

Over time, several classic topologies have been developed to meet different needs for cost, performance, resilience, and ease of maintenance. These include:
- ring network,
- tree network,
- bus network,
- star network,
- mesh network.


### Ring network

In a ring topology, devices are connected in a closed loop: each station is linked to the next, and the last one connects back to the first. In this setup, every device acts as a relay, passing data along to the next link. Depending on the network type, information can circulate in one direction only, or in both.

The advantage of this arrangement lies in the simplicity of its cabling, and the absence of dependence on any central equipment. However, the continuity of the entire network depends on the health of each individual element: the failure of a single station can interrupt the entire communication system. This is why redundancy or bypass mechanisms are often put in place.


![Image](assets/fr/001.webp)


### Tree network

The tree network, or hierarchical topology, is modeled after the structure of a family tree. It consists of successive levels: a root node at the top connects to several lower-level nodes, which may themselves connect to other nodes, and so on.

This hierarchical layout works particularly well for large networks that need a clear division of responsibilities and segmented management. However, it also makes the network vulnerable to the failure of higher-level nodes: losing the root or a main branch can cut off entire sections of the infrastructure.


![Image](assets/fr/002.webp)


### Bus network

In a bus topology, all devices share the same transmission medium, typically a coaxial line or optical fiber. Each unit is passively connected, meaning it doesn't actively modify the signal, and it can send or receive data over this shared channel.

The bus topology's main advantage is low installation cost, thanks to simplified cabling.  However, in older coaxial-based implementations (Ethernet 10BASE2/10BASE5), disconnecting or losing a single station could disrupt or even halt all traffic, as the bus electrical continuity and termination impedance would no longer be maintained. Having a single physical medium is also a critical weakness: any break or fault stops communication for the entire network.


![Image](assets/fr/003.webp)


### Star network

The star topology, also known as "hub and spoke", is the most common today, especially in home and office Ethernet networks. Here, all devices connect to a single central device.

This layout makes management and maintenance easy: if one peripheral device fails, the rest of the network remains unaffected. The downside is that the central device is a single point of failure: if it goes down, communication stops everywhere. Cable quality and link lengths must also be carefully considered to maintain good performance.


![Image](assets/fr/004.webp)


**Note**: there are still networks organized in a linear, bus-like topology, where equipment is connected one after the other. This solution, although inexpensive to deploy, has the major drawback that a single break isolates some of the hosts, splitting the network into independent subsets.

### Mesh network

The mesh network is designed for maximum redundancy: every device is directly connected to every other device. This ensures service continuity even if multiple links or devices fail, as traffic can be re-routed along alternative paths.

The trade-off is that the number of connections to be established increases rapidly with the number of terminals. For `N` connection points, `N × (N-1) / 2` separate links are required, making this topology expensive and complex to deploy. It's therefore used mainly in critical networks requiring very high availability, such as certain parts of the Internet or sensitive industrial systems.


![Image](assets/fr/005.webp)


Other variations exist, such as grid or hypercube networks, which are designed for specialized needs in distributed computing or parallel processing.

On a global scale, the Internet is a massive interconnection of networks using diverse topologies, unified by common addressing (IPv4 and IPv6) and a collection of standardized protocols defined by the IETF (*Internet Engineering Task Force*). This diversity means the Internet follows no single topology: its structure is flexible, scalable and independent of the logical addressing scheme that makes it usable.


## The origins of TCP/IP

<chapterId>266b6864-8789-48d7-bc85-001cb9f1651f</chapterId>


The origins of the TCP protocol lie with **ARPA** (*Advanced Research Projects Agency*, renamed "DARPA" in 1972), which launched the **ARPANET** project in 1966. The first ARPANET segment went live in October 1969, interconnecting UCLA and Stanford universities. The aim was to link research centers through a packet-switched network that could keep communications running even in the event of partial infrastructure failure.

As part of this dynamic, ARPA financed the University of Berkeley to integrate the first TCP/IP protocols into its BSD Unix system. This played a major role in spreading and standardizing the protocol, first in the academic world, and later in industry.

**Note**: at that time, computer scientists didn't yet have Linux (which wouldn't appear until the early 1990s), nor Minix, the educational system designed by Andrew Tanenbaum.  The main options were Unix, or, sometimes, proprietary mainframes like OpenVMS. Thanks to its flexibility and openness, Unix was instrumental in spreading the first networking concepts.

Strictly speaking, TCP/IP is not a single protocol but a suite of protocols built around TCP and IP. It rose to prominence because it provided a standardized programming interface for exchanging data between machines on the same network. This interface, based on primitives called "sockets", made it possible to create reliable and flexible connections while integrating essential application protocols.

ARPANET is therefore the historical foundation of today's Internet. Indeed, the Internet is a global network based on the principle of packet switching, where information circulates using a set of standardized protocols that ensure compatibility and interoperability between heterogeneous systems. This open architecture has enabled the development and deployment of countless services and applications, including:
- emails,
- the World Wide Web (www),
- file transfer and sharing...

The governance and evolution of these protocols are overseen by the ***Internet Architecture Board*** (IAB). 
This organization coordinates technical directions through two main structures:
- **IRTF** (_Internet Research Task Force_), which conducts long-term research on protocol evolution and improvement.
- **IETF** (_Internet Engineering Task Force_), which develops, standardizes, and documents the operational protocols used on the Internet

The distribution of network resources (IP address ranges, autonomous system numbers, root domain names, etc.) is coordinated internationally by **IANA/ICANN**. Operational management relies on: **RIR** (*Regional Internet Registries*): **RIPE NCC** (Europe, Middle East, Central Asia), **ARIN**, **APNIC**, **LACNIC** and **AFRINIC**.

All TCP/IP protocol specifications are recorded in documents called **RFC** (_Request For Comments_), which serve as authoritative technical references. RFCs are continually updated and numbered to reflect the ongoing evolution of the protocol suite.

The TCP/IP stack is often represented as a stack of four functional layers,  often compared to the seven-layer **OSI** (_Open Systems Interconnection_) model developed by the **ISO** (_International Standards Organization_), which serves as a conceptual reference for networking.

The four layers of the TCP/IP model are:
- the NETWORK ACCESS layer, which provides the physical link and media access control protocols;
- the INTERNET layer, which handles routing and IP addressing;
- the TRANSPORT layer, which guarantees the reliability and management of data flows using protocols such as TCP or UDP ;
- the APPLICATION layer, which groups together user and software protocols such as HTTP, FTP, SMTP and DNS.


![Image](assets/fr/006.webp)


Today, the most widely used version of IP is IPv4, but its 32-bit address space has clear limitations. This led to the creation of IPv6, which uses 128-bit addressing and offers virtually unlimited capacity: essential for supporting the explosive growth of connected devices and meeting the challenges of the Internet of Things, mobility, and security.

Each layer of the TCP/IP stack provides specific services, making it possible to address different networking needs in a modular way: physical transmission, logical addressing, data integrity, and application-level services.

| Device example    | Description                                                                               | 	TCP/IP layer |
| ---------------------- | ----------------------------------------------------------------------------------------- | ----------------------- |
| Web server            | Application services closest to end users                                      | Application             |
| Gateway or proxy    | 	Encodes, encrypts, compresses useful data                                              | Application             |
| Session switch | Establishes sessions between applications                                               | Application             |
| Firewall or L4 router | Establishes, maintains, and terminates sessions between endpoint devices                  | Transport               |
| Router                | Globally addresses interfaces and determines optimal paths through a network | Network                  |
| Switch   | Locally addresses interfaces and forwards traffic via MAC                            | Network Access         |
| Network Interface Card (NIC)     | Signal encoding, cabling, connectors, physical specifications                        | Network Access         |

https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864

## IPv5 QoS protocol

<chapterId>570ded19-be61-4005-844e-9490570a6455</chapterId>


The header of an IP packet is an essential data structure, divided into several fields, each with a specific role to ensure the packets are transmitted and processed correctly as they travel through the network. These fields include the destination IP address (needed to route the packet to its intended recipient), the header length indicated by the IHL (*Internet Header Length*) field, the total packet length recorded in the *Total Length field*, control and verification information, and other parameters for managing communication flow and quality.

The very first field in the header is called Version. This 4-bit value specifies which version of the IP protocol the packet follows. It's important because it tells each router or intermediate device how to interpret and handle the encapsulated data.

**Note**: The management and assignment of IP protocol versions is under the responsibility of **IANA**. A 4-bit field allows for 16 binary combinations (values 0 to 15). As of today, their assignment is as follows:


| Version Number | Protocol   | Version Description         | Reference               |
| -------------- | ---------- | --------------------------- | ----------------------- |
| 0–1            | Reserved   | Reserved                    |                         |
| 2–3            | Unassigned | Unassigned                  |                         |
| 4              | IP         | Internet Protocol           | RFC 791                 |
| **5**          | **ST**     | **ST Datagram mode**        | **RFC 1190** / RFC 1819 |
| 6              | IPv6       | Internet Protocol version 6 | RFC 8200                |
| 7              | TP/IX      | The Next Internet           | RFC 1475                |
| 8              | PIP        | The P Internet Protocol     | RFC 1621                |
| 9              | TUBA       | Tuba                        | RFC 1347                |
| 10–14          | Unassigned | Unassigned                  |                         |
| 15             | Reserved   | Reserved                    |                         |

Among these is IPv5, which, although largely unknown to the public, did exist as the ST (_Stream Protocol_). Developed in the 1980s, IPv5 was designed to address a growing need at the time: providing "_Quality of Service_" (QoS) for certain data flows that required continuous, stable transmission, such as Voice over IP or multimedia streams. Its goal was to guarantee end-to-end bandwidth and priority, a concept similar to what the RSVP (_Resource Reservation Protocol_) offers today for dynamically reserving network resources on modern routers.

However, IPv5 remained experimental and was implemented on only a small number of network devices. Its limited adoption, combined with the rapidly growing need for more address space, led Internet designers to skip directly from IPv4 to IPv6. This avoided both IPv4's address limitations and any risk of confusion or incompatibility with IPv5's experimental specifications.

Although IPv5 never saw widespread use, it played an important role in shaping early thinking about QoS and traffic management. Today, it is more of a historical marker than a working standard.

**Reminder** - A protocol is a set of communication rules: data structures, algorithms, packet formats, and conventions that allow different devices to exchange information reliably and understandably. A service is the concrete implementation of a protocol through specific programs (clients, servers) that follow these rules and make the functionality available to users and applications.

We can now take a closer look at the structure and operation of the IP protocol, the essential foundation of all network communication.


## The IP protocol

<chapterId>758fddbd-b652-4c18-bd1e-d038bd2e4d05</chapterId>


### Definitions and general information

The IP protocol, or "***Internet Protocol***", is the backbone of the TCP/IP model. It carries data packets from one host to another within a network, whether it's local or spans the globe. It has two key roles: managing the logical addressing of devices, and ensuring packets are routed across often heterogeneous and interconnected networks.

At the physical level, transmission relies on hardware interfaces to establish point-to-point connections between nodes. However, it is the IP protocol that makes end-to-end communication possible, giving each packet the information it needs to navigate through multiple possible paths to its destination.

Three network configuration elements determine how a packet is sent on its way:
- **IP address**: uniquely identifies the destination host in the network.
- **Subnet mask**: specifies which part of the address identifies the network and which part identifies the host, enabling logical division into subnets.
- **The gateway**: indicates the intermediate router through which the packet should pass to reach an external network or another segment of the local network.

On the Internet, data doesn't flow as one continuous stream, but it's sent as **datagrams**: independent blocks of data, each encapsulated with all the information needed for delivery. This is the principle of **packet switching**, where information is split into self-contained units that may take different paths to reach the same recipient.

In addition to the payload (*payload*), each IP datagram contains a structured header with fields such as the destination address, source address, type of service, protocol version number and other control information needed to manage the transmission.

The theoretical maximum size of an IP datagram is **65,536 octets**, a limit set by the total length field in the header. In practice, this size is rarely reached, as the physical networks carrying the packets (Ethernet, Wi-Fi, fiber optics...) usually impose a stricter limits known as **MTU** (_Maximum Transmission Unit_). If a datagram exceeds the MTU of the physical link, it must be split into smaller packets, each sent separately and reassembled on arrival.

This adaptability makes IP a robust and flexible protocol, able to operate over a wide variety of underlying technologies while maintaining universal compatibility between heterogeneous systems and networks.


### Fragmentation of IP datagrams

When an IP datagram needs to pass through a network whose transmission capacity is smaller than the datagram itself, it must be **fragmented** so it can travel without issue. This physical size limit is called the **MTU** (Maximum Transmission Unit): the largest frame size that can pass over a given network without being split.

Each network technology imposes its own MTU, determined by its hardware and protocol characteristics. Common values include:
- **ARPANET**: 1000 bytes
- **Ethernet**: 1500 bytes
- **FDDI**: 4470 bytes

When a datagram exceeds the MTU of a network segment it needs to cross, routing equipment will split it into smaller **fragments** that comply with the limit. This typically happens when moving from a high-MTU network to one with a lower capacity. For example, a datagram coming from an FDDI network may need to be fragmented before being sent over an Ethernet segment.


![Image](assets/fr/008.webp)


The fragmentation process works like this:
- The router breaks the datagram into fragments that are no larger than the target network's MTU.
- Each fragment's size is a multiple of 8 bytes, since the IP protocol uses this unit to encode the reassembly offset.
- Every fragment gets its own IP header, which contains the information needed by the final recipient to reassemble them in the correct order.

Once fragmented, the pieces travel independently through the network. They may take different routes, depending on routing tables, link loads, or outages. There's no guarantee they'll arrive in the order they were sent.

On arrival, the receiving machine handles **reassembly**. Using the information in the headers (shared identifier, offset, and fragmentation flags), it puts the fragments back in the right order to reconstruct the original datagram before transmitting it to the next layer. If even one fragment is lost or corrupted, the whole datagram is usually discarded, without every piece, the result would be incomplete or unusable.

Although effective, fragmentation and reassembly come with downsides: extra processing for routers and hosts, and a higher chance of packet loss, which can increase retransmissions. That's why careful MTU management and packet size optimization are important for smooth, efficient IP communication.


### Data encapsulation

To ensure that data is routed correctly through the layers of the TCP/IP model, the process of **encapsulation** plays a key role. At each stage as a message travels from the sender's application to the recipient's machine, extra information, known as headers, is added. These headers give intermediate devices and software layers the instructions they need to process, deliver, and, if necessary, reassemble the data.

When a message is sent, it passes through the four layers of the TCP/IP stack. At each layer, a new header is added in front of the existing data: each header contains specific metadata, such as logical or physical addresses, communication ports, sequence numbers, error-control flags, and any information needed to manage transmission and routing.

Transmission thus follows a structured process: 
- The Application layer creates the initial **message**, containing the raw data.
- The Transport layer encapsulates it into a **segment**, adding source and destination ports, sequence numbers, and flow-control mechanisms.
- The Internet layer adds to the segment an IP header to form a **datagram**, specifying source and destination IP addresses.
- The Network Access layer wraps the datagram into a **frame**, adding MAC addresses and integrity check codes (CRC).


![Image](assets/fr/009.webp)


This encapsulation process ensures both the integrity and traceability of the data, and also its adaptability: when moving from one network to another, the headers provide devices with the information needed to choose the route, check validity, or perform fragmentation if necessary.

Upon arrival, the process is reversed: the receiving machine gets the frame at the Network Access layer, which reads and removes the corresponding header. The datagram is then passed to the Internet layer, which reads the IP header and removes it in turn to deliver the segment to the Transport layer. The Transport layer processes the transport headers, checks the integrity of the stream, and finally delivers the **message** to the target application in its original state.


![Image](assets/fr/010.webp)


The transformation of the data at each layer can be summarized as:
- **Message**: block of information at the Application layer.
- **Segment**: data unit after encapsulation by the Transport layer.
- **Datagram**: form taken following the addition of the IP header by the Internet layer.
- **Frame**: final block ready for transmission over the physical medium by the Network Access layer.


![Image](assets/fr/011.webp)


This process, essential to the reliability and universality of Internet communications, ensures that every piece of data, no matter how fragmented or complex, can be transported end-to-end while remaining comprehensible and usable by the receiving machine.


### IP addressing

Even with packet switching, fragmentation, and encapsulation in place, a network still couldn't function without a reliable addressing system. To ensure that each data packet reaches the correct recipient, the Internet layer uses a unique identifier: the **IP address**. 
In IPv4, an IP address is coded on **32 bits** and written as four decimal numbers separated by dots, in the familiar N1.N2.N3.N4 format (for example: 192.168.1.12).

An IP address has two parts:
- **_netid_**: identifies the network that the host belongs to
- **_hostid_**: identifies the specific host within that network
This separation allows the global Internet to be logically structured into many interconnected networks.

Historically, the IPv4 system relied on a class-based scheme, labeled from A to E, which defined the range of address and their intended use. Each class allocated a set number of bits to the _netid_ and _hostid_, directly affecting the possible number of networks and hosts.


| **Class** | **IPv4 Address Range**            | **Usage**                    |
| --------- | --------------------------------- | ---------------------------- |
| A         | 1.x.x.x to 126.x.x.x              | Unicast addresses            |
|           | (127.x.x.x reserved for loopback) | Local loopback               |
| B         | 128.0.x.x to 191.255.x.x          | Unicast addresses            |
| C         | 192.0.0.x to 223.255.255.x        | Unicast addresses            |
| D         | 224.0.0.0 to 239.255.255.255      | IP Multicast                 |
| E         | 240.0.0.0 to 255.255.255.255      | Reserved for experimentation |

Not all possible values can be assigned to hosts. For example, in a **class C** address, the last byte offers 8 bits (256 values). But two of these are reserved:
- 0: identifies the network itself
- 255: is the **broadcast** address, used to send a packet to all hosts in the network at once.
That leaves 254 usable addresses for devices.

The number of available addresses varies widely between classes: from large public networks in class A, to corporate networks in class B, to smaller local networks in class C.


![Image](assets/fr/013.webp)


Some address ranges are reserved for private use and never routed directly on the Internet. These are known as **private addresses**, and are used inside organizations, businesses, or homes, and require address translation, typically NAT (*Network Address Translation*), to reach the public Internet. These are:
- **Class A**: from 10.0.0.0 to 10.255.255.255
- **Class B**: from 172.16.0.0 to 172.31.255.255
- **Class C**: from 192.168.0.0 to 192.168.255.255

When a device with a private address accesses the Internet, a NAT-enabled router or gateway replaces it with a valid public address.

Example: If a host has the address **192.168.7.5**, we can deduce:
- 192.168.7.0: network address
- 192.168.7.1: often the local router
- 192.168.7.5: the host itself

Another special case is **127.0.0.1**, known as the "***loopback***". 
On Linux systems, it is associated with the Interface **lo**. This address allows a machine to address itself for local testing or diagnostics, without going through a physical Interface. The entire **127.0.0.0/8** range is reserved for this purpose.

To optimize address use and design complex networks, the **subnetmask** (_netmask_) is essential. This binary mask separates the _netid_ from the _hostid_ in an IP address. 
Each class has a default mask: 
- **255.0.0.0** for class A, 
- **255.255.0.0** for class B,
- **255.255.255.0** for class C.

Good network design follows a basic rule: devices that must communicate directly should be in the same network or subnet. To segment a network, we use subnetting, dividing a network into smaller subnets by using a more specific mask.

Subnetting example:
A **class C** network: 192.168.1.0/24 with a default mask of 255.255.255.0. 
We want 4 subnets of up to 60 hosts each.

**Step 1**: Number of addresses needed per subnet = 60 + 2 reserved addresses (network + broadcast) = 62.

**Step 2**: Find the nearest power of 2 ≥ 62. ->  2⁶ = 64.

**Step 3: Adjust the mask. Keep the _netid_ bits and reserve the needed _hostid_ bits. We obtain a binary mask which, once converted, gives **255.255.255.192**.

```
11111111 11111111 11111111 11000000
```

**Step 4**: Calculate the address ranges for each subnet, varying the bits reserved for the host.


| Subnet ID (bits) | Subnet Address   | Subnet Mask     | Address Range                 | Broadcast Address |
| ---------------- | ---------------- | --------------- | ----------------------------- | ----------------- |
| 00               | 192.168.1.0/26   | 255.255.255.192 | 192.168.1.1 – 192.168.1.62    | 192.168.1.63      |
| 01               | 192.168.1.64/26  | 255.255.255.192 | 192.168.1.65 – 192.168.1.126  | 192.168.1.127     |
| 10               | 192.168.1.128/26 | 255.255.255.192 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191     |
| 11               | 192.168.1.192/26 | 255.255.255.192 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255     |


**Step 5**: This creates four subnetworks, each supporting up to 62 machines, while keeping the overall addressing scheme efficient. The _hostid_ portion is split into a _subnetid_ part and a host part.


![Image](assets/fr/016.webp)


This fundamental principle of subnetting remains indispensable in modern network engineering, allowing precise IP allocation, better traffic control, strong segment isolation, and scalable network management.


### CIDR addressing

In the early 1990s, as the Internet spread rapidly through businesses and organizations, the traditional IP addressing system based on classes (A, B, C) began to show its limits.
Its rigid structure led to significant waste of IP addresses and made routing tables increasingly large, complex, and difficult to maintain. 
To address these issues, a more flexible and efficient method was introduced: **CIDR** (_Classless Inter-Domain Routing_). CIDR has gradually become the standard, largely replacing the old class-based system.

The core idea behind CIDR is the ability to group several adjacent networks, especially Class C blocks, into a single logical unit called a **supernet** (_supernet_). With this aggregation, a single entry in the routing table can represent multiple subnetworks, reducing the number of routes routers need to handle and improving their performance.

While Class C networks initially had the greatest need for aggregation due to their smaller capacity, the principle has also been applied to Class B and, in theory, even Class A networks, though the latter are less affected thanks to their large address range.

With CIDR, the concept of fixed classes disappears. The address space is treated as a continuous range that can be divided or aggregated as needed. CIDR blocks are defined using subnet masks that are not limited to the defaults of A, B, or C classes. A CIDR block can represent either a single network or a contiguous set of subnetworks sharing the same prefix.

A CIDR block is written in the format "address/prefix", where the number after the slash indicates how many bits make up the network portion. For example, /17 means that the first 17 bits identify the network, while the remaining 15 bits identify hosts.

Example:
A /17 block contains 2^(32-17) addresses so 2^15 = 32,768 total addresses. Subtracting the two reserved addresses (network and broadcast) leaves 32,766 usable host addresses. This allows network administrators to size their subnets precisely to match real-world needs, avoiding unnecessary waste.

To make CIDR sizing easier to understand, here is a table of common prefixes and their equivalent subnet masks and usable addresses:

| CIDR Prefix | Available Host Bits | Subnet Mask     | Usable Host Addresses         |
| ----------- | ------------------- | --------------- | ----------------------------- |
| /8          | 24                  | 255.0.0.0       | 2^24 - 2 = 16,777,214         |
| /12         | 20                  | 255.240.0.0     | 2^20 - 2 = 1,048,574          |
| /16         | 16                  | 255.255.0.0     | 2^16 - 2 = 65,534             |
| /20         | 12                  | 255.255.240.0   | 2^12 - 2 = 4,094              |
| /24         | 8                   | 255.255.255.0   | 2^8 - 2 = 254                 |
| /26         | 6                   | 255.255.255.192 | 2^6 - 2 = 62                  |
| /27         | 5                   | 255.255.255.224 | 2^5 - 2 = 30                  |
| /28         | 4                   | 255.255.255.240 | 2^4 - 2 = 14                  |
| /29         | 3                   | 255.255.255.248 | 2^3 - 2 = 6                   |
| /30         | 2                   | 255.255.255.252 | 2^2 - 2 = 2                   |
| /31         | 1                   | 255.255.255.254 | 2^1 = 2 (point-to-point only) |
| /32         | 0                   | 255.255.255.255 | 1 (host address only)         |


**NOTE**: Historically, RFC 950 discouraged the use of subnet zero, mainly to avoid confusion in routing.  This restriction became obsolete with RFC 1878, which fully allows its use. The old limitation was mostly due to imcompatibility with older hardware that could not handle CIDR correctly. Modern equipment has no such problem.

For example, the subnet **1.0.0.0** with the subnet mask **255.255.0.0** once ambiguous with the class A network identifier, is now perfectly valid and usable.

**TIP**: for error-free subnet calculations and rapid conversion of addresses to CIDR notation, there are handy tools like ***ipcalc***. This "network calculator" clearly shows address breakdowns, available ranges, and associated masks, ideal for both administrators and students learning CIDR.

```shell
sudo apt install ipcalc
```

https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d

## The TCP protocol

<chapterId>860bf7d5-a502-4d10-a12c-9827f6c2d393</chapterId>


The **TCP protocol** (_Transmission Control Protocol_) plays a central role in the TRANSPORT layer of the TCP/IP model. It acts as a bridge between applications and the Internet layer, ensuring the reliable transfer of data between two distant machines.
While the IP protocol simply sends packets without guaranteeing delivery or order, TCP ensures the integrity and consistency of the data flow, delivering it loss-free, in the correct order, and without duplicates.

TCP's main responsibilities include:
- Reordering received segments;
- Monitoring the flow of data to avoid congestion;
- Splitting or reassembling data blocks into suitable units (segments);
- Managing the establishment and termination of connections between both ends of the communication.

TCP is a connection-oriented protocol, meaning it sets up an explicit, ongoing relationship between client and server. To do this, it uses **sequence numbers** and **acknowledgements**: for every segment sent, a unique identifier is assigned so the receiving machine can check both the order and integrity of the data. The receiver then returns an acknowledgement segment with the **ACK flag** set to 1, confirming receipt and indicating the next expected sequence number.


![Image](assets/fr/018.webp)


To improve reliability, TCP uses a timer: once a segment is sent, a countdown starts. If an acknowledgement does not arrive within the timeout period, the sender automatically retransmits the segment, assuming it was lost in transit. This automatic retransmission mechanism offsets the losses inherent to IP networks, which can occur in cases of congestion, routing errors, or hardware failures.


![Image](assets/fr/019.webp)


TCP is able to detect and handle duplicates. If a retransmitted segment arrives but the original also shows up, the receiver uses the sequence numbers to identify the duplicate and keep only the correct copy, eliminating any ambiguity.

For this process to work, both machines must share a common understanding of their initial sequence numbers. This is ensured by following a strict connection procedure: on the one hand, the **server** listens on a specific port, waiting for an incoming request (passive mode); on the other, the **client** actively initiates the connection by sending a request to the server on the same service port.

**NOTE**: A "port" is a numerical identifier (from 0 to 65,535) assigned to a network application on a computer. It is used to differentiate multiple services running simultaneously on the same IP address. When a client sends data, it specifies the port number so the server's operating system knows which program  should receive it (e.g. 80 for HTTP, 443 for HTTPS, 25 for SMTP). Ports act like dedicated doors, directing traffic in and out, preventing confusion between services, and allowing fine-grained access control through firewalls or filtering rules.

The sequence synchronization exchange is based on the famous **"*three-way handshake*"** mechanism, similar to the way two people greet each other to establish contact. This initialization phase, which ensures TCP's reliability, takes place in 3 stages:
1. **SYN:** The client sends an initial synchronization segment (**SYN**) with the appropriate flag set and an initial sequence number (e.g., C);
2. **SYN-ACK:** The receiving server responds with an acknowledgement segment (**SYN-ACK**), it acknowledges the client's sequence number and provides its own initial sequence number;
3. **ACK:** The client sends a final acknowledgement (**ACK**) confirming receipt of the server's sequence number, finalizing synchronization. The SYN flag is now disabled and the ACK flag remains set indicating that the connection is established.


![Image](assets/fr/020.webp)


This exchange protocol ensures that both parties share the same numbering base before transmitting payload data. Once this synchronization is complete, the session is opened: segments can now travel in both directions, each acknowledged upon receipt, ensuring maximum reliability of the data flow.

This ***three-way handshake*** only concerns connection establishment. For closing, TCP uses a *four-way handshake*: FIN → ACK → FIN → ACK, which guarantees that no segment in transit is lost before the connection is completely released.

Although designed for robustness and reliability, this process has also given rise to exploitable vulnerabilities. For example, attacks such as **IP Spoofing** aim to bypass or corrupt this trust relationship by posing as an authorized machine through falsified sequence numbers, creating a breach that allows interception or manipulation of the data stream.

To limit the risks of sequence synchronization hijacking and to manage network load, the TCP protocol uses a flow management technique known as "**_Sliding Window_**". This system regulates how much data can be sent without requiring an immediate acknowledgement for each segment, thus reducing unnecessary overload on the network while maintaining good reliability.

In practical terms, the sliding window defines a range of sequence numbers that can circulate freely between sender and receiver without each individual segment beeing acknowledged. As acknowledgements are received by the sending system, the window "slides": it slides to the right making room for new segments to be sent. The size of this window (critical for optimizing throughput while avoiding congestion) is specified in the "*Window*" field of the TCP header.

**Example**: if the initial sequence number is 3 and the window extends to sequence 5,segments numbered 3 to 5 can be sent without waiting for individual acknowledgements.


![Image](assets/fr/021.webp)


The size of the sliding window is not fixed; it adjusts dynamically to network conditions and the receiver's processing capacity.  If the receiver can handle a greater volume of data, it indicates this through the Window field, prompting the sender to expand its window. Conversely, in case of overload or risk of saturation, the receiver can request a reduction, the sender will wait until the window moves forward to send additional segments.

The protocol provides a symmetrical procedure for closing a TCP connection to ensure a clean, orderly shutdown. Either machine can initiate closure by sending a segment with the **FIN** flag set to 1, signalling its intent to end the communication. It then waits until all in-transit segments have been received and ignores any further data.

Upon receiving this segment, the other machine sends an acknowledgement, also marked with the FIN flag. It then finishes sending any remaining data before informing the local application that the coonection has been closed. This double confirmation ensures an orderly shutdown and minimizes the risk of data loss.

This precise management,combining IP's flexible routing with TCP's strict control, is often illustrated by a diagram contrasting the speed of the IP protocol (which works on a **"best effort "** basis, with no guarantee of delivery) against the reliability of the TCP protocol (which manages transmission through acknowledgements and negotiated sequences).


![Image](assets/fr/022.webp)


In some cases, however, absolute reliability is not the priority: speed and simplicity are. This is true for applications like live streaming or VoIP, which can tolerate some packet loss without seriously affecting user experience. In such cases, **UDP** (_User Datagram Protocol_) is preferred.

UDP operates on a fundamentally different principle from TCP: it is **connectionless**, meaning no prior relationship is established between sender and receiver. When a machine sends packets via UDP, they are transmitted one way; the receiver does not send acknowledgements, and the sender has no confirmation that the message arrived. The UDP header is intentionally minimal, containing only the source port, destination port, segment length, and a checksum, with no built-in acknowledgment or state-control mechanism. As always, IP addresses are carried by the underlying IP header.

A common analogy is that TCP is like a **phone call**, where a circuit is established, followed and controlled throughout the conversation. While, the UDP protocol is like **posting a mail**, where the sender slips a letter into a mailbox with no immediate proof of delivery or systematic feedback.

This complementarity between TCP and UDP enables modern networks to adapt to a variety of needs, choosing maximum reliability or prioritizing speed, depending on the application.


## Service primitives

<chapterId>4480afb7-e950-4ccb-88fa-d132f9dc3479</chapterId>


### Layered architecture and exchange organization

As we've seen, **services** are the concrete implementation of the protocols we've described  so far. While the TCP/IP model differs from the **OSI** model, it adopts the same layered approach: each layer is designed to perform a specific function and to provide **services** to the layer directly above it, resulting in a modular, robust, and easily maintainable architecture.

Each layer builds on the capabilities of the one below it, and in turn provides the layer above with a consistent Interface for managing data. In this architecture, every layer has its own **data structures**, carefully defined to ensure perfect compatibility with the other layers. This compatibility is essential for smooth, reliable, and clear communication from one endpoint to another.

Two key aspects govern these exchanges:
- **Vertical aspect**: the relationship between one layer and the one above or below it (from layer N to layer N+1, and vice versa).


![Image](assets/fr/023.webp)


- **Horizontal aspect**: the interaction between remote applications, i.e., the dialogue between a **client** and a **server**, in either direction.


![Image](assets/fr/024.webp)


The layered architecture follows the principle that each layer processes only the information within its scope: data structures, headers and control mechanisms vary from one layer to another, but together they form a coherent system, ensuring data is gradually routed to its final destination.

**Reminder**: Specific terminology is used to describe the data units exchanged between layers: 
- **message** for the Application layer, 
- **segment** for the Transport layer (TCP), 
- **datagram** for the Internet layer (IP), 
- **frame** for the Network Access layer. 

The table below summarizes the terms for TCP and UDP contexts:

| TCP/IP Layer         | Unit Name (TCP) | Unit Name (UDP) |
|----------------------|------------------|------------------|
| Application Layer    | Stream           | Message          |
| Transport Layer      | Segment          | Packet           |
| Internet Layer       | Datagram         | Datagram         |
| Network Access Layer | Frame            | Frame            |

### Service primitives and data units

At the core of this system are **service primitives**, which act as communication interfaces. These primitives function like service desks, listening on reserved specific **ports** and allowing processes to establish, maintain, and terminate network connections in a controlled way. While protocols organize the format and transmission of data across the network, it is the **services and their primitives** that provide the vertical link between the layers.

By combining the horizontal aspect (communication between distributed applications) with the vertical aspect (internal interactions between layers), the TCP/IP model delivers a complete, scalable architecture. Overlapping these two perspectives gives a clear overview of how data is exchanged in structured network communication.


![Image](assets/fr/026.webp)


### Part summary

In this first major section, we explored the core architecture that governs the configuration and operation of today's Internet-connected networks. This architecture is based on a **four-layer model**, inspired by the OSI model, and built around the **TCP/IP** protocol suite, the backbone of modern communications. We saw that TCP, with its connection-oriented approach, ensures reliable transfers, while UDP, lighter and faster, is preferred when speed is more important than reliability.

The proper functioning of this model relies on the implementation of protocols through **service primitives**. These ensure the link between layers, enabling data processing to be adapted to the specific requirements of each level, from transport to application, including Internet and network access. This modular approach makes the system both flexible and robust.

IP addressing is another cornerstone of this infrastructure. Every connected device is identified by a **unique IP address**, taken from an address space organized into **classes** (from A to E). Some of these addresses are reserved for special purposes, such as local loopback or multicast, while others, known as "private addresses", are not routed over the Internet without translation (NAT). This classification enables a logical, hierarchical organization of networks.

We also examined the concept of **subnetworks**, which makes it possible to divide a network segments to better manage IP resources and optimize data flow. While manual subdivision using subnet masks remains an important principle, it has largely been modernized thanks to **CIDR** (_Classless Inter-Domain Routing_). This method has transformed address management by enabling more flexible and rational allocation of IP ranges, while reducing the size of routing tables.

By mastering these concepts - layers, protocols, service primitives, addressing and subnetting - you gain a solid foundation for understanding the technical workings of modern networks, and for efficiently configuring a network infrastructure to meet today's needs. 

In the next section, we'll take a closer look at IPv4 addressing.


# IPv4 addressing

<partId>83f3c3e5-378c-440f-a095-df210842efde</partId>


## Using IPv4

<chapterId>79e4dd18-446a-435b-9f25-c88a00f8bec6</chapterId>


In this section, we will go deeper and look at how **IPv4** addresses are actually implemented in a real-world network. We'll break down their format, the logic behind them, and how they connect with other key network elements like **DNS names**, **MAC addresses**, **subnetworks** and **translation techniques**.

An IP address is a unique numerical identifier assigned to each **network Interface** on a device. It makes it possible to locate this device within a network and reach it to transmit data. For example, a router, server, workstation, network printer or even a surveillance camera has at least one IP address of its own. The IP address makes **routing** possible, i.e. moving packets from point A to point B, even if they are physically far apart.

IP addresses can be assigned in two main ways:
- **Static**: Manually set on the device.
- **Dynamic**: Automatically assigned on-demand by a DHCP (_Dynamic Host Configuration Protocol_) server. DHCP simplifies network management, eliminating the need for manual configuration while enabling precise control through reservations and lease durations.

**IPv4** addresses are written in a **32-bit** format split into **four bytes**. Each byte contains 8 bits and represent a decimal number from 0 to 255. The 4 bytes are separated by dots to form a clear, legible notation.

example: address 172.16.254.1_


![Image](assets/fr/027.webp)


Each bit in a byte has a value (or "weight"): the left-hand bit (the most significant bit) is worth 128, the next 64, then 32, 16, 8, 4, 2 and 1 for the right-hand bit (the least significant bit). In this way, binary writing is converted to decimal by the simple addition of the set weights.

The table below illustrates this correspondence:


| Binary Code | Activated Bit Values          | Decimal Value |
|-------------|-------------------------------|---------------|
| 00000000    | 0                             | 0             |
| 00000001    | 1                             | 1             |
| 00000011    | 1 + 2                         | 3             |
| 00000111    | 1 + 2 + 4                     | 7             |
| 00001111    | 1 + 2 + 4 + 8                 | 15            |
| 00011111    | 1 + 2 + 4 + 8 + 16            | 31            |
| 00111111    | 1 + 2 + 4 + 8 + 16 + 32       | 63            |
| 01111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64  | 127           |
| 11111111    | 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 | 255      |

To convert binary to decimal, add the weights of the bits that are set to 1.

| Binary     | Decimal Value |
| ---------- | ------------- |
| `10101100` | 172           |
| `00010000` | 16            |
| `11111110` | 254           |
| `00000001` | 1             |

An IP address identifies a single **network interface**, not the whole device. A multi-port router or firewall has multiple interfaces, each with its own IP address. One interface can even have several IP addresses (for example, to serve multiple virtual networks or services).

Every IP packet contains two IP addresses in its header:
- The source address (**sender**)
- The destination address (**receiver**)
Routers read these addresses to figure out the best path to send the packet until it reaches the destination. Without strict addressing rules, network traffic couldn't be routed correctly and global interconnection of networks would be impossible.

An IPv4 address has two parts: 
- **NetID**: identifies the network
- **HostID**:  identifies a device within that network
The **subnet mask** determines where the NetID ends and the HostID begins, specifying how many bits belong to each portion. The longer the NetID, the greater the number of possible subnets, but the number of hosts per subnet decreases accordingly.

Originally, IPv4 networks were divided into five **classes**: (A, B, C, D and E). Each class corresponds to a specific NetID range and defines a fixed granularity:
- Class A: very large networks with a large number of hosts
- Class B: medium-sized networks
- Class C: small networks
- Class D: addresses reserved for multicasting (_multicast_)
- Class E: experimental addresses, not used for conventional addressing


| Class | Leading Bits | First Byte Range | Default Subnet Mask | Purpose                          |
| ----- | ------------ | ---------------- | ------------------- | -------------------------------- |
| A     | 0            | 0 – 127          | 255.0.0.0           | Very large networks              |
| B     | 10           | 128 – 191        | 255.255.0.0         | Medium-sized networks            |
| C     | 110          | 192 – 223        | 255.255.255.0       | Small networks                   |
| D     | 1110         | 224 – 239        | N/A                 | Multicast addresses              |
| E     | 1111         | 240 – 255        | N/A                 | Experimental (not publicly used) |

Special Addresses:
- **Network address**: Identifies the network itself (used in routing tables).
- **Broadcast address**: Sends data to all devices in the subnet at once (all HostID bits set to 1).

The following ranges are reserved for internal use:
- **10.0.0.0/8** (Private Class A)
- **127.0.0.0/8** (local loopback or _loopback_)
- **172.16.0.0 to 172.31.255.255** (private Class B)
- **192.168.0.0 to 192.168.255.255** (private Class C)

The addresses **127.0.0.1** and, more generally, the entire 127.0.0.0/8 range is used for internal testing: any request sent to it never leaves the machine. This is useful for checking that a local network service is working without involving the wider network.

To make better use of the address space, administrators often split networks into **subnets** using subnet masks or **CIDR** notation (_Classless Inter-Domain Routing_). CIDR allows more precise management and helps avoid wasting addresses. Today, CIDR is essential for fine-tuning IP ranges and reducing the size of routing tables.

In modern networks, IP addressing is usually paired with other identifiers:

- **domain name** registered in a **DNS** (_Domain Name System_): It associates a numeric IP address with a human-friendly name.
- **MAC address**: a physical identifier engraved in the network card, used for local transport (_Ethernet_). When an IP packet needs to be physically transmitted, the ARP table matches the IP address with the MAC address of the destination.

To deal with IPv4 address shortages and to add a layer of security, networks often use address translation (_NAT_). NAT allows many private devices to share a single public IP address when accessing the Internet. 

**Note**: Online and built-in OS tools, such as the [Grenoble CRIC calculator](http://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/), make subnet and mask calculations much easier.
These utilities help to plan network splitting efficiently.

In conclusion, the broadcast address remains a practical function for sending the same message to all devices connected to a segment: this is achieved by setting all bits in the HostID portion to 1 so all hosts are targeted.


## The different types of IPv4 address

<chapterId>2adfad24-a90d-45b5-b808-3d2f6598bebf</chapterId>


IPv4 addresses fall into two main categories: public addresses, directly accessible on the Internet, and private addresses, intended for internal use within a local network.

A public IPv4 address is globally unique and routable across the Internet. It is assigned by official authorities and required for public-facing services such as websites, email servers, or cloud infrastructure.
The worldwide uniqueness of these addresses is essential to avoid any routing conflicts or collisions.

The **IANA** (_Internet Assigned Numbers Authority_), operating under the **ICANN** (_Internet Corporation for Assigned Names and Numbers_), manages the distribution of these IP ranges. In concrete terms, IANA divides the IPv4 space into 256 blocks of size /8, according to CIDR notation. Each block represents just over 16.7 million addresses (2³² / 2⁸).

These unicast address blocks are entrusted by IANA to the **Regional Internet Registries** (RIRs). These RIRs are responsible for redistributing the addresses at regional level, according to the real needs of access providers, companies or administrations. The unicast address space extends from blocks **1/8 to 223/8**, with portions either reserved for special uses (research, documentation, testing), or allocated directly to a network or RIR for redistribution.

To check who owns a public IP address, you can consult the RIR databases using the **whois** command, or by using the web interfaces provided by each registry. These tools can be used to trace the address back to the organization or provider that declared it.

Conversely, there are private IPv4 addresses, a practical response to the shortage of public addresses. These addresses, which are not routable on the Internet, are reserved for local environments: corporate networks, home LANs, datacenters or computing clusters. They are not unique worldwide: many private networks can reuse the same IP ranges without interference, as long as they remain isolated or use a network address translation device to access the internet.

To allow a device with a private IP address to access the Internet, networks use NAT (Network Address Translation). NAT works by dynamically replacing the private address with a public one, enabling dozens (or even hundreds) of devices to share a single public IP address. This method optimizes the use of IPv4 space and also adds a layer of security by hiding the internal network structure.

Another special category is **unspecified** addresses. The IPv4 notation **0.0.0.0** or its IPv6 version **::/128** means "no specific address". Such an address is invalid as a network address destination, but it can be used locally by a host to indicate "all interfaces" or "no address assigned yet". This is common in DHCP dynamic assignment or for listening on all server interfaces.

IPv6 also supports private addressing, but the standard generally recommends public addressing to avoid stacking multiple NAT layers. The **site-local addresses** (_site-local_) of the **fec0::/10** block were deprecated by **RFC 3879** for consistency and security reasons. They were replaced with **Unique Local Addresses** (_ULA_) located in the **fc00::/7** block. ULAs allow the creation of private IPv6 networks with clean internal routing, using a randomly generated 40-bit identifier to ensure local uniqueness.

IPv4 exhaustion was officially confirmed in 2011. To extend its lifespan, the Internet community adopted several strategies:
- Gradual migration to **IPv6**
- Widespread use of **NAT**
- Stricter allocation policies from RIRs, requiring precise justification and management of address needs 
- Recovery of unused or voluntarily returned address blocks by companies

These measures show that IP addressing is not just a technical challenge, but also a matter of global governance, central to the Internet's ongoing expansion.


## DNS, an address directory

<chapterId>511244ec-ba43-44ac-b4c3-b41579a15cff</chapterId>


Let's be honest, humans aren't great at memorizing long strings of numbers, whether in binary or decimal form. This challenge becomes even greater with IP addresses, which can be complex and a single IP address can sometimes mask multiple addresses, especially when techniques like NAT or virtual hosting are involved.

To make things easier, the Application layer uses a system that links an IP address to a logical, human-readable name. This is the role of **DNS** (*Domain Name System*), a massive, hierarchical, distributed directory that matches readable domain names to IP addresses. The system is based on a set of protocols and services. The most widely used DNS server software is **BIND** (_Berkeley Internet Name Domain_), an open-source software package that references much of the Internet’s DNS infrastructure.

The core idea behind DNS is simple: for any connected service, whether a website, mail server, or another network service, there is a record mapping a domain name to one or more IP addresses. This works in two directions:
- Forward resolution: translating a name into an IP address.
- Reverse resolution: finding the domain name associated with a given IP address.
This makes network addressing usable for humans while preserving the precision routers need to move data correctly.

A domain name is always structured hierarchically, with each level separated by a dot: the full name is called **FQDN** (_Fully Qualified Domain Name_). The rightmost part is the **TLD** (_Top Level Domain_) such as `.com`, `.org` or `.fr`. The left-most part designates the host, i.e. the specific machine or service linked to the IP address.

The DNS system is designed as a **tree of zones**. A **zone** is a section of the domain namespace managed by a specific DNS server. A single zone can contain multiple **subdomains**, which may themselves be delegated to other zones managed by different servers. Administrators are responsible for maintaining their zones: handling updates, delegations, and overall management.

This structure allows not just pointing to a main domain (e.g. `example.com`), but also fine-tuning records for individual hosts (`www`, `mail`, `ftp`, etc.). In the early days of networking, this mapping was handled with static files like (`/etc/hosts` on Unix systems), but such a method quickly became impractical for a fast-growing, interconnected Internet.

It's important to understand that a **DNS server** may only serve a limited scope. For example, a company's internal DNS server might not be directly accessible from the Internet. If this DNS is not configured to forward queries, or does not have a trusted relationship with other servers, some queries will fail: neither the name nor the IP address can then be resolved outside the defined zone.

DNS also plays a role in email routing. For example, a **MX** (_Mail Exchange_) record specifies the mail servers responsible for receiving e-mails for a given domain. These records define priorities (weighting factor) and failover solutions. The zone file of a DNS server must contain a **SOA** (_Start Of Authority_) record, which designates the server as the official source of information for that zone.

Thanks to its hierarchical, distributed structure, DNS remains a cornerstone of the Internet, allowing users to access services through clear, memorable domain names instead of long, technical IP addresses.

In the next chapter, we'll explore another fundamental concept: **Ethernet addresses**, also known as **MAC addresses**, which ensure data delivery at the physical layer of local networks.


## Discovering Ethernet addresses and ARP

<chapterId>d02109f6-9bf9-4261-a8f9-e1aa4398b949</chapterId>


### Definitions

For the data routing protocol to work reliably and consistently, one key component is essential. As humans, we can easily identify a machine by its IP address or by its name retrieved through DNS. A machine, however, must be able to unambiguously recognize the destination device to deliver packets. To do this, it relies on a specific hardware identifier, directly used by its network interface: the MAC address (_Media Access Control_).

**Note**: This has nothing to do with a "physical address" in memory architecture. In computing, a physical memory address refers to a specific location on the memory bus, as opposed to a virtual address managed by the operating system. A MAC address, by contrast, relates strictly to network hardware.

A MAC address is permanently and uniquely assigned by the manufacturer the equipment is manufactured. The MAC address unequivocally identifies the network card whether it's a computer, smartphone, printer, or any other connected device. Unlike an IP address, which can change dynamically (via a DHCP server or manual configuration), the MAC address normally remains the same throughout the device's lifetime, unless it is deliberately altered.

Every network interface, wired or wireless, has its own MAC address. This address is used within the data link layer (layer 2 of the OSI model) to insert and manage the hardware address in each network frame exchanged. This is sometimes referred to as the _Ethernet address_ or _UAA_ (_Universally Administered Address_). Standardized on a length of 48 bits, or 6 bytes, it is written in hexadecimal notation, generally in the form of bytes separated by `:` or `-`.

For example: `5A:BC:17:A2:AF:15`

In this structure, the first three bytes identify the network card manufacturer: this is known as the **OUI** (*Organisationally Unique Identifier*). These prefixes, assigned by the IEEE, are also used in other hardware addressing schemes, such as Bluetooth and LLDP, to guarantee worldwide uniqueness.

### Changing a MAC Address (MAC Spoofing)

In theory, the MAC address is designed to remain fixed, but there are ways of modifying it, notably to meet particular needs or to circumvent certain constraints. This operation, often referred to as _spoofing MAC_, involves replacing the original hardware address with a different value, defined at software level. Some operating systems facilitate this modification, particularly when the actual Ethernet address is not directly used by the driver.

The reasons for such a change are varied. It could be the need for a given application to require a specific Ethernet address in order to function correctly, or to resolve a conflict of identical addresses between two devices sharing the same local network.

Changing the MAC address can also be motivated by privacy considerations: by hiding the unique identifier engraved on the card, users reduce the possibility of their device being tracked by networks or surveillance services. However, this practice is not without consequences. Changing a MAC address can disrupt certain filtering devices, or require firewalls to be reconfigured to authorize the new hardware.

Some networks, particularly Wi-Fi, use MAC address filtering to allow only devices with approved addresses. While this adds a basic level of control, it is not secure on its own. An attacker can capture a valid MAC address already authorized on the network and clone it to bypass restrictions. For this reason, MAC filtering should always be combined with stronger security measures.

### MAC/IP correspondence

For a local network to work efficiently, there must be a clear mapping between physical addresses (MAC addresses) and logical addresses (IP addresses). Without this link, a computer might know the IP address of a destination but wouldn't know how to physically send data to it on the local network.
This mapping is handled automatically by the ARP (_Address Resolution Protocol_).

In practice, when a user wants to know the MAC address corresponding to a specific IP address, the user can use the `arp` utility. This tool checks the machine's local ARP table to display known matches between IP addresses and MAC addresses on the local network. In this way, it is possible to quickly verify the effective link between the logical and physical layers.

Practical example: if you want to check which network card corresponds to the IP address `192.168.1.5`, use the following command:

```bash
arp –a 192.168.1.5
```

The output will display the associated physical address (MAC), the nature of the input (static or dynamic) and the Interface concerned.

```
Interface: 192.168.1.5 --- 0x5
IP Address            MAC Address                Type
192.168.1.5           00:54:BC:17:14:6E          D
```

It's important to remember that the MAC address and the IP address are two completely different identifiers, yet closely complementary. The MAC address is uniquely engraved into each network interface by the manufacturer and is used to physically identify the device on the local network. The IP address, on the other hand, is a logical address assigned either dynamically or statically, allowing the machine to join the IP network and exchange packets beyond its local network.

- Visual example of MAC address:

![Image](assets/fr/032.webp)


- Visual example of an IP address:

![Image](assets/fr/027.webp)


In a corporate environment, these two addressing levels cannot function separately. For example, when a DHCP server automatically assigns an IP address, the MAC address of the equipment is used as the starting point. The computer sends a DHCP broadcast request containing its MAC address so the server can assign an available IP address to the correct device. Without this hardware identification, the DHCP server wouldn't know which device to deliver the address to.

The ARP protocol is therefore fundamental: it provides the link between IP addresses and physical addresses, enabling machines to translate a logical destination into an actual physical destination. When a computer needs to send a packet to a machine on the same network, it first consults its ARP table to check whether the recipient's MAC address is already known. If not, it broadcasts an ARP request to all hosts on the local network. The machine that recognizes the target IP address in this request responds by specifying its MAC address. The sender then writes this IP/MAC pair to his ARP cache, to avoid having to repeat the operation each time the request is sent.

This ARP table acts as a mini-mapping directory, dynamically updated in a similar way as DNS associates domain names with IP addresses. Without ARP, no local exchange would be possible, as the data link layer needs to know the MAC address in order to encapsulate Ethernet frames correctly.

Conversely, the RARP protocol (_Reverse Address Resolution Protocol_) was designed for the opposite situation: enabling a machine that knows only its MAC address to discover its IP address. This was common the case for older workstations without a local hard disk, which had to boot over the network and request an IP address. RARP was eventually replaced by **BOOTP** and then **DHCP**, which are more flexible and automated.

These association protocols play an important role in routing. A router is essentially a machine with multiple network interfaces, connecting different segments. When a router receives a frame, it processes it to extract the IP datagram and examines the IP header to determine the destination. If the destination is on a directly connected network, the datagram is delivered directly after updating the header. If the destination belongs to another network, the router consults its routing table to identify the best path, or _next hop_, to the destination.

This breaks the route into shorter, more manageable segments. Each intermediate router only knows the next step, not necessarily the final destination.

**Reminder:** Direct delivery happens when sender and receiver are on the same physical network. Otherwise, delivery is indirect and passes through one or more routers.

The routing table, managed either manually (static routing) or dynamically (dynamic routing), contains the information needed to decide which route to take. In small networks, a static configuration is enough. In larger infrastructures, dynamic routing is essential to automatically adjust routes when the topology changes or a link goes down.

The routing table acts as a mapping table between target IP addresses and next gateways. It usually stores network identifiers (_network ID_) rather than every individual host address, which greatly reduces its size.

| Destination Address | Next-Hop Router Address | Interface |
| ------------------- | ----------------------- | --------- |

Using these entries, the router can quickly determine through which Interface and to which node each datagram should be sent. Combined with ARP for resolving the matching MAC addresses, this ensures efficient and reliable data transfer across the network.

Finally, dynamic routing protocols include standards such as RIP (_Routing Information Protocol_), based on the distance algorithm, and OSPF (_Open Shortest Path First_), which calculates the shortest paths in complex topology. These protocols constantly exchange updates to optimize routes, reduce transmission costs, and improve resilience against outages or congestion.


## NAT: Address Translation

<chapterId>4f984d5d-f2e0-4faf-b703-ff315f32cef4</chapterId>


### Definition

Network Address Translation_ (NAT) is a technique developed to address the gradual depletion of available IPv4 addresses. Designed as an interim solution before the widespread adoption of IPv6, NAT enabled companies and individuals to keep connecting large numbers of machines while using only a limited set of public IP addresses.

**Important reminder:** the move from IPv4 to IPv6 theoretically solves the exhaustion problem by expanding the address space from 32 bits to 128 bits, providing an almost unlimited number of addresses (2^128). In practice, however, the transition is still incomplete, and NAT remains widely used today.

The principle behind NAT is simple but highly effective: instead of assigning a unique public IP address to every device on the internal network, a single routable address (or a small pool of addresses) is used for all private devices. The NAT gateway, often integrated into the router or firewall, then dynamically translates the internal IP address along with the information needed to route traffic correctly to the outside world, and ensures that responses are returned to the original sender.

This approach has an immediate benefit: it completely hides the internal network architecture. To an outside observer, all requests from workstations, servers or printers appear to come from the same public identity. Private addresses, usually taken from reserved ranges (e.g. 192.168.x.x or 10.x.x.x), remain invisible from the Internet.

In addition to addressing IPv4 scarcity, NAT also strengthens security by creating a first logical barrier between the internal and public networks. Unsolicited inbound communications are naturally blocked, since only connections initiated from inside the network benefit the necessary translation to receive responses.


![Image](assets/fr/035.webp)


### Translation types

NAT can be implemented in different ways to suit specific needs. The two main modes of operation are static translation and dynamic translation.

**Static translation** creates a fixed mapping between a private IP address and a public IP address. Each internal machine is permanently linked to its dedicated public address. For example, an internal device configured as 192.168.20.1 could be associated with the routable address 157.54.130.1. When an outgoing packet leaves the local network, the router replaces the packet's source address with the public address, and performs the reverse operation for incoming traffic. This bidirectional translation is transparent to the user.

**Warning:** While this method isolates the internal network, it doesn't solve the shortage of public IP addresses, since you still need as many public addresses as there are machines to expose. Static translation is therefore mainly used when certain internal resources must remain reachable from the outside (web server, mail server...).

**Dynamic translation**, on the other hand, uses a pool of public IP addresses. When an internal host starts a connection, the router temporarily assigns one of these public addresses to the host's private address for the duration of the session. The link is 1-to-1, but temporary:once the connection ends, the public address becomes available for another device. Dynamic NAT therefore reduces the number of public addresses needed when not all machines are online at the same time, but it still requires a block of external addresses at least as large as the maximum number of simultaneous connections.

**Port translation** (PAT), also known as *NAT overload* or *IP masquerading*, goes a step further: all private devices share a single public IP address (or a very small number). To distinguish sessions, the gateway modifies not only the source address, but also the source port. It keeps a table linking each *(private address, private port)* pair to a unique *(public address, public port)* pair. This form of NAT is used in almost all home routers, allowing dozens of devices (computers, smartphones, connected objects, etc.) to share the same public IP address, while maintaining fluid communication.

NAT therefore extends IPv4's lifespan, while adding a valuable layer of segmentation and security. However, as IPv6 adoption grows and its vast address space become more widely used, the role of NAT will likely decline, though for compatibility and control purposes, it will still be used in some environments to segment and filter traffic.

### NAT implementation

To ensure the proper operation of address translation, the NAT router or gateway must keep an accurate record of the mappings established between each private address on the internal network and the public address it uses to communicate with the outside world. This information is stored in what's known as the "NAT translation table", which plays a central role in managing network traffic.

Each entry in this table links at least one pair: the internal IP address of the sending machine and the external IP address that will be exposed on the Internet. When a packet from the private network is sent to a public destination, the NAT router intercepts the frame, analyzes the IP and TCP/UDP headers, then replaces the private source address with the gateway's public address. On the return path, the same gateway captures the incoming packet, checks the mapping table and performs the reverse operation to redirect the flow to the original internal IP address.

This dynamic translation principle relies on precise table management: each entry remains valid as long as there is active traffic to justify it. After a configurable period of inactivity, the entry is cleared and can be reused for new connections.

_Example of a simplified NAT translation table:_

| Internal IP   | External IP    | Duration (sec) | Reusable? |
| ------------- | -------------- | -------------- | --------- |
| 10.101.10.20  | 193.48.100.174 | 1,200          | no        |
| 10.100.54.251 | 193.48.101.8   | 3,601          | yes       |
| 10.100.0.89   | 193.48.100.46  | 0              | no        |

In this example, if no packet has passed through for the second entry in over an hour (3,600 seconds), it is marked as reusable. Conversely, a duration of zero indicates an active communication, with the mapping locked.

While NAT operates transparently for most common uses (web browsing, e-mail, file transfer, etc.), it can create additional challenges for certain network applications. Some technologies rely on explicitly exchanging IP addresses or ports within the packet payload. After passing through a NAT gateway, this information becomes inconsistent.

Typical examples of limitations include:
- Peer-to-peer protocols (P2P), which require direct connections between devices, are hindered by the NAT barrier, since all internal machine shares the same external IP address and cannot be reached directly without specific configuration (such as *port forwarding* or UPnP);
- The IPSec protocol, used to secure network communications, encrypts packet headers. Because NAT must modify these headers to replace IP addresses, encryption makes this impossible without adaptation mechanisms such as NAT-T (*NAT Traversal*);
- The X Window protocol, which allows remote display of graphical applications on Unix/Linux, works in a way that the X server actively sends TCP connections to clients. This reversal of the usual direction of connections can be blocked by NAT.

In general, any protocol that explicitly includes the internal IP address in the packet payload will be affected, since that address will no longer match the real, internet-visible address after translation.

**Important note:** To address these issues, some NAT routers offer _Deep Packet Inspection_ (DPI) or _Protocol Helpers_ , which inspect packet contents to identify and dynamically replace addresses or port numbers within application data. This requires in-depth knowledge of the protocol format, and can create security vulnerabilities or increase resource usage.

**Caution:** Although NAT helps hide the internal network and control incoming traffic, it is not a substitute for a dedicated firewall. Translation alone is not a complete security barrier: it must always be complemented by clear filtering rules to block unsolicited or unwanted traffic.

_To illustrate how this works in practice, consider the following example:_


![Image](assets/fr/037.webp)


In this scenario, an internal workstation can access the internal web server simply by calling the URL `http://192.168.1.20:80`. Specifying the port is optional here, since `80` is the standard HTTP port.Conversely, if a request is initiated from the outside, the user will enter the public address `http://85.152.44.14:80`. The NAT router receives the request, consults its mapping table, and automatically translates the public address into a private one, redirecting the connection to `http://192.168.1.20:80`.

The same principle applies to any other server authorized to receive internet connections, such as the Extranet server (blue circuit in the diagram).

**Practical note:** in virtualized environments, network interfaces called _virbrX_ (for _Virtual Bridge X_) are commonly used. These virtual bridges, provided in particular by the libvirt library or the Xen hypervisor, connect the virtual internal network of guest machines to the physical network while applying NAT. They are generally configured via scripts in `/etc/sysconfig/network-scripts/`, as shown below for `virbr0`:

```ini
NAME=""
BOOTPROTO=none
MACADDR=""
TYPE=Bridge
DEVICE=virbr0
NETMASK=255.255.255.0
MTU=""
BROADCAST=192.168.0.255
IPADDR=192.168.0.1
NETWORK=192.168.0.0
ONBOOT=yes
```

Once the virtual bridge is in place, you need to enable IP routing and configure port translation with `iptables`:

```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```

```shell
iptables -t nat -A POSTROUTING -o <WAN> -s 192.168.0.0/24 -j MASQUERADE
```

With this configuration, outgoing traffic is routed and NAT translation is applied, allowing virtual machines to communicate with the outside world without directly exposing their internal IP addresses.

In the next chapter, we'll look in detail at IP address configuration under Linux, covering both simple and advanced methods suited to different administration contexts.


https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864


## How do I configure the network with `ip`?

<chapterId>8ba7e946-d2a0-4841-8d54-e85ba96baa25</chapterId>


### Standard configuration

After covering the theoretical foundations of networking and understanding how IP addresses, masks, routing, and translation work together, it's time to move on to practical configuration. On GNU/Linux, network setup is now handled with the **`ip`** command (_iproute2_ package), which replaces the older `ifconfig`.

`ip` lets you assign or change an IP address, change a mask, start or stop an interface, or check its status at any time.

**TIPS:** to display all interfaces (active or not): `ip addr show`

Example: assigning a static address and activating Interface

Add address `192.168.1.2/24` to Interface `eth0`:

```shell
ip addr add 192.168.1.2/24 dev eth0
```

Activate Interface:

```shell
ip link set dev eth0 up
```

Deactivate the same Interface:

```shell
ip link set dev eth0 down
```

Display the status of a specific Interface:

```shell
ip addr show dev eth2
```

**Practical tip:** with `ip`, adding an additional address to an interface no longer requires a `:1` suffix. Just add another `ip addr add ...` line:

```shell
ip addr add 172.18.2.39/24 dev eth2
```

### Activation scripts: ifup / ifdown

The `ifup` and `ifdown` utilities read static configuration files from `/etc/sysconfig/network-scripts/` (on RHEL, CentOS, Rocky Linux, AlmaLinux...) or `/etc/network/interfaces` (on Debian/Ubuntu) to cleanly bring interfaces up or down.

```shell
ifup eth1
ifdown eth2
```

Configuration files (RHEL-like):
- **/etc/sysconfig/network**: global settings (NETWORKING, HOSTNAME, GATEWAY...).
- **ifcfg-**: settings specific to each interface.

Static example (ifcfg-eth0):

```ini
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.2.5
NETMASK=255.255.255.0
GATEWAY=192.168.2.1
```

DHCP example:

```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```

This modular structure is still valid and can be easily automated on current systems.

### Advanced configuration: bonding

In professional environments, the aim is to guarantee service continuity and/or to aggregate bandwidth. *Bonding* (or *teaming* with _teamd_) mechanisms meet these needs: several physical interfaces function as a single logical Interface, often called `bond0` or `team0`.


![Image](assets/fr/039.webp)


Prerequisites:
- Load the `bonding` module (or use `teamd`) ;
- Have at least two physical interfaces available.

#### The various common bonding methods:

|Mode|Name|Principle|
|---|---|---|
|0|balance-rr|Round-robin, cyclic distribution of frames|
|1|active-backup|Single active interface with hot failover |
|2|balance-xor|Selection based on XOR of src/dst MAC addresses|
|3|broadcast|Broadcast simultaneously on all interfaces   |
|4|802.3ad (LACP)|Standardized dynamic aggregation; requires compatible switch|
|5|tlb (Transmit Load Balancing)|Balancing based on transmit load|
|6|alb (Adaptive Load Balancing)|Adaptive balancing; also balances receive via ARP|

#### Setting up with `ip link

- Disable physical interfaces:

```shell
ip link set eth0 down
ip link set eth1 down
```

- Creat the bonded Interface:

```shell
ip link add bond0 type bond mode balance-alb
```

- Configure options after creation

```shell
ip link set bond0 type bond miimon 100
```

- Assign MAC and IP addresses:

```shell
ip link set dev bond0 address 00:17:56:BC:02:3A
ip addr add 192.168.2.3/24 dev bond0
ip route add default via 192.168.2.1
```

- Attach slave interfaces:

```shell
ip link set eth0 master bond0
ip link set eth1 master bond0
```

- Bring everything back up:

```shell
ip link set bond0 up
ip link set eth0 up
ip link set eth1 up
```

**Tip:** to detach a slave without taking down the bond: `ip link set eth1 nomaster`

#### Permanent configuration (RHEL-like)

Create three files in `/etc/sysconfig/network-scripts`:

_ifcfg-bond0_

```ini
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=none
IPADDR=192.168.2.3
NETMASK=255.255.255.0
BROADCAST=192.168.2.255
GATEWAY=192.168.2.1
BONDING_OPTS="mode=balance-alb miimon=100"
```

_ifcfg-eth0_

```ini
DEVICE=eth0
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```

_ifcfg-eth1_

```ini
DEVICE=eth1
ONBOOT=yes
MASTER=bond0
SLAVE=yes
```

Then:

```shell
systemctl restart network
```

#### Additional IP address (modern alias)

With `ip`, you can simply add a second address to the same device:

```shell
ip addr add 192.168.1.2/24 dev eth0
```

To make this alias persistent after a reboot, either add a second `IPADDR2=...` / `PREFIX2=...` block to `ifcfg-eth0`, or create a new *NetworkManager* connection via `nmcli`.

Thanks to `ip` and related commands (`ip link`, `ip addr`, `ip route`), network configuration is more consistent, scriptable and clear. Bonding is a key component of high-availability architectures, and assigning multiple addresses to a single interface has become much simpler.

In the next chapter, we’ll look at the specifics and implementation of IPv6 addressing.

# IPv6 addressing

<partId>9b1d87f1-2a68-496e-b5dd-76cf74fb8cde</partId>

## IPv6: Standards and definitions

<chapterId>d1f16f0a-1104-460d-8d67-f725665f8e3f</chapterId>


We now move to the next generation of IP addressing: the IPv6 protocol, originally known as IPng (_IP Next Generation_). Designed to overcome the structural limitations of IPv4, this protocol introduces a vastly expanded addressing architecture, as well as numerous technical optimizations.

The motivations behind the adoption of IPv6 are varied, and address critical needs for the evolution of the Internet. Firstly, IPv6's role is to support the exponential growth in the number of connected devices (an objective unattainable with IPv4's limited address space). Secondly, the protocol aims to reduce the size of routing tables, making exchanges more efficient and reducing the workload of routers in the long term.

IPv6 also seeks to simplify certain aspects of packet handling, improving datagram flow and optimizing transfer speeds between networks. From a security standpoint, the AH/ESP headers of the *IPsec* protocol are included in the base specification, and all IPv6 nodes must be able to support them (RFC 6434). Their use, however, remains optional: it is up to the administrator to enable them depending on the context.

Other objectives include more precise handling of service types, notably to ensure better quality for real-time applications (VoIP, videoconferencing, etc.). IPv6 is also designed to allow more flexible mobility management: a device can change access points without changing its address in a way that is visible to its peers.

Finally, IPv6 was designed to coexist with legacy protocols. Although it is not directly binary-compatible with IPv4, it remains fully interoperable with higher-layer protocols such as TCP, UDP, ICMPv6 and DNS, as well as with routing protocols such as OSPF and BGP, subject to certain adjustments. For multicast management, IPv6 uses the MLD (*Multicast Listener Discovery*) protocol, which is the functional equivalent of IGMP in the IPv4 environment.

### Notation rules

One of the most significant changes in IPv6 is the format of the IP address itself. To address the chronic shortage of IPv4 addresses, the length of the address has been increased from 32 bits to 128 bits, so 16 bytes. In theory, this yields a possible address space of:

$$3.4 \times 10^{38}$$

This ensures virtually unlimited capacity for all current and future equipment.

IPv6 addresses are written very differently from the familiar dotted decimal notation. An IPv6 address is made up of eight 16-bit groups, written in hexadecimal and separated by colons `:`.

For example:

```
1987:0c02:0000:84c2:0000:0000:cf2a:9077
```

To simplify notation, leading zeros in each group can be omitted. The above example then becomes:

```
1987:c02:0:84c2:0:0:cf2a:9077
```

In addition, a single continuous sequence of zero groups can be replaced with::, further shortening the address:

```
1987:c02:0:84c2::cf2a:9077
```

**Warning:** this rule is strict: only one sequence of consecutive zeros can be replaced by `::`. If an address contains multiple zeros sequences, only the longest one is condensed. This ensures both uniqueness and readability.

**Important detail:** the `:` characterused to separate hexadecimal blocks can cause ambiguity in URLs, since `:` is also used to indicate a service port. To avoid confusion, IPv6 addresses in URL must be enclosed in square brackets `[ ]`.

Example of HTTP access to a specific port for the address `2002:400:2A41:378::34A2:36`:

```
http://[2002:400:2A41:378::34A2:36]:8080
```

When representing an IPv4 address in an IPv6 context, you can use a mixed notation in dotted decimal form, preceded by`::`:

```
::192.168.1.5
```

This compatibility helps ease the transition between the two protocols by allowing IPv4 blocks to be included within the IPv6 address space.

**Note:** To standardize how addresses are written, RFC 5952 defines a canonical format with abbreviation rules to avoid multiple representations of the same address. Following these recommendations helps reduce misinterpretation and ensures consistent network configurations.

### IPv6 address types

IPv6 differs from its predecessor through a wide range of address categories, each designed to specific uses, while allowing flexible routing and network management. As with IPv4, addresses can be global, local, reserved or specific to certain transition mechanisms.

An unspecified IPv6 address is represented by `::` or, more explicitly, `::0.0.0.0`. This special form is used during address acquisition, or as a default value to indicate the absence of an address.


| IPv6 Address Prefix | Description                                 |
| ------------------- | ------------------------------------------- |
|::/8                | Reserved addresses                          |
| 2000::/3            | Unicast addresses, routable on the Internet |
| fc00::/7            | Unique local addresses (1)                  |
| fe80::/10           | Link-local addresses                        |
| ff00::/8            | Multicast addresses                         |

(1): *On a private LAN, the `fd00::/8` prefix is preferred for assigning internal addresses that are not routable on the Internet.*

#### Reserved addresses

Certain IPv6 ranges are explicitly reserved and must not be used as global addresses. They have specific technical purposes:
- **`::/128`**: unspecified address, never permanently assigned to a device, but used as a source address by a machine awaiting configuration.
- **`::1/128`**: the _loopback_ address, the direct equivalent of `127.0.0.1` in IPv4, which allows a machine to address itself.
- **`64:ff9b::/96`**: Reserved for protocol translators to enable IPv4/IPv6 interconnection, as defined in RFC 6052.
- **`::ffff:0:0/96`**: compatibility block for representing an IPv4 address in a specific IPv6 structure, often used internally by applications.

These blocks guarantee interoperability and facilitate migration between the two protocol version.

#### Global unicast addresses

Global unicast addresses make up most of the publicly routable IPv6 space, representing about 1/8th of the address space. Since 1999, IANA has allocated these blocks, such as the `2001::/16` prefix, in CIDR blocks (from `/23` to `/12`) to regional registries, which then redistribute them to providers and organizations.

Some ranges have special documented uses:
- **`2001:2::/48`**: Reserved for performance and interoperability testing (RFC 5180).
- **`2001:db8::/32`**: Reserved for documentation and examples (RFC 3849).
- **`2002::/16`**: Used for the 6to4 mechanism, which allows IPv6 traffic to travel across an IPv4 infrastructure (useful during the transition phase between the two protocols).

**Note:** a large proportion of global addresses remain unused, serving as a reserve for future Internet growth.

#### Unique local addresses (ULA)

Unique local addresses (`fc00::/7`) are the IPv6 equivalent of IPv4 private addresses (RFC1918). They enable the creation of isolated internal networks without risking conflicts with public addressing. In practice, the effective prefix is `fd00::/8`, with the 8th bit set to 1 to indicate local usage. Each ULA block includes a 40-bit pseudo-random identifier, minimizing address collisions when connecting separate private networks.

#### Link-local addresses

Link-local addresses (`fe80::/64`) are used exclusively for communication within the same Layer 2 segment (same VLAN or switch). They are never routed beyond the local link. Each network Interface automatically generates a link-local address, often derived from its MAC address using the EUI-64 scheme.

**Special feature**: the same machine can use the same link-local address on multiple interfaces, but the interface must be specified when communicating to avoid ambiguity.

#### Multicast addresses

In IPv6, broadcast has been replaced by multicast, a more efficient way to deliver packets to a defined group of recipients. The multicast range is prefixed with `ff00::/8`. These includes addresses like `ff02::1`, which targets all nodes on the local link. While convenient, this address is no longer recommended for applications, as it can generate uncontrolled broadcasts.

A common use of multicast is the _Neighbor Discovery Protocol_ (NDP), which replaces ARP in IPv6. NDP uses specific multicast addresses, such as `ff02::1:ff00:0/104`, to automatically discover other hosts connected to the same link.

By combining these address types, IPv6 provides a complete set of options to meet the needs of global routing, local communications, IPv4/IPv6 migration, and automatic device configuration, while improving transmission efficiency.

### Address scope

The scope of an IPv6 address defines the exact domain in which it is valid and unique. Understanding this concept is key to mastering packet routing and logical organization of an IPv6 network. IPv6 addresses are generally grouped into three main categories based on their scope and usage: unicast, anycast and multicast.

**Unicast addresses** are the most common and include several distinct subtypes. 
These include the _loopback_ (`::1`) address, whose scope is limited to the host using it, and which is used to test the network stack internally without sending traffic over the physical network. 
Then there are link-local addresses (_link-local_), whose scope is restricted to a single network segment: they are used for direct communications between devices on the same physical or logical link (e.g. a single switch or VLAN). 
Finally, unique local addresses (_ULA_, for _Unique Local Addresses_) are internal to a private network. They may be routed between multiple private segments but are never visible on the Internet.

Conceptually, IPv6 addresses are often represented as a binary structure where the first half (the first 64 bits) identifies the network prefix, and the second half (also 64 bits) uniquely identifies the device's interface on that network. This split makes address autoconfiguration easier through mechanisms like SLAAC (_Stateless Address Autoconfiguration_), which allow machines to automatically generate a stable address based on the MAC address or a pseudo-random identifier.

| Field     | Prefix | L | Global ID | Subnet | Interface ID |
|-----------|--------|---|-----------|--------|---------------|
| Bits      | 7      | 1 | 40        | 16     | 64            |

The IPv6 architecture follows the hierarchical global routing model of today's Internet. Prefix partitioning enables regional registries and network operators to manage address allocation in a decentralized way, while ensuring global uniqueness. Within this framework the same host can simultaneously hold a global unicast address for internet communication and a link-local address for local interactions, e.g. with immediate neighborhood or for router discovery messages.

| Field     | Prefix | Zero | Interface ID |
|-----------|--------|------|--------------|
| Bits      | 10     | 54   | 64           |

**Anycast addresses** represent an intermediate concept that builds on the unicast model but can behave like multicast in certain cases. An anycast address is, in essence, a unicast address assigned to several interfaces distributed over different network nodes. When a packet is sent to an anycast address, the IPv6 protocol aims to deliver it to one of the hosts sharing that address, typically the one closest in terms of routing topology. This approach optimizes query processing speed and improves the resilience of distributed services. A classic example is the root DNS servers, where anycast addressing automatically directs queries to the nearest point of presence.


| Field     | Prefix | Subnet | Interface ID |
|-----------|--------|--------|--------------|
| Bits      | 48     | 16     | 64           |

In IPv6, **multicast addresses** replace the broadcast mechanism, which was considered too costly and unsuitable for a global-scale network. A multicast address identifies a group of interfaces, typically across multiple hosts, that wish to receive the same packets simultaneously. 
Each multicast address includes a special 4-bit _scope_ field, which defines the geographic or logical limit of the broadcast:
- A scope of `1` means the packet is for the local device only.
- A scope of `2` restricts the packet to the local link: all devices on the same physical or virtual segment can receive it.
- A scope of `5` extends the reach to a site, typically an entire corporate network.
- A scope of `8` extends the reach to an organization, enabling delivery across all subnets of the same entity.
- A scope of `e` (14 in hexadecimal) indicates a global reach, making the multicast group accessible from anywhere on the Internet if the routing infrastructure supports it.

The structure of an IPv6 multicast address includes: 
- a _Flag_ field (4 bits) specifies whether the group is permanent or temporary,
- a _Scope_ field (4 bits) defines the scope, 
- an identification field (112 bits) identifying the multicast group number.

| Field      | Prefix | Flags | Scope | Group ID |
|------------|--------|--------|--------|----------|
| Bits       | 8      | 4      | 4      | 112      |

A well-known example of IPv6 multicast in action is the _Neighbor Discovery Protocol_ (NDP). Rather than using ARP as in IPv4, NDP relies on multicast addresses such as `ff02::1:ff00:0/104` to broadcast neighbor discovery requests, targeting only the relevant hosts on the same link.

By defining address scopes so precisely, IPv6 structures how data flows are sent, received, and routed. This granularity makes the protocol more flexible and efficient for managing both local and global communications, while avoiding the downsides of generalized broadcasting.

## Address assignment in a local network

<chapterId>4c9c3e52-59bc-499a-af0a-6dd369a9e029</chapterId>

In this chapter, we'll look at one of the most practical aspects of IPv6 deployment: assigning IP addresses to hosts on a local network. The IPv6 architecture has been designed for flexibility, allowing each device to generate its own address automatically, while still allowing fully manual configuration when needed.

An IPv6 local network systematically divides the address into two parts: 
- the first 64 bits represent the subnet prefix, usually provided by a router or an address authority;
- the remaining 64 bits are used by the host to uniquely identify itself on that segment. 
This model greatly simplifies route aggregation and address block management.

Two main approaches are used to assign addresses to devices:
- Manual configuration, where the administrator specifies each interface's exact address;
- Automatic configuration,where devices generate or obtain their own addresses dynamically.

In manual configuration, the administrator assigns the complete IPv6 address to each interface. Certain values remain reserved:
- `::/128`: unspecified address, never permanently assigned ;
- `::1/128`: loopback address (_loopback_), IPv4 equivalent: `127.0.0.1`.

Unlike IPv4, there is no _broadcast_ concept; "all zeros" or "all ones" combinations in the host portion have no special meaning.
Manual configuration is still useful in controlled environments but becomes difficult to maintain at scale.

For automatic configuration, several methods exist:
- The **NDP** (_Neighbor Discovery Protocol_) protocol, specified by RFC4862, enables *stateless* auto-configuration. In this mode, the host receives a network prefix from a local router, and completes the address itself with an identifier based on its MAC address. This method is simple to deploy, and requires no central server.
- Implementations like those in Windows can generate the host portion pseudo-randomly to improve privacy by avoiding direct exposure of the MAC address. Revealing the MAC address in IPv6 packets can raise privacy concerns, as it allows tracking of a device across different networks.
- DHCPv6 protocol: Defined in RFC3315 and similar to the DHCP used for IPv4, it enables more controlled and centralized configuration, including lease management, extra options (DNS, MTU...), and databases registration. DHCPv6 can operate alone or alongside stateless configuration to provide additional parameters without assigning the IP address itself.

**Important note:** In the MAC-based method, the MAC address is converted to a 64-bit identifier using the EUI-64 format. This mechanism inserts the bytes `FF:FE` in the middle of the original MAC address (in 48 bits), and inverts the 7th bit to indicate global uniqueness. The result is a stable Interface identifier, used in the full IPv6 address.

Here's an example of how to transform a MAC address into EUI-64:

![Image](assets/fr/045.webp)


However, due to growing concerns over device tracking, modern operating systems (notably Linux, Windows 10+, macOS, Android) now enable privacy extensions by default. These use randomly generated interface identifiers that are periodically renewed for outgoing connections, while keeping a stable identifier for internal communications (such as DNS or DHCPv6).

As with DHCP in IPv4, automatically assigned IPv6 addresses can have two lifetimes, defined by DHCPv6 routers or servers:
- *Preferred lifetime*: after this period, the address remains valid, but is no longer used to initiate new connections;
- *Valid lifetime*: when this time expires, the address is completely removed from the Interface configuration.

This system makes it possible to manage network changes dynamically, for example, ensuring a smooth transition from one ISP to another. By updating the prefix announced by routers and adjusting DNS records in parallel, IPv6 migration can be carried out without any noticeable service interruption.

**Tip:** The combined use of address and DNS lifecycles makes it possible to implement a gradual transition strategy, where new connections move to a new topology, while existing connections continue until their natural end.

In short, IPv6 offers a wide range of flexibility for address assignment: manual configuration, stateless or stateful auto-configuration, DHCPv6, or random generation. EEach approach comes with its own advantages and limitations, and can be adapted according to the required level of control, the size of the network, or privacy needs.

## Assigning IPv6 address blocks

<chapterId>45cce866-1b58-4888-b3fe-15c922180839</chapterId>

### Address distribution

The IPv6 address allocation scheme has been structured to meet two objectives: to guarantee global address uniqueness, and to enable a logical hierarchy that favors the aggregation and simplification of routing tables. 
As with IPv4, the *Internet Assigned Numbers Authority* (IANA) sits at the top of this hierarchy. It manages the global unicast address space and delegates address blocks to the five regional Internet registries (_RIR_).

The five existing RIRs are:
- ARIN (North America),
- RIPE NCC (Europe, Middle East, Central Asia),
- APNIC (Asia-Pacific),
- AFRINIC (Africa),
- LACNIC (Latin America and the Caribbean).

IANA allocates IPv6 blocks of varying size to each RIR, generally between /23 and /12. These approach offers flexibility while ensuring long-term scalability. The RIRs, in turn, redistribute these blocks to Internet Service Providers (ISPs), large corporations, and public institutions.

Since 2006, each RIR has received an IPv6 /12 block from IANA, a fixed size designed to ensure a stable and sufficiently large reserve for future growth. RIRs usually subdivide these into /23, /26 or /29 blocks. ISPs most often receive /32 blocks, although this size can vary depending on the ISP's size and geographical area. They typically allocate /48 blocks to customers. Each /48 provides 65,536 distinct /64 subnets (an enormous capacity compared to IPv4).

**Important note:** a /32 block contains exactly 65,536 /48 sub-blocks. This means that every ISP can serve tens of thousands of customers without exhausting their allocation. Thanks to its /48, each customer will then have a gigantic amount of space to structure its own internal network with as many /64 segments as it wishes.

The typical allocation hierarchy looks like this:

| IANA | RIR | LIR | Customer | Subnet | Interface |
|------|-----|-----|----------|--------|-----------|
|  3   | 20  |  9  |    16    |   16   |     64    |

With this abundance of addresses, NAT (*Network Address Translation*), once essential in IPv4 to cope with address shortages, is no longer necessary. Every host can have a unique, globally routable public address, simplifying end-to-end connectivity and making protocols like IPSec, VoIP, or inbound connections easier to use.

To check which organization an IPv6 address belongs to, you can use the `whois` command to query public RIR databases. This transparency makes it possible to identify the organization that owns a prefix, which can be useful for network, analysis or security purposes.

### PA vs PI addressing

Originally, the IPv6 allocation model was based solely on PA (*Provider Aggregatable*) blocks, which means linked to the ISP. In this model, an organization receives its prefix from its ISP, meaning that changing providers requires renumbering the entire infrastructure.

While IPv6's auto-configuration features and address lifetimes make renumbering easier, it remains inconvenient for organizations with critical infrastructure or multiple provider connections for redundancy requirements.

Since 2009, allocation policies have allowed for PI (*Provider Independent*) blocks. These blocks (generally /48 in size) are allocated directly to a company or institution by an RIR, independently of any ISP. This model is particularly well suited to organizations practicing *multihoming*, (meaning connected to several operators simultaneously). For example, in Europe, RIPE-512 outlines the policy for PI allocations.

### Subnet mask notation

As in IPv4, IPv6  uses CIDR (*Classless Inter-Domain Routing*). This consists of indicating the number of bits making up the prefix after the address, using the `/` character.

Take the following example:

```
2001:db8:1:1a0::/59
```

This means that the first 59 bits are fixed and identify the network. All remaining bits (here 69 bits) can be used to identify subnets or hosts.

Thus, this notation covers addresses from `2001:db8:1:1a0:0:0:0:0` to `2001:db8:1:1bf:ffff:ffff:ffff:ffff`.

This block therefore covers a set of 8 /64 subnets, each capable of hosting a massive number of devices.

CIDR notation allows for precise address space planning, from large-scale networks to home setups and virtualized environments, and encourages route aggregation, reducing router load and improving scalability.

### IPv6 packets and headers

IPv6 packet format differs from IPv4 by being both simpler and more extensible. An IPv6 datagram always begins with a fixed-size header of 40 bytes containing all the essential routing information. This streamlined approach, compared to IPv4's header variable length (from 20 to 60 byte), enables faster and more efficient packet processing by routers.

However, IPv6 does not remove functionality: instead of integrating numerous optional fields in the main header, it introduces a system of extension headers, placed immediately after the basic header. These optional headers make it possible to add data or instructions specific to certain functions, without unnecessarily burdening ordinary packets.

Some extension headers follow a fixed structure, while others can hold a variable number of options. In These options are encoded as `{Type, Length, Value}` triplets:
- The "Type" field (1 byte) indicates the nature of the option;
- The first two bits of the "Type" specify what routers should do if the option is not recognized:
 - Ignore the option and continue treatment,
 - Drop the datagram,
 - Drop and send an ICMP error to the source.
 - Drop the datagram without notification (in the case of multicast packets).
- The "Length" field (1 byte) specifies the size of the "Value" field, from 0 to 255 bytes;
- The "Value" field contains the data associated with the option.

Here's an overview of the different types of extension headers defined by IPv6.

#### Hop-by-Hop header

This header, if present, is always placed immediately after the base header. It contains information that must be processed by every router along the packet's path, unlike most other headers, which are usually handled only by the destination node. Typical uses include signaling global parameters or requesting specific processing steps as the packet travels through the network.

![Image](assets/fr/047.webp)

#### Routing header

The routing header specifies a list of intermediate addresses the packet must pass through. There are two main routing modes:
- Strict routing: the exact path is predefined
- Loose routing: only certain mandatory steps are specified.

The first four fields of this rooting header are:
- **Next Header**: identifies the type of the next header;
- **Routing Type**: defines the routing method (usually `0`);
- **Segments left**: number of segments remaining to traverse ;
- **Address[n]**: list of intermediate addresses.

The "Segments Left" field starts with the total number of remaining segments and is decremented by one at each hop.

![Image](assets/fr/048.webp)

#### Fragmentation header

In IPv6, only the source host is allowed to fragment a datagram, unlike IPv4 where routers could also do so. All IPv6 nodes must be able to handle packets of at least 1280 bytes. If a router encounters a packet larger than the MTU of the next link, it sends an *ICMPv6 Packet Too Big* message back to the source, which then adjusts the size of its transmissions.

The fragmentation header contains the following fields:
- **Identification**: unique datagram identifier for reassembly.
- **Fragment Offset**: the fragment's position within the original datagram.
- **M flag**: indicates whether more fragments follow.

![Image](assets/fr/049.webp)

#### Authentication header (AH)

This header is designed to secure communications by verifying both the sender's authenticity and the integrity of the data. It is commonly used with the IPsec protocol. Using an authentication code, the recipient can confirm that the message truly comes from the expected sender and that it has not been altered in transit.

In the event of a fraudulent modification attempt, the authentication code will no longer match, and the datagram may be rejected. This mechanism also protects against replay attacks by detecting unauthorized duplications.

![Image](assets/fr/050.webp)

#### Destination Options Header

This header is intended only for the final recipient of the datagram. It can be used to add options or metadata specific to the application, without being taken into account by intermediate routers.

Initially, no such option was defined in the protocol. However, this header was introduced when IPv6 was designed, to allow future extensions to be added without modifying the overall packet structure. The null option, for example, is used only to pad the header to a multiple of 8 bytes for memory alignment purposes.

![Image](assets/fr/051.webp)

IPv6 packet design is built on a clear separation between a minimal base header and modular extension headers. This architecture ensures both standard processing performance and the flexibility needed to evolve the protocol and integrate security, complex routing or quality-of-service mechanisms, while maintaining compatibility with future infrastructures.

## Relationship between IPv6 and DNS

<chapterId>421eacb8-b80b-4aee-910f-e069ed805f00</chapterId>

In modern networks, the DNS (*Domain Name System*) translates domain names into IP addresses that machines can use. With the introduction of IPv6, DNS had to adapt to support 128-bit addresses while maintaining backward compatibility with IPv4. This coexistence is especially important in dual-stack environments, where both IP versions operate simultaneously.

### IPv6-specific DNS records

To associate a domain name with an IPv6 address, DNS uses a AAAA (*quad-A*) record, analogous to the  "A" record for IPv4 addresses. The AAAA record explicitly maps a domain name to an IPv6 address. 
Example:

```shell
ipv6.mydmn.org.         IN      AAAA    2001:66c:2a8:22::c100:68b
```

This record indicates that the domain `ipv6.mydmn.org` resolves to the IPv6 address `2001:66c:2a8:22::c100:68b`. It is possible, and even recommended for maximum compatibility, to associate the same domain name with several IP addresses, whether IPv4 (via an A record) or IPv6 (via an AAAA record). This allows IPv6-compatible customers to prefer IPv6, while ensuring IPv4-only clients remain supported.

In addition, DNS supports reverse resolution, meaning it can look up the domain name associated to a given IP address. In the case of IPv6, this operation uses PTR records placed in the `ip6.arpa` zone. This zone is specifically reserved for IPv6 reverse resolution. For IPv4, it is the `in-addr.arpa` zone.

### Reverse resolution

Reverse resolution of an IPv6 address follows a strict process: 
1) Expand the address into full hexadecimal notation (16 bytes, i.e. 32 hexadecimal digits).
Example:  

```shell
2001:66c:2a8:22::c100:68b
```

Becomes:

```shell
2001:066c:02a8:0022:0000:0000:c100:068b
```

2) Reverse the order of each hexadecimal digit (nibble), separate them with dots and append `ip6.arpa`:

```shell
b.8.6.0.0.0.1.c.0.0.0.0.0.0.0.0.2.2.0.0.8.a.2.0.c.6.6.0.1.0.0.2.ip6.arpa  IN PTR  ipv6.mydmn.org
```

This structure ensures standardized, unique reverse lookups in the IPv6 address space.

**Please note**: DNS queries can travel over either an IPv4 or IPv6. The transport protocol used has no effect on the type of records returned. 
For example:
- A client connected over IPv6 can request an IPv4 record.
- A client connected over IPv4 can request an IPv6 record. 
The DNS server simply responds with the records it has, regardless of the query's transport protocol.

When a hostname is mapped to both IPv4 and IPv6, the choice of which address to use is governed by RFC 6724, which defines an address selection algorithm based on factors such as prefix preference, scope, and reachability. By default, IPv6 is generally preferred unless overridden by system or network configuration.

**Important reminder**: when embedding an IPv6 address in a URL (*Uniform Resource Locator*), it must be enclosed in square brackets (`[]`). This avoids confusion between the colon (`:`) inside the IPv6 address and the colon separating the hostname from the port in the URL.

Valid example:

```shell
http://[2001:db8::1]:8080
```

This ensures that the URL is processed correctly by both browsers and web servers.

Integrating IPv6 into the DNS system therefore relies on new record types, a strict method for reverse resolution, and precise selection and formatting rules to ensure routing compatibility and consistency.

### Part summary

In this section, we explored the fundamental principles of IPv6 addressing. We began by examining the structure of IPv6 address: its 128-bit length, hexadecimal notation, and the simplification rules used to shorten repetitive sequences of zeros. This design enables IPv6 to overcome the limitations of IPv4's address space, while guaranteeing scalability and efficient hierarchy.

We then looked at the different categories of IPv6 addresses: unicast, anycast and multicast, detailing their scope, typical use and representation in the address space.

Next, we reviewed the methods of assigning IPv6 addresses within a local network, whether by manual configuration, via the DHCPv6 protocol, or using stateless autoconfiguration mechanisms such as those offered by NDP. These approaches enable devices to automatically generate their own address from the provided prefix and their MAC address (via EUI-64), while offering flexibility in terms of lifetime management and privacy.

We've also detailed how address blocks are allocated, starting from IANA, which distributes them to the five RIRs (*Registered Internet Regions*), and then to the ISPs, who redistribute them to their customers as subnets (often in /48, allowing 65536 /64 subnetworks). The distinction between _Provider Aggregatable_ (PA) and _Provider Independent_ (PI) blocks helps manage _multihoming_ or provider-change scenarios.

We saw that DNS has adapted to IPv6 with the introduction of the AAAA record, and that reverse resolution mechanisms now rely on the `ip6.arpa` zone. Importantly, DNS remains independent of the transport protocol used (IPv4 or IPv6), ensuring seamless interoperability in a dual-stack environment.

IPv6 is therefore not just an incremental improvement over IPv4, but a complete redesign of the addressing system, built to meet both current and future challenges of the global Internet.

In the final part of this NET 302 course, we will move into practice and focus on network diagnostic tools.


# Network diagnostic tools

<partId>368a5c6f-ec48-4b28-970f-3a770788ad37</partId>

## Network Access Layer tools

<chapterId>1d25a21d-6900-4fbe-a438-e06c8afb9e02</chapterId>

In this first chapter of the final section on network diagnostics, we focus on tools for analyzing the network access layer of the TCP/IP model. This layer is responsible for direct communication between devices on the same physical network, notably through the use of MAC addresses and physical network interfaces such as Ethernet cards or Wi-Fi interfaces.

The aim here is to provide administrators with practical tools to inspect, test and optimize this essential layer of low-level connectivity. These tools can be used to verify the proper operation of interfaces, troubleshoot network card configuration issues, or detect anomalies such as collisions, packet loss or link errors.

### IP/MAC neighborhood utilities

#### `Arp` tool

One of the oldest diagnostic tools at the Network Access layer is the `arp` command. Although increasingly replaced by modern alternatives such as `ip neigh` (which we'll discover shortly). `Arp` is still present on many systems to view or manipulate the ARP (*Address Resolution Protocol*) cache. This cache stores the mappings between IP addresses and MAC addresses known locally on a machine. In other words, it allows you to determine which physical (MAC) address corresponds to a given IP address on the local network.

In practice, when a host wants to send a packet to an IP address within the same subnet, it must first know the target machine's MAC address. This mapping is handled by ARP, which broadcasts a request on the local network and receives a reply containing the corresponding MAC address. This result is then stored temporarily in a local table called the "ARP cache", to avoid repeating the requests for every new packet.

To view the contents of this cache and check the entries currently known to the machine, use:

```bash
arp -a
```

This command lists all locally registered IP/MAC mappings, across all interfaces. Each line provides the host name (if resolvable), the IP address, the corresponding MAC address and the Interface where the mapping is observed.

To filter the display to a specific IP address, simply specify it:

```bash
arp -a 192.168.1.5
```

This makes it easy to check whether a particular IP address is present in the cache, which can help diagnose communication failures between two hosts on the same network.

Likewise, to display only the ARP entries associated with a specific network interface (for example an Ethernet card named `eth0`), you can use:

```bash
arp -a -i eth0
```

This is especially useful in multi-interface environments (wired, wireless, VPN, etc.), where one host may have several network adapters.

The `arp` command is not limited to read-only use. It can also be used to manually edit the ARP cache, an invaluable feature in certain advanced troubleshooting scenarios or when simulating specific conditions. For instance, you can manually add an IP/MAC mapping:

```bash
arp -s 192.168.1.7 00:17:BC:56:4F:25 -i eth2
```

This command creates a static entry in the local ARP table, associating the IP address `192.168.1.7` with the MAC address `00:17:BC:56:4F:25` on the Interface `eth2`.If no interface is specified, the system automatically uses the first applicable one.

You can also remove an entry from the ARP cache, either to correct an error or to force a rediscovery:

```bash
arp -d 192.168.1.7
```

This deletes the entry, ensuring that the next communication attempt triggers a fresh ARP request.

**NOTE**: The delete option also accepts an interface name, allowing you to target the removal of a specific entry more precisely.

In summary, the `arp` tool provides low-level diagnostics, particularly useful in local networks where connectivity problems can often be traced back to incorrect or obsolete address resolution. However, on recent systems, particularly with modern Linux distributions, this tool is increasingly being replaced by the `ip neigh` command, from the `iproute2` toolset, which offers similar functionality in a more unified framework.

#### `Ip neigh` tool

On modern systems, notably recent Linux distributions, the `ip neigh` command is the go-to tool for inspecting and managing mappings between IP and MAC addresses. This command is part of the `iproute2` suite, which is gradually replacing older tools such as `arp`, providing a more consistent and flexible framework for diagnostics at the data link layer.

The `ip neigh` command query the local IP neighbor cache, which is equivalent to the ARP cache for IPv4 and the NDP (_Neighbor Discovery Protocol_) cache for IPv6. This cache stores known associations between IP addresses (v4 or v6) and MAC addresses, along with their status (valid, pending, expired...).

The basic command to display the cache is:

```bash
ip neigh
```

This outputs a list of entries, showing the destination IP address, the relevant network interface, the associated MAC address (if available), and the entry's state (e.g. `REACHABLE`, `STALE`, `DELAY`, `FAILED`...).

Example output:

```bash
192.168.1.5 dev eth0 lladdr 00:17:BC:56:4F:25 REACHABLE
```

This line indicates that the machine knows of a valid mapping between IP address `192.168.1.5` and MAC address `00:17:BC:56:4F:25` via Interface `eth0`.

You can also filter entries by criteria such as IP address, interface, or state. For example, to query only address `192.168.1.7`:

```bash
ip neigh show 192.168.1.7
```

Or to display all entries for interface `eth1`:

```bash
ip neigh show dev eth1
```

Beyond consultation, `ip neigh` can also be used to manually edit the cache. For instance, to add a static entry:

```bash
ip neigh add 192.168.1.7 lladdr 00:17:BC:56:4F:25 dev eth1 nud permanent
```

This permanently associates the IP address `192.168.1.7` with the specified MAC address on interface `eth1`. The `nud permanent` option (for _Neighbor Unreachability Detection_) ensures that the entry will not be automatically invalidated.

Conversely, to delete a cache entry:

```bash
ip neigh del 192.168.1.7 dev eth1
```

This forces the system to re-resolve the mapping the next time it communicates with that address.

**NOTE**: The `ip neigh` tool works for both IPv4 and IPv6. For IPv4, it interfaces with ARP; for IPv6, it interacts with NDP. This provides a unified, consistent approach to managing IP/MAC relationships across protocol families, making `ip neigh` the modern standard for neighbor management on Linux systems.

### Package analysis tools

To thoroughly analyze what is happening on a computer network, administrators need tools that can capture the packets exchanged between machines. Two utilities stand out as benchmarks: `tcpdump` and `Wireshark`. These tools are essential for diagnosing abnormal behavior, auditing protocol exchanges, or studying network security by inspecting frame contents.

#### `ttcpdump`: command-line analysis

`tcpdump` is a highly powerful command-line tool designed to capture and display packets traveling through a network interface. It operates in real time, and thanks to its lightweight design, can be used on systems without a graphical interface or with limited resources. It relies on the `libpcap` library, which provides hardware-independent low-level capture functions.

A common use of `tcpdump` is to monitor the network activity of a machine or network segment, filtering packets according to specific criteria. Results can be redirected to a file, allowing traffic to be archived for later analysis or replayed in another tool, such as Wireshark.

The general command syntax is:

```bash
tcpdump -w <file.cap> -i <interface> -s <snapshot_length> -n <filters>
```

- `-w` writes captured packets to a file in `libpcap` format (extension `.cap` or `.pcap`);
- `-i` specifies the network interface to monitor (e.g. `eth0`, `wlan0`);
- `-s` sets the maximum amount of data captured per packet. Specifying `0` captures all packets;
- `-n` disables DNS and service name resolution, improving performance.

Expression filters at the end of the command let you restrict captures to a subset of traffic. You can combine the keywords `host`, `port`, `src`, `dst`, etc., to refine selection.

Example: to capture HTTP packets (port 80) to or from the `192.168.25.24` server, and save them in a `fichier.cap` file:

```bash
tcpdump -w fichier.cap -i eth0 -s 0 -n port 80 and host 192.168.25.24
```

The resulting file can later be analyzed in a graphical tool or replayed on another system.

#### Wireshark: advanced visual analysis

Wireshark, formerly known as *Ethereal*,is a complete network analysis program with a graphical interface. Unlike `tcpdump`, it provides structured, detailed visualization of packets, including protocol dissection, flow graphs, traffic statistics, and interactive filters. It also relies on `libpcap`, which means it can open and process capture files generated by `tcpdump`.

Wireshark is available on many operating systems, including Linux and Windows. Installing it requires administrator privileges to access the capture interfaces. Once launched, you can select a network interface from the *Capture* menu. Clicking *Start* begins real-time packet recording. The display is divided into three panes:
- the list of captured frames ;
- protocol-decoded details,
- raw hexadecimal data.


![Image](assets/fr/052.webp)


Wireshark excels in scenarios where you need to observe complex protocol behavior, reconstruct application dialogs (such as an HTTP or DNS session), or study service response times. It also supports highly specific display filters using its dedicated syntax (different from that of `tcpdump`) to focus only on relevant packets.

#### Complementary tools

It's important to note that `tcpdump` and Wireshark are not interchangeable: each has its own strengths. `tcpdump` is better suited to command-line environments, automated scripts and remote server interventions, while Wireshark is ideal for detailed, interactive and educational traffic analysis.

The two tools can be combined: a capture can be made on a remote system with `tcpdump`, then the `.cap` file is transferred for analysis with Wireshark on a local machine. This approach is widely used in practice.

### Interface analysis tools

At the Network Access layer, it is often necessary to query and configure physical network interfaces in order to diagnose malfunctions, optimize performance, or verify connection integrity. One of the most powerful tools available under Linux for this purpose is `ethtool`, a command-line utility that not only provides detailed technical information about an Ethernet interface, but also allows you to adjust some of its parameters in real time.

#### View Interface specifications

A core feature of `ethtool` is its ability to query an interface and display its current characteristics. This allows you to check:
- link speed (e.g. 100 Mbit/s, 1 Gbit/s or 10 Gbit/s) ;
- negotiation mode (half duplex or full duplex) ;
- whether autonegotiation is enabled;
- the type of port (copper, fiber, etc.) ;
- link status (active or not) ;
- support for advanced features such as *Wake-on-LAN*.

This information is especially useful for diagnosing problems related to physical connectivity or mismatched negotiation settings between the host's network card and the equipment it connects to (switch, router, etc.).

To obtain this information, simply run:

```bash
ethtool enp0s3
```

This command outputs a detailed report on the `enp0s3` interface, a common naming convention on CentOS or RHEL-based systems.


![Image](assets/fr/053.webp)


#### Dynamically modify Interface parameters

`ethtool` is not limited to observation: it also allows you to adjust certain interface parameters without rebooting the machine. This makes it possible, for example, to force a specific link speed or enable features according to the needs of the local network.

The `-s` option is used to dynamically configure parameters such as:
- link speed (`speed`), set explicitly (e.g. 1000 for 1 Gbit/s) ;
- duplex mode (`duplex`), either `half` or `full` ;
- enabling or disabling autonegotiation (`autoneg`) ;
- enabling of *Wake-on-LAN* (`wol`) ;
- port type.

Example 1: enable autonegotiation on an interface:

```bash
ethtool -s enp0s3 autoneg on
```

Example 2: enable the *Wake-on-LAN* feature (to allow the machine to wake up remotely via a magic packet):

```bash
ethtool -s enp0s3 wol p
```

In this example, the `p` option specifies that wake-up will occur as soon as a *Wake-on-LAN* packet is detected. This setup is often used in enterprise environments to perform overnight updates or remote maintenance.

#### Tool installation

It is important to note that `ethtool` is not always installed by default. On Red Hat/CentOS distributions, it can be installed with the command:

```bash
yum install -y ethtool
```

On Debian and Ubuntu, the equivalent command is:

```bash
sudo apt install ethtool
```

**WARNING**: in all `ethtool` commands, the name of the network interface must be specified immediately after the option (as `-s`). Any syntax error in the placement of parameters will make the command invalid or ineffective.


## Network layer tools

<chapterId>d2c5bf35-4284-4af8-8e8b-049c696a511b</chapterId>

### Traffic analysis tools

In network diagnostics, the `ping` command remains one of the simplest yet most powerful tools for testing connectivity between two machines. It checks whether a remote host is reachable at a given time, while also providing information on latency, link stability, and DNS resolution.

The `ping` command relies on the ICMP (*Internet Control Message Protocol*) protocol. When a user sends a `ping` request, the system sends an ICMP "Echo Request" packet to an IP address or hostname. If the target machine is online and the network path is valid, it responds with an ICMP "Echo Reply" packet. This simple mechanism can be used to measure latency and detect connectivity or name resolution problems.

Example of a classic command:

```bash
ping 172.17.18.19
```

Typical response:

```bash
mydmn.org (172.17.18.19): 56 data bytes
64 bytes from 172.17.18.19: icmp_seq=0 ttl=56 time=7.7 ms
64 bytes from 172.17.18.19: icmp_seq=1 ttl=56 time=6.0 ms
64 bytes from 172.17.18.19: icmp_seq=2 ttl=56 time=5.5 ms
```

In this example, name resolution has been performed automatically: the domain `mydmn.org` is associated with the IP address `172.17.18.19`, confirming that DNS resolution works correctly. The command also provides technical details such as:
- iCMP sequence number (`icmp_seq`), useful for checking the order of responses;
- TTL (*Time-To-Live*), which indicates the number of remaining hops before the packet is discarded;
- round-trip time/delay (`time`), expressed in milliseconds, providing an estimate of link latency.

#### More detailed analysis of ICMP parameters

The TTL is a critical field in the IP protocol. Each datagram is initialized with a TTL value by the sender (often 64, 128 or 255). Every router along the path decrements this value by 1. If the TTL reaches 0 before reaching its destination, the packet is discarded and an ICMP error is returned to the sender. This mechanism prevents infinite routing loops.

The propagation time (*round-trip delay/time*) measures the delay for a packet to leave the sender, reach the target, and return. In practice, a delay below 200 ms is considered acceptable for a stable link. Abnormally high delays may indicate network congestion, inefficient routing, or poor link quality.

#### Advanced `ping` usage

`ping` provides options to refine tests and observe specific network behaviors.

To send broadcast requests, you can use the `-b` option to target all hosts on a subnet:
```bash
ping -b 192.168.1.255
```

This is useful on local networks to quickly detect active hosts or test how the network handles broadcast requests. However, in many setups, routers and firewalls block broadcast pings to prevent amplification attacks.

You can also specify a custom interval between requests with the `-i` option (default: 1 second):

```bash
ping -i 0.2 -c 10 192.168.1.7
```

This sends 10 ICMP requests at 0.2-second intervals. Such testing is useful for detecting latency fluctuations over a short period or for lightly stressing a link to evaluate its stability.

### Routing table analysis tools

The `ip route` command, part of the `iproute2` suite, is the recommended and standard tool on modern Linux systems for inspecting and managing the kernel's IP routing table. It replaces the obsolete `route` command, offering clearer syntax, greater consistency, and extended support for modern features (IPv6, multiple tables, namespaces, etc.).

#### Displaying the routing table

To display the current routing table:

```bash
ip route show
```

This output lists all routes known to the kernel, that is, the paths outgoing packets take depending on their destination.

Example output:

```bash
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```

Each line represents a route. Key fields include:
- **default**: the default route, used when no more specific route matches.
- **via**: the gateway used to reach the destination.
- **dev**: the network interface used.
- **proto**: how the route was created (manual, DHCP, kernel, etc.).
- **metric**: route cost, used to prioritize multiple possible paths.
- **scope**: route scope (e.g. `link` for a directly connected route).
- **src**: the source IP address used for outgoing packets on this interface.

#### Adding and deleting routes

You can also modify the routing table dynamically, for example by adding or removing static routes.

Adding a static route:

```bash
ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```

This configures a route to the `192.168.1.0/24` network, via the `192.168.1.1` gateway on interface `eth0`.

Remove this route:

```bash
ip route del 192.168.1.0/24
```

This command deletes the previously defined route.

#### Useful commands

Here are some useful variants for analysis or scripting:
- `ip -4 route`: displays IPv4 routes only;
- `ip -6 route`: displays IPv6 routes only;
- `ip route list table main`: displays the main routing table (default value) ;
- `ip route get <Address>`: show which interface and gateway a packet to the given address would use.

Example:

```bash
ip route get 8.8.8.8
```

This displays the exact route a packet would take to reach `8.8.8.8`.

### Tracing tools

One of the most effective tools for analyzing the route taken by IP packets between a source host and a target destination is the `traceroute` command. It shows, step by step, the path followed by packets and identifies the intermediate routers they traverse. In the event of a network link malfunction or service outage, `traceroute` helps pinpoint the precise location of the problem.

As with the `ping` command, the target can be specified either by its fully qualified domain name (FQDN) or by its IP address. For example:

```bash
traceroute mydmn.org
```

#### Operating principle

`traceroute` relies on the TTL (*Time To Live*) field in the IP packets header. As explained earlier, this field is a counter decremented by each router along the path. When the TTL reaches zero, the packet is discarded, and the router returns an ICMP "Time Exceeded" message to the sender. This mechanism prevents infinite loops in the event of misrouting.

`traceroute` takes advantage of this behavior to map the routers between sender and recipient:
- It first sends a series of UDP packets (usually three), with a TTL of 1. The first router encounters a TTL of 0 so it discards the packet and then replies with an ICMP message, revealing its IP address and response time.
- Next, it sends another series of packets with a TTL of 2, revealing the second router.
- The process repeats until the destination is reached, at which point the host responds with an ICMP Port Unreachable message, indicating that the endpoint has been reached.

By default, `traceroute` uses UDP packets sent to unused ports (typically starting at 33434), but can also be configured to use ICMP (like `ping`) or even TCP, depending on systems or command variants.

Example output:

```bash
traceroute to www.google.fr (216.58.210.35), 64 hops max, 52 byte packets

1  par81-024.ff.avast.com (62.210.189.205)   25.107 ms  24.235 ms  24.383 ms
2  62-210-189-1.rev.poneytelecom.eu (62.210.189.1)  27.341 ms  27.119 ms  28.184 ms
3  a9k1-45x-s43-1.dc3.poneytelecom.eu (195.154.1.92)  25.910 ms  25.040 ms  25.558 ms
4  72.14.218.182 (72.14.218.182)  36.234 ms  39.907 ms  38.130 ms
5  108.170.244.177 (108.170.244.177)  25.880 ms
108.170.244.240 (108.170.244.240)  25.791 ms
108.170.244.177 (108.170.244.177)  26.449 ms
6  216.239.62.143 (216.239.62.143)  26.491 ms
216.239.43.157 (216.239.43.157)  26.414 ms
216.239.62.139 (216.239.62.139)  26.400 ms
...
9  108.170.246.161 (108.170.246.161)  33.174 ms
108.170.246.129 (108.170.246.129)  34.342 ms
108.170.246.161 (108.170.246.161)  33.707 ms
10  108.170.232.105 (108.170.232.105)  33.845 ms  33.846 ms
108.170.232.103 (108.170.232.103)  34.206 ms
11  lhr25s11-in-f35.1e100.net (216.58.210.35)  34.094 ms  33.353 ms  33.718 ms
```

Each line corresponds to a router traversed, with up to three time measurements (in milliseconds) indicating the latency of the round trip to that router. These values help assess the performance of each network segment.

#### Result interpretation

If a router doesn't respond or filters ICMP messages, asterisks `*` are displayed instead of the response time. This may indicate:
- a firewall blocking ICMP replies,
- a device configured not to respond, or
- a temporary connectivity issue along the path.

Thus, `traceroute` not only identifies the route taken but also highlights points of abnormal latency or interruptions.

On some systems, the equivalent `tracepath` command can be used, which does not require root privileges. For IPv6, use `traceroute6` or `tracepath6`.

Example for IPv6 tracing:

```bash
traceroute6 ipv6.google.com
```

### Tools for checking active connections

To diagnose active network connections and monitor network activity on a Linux system, the `ss` command (short for _socket statistics_) is the modern reference tool. Part of the `iproute2` suite, it replaces the now-obsolete `netstat`, offering better performance and more accurate results.

`ss` displays active TCP and UDP connections, listening ports, local and remote addresses, connection states and associated processes.

#### General use

When run without options, the `ss` command displays active TCP connections. Basic syntax:

```bash
ss [options]
```

Some common options for refining analysis:
- `-t`: show TCP connections only;
- `-u`: show UDP connections only;
- `-l`: show listening sockets only;
- `-n`: disable name resolution (raw IPs and port numbers) ;
- `-p`: display each socket associated processes (PID and program name),
- `-a`: show all connections, including inactive ones,
- `-s`: display high-level socket statistics.

#### Case studies

To display all active connections using TCP port 80 (HTTP):

```bash
ss -ant | grep ':80'
```

This shows active TCP connections involving port 80. States such as `LISTEN`, `ESTABLISHED`, `TIME-WAIT` indicate the current status of each exchange.

Example output:
```
ESTAB 0 0 192.168.1.10:54321  93.184.216.34:80
```

To display all network connections with associated processes:

```bash
ss -tulnp
```

To obtain an overall socket usage summary:
```bash
ss -s
```

To filter UDP connections only:
```bash
ss -unp
```

These commands are particularly useful for detecting suspicious connections, unexpected listening ports, or monitoring the activity of a specific service.

## Transport and top layer tools

<chapterId>bce47931-930e-4288-b0fd-666c9a1066b5</chapterId>

### DNS query tools

In the upper layers of the TCP/IP model, especially at the Application layer, it's important to understand how name resolution works. DNS query tools let you check whether a domain name is correctly associated with an IP address, and also help diagnose DNS server issues such as misconfiguration, propagation delays, or unavailability. These tools are essential for any network administrator or any user wanting a deeper understanding of DNS exchanges in an IP environment.

#### The `nslookup` command

The simplest DNS query tool is `nslookup`. It sends a query to a DNS server and returns the IP address associated with a domain name (or vice versa). By default, it queries the system's configured DNS server, but you can also specify a server directly in the command.

Example of a direct lookup:
```bash
nslookup mydmn.org
```

Querying a specific DNS server:
```bash
nslookup mydmn.org 192.6.23.4
```

The request asks the DNS server at `192.6.23.4` to resolve the name `mydmn.org`. This is particularly useful to check if a given DNS server recognizes a domain name or to verify that the server is working properly.

#### The `dig` command

`dig` (*Domain Information Groper*) is a more modern, complete, and flexible tool than `nslookup`. It supports complex queries and provides detailed information about the resolution process, the hierarchy of servers involved, the type of record returned (A, AAAA, MX, TXT, etc.), and any errors encountered.

Basic query example:
```bash
dig mydmn.org
```

Querying a specific DNS server:
```bash
dig @192.6.23.4 mydmn.org
```

This command checks the availability of a DNS record on a given server. 
One of `dig`'s key advantages is that it shows the details of the DNS response, making it very useful for diagnosing configuration errors.

#### Manual configuration of DNS resolvers

Sometimes its necessary to override the DNS servers used locally, for example, in test environments or to force the use of specific servers. This can be done by editing the `/etc/resolv.conf` file, which defines the system's DNS resolution settings.

Example configuration:

```bash
vi /etc/resolv.conf

search mydmn.org
nameserver 192.168.1.10
nameserver 192.168.1.11
```

- The `search` field specifies a domain to append automatically when resolving short names.
- The `nameserver` entries define the DNS servers to use, in order of priority.

On many modern distributions (especially those using `systemd-resolved`), changes to `/etc/resolv.conf` are temporary and may be overwritten at reboot or network reconnection. More permanent methods include using `resolvconf`, `systemd-resolved`, or modifying *NetworkManager* configurations.

#### The `host` command

Another simple but effective DNS tool is `host`. It resolves domain names into IP addresses (or the reverse) and can help diagnose DNS failures or misconfigurations on a network interface.

Examples:
```bash
host mydmn.org
```

Reverse lookup:
```bash
host 192.6.23.4
```

`host` is particularly handy for quick checks, especially when used in command-line scripts.

Repeated or intensive queries to third-party DNS servers without permission may be interpreted as intrusion attempts or malicious activity. Used improperly, or against networks you don't control, these commands can resemble reconnaissance scans, which are often a first step in an attack. Always restrict their use to environments you administer or where you have explicit authorization.

### Network Scanning Tools

When monitoring or securing a local or wide area network, it's crucial to identify active devices and the services they expose. This is exactly what the `nmap` (*Network Mapper*) tool does.

https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

#### Introducing `nmap`

`nmap` allows targeted scanning of one or more hosts to detect open ports, available services (HTTP, SSH, DNS, etc.), and sometimes even the type of operating system in use. Thanks to its many options, `nmap` provides a precise overview of a network's exposure surface, essential during auditing or hardening phases of infrastructure management.

Just like the `host` command, `nmap` must never be used on networks or infrastructures you don’t own, or without explicit authorization. Unauthorized port scans can be flagged as malicious reconnaissance attempts, are often detected by security systems (firewalls, IDS/IPS), and can even lead to legal consequences.

#### Basic use

To scan a specific host and view its open ports:
```bash
nmap 192.168.0.1
```

This command scan the 1000 most common ports on host `192.168.0.1` and display the services accessed and protocols used. If DNS resolution is configured, you can also use the hostname instead of the IP address.

#### Complete network scan

One of `nmap`'s advantages is its ability to scan an entire range of addresses with a single command. This makes it easy, for example, to quickly inventory all active machines on a network:

```bash
nmap 192.168.0.0/24
```

In this case, all hosts in the range `192.168.0.0` to `192.168.0.255` will be queried. For each IP address, the results list the open ports, their status (open, filtered, etc.), and, when possible, the name of the corresponding service.


![Image](assets/fr/055.webp)


An administrator can rely on `nmap` for several tasks:
- **Detecting active hosts**: identify which machines respond within a subnet;
- **Service inventory**: ensure only the necessary ports are accessible (principle of least privilege);
- **Compliance check**: compare open ports against the organization's security policy;
- **Vulnerability prevention**: spot insecure or outdated services running on critical machines.

https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

### Process interrogation tools

For in-depth analysis of active processes and open files, especially in a networking context, Linux administrators often turn to the `lsof` (*List Open Files*) command. Despite its name, `lsof` is not limited to traditional files: on UNIX systems, everything is considered a file, including network sockets, devices, and communication channels.

This tool therefore provides a cross-sectional view of the system by correlating active processes, open network ports, accessed files, and the users involved.

#### Network analysis with `lsof`

The `-i` option restricts the output to network connections (TCP, UDP, IPv4, or IPv6). This makes it easy to see which processes are communicating over the network:

```bash
lsof -i
```

This command lists all running processes using a network socket, showing the port in use, protocol (TCP/UDP), connection state, as well as the PID and associated user.

#### Filtering by IP address or port

You can refine searches by specifying an IP address and a port, isolating a particular network flow. For example, to check an SMTP session (port 25) with a specific host:

```bash
lsof -n -i @192.168.2.1:25
```

This will display only active network connections with host `192.168.2.1` on port 25, useful for diagnosing suspicious activity or SMTP flow issues.

#### Device access tracking

Another strength of `lsof` is tracking special files such as disk partitions. For instance, to check which processes have opened files on `/dev/sda1`:

```bash
lsof /dev/sda1
```

This is handy when an unmount attempt fails because the device is still in use, or when investigating which applications are accessing a partition.

#### Cross-analysis: process and network

Options can be combined for precise insights. For example, to see all network ports opened by a process with PID 1521:

```bash
lsof -i -a -p 1521
```

The `-a` option intersects criteria (`-i` and `-p`), restricting the output to only network connections of that process.

#### Multi-user tracking

`lsof` can also be used to analyze activity by specific users, listing all the files they've opened, optionally filtered by PID:

```bash
lsof -p 1521 -u 500,phil
```

This shows the files or network connections used by user `phil` or UID 500, limited to process 1521.

### Section Summary

In this final section, we've explored a wide range of indispensable tools for diagnosing, analyzing, and administering computer networks. Structured around the layers of the TCP/IP model, this study not only clarifies how network communications work but also establishes a rigorous methodology for identifying, isolating, and resolving potential issues.

These tools give administrators a coherent set of technical levers to monitor network health, analyze traffic, audit connections and quickly intervene on faulty equipment or services.

#### Network Access Layer

Tools providing direct visibility into interfaces and frames:
- **arp / ip neigh**: inspect and modify the ARP/NDP cache to check or correct IP-MAC associations;
- **tcpdump**: command-line packet capture, filterable and exportable;
- **Wireshark**: graphical packet analysis with deep protocol decoding;
- **ethtool**: query and adjust Ethernet card physical parameters (speed, duplex, WoL, etc.).

#### Network layer

Tools for assessing IP connectivity, routing, and packet traffic:
- **ping**: test reachability and measure latency with ICMP;
- **ip route**: inspect and modify the routing table to control packet paths;
- **traceroute**: hop-by-hop identification of routers along the route to a destination;
- **ss**: detailed inventory of TCP/UDP sockets and associated processes (successor to netstat).

#### Transport and Application layers

Tools for diagnosing services and processes:
- **nslookup / dig / host**: DNS queries to validate name resolution and analyze records;
- **nmap**: explore open ports and exposed services to assess attack surface;
- **lsof**: list files and sockets opened by processes, correlating system and network activity.

Mastering these tools, each aligned with a specific stage of the TCP/IP model, enables a methodical approach: starting from the physical layer, moving through routing, and up to application services. This chain of expertise equips administrators to diagnose, secure and optimize their infrastructure, ensuring both network performance and availability.

# Final part

<partId>09d5393c-63bc-42fc-bf79-c65e380211bd</partId>

## Reviews & Ratings

<chapterId>114c33c0-9831-4d74-affd-f5d37adc53c3</chapterId>

<isCourseReview>true</isCourseReview>

## Final examination

<chapterId>b99e005e-8dd0-4fa4-b302-f940c27a30ac</chapterId>

<isCourseExam>true</isCourseExam>

## Conclusion

<chapterId>3b449814-78f3-41c0-8138-0a04f3682719</chapterId>

<isCourseConclusion>true</isCourseConclusion>
