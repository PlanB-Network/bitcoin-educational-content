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

NET 302 is aimed above all at students, Linux users or simply the curious who want to understand the basics of networking and strengthen their autonomy in managing, troubleshooting and optimizing infrastructures.

Join us and turn your knowledge into real operational expertise!

___

This NET 302 course is an adapted of  *Les bases du réseau : TCP/IP, IPv4 et IPv6*, written by Philippe Pierre in French and published on [IT-Connect](https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/), under Creative Commons Attribution - ShareAlike 4.0 International ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)).


Substantial changes have been made to the original version by Loïc Morel: the text has been entirely rewritten, expanded and enriched to provide updated, in-depth content, while preserving the educational spirit of Philippe Pierre's original work. The diagrams have also been revised.

+++


# Introduction

<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>


## Course overview

<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>

This course provides a complete introduction to the fundamentals of IP networks. It is structured into four main sections, each covering an essential aspect for understanding, configuring and diagnosing a computer network.

### TCP/IP protocol

In this first part, we'll lay the groundwork by exploring the concept of networking and the history of the TCP/IP protocol. We'll study its main components: IP, TCP, along with a brief look at the IPv5 QoS protocol. We'll also cover service primitives to better understand the logic of data exchange.

### IPv4 addressing

We will then move on to a module dedicated to IPv4 addressing. You'll learn how IPv4 is used in practice, its different address types (private, public, broadcast, etc.), the fundamental role of DNS, as well as how Ethernet addresses and the ARP protocol work. You will also discover NAT (Network Address Translation) and the basics of network configuration.

### IPv6 addressing

The third part focuses on IPv6 addressing, which is necessary to address the limitations of IPv4. We'll go through its standards and definitions, address assignment within a local network, address block management and the relationship between IPv6 and DNS.

### Network diagnostic tools

Finally, we'll conclude with a presentation of the main network diagnostics tools. These will enable you to analyze, control and troubleshout malfunctions. This part will be structured by layers: Network Access, Network, Transport and Upper layers.

By the end of this course, you'll have the fundamental knowledge to efficiently administer a network infrastructure and diagnose potential issues.

Ready to dive into the world of computer networks? Let's go !

**NOTE**: The descriptions are based on a GNU/Linux CentOS 7 system. However, network configurations are largely the same between a Debian and a CentOS system. So, we won't make any distinction. When there is one, we'll prefix it with a specific logo.

**N.B.**: If you come across any unfamiliar terms during the course, please consult [the glossary](https://planb.network/resources/glossary) for definitions.


# TCP/IP protocols

<partId>53fd4b73-cdf1-4865-ba29-1ac8ec3e9e9a</partId>


## What is a network?

<chapterId>7370904f-f8f5-4ad4-a63a-5931d94c3b3b</chapterId>


In this first module, we'll take an in-depth look at the TCP/IP protocol, the cornerstone of modern digital communications. We will discuss its origins, its fundamental principles, and the addressing system it uses, which is essential for ensuring the flow of information between connected devices.

We'll also detail the main components that structure this model, and explain how they interact to form an operational, reliable and scalable network. But first, it's essential to go back to the concept of a network.

Etymologically, a network refers to a set of points connected to one another, forming an interconnected structure. In telecommunications and computing, this definition translates into a group of devices (computers, routers, switches, access points, etc.) capable of exchanging data via physical or wireless media. A network thus enables the continuous or intermittent flow of information, depending on requirements, the protocols in use and the nature of the deployed architecture.

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

The tree network, or hierarchical topology, , is modeled after the structure of a family tree. It consists of successive levels: a root node at the top connects to several lower-level nodes, which may themselves connect to other nodes, and so on.

This hierarchical layout works particularly well for large networks that need a clear division of responsibilities and segmented management. However, it also makes the network vulnerable to the failure of higher-level nodes : losing the root or a main branch can cut off entire sections of the infrastructure.


![Image](assets/fr/002.webp)


### Bus network

In a bus topology, all devices share the same transmission medium, typically a coaxial line or optical fiber. Each unit is passively connected, meaning it doesn't actively modify the signal, and it can send or receive data over this shared channel.

The bus topology's main advantage is low installation cost, thanks to simplified cabling.  However, in older coaxial-based implementations (Ethernet 10BASE2/10BASE5), disconnecting or losing a single station could disrupt or even halt all traffic, as the bus's electrical continuity and termination impedance would no longer be maintained. Having a single physical medium is also a critical weakness : any break or fault stops communication for the entire network.


![Image](assets/fr/003.webp)


### Star network

The star topology, also known as "hub and spoke", is the most common today, especially in home and office Ethernet networks. Here, all devices connect to a single central device.

This layout makes management and maintenance easy: if one peripheral device fails, the rest of the network remains unaffected. The downside is that the central device is a single point of failure, if it goes down, communication stops everywhere. Cable quality and link lengths must also be carefully considered to maintain good performance.


![Image](assets/fr/004.webp)


**Note**: there are still networks organized in a linear, bus-like topology, where equipment is connected one after the other. This solution, although inexpensive to deploy, has the major drawback that a single break isolates some of the hosts, splitting the network into independent subsets.

### Mesh network

The mesh network is designed for maximum redundancy: every device is directly connected to every other device. This ensures service continuity even if multiple links or devices fail, as traffic can be rerouted along alternative paths.

The trade-off is that the number of connections to be established increases rapidly with the number of terminals. For `N` connection points, `N × (N-1) / 2` separate links are required, making this topology expensive and complex to deploy. It's therefore used mainly in critical networks requiring very high availability, such as certain parts of the Internet or sensitive industrial systems.


![Image](assets/fr/005.webp)


Other variations exist, such as grid or hypercube networks, which are designed for specialized needs in distributed computing or parallel processing.

On a global scale, the Internet is a massive interconnection of networks using diverse topologies, unified by common addressing (IPv4 and IPv6) and a collection of standardized protocols defined by the IETF (*Internet Engineering Task Force*). This diversity means the Internet follows no single topology : its structure is flexible, scalable and independent of the logical addressing scheme that makes it usable.


## The origins of TCP/IP

<chapterId>266b6864-8789-48d7-bc85-001cb9f1651f</chapterId>


The origins of the TCP protocol lie with **ARPA** (*Advanced Research Projects Agency*, renamed "DARPA" in 1972), which launched the **ARPANET** project in 1966. The first ARPANET segment went live in October 1969, interconnecting UCLA and Stanford universities. The aim was to link research centers through a packet-switched network that could keep communications running even in the event of partial infrastructure failure.

As part of this dynamic, ARPA financed the University of Berkeley to integrate the first TCP/IP protocols into its BSD Unix system. This played a major role in spreading and standardizing the protocol, first in the academic world, and later in industry.

**Note**: at that time, computer scientists didn't yet have Linux (which wouldn't appear until the early 1990s), nor Minix, the educational system designed by Andrew Tanenbaum.  The main options were Unix, or sometimes proprietary mainframes like OpenVMS. Thanks to its flexibility and openness, Unix was instrumental in spreading the first networking concepts.

Strictly speaking, TCP/IP is not a single protocol but a suite of protocols built around TCP and IP. It rose to prominence because it provided a standardized programming interface for exchanging data between machines on the same network. This interface, based on primitives called "sockets", made it possible to create reliable and flexible connections while integrating essential application protocols.

ARPANET is therefore the historical foundation of today's Internet. Indeed, the Internet is a global network based on the principle of packet switching, where information circulates using a set of standardized protocols that ensure compatibility and interoperability between heterogeneous systems. This open architecture has enabled the development and deployment of countless services and applications, including:
- emails,
- the World Wide Web (www),
- file transfer and sharing...

The governance and evolution of these protocols are overseen by the ***Internet Architecture Board*** (IAB). 
This organization coordinates technical directions through two main structures:
- IRTF** (_Internet Research Task Force_), which conducts long-term research on protocol evolution and improvement.
- IETF** (_Internet Engineering Task Force_), which develops, standardizes, and documents the operational protocols used on the Internet

The distribution of network resources (IP address ranges, autonomous system numbers, root domain names, etc.) is coordinated internationally by **IANA/ICANN**. Operational management relies on : **RIR** (*Regional Internet Registries*): **RIPE NCC** (Europe, Middle East, Central Asia), **ARIN**, **APNIC**, **LACNIC** and **AFRINIC**.

All TCP/IP protocol specifications are recorded in documents called **RFC** (_Request For Comments_), which serve as authoritative technical references. RFCs are continually updated and numbered to reflect the ongoing evolution of the protocol suite.

The TCP/IP stack is often represented as a stack of four functional layers,  often compared to the seven-layer **OSI** (_Open Systems Interconnection_) model developed by the **ISO** (_International Standards Organization_), which serves as a conceptual reference for networking.

The four layers of the TCP/IP model are:
- the NETWORK ACCESS layer, which provides the physical link and media access control protocols;
- the INTERNET layer, which handles routing and IP addressing;
- the TRANSPORT layer, which guarantees the reliability and management of data flows using protocols such as TCP or UDP ;
- the APPLICATION layer, which groups together user and software protocols such as HTTP, FTP, SMTP and DNS.


![Image](assets/fr/006.webp)


Today, the most widely used version of IP is IPv4, but its 32-bit address space has clear limitations. This led to the creation of IPv6, which uses 128-bit addressing and offers virtually unlimited capacity : essential for supporting the explosive growth of connected devices and meeting the challenges of the Internet of Things, mobility, and security.

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

**Note: the management and assignment of IP protocol versions is handled by **IANA**. A 4-bit field allows for 16 binary combinations (values 0 to 15). Their current assignment are:


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

**Reminder**: A protocol is a set of communication rules : data structures, algorithms, packet formats, and conventions that allow different devices to exchange information reliably and understandably. A service is the concrete implementation of a protocol through specific programs (clients, servers) that follow these rules and make the functionality available to users and applications.

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

On the Internet, data doesn't flow as one continuous stream, it's sent as as **datagrams** : independent blocks of data, each encapsulated with all the information needed for delivery. This is the principle of **packet switching**, where information is split into self-contained units that may take different paths to reach the same recipient.

In addition to the payload (*payload*), each IP datagram contains a structured header with fields such as  the destination address, source address, type of service, protocol version number and other control information needed to manage the transmission.

The theoretical maximum size of an IP datagram is **65,536 octets**, a limit set by the total length field in the header. In practice, this size is rarely reached, as the physical networks carrying the packets (Ethernet, Wi-Fi, fiber optics...) usually impose a stricter limits known as **MTU** (_Maximum Transmission Unit_). If a datagram exceeds the MTU of the physical link, it must be split into smaller packets, each sent separately and reassembled on arrival.

This adaptability makes IP a robust and flexible protocol, able to operate over a wide variety of underlying technologies while maintaining universal compatibility between heterogeneous systems and networks.


### Fragmentation of IP datagrams

When an IP datagram needs to pass through a network whose transmission capacity is smaller than the datagram itself, it must be **fragmented** so it can travel without issue. This physical size limit is called the **MTU** (Maximum Transmission Unit) : the largest frame size that can pass over a given network without being split.

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
- **_netid_** : identifies the network the host belongs to
- **_hostid_** : identifies the specific host within that network
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
- 0 : identifies the network itself
- 255 : is the **broadcast** address, used to send a packet to all hosts in the network at once.
That leaves 254 usable addresses for devices.

The number of available addresses varies widely between classes : from large public networks in class A, to corporate networks in class B, to smaller local networks in class C.


![Image](assets/fr/013.webp)


Some address ranges are reserved for private use and never routed directly on the Internet. These are known as **private addresses**, and are used inside organizations, businesses, or homes, and require address translation, typically NAT (*Network Address Translation*), to reach the public Internet. These are:
- **Class A**: from 10.0.0.0 to 10.255.255.255
- **Class B**: from 172.16.0.0 to 172.31.255.255
- **Class C**: from 192.168.0.0 to 192.168.255.255

When a device with a private address accesses the Internet, a NAT-enabled router or gateway replaces it with a valid public address.

Example: If a host has the address **192.168.7.5**, we can deduce:
- 192.168.7.0 : network address
- 192.168.7.1 : often the local router
- 192.168.7.5 : the host itself

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

A CIDR block is written in the format address/prefix, where the number after the slash indicates how many bits make up the network portion. For example, /17 means that the first 17 bits identify the network, while the remaining 15 bits identify hosts.

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


**NOTE**: Historically, RFC 950 discouraged the use of subnet zero, mainly to avoid confusion in routing.  This restriction became obsolete with RFC 1878, which fully allows its use. The old limitation was mostly due to older hardware that could not handle CIDR correctly. Modern equipment has no such problem.

For example, the subnet **1.0.0.0** with the mask **255.255.0.0** once ambiguous with the class A network identifier, is now perfectly valid and usable.

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


To improve reliability, TCP uses a timer: once a segment is sent, a countdown starts. f an acknowledgement does not arrive within the timeout period, the sender automatically retransmits the segment, assuming it was lost in transit. This automatic retransmission mechanism offsets the losses inherent to IP networks, which can occur in cases of congestion, routing errors, or hardware failures.


![Image](assets/fr/019.webp)


TCP is able to detect and handle duplicates. If a retransmitted segment arrives but the original also shows up, the receiver uses the sequence numbers to identify the duplicate and keep only the correct copy, eliminating any ambiguity.

For this process to work, both machines must share a common understanding of their initial sequence numbers. This is ensured by following a strict connection procedure: on the one hand, the **server** listens on a specific port, waiting for an incoming request (passive mode); on the other, the **client** actively initiates the connection by sending a request to the server on the same service port.

**NOTE**: A "port" is a numerical identifier (from 0 to 65,535) assigned to a network application on a computer. It is used to differentiate multiple services running simultaneously on the same IP address. When a client sends data, it specifies the port number so the server's operating system knows which program  should receive it (e.g. 80 for HTTP, 443 for HTTPS, 25 for SMTP). Ports act like dedicated doors, directing traffic in and out, preventing confusion between services, and allowing fine-grained access control through firewalls or filtering rules.

The sequence synchronization exchange is based on the famous **"*three-way handshake*"** mechanism, similar to the way two people greet each other to establish contact. This initialization phase, which ensures TCP's reliability, takes place in 3 stages:
1. **SYN:** The client sends an initial synchronization segment (**SYN**) with the appropriate flag set and an initial sequence number (e.g., C);
2. **SYN-ACK:** The receiving server responds with an acknowledgement segment (**SYN-ACK**), it acknowledges the client's sequence number and provides its own initial sequence number,
3. **ACK:** The client sends a final acknowledgement (**ACK**) confirming receipt of the server's sequence number, finalizing synchronization. The SYN flag is now disabled and the ACK flag remains set indicating that the connection is established.


![Image](assets/fr/020.webp)


This exchange protocol ensures that both parties share the same numbering base before transmitting payload data. Once this synchronization is complete, the session is opened: segments can now travel in both directions, each acknowledged upon receipt, ensuring maximum reliability of the data flow.

This ***three-way handshake*** only concerns connection establishment. For closing, TCP uses a *four-way handshake*: FIN → ACK → FIN → ACK, which guarantees that no segment in transit is lost before the connection is completely released.

Although designed for robustness and reliability, this process has also given rise to exploitable vulnerabilities. For example, attacks such as **IP Spoofing** aim to bypass or corrupt this trust relationship by impersonating an authorized machine through falsified sequence numbers, creating a breach that allows interception or manipulation of the data stream.

To limit the risks of sequence synchronization hijacking and to manage network load, the TCP protocol uses a flow management technique known as "**_Sliding Window_**". This system regulates how much data can be sent without requiring an immediate acknowledgement for each segment, thus reducing unnecessary overload on the network while maintaining good reliability.

In practical terms, the sliding window defines a range of sequence numbers that can circulate freely between sender and receiver without each individual segment beeing acknowledged. As acknowledgements are received by the sending system, the window "slides": it slides to the right making room for new segments to be sent. The size of this window (critical for optimizing throughput while avoiding congestion) is specified in the "*Window*" field of the TCP header.

**Example**: if the initial sequence number is 3 and the window extends to sequence 5,segments numbered 3 to 5 can be sent without waiting for individual acknowledgements.


![Image](assets/fr/021.webp)


The size of the sliding window is not fixed; it adjusts dynamically to network conditions and the receiver's processing capacity.  If the receiver can handle a greater volume of data, it indicates this through the Window field, prompting the sender to expand its window. Conversely, in case of overload or risk of saturation, the receiver can request a reduction, the sender will wait until the window moves forward to send additional segments.

The protocol provides a symmetrical procedure for closing a TCP connection to ensure a clean, orderly shutdown. Either machine can initiate closure by sending a segment with the **FIN** flag set to 1, signalling its intent to end the communication. It then waits until all in-transit segments have been received and ignores any further data.

Upon receiving this segment, the other machine sends an acknowledgement, also marked with the FIN flag. It then finishes sending any remaining data before informing the local application that the coonection has been closed. This double confirmation ensures an orderly shutdown and minimizes the risk of data loss.

This precise management,combining IP's flexible routing with TCP's strict control, is often illustrated by a diagram contrasting the speed of the IP protocol (which works on a **"best effort "** basis, with no guarantee of delivery) against the reliability of the TCP protocol (which manages transmission through acknowledgements and negotiated sequences).


![Image](assets/fr/022.webp)


In some cases, however, absolute reliability is not the priority : speed and simplicity are. This is true for applications like live streaming or VoIP, which can tolerate some packet loss without seriously affecting user experience. In such cases, **UDP** (_User Datagram Protocol_) is preferred.

UDP operates on a fundamentally different principle from TCP: it is **connectionless**, meaning no prior relationship is established between sender and receiver. When a machine sends packets via UDP, they are transmitted one way; the receiver does not send acknowledgements, and the sender has no confirmation that the message arrived. The UDP header is intentionally minimal, containing only the source port, destination port, segment length, and a checksum, with no built-in acknowledgment or state-control mechanism. As always, IP addresses are carried by the underlying IP header.

A common analogy is that TCP is like a **phone call**, where a circuit is established, followed and controlled throughout the conversation. While, the UDP protocol is like **posting a mail**, where the sender slips a letter into a mailbox with no immediate proof of delivery or systematic feedback.

This complementarity between TCP and UDP enables modern networks to adapt to a variety of needs, choosing maximum reliability or prioritizing speed, depending on the application.


## Service primitives

<chapterId>4480afb7-e950-4ccb-88fa-d132f9dc3479</chapterId>


### Layered architecture and exchange organization

As we've seen, **services** are the concrete implementation of the protocols we've described  so far. While the TCP/IP model differs from the **OSI** model, it adopts the same layered approach: each layer is designed to perform a specific function and to provide **services** to the layer directly above it, resulting in a modular, robust, and easily maintainable architecture.

Each layer builds on the capabilities of the one below it, and in turn provides the layer above with a consistent Interface for managing data. In this architecture, every layer has its own **data structures**, carefully defined to ensure perfect compatibility with the other layers. This compatibility is essential for smooth, reliable, and clear communication from one endpoint to another.

Two key aspects govern these exchanges:
- **Vertical aspect** : the relationship between one layer and the one above or below it (from layer N to layer N+1, and vice versa).


![Image](assets/fr/023.webp)


- **Horizontal aspect** : the interaction between remote applications, i.e., the dialogue between a **client** and a **server**, in either direction.


![Image](assets/fr/024.webp)


The layered architecture follows the principle that each layer processes only the information within its scope: data structures, headers and control mechanisms vary from one layer to another, but together they forms a coherent system, ensuring data is gradually routed to its final destination.

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
- **domain name** registered in a **DNS** (_Domain Name System_) :Associates a numeric IP address with a human-friendly name.
- **MAC address**: physical identifier engraved in the network card, used for local transport (_Ethernet_). When an IP packet needs to be physically transmitted, the ARP table matches the IP address with the MAC address of the destination.

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

In the next chapter, we'll explore another fundamental concept:  **Ethernet addresses**, also known as **MAC addresses**, which ensure data delivery at the physical layer of local networks.


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
Interface : 192.168.1.5 --- 0x5
IP Address            MAC Address                Type
192.168.1.5           00:54:BC:17:14:6E          D
```

It's important to remember that the MAC address and the IP address are two completely different identifiers, yet closely complementary. The MAC address is uniquely engraved into each network interface by the manufacturer and is used to physically identify the device on the local network. The IP address, on the other hand, is a logical address assigned either dynamically or statically, allowing the machine to join the IP network and exchange packets beyond its local network.

- Visual example of MAC address :

![Image](assets/fr/032.webp)


- Visual example of an IP address :

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

Network Address Translation_ (NAT) is a technique that was developed to compensate for the gradual depletion of the IPv4 address pool. Conceived as an intermediary mechanism before IPv6 became widespread, NAT enabled companies and individuals to continue connecting a large number of machines while using a limited number of public IP addresses.

**Important reminder:** the transition from IPv4 to IPv6 theoretically solves this exhaustion problem, since the address space is increased from 32 bits to 128 bits, offering an almost unlimited number of addresses (2^128). In practice, however, the transition remains partial, and NAT is still very widespread.

The NAT principle is based on a simple but particularly effective operation: instead of assigning a unique public IP address to each machine on the internal network, a single routable address (or a small pool of addresses) is used for all private terminals. The NAT gateway, often integrated into the router or firewall, then dynamically translates the internal IP address and the information needed to route traffic correctly to the outside world, and returns the replies to the sending machine.

The immediate advantage of this procedure is that it completely masks the network's internal architecture. To an outside observer, all requests from workstations, servers or printers share the same public identity. Private addressing, generally consisting of IP addresses from reserved ranges (e.g. 192.168.x.x or 10.x.x.x), therefore remains invisible from the Internet.

In addition to responding to the shortage of IPv4 addresses, NAT strengthens security by creating a first logical barrier between the internal network and the public network. Unsolicited incoming communications are naturally filtered out, as only connections initiated from inside the network benefit from the translation required to receive responses.


![Image](assets/fr/035.webp)


### Translation types

NAT can be implemented in a variety of ways, adapted to specific needs. There are two main modes of operation: static translation and dynamic translation.

**Static translation** consists in establishing a fixed correspondence between a private IP address and a public IP address. Each internal machine then has a dedicated public address permanently associated with it. For example, an internal machine configured as 192.168.20.1 can be associated with the routable address 157.54.130.1. When an outgoing packet leaves the local network, the router modifies the packet's source address to substitute the public address, and performs the opposite operation for incoming traffic. This bidirectional translation is transparent to the user.

**Warning:** although this mechanism isolates the internal network, it doesn't solve the problem of a shortage of public IP addresses, because you always need as many public addresses as there are machines to expose. Static translation is therefore mainly used when certain internal resources must remain reachable from the outside (web server, mail server...).

Dynamic translation, on the other hand, provides a pool of public IP addresses. When an internal host initiates a connection, the router temporarily selects one of these addresses and associates it with the host's private address for the duration of the session. The link is 1-to-1, but temporary: as soon as the flow is interrupted, the public address becomes available again for another station. Dynamic NAT therefore saves on the number of public addresses when not all machines need to be connected at the same time, but it still requires a block of external addresses at least equal in size to the maximum number of simultaneous connections.

Port translation (PAT), also known as *NAT overload* or *IP masquerading*, goes one step further: all private machines share a single public IP address (or a very small number). To differentiate between sessions, the gateway modifies not only the source address, but also the source port. It then maintains a table associating each *(private address, private port)* pair with a unique *(public address, public port)* pair. This form of NAT is used in almost all home boxes and routers, enabling dozens of terminals (computers, smartphones, connected objects, etc.) to share the same public IP address, while maintaining fluid communication.

NAT therefore extends IPv4's lifespan, while adding an appreciable level of partitioning and security. However, with the gradual adoption of IPv6 and its immense address space, the role of NAT will tend to diminish, even if, for reasons of compatibility and control, it will still be used in certain environments to segment and filter flows.


### NAT implementation

To guarantee the correct operation of the address translation mechanism, the NAT router or gateway must keep a precise record of the correspondences established between each private address on the internal network and the public address it uses to communicate with the outside world. This information is stored in a table known as the "NAT translation table", which plays a central role in network flow management.

Each entry in this table associates at least one pair, consisting of the internal IP address of the sending machine and the external IP address that will be exposed on the Internet. When a packet from the private network is sent to a public destination, the NAT router intercepts the frame, analyzes the IP and TCP/UDP headers, then replaces the private source address with the gateway's public address. In the return direction, the incoming packet is captured by the same gateway, which checks the mapping table and performs the reverse operation to redirect the flow to the original internal IP address.

This dynamic translation principle is based on fine-tuned table management: each entry remains valid as long as active traffic justifies it. After a configurable period of inactivity, the entry is purged and can be reused for new connections.

example of a simplified NAT translation table :_


| Internal IP   | External IP    | Duration (sec) | Reusable? |
| ------------- | -------------- | -------------- | --------- |
| 10.101.10.20  | 193.48.100.174 | 1,200          | no        |
| 10.100.54.251 | 193.48.101.8   | 3,601          | yes       |
| 10.100.0.89   | 193.48.100.46  | 0              | no        |

In this example, if no packet has transited for the second line for more than an hour (3600 seconds), the entry is marked as reusable. Conversely, a duration field of zero indicates that a communication is in progress and that the correspondence is locked.

Although NAT integrates seamlessly into the majority of current applications (web browsing, e-mail, file transfer, etc.), it can introduce additional constraints for certain network applications. Some technologies rely on the explicit exchange of IP addresses or ports in the body of packets. However, this information becomes incoherent after passing through the NAT gateway.

Among the most typical cases of limitations are :
- Peer-to-peer protocols (P2P), which require the establishment of direct connections between stations, are disrupted by the NAT barrier, as each internal machine shares the same external IP address and cannot be contacted directly without specific configuration (such as *port forwarding* or UPnP);
- The IPSec protocol, used to secure network communications, encrypts packet headers. However, since NAT needs to modify these headers to replace IP addresses, encryption makes this modification impossible, compromising compatibility without adaptation mechanisms such as NAT-T (*NAT Traversal*);
- The X Window protocol, which enables remote display of graphical applications under Unix/Linux, operates according to a logic in which the X server actively sends TCP connections to clients. This reversal of the usual direction of connections can be blocked by NAT translation.

In general, any protocol that includes an explicit reference to the internal IP address in the packet payload will be affected, as this address no longer corresponds to the real address visible from the Internet once the translation has been carried out.

**Important note:** To overcome these problems, some NAT routers feature _Deep Packet Inspection_ (DPI) or _Protocol Helpers_ functions, which inspect packet contents to identify and dynamically replace addresses or port numbers in application data. However, this manipulation requires a thorough knowledge of the protocol format to be processed, and can represent a vulnerability or a resource overhead.

**A word of caution:** Although NAT helps to mask the internal network and control the flow of incoming traffic, it is no substitute for a dedicated firewall. Translation is not a complete security barrier: it must always be complemented by precise filtering rules to block unsolicited or unwanted traffic.

to illustrate how this works in practice, let's take the following example:_


![Image](assets/fr/037.webp)


In this scenario, an internal workstation can access the internal web server by calling the URL `http://192.168.1.20:80` directly. Here, port specification is optional, since `80` is the standard port for HTTP. Conversely, if a request is initiated from the outside, the user will enter the public address `http://85.152.44.14:80`. The NAT router receives the request, consults its mapping table and automatically translates the public address into a private one, redirecting the connection to `http://192.168.1.20:80`.

This principle is identical for any other server authorized to receive connections from the Internet, such as the Extranet server (blue circuit on the diagram).

**Practical note:** in virtualized environments, network interfaces called _virbrX_ (for _Virtual Bridge X_) are frequently encountered. These virtual bridges, provided in particular by the libvirt library or the Xen hypervisor, are used to connect the virtual internal network of guest machines to the physical network, while applying NAT. They are generally configured via scripts located in `/etc/sysconfig/network-scripts/`, as illustrated below for `virbr0` :

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

Once the virtual bridge is in place, you need to enable IP routing and configure port translation with `iptables` :

```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```

```shell
iptables -t nat -A POSTROUTING -o <WAN> -s 192.168.0.0/24 -j MASQUERADE
```

With this configuration, outgoing traffic is routed and NAT translation is provided, enabling virtual machines to communicate with the outside world without directly exposing their internal IP addresses.

In the following chapter, we'll take a detailed look at IP address configuration under Linux, using simple and advanced methods adapted to different administration contexts.


https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864


## How do I configure the network with `ip`?

<chapterId>8ba7e946-d2a0-4841-8d54-e85ba96baa25</chapterId>


### Standard configuration

Having established the theoretical foundations of networking and understood how IP addresses, masks, routing and translation work together, it's time to get down to the nitty-gritty. Under GNU/Linux, network configuration is now done with the **`ip`** command (_iproute2_ package), which replaces the historic `ifconfig`.

A veritable Swiss army knife, `ip` lets you assign or modify an IP address, change a mask, start or stop a Interface, or consult its status at any time.

**ASTUCE:** to view all interfaces (active or not): `ip addr show`

Example: assigning a static address and activating Interface

Add address `192.168.1.2/24` to Interface `eth0` :

```shell
ip addr add 192.168.1.2/24 dev eth0
```

Activate Interface:

```shell
ip link set dev eth0 up
```

To deactivate the same Interface :

```shell
ip link set dev eth0 down
```

To display the status of a specific Interface :

```shell
ip addr show dev eth2
```

**Practical tip:** with `ip`, adding an additional address to a Interface no longer requires a `:1` suffix. Just add a second line `ip addr add ...` :

```shell
ip addr add 172.18.2.39/24 dev eth2
```


### Activation scripts: ifup / ifdown

The `ifup` and `ifdown` utilities read static files from `/etc/sysconfig/network-scripts/` (on RHEL, CentOS, Rocky Linux, AlmaLinux...) or `/etc/network/interfaces` (on Debian/Ubuntu) to cleanly enable or disable interfaces.

```shell
ifup eth1
ifdown eth2
```

Configuration files (RHEL-like) :
- /etc/sysconfig/network**: global parameters (NETWORKING, HOSTNAME, GATEWAY...).
- ifcfg-***: parameters specific to each Interface.

Static example (ifcfg-eth0) :

```ini
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.2.5
NETMASK=255.255.255.0
GATEWAY=192.168.2.1
```

DHCP example :

```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```

This modular structure is still valid and can be easily automated on current systems.


### Advanced configuration: bonding

In professional environments, the aim is to guarantee continuity of service and/or to aggregate bandwidth. Bonding* (or *teaming* with _teamd_) mechanisms meet these needs: several physical interfaces function as a single logical Interface, often called `bond0` or `team0`.


![Image](assets/fr/039.webp)


Prerequisites :
- Load the `bonding` module (or use `teamd`) ;
- At least two physical interfaces.


#### The various common bonding methods :

|Mode|Nom|Principe|
|---|---|---|
|0|balance-rr|Round-robin, répartition circulaire des trames|
|1|active-backup|Une seule interface active, bascule à chaud|
|2|balance-xor|Sélection via XOR MAC src/dst|
|3|broadcast|Diffusion simultanée sur toutes les interfaces|
|4|802.3ad (LACP)|Agrégation dynamique normalisée, nécessite switch compatible|
|5|tlb (Transmit Load Balancing)|Répartition selon la charge d’émission|
|6|alb (Adaptive Load Balancing)|Répartition adaptative, équilibre aussi la réception via ARP|


#### Setting up with `ip link

- Disable physical interfaces :

```shell
ip link set eth0 down
ip link set eth1 down
```

- Creating the crowded Interface:

```shell
ip link add bond0 type bond mode balance-alb
```

- Configure options after creation

```shell
ip link set bond0 type bond miimon 100
```

- Assign MAC and IP addresses :

```shell
ip link set dev bond0 address 00:17:56:BC:02:3A
ip addr add 192.168.2.3/24 dev bond0
ip route add default via 192.168.2.1
```

- Attach slave interfaces :

```shell
ip link set eth0 master bond0
ip link set eth1 master bond0
```

- Put everything back into service:

```shell
ip link set bond0 up
ip link set eth0 up
ip link set eth1 up
```

**Tip:** to detach a slave without cutting the bond: `ip link set eth1 nomaster`


#### Permanent configuration (RHEL-like)

Create three files in `/etc/sysconfig/network-scripts` :

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

Then :

```shell
systemctl restart network
```


#### Additional IP address (modern alias)

With `ip`, you simply add a second address on the same device:

```shell
ip addr add 192.168.1.2/24 dev eth0
```

For this alias to survive reboot, create a second `IPADDR2=...` / `PREFIX2=...` block in `ifcfg-eth0`, or a new *NetworkManager* connection via `nmcli`.

Thanks to `ip` and related commands (`ip link`, `ip addr`, `ip route`), network configuration gains in consistency, scriptability and clarity. Bonding is a cornerstone of high-availability architectures, and Interface's ability to add multiple addresses has been greatly simplified.

In the rest of this course, we'll look at the specifics and implementation of IPv6 addressing.


# IPv6 addressing

<partId>9b1d87f1-2a68-496e-b5dd-76cf74fb8cde</partId>


## IPv6: Standards and definitions

<chapterId>d1f16f0a-1104-460d-8d67-f725665f8e3f</chapterId>


We now turn to the next generation of IP addressing: the IPv6 protocol, originally known as IPng (_IP Next Generation_). Designed to overcome the structural limitations of IPv4, this protocol introduces a vastly expanded addressing architecture, as well as numerous technical optimizations.

The reasons behind the adoption of IPv6 are manifold, and address critical needs for the evolution of the Internet. Firstly, IPv6 had to support the exponential growth in the number of connected devices (an objective unattainable with IPv4's limited address space). Secondly, the protocol aims to reduce the size of routing tables, making exchanges more efficient and lightening the workload of routers in the long term.

IPv6 also aims to simplify certain aspects of packet processing, to streamline datagram flow and optimize transfer speed between networks. From a security point of view, the AH/ESP headers of the *IPsec* protocol are part of the basic set, and all IPv6 nodes must be able to support them (RFC 6434). However, their use remains optional: the administrator decides whether or not to activate them, depending on the context.

Other objectives include more detailed consideration of service types, notably to guarantee better quality for real-time applications (VoIP, videoconferencing, etc.). IPv6 should also enable more flexible management of mobility: a device can thus change access point without changing its address in a way that is visible to its correspondents.

Finally, IPv6 has been designed to coexist with legacy protocols. While it is not directly binary-compatible with IPv4, it is perfectly interoperable with higher layers such as TCP, UDP, ICMPv6 and DNS, as well as with routing protocols such as OSPF and BGP, subject to certain adjustments. For multicast management, IPv6 uses the MLD (*Multicast Listener Discovery*) protocol, the functional equivalent of IGMP in the IPv4 environment.


### Writing rules

One of the major changes with IPv6 is the IP address format itself. To resolve the chronic shortage of IPv4 addresses, the length of the address has been increased to 128 bits, or 16 bytes, compared with only 32 bits for IPv4. In theory, this opens up a range of possible addresses from :

$$3.4 \times 10^{38}$$

This guarantees virtually unlimited capacity for all current and future equipment.

The way IPv6 addresses are written differs significantly from conventional dotted decimal notation. An IPv6 address is made up of eight 16-bit groups, expressed in hexadecimal and separated by colons `:`.

For example:

```
1987:0c02:0000:84c2:0000:0000:cf2a:9077
```

To simplify the writing, the leading zeros of each group can be omitted. The previous example then becomes :

```
1987:c02:0:84c2:0:0:cf2a:9077
```

In addition, a single continuous sequence of groups of zeros can be replaced by the notation `::`, thus condensing the address:

```
1987:c02:0:84c2::cf2a:9077
```

**Warning:** the rule is strict: a single sequence of consecutive zeros can be abbreviated by `::`. If an address contains several sequences of zeros, only the longest is condensed. This principle guarantees the uniqueness and legibility of the address.

**Important peculiarity:** the `:` character used to separate hexadecimal blocks poses a potential problem in URLs, as `:` is also used to indicate the service port. To remove any ambiguity, IPv6 addresses inserted in a URL must be enclosed in square brackets `[ ]`.

Example of HTTP access on a specific port for the address `2002:400:2A41:378::34A2:36` :

```
http://[2002:400:2A41:378::34A2:36]:8080
```

When you want to express an IPv4 address in an IPv6 context, you can use a mixed notation in dotted decimal, preceded by the string `::` :

```
::192.168.1.5
```

This compatibility facilitates the transition between the two protocols by allowing IPv4 blocks to be included in the IPv6 space.

**Note:** To standardize representations, RFC 5952 defines a canonical format that specifies the abbreviation rules to be followed to avoid multiple variants of the same address. Compliance with these recommendations helps to limit misinterpretation and ensure the consistency of network configurations.


### IPv6 address types

IPv6 addressing is distinguished from its predecessor by a wide variety of address categories, each designed to meet specific needs, while guaranteeing flexible routing and network management. As with IPv4, addresses can be global, local, reserved or specific to certain transition mechanisms.

An unspecified IPv6 address is represented by `::` or, in more explicit form, `::0.0.0.0`. This particular form is used when acquiring an address, or as a default value to indicate the absence of an address.


| IPv6 Address Prefix | Description                                 |
| ------------------- | ------------------------------------------- |
| ::/8                | Reserved addresses                          |
| 2000::/3            | Unicast addresses, routable on the Internet |
| fc00::/7            | Unique local addresses (1)                  |
| fe80::/10           | Link-local addresses                        |
| ff00::/8            | Multicast addresses                         |

(1) : *On a private LAN, the `fd00::/8` prefix is preferred for assigning internal addresses that are not routable on the Internet.*


#### Reserved addresses

Some IPv6 ranges are explicitly reserved and must not be used as global addresses. They have a well-defined technical role:
- `::/128`**: unspecified address, never persistently assigned to a device, but used as a source address by a machine awaiting configuration.
- `::1/128`**: the address of _loopback_, the direct equivalent of `127.0.0.1` in IPv4, which allows a machine to address itself.
- `64:ff9b::/96`**: block reserved for protocol translators for IPv4/IPv6 interconnection, as defined in RFC6052.
- `::ffff:0:0/96`**: compatibility block for representing an IPv4 address in a specific IPv6 structure, often used internally by applications.

These blocks guarantee interoperability and facilitate migration between the two versions of the protocol.


#### Unicast global addresses

Unicast global addresses make up the bulk of the publicly routable IPv6 space. They represent around 1/8th of the address space. Since 1999, IANA has been allocating these blocks, such as the `2001::/16` prefix, in CIDR blocks (from `/23` to `/12`) to regional registries, which then redistribute them to providers and organizations.

Some beaches have specific documented uses:
- `2001:2::/48`**: reserved for performance and interoperability tests, RFC5180.
- `2001:db8::/32`**: reserved for documentation and examples, RFC3849.
- `2002::/16`**: used for the 6to4 mechanism, which enables IPv6 traffic to be transported across an IPv4 infrastructure (important for the transition phase between the two protocols).

**Please note:** a large proportion of global addresses remain untapped, providing a reserve for future Internet extensions.


#### Unique local addresses (ULA)

Unique local addresses (`fc00::/7`) are the IPv6 equivalent of IPv4 private addresses (RFC1918). They enable the creation of isolated internal networks without the risk of conflict with public addressing. In practice, the effective prefix is `fd00::/8`, with the 8th bit set to 1 to define local usage. Each ULA block incorporates a 40-bit pseudo-random identifier, thus minimizing address collisions when interconnecting separate private networks.


#### Link-local addresses

Link-local addresses (`fe80::/64`) are used exclusively for internal communications on the same Layer 2 segment (same VLAN or switch). They are never routed beyond the local link. Each network Interface automatically generates a link-local address, often derived from its MAC address via the EUI-64 scheme.

Special feature: the same machine can use the same link-local address on several interfaces, provided that Interface is specified during communications to avoid any ambiguity.


#### Multicast addresses

In IPv6, the concept of broadcast has been replaced by multicast, a more efficient way of distributing packets to a defined group of recipients. The multicast range is prefixed by `ff00::/8`. These addresses include `ff02::1`, which targets all nodes on the local link. Although practical, this address is no longer recommended for applications, as it can generate uncontrolled broadcasts.

A frequent use of multicast is the _Neighbor Discovery Protocol_ (NDP), which replaces ARP in IPv6. NDP relies on specific multicast addresses, such as `ff02::1:ff00:0/104`, to automatically discover other hosts connected to the same link.

By combining these address types, IPv6 offers a complete palette to meet the needs of global routing, local communications, IPv4/IPv6 migration and device autoconfiguration, while improving the efficiency of network transmissions.


### Address perimeter

The scope of an IPv6 address (*scope*) precisely defines the domain in which this address is considered valid and unique. Understanding this notion is important for mastering packet routing and the logical organization of an IPv6 network. IPv6 addresses are generally grouped into three broad categories according to their scope and mode of use: unicast, anycast and multicast.

Unicast addresses** are the most common category, and include several distinct subtypes. These include the _loopback_ (`::1`) address, whose scope is strictly limited to the host using it, and which enables the network stack to be tested internally without sending traffic over the physical network. Then there are link-local addresses (_link-local_), whose scope is restricted to a single network segment: they are used for direct communications between devices located on the same physical or logical link (e.g. a single switch or VLAN). Finally, unique local addresses (_ULA_, for _Unique Local Addresses_) correspond to address ranges internal to a corporate network; they have a potentially wider scope, as they can be routed across several private segments, but are never visible on the Internet.

This conceptual breakdown often takes the form of a binary structure in which the first half of the address (the first 64 bits) identifies the network prefix, and the second half (also 64 bits) uniquely identifies the Interface of the equipment on that network. This separation facilitates address autoconfiguration through mechanisms such as SLAAC (_Stateless Address Autoconfiguration_), which allow machines to automatically generate a stable address based on the MAC address or a pseudo-random identifier.


| Field     | Prefix | L | Global ID | Subnet | Interface ID |
|-----------|--------|---|-----------|--------|---------------|
| Bits      | 7      | 1 | 40        | 16     | 64            |

The IPv6 architecture is based on the hierarchical global routing model of today's Internet: prefix partitioning enables regional registries and operators to manage address distribution in a decentralized way, while ensuring global uniqueness. It is within this framework that the same host can simultaneously possess a global unicast address, for communicating on the Internet, and a link-local address for interacting locally, e.g. for immediate neighborhood or router discovery messages.


| Field     | Prefix | Zero | Interface ID |
|-----------|--------|------|--------------|
| Bits      | 10     | 54   | 64           |

Anycast addresses** represent an intermediate concept that takes advantage of the unicast model, while offering multicast-like behavior in some cases. An anycast address is, in fact, a unicast address assigned to several interfaces distributed over different network nodes. When a packet is sent to an anycast address, the IPv6 protocol endeavors to deliver it to one of the hosts sharing this address, generally giving priority to the one closest according to the routing topology. This principle optimizes query processing speed and improves the resilience of distributed services: a typical example is that of root DNS servers, for which anycast addressing automatically directs queries to the nearest point of presence.


| Field     | Prefix | Subnet | Interface ID |
|-----------|--------|--------|--------------|
| Bits      | 48     | 16     | 64           |

Finally, in IPv6, **multicast addresses** replace the broadcast mechanism, deemed too costly and unsuitable for a global network. A multicast address identifies a group of interfaces, usually spread over several hosts, that wish to receive the same packets simultaneously. For each multicast address, the range is specified by a special field: the 4 _scope_ bits included in the address structure. These bits define the geographic or logical broadcast limit:
- A scope of `1` means that the packet is intended for local equipment only.
- A scope of `2` indicates a range limited to the local link: all devices on the same physical or virtual segment can receive the message.
- A scope of `5` extends the reach to the site, typically to an entire internal corporate network.
- A scope of `8` extends the reach to an organization, enabling distribution to all sub-networks of the same entity.
- Finally, a scope of `e` (14 in hexadecimal) designates a global reach, which makes the multicast group accessible from the entire Internet, provided the routing infrastructure allows it.

Each IPv6 multicast address is structured into several fields: a _Flag_ field (4 bits) specifies whether the group is permanent or transient, a _Scope_ field (4 bits) defines the scope, and an identification field (112 bits) indicates the multicast group number.


| Field      | Prefix | Flags | Scope | Group ID |
|------------|--------|--------|--------|----------|
| Bits       | 8      | 4      | 4      | 112      |

An emblematic example of IPv6 multicast is the use of the _Neighbor Discovery Protocol_ (NDP). Rather than using ARP as in IPv4, NDP relies on multicast addresses such as `ff02::1:ff00:0/104` to broadcast its neighbor discovery requests, soliciting only the hosts concerned on the same link.

The IPv6 address perimeter thus finely structures the way data flows are transmitted, received and routed. This granularity makes the protocol more flexible and efficient for managing both local and global communications, while avoiding the disadvantages of generalized broadcasting.


## Address assignment in a local network

<chapterId>4c9c3e52-59bc-499a-af0a-6dd369a9e029</chapterId>


In this chapter, we'll look at one of the most concrete aspects of IPv6 implementation: assigning IP addresses to hosts on a local network. The IPv6 architecture has been designed to offer great flexibility, allowing each machine to automatically generate its own address, while leaving open the possibility of entirely manual configuration.

An IPv6 local network is based on a systematic division of the address into two parts: the first 64 bits represent the subnet prefix, usually provided by a router or addressing authority, while the remaining 64 bits are used by the host to uniquely identify itself on that segment. This model greatly simplifies route aggregation and address block management.

Two main approaches are used to assign addresses to equipment:
- Manual configuration, in which the administrator precisely specifies the address of each Interface ;
- Automatic configuration, enabling equipment to dynamically generate or obtain its own address.

In manual configuration, the administrator sets the full IPv6 address on each Interface. Please note: some values remain reserved:
- `::/128` : unspecified address, never permanently assigned ;
- `::1/128`: loopback address (_loopback_), IPv4 equivalent: `127.0.0.1`.

On the other hand, there is no concept of _broadcast_ as in IPv4; the other "all to 0" or "all to 1" combinations in the host part have no particular role. This manual approach remains relevant in controlled environments, but it quickly becomes cumbersome to maintain on a large scale.

In automatic configuration, several methods exist to enable equipment to obtain a functional IPv6 address without manual intervention. The **NDP** (_Neighbor Discovery Protocol_) protocol, specified by RFC4862, enables *stateless* auto-configuration. In this mode, the host receives a network prefix from a local router, and completes the address itself with an identifier based on its MAC address. This method is extremely simple to implement, and requires no central server.

Some implementations, such as those found in Windows systems, can use a pseudo-random draw to generate the host part of the address, which improves confidentiality compared with direct use of the MAC address. Indeed, the visibility of the MAC address in IPv6 packets raises privacy issues, as it enables a device to be tracked in different network contexts.

Another widely-used method is the use of the DHCPv6 protocol, specified in RFC3315. Similar to the DHCP used for IPv4, it enables more controlled, centralized configuration, with lease management, additional options (DNS, MTU...), and registration in databases. DHCPv6 can be used alone or in conjunction with stateless configuration to provide additional parameters without necessarily assigning the IP address itself.

**Important note:** when using the MAC address-based method, the MAC address is transformed into a 64-bit identifier by the EUI-64 mechanism. This mechanism inserts the bytes `FF:FE` in the center of the original MAC address (in 48 bits), and inverts the 7th bit to mark global uniqueness. The result is a stable Interface identifier, used in the full IPv6 address.

Here's an example of how to transform a MAC address into EUI-64:


![Image](assets/fr/045.webp)


However, due to growing concerns around device tracking, modern operating systems (notably Linux, Windows 10+, macOS, Android) offer "privacy extension" mechanisms by default, which use random Interface identifiers that are periodically renewed for outgoing connections, while retaining a stable identifier for internal communications (DNS, DHCPv6...).

As with DHCP in IPv4, automatically assigned IPv6 addresses can be associated with two lifetimes defined by DHCPv6 routers or servers:
- Preferred lifetime*: after this period, the address remains valid, but is no longer used to initiate new connections;
- Valid lifetime*: when this time expires, the address is completely removed from the Interface configuration.

This logic makes it possible to dynamically manage network evolution, ensuring, for example, a smooth transition from an old ISP to a new one. By updating the prefix announced by routers and adjusting DNS records in parallel, IPv6 migration can be carried out with no discernible service interruption.

**Tip:** The combined use of address and DNS lifecycles makes it possible to implement a gradual transition strategy, where new connections move to a new topology, while old ones end their lifecycle seamlessly.

In short, IPv6 offers a wide range of flexibility for address assignment: manual configuration, auto-configuration with or without state, DHCPv6, or random generation. Each approach has its own advantages and constraints, and can be adapted to suit the level of control required, the size of the network, or confidentiality requirements.


## Assigning IPv6 address blocks

<chapterId>45cce866-1b58-4888-b3fe-15c922180839</chapterId>


### Address distribution

The IPv6 address allocation scheme has been structured to meet two objectives: to guarantee global address uniqueness, and to enable a logical hierarchy that favors the aggregation and simplification of routing tables. As with IPv4, the *Internet Assigned Numbers Authority* (IANA) remains at the top of this hierarchy. It manages the global unicast address space and delegates address blocks to the five regional Internet registries (_RIR_).

The five existing RIRs are :
- ARIN (North America),
- RIPE NCC (Europe, Middle East, Central Asia),
- APNIC (Asia-Pacific),
- AFRINIC (Africa),
- LACNIC (Latin America and the Caribbean).

IANA allocates IPv6 blocks of variable size to each RIR, generally between /23 and /12. These sizes allow great flexibility while ensuring long-term scalability. Once these blocks have been received, the RIRs are responsible for redistributing them to Internet Service Providers (ISPs), large corporations or public institutions.

IANA allocates each RIR an IPv6 /12 block. This unique size, fixed since 2006, ensures that each regional registry has a stable and sufficiently large reserve for its long-term needs. Once this /12 has been received, the RIR typically subdivides it into /23, /26 or /29. ISPs are most often allocated /32 blocks, although this size can vary depending on the ISP's size and geographical area. In turn, they can allocate each of their customers a /48 block, giving each organization 65,536 distinct /64 subnets (which is extremely generous compared to IPv4).

**Important note:** a /32 block contains exactly 65,536 /48 sub-blocks. This means that every ISP can serve tens of thousands of customers without running out of addresses. Thanks to its /48, each customer will then have a gigantic amount of space to structure its own internal network with as many /64 segments as it wishes.

This hierarchy can be seen in the following table, which illustrates the typical block sizes allocated to each level:

| IANA | RIR | LIR | Customer | Subnet | Interface |
|------|-----|-----|----------|--------|-----------|
|  3   | 20  |  9  |    16    |   16   |     64    |

With this abundance of addresses, NAT (*Network Address Translation*), which has become virtually indispensable in IPv4 to compensate for the shortage of public addresses, is no longer necessary. Every host connected to the Internet can have a unique, global public address, simplifying end-to-end connectivity and facilitating the use of protocols such as IPSec, VoIP or inbound connections.

To check to which organization an IPv6 address has been assigned, you can use the `whois` command, which queries public RIR databases. This transparency makes it possible to identify the organization that owns a prefix, which can be useful for network, analysis or security purposes.


### PA vs PI addressing

Originally, the IPv6 allocation model was based solely on the use of PA (*Provider Aggregatable*) blocks, i.e. linked to the ISP. In this model, the client organization receives its prefix from the ISP, which means that if it changes provider, it will have to renumber its entire infrastructure.

This mechanism is facilitated by IPv6's auto-configuration capabilities and address lifetime management, but it remains restrictive for companies with critical infrastructures or redundancy requirements with multiple providers.

This is why, from 2009 onwards, allocation policies have been extended to allow the existence of PI (*Provider Independent*) blocks. These blocks (generally /48 in size) are allocated directly to a company or institution by an RIR, independently of any ISP. This model is particularly well suited to organizations practicing *multihoming*, i.e. connected to several operators simultaneously. Document RIPE-512 details the European policy for allocating these PI blocks, for example.


### Notation of subnet masks

As in IPv4, IPv6 subnet notation uses CIDR (*Classless Inter-Domain Routing*). This consists of indicating the number of bits making up the prefix after the address, using the `/` character.

Take the following example:

```
2001:db8:1:1a0::/59
```

This means that the first 59 bits are fixed and identify the network. All remaining bits (here 69 bits) can be varied to identify subnets or hosts.

Thus, this notation covers addresses from `2001:db8:1:1a0:0:0:0:0` to `2001:db8:1:1bf:ffff:ffff:ffff:ffff`.

This block therefore covers a set of 8 /64 subnets, each capable of hosting a very large number of hosts.

The flexibility offered by this notation enables fine-tuned address space planning, whether in large infrastructures, home networks or virtualized environments. It also favors route aggregation, reducing the load on routers and facilitating large-scale deployment.


### IPv6 packets and headers

The format of an IPv6 packet differs from its IPv4 predecessor in its apparent simplicity and great extensibility. An IPv6 datagram always begins with a fixed-size header of 40 bytes, which contains the information essential for routing the packet. This is a much more streamlined choice than the IPv4 header (which could vary from 20 to 60 bytes), enabling routers to process packets faster and more efficiently.

However, IPv6 does not sacrifice functionality: instead of integrating numerous optional fields in the main header, it introduces a system of extension headers, placed immediately after the basic header. These optional headers make it possible to add data or instructions specific to certain functions, without unnecessarily burdening the processing of ordinary packets.

Some of these headers follow a rigid format, but others are designed to contain a variable number of options. In these cases, each option is encoded according to a triplet `{Type, Length, Value}` :
- The "Type" field (1 byte) indicates the nature of the option;
- The first two bits of the "Type" specify what routers should do if the option is not recognized:
 - Ignore the option and continue treatment,
 - Delete the datagram,
 - Delete the datagram and return an ICMP error message to the source,
 - Delete datagram without notification (in the case of multicast packets).
- The "Length" field (1 byte) specifies the size of the "Value" field, from 0 to 255 bytes;
- The "Value" field contains the data associated with the option.

Here's an overview of the different types of extension headers defined by IPv6.


#### Hop-by-Hop header

This header, if present, is always placed immediately after the base header. It contains information intended to be read by each router traversed, which distinguishes it from other headers generally processed only by the destination. It is typically used to signal global parameters or trigger specific processing along the route.


![Image](assets/fr/047.webp)


#### Routing header

The routing header is used to specify a list of intermediate addresses through which the packet must pass. There are two main approaches:
- Strict routing: the exact path is determined in advance;
- Loose routing: only certain mandatory steps are specified.

The first four fields of this header are :
- Next Header** : identifies the type of the next header;
- Routing Type**: defines the routing method (usually `0`);
- Left** segments: number of segments remaining to be covered ;
- Address[n]**: list of intermediate addresses.

The "Segments Left" field is initialized to the total number of segments remaining, and is decremented by one for each jump.


![Image](assets/fr/048.webp)


#### Fragmentation header

Unlike IPv4, where routers could fragment packets, only the source host is allowed to fragment an IPv6 datagram. All IPv6 nodes must be able to transmit packets of at least 1280 bytes. If a router encounters a packet larger than the MTU of the next link, it sends an *ICMPv6 Packet Too Big* message back to the source, which then adjusts the size of its transmissions.

The fragmentation header contains the following fields:
- Identification**: datagram identifier for reconstruction.
- Fragment Offset**: fragment position in the original datagram.
- M flag**: indicates whether any other fragments remain.


![Image](assets/fr/049.webp)


#### Authentication header (AH)

This header is designed to secure communications by guaranteeing the authenticity of the sender and the integrity of the data. It is used in particular with the IPsec protocol. Thanks to a verification code (authenticator), the recipient can be sure that the message actually comes from the expected sender, and that it has not been altered en route.

In the event of a fraudulent modification attempt, the authentication code will no longer match, and the datagram may be rejected. This mechanism also combats replay attacks, by detecting unauthorized duplications.


![Image](assets/fr/050.webp)


#### Header Destination option

This header is intended only for the final recipient of the datagram. It can be used to add options or metadata specific to the application, without being taken into account by intermediate routers.

Initially, no such option was defined in the protocol. However, this header was introduced when IPv6 was designed, to allow future extensions to be added without modifying the overall packet structure. The null option, for example, is only used to complete the header up to a multiple of 8 bytes, for memory alignment reasons.


![Image](assets/fr/051.webp)


IPv6 packet design is therefore based on a clear separation between a minimalist base header and optional extension headers, introduced in a modular fashion. This architecture guarantees both standard processing performance and the flexibility needed to evolve the protocol and integrate security, complex routing or quality-of-service mechanisms, while maintaining compatibility with future infrastructures.


## Relationship between IPv6 and DNS

<chapterId>421eacb8-b80b-4aee-910f-e069ed805f00</chapterId>


In modern networks, the DNS (*Domain Name System*) translates domain names into IP addresses that can be used by machines. With the introduction of IPv6, DNS naturally had to adapt to support the new 128-bit addresses, while maintaining compatibility with IPv4. This coexistence is important in dual-stack environments, where both versions of the IP protocol coexist.


### IPv6-specific DNS records

To associate a domain name with an IPv6 address, DNS uses a type AAAA (*quad-A*) record, by analogy with the type "A" used for IPv4 addresses. The AAAA record indicates that a domain name corresponds to a given IPv6 address. Here's a concrete example:

```shell
ipv6.mydmn.org.         IN      AAAA    2001:66c:2a8:22::c100:68b
```

This record indicates that the domain `ipv6.mydmn.org` is associated with the IPv6 address `2001:66c:2a8:22::c100:68b`. It is perfectly possible, and even recommended in the context of compatibility, to associate the same domain name with several IP addresses, whether IPv4 (via an A record) or IPv6 (via an AAAA record). This allows IPv6-compatible customers to prefer the latter version of the protocol, while ensuring that IPv4-only customers can continue to use it.

DNS also supports reverse resolution, i.e. the mapping of an IP address to a domain name. In the case of IPv6, this operation uses PTR records placed in the `ip6.arpa` zone. This zone is specifically reserved for IPv6 reverse resolution, as is the `in-addr.arpa` zone for IPv4.


### Reverse resolution

The reverse resolution of an IPv6 address follows a strict rule: we transform the address into full hexadecimal notation (16 bytes, i.e. 32 characters), reverse the order of each hexadecimal digit, and separate them with periods, suffixing the whole with `ip6.arpa`. For example, for the following address

```shell
2001:66c:2a8:22::c100:68b
```

It is first extended to 32 hexadecimal digits:

```shell
2001:066c:02a8:0022:0000:0000:c100:068b
```

We then invert each nibble and separate them with dots, ending with `ip6.arpa` :

```shell
b.8.6.0.0.0.1.c.0.0.0.0.0.0.0.0.2.2.0.0.8.a.2.0.c.6.6.0.1.0.0.2.ip6.arpa  IN PTR  ipv6.mydmn.org
```

This method guarantees the uniqueness and standardization of reverse resolutions in the IPv6 address space.

**Please note**: DNS queries can be sent over either an IPv4 or IPv6 connection. The transport protocol used has no influence on the type of response expected. In other words, an IPv6-connected client can request an IPv4 address, and vice versa. The DNS server must therefore provide the available information, without relying on the protocol used by the client for the request.

The choice between an IPv4 or IPv6 address to be used to connect to a target machine, when a host name is associated with both address types, is governed by RFC 6724. This standard defines an address selection algorithm based on criteria such as proximity, range, or explicit preference of certain prefixes. By default, IPv6 generally takes precedence over IPv4, unless otherwise configured by the system or network administrator.

**Important reminder**: when an IPv6 address is to be used in a URL (*Uniform Resource Locator*), it must be enclosed in square brackets (`[]`). This avoids any confusion between the colon (`:`) used to separate the segments of the IPv6 address and those used in the URL to separate the host name from the service port.

Valid example:

```shell
http://[2001:db8::1]:8080
```

This ensures that the URL is processed correctly by both browsers and web servers.

Integrating IPv6 into the DNS system therefore relies on new record types, a strict method for reverse resolution, and precise selection and formatting rules to ensure routing compatibility and consistency.


### Part summary

In this section, we explore in detail the fundamental principles governing IPv6 addressing. We began by explaining how an IPv6 address is structured, focusing on its 128-bit length, its hexadecimal notation, and the various writing simplification rules used to shorten certain repetitive sequences of zeros. This structure enables IPv6 to overcome the limitations of IPv4's address space, while guaranteeing efficient scalability and prioritization.

We then looked at the different categories of IPv6 addresses: unicast, anycast and multicast, detailing for each their scope, typical use and representation in the address space.

We then looked at ways of assigning IPv6 addresses in a local network, whether by manual configuration, via the DHCPv6 protocol, or using stateless autoconfiguration mechanisms such as those offered by NDP. These approaches enable devices to automatically generate their own address from the received prefix and their MAC address (via EUI-64), while ensuring flexibility in terms of lifetime management and confidentiality.

We've also detailed how address blocks are allocated, starting with IANA, which distributes them to the five RIRs (*Registered Internet Regions*), then to the ISPs, which redistribute them to their customers in the form of subnetworks (often in /48, allowing 65536 /64 subnetworks). The distinction between _Provider Aggregatable_ (PA) and _Provider Independent_ (PI) blocks makes it possible to handle _multihoming_ or change of provider situations.

We've seen that DNS adapts to IPv6 thanks to the AAAA record, and that reverse resolution mechanisms use a new structure in the `ip6.arpa` zone. The DNS protocol remains independent of the transport protocol used (IPv4 or IPv6), ensuring perfect interoperability in a dual-stack environment.

IPv6 is not simply an evolution of its predecessor, but a thorough overhaul of the addressing system, designed to meet the current and future challenges of the global network.

In the final part of this NET 302 course, we'll get down to the nitty-gritty of network diagnostics.


# Network diagnostic tools

<partId>368a5c6f-ec48-4b28-970f-3a770788ad37</partId>


## Network Access Layer tools

<chapterId>1d25a21d-6900-4fbe-a438-e06c8afb9e02</chapterId>


In this first chapter of the final section on network diagnostics, we'll focus on tools for analyzing the network access layer of the TCP/IP model. This layer is responsible for direct communication between devices connected to the same physical network, notably through the use of MAC addresses and physical network interfaces such as Ethernet cards or Wi-Fi interfaces.

The aim here is to provide administrators with the practical means to inspect, test and optimize this essential layer of low-level connectivity. These tools can be used to evaluate the correct operation of interfaces, diagnose problems linked to network card configuration, or identify anomalies such as collisions, packet loss or link errors.


### IP/MAC neighborhood utilities

#### Arp` tool

One of the historical tools for network diagnostics at the Network Access layer is the `arp` command. Although it is tending to be replaced by more modern commands such as `ip neigh` (which we'll discover shortly), `arp` is still present on many systems to consult or manipulate the ARP (*Address Resolution Protocol*) cache. This cache contains matches between IP addresses and MAC addresses known locally on a machine. In other words, it can be used to identify which physical address (MAC address) corresponds to a given IP address when communicating on a local network.

In concrete terms, when a host wishes to send a packet to an IP address belonging to the same subnet, it must first know the MAC address of the target machine. This association is made using the ARP protocol, which transmits a request on the local network and receives a response containing the MAC address of the corresponding machine. This information is then temporarily stored in a local table called the "ARP cache", to avoid repeated requests each time a packet is sent.

To consult this cache and observe the entries currently known by the machine, the following command can be used:

```bash
arp -a
```

This command lists all locally registered IP/MAC matches, across all interfaces. Each line provides the host name (if resolvable), the IP address, the corresponding MAC address and the Interface on which the match is observed.

If you wish to filter the display by focusing on a specific IP address, you can specify this address in the :

```bash
arp -a 192.168.1.5
```

This allows you to check whether a particular IP address is well known to the cache, which can help diagnose a communication failure between two hosts on the same network.

Similarly, to display only the ARP entries associated with a given Interface network (such as an Ethernet card named `eth0`), we can write :

```bash
arp -a -i eth0
```

This option is useful for targeting special cases, particularly in multi-card environments where one machine has several network interfaces (wired, wireless, VPN...).

The `arp` utility is not limited to consultation. It also lets you manually manipulate the ARP cache, which can prove invaluable in certain cases of advanced diagnosis or simulation of specific situations. For example, you can manually add an IP/MAC association:

```bash
arp -s 192.168.1.7 00:17:BC:56:4F:25 -i eth2
```

This command creates a static entry in the local ARP table, associating the IP address `192.168.1.7` with the MAC address `00:17:BC:56:4F:25` on the Interface `eth2`. If the Interface is not specified, the first Interface deemed applicable is used by default.

Finally, it is also possible to delete an entry from the ARP cache, if it is incorrect or if you wish to force a rediscovery:

```bash
arp -d 192.168.1.7
```

This command deletes the corresponding entry, forcing the machine to issue a new ARP request the next time it attempts to communicate with this IP address.

**NOTE**: The delete option also accepts a Interface name, if you wish to precisely target the entry to be deleted on a specific Interface.

In summary, the `arp` tool provides low-level diagnostics, particularly useful in local networks where connectivity problems can often be traced back to incorrect or obsolete address resolution. However, it should be noted that on recent systems, particularly with modern Linux distributions, this tool is increasingly being replaced by the `ip neigh` command, from the `iproute2` toolset, which offers similar functionality in a more unified framework.


#### Ip neigh` tool

On modern systems, notably recent Linux distributions, the `ip neigh` command is the benchmark tool for inspecting and managing mappings between IP and MAC addresses. This command is part of the `iproute2` suite, which is gradually replacing older tools such as `arp`, offering a more coherent and flexible Interface for network diagnostics at the data link layer.

The `ip neigh` command consults the local IP neighbor cache, which plays a role equivalent to the ARP cache for IPv4 and the NDP (_Neighbor Discovery Protocol_) cache for IPv6. This cache contains known associations between IP addresses (v4 or v6) and MAC addresses, as well as their status (valid, pending, expired...).

The basic command for displaying cache contents is :

```bash
ip neigh
```

It produces a list of known entries, in a synthetic form indicating the destination IP address, the Interface network concerned, the corresponding MAC address (if available), and the status of the entry (e.g. `REACHABLE`, `STALE`, `DELAY`, `FAILED`...).

Sample output:

```bash
192.168.1.5 dev eth0 lladdr 00:17:BC:56:4F:25 REACHABLE
```

This line indicates that the machine knows of a valid correspondence between IP address `192.168.1.5` and MAC address `00:17:BC:56:4F:25` via Interface `eth0`.

It is also possible to filter cache entries according to specific criteria, such as an IP address, a Interface, or a particular state. For example, to query only the address `192.168.1.7` :

```bash
ip neigh show 192.168.1.7
```

Or to display the entries associated with Interface `eth1` :

```bash
ip neigh show dev eth1
```

In addition to consultation, the `ip neigh` command also allows you to modify the cache manually. For example, to add a static entry :

```bash
ip neigh add 192.168.1.7 lladdr 00:17:BC:56:4F:25 dev eth1 nud permanent
```

This command permanently associates the IP address `192.168.1.7` with the MAC address indicated, on the Interface `eth1`. The keyword `nud permanent` (for _Neighbor Unreachability Detection_) specifies that the entry will not be invalidated automatically.

Conversely, to delete a cache entry :

```bash
ip neigh del 192.168.1.7 dev eth1
```

This forces the system to perform a new neighborhood resolution the next time a packet is sent to this address.

**NOTE**: The `ip neigh` tool works for both IPv4 and IPv6. It interacts with ARP in the former case, and with NDP in the latter, using a unified and consistent Interface for both protocol families. `ip neigh` therefore offers a modern, centralized approach to managing IP/MAC relationships on a host.


### Package analysis tools

To analyze in detail what is passing through a computer network, it is important to have tools capable of capturing packets exchanged between machines. Two utilities stand out as benchmarks for network administrators and analysts: `tcpdump` and `Wireshark`. These tools can be used to diagnose abnormal behavior, audit protocol exchanges, or study network security by inspecting the contents of frames.


#### ttcpdump`: command-line analysis

`tcpdump` is an extremely powerful command-line tool designed to capture and display packets circulating on a Interface network. It works in real time, and thanks to its light weight, it can be used on systems without graphics Interface or with limited resources. It is based on the `libpcap` library, which provides hardware-independent low-level capture functions.

A typical use of `tcpdump` is to monitor the network activity of a machine or network segment, filtering packets according to precise criteria. By redirecting the results to a file, it becomes possible to keep a trace of the traffic for later analysis or for replay in another tool, such as Wireshark.

Here is the general syntax of the command:

```bash
tcpdump -w <file.cap> -i <interface> -s <snapshot_length> -n <filters>
```

- `-w` writes captured packets to a file in `libpcap` format (extension `.cap` or `.pcap`);
- `-i` designates the Interface network to be monitored (e.g. `eth0`, `wlan0`);
- `-s` defines the maximum capture size for each packet. Specifying `0` captures all packets;
- `-n` prevents DNS resolution or conversion of IP addresses and ports to symbolic names, which speeds up performance.

Expression filters, located at the end of the command, allow you to capture only a specific subset of the traffic. You can combine the keywords `host`, `port`, `src`, `dst`, etc., to refine the selection.

Example: to capture HTTP packets (port 80) to or from the `192.168.25.24` server, and save them in a `fichier.cap` file:

```bash
tcpdump -w fichier.cap -i eth0 -s 0 -n port 80 and host 192.168.25.24
```

This capture can then be reused in a graphics tool or for playback on another system.


#### Wireshark: advanced visual analysis

Wireshark, formerly known as *Ethereal*, is a full-featured network analysis software with a graphical Interface. Unlike `tcpdump`, it allows detailed, structured visualization of packets, with protocol decomposition, flow graphs, traffic statistics and interactive filters. It is also based on `libpcap`, which enables it to open and exploit files captured by `tcpdump`.

Wireshark is available on many operating systems, including Linux and Windows. Installation requires administrator rights to access the capture Interface. Once launched, you can choose a network Interface from the *Capture* menu. Click on *Start* to start recording packets in real time. Packets are displayed in three sections:
- the list of frames ;
- details decoded by protocol ;
- hexadecimal raw data.


![Image](assets/fr/052.webp)


Wireshark excels in scenarios where you need to observe complex protocol behavior, reconstruct application dialogs (such as an HTTP or DNS session), or study service response times. It is also possible to apply very precise display filters using its dedicated syntax (different from that of `tcpdump`), in order to visualize only relevant packets.


#### Complementary tools

It's important to note that `tcpdump` and Wireshark are not interchangeable: each is specialized for a particular use. `tcpdump` is suited to command-line environments, automated analysis scripts and remote server interventions. Wireshark, on the other hand, is ideal for detailed, interactive and educational analysis of network traffic.

The two tools can be combined: a capture is made on a remote system with `tcpdump`, then the `.cap` file is transferred for analysis with Wireshark on a local machine. This approach is widely used.


### Interface analysis tools

At the Network Access layer, it's important to be able to query and configure physical network interfaces in order to diagnose malfunctions, optimize performance or check connection integrity. For this purpose, one of the most powerful tools available under Linux is `ethtool`, a command-line utility that not only provides detailed technical information about a Interface Ethernet, but also allows you to modify some of its parameters in real time.


#### View Interface specifications

One of the basic features of `ethtool` is its ability to query a Interface to display its current characteristics. In this way, you can find out :
- link speed (e.g. 100 Mbit/s, 1 Gbit/s or 10 Gbit/s) ;
- negotiation mode (half duplex or full duplex) ;
- whether or not autonegotiation is enabled;
- the type of port used (copper, fiber, etc.) ;
- link status (active or not) ;
- support for advanced features such as *Wake-on-LAN*.

This information is important for diagnosing problems linked to physical connectivity or misalignment of negotiations between the host's network card and the equipment to which it is connected (switch, router...).

To obtain this information, simply use the following command:

```bash
ethtool enp0s3
```

This command returns a complete set of data on the Interface `enp0s3`, often found in CentOS or RHEL-based distributions.


![Image](assets/fr/053.webp)


#### Dynamically modify Interface parameters

the `ethtool` is not limited to observation: it also allows you to act directly on certain Interface parameters without rebooting the machine. This allows you, for example, to force the link speed or activate specific options according to the needs of the local network.

The `-s` option is used to dynamically configure parameters such as :
- speed (`speed`) to be set explicitly (e.g. 1000 for 1 Gbit/s) ;
- the type of duplex (`duplex`) to choose between `half` or `full` ;
- activation or deactivation of auto-negotiation (`autoneg`) ;
- activation of *Wake-on-LAN* (`wol`) ;
- or the type of port.

Example 1: Activate autonegotiation on Interface :

```bash
ethtool -s enp0s3 autoneg on
```

Example 2: enable the *Wake-on-LAN* feature (to allow the machine to wake up remotely via a magic packet) :

```bash
ethtool -s enp0s3 wol p
```

In this example, the `p` option means that wake-up will occur as soon as a *Wake-on-LAN* packet is detected. This configuration is often used in professional environments for night-time updates or remote maintenance.


#### Tool installation

It is important to note that `ethtool` is not systematically installed by default. On Red Hat/CentOS distributions, it can be installed with the command :

```bash
yum install -y ethtool
```

On Debian and Ubuntu, the equivalent command is :

```bash
sudo apt install ethtool
```

**WARNING**: in all `ethtool` commands, the name of the Interface network must always be specified immediately after the option (as `-s`). Any syntax error in the position of the parameters will render the command invalid or ineffective.


## Network layer tools

<chapterId>d2c5bf35-4284-4af8-8e8b-049c696a511b</chapterId>


### Traffic analysis tools

In the field of network diagnostics, the `ping` command remains one of the simplest yet most powerful tools for checking connectivity between two machines. It establishes whether a remote host is reachable at a given time, while providing information on network latency, link stability and DNS name resolution.

The `ping` command is based on the ICMP (*Internet Control Message Protocol*) protocol. When a user sends a `ping` request, the system sends an ICMP "Echo Request" packet to an IP address or host name. If the target machine is online and the network path is valid, it responds with an ICMP "Echo Reply" packet. This simple mechanism can be used to measure latency and identify connectivity or name resolution problems.

Example of a classic order:

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

In this example, we can see that name resolution has been performed automatically. The domain name `mydmn.org` is associated with the IP address `172.17.18.19`, indicating that DNS resolution is working correctly. The command also provides technical data such as :
- iCMP sequence number (`icmp_seq`), useful for checking the order of arrival of responses;
- the TTL (*Time-To-Live*), which corresponds to the number of network hops remaining before the packet is destroyed;
- response time or round-trip time/delay (`time`), expressed in milliseconds, which gives an indication of link latency.


#### More detailed analysis of ICMP parameters

The TTL is a critical parameter in the IP protocol. Every datagram sent has a TTL field, initialized by the sender (often 64, 128 or 255). At each router crossed, this field is decremented by 1. If the TTL reaches 0 before reaching its destination, the packet is destroyed and an ICMP error is returned to the sender. This mechanism prevents infinite network loops.

Propagation time (*round-trip delay/time*) measures the total delay for a packet to leave the transmitter, reach the target and return. In practice, a delay of less than 200 milliseconds is considered satisfactory for a stable link. An abnormally long delay can be a symptom of network congestion, inefficient routing or poor link quality.


#### Advanced `ping` usage

The `ping` tool can be used with different options to refine tests and better observe certain network behaviors.

To send broadcast requests, you can use the `-b` option, which sends a request to all hosts on a subnet:

```bash
ping -b 192.168.1.255
```

This command is useful in local networks for quickly detecting active hosts or testing network behavior in the face of broadcast requests. However, beware: in many configurations, routers and firewalls block this type of request to prevent amplification attacks.

It is also possible to specify a custom send interval with the `-i` option (by default, requests are sent at one-second intervals):

```bash
ping -i 0.2 -c 10 192.168.1.7
```

Here, 10 ICMP requests are sent at 0.2-second intervals. This type of test is particularly useful for detecting latency fluctuations over a short period or for slightly stressing a link to observe its stability.


### Routing table analysis tools

The `ip route` command, from the `iproute2` suite, is the recommended and standard tool on modern Linux systems for consulting and manipulating the kernel's IP routing table. It replaces the old, obsolete `route` command, offering clearer syntax, greater consistency, and extended support for contemporary network features (IPv6, multiple tables, namespaces...).


#### Displaying the routing table

The following command displays the current state of the routing table:

```bash
ip route show
```

This result lists all the routes known to the kernel, i.e. the paths taken by outgoing IP packets according to their destination.

Typical output example:

```bash
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```

Each line represents a route. Here's an explanation of the essential fields:
- default**: default route, used if no more specific route is found.
- via**: address of the gateway used to reach the destination.
- dev** : Interface network used by packets.
- proto**: route source (manual, DHCP, kernel, etc.).
- metric**: cost of the route, used to distinguish between several possible paths.
- scope**: route scope (e.g. `link` for a directly connected route).
- src**: source IP address used on this Interface for outgoing communications.


#### Adding and deleting routes

The `ip route` tool can also be used to dynamically modify the routing table, in particular to add or remove static routes.

Adding a static route :

```bash
ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```

This configures a route to the `192.168.1.0/24` network, via the `192.168.1.1` gateway, via the Interface `eth0`.

Remove this route:

```bash
ip route del 192.168.1.0/24
```

This command deletes the previously defined route.


#### Useful commands

Here are some useful variants for analysis or scripting:
- `ip -4 route`: displays IPv4 routes only;
- `ip -6 route`: displays IPv6 routes only;
- ip route list table main` : displays the main routing table (default value) ;
- `ip route get <Address>`: determines which Interface and gateway a packet to a given address would be routed through.

Example:

```bash
ip route get 8.8.8.8
```

This returns the precise route a packet would take to address `8.8.8.8`.


### Tracing tools

One of the most effective tools for analyzing the route taken by IP packets between a source host and a target destination is the `traceroute` command. It allows you to visualize, step by step, the path taken by packets, identifying the intermediate routers crossed. In the event of a network link malfunction or service interruption, `traceroute` can be used to pinpoint the precise location of the fault.

As with the `ping` command, you can target the remote host either by its full domain name (FQDN), or by its IP address. For example:

```bash
traceroute mydmn.org
```

#### Operating principle

How `traceroute` works is based on the TTL (*Time To Live*) field present in the header of IP packets. As explained above, this field is a counter that is decremented each time a packet passes through a router. If the TTL value reaches zero, the packet is considered lost and is discarded by the router, which then returns an ICMP "Time Exceeded" message to the sender. This prevents infinite loops in the event of incorrect routing.

The `traceroute` tool exploits precisely this behavior to map the routers located between the sender and the recipient:
- It sends a first series of UDP packets (usually three), with a TTL equal to 1. The first router then encounters a zero TTL, destroys the packet and sends an ICMP response. Its IP address and response time are recorded;
- Then `traceroute` sends a new series of packets with a TTL equal to 2. The second router does the same;
- This process repeats until the packet reaches its destination, which then returns an ICMP "Port unreachable" message indicating that the host has been reached.

By default, the tool uses UDP packets sent on unused ports (typically from port 33434), but can be configured to use ICMP (like `ping`) or even TCP, depending on systems or command variants.

Here is an example of the result obtained:

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

Each line corresponds to a router traversed, with up to three time measurements (in milliseconds) indicating the latency of the round trip to that router. These times can be used to evaluate the performance of each segment of the path.


#### Interpretation of results

If a router doesn't respond or filters ICMP messages, asterisks `*` are displayed instead of the response time. This may mean :
- a firewall that blocks ICMP responses ;
- equipment configured not to respond to these messages;
- a temporary connectivity problem on the path.

The `traceroute` command not only identifies the route taken, but also pinpoints areas of abnormal latency or connection breaks.

On some systems, the command can be replaced by `tracepath`, which does not require root privileges. For IPv6 connections, use `traceroute6` or `tracepath6`.

Example for tracing an IPv6 route:

```bash
traceroute6 ipv6.google.com
```


### Tools for checking active connections

To diagnose current network connections and get an overview of network activity on a Linux system, the `ss` command (for _socket statistics_) is today's benchmark tool. Part of the `iproute2` suite, it replaces the now obsolete `netstat`, offering superior performance and greater accuracy.

`ss` displays active TCP and UDP connections, listening ports, local and remote addresses, connection status and associated processes.


#### General use

Executed without options, the `ss` command displays active TCP connections. Here's its basic syntax:

```bash
ss [options]
```

Some common options for refining analysis :
- `-t`: Displays TCP connections only;
- `-u`: Displays UDP connections only;
- `-l`: limits display to listening sockets ;
- `-n`: disables name resolution (raw display of IP addresses and port numbers) ;
- `-p`: displays the processes associated with each socket (PID and program name) ;
- `-a`: Displays all connections, including inactive ones;
- `-s`: provides high-level statistics on sockets.


#### Case studies

If you want to display all active connections using TCP port 80 (HTTP), you can use :

```bash
ss -ant | grep ':80'
```

This command displays active TCP connections involving port 80. Typical states (such as `LISTEN`, `ESTABLISHED`, `TIME-WAIT`) are used to interpret the status of current exchanges.

Sample output:

```
ESTAB 0 0 192.168.1.10:54321  93.184.216.34:80
```

To display all network connections with associated processes :

```bash
ss -tulnp
```

For an overall statistical summary of the sockets used :

```bash
ss -s
```

To filter UDP connections only :

```bash
ss -unp
```

These commands are particularly useful for spotting suspicious connections, listening for unexpected ports, or monitoring the network activity of a particular service.


## Transport and top layer tools

<chapterId>bce47931-930e-4288-b0fd-666c9a1066b5</chapterId>


### DNS query tools

In the upper layers of the TCP/IP model, and particularly at the Application layer, it's important to understand how name resolution works. DNS query tools can be used not only to check whether a domain name is correctly associated with an IP address, but also to diagnose DNS server configuration, propagation or inaccessibility problems. These tools are essential for any network administrator or user wishing to better understand DNS exchanges in an IP environment.


#### The `nslookup` command

The simplest DNS query tool is `nslookup`. It allows you to submit a query to a DNS server and obtain in return the IP address associated with a domain name (or vice versa). Used without options, it queries the DNS server configured on the system by default, but you can explicitly indicate a server to query by specifying it directly in the command.

Simple example of use with direct resolution :

```bash
nslookup mydmn.org
```

And to query a specific DNS server :

```bash
nslookup mydmn.org 192.6.23.4
```

This request asks the server at address `192.6.23.4` to resolve the name `mydmn.org`. This is a useful method when you want to check whether or not a given DNS server knows a domain name, or to verify that the server is functioning correctly.


#### The `dig` command

More modern, more complete and more flexible than `nslookup`, the `dig` (*Domain Information Groper*) command lets you perform complex DNS queries, while providing detailed information on the resolution process, the hierarchy of servers consulted, the type of record obtained (A, AAAA, MX, TXT, etc.) and any problems encountered.

Here is an example of a standard query:

```bash
dig mydmn.org
```

Or to target a specific DNS server:

```bash
dig @192.6.23.4 mydmn.org
```

This command is used to test the availability of a DNS record on a given server. One of the major advantages of `dig` is its ability to display the details of the returned DNS message, which is useful for diagnosing configuration errors.


#### Manual configuration of DNS resolvers

It is sometimes necessary to modify the DNS servers used locally, particularly in test environments or to force the use of specific servers. This can be done by editing the `/etc/resolv.conf` file, which defines the system's DNS lookup parameters.

Here is an example configuration:

```bash
vi /etc/resolv.conf

search mydmn.org
nameserver 192.168.1.10
nameserver 192.168.1.11
```

- The `search` field indicates the domain to be added automatically when resolving short names;
- The `nameserver` directives specify the IP addresses of the DNS servers to be used. The order in which they appear determines the query priority.

Note that this configuration is temporary in many modern distributions (especially with `systemd-resolved`) and may be overwritten each time you reboot or reconnect to the network. More permanent methods exist (such as using `resolvconf`, `systemd-resolved`, or modifying *NetworkManager* files).


#### The `host` command

The `host` tool is another simple but effective DNS utility. It allows you to resolve domain names to IP addresses, or vice versa, and can also be used to diagnose DNS response errors or failures on a Interface network.

Example of use:

```bash
host mydmn.org
```

Or for a reverse resolution :

```bash
host 192.6.23.4
```

It is particularly useful for spot checks, especially on the command line in automated scripts.

It's important to remember that repeatedly or intensively querying third-party DNS servers without authorization can be considered an intrusion attempt or malicious behavior. Certain commands, when misused (or used on networks that do not belong to you), can be assimilated to network reconnaissance, a first step in certain forms of attack. It is therefore important to limit the use of these tools to the environments you administer, or for which you are explicitly responsible.


### Network interrogation tools

When monitoring or securing a local or wide area network, it's important to be able to identify active equipment and the services they expose. This is precisely what the `nmap` (*Network Mapper*) tool enables.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

#### Introducing `nmap

`nmap` enables targeted interrogation of one or more hosts to detect open ports, accessible services (HTTP, SSH, DNS...) and sometimes even the type of operating system in use. Thanks to its numerous options, it is possible to obtain a precise and synthetic vision of the state of a network's exposure surface, which is essential in the auditing or hardening phases of an infrastructure.

As with the `host` command, it should never be used on a network or infrastructure that does not belong to you, or without explicit authorization. Unauthorized port scans can be considered as malicious reconnaissance attempts, and are often detected as such by security devices (firewalls, IDS/IPS), or even punished.


#### Basic use

To scan a specific host and view open ports, simply run :

```bash
nmap 192.168.0.1
```

This command will scan the 1000 most common ports on host `192.168.0.1` and display the services accessed and protocols used. If DNS is configured, it is also possible to use the host name instead of the IP address.


#### Complete network scan

One of the advantages of `nmap` is its ability to analyze a range of addresses with a single command. This makes it possible, for example, to draw up a quick inventory of the machines active on a given network:

```bash
nmap 192.168.0.0/24
```

In this example, all hosts in the range `192.168.0.0` to `192.168.0.255` will be queried. The result will show, for each IP address, the list of open ports, their status (open, filtered...), and if possible, the name of the corresponding service.


![Image](assets/fr/055.webp)


An administrator can use `nmap` for several tasks:
- Detection of active hosts: by scanning a subnet, we identify the machines that respond to a request;
- Inventory of exposed services: useful for checking that only necessary ports are accessible (principle of least privilege);
- Compliance check: compare open ports with network security policy ;
- Vulnerability prevention: identify insecure or obsolete services open on critical machines.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d


### Process interrogation tools

One of the most powerful tools available to Linux administrators is the `lsof` (*List Open Files*) command, for in-depth analysis of active processes and open files on a system, particularly in a network context. Contrary to what its name might suggest, `lsof` is not limited to classic files: in the UNIX system, everything is considered a file, including network sockets, peripherals, communication channels...

This tool therefore provides a cross-sectional view of the system, cross-referencing information on active processes, open network ports, files handled and users involved.


#### Network analysis with `lsof

The `-i` option allows you to restrict output to network connections, whether TCP, UDP, IPv4 or IPv6. It is useful for quickly observing which processes are interacting with the network:

```bash
lsof -i
```

This type of command lists all running processes using a network socket, with information on the port used, the protocol (TCP/UDP), the connection status, as well as the PID and corresponding user.


#### Filtering by IP address or port

To refine the search, you can specify an IP address and a port. This makes it possible to isolate a specific network flow, for example an SMTP communication (port 25) with a given machine:

```bash
lsof -n -i @192.168.2.1:25
```

This will display only active network connections with host `192.168.2.1` on port 25, which can be useful for diagnosing suspicious activity or SMTP blocking.


#### Device access tracking

One of the great advantages of `lsof` is its ability to monitor the use of special files, such as disk partitions. For example, you can find out which processes have opened files on the `/dev/sda1` partition:

```bash
lsof /dev/sda1
```

This is useful when a dismount attempt fails because the device is still in use, or when trying to understand which applications are accessing a given partition.


#### Cross-analysis: process and network

You can combine several options to obtain precise information on the resources opened by a specific process. For example, to find out all the network ports opened by the process with PID 1521 :

```bash
lsof -i -a -p 1521
```

The `-a` option performs an intersection of criteria (here: `-i` and `-p`), thus limiting the display to network connections belonging to this process alone.


#### Multi-user tracking

Finally, `lsof` can also be used to analyze the behavior of one or more users, by listing all files opened by them, possibly filtering by PID :

```bash
lsof -p 1521 -u 500,phil
```

This command can be used, for example, to find out which files or network connections are being used by user `phil` or UID 500, for process 1521.


### Part summary

By the end of this final section, we have explored a wide range of tools that are indispensable for diagnosing, analyzing and administering computer networks. This study, organized around the different layers of the TCP/IP model, not only provides a better understanding of how network communications work, but also a rigorous methodology for identifying, locating and resolving potential problems.

These tools provide administrators with a coherent set of technical levers for monitoring network status, analyzing flows, auditing connections and rapidly intervening on faulty equipment or services.


#### Network Access Layer

These utilities provide direct visibility of interfaces and frames:
- arp / ip neigh**: inspect and modify the ARP/NDP cache to check or correct IP-MAC associations;
- tcpdump**: filterable and exportable command-line capture of packets circulating on a Interface ;
- Wireshark**: in-depth graphical decoding of frames for ;
- ethtool**: dynamic interrogation and adjustment of Ethernet card physical parameters (speed, duplex, WoL, etc.).


#### Network layer

Here we evaluate IP connectivity, routing and packet flow:
- ping**: reachability test and latency measurement via ICMP ;
- ip route**: consult and manipulate the routing table to control the paths taken ;
- traceroute**: hop-by-hop identification of routers traversed to destination;
- ss**: precise inventory of TCP/UDP sockets and associated processes (replaces netstat).


#### Transport and Application layers

At higher levels, the aim is to diagnose services and processes:
- nslookup / dig / host**: DNS queries to validate name resolution and analyze ;
- nmap**: explore open ports and exposed services to assess the attack surface;
- lsof**: inventory of files and sockets opened by processes, to correlate system and network activities.

Mastery of these tools, each dedicated to a specific stage of the TCP/IP model, enables a methodical approach to be adopted: from the physical layer, through routing, right up to application services. This chain of expertise gives administrators the ability to diagnose, secure and optimize the infrastructure, thus guaranteeing network performance and availability.


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