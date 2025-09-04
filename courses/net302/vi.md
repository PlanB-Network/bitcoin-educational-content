---
name: Mạng IP từ lý thuyết đến thực hành
goal: Nắm vững những kiến thức cơ bản về mạng IP để cấu hình và khắc phục sự cố tốt hơn.
objectives: 


  - Hiểu kiến trúc và hoạt động của giao thức TCP/IP
  - Giải thích sự khác biệt, ưu điểm và hạn chế của IPv4 và IPv6
  - Xác định và phân biệt các loại IP Address khác nhau
  - Cấu hình và xác minh địa chỉ IP trên hệ thống Unix/Linux
  - Sử dụng các công cụ chẩn đoán chính để phân tích và giải quyết các vấn đề mạng


---

# Kỹ năng thiết yếu để điều hướng thế giới IP


Khám phá cốt lõi của thế giới IP và trang bị cho mình kiến thức để hiểu và quản lý mạng hiệu quả. Trong khóa học này, bạn sẽ được học mọi thứ cần biết về mạng máy tính một cách rõ ràng và thực tế.


Bạn sẽ tìm hiểu cách thức hoạt động của mạng và địa chỉ IP, cách phân biệt giữa IPv4 và IPv6, cách xác định và sử dụng các danh mục Address khác nhau và cách nắm bắt toàn bộ tầm quan trọng của giao thức TCP/IP và các liên kết mà nó tạo ra giữa địa chỉ IP, địa chỉ vật lý và tên DNS.


NET 302 chủ yếu hướng đến sinh viên, người dùng Linux hoặc đơn giản là những người tò mò muốn hiểu những kiến thức cơ bản về mạng và tăng cường khả năng tự chủ trong việc quản lý, khắc phục sự cố và tối ưu hóa cơ sở hạ tầng.


Hãy tham gia cùng chúng tôi và biến kiến thức của bạn thành chuyên môn vận hành thực tế!


___


Khóa học NET 302 này là bản chuyển thể của khóa học *Cơ bản về mạng: TCP/IP, IPv4 và IPv6*, được Philippe Pierre viết bằng tiếng Pháp và xuất bản trên [IT-Connect](https://www.it-connect.fr/cours/les-bases-du-reseau-tcpip-ipv4-et-ipv6/), theo giấy phép Creative Commons Attribution-NonCommercial 4.0 International ([CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)).



Phiên bản gốc của Loïc Morel đã có những thay đổi đáng kể: toàn bộ văn bản đã được viết lại, mở rộng và bổ sung để cung cấp nội dung cập nhật, chuyên sâu, đồng thời vẫn giữ nguyên tinh thần giáo dục của tác phẩm gốc của Philippe Pierre. Các sơ đồ cũng đã được hiệu chỉnh.


+++


# Giới thiệu


<partId>a52b996d-1e23-470f-a9df-7ad88790099a</partId>



## Tổng quan về khóa học


<chapterId>9f238ecd-c9bb-4886-a205-2beba609fb13</chapterId>


Khóa học này cung cấp phần giới thiệu đầy đủ về các nguyên tắc cơ bản của mạng IP. Khóa học được cấu trúc thành bốn phần chính, mỗi phần đề cập đến một khía cạnh thiết yếu để hiểu, cấu hình và chẩn đoán các sự cố trong mạng máy tính.


### Giao thức TCP/IP


Trong phần đầu tiên này, chúng ta sẽ đặt nền móng bằng cách khám phá khái niệm mạng và lịch sử của giao thức TCP/IP. Chúng ta sẽ nghiên cứu các thành phần chính của nó: IP, TCP, cùng với một cái nhìn tổng quan về giao thức QoS của IPv5. Chúng ta cũng sẽ tìm hiểu các nguyên hàm dịch vụ để hiểu rõ hơn về logic của dữ liệu Exchange.


### Địa chỉ IPv4


Sau đó, chúng ta sẽ chuyển sang một học phần chuyên sâu về địa chỉ IPv4. Bạn sẽ tìm hiểu cách sử dụng IPv4 trong thực tế, các loại Address khác nhau (riêng tư, công cộng, phát sóng, v.v.), vai trò cơ bản của DNS, cũng như cách hoạt động của địa chỉ Ethernet và giao thức ARP. Bạn cũng sẽ tìm hiểu về NAT (Chuyển đổi Address Mạng) và những kiến thức cơ bản về cấu hình mạng.


### Địa chỉ IPv6


Phần thứ ba tập trung vào địa chỉ IPv6, một yếu tố cần thiết để khắc phục những hạn chế của IPv4. Chúng ta sẽ tìm hiểu các tiêu chuẩn và định nghĩa của nó, Address Assignment trong mạng cục bộ, quản lý khối Address và mối quan hệ giữa IPv6 và DNS.


### Công cụ chẩn đoán mạng


Cuối cùng, chúng tôi sẽ kết thúc bằng phần trình bày về các công cụ chẩn đoán mạng chính. Chúng sẽ cho phép bạn phân tích, kiểm soát và khắc phục sự cố. Phần này sẽ được cấu trúc theo các lớp: Truy cập Mạng, Mạng, Vận chuyển và Lớp trên.


Đến cuối khóa học này, bạn sẽ có kiến thức cơ bản để quản lý hiệu quả cơ sở hạ tầng mạng và chẩn đoán các vấn đề tiềm ẩn.


Bạn đã sẵn sàng khám phá thế giới mạng máy tính chưa? Bắt đầu thôi!


**LƯU Ý**: Các mô tả được dựa trên hệ thống GNU/Linux CentOS 7. Tuy nhiên, cấu hình mạng phần lớn giống nhau khi so sánh Debian với hệ thống CentOS. Vì vậy, chúng tôi sẽ không phân biệt. Nếu có, chúng tôi sẽ thêm một logo cụ thể vào trước.


**Lưu ý**: Nếu bạn gặp bất kỳ thuật ngữ nào không quen thuộc trong suốt khóa học, vui lòng tham khảo [thuật ngữ](https://planb.network/resources/glossary) để biết định nghĩa.



# Giao thức TCP/IP


<partId>53fd4b73-cdf1-4865-ba29-1ac8ec3e9e9a</partId>



## Mạng là gì?


<chapterId>7370904f-f8f5-4ad4-a63a-5931d94c3b3b</chapterId>



Trong học phần đầu tiên này, chúng ta sẽ tìm hiểu sâu hơn về giao thức TCP/IP, nền tảng của truyền thông kỹ thuật số hiện đại. Chúng ta sẽ thảo luận về nguồn gốc, các nguyên tắc cơ bản và hệ thống địa chỉ mà nó sử dụng, vốn rất cần thiết để đảm bảo luồng thông tin giữa các thiết bị được kết nối.


Chúng tôi cũng sẽ trình bày chi tiết các thành phần chính cấu thành nên mô hình này và giải thích cách chúng tương tác để tạo nên một mạng lưới vận hành ổn định, đáng tin cậy và có khả năng mở rộng. Nhưng trước tiên, điều quan trọng là phải quay lại khái niệm mạng lưới.


Về mặt từ nguyên, mạng là tập hợp các điểm được liên kết với nhau, tạo thành một cấu trúc kết nối. Trong viễn thông và điện toán, định nghĩa này được hiểu là một nhóm các thiết bị (máy tính, bộ định tuyến, bộ chuyển mạch, điểm truy cập, v.v.) có khả năng trao đổi dữ liệu qua phương tiện vật lý hoặc không dây. Do đó, mạng cho phép luồng thông tin liên tục hoặc gián đoạn, tùy thuộc vào yêu cầu, giao thức đang sử dụng và bản chất của kiến trúc được triển khai.


Theo thời gian, một số cấu trúc mạng cổ điển đã được phát triển để đáp ứng các nhu cầu khác nhau về chi phí, hiệu suất, khả năng phục hồi và dễ bảo trì. Những cấu trúc này bao gồm:


- mạng vòng,
- mạng lưới cây,
- mạng lưới xe buýt,
- mạng lưới ngôi sao,
- mạng lưới mắt cáo.



### Mạng vòng


Trong cấu trúc mạng vòng, các thiết bị được kết nối theo một vòng kín: mỗi trạm được liên kết với trạm tiếp theo, và trạm cuối cùng kết nối trở lại trạm đầu tiên. Trong cấu hình này, mỗi thiết bị hoạt động như một rơle, truyền dữ liệu đến liên kết tiếp theo. Tùy thuộc vào loại mạng, thông tin có thể chỉ lưu thông theo một hướng hoặc cả hai hướng.


Ưu điểm của giải pháp này nằm ở tính đơn giản của hệ thống cáp và không phụ thuộc vào bất kỳ thiết bị trung tâm nào. Tuy nhiên, tính liên tục của toàn bộ mạng lưới phụ thuộc vào tình trạng hoạt động của từng thành phần riêng lẻ: sự cố của một trạm duy nhất có thể làm gián đoạn toàn bộ hệ thống truyền thông. Đây là lý do tại sao các cơ chế dự phòng hoặc bỏ qua thường được áp dụng.



![Image](assets/fr/001.webp)



### Mạng lưới cây


Mạng lưới cây, hay cấu trúc phân cấp, được mô phỏng theo cấu trúc của cây phả hệ. Nó bao gồm các cấp bậc liên tiếp: một nút gốc ở trên cùng kết nối với một số nút cấp thấp hơn, các nút này có thể kết nối với các nút khác, v.v.


Bố cục phân cấp này đặc biệt hiệu quả với các mạng lớn cần phân chia trách nhiệm rõ ràng và quản lý phân đoạn. Tuy nhiên, nó cũng khiến mạng dễ bị tổn thương trước sự cố của các nút cấp cao hơn: việc mất nút gốc hoặc một nhánh chính có thể cắt đứt toàn bộ các phần của cơ sở hạ tầng.



![Image](assets/fr/002.webp)



### Mạng lưới xe buýt


Trong cấu trúc bus, tất cả các thiết bị chia sẻ cùng một môi trường truyền dẫn, thường là đường truyền đồng trục hoặc cáp quang. Mỗi thiết bị được kết nối thụ động, nghĩa là nó không chủ động sửa đổi tín hiệu và có thể gửi hoặc nhận dữ liệu qua kênh chung này.


Ưu điểm chính của cấu trúc bus là chi phí lắp đặt thấp, nhờ hệ thống cáp được đơn giản hóa. Tuy nhiên, trong các triển khai cáp đồng trục cũ (Ethernet 10BASE2/10BASE5), việc ngắt kết nối hoặc mất một trạm duy nhất có thể làm gián đoạn hoặc thậm chí dừng toàn bộ lưu lượng, do tính liên tục về điện và trở kháng đầu cuối của bus sẽ không còn được duy trì. Việc chỉ có một môi trường vật lý duy nhất cũng là một điểm yếu nghiêm trọng: bất kỳ sự cố hoặc gián đoạn nào cũng sẽ làm gián đoạn giao tiếp của toàn bộ mạng.



![Image](assets/fr/003.webp)



### Mạng lưới sao


Cấu trúc hình sao, còn được gọi là "trục và nan hoa", là cấu trúc phổ biến nhất hiện nay, đặc biệt là trong mạng Ethernet gia đình và văn phòng. Ở đây, tất cả các thiết bị kết nối với một thiết bị trung tâm duy nhất.


Bố cục này giúp việc quản lý và bảo trì trở nên dễ dàng: nếu một thiết bị ngoại vi bị lỗi, phần còn lại của mạng vẫn không bị ảnh hưởng. Nhược điểm là thiết bị trung tâm là điểm lỗi duy nhất: nếu nó ngừng hoạt động, giao tiếp sẽ bị gián đoạn ở mọi nơi. Chất lượng cáp và chiều dài liên kết cũng cần được cân nhắc kỹ lưỡng để duy trì hiệu suất tốt.



![Image](assets/fr/004.webp)



**Lưu ý**: Vẫn có những mạng được tổ chức theo cấu trúc tuyến tính, dạng bus, trong đó các thiết bị được kết nối lần lượt. Giải pháp này, mặc dù không tốn kém để triển khai, nhưng có nhược điểm lớn là chỉ cần một lần ngắt kết nối sẽ cô lập một số máy chủ, chia mạng thành các tập hợp con độc lập.


### Mạng lưới lưới


Mạng lưới được thiết kế để đạt độ dự phòng tối đa: mọi thiết bị đều được kết nối trực tiếp với mọi thiết bị khác. Điều này đảm bảo tính liên tục của dịch vụ ngay cả khi nhiều liên kết hoặc thiết bị gặp sự cố, vì lưu lượng có thể được định tuyến lại theo các đường dẫn thay thế.


Nhược điểm là số lượng kết nối cần thiết lập tăng nhanh theo số lượng thiết bị đầu cuối. Với `N` điểm kết nối, cần `N × (N-1) / 2` liên kết riêng biệt, khiến cấu trúc này tốn kém và phức tạp khi triển khai. Do đó, nó chủ yếu được sử dụng trong các mạng quan trọng đòi hỏi tính khả dụng rất cao, chẳng hạn như một số phần của Internet hoặc các hệ thống công nghiệp nhạy cảm.



![Image](assets/fr/005.webp)



Ngoài ra còn có các biến thể khác, chẳng hạn như mạng lưới lưới hoặc mạng siêu khối, được thiết kế cho các nhu cầu chuyên biệt trong tính toán phân tán hoặc xử lý song song.


Trên phạm vi toàn cầu, Internet là một mạng lưới kết nối khổng lồ sử dụng nhiều cấu trúc mạng khác nhau, được thống nhất bởi địa chỉ chung (IPv4 và IPv6) và một tập hợp các giao thức chuẩn hóa do IETF (*Lực lượng Đặc nhiệm Kỹ thuật Internet*) định nghĩa. Sự đa dạng này đồng nghĩa với việc Internet không tuân theo một cấu trúc mạng duy nhất: cấu trúc của nó linh hoạt, có khả năng mở rộng và độc lập với sơ đồ địa chỉ logic giúp nó có thể sử dụng được.



## Nguồn gốc của TCP/IP


<chapterId>266b6864-8789-48d7-bc85-001cb9f1651f</chapterId>



Nguồn gốc của giao thức TCP bắt nguồn từ **ARPA** (*Cơ quan Dự án Nghiên cứu Tiên tiến*, đổi tên thành "DARPA" vào năm 1972), đơn vị đã khởi động dự án **ARPANET** vào năm 1966. Phân đoạn ARPANET đầu tiên được triển khai vào tháng 10 năm 1969, kết nối các trường đại học UCLA và Stanford. Mục tiêu là kết nối các trung tâm nghiên cứu thông qua một mạng chuyển mạch gói, có thể duy trì liên lạc ngay cả khi cơ sở hạ tầng bị lỗi một phần.


Trong nỗ lực này, ARPA đã tài trợ cho Đại học Berkeley tích hợp các giao thức TCP/IP đầu tiên vào hệ thống BSD Unix của trường. Điều này đóng vai trò quan trọng trong việc phổ biến và chuẩn hóa giao thức, đầu tiên là trong giới học thuật, và sau đó là trong ngành công nghiệp.


**Lưu ý**: Vào thời điểm đó, các nhà khoa học máy tính chưa có Linux (mà mãi đến đầu những năm 1990 mới xuất hiện), cũng chưa có Minix, hệ thống giáo dục do Andrew Tanenbaum thiết kế. Các lựa chọn chính là Unix, hoặc đôi khi là các máy chủ lớn độc quyền như OpenVMS. Nhờ tính linh hoạt và tính mở, Unix đã đóng vai trò quan trọng trong việc truyền bá các khái niệm mạng đầu tiên.


Nói một cách chính xác, TCP/IP không phải là một giao thức đơn lẻ mà là một bộ giao thức được xây dựng xung quanh TCP và IP. Nó nổi lên nhờ cung cấp một Interface lập trình chuẩn hóa để trao đổi dữ liệu giữa các máy trong cùng một mạng. Interface này, dựa trên các nguyên hàm gọi là "socket", cho phép tạo ra các kết nối đáng tin cậy và linh hoạt trong khi tích hợp các giao thức ứng dụng thiết yếu.


ARPANET do đó là nền tảng lịch sử của Internet ngày nay. Thực tế, Internet là một mạng lưới toàn cầu dựa trên nguyên lý chuyển mạch gói, trong đó thông tin được lưu thông bằng một bộ giao thức chuẩn hóa đảm bảo tính tương thích và khả năng tương tác giữa các hệ thống không đồng nhất. Kiến trúc mở này đã cho phép phát triển và triển khai vô số dịch vụ và ứng dụng, bao gồm:


- email,
- Mạng lưới toàn cầu (www),
- chuyển và chia sẻ tập tin...


Việc quản lý và phát triển các giao thức này được giám sát bởi ***Hội đồng Kiến trúc Internet*** (IAB).

Tổ chức này điều phối các hướng kỹ thuật thông qua hai cấu trúc chính:


- IRTF** (_Lực lượng đặc nhiệm nghiên cứu Internet_), tiến hành nghiên cứu dài hạn về sự phát triển và cải tiến giao thức.
- IETF** (_Lực lượng đặc nhiệm kỹ thuật Internet_), phát triển, chuẩn hóa và lập tài liệu về các giao thức hoạt động được sử dụng trên Internet


Việc phân phối tài nguyên mạng (dải IP Address, số hiệu hệ thống tự trị, tên miền gốc, v.v.) được điều phối quốc tế bởi **IANA/ICANN**. Quản lý vận hành dựa trên: **RIR** (*Cơ quan Đăng ký Internet Khu vực*): **RIPE NCC** (Châu Âu, Trung Đông, Trung Á), **ARIN**, **APNIC**, **LACNIC** và **AFRINIC**.


Tất cả các thông số kỹ thuật của giao thức TCP/IP đều được ghi lại trong các tài liệu gọi là **RFC** (_Yêu cầu bình luận_), đóng vai trò là tài liệu tham khảo kỹ thuật có thẩm quyền. RFC liên tục được cập nhật và đánh số để phản ánh sự phát triển không ngừng của bộ giao thức.


Ngăn xếp TCP/IP thường được biểu diễn dưới dạng một ngăn xếp gồm bốn lớp chức năng, thường được so sánh với mô hình **OSI** (_Kết nối hệ thống mở_) bảy Layer do **ISO** (_Tổ chức tiêu chuẩn quốc tế_) phát triển, đóng vai trò là tài liệu tham khảo khái niệm về mạng.


Bốn lớp của mô hình TCP/IP là:


- NETWORK ACCESS Layer cung cấp các giao thức kiểm soát truy cập phương tiện và liên kết vật lý;
- INTERNET Layer, xử lý định tuyến và địa chỉ IP;
- TRANSPORT Layer, đảm bảo độ tin cậy và quản lý luồng dữ liệu bằng các giao thức như TCP hoặc UDP;
- ỨNG DỤNG Layer, nhóm các giao thức người dùng và phần mềm như HTTP, FTP, SMTP và DNS.



![Image](assets/fr/006.webp)



Ngày nay, phiên bản IP được sử dụng rộng rãi nhất là IPv4, nhưng không gian địa chỉ Address 32-bit của nó có những hạn chế rõ ràng. Điều này dẫn đến sự ra đời của IPv6, sử dụng địa chỉ 128-bit và cung cấp dung lượng gần như không giới hạn: thiết yếu để hỗ trợ sự phát triển bùng nổ của các thiết bị kết nối và đáp ứng những thách thức của Internet vạn vật, tính di động và bảo mật.


Mỗi Layer của ngăn xếp TCP/IP cung cấp các dịch vụ cụ thể, giúp đáp ứng các nhu cầu mạng khác nhau theo cách mô-đun: truyền vật lý, định địa chỉ logic, tính toàn vẹn dữ liệu và các dịch vụ cấp ứng dụng.


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

## Giao thức QoS IPv5


<chapterId>570ded19-be61-4005-844e-9490570a6455</chapterId>



Tiêu đề của gói tin IP là một cấu trúc dữ liệu thiết yếu, được chia thành nhiều trường, mỗi trường có một vai trò cụ thể để đảm bảo các gói tin được truyền và xử lý chính xác khi chúng di chuyển qua mạng. Các trường này bao gồm địa chỉ IP đích Address (cần thiết để định tuyến gói tin đến người nhận dự định), độ dài tiêu đề được chỉ định bởi trường IHL (*Độ dài Tiêu đề Internet*), tổng chiều dài gói tin được ghi lại trong trường *Độ dài Tổng*, thông tin điều khiển và xác minh, cùng các tham số khác để quản lý luồng và chất lượng truyền thông.


Trường đầu tiên trong tiêu đề được gọi là Phiên bản (Version). Giá trị 4 bit này chỉ định phiên bản giao thức IP mà gói tin tuân theo. Điều này rất quan trọng vì nó cho mỗi bộ định tuyến hoặc thiết bị trung gian biết cách diễn giải và xử lý dữ liệu được đóng gói.


**Lưu ý**: Việc quản lý và phân bổ các phiên bản giao thức IP thuộc trách nhiệm của **IANA**. Một trường 4 bit cho phép 16 tổ hợp nhị phân (giá trị từ 0 đến 15). Cho đến nay, sự phân bổ của chúng như sau:



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

Trong số đó có IPv5, mặc dù phần lớn chưa được công chúng biết đến, nhưng đã tồn tại dưới dạng ST (Giao thức luồng). Được phát triển vào những năm 1980, IPv5 được thiết kế để đáp ứng nhu cầu ngày càng tăng vào thời điểm đó: cung cấp "Chất lượng Dịch vụ" (QoS) cho một số luồng dữ liệu nhất định yêu cầu truyền tải liên tục, ổn định, chẳng hạn như Thoại qua IP (VoIP) hoặc các luồng đa phương tiện. Mục tiêu của nó là đảm bảo băng thông và mức độ ưu tiên từ đầu đến cuối, một khái niệm tương tự như RSVP (Giao thức Đặt trước Tài nguyên) hiện nay, cho phép đặt trước tài nguyên mạng một cách linh hoạt trên các bộ định tuyến hiện đại.


Tuy nhiên, IPv5 vẫn còn trong giai đoạn thử nghiệm và chỉ được triển khai trên một số ít thiết bị mạng. Việc áp dụng hạn chế, cùng với nhu cầu ngày càng tăng về không gian Address, đã khiến các nhà thiết kế Internet chuyển thẳng từ IPv4 sang IPv6. Điều này tránh được cả những hạn chế của Address của IPv4 lẫn nguy cơ nhầm lẫn hoặc không tương thích với các thông số kỹ thuật thử nghiệm của IPv5.


Mặc dù IPv5 chưa bao giờ được sử dụng rộng rãi, nhưng nó đã đóng một vai trò quan trọng trong việc định hình tư duy ban đầu về QoS và quản lý lưu lượng. Ngày nay, nó mang tính lịch sử hơn là một tiêu chuẩn hoạt động.


**Lưu ý** - Giao thức là một tập hợp các quy tắc giao tiếp: cấu trúc dữ liệu, thuật toán, định dạng gói tin và các quy ước cho phép các thiết bị khác nhau truyền tải thông tin một cách đáng tin cậy và dễ hiểu. Dịch vụ là việc triển khai cụ thể một giao thức thông qua các chương trình cụ thể (máy khách, máy chủ) tuân theo các quy tắc này và cung cấp chức năng cho người dùng và ứng dụng.


Bây giờ chúng ta có thể xem xét kỹ hơn cấu trúc và hoạt động của giao thức IP, nền tảng thiết yếu của mọi giao tiếp mạng.



## Giao thức IP


<chapterId>758fddbd-b652-4c18-bd1e-d038bd2e4d05</chapterId>



### Định nghĩa và thông tin chung


Giao thức IP, hay "***Giao thức Internet***", là xương sống của mô hình TCP/IP. Nó truyền tải các gói dữ liệu từ máy chủ này đến máy chủ khác trong một mạng, dù là mạng cục bộ hay mạng toàn cầu. Nó có hai vai trò chính: quản lý việc định địa chỉ logic của các thiết bị và đảm bảo các gói được định tuyến qua các mạng thường không đồng nhất và được kết nối với nhau.


Ở cấp độ vật lý, việc truyền tải dựa vào giao diện phần cứng để thiết lập kết nối điểm-điểm giữa các nút. Tuy nhiên, chính giao thức IP mới giúp thực hiện giao tiếp đầu cuối, cung cấp cho mỗi gói tin thông tin cần thiết để điều hướng qua nhiều đường dẫn có thể đến đích.


Ba cấu hình mạng Elements xác định cách một gói tin được gửi trên đường đi:


- IP Address**: xác định duy nhất máy chủ đích trong mạng.
- Mặt nạ mạng con**: chỉ định phần nào của Address xác định mạng và phần nào xác định máy chủ, cho phép phân chia hợp lý thành các mạng con.
- Cổng**: chỉ ra bộ định tuyến trung gian mà gói tin phải đi qua để đến được mạng bên ngoài hoặc một phân đoạn khác của mạng cục bộ.


Trên Internet, dữ liệu không chảy thành một luồng liên tục, mà được gửi dưới dạng **datagram**: các khối dữ liệu độc lập, mỗi khối được đóng gói với tất cả thông tin cần thiết để truyền tải. Đây là nguyên lý của **chuyển mạch gói**, trong đó thông tin được chia thành các đơn vị độc lập, có thể đi theo nhiều đường dẫn khác nhau để đến cùng một người nhận.


Ngoài phần tải trọng (*payload*), mỗi gói dữ liệu IP còn chứa một tiêu đề có cấu trúc với các trường như đích Address, nguồn Address, loại dịch vụ, số phiên bản giao thức và các thông tin điều khiển khác cần thiết để quản lý quá trình truyền tải.


Kích thước tối đa lý thuyết của một gói tin IP là **65.536 octet**, một giới hạn được thiết lập bởi trường tổng chiều dài trong tiêu đề. Trên thực tế, kích thước này hiếm khi đạt được, vì các mạng vật lý truyền tải các gói tin (Ethernet, Wi-Fi, cáp quang...) thường áp dụng một giới hạn chặt chẽ hơn được gọi là **MTU** (Đơn vị Truyền Tối đa). Nếu một gói tin vượt quá MTU của liên kết vật lý, nó phải được chia thành các gói tin nhỏ hơn, mỗi gói được gửi riêng biệt và được ghép lại khi đến nơi.


Khả năng thích ứng này làm cho IP trở thành một giao thức mạnh mẽ và linh hoạt, có thể hoạt động trên nhiều công nghệ cơ bản khác nhau trong khi vẫn duy trì khả năng tương thích chung giữa các hệ thống và mạng không đồng nhất.



### Phân mảnh các gói dữ liệu IP


Khi một gói tin IP cần truyền qua một mạng có dung lượng truyền nhỏ hơn chính gói tin đó, gói tin đó phải được **phân mảnh** để có thể truyền đi mà không gặp sự cố. Giới hạn kích thước vật lý này được gọi là **MTU** (Đơn vị Truyền Tối đa): kích thước khung lớn nhất có thể truyền qua một mạng nhất định mà không bị chia tách.


Mỗi công nghệ mạng áp dụng MTU riêng, được xác định bởi đặc điểm phần cứng và giao thức. Các giá trị phổ biến bao gồm:


- ARPANET**: 1000 byte
- Ethernet**: 1500 byte
- FDDI**: 4470 byte


Khi một datagram vượt quá MTU của một phân đoạn mạng mà nó cần đi qua, thiết bị định tuyến sẽ chia nó thành các **mảnh** nhỏ hơn, tuân thủ giới hạn. Điều này thường xảy ra khi di chuyển từ mạng có MTU cao sang mạng có dung lượng thấp hơn. Ví dụ: một datagram đến từ mạng FDDI có thể cần được phân mảnh trước khi được gửi qua phân đoạn Ethernet.



![Image](assets/fr/008.webp)



Quá trình phân mảnh hoạt động như sau:


- Bộ định tuyến chia gói dữ liệu thành các đoạn có kích thước không lớn hơn MTU của mạng đích.
- Kích thước của mỗi đoạn là bội số của 8 byte, vì giao thức IP sử dụng đơn vị này để mã hóa độ lệch lắp ráp lại.
- Mỗi đoạn mã đều có tiêu đề IP riêng, chứa thông tin cần thiết để người nhận cuối cùng có thể lắp ráp lại theo đúng thứ tự.


Sau khi bị phân mảnh, các mảnh sẽ di chuyển độc lập qua mạng. Chúng có thể đi theo các tuyến đường khác nhau, tùy thuộc vào bảng định tuyến, tải liên kết hoặc sự cố. Không có gì đảm bảo chúng sẽ đến đích theo đúng thứ tự đã gửi.


Khi đến nơi, máy nhận sẽ xử lý việc **lắp ráp lại**. Sử dụng thông tin trong các tiêu đề (mã định danh chung, offset và cờ phân mảnh), máy nhận sẽ sắp xếp các mảnh lại theo đúng thứ tự để tái tạo lại datagram gốc trước khi truyền đến Layer tiếp theo. Nếu chỉ cần một mảnh bị mất hoặc bị hỏng, toàn bộ datagram thường sẽ bị loại bỏ. Nếu thiếu tất cả các mảnh, kết quả sẽ không đầy đủ hoặc không sử dụng được.


Mặc dù hiệu quả, việc phân mảnh và lắp ráp lại cũng có những nhược điểm: bộ định tuyến và máy chủ phải xử lý thêm, và nguy cơ mất gói tin cao hơn, có thể làm tăng số lần truyền lại. Đó là lý do tại sao việc quản lý MTU cẩn thận và tối ưu hóa kích thước gói tin rất quan trọng để giao tiếp IP trơn tru và hiệu quả.



### Đóng gói dữ liệu


Để đảm bảo dữ liệu được định tuyến chính xác qua các lớp của mô hình TCP/IP, quá trình **đóng gói** đóng một vai trò quan trọng. Ở mỗi giai đoạn khi một thông điệp đi từ ứng dụng của người gửi đến máy của người nhận, thông tin bổ sung, được gọi là tiêu đề, sẽ được thêm vào. Các tiêu đề này cung cấp cho các thiết bị trung gian và các lớp phần mềm các hướng dẫn cần thiết để xử lý, phân phối và, nếu cần, lắp ráp lại dữ liệu.


Khi một thông điệp được gửi đi, nó sẽ đi qua bốn lớp của ngăn xếp TCP/IP. Tại mỗi Layer, một tiêu đề mới được thêm vào trước dữ liệu hiện có: mỗi tiêu đề chứa siêu dữ liệu cụ thể, chẳng hạn như địa chỉ logic hoặc vật lý, cổng giao tiếp, số thứ tự, cờ kiểm soát lỗi và bất kỳ thông tin nào cần thiết để quản lý việc truyền tải và định tuyến.


Quá trình truyền tải do đó tuân theo một quá trình có cấu trúc:


- Ứng dụng Layer tạo **thông điệp** ban đầu, chứa dữ liệu thô.
- Transport Layer đóng gói thông tin này thành một **phân đoạn**, thêm các cổng nguồn và đích, số thứ tự và cơ chế kiểm soát luồng.
- Internet Layer thêm vào phân đoạn một tiêu đề IP để tạo thành **datagram**, chỉ định địa chỉ IP nguồn và đích.
- Network Access Layer gói datagram vào một **khung**, thêm địa chỉ MAC và mã kiểm tra tính toàn vẹn (CRC).



![Image](assets/fr/009.webp)



Quá trình đóng gói này đảm bảo tính toàn vẹn và khả năng truy xuất của dữ liệu cũng như khả năng thích ứng của dữ liệu: khi di chuyển từ mạng này sang mạng khác, các tiêu đề cung cấp cho thiết bị thông tin cần thiết để chọn tuyến đường, kiểm tra tính hợp lệ hoặc thực hiện phân mảnh nếu cần.


Khi đến nơi, quy trình được đảo ngược: máy nhận nhận khung tại Network Access Layer, nơi đọc và xóa tiêu đề tương ứng. Sau đó, datagram được chuyển đến Internet Layer, nơi đọc tiêu đề IP và xóa tiêu đề này để chuyển phân đoạn đến Transport Layer. Transport Layer xử lý tiêu đề truyền tải, kiểm tra tính toàn vẹn của luồng và cuối cùng chuyển **thông điệp** đến ứng dụng đích ở trạng thái ban đầu.



![Image](assets/fr/010.webp)



Quá trình chuyển đổi dữ liệu tại mỗi Layer có thể được tóm tắt như sau:


- Tin nhắn**: khối thông tin tại Ứng dụng Layer.
- Phân đoạn**: đơn vị dữ liệu sau khi được đóng gói bởi Transport Layer.
- Datagram**: dạng được tạo ra sau khi tiêu đề IP được thêm vào bởi Internet Layer.
- Khung**: khối cuối cùng sẵn sàng để truyền qua phương tiện vật lý bởi Network Access Layer.



![Image](assets/fr/011.webp)



Quá trình này, rất cần thiết cho độ tin cậy và tính phổ biến của truyền thông Internet, đảm bảo rằng mọi dữ liệu, bất kể phân mảnh hay phức tạp đến đâu, đều có thể được truyền tải từ đầu đến cuối trong khi vẫn dễ hiểu và có thể sử dụng được bởi máy nhận.



### Địa chỉ IP


Ngay cả khi đã áp dụng chuyển mạch gói, phân mảnh và đóng gói, mạng vẫn không thể hoạt động nếu không có hệ thống định địa chỉ đáng tin cậy. Để đảm bảo mỗi gói dữ liệu đến đúng người nhận, Internet Layer sử dụng một mã định danh duy nhất: **IP Address**.

Trong IPv4, IP Address được mã hóa trên **32 bit** và được viết dưới dạng bốn số thập phân được phân tách bằng dấu chấm, theo định dạng N1.N2.N3.N4 quen thuộc (ví dụ: 192.168.1.12).


IP Address có hai phần:


- _netid_**: xác định mạng mà máy chủ thuộc về
- _hostid_**: xác định máy chủ cụ thể trong mạng đó

Sự tách biệt này cho phép Internet toàn cầu được cấu trúc hợp lý thành nhiều mạng lưới kết nối với nhau.


Trước đây, hệ thống IPv4 dựa trên sơ đồ phân lớp, được đánh dấu từ A đến E, xác định phạm vi của Address và mục đích sử dụng của chúng. Mỗi lớp phân bổ một số bit nhất định cho _netid_ và _hostid_, ảnh hưởng trực tiếp đến số lượng mạng và máy chủ có thể có.



| **Class** | **IPv4 Address Range**            | **Usage**                    |
| --------- | --------------------------------- | ---------------------------- |
| A         | 1.x.x.x to 126.x.x.x              | Unicast addresses            |
|           | (127.x.x.x reserved for loopback) | Local loopback               |
| B         | 128.0.x.x to 191.255.x.x          | Unicast addresses            |
| C         | 192.0.0.x to 223.255.255.x        | Unicast addresses            |
| D         | 224.0.0.0 to 239.255.255.255      | IP Multicast                 |
| E         | 240.0.0.0 to 255.255.255.255      | Reserved for experimentation |

Không phải tất cả các giá trị khả thi đều có thể được gán cho máy chủ. Ví dụ, trong **lớp C** Address, byte cuối cùng cung cấp 8 bit (256 giá trị). Tuy nhiên, hai trong số này được dành riêng:


- 0: xác định chính mạng
- 255: là **phát sóng** Address, được sử dụng để gửi một gói tin đến tất cả các máy chủ trong mạng cùng một lúc.

Như vậy còn lại 254 địa chỉ có thể sử dụng cho các thiết bị.


Số lượng địa chỉ khả dụng thay đổi rất nhiều giữa các lớp: từ mạng công cộng lớn ở lớp A, đến mạng doanh nghiệp ở lớp B, đến mạng cục bộ nhỏ hơn ở lớp C.



![Image](assets/fr/013.webp)



Một số dải địa chỉ Address được dành riêng cho mục đích sử dụng cá nhân và không bao giờ được định tuyến trực tiếp trên Internet. Những dải địa chỉ này được gọi là **địa chỉ riêng**, được sử dụng trong các tổ chức, doanh nghiệp hoặc hộ gia đình, và yêu cầu chuyển đổi Address, thường là NAT (*Chuyển đổi Address Mạng*), để truy cập Internet công cộng. Các dải địa chỉ này bao gồm:


- Lớp A**: từ 10.0.0.0 đến 10.255.255.255
- Lớp B**: từ 172.16.0.0 đến 172.31.255.255
- Lớp C**: từ 192.168.0.0 đến 192.168.255.255


Khi một thiết bị có Address riêng truy cập Internet, bộ định tuyến hoặc cổng hỗ trợ NAT sẽ thay thế thiết bị đó bằng Address công cộng hợp lệ.


Ví dụ: Nếu máy chủ có Address **192.168.7.5**, chúng ta có thể suy ra:


- 192.168.7.0: mạng Address
- 192.168.7.1: thường là bộ định tuyến cục bộ
- 192.168.7.5: chính máy chủ


Một trường hợp đặc biệt khác là **127.0.0.1**, được gọi là "***loopback***".

Trên các hệ thống Linux, nó được liên kết với Interface **lo**. Address này cho phép máy tính tự Address để kiểm tra hoặc chẩn đoán cục bộ mà không cần thông qua Interface vật lý. Toàn bộ dải **127.0.0.0/8** được dành riêng cho mục đích này.


Để tối ưu hóa việc sử dụng Address và thiết kế các mạng phức tạp, mặt nạ mạng con (_netmask_) là rất cần thiết. Mặt nạ nhị phân này phân tách _netid_ với _hostid_ trong một IP Address.

Mỗi lớp có một mặt nạ mặc định:


- 255.0.0.0** cho lớp A,
- 255.255.0.0** cho lớp B,
- 255.255.255.0** cho lớp C.


Thiết kế mạng tốt tuân theo một quy tắc cơ bản: các thiết bị phải giao tiếp trực tiếp phải nằm trong cùng một mạng hoặc mạng con. Để phân đoạn mạng, chúng ta sử dụng kỹ thuật chia mạng thành các mạng con nhỏ hơn bằng cách sử dụng một mặt nạ cụ thể hơn.


Ví dụ về chia mạng con:

Mạng **lớp C**: 192.168.1.0/24 với mặt nạ mặc định là 255.255.255.0.

Chúng tôi muốn có 4 mạng con, mỗi mạng có tối đa 60 máy chủ.


**Bước 1**: Số địa chỉ cần thiết cho mỗi mạng con = 60 + 2 địa chỉ dành riêng (mạng + phát sóng) = 62.


**Bước 2**: Tìm lũy thừa gần nhất của 2 ≥ 62. -> 2⁶ = 64.


**Bước 3: Điều chỉnh mặt nạ. Giữ lại các bit _netid_ và dành riêng các bit _hostid_ cần thiết. Chúng ta thu được một mặt nạ nhị phân, sau khi chuyển đổi, sẽ cho ra **255.255.255.192**.


```
11111111 11111111 11111111 11000000
```


**Bước 4**: Tính toán phạm vi Address cho mỗi mạng con, thay đổi các bit dành riêng cho máy chủ.



| Subnet ID (bits) | Subnet Address   | Subnet Mask     | Address Range                 | Broadcast Address |
| ---------------- | ---------------- | --------------- | ----------------------------- | ----------------- |
| 00               | 192.168.1.0/26   | 255.255.255.192 | 192.168.1.1 – 192.168.1.62    | 192.168.1.63      |
| 01               | 192.168.1.64/26  | 255.255.255.192 | 192.168.1.65 – 192.168.1.126  | 192.168.1.127     |
| 10               | 192.168.1.128/26 | 255.255.255.192 | 192.168.1.129 – 192.168.1.190 | 192.168.1.191     |
| 11               | 192.168.1.192/26 | 255.255.255.192 | 192.168.1.193 – 192.168.1.254 | 192.168.1.255     |


**Bước 5**: Thao tác này tạo ra bốn mạng con, mỗi mạng hỗ trợ tối đa 62 máy, đồng thời vẫn đảm bảo tính hiệu quả của sơ đồ địa chỉ tổng thể. Phần _hostid_ được chia thành phần _subnetid_ và phần host.



![Image](assets/fr/016.webp)



Nguyên lý cơ bản của việc chia mạng con này vẫn không thể thiếu trong kỹ thuật mạng hiện đại, cho phép phân bổ IP chính xác, kiểm soát lưu lượng tốt hơn, cô lập phân đoạn mạnh mẽ và quản lý mạng có khả năng mở rộng.



### Địa chỉ CIDR


Vào đầu những năm 1990, khi Internet lan rộng nhanh chóng trong các doanh nghiệp và tổ chức, hệ thống địa chỉ IP truyền thống dựa trên các lớp (A, B, C) bắt đầu cho thấy những hạn chế của nó.

Cấu trúc cứng nhắc của nó dẫn đến lãng phí đáng kể địa chỉ IP và làm cho các bảng định tuyến ngày càng lớn, phức tạp và khó bảo trì.

Để giải quyết những vấn đề này, Address đã giới thiệu một phương pháp linh hoạt và hiệu quả hơn: **CIDR** (_Định tuyến liên miền không phân lớp_). CIDR đã dần trở thành tiêu chuẩn, thay thế phần lớn hệ thống dựa trên phân lớp cũ.


Ý tưởng cốt lõi đằng sau CIDR là khả năng nhóm nhiều mạng liền kề, đặc biệt là các khối Lớp C, thành một đơn vị logic duy nhất gọi là **siêu mạng** (_supernet_). Với sự tổng hợp này, một mục duy nhất trong bảng định tuyến có thể đại diện cho nhiều mạng con, giúp giảm số lượng tuyến đường mà bộ định tuyến cần xử lý và cải thiện hiệu suất của chúng.


Trong khi ban đầu, mạng Lớp C có nhu cầu tổng hợp lớn nhất do dung lượng nhỏ hơn, nguyên tắc này cũng đã được áp dụng cho Mạng Lớp B và về mặt lý thuyết, thậm chí cả Mạng Lớp A, mặc dù mạng Lớp A ít bị ảnh hưởng hơn nhờ phạm vi Address lớn của chúng.


Với CIDR, khái niệm lớp cố định biến mất. Không gian Address được coi là một phạm vi liên tục có thể được chia nhỏ hoặc tổng hợp khi cần thiết. Các khối CIDR được định nghĩa bằng cách sử dụng mặt nạ mạng con không bị giới hạn bởi các lớp mặc định A, B hoặc C. Một khối CIDR có thể đại diện cho một mạng đơn lẻ hoặc một tập hợp các mạng con liền kề chia sẻ cùng một tiền tố.


Khối CIDR được viết theo định dạng "Address/prefix", trong đó số sau dấu gạch chéo cho biết số bit tạo nên phần mạng. Ví dụ: /17 nghĩa là 17 bit đầu tiên xác định mạng, trong khi 15 bit còn lại xác định máy chủ.


Ví dụ:

Khối /17 chứa 2^(32-17) địa chỉ, do đó tổng cộng 2^15 = 32.768 địa chỉ. Trừ đi hai địa chỉ dành riêng (mạng và phát sóng), còn lại 32.766 địa chỉ máy chủ khả dụng. Điều này cho phép quản trị viên mạng định cỡ chính xác các mạng con của mình để phù hợp với nhu cầu thực tế, tránh lãng phí không cần thiết.


Để giúp bạn hiểu rõ hơn về kích thước CIDR, dưới đây là bảng các tiền tố phổ biến cùng mặt nạ mạng con tương đương và địa chỉ có thể sử dụng:


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


**LƯU Ý**: Trước đây, RFC 950 không khuyến khích sử dụng subnet zero, chủ yếu để tránh nhầm lẫn trong định tuyến. Hạn chế này đã trở nên lỗi thời với RFC 1878, phiên bản cho phép sử dụng hoàn toàn. Hạn chế cũ chủ yếu là do không tương thích với phần cứng cũ không thể xử lý CIDR chính xác. Thiết bị hiện đại không gặp vấn đề tương tự.


Ví dụ, mạng con **1.0.0.0** với mặt nạ mạng con **255.255.0.0** trước đây không rõ ràng với mã định danh mạng lớp A, nhưng giờ đây hoàn toàn hợp lệ và có thể sử dụng được.


**MẸO**: Để tính toán mạng con không lỗi và chuyển đổi nhanh chóng địa chỉ sang ký hiệu CIDR, có những công cụ tiện dụng như ***ipcalc***. "Máy tính mạng" này hiển thị rõ ràng các phân tích Address, phạm vi khả dụng và các mặt nạ liên quan, lý tưởng cho cả quản trị viên và sinh viên đang học CIDR.


```shell
sudo apt install ipcalc
```


https://planb.network/tutorials/computer-security/communication/angry-ip-scanner-47f7c943-53b7-4098-b167-4cec8e747b5d

## Giao thức TCP


<chapterId>860bf7d5-a502-4d10-a12c-9827f6c2d393</chapterId>



**Giao thức TCP** (_Giao thức Điều khiển Truyền_) đóng vai trò trung tâm trong TRANSPORT Layer của mô hình TCP/IP. Nó hoạt động như một cầu nối giữa các ứng dụng và Internet Layer, đảm bảo việc truyền dữ liệu đáng tin cậy giữa hai máy tính ở xa.

Trong khi giao thức IP chỉ gửi các gói tin mà không đảm bảo việc phân phối hoặc thứ tự, TCP đảm bảo tính toàn vẹn và nhất quán của luồng dữ liệu, truyền dữ liệu không bị mất mát, theo đúng thứ tự và không trùng lặp.


Trách nhiệm chính của TCP bao gồm:


- Sắp xếp lại các phân đoạn đã nhận;
- Theo dõi luồng dữ liệu để tránh tắc nghẽn;
- Chia hoặc lắp ráp lại các khối dữ liệu thành các đơn vị phù hợp (phân đoạn);
- Quản lý việc thiết lập và chấm dứt kết nối giữa hai đầu của giao tiếp.


TCP là một giao thức hướng kết nối, nghĩa là nó thiết lập một mối quan hệ rõ ràng, liên tục giữa máy khách và máy chủ. Để làm được điều này, nó sử dụng **số thứ tự** và **xác nhận**: với mỗi phân đoạn được gửi đi, một mã định danh duy nhất được gán để máy nhận có thể kiểm tra cả thứ tự và tính toàn vẹn của dữ liệu. Sau đó, máy nhận trả về một phân đoạn xác nhận với **cờ ACK** được đặt thành 1, xác nhận đã nhận và chỉ ra số thứ tự dự kiến tiếp theo.



![Image](assets/fr/018.webp)



Để cải thiện độ tin cậy, TCP sử dụng bộ đếm thời gian: sau khi một phân đoạn được gửi đi, quá trình đếm ngược sẽ bắt đầu. Nếu không nhận được xác nhận trong khoảng thời gian chờ, bên gửi sẽ tự động truyền lại phân đoạn, giả định rằng nó đã bị mất trong quá trình truyền tải. Cơ chế truyền lại tự động này bù đắp cho những tổn thất vốn có của mạng IP, có thể xảy ra trong trường hợp tắc nghẽn, lỗi định tuyến hoặc lỗi phần cứng.



![Image](assets/fr/019.webp)



TCP có khả năng phát hiện và xử lý các bản sao. Nếu một phân đoạn được truyền lại đến nhưng bản gốc cũng xuất hiện, bên nhận sẽ sử dụng số thứ tự để xác định bản sao và chỉ giữ lại bản sao chính xác, loại bỏ mọi sự mơ hồ.


Để quy trình này hoạt động, cả hai máy phải cùng hiểu rõ về số thứ tự ban đầu của chúng. Điều này được đảm bảo bằng cách tuân theo một quy trình kết nối nghiêm ngặt: một mặt, **máy chủ** lắng nghe trên một cổng cụ thể, chờ yêu cầu đến (chế độ thụ động); mặt khác, **máy khách** chủ động khởi tạo kết nối bằng cách gửi yêu cầu đến máy chủ trên cùng một cổng dịch vụ.


**LƯU Ý**: "Cổng" là một mã định danh số (từ 0 đến 65.535) được gán cho một ứng dụng mạng trên máy tính. Mã này được sử dụng để phân biệt nhiều dịch vụ chạy đồng thời trên cùng một địa chỉ IP Address. Khi máy khách gửi dữ liệu, nó sẽ chỉ định số cổng để hệ điều hành của máy chủ biết chương trình nào sẽ nhận dữ liệu (ví dụ: 80 cho HTTP, 443 cho HTTPS, 25 cho SMTP). Cổng hoạt động như những cánh cửa chuyên dụng, điều hướng lưu lượng ra vào, ngăn ngừa nhầm lẫn giữa các dịch vụ và cho phép kiểm soát truy cập chi tiết thông qua tường lửa hoặc các quy tắc lọc.


Đồng bộ hóa trình tự Exchange dựa trên cơ chế bắt tay ba bước nổi tiếng, tương tự như cách hai người chào nhau để thiết lập liên lạc. Giai đoạn khởi tạo này, đảm bảo độ tin cậy của TCP, diễn ra trong 3 giai đoạn:

1. **SYN:** Máy khách gửi một phân đoạn đồng bộ hóa ban đầu (**SYN**) với cờ thích hợp được đặt và số thứ tự ban đầu (ví dụ: C);

2. **SYN-ACK:** Máy chủ nhận phản hồi bằng một đoạn xác nhận (**SYN-ACK**), xác nhận số thứ tự của máy khách và cung cấp số thứ tự ban đầu của riêng nó;

3. **ACK:** Máy khách gửi xác nhận cuối cùng (**ACK**) xác nhận đã nhận được số thứ tự của máy chủ, hoàn tất quá trình đồng bộ hóa. Cờ SYN hiện đã bị vô hiệu hóa và cờ ACK vẫn được đặt, cho biết kết nối đã được thiết lập.



![Image](assets/fr/020.webp)



Giao thức Exchange này đảm bảo cả hai bên chia sẻ cùng một cơ sở đánh số trước khi truyền dữ liệu tải trọng. Sau khi quá trình đồng bộ hóa này hoàn tất, phiên sẽ được mở: các phân đoạn giờ đây có thể di chuyển theo cả hai hướng, mỗi phân đoạn đều được xác nhận khi nhận được, đảm bảo độ tin cậy tối đa của luồng dữ liệu.


***Cơ chế bắt tay ba bước*** này chỉ liên quan đến việc thiết lập kết nối. Để đóng, TCP sử dụng *cơ chế bắt tay bốn bước*: FIN → ACK → FIN → ACK, đảm bảo không có phân đoạn nào bị mất trong quá trình truyền tải trước khi kết nối được giải phóng hoàn toàn.


Mặc dù được thiết kế để đảm bảo độ bền và độ tin cậy, quy trình này cũng làm phát sinh các lỗ hổng dễ bị khai thác. Ví dụ, các cuộc tấn công như **IP Spoofing** nhằm mục đích bỏ qua hoặc làm hỏng mối quan hệ tin cậy này bằng cách giả mạo máy được ủy quyền thông qua số thứ tự giả mạo, tạo ra một lỗ hổng cho phép chặn hoặc thao túng luồng dữ liệu.


Để hạn chế rủi ro bị chiếm đoạt đồng bộ hóa chuỗi và quản lý tải mạng, giao thức TCP sử dụng kỹ thuật quản lý luồng được gọi là "**_Cửa sổ trượt_**". Hệ thống này điều chỉnh lượng dữ liệu có thể được gửi mà không yêu cầu xác nhận ngay lập tức cho mỗi phân đoạn, do đó giảm thiểu tình trạng quá tải không cần thiết trên mạng trong khi vẫn duy trì độ tin cậy tốt.


Trên thực tế, cửa sổ trượt xác định một dãy số thứ tự có thể luân chuyển tự do giữa bên gửi và bên nhận mà không cần xác nhận từng phân đoạn riêng lẻ. Khi hệ thống gửi nhận được xác nhận, cửa sổ sẽ "trượt": nó trượt sang phải để tạo khoảng trống cho các phân đoạn mới được gửi. Kích thước của cửa sổ này (rất quan trọng để tối ưu hóa thông lượng đồng thời tránh tắc nghẽn) được chỉ định trong trường "*Cửa sổ*" của tiêu đề TCP.


**Ví dụ**: nếu số thứ tự ban đầu là 3 và cửa sổ mở rộng đến thứ tự 5, các phân đoạn được đánh số từ 3 đến 5 có thể được gửi mà không cần chờ xác nhận riêng lẻ.



![Image](assets/fr/021.webp)



Kích thước của cửa sổ trượt không cố định; nó tự động điều chỉnh theo điều kiện mạng và khả năng xử lý của bộ thu. Nếu bộ thu có thể xử lý khối lượng dữ liệu lớn hơn, nó sẽ hiển thị điều này thông qua trường Cửa sổ, nhắc bộ gửi mở rộng cửa sổ. Ngược lại, trong trường hợp quá tải hoặc có nguy cơ bão hòa, bộ nhận có thể yêu cầu giảm kích thước cửa sổ, bộ gửi sẽ đợi cho đến khi cửa sổ di chuyển về phía trước để gửi thêm phân đoạn.


Giao thức cung cấp một quy trình đối xứng để đóng kết nối TCP nhằm đảm bảo việc tắt máy được thực hiện gọn gàng, có trật tự. Mỗi máy có thể khởi tạo việc đóng bằng cách gửi một phân đoạn với cờ **FIN** được đặt thành 1, báo hiệu ý định kết thúc giao tiếp. Sau đó, máy sẽ đợi cho đến khi tất cả các phân đoạn đang truyền tải được nhận và bỏ qua mọi dữ liệu tiếp theo.


Khi nhận được phân đoạn này, máy kia sẽ gửi một xác nhận, cũng được đánh dấu bằng cờ FIN. Sau đó, nó hoàn tất việc gửi bất kỳ dữ liệu nào còn lại trước khi thông báo cho ứng dụng cục bộ rằng kết nối đã bị đóng. Việc xác nhận kép này đảm bảo việc tắt máy diễn ra theo thứ tự và giảm thiểu rủi ro mất dữ liệu.


Việc quản lý chính xác này, kết hợp định tuyến linh hoạt của IP với khả năng kiểm soát chặt chẽ của TCP, thường được minh họa bằng sơ đồ so sánh tốc độ của giao thức IP (hoạt động theo nguyên tắc **"cố gắng hết sức"**, không đảm bảo về khả năng phân phối) với độ tin cậy của giao thức TCP (quản lý việc truyền tải thông qua xác nhận và trình tự được thương lượng).



![Image](assets/fr/022.webp)



Tuy nhiên, trong một số trường hợp, độ tin cậy tuyệt đối không phải là ưu tiên hàng đầu, mà là tốc độ và sự đơn giản. Điều này đúng với các ứng dụng như phát trực tiếp hoặc VoIP, vốn có thể chịu được một số mất mát gói tin mà không ảnh hưởng nghiêm trọng đến trải nghiệm người dùng. Trong những trường hợp như vậy, **UDP** (_Giao thức Datagram Người dùng_) được ưu tiên.


UDP hoạt động theo một nguyên lý hoàn toàn khác với TCP: nó **không kết nối**, nghĩa là không có mối quan hệ nào được thiết lập trước đó giữa người gửi và người nhận. Khi một máy gửi gói tin qua UDP, chúng được truyền một chiều; người nhận không gửi xác nhận, và người gửi không có xác nhận nào về việc tin nhắn đã đến. Tiêu đề UDP được thiết kế tối giản, chỉ chứa cổng nguồn, cổng đích, độ dài phân đoạn và giá trị tổng kiểm tra, không có cơ chế xác nhận hoặc kiểm soát trạng thái tích hợp. Như thường lệ, địa chỉ IP được chứa trong tiêu đề IP cơ bản.


A common analogy is that TCP is like a **phone call**, where a circuit is established, followed and controlled throughout the conversation. While, the UDP protocol is like **posting a mail**, where the sender slips a letter into a mailbox with no immediate proof of delivery or systematic feedback.


This complementarity between TCP and UDP enables modern networks to adapt to a variety of needs, choosing maximum reliability or prioritizing speed, depending on the application.



## Nguyên thủy dịch vụ


<chapterId>4480afb7-e950-4ccb-88fa-d132f9dc3479</chapterId>



### Kiến trúc phân lớp và tổ chức Exchange


Như chúng ta đã thấy, **dịch vụ** là triển khai cụ thể của các giao thức đã mô tả ở trên. Mặc dù mô hình TCP/IP khác với mô hình **OSI**, nhưng nó áp dụng cùng một phương pháp phân lớp: mỗi Layer được thiết kế để thực hiện một chức năng cụ thể và cung cấp **dịch vụ** cho Layer ngay phía trên nó, tạo nên một kiến trúc mô-đun, mạnh mẽ và dễ bảo trì.


Mỗi Layer được xây dựng dựa trên khả năng của lớp bên dưới, và ngược lại, cung cấp cho Layer lớp trên một Interface thống nhất để quản lý dữ liệu. Trong kiến trúc này, mỗi Layer đều có **cấu trúc dữ liệu** riêng, được xác định cẩn thận để đảm bảo khả năng tương thích hoàn hảo với các lớp khác. Khả năng tương thích này rất cần thiết cho việc truyền thông trơn tru, đáng tin cậy và rõ ràng từ điểm cuối này đến điểm cuối khác.


Có hai khía cạnh chính chi phối những trao đổi này:


- Góc nhìn thẳng đứng**: mối quan hệ giữa một Layer và Layer ở trên hoặc ở dưới nó (từ Layer N đến Layer N+1 và ngược lại).



![Image](assets/fr/023.webp)




- Góc nhìn ngang**: sự tương tác giữa các ứng dụng từ xa, tức là cuộc đối thoại giữa **máy khách** và **máy chủ**, theo cả hai hướng.



![Image](assets/fr/024.webp)



Kiến trúc phân lớp tuân theo nguyên tắc rằng mỗi Layer chỉ xử lý thông tin trong phạm vi của nó: cấu trúc dữ liệu, tiêu đề và cơ chế điều khiển khác nhau giữa các Layer, nhưng khi kết hợp lại, chúng tạo thành một hệ thống thống nhất, đảm bảo dữ liệu được định tuyến dần dần đến đích cuối cùng.


**Nhắc nhở**: Thuật ngữ cụ thể được sử dụng để mô tả các đơn vị dữ liệu được trao đổi giữa các lớp:


- tin nhắn** cho Ứng dụng Layer,
- phân đoạn** cho Giao thức vận chuyển Layer (TCP),
- datagram** cho Internet Layer (IP),
- khung** cho Network Access Layer.


Bảng dưới đây tóm tắt các thuật ngữ cho bối cảnh TCP và UDP:


| TCP/IP Layer         | Unit Name (TCP) | Unit Name (UDP) |
|----------------------|------------------|------------------|
| Application Layer    | Stream           | Message          |
| Transport Layer      | Segment          | Packet           |
| Internet Layer       | Datagram         | Datagram         |
| Network Access Layer | Frame            | Frame            |

### Các nguyên mẫu dịch vụ và đơn vị dữ liệu


Cốt lõi của hệ thống này là **các nguyên hàm dịch vụ**, hoạt động như các giao diện truyền thông. Các nguyên hàm này hoạt động giống như các bàn dịch vụ, lắng nghe trên các **cổng** cụ thể được dành riêng và cho phép các quy trình thiết lập, duy trì và chấm dứt các kết nối mạng một cách có kiểm soát. Trong khi các giao thức tổ chức định dạng và truyền dữ liệu qua mạng, thì **các dịch vụ và các nguyên hàm của chúng** mới là yếu tố tạo nên liên kết dọc giữa các lớp.


Bằng cách kết hợp khía cạnh ngang (giao tiếp giữa các ứng dụng phân tán) với khía cạnh dọc (tương tác nội bộ giữa các lớp), mô hình TCP/IP mang lại một kiến trúc hoàn chỉnh, có khả năng mở rộng. Việc chồng chéo hai góc nhìn này mang lại cái nhìn tổng quan rõ ràng về cách dữ liệu được trao đổi trong giao tiếp mạng có cấu trúc.



![Image](assets/fr/026.webp)



### Tóm tắt phần


Trong phần chính đầu tiên này, chúng ta đã khám phá kiến trúc cốt lõi chi phối việc cấu hình và vận hành các mạng kết nối Internet ngày nay. Kiến trúc này dựa trên mô hình **bốn Layer**, lấy cảm hứng từ mô hình OSI, và được xây dựng xung quanh bộ giao thức **TCP/IP**, xương sống của truyền thông hiện đại. Chúng ta đã thấy rằng TCP, với cách tiếp cận hướng kết nối, đảm bảo truyền tải dữ liệu đáng tin cậy, trong khi UDP, nhẹ hơn và nhanh hơn, được ưa chuộng hơn khi tốc độ quan trọng hơn độ tin cậy.


Hoạt động hiệu quả của mô hình này phụ thuộc vào việc triển khai các giao thức thông qua **các nguyên hàm dịch vụ**. Các giao thức này đảm bảo liên kết giữa các lớp, cho phép xử lý dữ liệu được điều chỉnh theo các yêu cầu cụ thể của từng cấp độ, từ vận chuyển đến ứng dụng, bao gồm cả truy cập Internet và mạng. Cách tiếp cận mô-đun này làm cho hệ thống vừa linh hoạt vừa mạnh mẽ.


Địa chỉ IP là một nền tảng khác của cơ sở hạ tầng này. Mỗi thiết bị được kết nối được xác định bằng một **IP Address** duy nhất, được lấy từ không gian Address được tổ chức thành các **lớp** (từ A đến E). Một số địa chỉ này được dành riêng cho các mục đích đặc biệt, chẳng hạn như vòng lặp cục bộ hoặc đa hướng, trong khi một số khác, được gọi là "địa chỉ riêng", không được định tuyến qua Internet mà không cần biên dịch (NAT). Phân loại này cho phép tổ chức mạng theo thứ bậc, logic.


Chúng tôi cũng đã xem xét khái niệm **mạng con**, cho phép chia các phân đoạn mạng để quản lý tài nguyên IP tốt hơn và tối ưu hóa luồng dữ liệu. Mặc dù việc chia nhỏ thủ công bằng mặt nạ mạng con vẫn là một nguyên tắc quan trọng, nhưng nó đã được hiện đại hóa phần lớn nhờ **CIDR** (Định tuyến Liên miền Không Phân lớp). Phương pháp này đã chuyển đổi cách quản lý Address bằng cách cho phép phân bổ dải IP linh hoạt và hợp lý hơn, đồng thời giảm kích thước của bảng định tuyến.


Bằng cách nắm vững các khái niệm này - lớp, giao thức, nguyên mẫu dịch vụ, địa chỉ và chia mạng con - bạn sẽ có được nền tảng vững chắc để hiểu cách thức hoạt động kỹ thuật của các mạng hiện đại và để cấu hình hiệu quả cơ sở hạ tầng mạng nhằm đáp ứng nhu cầu ngày nay.


Trong phần tiếp theo, chúng ta sẽ xem xét kỹ hơn về địa chỉ IPv4.



# Địa chỉ IPv4


<partId>83f3c3e5-378c-440f-a095-df210842efde</partId>



## Sử dụng IPv4


<chapterId>79e4dd18-446a-435b-9f25-c88a00f8bec6</chapterId>



Trong phần này, chúng ta sẽ đi sâu hơn và xem xét cách các địa chỉ **IPv4** thực sự được triển khai trong mạng lưới thực tế. Chúng ta sẽ phân tích định dạng, logic đằng sau chúng và cách chúng kết nối với các mạng quan trọng khác của Elements như **tên DNS**, **địa chỉ MAC**, **mạng con** và **kỹ thuật dịch**.


IP Address là một mã định danh số duy nhất được gán cho mỗi **Interface** mạng trên một thiết bị. Mã này cho phép định vị thiết bị này trong mạng và truy cập thiết bị để truyền dữ liệu. Ví dụ: bộ định tuyến, máy chủ, máy trạm, máy in mạng hoặc thậm chí camera giám sát đều có ít nhất một IP Address riêng. IP Address giúp việc định tuyến trở nên khả thi, tức là di chuyển các gói tin từ điểm A đến điểm B, ngay cả khi chúng ở cách xa nhau về mặt vật lý.


Địa chỉ IP có thể được chỉ định theo hai cách chính:


- Tĩnh**: Cài đặt thủ công trên thiết bị.
- Dynamic**: Được tự động gán theo yêu cầu bởi máy chủ DHCP (_Giao thức Cấu hình Máy chủ Động_). DHCP đơn giản hóa việc quản lý mạng, loại bỏ nhu cầu cấu hình thủ công đồng thời cho phép kiểm soát chính xác thông qua việc đặt chỗ và thời hạn thuê.


Địa chỉ IPv4 được viết theo định dạng 32 bit, chia thành bốn byte. Mỗi byte chứa 8 bit và biểu diễn một số thập phân từ 0 đến 255. 4 byte được phân cách bằng dấu chấm để tạo thành ký hiệu rõ ràng, dễ đọc.


ví dụ: Address 172.16.254.1_



![Image](assets/fr/027.webp)



Mỗi bit trong một byte đều có một giá trị (hay "trọng số"): bit bên trái (bit quan trọng nhất) có giá trị là 128, tiếp theo là 64, rồi đến 32, 16, 8, 4, 2 và 1 cho bit bên phải (bit ít quan trọng nhất). Theo cách này, việc ghi nhị phân được chuyển đổi sang thập phân bằng cách cộng đơn giản các trọng số đã thiết lập.


Bảng dưới đây minh họa sự tương ứng này:



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

Để chuyển đổi nhị phân sang thập phân, hãy cộng trọng số của các bit được đặt thành 1.


| Binary     | Decimal Value |
| ---------- | ------------- |
| `10101100` | 172           |
| `00010000` | 16            |
| `11111110` | 254           |
| `00000001` | 1             |

IP Address xác định một **mạng Interface** duy nhất, chứ không phải toàn bộ thiết bị. Bộ định tuyến hoặc tường lửa đa cổng có nhiều giao diện, mỗi giao diện có IP Address riêng. Một Interface thậm chí có thể có nhiều địa chỉ IP (ví dụ: để phục vụ nhiều mạng hoặc dịch vụ ảo).


Mỗi gói IP chứa hai địa chỉ IP trong phần tiêu đề:


- Nguồn Address (**người gửi**)
- Điểm đến Address (**máy thu**)

Bộ định tuyến đọc các địa chỉ này để tìm ra đường dẫn tốt nhất để gửi gói tin cho đến khi nó đến đích. Nếu không có các quy tắc định địa chỉ nghiêm ngặt, lưu lượng mạng sẽ không thể được định tuyến chính xác và việc kết nối mạng toàn cầu sẽ là bất khả thi.


IPv4 Address có hai phần:


- NetID**: xác định mạng
- HostID**: xác định một thiết bị trong mạng đó

**Subnet mask** xác định vị trí kết thúc của NetID và bắt đầu của HostID, chỉ định số bit thuộc về mỗi phần. NetID càng dài, số lượng mạng con có thể có càng lớn, nhưng số lượng máy chủ trên mỗi mạng con cũng giảm tương ứng.


Ban đầu, mạng IPv4 được chia thành năm **lớp**: (A, B, C, D và E). Mỗi lớp tương ứng với một dải NetID cụ thể và xác định một mức độ chi tiết cố định:


- Lớp A: mạng rất lớn với số lượng máy chủ lớn
- Lớp B: mạng cỡ trung bình
- Lớp C: mạng nhỏ
- Lớp D: địa chỉ dành riêng cho đa hướng (_multicast_)
- Lớp E: địa chỉ thử nghiệm, không được sử dụng cho địa chỉ thông thường



| Class | Leading Bits | First Byte Range | Default Subnet Mask | Purpose                          |
| ----- | ------------ | ---------------- | ------------------- | -------------------------------- |
| A     | 0            | 0 – 127          | 255.0.0.0           | Very large networks              |
| B     | 10           | 128 – 191        | 255.255.0.0         | Medium-sized networks            |
| C     | 110          | 192 – 223        | 255.255.255.0       | Small networks                   |
| D     | 1110         | 224 – 239        | N/A                 | Multicast addresses              |
| E     | 1111         | 240 – 255        | N/A                 | Experimental (not publicly used) |

Địa chỉ đặc biệt:


- Mạng Address**: Xác định chính mạng (được sử dụng trong bảng định tuyến).
- Phát sóng Address**: Gửi dữ liệu đến tất cả các thiết bị trong mạng con cùng một lúc (tất cả các bit HostID được đặt thành 1).


Các phạm vi sau đây được dành riêng cho mục đích sử dụng nội bộ:


- 10.0.0.0/8** (Lớp A riêng tư)
- 127.0.0.0/8** (vòng lặp cục bộ hoặc _loopback_)
- 172.16.0.0 đến 172.31.255.255** (lớp B riêng tư)
- 192.168.0.0 đến 192.168.255.255** (lớp C riêng tư)


Địa chỉ **127.0.0.1** và, nói chung hơn, toàn bộ dải 127.0.0.0/8 được sử dụng cho mục đích kiểm tra nội bộ: mọi yêu cầu được gửi đến địa chỉ này sẽ không bao giờ rời khỏi máy. Điều này hữu ích để kiểm tra xem dịch vụ mạng cục bộ có hoạt động hay không mà không cần sự can thiệp của mạng lưới rộng hơn.


Để tận dụng tốt hơn không gian Address, quản trị viên thường chia mạng thành các **mạng con** bằng cách sử dụng mặt nạ mạng con hoặc ký hiệu **CIDR** (_Classless Inter-Domain Routing_). CIDR cho phép quản lý chính xác hơn và giúp tránh lãng phí địa chỉ. Ngày nay, CIDR rất cần thiết để tinh chỉnh dải IP và giảm kích thước bảng định tuyến.


Trong các mạng hiện đại, địa chỉ IP thường được ghép nối với các mã định danh khác:



- tên miền** được đăng ký trong **DNS** (_Hệ thống tên miền_): Nó liên kết một số IP Address với một tên thân thiện với con người.
- MAC Address**: một mã định danh vật lý được khắc trên card mạng, được sử dụng cho việc truyền tải cục bộ (_Ethernet_). Khi một gói tin IP cần được truyền tải vật lý, bảng ARP sẽ so khớp IP Address với MAC Address của đích.


Để giải quyết tình trạng thiếu hụt IPv4 Address và tăng cường bảo mật cho Layer, các mạng thường sử dụng giao thức chuyển đổi Address (_NAT_). NAT cho phép nhiều thiết bị riêng tư chia sẻ một địa chỉ IP công cộng Address duy nhất khi truy cập Internet.


**Lưu ý**: Các công cụ trực tuyến và tích hợp sẵn của hệ điều hành, chẳng hạn như [máy tính Grenoble CRIC](http://cric.grenoble.cnrs.fr/Administrateurs/Outils/CalculMasque/), giúp việc tính toán mạng con và mặt nạ dễ dàng hơn nhiều.

Các tiện ích này giúp lập kế hoạch phân chia mạng một cách hiệu quả.


Tóm lại, Address vẫn là một chức năng thực tế để gửi cùng một thông điệp đến tất cả các thiết bị được kết nối với một phân đoạn: điều này đạt được bằng cách đặt tất cả các bit trong phần HostID thành 1 để tất cả các máy chủ đều được nhắm mục tiêu.



## Các loại IPv4 Address khác nhau


<chapterId>2adfad24-a90d-45b5-b808-3d2f6598bebf</chapterId>



Địa chỉ IPv4 được chia thành hai loại chính: địa chỉ công cộng, có thể truy cập trực tiếp trên Internet và địa chỉ riêng, dành cho mục đích sử dụng nội bộ trong mạng cục bộ.


Địa chỉ IPv4 Address công cộng là duy nhất trên toàn cầu và có thể định tuyến trên Internet. Địa chỉ này được cấp phát bởi các cơ quan chính thức và bắt buộc đối với các dịch vụ công cộng như trang web, máy chủ email hoặc cơ sở hạ tầng đám mây.

Tính duy nhất trên toàn thế giới của các địa chỉ này là điều cần thiết để tránh mọi xung đột hoặc va chạm định tuyến.


**IANA** (_Cơ quan Cấp phát Số hiệu Internet_), hoạt động dưới sự quản lý của **ICANN** (_Tổ chức Cấp phát Tên và Số hiệu Internet_), quản lý việc phân phối các dải IP này. Cụ thể, IANA chia không gian IPv4 thành 256 khối, mỗi khối có kích thước /8, theo ký hiệu CIDR. Mỗi khối đại diện cho hơn 16,7 triệu địa chỉ (2³² / 2⁸).


Các khối Address đơn hướng này được IANA ủy thác cho **Các Cơ quan Đăng ký Internet Khu vực** (RIR). Các RIR này chịu trách nhiệm phân phối lại địa chỉ ở cấp khu vực, tùy theo nhu cầu thực tế của các nhà cung cấp dịch vụ truy cập, công ty hoặc cơ quan quản lý. Không gian Address đơn hướng trải dài từ khối **1/8 đến 223/8**, với các phần được dành riêng cho các mục đích sử dụng đặc biệt (nghiên cứu, lập tài liệu, thử nghiệm) hoặc được phân bổ trực tiếp cho mạng hoặc RIR để phân phối lại.


Để kiểm tra xem ai sở hữu địa chỉ IP công cộng Address, bạn có thể tham khảo cơ sở dữ liệu RIR bằng lệnh **whois** hoặc sử dụng giao diện web do mỗi cơ quan đăng ký cung cấp. Các công cụ này có thể được sử dụng để truy xuất Address về tổ chức hoặc nhà cung cấp đã khai báo nó.


Ngược lại, có các địa chỉ IPv4 riêng, một giải pháp thiết thực cho tình trạng thiếu hụt địa chỉ công cộng. Những địa chỉ này, không thể định tuyến trên Internet, được dành riêng cho các môi trường cục bộ: mạng doanh nghiệp, mạng LAN gia đình, trung tâm dữ liệu hoặc cụm máy tính. Chúng không phải là duy nhất trên toàn thế giới: nhiều mạng riêng có thể sử dụng lại cùng một dải IP mà không bị nhiễu, miễn là chúng được cách ly hoặc sử dụng thiết bị chuyển đổi mạng Address để truy cập Internet.


Để cho phép một thiết bị có địa chỉ IP riêng Address truy cập Internet, các mạng sử dụng NAT (Network Address Translation). NAT hoạt động bằng cách thay thế địa chỉ IP riêng Address bằng một địa chỉ IP công cộng, cho phép hàng chục (thậm chí hàng trăm) thiết bị cùng chia sẻ một địa chỉ IP công cộng Address. Phương pháp này tối ưu hóa việc sử dụng không gian IPv4 và cũng bổ sung thêm một Layer bảo mật bằng cách ẩn cấu trúc mạng nội bộ.


Một danh mục đặc biệt khác là địa chỉ **không xác định**. Ký hiệu IPv4 **0.0.0.0** hoặc phiên bản IPv6 của nó **::/128** có nghĩa là "không có Address cụ thể". Address như vậy không hợp lệ làm đích Address mạng, nhưng nó có thể được máy chủ sử dụng cục bộ để chỉ định "tất cả các giao diện" hoặc "chưa có Address nào được gán". Điều này phổ biến trong DHCP động Assignment hoặc để lắng nghe trên tất cả các giao diện máy chủ.


IPv6 cũng hỗ trợ địa chỉ riêng tư, nhưng tiêu chuẩn thường khuyến nghị địa chỉ công khai để tránh chồng chéo nhiều lớp NAT. Địa chỉ **site-local** (_site-local_) của khối **fec0::/10** đã bị loại bỏ trong **RFC 3879** vì lý do nhất quán và bảo mật. Chúng được thay thế bằng Địa chỉ cục bộ duy nhất** (_ULA_) nằm trong khối **fc00::/7**. ULA cho phép tạo các mạng IPv6 riêng tư với định tuyến nội bộ rõ ràng, sử dụng mã định danh 40 bit được tạo ngẫu nhiên để đảm bảo tính duy nhất cục bộ.


Sự cạn kiệt IPv4 đã được chính thức xác nhận vào năm 2011. Để kéo dài tuổi thọ của nó, cộng đồng Internet đã áp dụng một số chiến lược sau:


- Di chuyển dần dần sang **IPv6**
- Sử dụng rộng rãi **NAT**
- Chính sách phân bổ chặt chẽ hơn từ RIR, yêu cầu phải có sự giải trình và quản lý chính xác nhu cầu Address
- Các công ty thu hồi các khối Address chưa sử dụng hoặc tự nguyện trả lại


Những biện pháp này cho thấy rằng việc phân phối địa chỉ IP không chỉ là một thách thức về mặt kỹ thuật mà còn là vấn đề quản trị toàn cầu, đóng vai trò trung tâm trong sự phát triển liên tục của Internet.



## DNS, một thư mục Address


<chapterId>511244ec-ba43-44ac-b4c3-b41579a15cff</chapterId>



Thành thật mà nói, con người không giỏi ghi nhớ những chuỗi số dài, dù là nhị phân hay thập phân. Thách thức này càng trở nên lớn hơn với địa chỉ IP, vốn có thể phức tạp và một địa chỉ IP duy nhất đôi khi có thể che giấu nhiều địa chỉ, đặc biệt là khi sử dụng các kỹ thuật như NAT hoặc lưu trữ ảo.


Để đơn giản hóa mọi việc, Ứng dụng Layer sử dụng một hệ thống liên kết IP Address với một tên miền logic, dễ đọc. Đây chính là vai trò của **DNS** (*Hệ thống Tên Miền*), một thư mục phân tán, phân cấp, đồ sộ, giúp khớp tên miền dễ đọc với địa chỉ IP. Hệ thống này dựa trên một tập hợp các giao thức và dịch vụ. Phần mềm máy chủ DNS được sử dụng rộng rãi nhất là **BIND** (_Berkeley Internet Name Domain_), một gói phần mềm mã nguồn mở tham chiếu đến phần lớn cơ sở hạ tầng DNS của Internet.


Ý tưởng cốt lõi đằng sau DNS rất đơn giản: đối với bất kỳ dịch vụ được kết nối nào, dù là trang web, máy chủ thư hay dịch vụ mạng khác, đều có một bản ghi ánh xạ tên miền với một hoặc nhiều địa chỉ IP. Điều này hoạt động theo hai hướng:


- Giải quyết chuyển tiếp: dịch tên thành IP Address.
- Giải pháp đảo ngược: tìm tên miền liên quan đến IP Address nhất định.

Điều này giúp con người có thể sử dụng địa chỉ mạng trong khi vẫn đảm bảo độ chính xác mà bộ định tuyến cần để di chuyển dữ liệu một cách chính xác.


Tên miền luôn được cấu trúc theo thứ bậc, mỗi cấp được phân cách bằng một dấu chấm: tên đầy đủ được gọi là **FQDN** (Tên miền đủ điều kiện). Phần ngoài cùng bên phải là **TLD** (Tên miền cấp cao nhất) chẳng hạn như `.com`, `.org` hoặc `.fr`. Phần ngoài cùng bên trái chỉ định máy chủ, tức là máy hoặc dịch vụ cụ thể được liên kết với IP Address.


Hệ thống DNS được thiết kế dưới dạng **cây vùng**. **Vùng** là một phần của không gian tên miền được quản lý bởi một máy chủ DNS cụ thể. Một vùng có thể chứa nhiều **miền con**, và bản thân các miền con này có thể được phân quyền cho các vùng khác do các máy chủ khác nhau quản lý. Quản trị viên chịu trách nhiệm duy trì vùng của mình: xử lý cập nhật, phân quyền và quản lý chung.


Cấu trúc này không chỉ cho phép trỏ đến một tên miền chính (ví dụ: `example.com`) mà còn tinh chỉnh các bản ghi cho từng máy chủ riêng lẻ (`www`, `mail`, `ftp`, v.v.). Trong những ngày đầu của mạng, việc ánh xạ này được xử lý bằng các tệp tĩnh như (`/etc/hosts` trên các hệ thống Unix), nhưng phương pháp này nhanh chóng trở nên không thực tế đối với một Internet kết nối đang phát triển nhanh chóng.


Điều quan trọng cần hiểu là **máy chủ DNS** chỉ có thể phục vụ một phạm vi hạn chế. Ví dụ: máy chủ DNS nội bộ của một công ty có thể không thể truy cập trực tiếp từ Internet. Nếu DNS này không được cấu hình để chuyển tiếp truy vấn, hoặc không có mối quan hệ tin cậy với các máy chủ khác, một số truy vấn sẽ không thành công: cả tên miền lẫn địa chỉ IP Address đều không thể được phân giải bên ngoài vùng đã xác định.


DNS cũng đóng vai trò trong việc định tuyến email. Ví dụ: bản ghi **MX** (_Mail Exchange_) chỉ định các máy chủ email chịu trách nhiệm nhận email cho một tên miền nhất định. Những bản ghi này xác định mức độ ưu tiên (hệ số trọng số) và các giải pháp dự phòng. Tệp vùng của máy chủ DNS phải chứa bản ghi **SOA** (_Start Of Authority_), chỉ định máy chủ là nguồn thông tin chính thức cho vùng đó.


Nhờ cấu trúc phân cấp, phân tán, DNS vẫn là nền tảng của Internet, cho phép người dùng truy cập các dịch vụ thông qua tên miền rõ ràng, dễ nhớ thay vì địa chỉ IP kỹ thuật dài dòng.


Trong chương tiếp theo, chúng ta sẽ khám phá một khái niệm cơ bản khác: **Địa chỉ Ethernet**, còn được gọi là **địa chỉ MAC**, đảm bảo việc phân phối dữ liệu tại Layer vật lý của mạng cục bộ.



## Khám phá địa chỉ Ethernet và ARP


<chapterId>d02109f6-9bf9-4261-a8f9-e1aa4398b949</chapterId>



### Định nghĩa


Để giao thức định tuyến dữ liệu hoạt động đáng tin cậy và nhất quán, cần có một thành phần quan trọng. Là con người, chúng ta có thể dễ dàng xác định một máy tính bằng địa chỉ IP Address hoặc bằng tên được truy xuất qua DNS. Tuy nhiên, máy tính phải có khả năng nhận dạng rõ ràng thiết bị đích để phân phối các gói tin. Để làm được điều này, nó dựa vào một mã định danh phần cứng cụ thể, được mạng Interface của nó sử dụng trực tiếp: MAC Address (Media Access Control).


**Lưu ý**: Điều này không liên quan gì đến "Address vật lý" trong kiến trúc bộ nhớ. Trong điện toán, Address bộ nhớ vật lý đề cập đến một vị trí cụ thể trên bus bộ nhớ, trái ngược với Address ảo do hệ điều hành quản lý. Ngược lại, Address MAC chỉ liên quan chặt chẽ đến phần cứng mạng.


MAC Address được nhà sản xuất thiết bị gán cố định và duy nhất. MAC Address nhận dạng rõ ràng card mạng, cho dù đó là máy tính, điện thoại thông minh, máy in hay bất kỳ thiết bị được kết nối nào khác. Không giống như IP Address, có thể thay đổi linh hoạt (thông qua máy chủ DHCP hoặc cấu hình thủ công), MAC Address thường giữ nguyên trong suốt vòng đời của thiết bị, trừ khi bị thay đổi một cách có chủ đích.


Mỗi mạng Interface, dù có dây hay không dây, đều có địa chỉ MAC riêng Address. Địa chỉ Address này được sử dụng trong liên kết dữ liệu Layer (Layer 2 của mô hình OSI) để chèn và quản lý phần cứng Address trong mỗi khung mạng được trao đổi. Địa chỉ này đôi khi được gọi là _địa chỉ Ethernet_ hoặc _UAA_ (_Địa chỉ được quản lý chung_). Được chuẩn hóa trên độ dài 48 bit, hay 6 byte, địa chỉ này được viết dưới dạng thập lục phân, thường ở dạng các byte được phân tách bằng dấu `:` hoặc `-`.


Ví dụ: `5A:BC:17:A2:AF:15`


Trong cấu trúc này, ba byte đầu tiên xác định nhà sản xuất card mạng: được gọi là **OUI** (Mã định danh duy nhất về mặt tổ chức*). Các tiền tố này, do IEEE chỉ định, cũng được sử dụng trong các sơ đồ định địa chỉ phần cứng khác, chẳng hạn như Bluetooth và LLDP, để đảm bảo tính duy nhất trên toàn thế giới.


### Thay đổi MAC Address (MAC Spoofing)


Về lý thuyết, MAC Address được thiết kế để duy trì trạng thái cố định, nhưng có nhiều cách để sửa đổi nó, đặc biệt là để đáp ứng các nhu cầu cụ thể hoặc để vượt qua một số hạn chế nhất định. Thao tác này, thường được gọi là _giả mạo MAC_, bao gồm việc thay thế Address phần cứng ban đầu bằng một giá trị khác, được xác định ở cấp độ phần mềm. Một số hệ điều hành hỗ trợ việc sửa đổi này, đặc biệt khi Ethernet Address thực tế không được trình điều khiển sử dụng trực tiếp.


Lý do cho sự thay đổi này rất đa dạng. Có thể là do một ứng dụng cụ thể cần một Ethernet Address cụ thể để hoạt động chính xác, hoặc để giải quyết xung đột địa chỉ giống hệt nhau giữa hai thiết bị chia sẻ cùng một mạng cục bộ.


Việc thay đổi địa chỉ MAC Address cũng có thể được thúc đẩy bởi các cân nhắc về quyền riêng tư: bằng cách ẩn mã định danh duy nhất được khắc trên thẻ, người dùng giảm khả năng thiết bị của họ bị theo dõi bởi các mạng lưới hoặc dịch vụ giám sát. Tuy nhiên, việc này không phải là không có hậu quả. Việc thay đổi địa chỉ MAC Address có thể làm gián đoạn một số thiết bị lọc hoặc yêu cầu phải cấu hình lại tường lửa để cấp quyền cho phần cứng mới.


Một số mạng, đặc biệt là Wi-Fi, sử dụng bộ lọc MAC Address để chỉ cho phép các thiết bị có địa chỉ được phê duyệt. Mặc dù điều này bổ sung một mức độ kiểm soát cơ bản, nhưng bản thân nó không an toàn. Kẻ tấn công có thể chiếm được một MAC Address hợp lệ đã được ủy quyền trên mạng và sao chép nó để vượt qua các hạn chế. Vì lý do này, bộ lọc MAC nên luôn được kết hợp với các biện pháp bảo mật mạnh hơn.


### Giao tiếp MAC/IP


Để mạng cục bộ hoạt động hiệu quả, cần phải có sự ánh xạ rõ ràng giữa địa chỉ vật lý (địa chỉ MAC) và địa chỉ logic (địa chỉ IP). Nếu không có liên kết này, máy tính có thể biết địa chỉ IP Address của đích đến nhưng sẽ không biết cách gửi dữ liệu vật lý đến đích đó trên mạng cục bộ.

Việc ánh xạ này được xử lý tự động bởi ARP (_Giao thức phân giải địa chỉ_).


Trên thực tế, khi người dùng muốn biết địa chỉ MAC Address tương ứng với một địa chỉ IP cụ thể của Address, người dùng có thể sử dụng tiện ích `arp`. Công cụ này sẽ kiểm tra bảng ARP cục bộ của máy để hiển thị các kết quả khớp đã biết giữa địa chỉ IP và địa chỉ MAC trên mạng cục bộ. Bằng cách này, có thể nhanh chóng xác minh liên kết hiệu quả giữa lớp logic và lớp vật lý.


Ví dụ thực tế: nếu bạn muốn kiểm tra card mạng nào tương ứng với IP Address `192.168.1.5`, hãy sử dụng lệnh sau:


```bash
arp –a 192.168.1.5
```


Đầu ra sẽ hiển thị Address vật lý (MAC) liên quan, bản chất của đầu vào (tĩnh hoặc động) và Interface liên quan.


```
Interface: 192.168.1.5 --- 0x5
IP Address            MAC Address                Type
192.168.1.5           00:54:BC:17:14:6E          D
```


Điều quan trọng cần nhớ là MAC Address và IP Address là hai mã định danh hoàn toàn khác nhau, nhưng lại bổ sung chặt chẽ cho nhau. MAC Address được nhà sản xuất khắc riêng vào mỗi mạng Interface và được sử dụng để nhận dạng vật lý thiết bị trên mạng cục bộ. Mặt khác, IP Address là một Address logic được gán động hoặc tĩnh, cho phép máy tính tham gia các gói tin mạng IP và Exchange bên ngoài mạng cục bộ của nó.



- Ví dụ trực quan về MAC Address:


![Image](assets/fr/032.webp)




- Ví dụ trực quan về IP Address:


![Image](assets/fr/027.webp)



Trong môi trường doanh nghiệp, hai cấp địa chỉ này không thể hoạt động riêng biệt. Ví dụ: khi máy chủ DHCP tự động gán địa chỉ IP Address, địa chỉ MAC Address của thiết bị được sử dụng làm điểm khởi đầu. Máy tính gửi yêu cầu phát sóng DHCP chứa địa chỉ MAC Address của nó để máy chủ có thể gán địa chỉ IP Address khả dụng cho đúng thiết bị. Nếu không có nhận dạng phần cứng này, máy chủ DHCP sẽ không biết nên phân phối Address đến thiết bị nào.


Do đó, giao thức ARP rất cơ bản: nó cung cấp liên kết giữa địa chỉ IP và địa chỉ vật lý, cho phép máy tính dịch một đích đến logic thành đích đến vật lý thực tế. Khi một máy tính cần gửi một gói tin đến một máy tính khác trong cùng mạng, trước tiên nó sẽ tham khảo bảng ARP của máy tính đó để kiểm tra xem địa chỉ MAC Address của máy nhận đã được biết hay chưa. Nếu chưa, nó sẽ phát một yêu cầu ARP đến tất cả các máy chủ trong mạng cục bộ. Máy tính nào nhận ra địa chỉ IP đích Address trong yêu cầu này sẽ phản hồi bằng cách chỉ định địa chỉ MAC Address của nó. Sau đó, máy gửi sẽ ghi cặp IP/MAC này vào bộ nhớ đệm ARP của mình để tránh phải lặp lại thao tác mỗi khi yêu cầu được gửi đi.


Bảng ARP này hoạt động như một thư mục ánh xạ thu nhỏ, được cập nhật động theo cách tương tự như cách DNS liên kết tên miền với địa chỉ IP. Nếu không có ARP, Exchange cục bộ sẽ không thể hoạt động, vì liên kết dữ liệu Layer cần biết địa chỉ MAC Address để đóng gói các khung Ethernet một cách chính xác.


Ngược lại, giao thức RARP (_Giao thức Giải quyết Address Ngược_) được thiết kế cho tình huống ngược lại: cho phép một máy chỉ biết địa chỉ MAC Address của nó khám phá ra địa chỉ IP Address của nó. Điều này thường xảy ra với các máy trạm cũ không có đĩa Hard cục bộ, phải khởi động qua mạng và yêu cầu địa chỉ IP Address. RARP cuối cùng đã được thay thế bằng **BOOTP** và sau đó là **DHCP**, linh hoạt và tự động hơn.


Các giao thức liên kết này đóng vai trò quan trọng trong định tuyến. Về cơ bản, bộ định tuyến là một máy tính có nhiều giao diện mạng, kết nối các phân đoạn mạng khác nhau. Khi bộ định tuyến nhận được một khung dữ liệu, nó sẽ xử lý khung dữ liệu đó để trích xuất gói tin IP và kiểm tra tiêu đề IP để xác định đích đến. Nếu đích đến nằm trên một mạng được kết nối trực tiếp, gói tin sẽ được gửi ngay sau khi cập nhật tiêu đề. Nếu đích đến thuộc một mạng khác, bộ định tuyến sẽ tham khảo bảng định tuyến của mình để xác định đường dẫn tốt nhất, hay _next hop_, đến đích.


Điều này chia tuyến đường thành các đoạn ngắn hơn, dễ quản lý hơn. Mỗi bộ định tuyến trung gian chỉ biết bước tiếp theo, chứ không nhất thiết biết đích đến cuối cùng.


**Lưu ý:** Việc gửi trực tiếp diễn ra khi người gửi và người nhận ở trên cùng một mạng vật lý. Nếu không, việc gửi sẽ diễn ra gián tiếp và đi qua một hoặc nhiều bộ định tuyến.


Bảng định tuyến, được quản lý thủ công (định tuyến tĩnh) hoặc động (định tuyến động), chứa thông tin cần thiết để quyết định tuyến đường nào nên đi. Trong các mạng nhỏ, cấu hình tĩnh là đủ. Trong các cơ sở hạ tầng lớn hơn, định tuyến động là điều cần thiết để tự động điều chỉnh tuyến đường khi cấu trúc mạng thay đổi hoặc một liên kết bị sập.


Bảng định tuyến hoạt động như một bảng ánh xạ giữa các địa chỉ IP đích và các cổng tiếp theo. Nó thường lưu trữ mã định danh mạng (_network ID_) thay vì từng máy chủ Address riêng lẻ, giúp giảm đáng kể kích thước của nó.


| Destination Address | Next-Hop Router Address | Interface |
| ------------------- | ----------------------- | --------- |

Sử dụng các mục nhập này, bộ định tuyến có thể nhanh chóng xác định Interface nào và nút nào mà mỗi gói dữ liệu nên được gửi. Kết hợp với ARP để phân giải các địa chỉ MAC trùng khớp, điều này đảm bảo truyền dữ liệu hiệu quả và đáng tin cậy trên toàn mạng.


Cuối cùng, các giao thức định tuyến động bao gồm các tiêu chuẩn như RIP (_Routing Information Protocol_), dựa trên thuật toán khoảng cách, và OSPF (_Open Shortest Path First_), tính toán các đường dẫn ngắn nhất trong cấu trúc mạng phức tạp. Các giao thức này liên tục được cập nhật để tối ưu hóa tuyến đường, giảm chi phí truyền tải và cải thiện khả năng phục hồi khi xảy ra sự cố ngừng hoạt động hoặc tắc nghẽn.



## NAT: Bản dịch Address


<chapterId>4f984d5d-f2e0-4faf-b703-ff315f32cef4</chapterId>



### Sự định nghĩa


NAT (Network Address Translation_) là một kỹ thuật được phát triển để giải quyết vấn đề cạn kiệt dần địa chỉ IPv4 khả dụng. Được thiết kế như một giải pháp tạm thời trước khi IPv6 được áp dụng rộng rãi, NAT cho phép các công ty và cá nhân tiếp tục kết nối số lượng lớn máy tính trong khi chỉ sử dụng một bộ địa chỉ IP công cộng hạn chế.


**Lưu ý quan trọng:** Việc chuyển đổi từ IPv4 sang IPv6 về mặt lý thuyết sẽ giải quyết vấn đề cạn kiệt bằng cách mở rộng không gian Address từ 32 bit lên 128 bit, cung cấp số lượng địa chỉ gần như không giới hạn (2^128). Tuy nhiên, trên thực tế, quá trình chuyển đổi vẫn chưa hoàn tất, và NAT vẫn được sử dụng rộng rãi cho đến ngày nay.


Nguyên lý đằng sau NAT rất đơn giản nhưng hiệu quả cao: thay vì gán một địa chỉ IP công cộng duy nhất Address cho mọi thiết bị trong mạng nội bộ, một địa chỉ Address có thể định tuyến duy nhất (hoặc một nhóm địa chỉ nhỏ) sẽ được sử dụng cho tất cả các thiết bị riêng. Cổng NAT, thường được tích hợp vào bộ định tuyến hoặc tường lửa, sau đó sẽ tự động dịch địa chỉ IP Address nội bộ cùng với thông tin cần thiết để định tuyến lưu lượng truy cập chính xác ra thế giới bên ngoài, và đảm bảo phản hồi được trả về cho người gửi ban đầu.


Cách tiếp cận này mang lại lợi ích tức thì: nó ẩn hoàn toàn kiến trúc mạng nội bộ. Đối với người quan sát bên ngoài, tất cả các yêu cầu từ máy trạm, máy chủ hoặc máy in dường như đều đến từ cùng một danh tính công khai. Các địa chỉ riêng, thường được lấy từ các dải địa chỉ được bảo lưu (ví dụ: 192.168.x.x hoặc 10.x.x.x), vẫn ẩn khỏi Internet.


Ngoài việc giải quyết tình trạng khan hiếm IPv4, NAT còn tăng cường bảo mật bằng cách tạo ra một rào cản logic đầu tiên giữa mạng nội bộ và mạng công cộng. Các giao tiếp đến không mong muốn sẽ tự động bị chặn, vì chỉ những kết nối được khởi tạo từ bên trong mạng mới được hưởng lợi từ quá trình chuyển đổi cần thiết để nhận phản hồi.



![Image](assets/fr/035.webp)



### Các loại bản dịch


NAT có thể được triển khai theo nhiều cách khác nhau tùy theo nhu cầu cụ thể. Hai chế độ hoạt động chính là dịch chuyển tĩnh và dịch chuyển động.


**Chuyển đổi tĩnh** tạo ra một ánh xạ cố định giữa địa chỉ IP riêng Address và địa chỉ IP công cộng Address. Mỗi máy nội bộ được liên kết cố định với địa chỉ IP công cộng Address chuyên dụng của nó. Ví dụ: một thiết bị nội bộ được cấu hình là 192.168.20.1 có thể được liên kết với địa chỉ Address có thể định tuyến 157.54.130.1. Khi một gói tin đi ra khỏi mạng cục bộ, bộ định tuyến sẽ thay thế địa chỉ Address nguồn của gói tin bằng địa chỉ Address công cộng và thực hiện thao tác ngược lại cho lưu lượng đến. Việc chuyển đổi hai chiều này hoàn toàn trong suốt với người dùng.


**Cảnh báo:** Mặc dù phương pháp này cô lập mạng nội bộ, nhưng nó không giải quyết được tình trạng thiếu hụt địa chỉ IP công cộng, vì bạn vẫn cần số lượng địa chỉ công cộng tương ứng với số lượng máy tính cần hiển thị. Do đó, chuyển đổi tĩnh chủ yếu được sử dụng khi một số tài nguyên nội bộ nhất định phải được truy cập từ bên ngoài (máy chủ web, máy chủ thư...).


**Chuyển đổi động**, mặt khác, sử dụng một nhóm địa chỉ IP công cộng. Khi một máy chủ nội bộ bắt đầu kết nối, bộ định tuyến sẽ tạm thời gán một trong những địa chỉ công cộng này cho Address riêng của máy chủ trong suốt phiên. Liên kết này là 1-1, nhưng chỉ mang tính tạm thời: khi kết nối kết thúc, Address công cộng sẽ khả dụng cho một thiết bị khác. Do đó, NAT động giảm số lượng địa chỉ công cộng cần thiết khi không phải tất cả các máy đều trực tuyến cùng một lúc, nhưng vẫn yêu cầu một khối địa chỉ bên ngoài ít nhất bằng số lượng kết nối đồng thời tối đa.


**Chuyển đổi cổng** (PAT), còn được gọi là *NAT overload* hoặc *IP masquerading*, tiến xa hơn một bước: tất cả các thiết bị riêng tư chia sẻ một địa chỉ IP công cộng duy nhất Address (hoặc một số lượng rất nhỏ). Để phân biệt các phiên, cổng không chỉ sửa đổi Address nguồn mà còn sửa đổi cả cổng nguồn. Cổng này lưu giữ một bảng liên kết mỗi cặp *(private Address, private port)* với một cặp *(public Address, public port)* duy nhất. Hình thức NAT này được sử dụng trong hầu hết các bộ định tuyến gia đình, cho phép hàng chục thiết bị (máy tính, điện thoại thông minh, thiết bị được kết nối, v.v.) chia sẻ cùng một địa chỉ IP công cộng Address, đồng thời duy trì kết nối liền mạch.


Do đó, NAT kéo dài tuổi thọ của IPv4, đồng thời bổ sung thêm một Layer giá trị về phân đoạn và bảo mật. Tuy nhiên, khi việc áp dụng IPv6 ngày càng tăng và không gian Address rộng lớn của nó được sử dụng rộng rãi hơn, vai trò của NAT có thể sẽ giảm sút, mặc dù về mặt tương thích và kiểm soát, nó vẫn sẽ được sử dụng trong một số môi trường để phân đoạn và lọc lưu lượng.


### Triển khai NAT


Để đảm bảo hoạt động chính xác của quá trình biên dịch Address, bộ định tuyến hoặc cổng NAT phải lưu giữ một bản ghi chính xác về các ánh xạ được thiết lập giữa mỗi Address riêng trên mạng nội bộ và Address công cộng mà nó sử dụng để giao tiếp với thế giới bên ngoài. Thông tin này được lưu trữ trong cái được gọi là "bảng biên dịch NAT", đóng vai trò trung tâm trong việc quản lý lưu lượng mạng.


Mỗi mục trong bảng này liên kết ít nhất một cặp: IP nội bộ Address của máy gửi và IP bên ngoài Address sẽ được hiển thị trên Internet. Khi một gói tin từ mạng riêng được gửi đến đích công cộng, bộ định tuyến NAT sẽ chặn khung, phân tích tiêu đề IP và TCP/UDP, sau đó thay thế Address nguồn riêng bằng Address công cộng của cổng. Trên đường trả về, cùng cổng đó sẽ bắt gói tin đến, kiểm tra bảng ánh xạ và thực hiện thao tác ngược lại để chuyển hướng luồng đến IP nội bộ Address ban đầu.


Nguyên lý dịch chuyển động này dựa trên việc quản lý bảng chính xác: mỗi mục nhập vẫn hợp lệ miễn là có lưu lượng truy cập đang hoạt động để xác minh. Sau một khoảng thời gian không hoạt động có thể cấu hình, mục nhập sẽ được xóa và có thể được sử dụng lại cho các kết nối mới.


_Ví dụ về bảng dịch NAT được đơn giản hóa:_


| Internal IP   | External IP    | Duration (sec) | Reusable? |
| ------------- | -------------- | -------------- | --------- |
| 10.101.10.20  | 193.48.100.174 | 1,200          | no        |
| 10.100.54.251 | 193.48.101.8   | 3,601          | yes       |
| 10.100.0.89   | 193.48.100.46  | 0              | no        |

Trong ví dụ này, nếu không có gói tin nào được chuyển qua cho mục nhập thứ hai trong hơn một giờ (3.600 giây), nó được đánh dấu là có thể sử dụng lại. Ngược lại, thời lượng bằng 0 biểu thị giao tiếp đang hoạt động, với ánh xạ bị khóa.


Mặc dù NAT hoạt động minh bạch cho hầu hết các mục đích sử dụng phổ biến (duyệt web, email, truyền tệp, v.v.), nhưng nó có thể tạo ra những thách thức bổ sung cho một số ứng dụng mạng nhất định. Một số công nghệ dựa trên việc trao đổi rõ ràng địa chỉ IP hoặc cổng trong gói tin. Sau khi đi qua cổng NAT, thông tin này trở nên không nhất quán.


Các ví dụ điển hình về hạn chế bao gồm:


- Các giao thức ngang hàng (P2P), yêu cầu kết nối trực tiếp giữa các thiết bị, bị cản trở bởi rào cản NAT, vì tất cả các máy nội bộ đều chia sẻ cùng một IP bên ngoài Address và không thể truy cập trực tiếp nếu không có cấu hình cụ thể (chẳng hạn như *chuyển tiếp cổng* hoặc UPnP);
- Giao thức IPSec, được sử dụng để bảo mật thông tin liên lạc mạng, mã hóa tiêu đề gói tin. Vì NAT phải sửa đổi các tiêu đề này để thay thế địa chỉ IP, nên việc mã hóa sẽ không thể thực hiện được nếu không có các cơ chế thích ứng như NAT-T (*NAT Traversal*);
- Giao thức X Window, cho phép hiển thị từ xa các ứng dụng đồ họa trên Unix/Linux, hoạt động theo cách máy chủ X chủ động gửi các kết nối TCP đến máy khách. Việc đảo ngược hướng kết nối thông thường này có thể bị chặn bởi NAT.


Nhìn chung, bất kỳ giao thức nào bao gồm rõ ràng IP Address nội bộ trong tải trọng gói tin sẽ bị ảnh hưởng, vì Address đó sẽ không còn khớp với Address thực tế có thể nhìn thấy trên internet sau khi dịch.


**Lưu ý quan trọng:** Để giải quyết những vấn đề này, một số bộ định tuyến NAT cung cấp _Kiểm tra Gói Sâu_ (DPI) hoặc _Trợ lý Giao thức_, giúp kiểm tra nội dung gói tin để xác định và thay thế địa chỉ hoặc số cổng động trong dữ liệu ứng dụng. Điều này đòi hỏi kiến thức chuyên sâu về định dạng giao thức và có thể tạo ra lỗ hổng bảo mật hoặc tăng mức sử dụng tài nguyên.


**Lưu ý:** Mặc dù NAT giúp ẩn mạng nội bộ và kiểm soát lưu lượng truy cập đến, nhưng nó không thể thay thế tường lửa chuyên dụng. Bản dịch không phải là rào cản bảo mật hoàn chỉnh: nó luôn phải được bổ sung bởi các quy tắc lọc rõ ràng để chặn lưu lượng truy cập không mong muốn hoặc không được yêu cầu.


_Để minh họa cách thức hoạt động này trong thực tế, hãy xem xét ví dụ sau:_



![Image](assets/fr/037.webp)



Trong trường hợp này, một máy trạm nội bộ có thể truy cập máy chủ web nội bộ chỉ bằng cách gọi URL `http://192.168.1.20:80`. Việc chỉ định cổng ở đây là tùy chọn, vì `80` là cổng HTTP tiêu chuẩn. Ngược lại, nếu một yêu cầu được khởi tạo từ bên ngoài, người dùng sẽ nhập địa chỉ Address công khai `http://85.152.44.14:80`. Bộ định tuyến NAT nhận được yêu cầu, tham khảo bảng ánh xạ của nó và tự động chuyển đổi địa chỉ Address công khai thành địa chỉ Address riêng tư, chuyển hướng kết nối đến `http://192.168.1.20:80`.


Nguyên tắc tương tự cũng áp dụng cho bất kỳ máy chủ nào khác được phép nhận kết nối internet, chẳng hạn như máy chủ Extranet (mạch màu xanh trong sơ đồ).


**Lưu ý thực tế:** trong môi trường ảo hóa, các giao diện mạng được gọi là _virbrX_ (viết tắt của _Virtual Bridge X_) thường được sử dụng. Các cầu nối ảo này, đặc biệt được cung cấp bởi thư viện libvirt hoặc trình quản lý ảo hóa Xen, kết nối mạng nội bộ ảo của các máy khách với mạng vật lý trong khi áp dụng NAT. Chúng thường được cấu hình thông qua các tập lệnh trong `/etc/sysconfig/network-scripts/`, như được hiển thị bên dưới cho `virbr0`:


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


Sau khi cầu ảo được thiết lập, bạn cần bật định tuyến IP và cấu hình chuyển đổi cổng bằng `iptables`:


```shell
echo 1 > /proc/sys/net/ipv4/ip_forward
```


```shell
iptables -t nat -A POSTROUTING -o <WAN> -s 192.168.0.0/24 -j MASQUERADE
```


Với cấu hình này, lưu lượng đi sẽ được định tuyến và áp dụng chuyển đổi NAT, cho phép các máy ảo giao tiếp với thế giới bên ngoài mà không cần trực tiếp tiết lộ địa chỉ IP nội bộ của chúng.


Trong chương tiếp theo, chúng ta sẽ xem xét chi tiết về cấu hình IP Address trên Linux, bao gồm cả phương pháp đơn giản và nâng cao phù hợp với các bối cảnh quản trị khác nhau.



https://planb.network/tutorials/computer-security/communication/pi-hole-46a735c5-8af3-4cc3-a2c2-1d4f6a7dc428

https://planb.network/tutorials/computer-security/operating-system/opnsense-90c2785d-a0d7-4981-be8d-d290bbeb8263

https://planb.network/tutorials/computer-security/operating-system/pfsense-24eea96a-2fdc-42a6-a77b-89bc29149864


## Làm thế nào để cấu hình mạng bằng `ip`?


<chapterId>8ba7e946-d2a0-4841-8d54-e85ba96baa25</chapterId>



### Cấu hình tiêu chuẩn


Sau khi tìm hiểu nền tảng lý thuyết về mạng và hiểu cách thức hoạt động của địa chỉ IP, mặt nạ, định tuyến và dịch thuật, đã đến lúc chuyển sang cấu hình thực hành. Trên GNU/Linux, việc thiết lập mạng hiện được xử lý bằng lệnh **`ip`** (gói _iproute2_), thay thế cho lệnh `ifconfig` cũ.


`ip` cho phép bạn gán hoặc thay đổi IP Address, thay đổi mặt nạ, khởi động hoặc dừng Interface hoặc kiểm tra trạng thái của nó bất cứ lúc nào.


**MẸO:** để hiển thị tất cả các giao diện (đang hoạt động hoặc không): `ip addr show`


Ví dụ: gán Address tĩnh và kích hoạt Interface


Thêm Address `192.168.1.2/24` vào Interface `eth0`:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Kích hoạt Interface:


```shell
ip link set dev eth0 up
```


Vô hiệu hóa Interface:


```shell
ip link set dev eth0 down
```


Hiển thị trạng thái của một Interface cụ thể:


```shell
ip addr show dev eth2
```


**Mẹo thực tế:** với `ip`, việc thêm Address vào Interface không còn cần hậu tố `:1` nữa. Chỉ cần thêm một dòng `ip addr add ...` nữa:


```shell
ip addr add 172.18.2.39/24 dev eth2
```


### Các tập lệnh kích hoạt: ifup / ifdown


Tiện ích `ifup` và `ifdown` đọc các tệp cấu hình tĩnh từ `/etc/sysconfig/network-scripts/` (trên RHEL, CentOS, Rocky Linux, AlmaLinux...) hoặc `/etc/network/interfaces` (trên Debian/Ubuntu) để đưa giao diện lên hoặc xuống một cách gọn gàng.


```shell
ifup eth1
ifdown eth2
```


Tệp cấu hình (giống RHEL):


- /etc/sysconfig/network**: thiết lập chung (MẠNG, TÊN MÁY CHỦ, CỔNG...).
- ifcfg-**: cài đặt cụ thể cho từng Interface.


Ví dụ tĩnh (ifcfg-eth0):


```ini
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
IPADDR=192.168.2.5
NETMASK=255.255.255.0
GATEWAY=192.168.2.1
```


Ví dụ về DHCP:


```ini
DEVICE=eth0
BOOTPROTO=dhcp
ONBOOT=yes
```


Cấu trúc mô-đun này vẫn còn hiệu lực và có thể dễ dàng tự động hóa trên các hệ thống hiện tại.


### Cấu hình nâng cao: liên kết


Trong môi trường chuyên nghiệp, mục tiêu là đảm bảo tính liên tục của dịch vụ và/hoặc tổng hợp băng thông. Các cơ chế *liên kết* (hoặc *kết hợp* với _teamd_) đáp ứng những nhu cầu này: nhiều giao diện vật lý hoạt động như một Interface logic duy nhất, thường được gọi là `bond0` hoặc `team0`.



![Image](assets/fr/039.webp)



Điều kiện tiên quyết:


- Tải mô-đun `bonding` (hoặc sử dụng `teamd`);
- Có ít nhất hai giao diện vật lý.


#### Các phương pháp liên kết phổ biến khác nhau:


|Mode|Name|Principle|
|---|---|---|
|0|balance-rr|Round-robin, cyclic distribution of frames|
|1|active-backup|Single active interface with hot failover |
|2|balance-xor|Selection based on XOR of src/dst MAC addresses|
|3|broadcast|Broadcast simultaneously on all interfaces   |
|4|802.3ad (LACP)|Standardized dynamic aggregation; requires compatible switch|
|5|tlb (Transmit Load Balancing)|Balancing based on transmit load|
|6|alb (Adaptive Load Balancing)|Adaptive balancing; also balances receive via ARP|

#### Thiết lập với `ip link



- Vô hiệu hóa giao diện vật lý:


```shell
ip link set eth0 down
ip link set eth1 down
```



- Tạo Interface liên kết:


```shell
ip link add bond0 type bond mode balance-alb
```



- Cấu hình tùy chọn sau khi tạo


```shell
ip link set bond0 type bond miimon 100
```



- Chỉ định địa chỉ MAC và IP:


```shell
ip link set dev bond0 address 00:17:56:BC:02:3A
ip addr add 192.168.2.3/24 dev bond0
ip route add default via 192.168.2.1
```



- Đính kèm giao diện phụ:


```shell
ip link set eth0 master bond0
ip link set eth1 master bond0
```



- Đưa mọi thứ trở lại:


```shell
ip link set bond0 up
ip link set eth0 up
ip link set eth1 up
```


**Mẹo:** để tách một slave mà không phá vỡ liên kết: `ip link set eth1 nomaster`


#### Cấu hình cố định (giống RHEL)


Tạo ba tệp trong `/etc/sysconfig/network-scripts`:


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


Sau đó:


```shell
systemctl restart network
```


#### IP bổ sung Address (tên gọi hiện đại)


Với `ip`, bạn có thể dễ dàng thêm một Address thứ hai vào cùng một thiết bị:


```shell
ip addr add 192.168.1.2/24 dev eth0
```


Để duy trì bí danh này sau khi khởi động lại, hãy thêm khối `IPADDR2=...` / `PREFIX2=...` thứ hai vào `ifcfg-eth0` hoặc tạo kết nối *NetworkManager* mới thông qua `nmcli`.


Nhờ lệnh `ip` và các lệnh liên quan (`ip link`, `ip addr`, `ip route`), cấu hình mạng trở nên nhất quán, dễ dàng lập trình và rõ ràng hơn. Liên kết là một thành phần quan trọng của kiến trúc sẵn sàng cao, và việc gán nhiều địa chỉ cho một Interface đã trở nên đơn giản hơn rất nhiều.


Trong chương tiếp theo, chúng ta sẽ xem xét chi tiết và cách triển khai địa chỉ IPv6.


# Địa chỉ IPv6


<partId>9b1d87f1-2a68-496e-b5dd-76cf74fb8cde</partId>


## IPv6: Tiêu chuẩn và định nghĩa


<chapterId>d1f16f0a-1104-460d-8d67-f725665f8e3f</chapterId>



Bây giờ chúng ta chuyển sang thế hệ địa chỉ IP tiếp theo: giao thức IPv6, ban đầu được gọi là IPng (_IP Thế hệ tiếp theo_). Được thiết kế để khắc phục những hạn chế về cấu trúc của IPv4, giao thức này giới thiệu một kiến trúc địa chỉ được mở rộng đáng kể, cũng như nhiều tối ưu hóa kỹ thuật.


Động lực thúc đẩy việc áp dụng IPv6 rất đa dạng, và Address là nhu cầu thiết yếu cho sự phát triển của Internet. Thứ nhất, vai trò của IPv6 là hỗ trợ sự tăng trưởng theo cấp số nhân về số lượng thiết bị được kết nối (một mục tiêu không thể đạt được với không gian hạn chế của Address của IPv4). Thứ hai, giao thức này hướng đến việc giảm kích thước bảng định tuyến, giúp việc trao đổi dữ liệu hiệu quả hơn và giảm tải cho bộ định tuyến về lâu dài.


IPv6 cũng hướng đến việc đơn giản hóa một số khía cạnh của việc xử lý gói tin, cải thiện luồng dữ liệu và tối ưu hóa tốc độ truyền giữa các mạng. Về mặt bảo mật, tiêu đề AH/ESP của giao thức *IPsec* được bao gồm trong đặc tả cơ sở, và tất cả các nút IPv6 phải có khả năng hỗ trợ chúng (RFC 6434). Tuy nhiên, việc sử dụng chúng vẫn là tùy chọn: quản trị viên có thể bật chúng tùy theo ngữ cảnh.


Các mục tiêu khác bao gồm xử lý chính xác hơn các loại dịch vụ, đặc biệt là để đảm bảo chất lượng tốt hơn cho các ứng dụng thời gian thực (VoIP, hội nghị truyền hình, v.v.). IPv6 cũng được thiết kế để cho phép quản lý tính di động linh hoạt hơn: một thiết bị có thể thay đổi điểm truy cập mà không cần thay đổi Address theo cách mà các thiết bị ngang hàng có thể nhìn thấy.


Cuối cùng, IPv6 được thiết kế để cùng tồn tại với các giao thức cũ. Mặc dù không tương thích nhị phân trực tiếp với IPv4, nhưng nó vẫn hoàn toàn tương thích với các giao thức Layer cao hơn như TCP, UDP, ICMPv6 và DNS, cũng như với các giao thức định tuyến như OSPF và BGP, tùy thuộc vào một số điều chỉnh nhất định. Về quản lý đa hướng, IPv6 sử dụng giao thức MLD (*Multicast Listener Discovery*), tương đương về mặt chức năng với IGMP trong môi trường IPv4.


### Quy tắc ký hiệu


Một trong những thay đổi quan trọng nhất trong IPv6 là định dạng của chính IP Address. Để khắc phục tình trạng thiếu hụt địa chỉ IPv4 triền miên, Address đã tăng độ dài của Address từ 32 bit lên 128 bit, tức là 16 byte. Về lý thuyết, điều này tạo ra không gian Address khả thi là:


$$3,4 \lần 10^{38}$$


Điều này đảm bảo khả năng gần như không giới hạn cho tất cả các thiết bị hiện tại và tương lai.


Địa chỉ IPv6 được viết rất khác so với ký hiệu thập phân chấm quen thuộc. IPv6 Address bao gồm tám nhóm 16 bit, được viết theo hệ thập lục phân và phân tách bằng dấu hai chấm `:`.


Ví dụ:


```
1987:0c02:0000:84c2:0000:0000:cf2a:9077
```


Để đơn giản hóa ký hiệu, có thể bỏ số 0 đứng đầu trong mỗi nhóm. Ví dụ trên trở thành:


```
1987:c02:0:84c2:0:0:cf2a:9077
```


Ngoài ra, một chuỗi liên tục duy nhất của các nhóm số không có thể được thay thế bằng ::, rút ngắn hơn nữa Address:


```
1987:c02:0:84c2::cf2a:9077
```


**Cảnh báo:** quy tắc này rất nghiêm ngặt: chỉ có thể thay thế một chuỗi số 0 liên tiếp bằng `::`. Nếu Address chứa nhiều chuỗi số 0, chỉ chuỗi số 0 dài nhất được rút gọn. Điều này đảm bảo tính duy nhất và khả năng đọc.


**Chi tiết quan trọng:** ký tự `:` dùng để phân tách các khối thập lục phân có thể gây ra sự mơ hồ trong URL, vì `:` cũng được dùng để chỉ cổng dịch vụ. Để tránh nhầm lẫn, địa chỉ IPv6 trong URL phải được đặt trong dấu ngoặc vuông `[ ]`.


Ví dụ về quyền truy cập HTTP vào một cổng cụ thể cho Address `2002:400:2A41:378::34A2:36`:


```
http://[2002:400:2A41:378::34A2:36]:8080
```


Khi biểu diễn IPv4 Address trong ngữ cảnh IPv6, bạn có thể sử dụng ký hiệu hỗn hợp ở dạng thập phân chấm, đứng trước bởi `::`:


```
::192.168.1.5
```


Khả năng tương thích này giúp quá trình chuyển đổi giữa hai giao thức trở nên dễ dàng hơn bằng cách cho phép các khối IPv4 được đưa vào không gian IPv6 Address.


**Lưu ý:** Để chuẩn hóa cách viết địa chỉ, RFC 5952 định nghĩa một định dạng chuẩn với các quy tắc viết tắt để tránh việc sử dụng nhiều lần cùng một Address. Việc tuân thủ các khuyến nghị này giúp giảm thiểu việc hiểu sai và đảm bảo cấu hình mạng nhất quán.


### Các loại IPv6 Address


IPv6 khác biệt so với phiên bản tiền nhiệm ở một loạt các danh mục Address, mỗi danh mục được thiết kế cho các mục đích sử dụng cụ thể, đồng thời cho phép định tuyến và quản lý mạng linh hoạt. Giống như IPv4, địa chỉ có thể là toàn cầu, cục bộ, dành riêng hoặc dành riêng cho một số cơ chế chuyển đổi nhất định.


Một Address IPv6 không xác định được biểu thị bằng `::` hoặc, rõ ràng hơn, `::0.0.0.0`. Dạng đặc biệt này được sử dụng trong quá trình thu thập Address, hoặc làm giá trị mặc định để biểu thị sự vắng mặt của Address.



| IPv6 Address Prefix | Description                                 |
| ------------------- | ------------------------------------------- |
|::/8                | Reserved addresses                          |
| 2000::/3            | Unicast addresses, routable on the Internet |
| fc00::/7            | Unique local addresses (1)                  |
| fe80::/10           | Link-local addresses                        |
| ff00::/8            | Multicast addresses                         |

(1): *Trên mạng LAN riêng, tiền tố `fd00::/8` được ưu tiên để chỉ định các địa chỉ nội bộ không thể định tuyến trên Internet.*


#### Địa chỉ được bảo lưu


Một số dải IPv6 được dành riêng một cách rõ ràng và không được sử dụng làm địa chỉ toàn cầu. Chúng có mục đích kỹ thuật cụ thể:


- `::/128`**: Address không xác định, không bao giờ được gán cố định cho một thiết bị, nhưng được sử dụng làm Address nguồn bởi một máy đang chờ cấu hình.
- `::1/128`**: _loopback_ Address, tương đương trực tiếp với `127.0.0.1` trong IPv4, cho phép máy tính tự Address.
- `64:ff9b::/96`**: Dành riêng cho các trình dịch giao thức để kích hoạt kết nối IPv4/IPv6, như được định nghĩa trong RFC 6052.
- `::ffff:0:0/96`**: khối tương thích để biểu diễn IPv4 Address trong cấu trúc IPv6 cụ thể, thường được các ứng dụng sử dụng nội bộ.


Các khối này đảm bảo khả năng tương tác và tạo điều kiện thuận lợi cho việc di chuyển giữa hai phiên bản giao thức.


#### Địa chỉ đơn hướng toàn cầu


Địa chỉ unicast toàn cầu chiếm phần lớn không gian IPv6 có thể định tuyến công khai, chiếm khoảng 1/8 không gian Address. Từ năm 1999, IANA đã phân bổ các khối này, chẳng hạn như tiền tố `2001::/16`, trong các khối CIDR (từ `/23` đến `/12`) cho các cơ quan đăng ký khu vực, sau đó phân phối lại cho các nhà cung cấp và tổ chức.


Một số loại có công dụng đặc biệt được ghi chép lại:


- `2001:2::/48`**: Dành riêng cho việc thử nghiệm hiệu suất và khả năng tương tác (RFC 5180).
- `2001:db8::/32`**: Dành riêng cho tài liệu và ví dụ (RFC 3849).
- `2002::/16`**: Được sử dụng cho cơ chế 6to4, cho phép lưu lượng IPv6 di chuyển qua cơ sở hạ tầng IPv4 (hữu ích trong giai đoạn chuyển đổi giữa hai giao thức).


**Lưu ý:** một tỷ lệ lớn các địa chỉ toàn cầu vẫn chưa được sử dụng, đóng vai trò dự trữ cho sự phát triển Internet trong tương lai.


#### Địa chỉ cục bộ duy nhất (ULA)


Địa chỉ cục bộ duy nhất (`fc00::/7`) tương đương với địa chỉ riêng IPv4 trong IPv6 (RFC1918). Chúng cho phép tạo các mạng nội bộ biệt lập mà không có nguy cơ xung đột với địa chỉ công cộng. Trên thực tế, tiền tố hiệu dụng là `fd00::/8`, với bit thứ 8 được đặt thành 1 để biểu thị mức sử dụng cục bộ. Mỗi khối ULA bao gồm một mã định danh giả ngẫu nhiên 40 bit, giảm thiểu xung đột Address khi kết nối các mạng riêng biệt.


#### Địa chỉ liên kết cục bộ


Địa chỉ liên kết cục bộ (`fe80::/64`) chỉ được sử dụng cho giao tiếp trong cùng một phân đoạn Layer 2 (cùng VLAN hoặc switch). Chúng không bao giờ được định tuyến vượt ra ngoài liên kết cục bộ. Mỗi mạng Interface tự động tạo một Address liên kết cục bộ, thường được lấy từ địa chỉ MAC Address của nó bằng cách sử dụng sơ đồ EUI-64.


**Tính năng đặc biệt**: cùng một máy có thể sử dụng cùng một liên kết cục bộ Address trên nhiều giao diện, nhưng phải chỉ định Interface khi giao tiếp để tránh sự mơ hồ.


#### Địa chỉ đa hướng


Trong IPv6, broadcast đã được thay thế bằng multicast, một cách hiệu quả hơn để phân phối các gói tin đến một nhóm người nhận được xác định. Phạm vi multicast được thêm tiền tố `ff00::/8`. Các địa chỉ này bao gồm các địa chỉ như `ff02::1`, nhắm mục tiêu đến tất cả các nút trên liên kết cục bộ. Mặc dù tiện lợi, Address này không còn được khuyến nghị cho các ứng dụng nữa, vì nó có thể phát broadcast không kiểm soát.


Một ứng dụng phổ biến của multicast là _Giao thức Khám phá Hàng xóm_ (NDP), thay thế ARP trong IPv6. NDP sử dụng các địa chỉ multicast cụ thể, chẳng hạn như `ff02::1:ff00:0/104`, để tự động khám phá các máy chủ khác được kết nối với cùng một liên kết.


Bằng cách kết hợp các loại Address này, IPv6 cung cấp một bộ tùy chọn hoàn chỉnh để đáp ứng nhu cầu định tuyến toàn cầu, truyền thông cục bộ, di chuyển IPv4/IPv6 và cấu hình thiết bị tự động, đồng thời cải thiện hiệu quả truyền tải.


### Ống ngắm Address


Phạm vi của IPv6 Address xác định miền chính xác mà nó hợp lệ và duy nhất. Hiểu được khái niệm này là chìa khóa để nắm vững định tuyến gói tin và tổ chức logic của mạng IPv6. Địa chỉ IPv6 thường được nhóm thành ba loại chính dựa trên phạm vi và cách sử dụng: đơn hướng (unicast), bất kỳ hướng nào (anycast) và đa hướng (multicast).


**Địa chỉ đơn hướng** là loại phổ biến nhất và bao gồm một số loại phụ riêng biệt.

Bao gồm _loopback_ (`::1`) Address, có phạm vi giới hạn ở máy chủ sử dụng và được dùng để kiểm tra ngăn xếp mạng nội bộ mà không gửi lưu lượng qua mạng vật lý.

Sau đó, có các địa chỉ liên kết cục bộ (_link-local_), có phạm vi bị giới hạn trong một phân đoạn mạng duy nhất: chúng được sử dụng cho liên lạc trực tiếp giữa các thiết bị trên cùng một liên kết vật lý hoặc logic (ví dụ: một công tắc hoặc VLAN duy nhất).

Cuối cùng, các địa chỉ cục bộ duy nhất (_ULA_, viết tắt của _Unique Local Addresses_) là các địa chỉ nội bộ trong một mạng riêng. Chúng có thể được định tuyến giữa nhiều phân đoạn riêng nhưng không bao giờ hiển thị trên Internet.


Về mặt khái niệm, địa chỉ IPv6 thường được biểu diễn dưới dạng nhị phân, trong đó nửa đầu (64 bit đầu tiên) xác định tiền tố mạng, và nửa sau (cũng 64 bit) xác định duy nhất Interface của thiết bị trên mạng đó. Sự phân chia này giúp việc tự động cấu hình Address dễ dàng hơn thông qua các cơ chế như SLAAC (_Stateless Address Autoconfiguration_), cho phép máy tự động generate một Address ổn định dựa trên MAC Address hoặc một mã định danh giả ngẫu nhiên.


| Field     | Prefix | L | Global ID | Subnet | Interface ID |
|-----------|--------|---|-----------|--------|---------------|
| Bits      | 7      | 1 | 40        | 16     | 64            |

Kiến trúc IPv6 tuân theo mô hình định tuyến toàn cầu phân cấp của Internet ngày nay. Phân vùng tiền tố cho phép các cơ quan đăng ký khu vực và nhà điều hành mạng quản lý việc phân bổ Address theo cách phi tập trung, đồng thời đảm bảo tính duy nhất toàn cầu. Trong khuôn khổ này, cùng một máy chủ có thể đồng thời giữ một Address đơn hướng toàn cầu cho giao tiếp internet và một Address liên kết cục bộ cho các tương tác cục bộ, ví dụ như với các vùng lân cận hoặc cho các thông báo khám phá bộ định tuyến.


| Field     | Prefix | Zero | Interface ID |
|-----------|--------|------|--------------|
| Bits      | 10     | 54   | 64           |

**Địa chỉ Anycast** đại diện cho một khái niệm trung gian được xây dựng dựa trên mô hình đơn hướng nhưng có thể hoạt động như đa hướng trong một số trường hợp. Về bản chất, Anycast Address là một Unicast Address được gán cho nhiều giao diện phân tán trên các nút mạng khác nhau. Khi một gói tin được gửi đến Anycast Address, giao thức IPv6 sẽ chuyển gói tin đó đến một trong các máy chủ chia sẻ Address đó, thường là máy chủ gần nhất về mặt cấu trúc định tuyến. Cách tiếp cận này tối ưu hóa tốc độ xử lý truy vấn và cải thiện khả năng phục hồi của các dịch vụ phân tán. Một ví dụ điển hình là các máy chủ DNS gốc, nơi địa chỉ Anycast tự động chuyển hướng truy vấn đến điểm hiện diện gần nhất.



| Field     | Prefix | Subnet | Interface ID |
|-----------|--------|--------|--------------|
| Bits      | 48     | 16     | 64           |

Trong IPv6, **địa chỉ đa hướng** thay thế cơ chế phát sóng, vốn được coi là quá tốn kém và không phù hợp với mạng lưới toàn cầu. Address đa hướng xác định một nhóm giao diện, thường trên nhiều máy chủ, muốn nhận cùng một gói tin đồng thời.

Mỗi Address đa hướng bao gồm một trường _scope_ 4 bit đặc biệt, xác định giới hạn địa lý hoặc logic của chương trình phát sóng:


- Phạm vi `1` có nghĩa là gói tin chỉ dành cho thiết bị cục bộ.
- Phạm vi `2` giới hạn gói tin trong liên kết cục bộ: tất cả các thiết bị trên cùng một phân đoạn vật lý hoặc ảo đều có thể nhận được gói tin.
- Phạm vi `5` mở rộng phạm vi đến một trang web, thường là toàn bộ mạng công ty.
- Phạm vi `8` mở rộng phạm vi tiếp cận tới một tổ chức, cho phép phân phối trên tất cả các mạng con của cùng một thực thể.
- Phạm vi `e` (14 trong hệ thập lục phân) biểu thị phạm vi toàn cầu, giúp nhóm đa hướng có thể truy cập từ mọi nơi trên Internet nếu cơ sở hạ tầng định tuyến hỗ trợ.


Cấu trúc của IPv6 multicast Address bao gồm:


- trường _Flag_ (4 bit) chỉ định nhóm là vĩnh viễn hay tạm thời,
- trường _Scope_ (4 bit) xác định phạm vi,
- trường nhận dạng (112 bit) xác định số nhóm đa hướng.


| Field      | Prefix | Flags | Scope | Group ID |
|------------|--------|--------|--------|----------|
| Bits       | 8      | 4      | 4      | 112      |

Một ví dụ nổi tiếng về multicast IPv6 đang hoạt động là _Giao thức Khám phá Hàng xóm_ (NDP). Thay vì sử dụng ARP như trong IPv4, NDP dựa vào các địa chỉ multicast như `ff02::1:ff00:0/104` để phát các yêu cầu khám phá hàng xóm, chỉ nhắm mục tiêu đến các máy chủ liên quan trên cùng một liên kết.


Bằng cách định nghĩa phạm vi Address một cách chính xác, IPv6 cấu trúc cách thức gửi, nhận và định tuyến luồng dữ liệu. Độ chi tiết này giúp giao thức linh hoạt và hiệu quả hơn trong việc quản lý cả truyền thông cục bộ và toàn cầu, đồng thời tránh được những nhược điểm của việc phát sóng tổng quát.


## Address Assignment trong mạng cục bộ


<chapterId>4c9c3e52-59bc-499a-af0a-6dd369a9e029</chapterId>


Trong chương này, chúng ta sẽ xem xét một trong những khía cạnh thiết thực nhất của việc triển khai IPv6: gán địa chỉ IP cho các máy chủ trên mạng cục bộ. Kiến trúc IPv6 được thiết kế linh hoạt, cho phép mỗi thiết bị tự động kết nối generate với Address của riêng mình, đồng thời vẫn cho phép cấu hình thủ công hoàn toàn khi cần.


Mạng cục bộ IPv6 chia Address thành hai phần một cách có hệ thống:


- 64 bit đầu tiên biểu thị tiền tố mạng con, thường được cung cấp bởi bộ định tuyến hoặc cơ quan Address;
- 64 bit còn lại được máy chủ sử dụng để xác định duy nhất chính nó trên phân đoạn đó.

Mô hình này đơn giản hóa đáng kể việc tổng hợp tuyến đường và quản lý khối Address.


Có hai cách tiếp cận chính được sử dụng để gán địa chỉ cho các thiết bị:


- Cấu hình thủ công, trong đó người quản trị chỉ định chính xác Address của mỗi Interface;
- Cấu hình tự động, trong đó các thiết bị generate có thể tự động lấy địa chỉ của mình.


Trong cấu hình thủ công, quản trị viên sẽ gán toàn bộ IPv6 Address cho mỗi Interface. Một số giá trị vẫn được giữ nguyên:


- `::/128`: Address không xác định, không bao giờ được gán cố định;
- `::1/128`: vòng lặp Address (_loopback_), tương đương IPv4: `127.0.0.1`.


Không giống như IPv4, không có khái niệm _phát sóng_; các tổ hợp "toàn số không" hoặc "toàn số một" trong phần máy chủ không có ý nghĩa đặc biệt nào.

Cấu hình thủ công vẫn hữu ích trong môi trường được kiểm soát nhưng lại khó duy trì ở quy mô lớn.


Để cấu hình tự động, có một số phương pháp sau:


- Giao thức **NDP** (_Neighbor Discovery Protocol_), được chỉ định bởi RFC4862, cho phép tự động cấu hình *không trạng thái*. Ở chế độ này, máy chủ nhận được tiền tố mạng từ bộ định tuyến cục bộ và tự động thêm mã định danh dựa trên địa chỉ MAC Address của nó vào Address. Phương pháp này dễ triển khai và không yêu cầu máy chủ trung tâm.
- Các triển khai như trong Windows có thể generate phần máy chủ một cách giả ngẫu nhiên để cải thiện quyền riêng tư bằng cách tránh lộ trực tiếp địa chỉ MAC Address. Việc tiết lộ địa chỉ MAC Address trong các gói tin IPv6 có thể gây ra lo ngại về quyền riêng tư, vì nó cho phép theo dõi thiết bị trên nhiều mạng khác nhau.
- Giao thức DHCPv6: Được định nghĩa trong RFC3315 và tương tự như DHCP được sử dụng cho IPv4, giao thức này cho phép cấu hình được kiểm soát và tập trung hơn, bao gồm quản lý thuê bao, các tùy chọn bổ sung (DNS, MTU...), và đăng ký cơ sở dữ liệu. DHCPv6 có thể hoạt động độc lập hoặc kết hợp với cấu hình không trạng thái để cung cấp các tham số bổ sung mà không cần tự gán địa chỉ IP Address.


**Lưu ý quan trọng:** Trong phương pháp dựa trên MAC, MAC Address được chuyển đổi thành mã định danh 64 bit bằng định dạng EUI-64. Cơ chế này chèn các byte `FF:FE` vào giữa MAC Address gốc (48 bit) và đảo ngược bit thứ 7 để biểu thị tính duy nhất toàn cục. Kết quả là một mã định danh Interface ổn định, được sử dụng trong IPv6 Address đầy đủ.


Sau đây là ví dụ về cách chuyển đổi MAC Address thành EUI-64:


![Image](assets/fr/045.webp)



Tuy nhiên, do lo ngại ngày càng tăng về việc theo dõi thiết bị, các hệ điều hành hiện đại (đặc biệt là Linux, Windows 10+, macOS, Android) hiện cho phép mở rộng quyền riêng tư theo mặc định. Các tiện ích này sử dụng mã định danh Interface được tạo ngẫu nhiên, được gia hạn định kỳ cho các kết nối đi, đồng thời duy trì một mã định danh ổn định cho các giao tiếp nội bộ (chẳng hạn như DNS hoặc DHCPv6).


Giống như DHCP trong IPv4, địa chỉ IPv6 được gán tự động có thể có hai thời hạn tồn tại, được xác định bởi bộ định tuyến hoặc máy chủ DHCPv6:


- Tuổi thọ ưu tiên*: sau thời hạn này, Address vẫn có hiệu lực nhưng không còn được sử dụng để bắt đầu các kết nối mới;
- Thời hạn sử dụng hợp lệ*: khi thời hạn này hết hạn, Address sẽ bị xóa hoàn toàn khỏi cấu hình Interface.


Hệ thống này cho phép quản lý các thay đổi mạng một cách linh hoạt, ví dụ, đảm bảo quá trình chuyển đổi suôn sẻ từ ISP này sang ISP khác. Bằng cách cập nhật tiền tố được bộ định tuyến thông báo và điều chỉnh bản ghi DNS song song, việc di chuyển IPv6 có thể được thực hiện mà không gây gián đoạn dịch vụ đáng kể.


**Mẹo:** Việc kết hợp sử dụng vòng đời Address và DNS giúp có thể triển khai chiến lược chuyển đổi dần dần, trong đó các kết nối mới chuyển sang cấu trúc mạng mới, trong khi các kết nối hiện tại vẫn tiếp tục cho đến khi kết thúc.


Tóm lại, IPv6 cung cấp nhiều lựa chọn linh hoạt cho Address và Assignment: cấu hình thủ công, cấu hình tự động không trạng thái hoặc có trạng thái, DHCPv6 hoặc tạo ngẫu nhiên. Mỗi phương pháp đều có những ưu điểm và hạn chế riêng, và có thể được điều chỉnh tùy theo mức độ kiểm soát cần thiết, quy mô mạng hoặc nhu cầu riêng tư.


## Chỉ định các khối IPv6 Address


<chapterId>45cce866-1b58-4888-b3fe-15c922180839</chapterId>


### Phân phối Address


Sơ đồ phân bổ IPv6 Address được xây dựng nhằm đáp ứng hai mục tiêu: đảm bảo tính duy nhất toàn cầu của Address và cho phép phân cấp logic có lợi cho việc tổng hợp và đơn giản hóa các bảng định tuyến.

Tương tự như IPv4, *Cơ quan Quản lý Số hiệu Internet* (IANA) nằm ở vị trí cao nhất trong hệ thống phân cấp này. IANA quản lý không gian Address đơn hướng toàn cầu và phân bổ các khối Address cho năm cơ quan đăng ký Internet khu vực (_RIR_).


Năm RIR hiện có là:


- ARIN (Bắc Mỹ),
- RIPE NCC (Châu Âu, Trung Đông, Trung Á),
- APNIC (Châu Á - Thái Bình Dương),
- AFRINIC (Châu Phi),
- LACNIC (Mỹ Latinh và Caribe).


IANA phân bổ các khối IPv6 với kích thước khác nhau cho mỗi RIR, thường nằm trong khoảng từ /23 đến /12. Cách tiếp cận này mang lại sự linh hoạt đồng thời đảm bảo khả năng mở rộng lâu dài. Đổi lại, các RIR sẽ phân phối lại các khối này cho các Nhà cung cấp Dịch vụ Internet (ISP), các tập đoàn lớn và các tổ chức công.


Từ năm 2006, mỗi RIR đều nhận được một khối IPv6 /12 từ IANA, một kích thước cố định được thiết kế để đảm bảo dự trữ ổn định và đủ lớn cho sự phát triển trong tương lai. RIR thường chia nhỏ các khối này thành các khối /23, /26 hoặc /29. Các ISP thường nhận được các khối /32, mặc dù kích thước này có thể thay đổi tùy thuộc vào quy mô và khu vực địa lý của ISP. Họ thường phân bổ các khối /48 cho khách hàng. Mỗi khối /48 cung cấp 65.536 mạng con /64 riêng biệt (một dung lượng rất lớn so với IPv4).


**Lưu ý quan trọng:** một khối /32 chứa chính xác 65.536 khối con /48. Điều này có nghĩa là mỗi ISP có thể phục vụ hàng chục nghìn khách hàng mà không bị cạn kiệt phân bổ. Nhờ /48, mỗi khách hàng sẽ có một không gian khổng lồ để cấu trúc mạng nội bộ của riêng mình với số lượng phân đoạn /64 tùy ý.


Hệ thống phân bổ điển hình trông như thế này:


| IANA | RIR | LIR | Customer | Subnet | Interface |
|------|-----|-----|----------|--------|-----------|
|  3   | 20  |  9  |    16    |   16   |     64    |

Với sự phong phú của địa chỉ này, NAT (*Network Address Translation*), vốn từng là yếu tố thiết yếu trong IPv4 để đối phó với tình trạng thiếu hụt Address, giờ đây không còn cần thiết nữa. Mỗi máy chủ có thể có một Address công cộng duy nhất, có thể định tuyến toàn cầu, giúp đơn giản hóa kết nối đầu cuối và giúp các giao thức như IPSec, VoIP hoặc kết nối đến dễ sử dụng hơn.


Để kiểm tra xem IPv6 Address thuộc tổ chức nào, bạn có thể sử dụng lệnh `whois` để truy vấn cơ sở dữ liệu RIR công cộng. Tính minh bạch này cho phép xác định tổ chức sở hữu tiền tố, điều này có thể hữu ích cho mục đích mạng, phân tích hoặc bảo mật.


### Địa chỉ PA so với PI


Ban đầu, mô hình phân bổ IPv6 chỉ dựa trên các khối PA (*Provider Aggregatable*), nghĩa là được liên kết với ISP. Trong mô hình này, một tổ chức nhận tiền tố từ ISP của mình, nghĩa là việc thay đổi nhà cung cấp đòi hỏi phải đánh số lại toàn bộ cơ sở hạ tầng.


Mặc dù tính năng tự động cấu hình của IPv6 và thời gian sống của Address giúp việc đánh số lại dễ dàng hơn, nhưng vẫn bất tiện đối với các tổ chức có cơ sở hạ tầng quan trọng hoặc nhiều kết nối nhà cung cấp cho yêu cầu dự phòng.


Từ năm 2009, các chính sách phân bổ đã cho phép sử dụng các khối PI (*Nhà cung cấp độc lập*). Các khối này (thường có kích thước /48) được RIR phân bổ trực tiếp cho một công ty hoặc tổ chức, độc lập với bất kỳ ISP nào. Mô hình này đặc biệt phù hợp với các tổ chức áp dụng *multihoming* (tức là kết nối đồng thời với nhiều nhà mạng). Ví dụ, tại Châu Âu, RIPE-512 phác thảo chính sách phân bổ PI.


### Ký hiệu mặt nạ mạng con


Giống như IPv4, IPv6 sử dụng CIDR (*Định tuyến liên miền không phân lớp*). Điều này bao gồm việc chỉ ra số bit tạo nên tiền tố sau Address, sử dụng ký tự `/`.


Hãy lấy ví dụ sau:


```
2001:db8:1:1a0::/59
```


Điều này có nghĩa là 59 bit đầu tiên được cố định và dùng để xác định mạng. Tất cả các bit còn lại (ở đây là 69 bit) có thể được sử dụng để xác định mạng con hoặc máy chủ.


Do đó, ký hiệu này bao gồm các địa chỉ từ `2001:db8:1:1a0:0:0:0:0` đến `2001:db8:1:1bf:ffff:ffff:ffff:ffff`.


Do đó, khối này bao gồm một tập hợp 8/64 mạng con, mỗi mạng có khả năng lưu trữ một số lượng lớn thiết bị.


Ký hiệu CIDR cho phép lập kế hoạch không gian Address chính xác, từ mạng quy mô lớn đến thiết lập tại nhà và môi trường ảo hóa, đồng thời khuyến khích tổng hợp tuyến đường, giảm tải bộ định tuyến và cải thiện khả năng mở rộng.


### Các gói tin và tiêu đề IPv6


Định dạng gói tin IPv6 khác với IPv4 ở chỗ vừa đơn giản hơn vừa có khả năng mở rộng hơn. Một datagram IPv6 luôn bắt đầu bằng một tiêu đề cố định 40 byte chứa tất cả thông tin định tuyến cần thiết. Phương pháp tiếp cận hợp lý này, so với tiêu đề có độ dài biến thiên của IPv4 (từ 20 đến 60 byte), cho phép bộ định tuyến xử lý gói tin nhanh hơn và hiệu quả hơn.


Tuy nhiên, IPv6 không loại bỏ chức năng: thay vì tích hợp nhiều trường tùy chọn vào tiêu đề chính, nó giới thiệu một hệ thống tiêu đề mở rộng, được đặt ngay sau tiêu đề cơ bản. Các tiêu đề tùy chọn này cho phép thêm dữ liệu hoặc hướng dẫn cụ thể cho các chức năng nhất định mà không làm tăng gánh nặng không cần thiết cho các gói tin thông thường.


Một số tiêu đề mở rộng tuân theo cấu trúc cố định, trong khi một số khác có thể chứa số lượng tùy chọn thay đổi. Các tùy chọn này được mã hóa dưới dạng bộ ba `{Type, Length, Value}`:


- Trường "Loại" (1 byte) biểu thị bản chất của tùy chọn;
- Hai bit đầu tiên của "Type" chỉ định bộ định tuyến sẽ làm gì nếu tùy chọn không được nhận dạng:
 - Bỏ qua lựa chọn và tiếp tục điều trị,
 - Thả datagram,
 - Thả và gửi lỗi ICMP đến nguồn.
 - Hủy bỏ datagram mà không cần thông báo (trong trường hợp gói tin đa hướng).
- Trường "Chiều dài" (1 byte) chỉ định kích thước của trường "Giá trị", từ 0 đến 255 byte;
- Trường "Giá trị" chứa dữ liệu liên quan đến tùy chọn.


Sau đây là tổng quan về các loại tiêu đề mở rộng khác nhau được định nghĩa bởi IPv6.


#### Tiêu đề Hop-by-Hop


Tiêu đề này, nếu có, luôn được đặt ngay sau tiêu đề cơ sở. Nó chứa thông tin cần được xử lý bởi mọi bộ định tuyến dọc theo đường đi của gói tin, không giống như hầu hết các tiêu đề khác, thường chỉ được xử lý bởi nút đích. Các ứng dụng điển hình bao gồm báo hiệu các tham số toàn cục hoặc yêu cầu các bước xử lý cụ thể khi gói tin di chuyển qua mạng.


![Image](assets/fr/047.webp)


#### Tiêu đề định tuyến


Tiêu đề định tuyến chỉ định danh sách các địa chỉ trung gian mà gói tin phải đi qua. Có hai chế độ định tuyến chính:


- Định tuyến nghiêm ngặt: đường dẫn chính xác được xác định trước
- Lộ trình lỏng lẻo: chỉ xác định một số bước bắt buộc nhất định.


Bốn trường đầu tiên của tiêu đề gốc này là:


- Tiêu đề tiếp theo**: xác định loại tiêu đề tiếp theo;
- Kiểu định tuyến**: xác định phương pháp định tuyến (thường là `0`);
- Các đoạn còn lại**: số đoạn còn lại để đi qua;
- Address[n]**: danh sách các địa chỉ trung gian.


Trường "Các đoạn còn lại" bắt đầu bằng tổng số đoạn còn lại và giảm đi một ở mỗi bước nhảy.


![Image](assets/fr/048.webp)


#### Tiêu đề phân mảnh


Trong IPv6, chỉ máy chủ nguồn mới được phép phân mảnh một gói dữ liệu, không giống như IPv4, nơi các bộ định tuyến cũng có thể làm điều này. Tất cả các nút IPv6 phải có khả năng xử lý các gói tin có kích thước ít nhất 1280 byte. Nếu bộ định tuyến gặp một gói tin lớn hơn MTU của liên kết tiếp theo, nó sẽ gửi thông báo *ICMPv6 Packet Too Big* trở lại nguồn, sau đó nguồn sẽ điều chỉnh kích thước truyền tải.


Tiêu đề phân mảnh chứa các trường sau:


- Nhận dạng**: mã định danh datagram duy nhất để lắp ráp lại.
- Độ lệch đoạn**: vị trí của đoạn trong gói dữ liệu gốc.
- Cờ M**: chỉ ra liệu có thêm đoạn nào theo sau hay không.


![Image](assets/fr/049.webp)


#### Tiêu đề xác thực (AH)


Tiêu đề này được thiết kế để bảo mật thông tin liên lạc bằng cách xác minh cả tính xác thực của người gửi và tính toàn vẹn của dữ liệu. Tiêu đề này thường được sử dụng với giao thức IPsec. Sử dụng mã xác thực, người nhận có thể xác nhận rằng tin nhắn thực sự đến từ người gửi dự kiến và không bị thay đổi trong quá trình truyền tải.


Trong trường hợp cố gắng sửa đổi gian lận, mã xác thực sẽ không còn khớp nữa và datagram có thể bị từ chối. Cơ chế này cũng bảo vệ chống lại các cuộc tấn công phát lại bằng cách phát hiện các bản sao trái phép.


![Image](assets/fr/050.webp)


#### Tiêu đề Tùy chọn đích


Tiêu đề này chỉ dành cho người nhận cuối cùng của datagram. Nó có thể được sử dụng để thêm các tùy chọn hoặc siêu dữ liệu cụ thể cho ứng dụng mà không cần các bộ định tuyến trung gian lưu ý.


Ban đầu, không có tùy chọn nào như vậy được định nghĩa trong giao thức. Tuy nhiên, tiêu đề này đã được giới thiệu khi IPv6 được thiết kế, để cho phép các phần mở rộng trong tương lai được thêm vào mà không cần sửa đổi cấu trúc gói tin tổng thể. Ví dụ, tùy chọn null chỉ được sử dụng để thêm tiêu đề lên bội số của 8 byte cho mục đích căn chỉnh bộ nhớ.


![Image](assets/fr/051.webp)


Thiết kế gói tin IPv6 được xây dựng dựa trên sự phân tách rõ ràng giữa tiêu đề cơ sở tối thiểu và tiêu đề mở rộng dạng mô-đun. Kiến trúc này đảm bảo cả hiệu suất xử lý tiêu chuẩn và tính linh hoạt cần thiết để phát triển giao thức và tích hợp các cơ chế bảo mật, định tuyến phức tạp hoặc chất lượng dịch vụ, đồng thời duy trì khả năng tương thích với các cơ sở hạ tầng trong tương lai.


## Mối quan hệ giữa IPv6 và DNS


<chapterId>421eacb8-b80b-4aee-910f-e069ed805f00</chapterId>


Trong các mạng hiện đại, DNS (Hệ thống Tên miền) dịch tên miền thành địa chỉ IP mà máy tính có thể sử dụng. Với sự ra đời của IPv6, DNS đã phải thích ứng để hỗ trợ địa chỉ 128 bit trong khi vẫn duy trì khả năng tương thích ngược với IPv4. Sự đồng thời này đặc biệt quan trọng trong môi trường dual-stack, nơi cả hai phiên bản IP hoạt động đồng thời.


### Bản ghi DNS dành riêng cho IPv6


Để liên kết tên miền với IPv6 Address, DNS sử dụng bản ghi AAAA (*quad-A*), tương tự như bản ghi "A" cho địa chỉ IPv4. Bản ghi AAAA ánh xạ rõ ràng tên miền với IPv6 Address.

Ví dụ:


```shell
ipv6.mydmn.org.         IN      AAAA    2001:66c:2a8:22::c100:68b
```


Bản ghi này cho biết tên miền `ipv6.mydmn.org` phân giải thành IPv6 Address `2001:66c:2a8:22::c100:68b`. Có thể, và thậm chí được khuyến nghị để đạt được khả năng tương thích tối đa, kết hợp cùng một tên miền với nhiều địa chỉ IP, dù là IPv4 (thông qua bản ghi A) hay IPv6 (thông qua bản ghi AAAA). Điều này cho phép khách hàng tương thích IPv6 ưu tiên IPv6, đồng thời đảm bảo các khách hàng chỉ sử dụng IPv4 vẫn được hỗ trợ.


Ngoài ra, DNS hỗ trợ phân giải ngược, nghĩa là nó có thể tra cứu tên miền được liên kết với một địa chỉ IP Address nhất định. Trong trường hợp IPv6, thao tác này sử dụng các bản ghi PTR được đặt trong vùng `ip6.arpa`. Vùng này được dành riêng cho phân giải ngược IPv6. Đối với IPv4, đó là vùng `in-addr.arpa`.


### Độ phân giải ngược


Quá trình giải quyết ngược của IPv6 Address tuân theo một quy trình nghiêm ngặt:

1) Mở rộng Address thành ký hiệu thập lục phân đầy đủ (16 byte, tức là 32 chữ số thập lục phân).

Ví dụ:


```shell
2001:66c:2a8:22::c100:68b
```


Trở thành:


```shell
2001:066c:02a8:0022:0000:0000:c100:068b
```


2) Đảo ngược thứ tự của từng chữ số thập lục phân (nibble), phân tách chúng bằng dấu chấm và thêm `ip6.arpa`:


```shell
b.8.6.0.0.0.1.c.0.0.0.0.0.0.0.0.2.2.0.0.8.a.2.0.c.6.6.0.1.0.0.2.ip6.arpa  IN PTR  ipv6.mydmn.org
```


Cấu trúc này đảm bảo việc tra cứu ngược được chuẩn hóa và duy nhất trong không gian IPv6 Address.


**Xin lưu ý**: Truy vấn DNS có thể được truyền qua IPv4 hoặc IPv6. Giao thức truyền tải được sử dụng không ảnh hưởng đến loại bản ghi được trả về.

Ví dụ:


- Máy khách được kết nối qua IPv6 có thể yêu cầu bản ghi IPv4.
- Máy khách được kết nối qua IPv4 có thể yêu cầu bản ghi IPv6.

Máy chủ DNS chỉ phản hồi bằng các bản ghi mà nó có, bất kể giao thức truyền tải của truy vấn là gì.


Khi tên máy chủ được ánh xạ sang cả IPv4 và IPv6, việc lựa chọn sử dụng Address nào sẽ được quy định bởi RFC 6724, trong đó định nghĩa thuật toán lựa chọn Address dựa trên các yếu tố như ưu tiên tiền tố, phạm vi và khả năng tiếp cận. Theo mặc định, IPv6 thường được ưu tiên trừ khi bị ghi đè bởi cấu hình hệ thống hoặc mạng.


**Lưu ý quan trọng**: khi nhúng IPv6 Address vào URL (*Uniform Resource Locator*), địa chỉ này phải được đặt trong dấu ngoặc vuông (`[]`). Điều này tránh nhầm lẫn giữa dấu hai chấm (`:`) bên trong IPv6 Address và dấu hai chấm phân cách tên máy chủ với cổng trong URL.


Ví dụ hợp lệ:


```shell
http://[2001:db8::1]:8080
```


Điều này đảm bảo rằng URL được cả trình duyệt và máy chủ web xử lý chính xác.


Do đó, việc tích hợp IPv6 vào hệ thống DNS dựa vào các loại bản ghi mới, phương pháp nghiêm ngặt để giải quyết ngược và các quy tắc lựa chọn và định dạng chính xác để đảm bảo tính tương thích và tính nhất quán của định tuyến.


### Tóm tắt một phần


Trong phần này, chúng ta đã tìm hiểu các nguyên tắc cơ bản của địa chỉ IPv6. Đầu tiên, chúng ta sẽ xem xét cấu trúc của IPv6 Address: độ dài 128 bit, ký hiệu thập lục phân và các quy tắc đơn giản hóa được sử dụng để rút ngắn các chuỗi số 0 lặp lại. Thiết kế này cho phép IPv6 khắc phục những hạn chế của không gian Address của IPv4, đồng thời đảm bảo khả năng mở rộng và phân cấp hiệu quả.


Sau đó, chúng tôi xem xét các loại địa chỉ IPv6 khác nhau: đơn hướng, bất kỳ hướng nào và đa hướng, trình bày chi tiết phạm vi, cách sử dụng thông thường và cách thể hiện của chúng trong không gian Address.


Tiếp theo, chúng tôi đã xem xét các phương pháp gán địa chỉ IPv6 trong mạng cục bộ, dù là bằng cấu hình thủ công, thông qua giao thức DHCPv6, hay sử dụng các cơ chế tự động cấu hình không trạng thái như cơ chế do NDP cung cấp. Các phương pháp này cho phép thiết bị tự động gán địa chỉ IPv6 (generate) của chính nó từ tiền tố được cung cấp và địa chỉ MAC Address của nó (thông qua EUI-64), đồng thời mang lại sự linh hoạt về quản lý vòng đời và quyền riêng tư.


Chúng tôi cũng đã trình bày chi tiết cách phân bổ các khối Address, bắt đầu từ IANA, nơi phân phối chúng cho năm RIR (*Vùng Internet Đã Đăng ký*), và sau đó đến các ISP, những đơn vị này sẽ phân phối lại chúng cho khách hàng dưới dạng các mạng con (thường là /48, cho phép 65536 /64 mạng con). Sự khác biệt giữa các khối _Provider Aggregatable_ (PA) và _Provider Independent_ (PI) giúp quản lý các tình huống _multihoming_ hoặc thay đổi nhà cung cấp.


Chúng tôi nhận thấy DNS đã thích ứng với IPv6 với sự ra đời của bản ghi AAAA, và các cơ chế phân giải ngược hiện dựa trên vùng `ip6.arpa`. Điều quan trọng là DNS vẫn độc lập với giao thức truyền tải được sử dụng (IPv4 hoặc IPv6), đảm bảo khả năng tương tác liền mạch trong môi trường dual-stack.


Do đó, IPv6 không chỉ là sự cải tiến gia tăng so với IPv4 mà còn là sự thiết kế lại hoàn toàn hệ thống địa chỉ, được xây dựng để đáp ứng cả những thách thức hiện tại và tương lai của Internet toàn cầu.


Trong phần cuối của khóa học NET 302 này, chúng ta sẽ đi vào thực hành và tập trung vào các công cụ chẩn đoán mạng.



# Công cụ chẩn đoán mạng


<partId>368a5c6f-ec48-4b28-970f-3a770788ad37</partId>


## Công cụ truy cập mạng Layer


<chapterId>1d25a21d-6900-4fbe-a438-e06c8afb9e02</chapterId>


Trong chương đầu tiên của phần cuối về chẩn đoán mạng này, chúng tôi tập trung vào các công cụ phân tích truy cập mạng Layer của mô hình TCP/IP. Layer này chịu trách nhiệm giao tiếp trực tiếp giữa các thiết bị trên cùng một mạng vật lý, đặc biệt thông qua việc sử dụng địa chỉ MAC và các giao diện mạng vật lý như card Ethernet hoặc giao diện Wi-Fi.


Mục tiêu ở đây là cung cấp cho quản trị viên các công cụ thiết thực để kiểm tra, thử nghiệm và tối ưu hóa Layer thiết yếu này của kết nối cấp thấp. Các công cụ này có thể được sử dụng để xác minh hoạt động bình thường của giao diện, khắc phục sự cố cấu hình card mạng hoặc phát hiện các bất thường như xung đột, mất gói tin hoặc lỗi liên kết.


### Tiện ích lân cận IP/MAC


#### Công cụ `Arp`


Một trong những công cụ chẩn đoán lâu đời nhất tại Network Access Layer là lệnh `arp`. Mặc dù ngày càng được thay thế bởi các lựa chọn thay thế hiện đại như `ip neigh` (mà chúng ta sẽ sớm tìm hiểu), `Arp` vẫn hiện diện trên nhiều hệ thống để xem hoặc thao tác bộ đệm ARP (*Giao thức Phân giải Address*). Bộ đệm này lưu trữ các ánh xạ giữa địa chỉ IP và địa chỉ MAC được biết cục bộ trên một máy. Nói cách khác, nó cho phép bạn xác định Address vật lý (MAC) nào tương ứng với một địa chỉ IP Address nhất định trên mạng cục bộ.


Trên thực tế, khi một máy chủ muốn gửi một gói tin đến một IP Address trong cùng một mạng con, trước tiên nó phải biết địa chỉ MAC Address của máy đích. Việc ánh xạ này được xử lý bởi ARP, giao thức này sẽ phát một yêu cầu trên mạng cục bộ và nhận được phản hồi chứa địa chỉ MAC Address tương ứng. Kết quả này sau đó được lưu trữ tạm thời trong một bảng cục bộ gọi là "bộ nhớ đệm ARP", để tránh việc lặp lại các yêu cầu cho mỗi gói tin mới.


Để xem nội dung của bộ nhớ đệm này và kiểm tra các mục hiện được máy biết đến, hãy sử dụng:


```bash
arp -a
```


Lệnh này liệt kê tất cả các ánh xạ IP/MAC đã đăng ký cục bộ trên tất cả các giao diện. Mỗi dòng cung cấp tên máy chủ (nếu có thể phân giải được), IP Address, MAC Address tương ứng và Interface nơi ánh xạ được quan sát.


Để lọc màn hình theo IP cụ thể Address, chỉ cần chỉ định:


```bash
arp -a 192.168.1.5
```


Điều này giúp dễ dàng kiểm tra xem có IP Address cụ thể nào đó trong bộ nhớ đệm hay không, từ đó có thể giúp chẩn đoán lỗi giao tiếp giữa hai máy chủ trên cùng một mạng.


Tương tự như vậy, để chỉ hiển thị các mục ARP liên quan đến một mạng Interface cụ thể (ví dụ như card Ethernet có tên `eth0`), bạn có thể sử dụng:


```bash
arp -a -i eth0
```


Điều này đặc biệt hữu ích trong môi trường nhiều Interface (có dây, không dây, VPN, v.v.), trong đó một máy chủ có thể có nhiều bộ điều hợp mạng.


Lệnh `arp` không chỉ giới hạn ở chế độ chỉ đọc. Nó cũng có thể được sử dụng để chỉnh sửa thủ công bộ đệm ARP, một tính năng vô cùng hữu ích trong một số tình huống khắc phục sự cố nâng cao hoặc khi mô phỏng các điều kiện cụ thể. Ví dụ: bạn có thể thêm thủ công ánh xạ IP/MAC:


```bash
arp -s 192.168.1.7 00:17:BC:56:4F:25 -i eth2
```


Lệnh này tạo một mục tĩnh trong bảng ARP cục bộ, liên kết IP Address `192.168.1.7` với MAC Address `00:17:BC:56:4F:25` trên Interface `eth2`. Nếu không chỉ định Interface, hệ thống sẽ tự động sử dụng mục đầu tiên có thể áp dụng.


Bạn cũng có thể xóa một mục khỏi bộ đệm ARP để sửa lỗi hoặc để buộc phải khám phá lại:


```bash
arp -d 192.168.1.7
```


Thao tác này sẽ xóa mục nhập, đảm bảo rằng lần thử giao tiếp tiếp theo sẽ kích hoạt yêu cầu ARP mới.


**LƯU Ý**: Tùy chọn xóa cũng chấp nhận tên Interface, cho phép bạn nhắm mục tiêu xóa một mục cụ thể chính xác hơn.


Tóm lại, công cụ `arp` cung cấp khả năng chẩn đoán cấp thấp, đặc biệt hữu ích trong các mạng cục bộ, nơi các vấn đề kết nối thường có thể bắt nguồn từ việc giải quyết Address không chính xác hoặc lỗi thời. Tuy nhiên, trên các hệ thống gần đây, đặc biệt là với các bản phân phối Linux hiện đại, công cụ này đang ngày càng được thay thế bằng lệnh `ip neigh`, từ bộ công cụ `iproute2`, cung cấp chức năng tương tự trong một khuôn khổ thống nhất hơn.


#### Công cụ `Ip neigh`


Trên các hệ thống hiện đại, đặc biệt là các bản phân phối Linux gần đây, lệnh `ip neigh` là công cụ đắc lực để kiểm tra và quản lý ánh xạ giữa địa chỉ IP và địa chỉ MAC. Lệnh này là một phần của bộ `iproute2`, đang dần thay thế các công cụ cũ hơn như `arp`, cung cấp một khuôn khổ nhất quán và linh hoạt hơn cho việc chẩn đoán tại liên kết dữ liệu Layer.


Lệnh `ip neigh` truy vấn bộ nhớ đệm IP lân cận cục bộ, tương đương với bộ nhớ đệm ARP cho IPv4 và bộ nhớ đệm NDP (Giao thức Khám phá Hàng xóm) cho IPv6. Bộ nhớ đệm này lưu trữ các liên kết đã biết giữa địa chỉ IP (v4 hoặc v6) và địa chỉ MAC, cùng với trạng thái của chúng (hợp lệ, đang chờ xử lý, đã hết hạn...).


Lệnh cơ bản để hiển thị bộ nhớ đệm là:


```bash
ip neigh
```


Lệnh này sẽ đưa ra danh sách các mục nhập, hiển thị địa chỉ IP đích Address, mạng liên quan Interface, MAC Address được liên kết (nếu có) và trạng thái của mục nhập (ví dụ: `REACHABLE`, `STALE`, `DELAY`, `FAILED`...).


Ví dụ đầu ra:


```bash
192.168.1.5 dev eth0 lladdr 00:17:BC:56:4F:25 REACHABLE
```


Dòng này cho biết máy biết về ánh xạ hợp lệ giữa IP Address `192.168.1.5` và MAC Address `00:17:BC:56:4F:25` thông qua Interface `eth0`.


Bạn cũng có thể lọc các mục nhập theo các tiêu chí như IP Address, Interface hoặc tiểu bang. Ví dụ: để chỉ truy vấn Address `192.168.1.7`:


```bash
ip neigh show 192.168.1.7
```


Hoặc để hiển thị tất cả các mục nhập cho Interface `eth1`:


```bash
ip neigh show dev eth1
```


Ngoài việc tham khảo, `ip neigh` cũng có thể được sử dụng để chỉnh sửa bộ nhớ đệm thủ công. Ví dụ: để thêm một mục tĩnh:


```bash
ip neigh add 192.168.1.7 lladdr 00:17:BC:56:4F:25 dev eth1 nud permanent
```


Thao tác này sẽ liên kết vĩnh viễn địa chỉ IP Address `192.168.1.7` với địa chỉ MAC Address được chỉ định trên Interface `eth1`. Tùy chọn `nud permanent` (cho _Neighbor Unreachability Detection_) đảm bảo mục nhập sẽ không bị tự động vô hiệu hóa.


Ngược lại, để xóa mục bộ nhớ đệm:


```bash
ip neigh del 192.168.1.7 dev eth1
```


Điều này buộc hệ thống phải giải quyết lại ánh xạ vào lần tiếp theo khi giao tiếp với Address.


**LƯU Ý**: Công cụ `ip neigh` hoạt động cho cả IPv4 và IPv6. Đối với IPv4, nó giao tiếp với ARP; đối với IPv6, nó tương tác với NDP. Điều này cung cấp một phương pháp thống nhất và nhất quán để quản lý các mối quan hệ IP/MAC trên các họ giao thức, biến `ip neigh` thành tiêu chuẩn hiện đại cho việc quản lý lân cận trên các hệ thống Linux.


### Công cụ phân tích gói


Để phân tích kỹ lưỡng những gì đang diễn ra trên mạng máy tính, quản trị viên cần các công cụ có thể ghi lại các gói tin được trao đổi giữa các máy. Hai tiện ích nổi bật được sử dụng làm chuẩn mực: `tcpdump` và `Wireshark`. Những công cụ này rất cần thiết để chẩn đoán hành vi bất thường, kiểm tra trao đổi giao thức hoặc nghiên cứu bảo mật mạng bằng cách kiểm tra nội dung khung.


#### `ttcpdump`: phân tích dòng lệnh


`tcpdump` là một công cụ dòng lệnh cực kỳ mạnh mẽ được thiết kế để thu thập và hiển thị các gói tin truyền qua mạng Interface. Công cụ này hoạt động theo thời gian thực và nhờ thiết kế gọn nhẹ, có thể được sử dụng trên các hệ thống không có Interface đồ họa hoặc có tài nguyên hạn chế. Công cụ này dựa trên thư viện `libpcap`, cung cấp các chức năng thu thập dữ liệu cấp thấp độc lập với phần cứng.


Một ứng dụng phổ biến của `tcpdump` là giám sát hoạt động mạng của một máy hoặc phân đoạn mạng, lọc các gói tin theo các tiêu chí cụ thể. Kết quả có thể được chuyển hướng đến một tệp, cho phép lưu trữ lưu lượng để phân tích sau hoặc phát lại trong một công cụ khác, chẳng hạn như Wireshark.


Cú pháp lệnh chung là:


```bash
tcpdump -w <file.cap> -i <interface> -s <snapshot_length> -n <filters>
```



- `-w` ghi các gói tin đã chụp vào một tệp ở định dạng `libpcap` (phần mở rộng `.cap` hoặc `.pcap`);
- `-i` chỉ định mạng Interface cần giám sát (ví dụ: `eth0`, `wlan0`);
- `-s` thiết lập lượng dữ liệu tối đa được thu thập trên mỗi gói. Chỉ định `0` sẽ thu thập tất cả các gói;
- `-n` vô hiệu hóa DNS và phân giải tên dịch vụ, cải thiện hiệu suất.


Bộ lọc biểu thức ở cuối lệnh cho phép bạn giới hạn việc thu thập dữ liệu vào một tập hợp con lưu lượng. Bạn có thể kết hợp các từ khóa `host`, `port`, `src`, `dst`, v.v. để tinh chỉnh lựa chọn.


Ví dụ: để thu thập các gói HTTP (cổng 80) đến hoặc đi từ máy chủ `192.168.25.24` và lưu chúng vào tệp `fichier.cap`:


```bash
tcpdump -w fichier.cap -i eth0 -s 0 -n port 80 and host 192.168.25.24
```


Tệp kết quả sau đó có thể được phân tích bằng công cụ đồ họa hoặc phát lại trên hệ thống khác.


#### Wireshark: phân tích hình ảnh nâng cao


Wireshark, trước đây được gọi là *Ethereal*, là một chương trình phân tích mạng hoàn chỉnh với giao diện đồ họa Interface. Không giống như `tcpdump`, Wireshark cung cấp khả năng hiển thị chi tiết và có cấu trúc các gói tin, bao gồm phân tích giao thức, biểu đồ luồng, thống kê lưu lượng và bộ lọc tương tác. Wireshark cũng dựa trên `libpcap`, nghĩa là nó có thể mở và xử lý các tệp capture được tạo bởi `tcpdump`.


Wireshark có sẵn trên nhiều hệ điều hành, bao gồm Linux và Windows. Việc cài đặt Wireshark yêu cầu quyền quản trị viên để truy cập giao diện thu thập dữ liệu. Sau khi khởi chạy, bạn có thể chọn mạng Interface từ menu *Capture*. Nhấp vào *Start* để bắt đầu ghi lại gói tin theo thời gian thực. Màn hình được chia thành ba khung:


- danh sách các khung hình đã chụp;
- chi tiết được giải mã giao thức,
- dữ liệu thập lục phân thô.



![Image](assets/fr/052.webp)



Wireshark vượt trội trong các tình huống cần quan sát hành vi giao thức phức tạp, tái tạo hộp thoại ứng dụng (chẳng hạn như phiên HTTP hoặc DNS) hoặc nghiên cứu thời gian phản hồi của dịch vụ. Wireshark cũng hỗ trợ các bộ lọc hiển thị rất cụ thể bằng cú pháp chuyên dụng (khác với cú pháp của `tcpdump`) để chỉ tập trung vào các gói tin có liên quan.


#### Công cụ bổ sung


Điều quan trọng cần lưu ý là `tcpdump` và Wireshark không thể thay thế cho nhau: mỗi công cụ đều có thế mạnh riêng. `tcpdump` phù hợp hơn với môi trường dòng lệnh, tập lệnh tự động và can thiệp máy chủ từ xa, trong khi Wireshark lý tưởng cho việc phân tích lưu lượng truy cập chi tiết, tương tác và mang tính giáo dục.


Hai công cụ này có thể được kết hợp: có thể thực hiện capture trên một hệ thống từ xa bằng `tcpdump`, sau đó file `.cap` được chuyển để phân tích bằng Wireshark trên máy cục bộ. Cách tiếp cận này được sử dụng rộng rãi trong thực tế.


### Công cụ phân tích Interface


Tại Network Access Layer, việc truy vấn và cấu hình các giao diện mạng vật lý thường là cần thiết để chẩn đoán sự cố, tối ưu hóa hiệu suất hoặc xác minh tính toàn vẹn của kết nối. Một trong những công cụ mạnh mẽ nhất có sẵn trên Linux cho mục đích này là `ethtool`, một tiện ích dòng lệnh không chỉ cung cấp thông tin kỹ thuật chi tiết về Ethernet Interface mà còn cho phép bạn điều chỉnh một số thông số của nó theo thời gian thực.


#### Xem thông số kỹ thuật của Interface


Một tính năng cốt lõi của `ethtool` là khả năng truy vấn Interface và hiển thị các đặc điểm hiện tại của nó. Điều này cho phép bạn kiểm tra:


- tốc độ liên kết (ví dụ: 100 Mbit/giây, 1 Gbit/giây hoặc 10 Gbit/giây);
- chế độ đàm phán (bán song công hoặc toàn song công);
- có bật chế độ tự động thương lượng hay không;
- loại cổng (đồng, cáp quang, v.v.);
- trạng thái liên kết (hoạt động hay không);
- hỗ trợ các tính năng nâng cao như *Wake-on-LAN*.


Thông tin này đặc biệt hữu ích cho việc chẩn đoán các vấn đề liên quan đến kết nối vật lý hoặc cài đặt đàm phán không khớp giữa card mạng của máy chủ và thiết bị mà nó kết nối tới (bộ chuyển mạch, bộ định tuyến, v.v.).


Để có được thông tin này, chỉ cần chạy:


```bash
ethtool enp0s3
```


Lệnh này đưa ra báo cáo chi tiết về `enp0s3` Interface, một quy ước đặt tên phổ biến trên các hệ thống chạy CentOS hoặc RHEL.



![Image](assets/fr/053.webp)



#### Sửa đổi động các tham số Interface


`ethtool` không chỉ giới hạn ở việc quan sát: nó còn cho phép bạn điều chỉnh một số thông số Interface mà không cần khởi động lại máy. Điều này cho phép, ví dụ, áp đặt tốc độ liên kết cụ thể hoặc bật các tính năng theo nhu cầu của mạng cục bộ.


Tùy chọn `-s` được sử dụng để cấu hình động các tham số như:


- tốc độ liên kết (`tốc độ`), được thiết lập rõ ràng (ví dụ: 1000 cho 1 Gbit/giây);
- chế độ song công (`duplex`), có thể là `một nửa` hoặc `toàn bộ`;
- bật hoặc tắt tính năng tự động thương lượng (`autoneg`);
- kích hoạt *Wake-on-LAN* (`wol`);
- loại cổng.


Ví dụ 1: bật tính năng tự động thương lượng trên Interface:


```bash
ethtool -s enp0s3 autoneg on
```


Ví dụ 2: bật tính năng *Wake-on-LAN* (để cho phép máy tính thức dậy từ xa thông qua một gói tin ma thuật):


```bash
ethtool -s enp0s3 wol p
```


Trong ví dụ này, tùy chọn `p` chỉ định rằng việc đánh thức sẽ diễn ra ngay khi phát hiện gói tin *Wake-on-LAN*. Thiết lập này thường được sử dụng trong môi trường doanh nghiệp để thực hiện cập nhật qua đêm hoặc bảo trì từ xa.


#### Cài đặt công cụ


Điều quan trọng cần lưu ý là `ethtool` không phải lúc nào cũng được cài đặt mặc định. Trên các bản phân phối Red Hat/CentOS, bạn có thể cài đặt bằng lệnh:


```bash
yum install -y ethtool
```


Trên Debian và Ubuntu, lệnh tương đương là:


```bash
sudo apt install ethtool
```


**CẢNH BÁO**: trong tất cả các lệnh `ethtool`, tên mạng Interface phải được chỉ định ngay sau tùy chọn (dưới dạng `-s`). Bất kỳ lỗi cú pháp nào trong việc đặt tham số sẽ khiến lệnh không hợp lệ hoặc không hiệu quả.



## Công cụ mạng Layer


<chapterId>d2c5bf35-4284-4af8-8e8b-049c696a511b</chapterId>


### Công cụ phân tích lưu lượng truy cập


Trong chẩn đoán mạng, lệnh `ping` vẫn là một trong những công cụ đơn giản nhưng mạnh mẽ nhất để kiểm tra kết nối giữa hai máy. Lệnh này kiểm tra xem máy chủ từ xa có thể truy cập được tại một thời điểm nhất định hay không, đồng thời cung cấp thông tin về độ trễ, tính ổn định của liên kết và độ phân giải DNS.


Lệnh `ping` dựa trên giao thức ICMP (*Giao thức Tin nhắn Điều khiển Internet*). Khi người dùng gửi yêu cầu `ping`, hệ thống sẽ gửi gói tin ICMP "Echo Request" đến IP Address hoặc tên máy chủ. Nếu máy đích đang trực tuyến và đường dẫn mạng hợp lệ, nó sẽ phản hồi bằng gói tin ICMP "Echo Reply". Cơ chế đơn giản này có thể được sử dụng để đo độ trễ và phát hiện các sự cố kết nối hoặc phân giải tên miền.


Ví dụ về lệnh cổ điển:


```bash
ping 172.17.18.19
```


Phản ứng điển hình:


```bash
mydmn.org (172.17.18.19): 56 data bytes
64 bytes from 172.17.18.19: icmp_seq=0 ttl=56 time=7.7 ms
64 bytes from 172.17.18.19: icmp_seq=1 ttl=56 time=6.0 ms
64 bytes from 172.17.18.19: icmp_seq=2 ttl=56 time=5.5 ms
```


Trong ví dụ này, việc phân giải tên đã được thực hiện tự động: tên miền `mydmn.org` được liên kết với IP Address `172.17.18.19`, xác nhận rằng việc phân giải DNS hoạt động chính xác. Lệnh này cũng cung cấp các chi tiết kỹ thuật như:


- Số thứ tự iCMP (`icmp_seq`), hữu ích để kiểm tra thứ tự phản hồi;
- TTL (*Thời gian tồn tại*), chỉ ra số lượng bước nhảy còn lại trước khi gói tin bị loại bỏ;
- thời gian khứ hồi/độ trễ (`thời gian`), được thể hiện bằng mili giây, cung cấp ước tính về độ trễ liên kết.


#### Phân tích chi tiết hơn về các tham số ICMP


TTL là một trường quan trọng trong giao thức IP. Mỗi datagram được bên gửi khởi tạo với một giá trị TTL (thường là 64, 128 hoặc 255). Mỗi bộ định tuyến trên đường dẫn sẽ giảm giá trị này đi 1. Nếu TTL đạt 0 trước khi đến đích, gói tin sẽ bị loại bỏ và lỗi ICMP sẽ được trả về cho bên gửi. Cơ chế này ngăn ngừa vòng lặp định tuyến vô hạn.


Thời gian lan truyền (*trễ khứ hồi/thời gian*) đo độ trễ của một gói tin từ khi rời khỏi máy gửi, đến đích và quay trở lại. Trên thực tế, độ trễ dưới 200 ms được coi là chấp nhận được đối với một liên kết ổn định. Độ trễ cao bất thường có thể cho thấy tình trạng tắc nghẽn mạng, định tuyến không hiệu quả hoặc chất lượng liên kết kém.


#### Sử dụng `ping` nâng cao


`ping` cung cấp các tùy chọn để tinh chỉnh các bài kiểm tra và quan sát các hành vi mạng cụ thể.


Để gửi yêu cầu phát sóng, bạn có thể sử dụng tùy chọn `-b` để nhắm mục tiêu đến tất cả máy chủ trên một mạng con:

```bash
ping -b 192.168.1.255
```


Tính năng này hữu ích trên mạng cục bộ để nhanh chóng phát hiện các máy chủ đang hoạt động hoặc kiểm tra cách mạng xử lý các yêu cầu phát sóng. Tuy nhiên, trong nhiều thiết lập, bộ định tuyến và tường lửa chặn các lệnh phát sóng để ngăn chặn các cuộc tấn công khuếch đại.


Bạn cũng có thể chỉ định khoảng thời gian tùy chỉnh giữa các yêu cầu bằng tùy chọn `-i` (mặc định: 1 giây):


```bash
ping -i 0.2 -c 10 192.168.1.7
```


Thao tác này sẽ gửi 10 yêu cầu ICMP với khoảng thời gian 0,2 giây. Việc kiểm tra này hữu ích trong việc phát hiện các biến động độ trễ trong thời gian ngắn hoặc để tạo áp lực nhẹ lên một liên kết nhằm đánh giá tính ổn định của nó.


### Công cụ phân tích bảng định tuyến


Lệnh `ip route`, một phần của bộ `iproute2`, là công cụ được khuyến nghị và tiêu chuẩn trên các hệ thống Linux hiện đại để kiểm tra và quản lý bảng định tuyến IP của kernel. Lệnh này thay thế lệnh `route` lỗi thời, cung cấp cú pháp rõ ràng hơn, tính nhất quán cao hơn và hỗ trợ mở rộng cho các tính năng hiện đại (IPv6, nhiều bảng, không gian tên, v.v.).


#### Hiển thị bảng định tuyến


Để hiển thị bảng định tuyến hiện tại:


```bash
ip route show
```


Đầu ra này liệt kê tất cả các tuyến đường mà hạt nhân biết, tức là các đường dẫn mà các gói tin đi qua tùy thuộc vào đích đến của chúng.


Ví dụ đầu ra:


```bash
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```


Mỗi dòng thể hiện một tuyến đường. Các trường chính bao gồm:


- default**: tuyến đường mặc định, được sử dụng khi không có tuyến đường cụ thể nào phù hợp.
- via**: cổng được sử dụng để đến đích.
- dev**: mạng Interface được sử dụng.
- proto**: cách tạo tuyến đường (thủ công, DHCP, kernel, v.v.).
- metric**: chi phí tuyến đường, được sử dụng để ưu tiên nhiều đường dẫn có thể có.
- scope**: phạm vi tuyến đường (ví dụ: `link` cho tuyến đường được kết nối trực tiếp).
- src**: địa chỉ IP nguồn Address được sử dụng cho các gói tin đi trên Interface này.


#### Thêm và xóa tuyến đường


Bạn cũng có thể sửa đổi bảng định tuyến một cách linh hoạt, ví dụ bằng cách thêm hoặc xóa các tuyến tĩnh.


Thêm tuyến tĩnh:


```bash
ip route add 192.168.1.0/24 via 192.168.1.1 dev eth0
```


Cấu hình này sẽ định tuyến đến mạng `192.168.1.0/24` thông qua cổng `192.168.1.1` trên Interface `eth0`.


Xóa tuyến đường này:


```bash
ip route del 192.168.1.0/24
```


Lệnh này xóa tuyến đường đã xác định trước đó.


#### Các lệnh hữu ích


Sau đây là một số biến thể hữu ích để phân tích hoặc viết kịch bản:


- `ip -4 route`: chỉ hiển thị các tuyến đường IPv4;
- `ip -6 route`: chỉ hiển thị các tuyến đường IPv6;
- `ip route list table main`: hiển thị bảng định tuyến chính (giá trị mặc định);
- `ip route get <Address>`: hiển thị Interface và cổng nào mà gói tin đến Address sẽ sử dụng.


Ví dụ:


```bash
ip route get 8.8.8.8
```


Hiển thị lộ trình chính xác mà một gói tin sẽ đi qua để đến được `8.8.8.8`.


### Công cụ theo dõi


Một trong những công cụ hiệu quả nhất để phân tích tuyến đường mà các gói tin IP đi qua giữa máy chủ nguồn và đích là lệnh `traceroute`. Lệnh này hiển thị từng bước đường đi của các gói tin và xác định các bộ định tuyến trung gian mà chúng đi qua. Trong trường hợp đường truyền mạng bị trục trặc hoặc dịch vụ bị gián đoạn, `traceroute` giúp xác định chính xác vị trí sự cố.


Tương tự như lệnh `ping`, mục tiêu có thể được chỉ định bằng tên miền đủ điều kiện (FQDN) hoặc bằng địa chỉ IP Address. Ví dụ:


```bash
traceroute mydmn.org
```


#### Nguyên lý hoạt động


`traceroute` dựa vào trường TTL (*Thời gian tồn tại*) trong tiêu đề gói tin IP. Như đã giải thích trước đó, trường này là một bộ đếm được giảm dần bởi mỗi bộ định tuyến trên đường dẫn. Khi TTL bằng 0, gói tin sẽ bị loại bỏ và bộ định tuyến trả về thông báo ICMP "Đã vượt quá thời gian" cho người gửi. Cơ chế này ngăn ngừa vòng lặp vô hạn trong trường hợp định tuyến sai.


`traceroute` tận dụng hành vi này để ánh xạ các bộ định tuyến giữa người gửi và người nhận:


- Đầu tiên, nó gửi một loạt các gói UDP (thường là ba gói), với TTL là 1. Bộ định tuyến đầu tiên gặp TTL là 0 nên loại bỏ gói tin và sau đó trả lời bằng tin nhắn ICMP, tiết lộ IP Address và thời gian phản hồi.
- Tiếp theo, nó gửi một loạt các gói tin khác có TTL là 2, để lộ ra bộ định tuyến thứ hai.
- Quá trình lặp lại cho đến khi đạt đến đích, tại thời điểm đó, máy chủ sẽ phản hồi bằng thông báo ICMP Port Unreachable, cho biết điểm cuối đã được truy cập.


Theo mặc định, `traceroute` sử dụng các gói UDP được gửi đến các cổng chưa sử dụng (thường bắt đầu từ 33434), nhưng cũng có thể được cấu hình để sử dụng ICMP (như `ping`) hoặc thậm chí là TCP, tùy thuộc vào hệ thống hoặc biến thể lệnh.


Ví dụ đầu ra:


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


Mỗi dòng tương ứng với một bộ định tuyến được duyệt, với tối đa ba phép đo thời gian (tính bằng mili giây) cho biết độ trễ của vòng lặp đến bộ định tuyến đó. Các giá trị này giúp đánh giá hiệu suất của từng phân đoạn mạng.


#### Giải thích kết quả


Nếu bộ định tuyến không phản hồi hoặc lọc tin nhắn ICMP, dấu hoa thị `*` sẽ được hiển thị thay cho thời gian phản hồi. Điều này có thể chỉ ra:


- tường lửa chặn các phản hồi ICMP,
- một thiết bị được cấu hình không phản hồi hoặc
- sự cố kết nối tạm thời dọc theo đường đi.


Do đó, `traceroute` không chỉ xác định tuyến đường đã đi mà còn làm nổi bật các điểm có độ trễ bất thường hoặc gián đoạn.


Trên một số hệ thống, có thể sử dụng lệnh `tracepath` tương đương, không yêu cầu quyền root. Đối với IPv6, hãy sử dụng `traceroute6` hoặc `tracepath6`.


Ví dụ về theo dõi IPv6:


```bash
traceroute6 ipv6.google.com
```


### Công cụ kiểm tra kết nối đang hoạt động


Để chẩn đoán các kết nối mạng đang hoạt động và giám sát hoạt động mạng trên hệ thống Linux, lệnh `ss` (viết tắt của _socket statistics_) là công cụ tham chiếu hiện đại. Là một phần của bộ `iproute2`, lệnh này thay thế lệnh `netstat` hiện đã lỗi thời, mang lại hiệu suất tốt hơn và kết quả chính xác hơn.


`ss` hiển thị các kết nối TCP và UDP đang hoạt động, cổng lắng nghe, địa chỉ cục bộ và từ xa, trạng thái kết nối và các quy trình liên quan.


#### Sử dụng chung


Khi chạy mà không có tùy chọn, lệnh `ss` sẽ hiển thị các kết nối TCP đang hoạt động. Cú pháp cơ bản:


```bash
ss [options]
```


Một số tùy chọn phổ biến để tinh chỉnh phân tích:


- `-t`: chỉ hiển thị các kết nối TCP;
- `-u`: chỉ hiển thị các kết nối UDP;
- `-l`: chỉ hiển thị các ổ cắm đang lắng nghe;
- `-n`: vô hiệu hóa phân giải tên (IP thô và số cổng);
- `-p`: hiển thị từng tiến trình liên kết với ổ cắm (PID và tên chương trình),
- `-a`: hiển thị tất cả các kết nối, bao gồm cả các kết nối không hoạt động,
- `-s`: hiển thị số liệu thống kê ổ cắm cấp cao.


#### Các nghiên cứu điển hình


Để hiển thị tất cả các kết nối đang hoạt động bằng cổng TCP 80 (HTTP):


```bash
ss -ant | grep ':80'
```


Điều này hiển thị các kết nối TCP đang hoạt động liên quan đến cổng 80. Các trạng thái như `LISTEN`, `ESTABLISHED`, `TIME-WAIT` cho biết trạng thái hiện tại của mỗi Exchange.


Ví dụ đầu ra:

```
ESTAB 0 0 192.168.1.10:54321  93.184.216.34:80
```


Để hiển thị tất cả các kết nối mạng với các quy trình liên quan:


```bash
ss -tulnp
```


Để có được bản tóm tắt sử dụng ổ cắm tổng thể:

```bash
ss -s
```


Để chỉ lọc các kết nối UDP:

```bash
ss -unp
```


Các lệnh này đặc biệt hữu ích để phát hiện các kết nối đáng ngờ, cổng nghe lén không mong muốn hoặc theo dõi hoạt động của một dịch vụ cụ thể.


## Vận chuyển và các công cụ hàng đầu Layer


<chapterId>bce47931-930e-4288-b0fd-666c9a1066b5</chapterId>


### Công cụ truy vấn DNS


Ở các tầng trên của mô hình TCP/IP, đặc biệt là tại Ứng dụng Layer, việc hiểu rõ cách thức hoạt động của giải quyết tên miền là rất quan trọng. Các công cụ truy vấn DNS cho phép bạn kiểm tra xem tên miền có được liên kết chính xác với một địa chỉ IP Address hay không, đồng thời giúp chẩn đoán các sự cố máy chủ DNS như cấu hình sai, độ trễ lan truyền hoặc tình trạng không khả dụng. Những công cụ này rất cần thiết cho bất kỳ quản trị viên mạng hoặc người dùng nào muốn hiểu sâu hơn về trao đổi DNS trong môi trường IP.


#### Lệnh `nslookup`


Công cụ truy vấn DNS đơn giản nhất là `nslookup`. Công cụ này gửi một truy vấn đến máy chủ DNS và trả về địa chỉ IP Address được liên kết với tên miền (hoặc ngược lại). Theo mặc định, công cụ này sẽ truy vấn máy chủ DNS đã được cấu hình của hệ thống, nhưng bạn cũng có thể chỉ định máy chủ trực tiếp trong lệnh.


Ví dụ về tra cứu trực tiếp:

```bash
nslookup mydmn.org
```


Truy vấn một máy chủ DNS cụ thể:

```bash
nslookup mydmn.org 192.6.23.4
```


Yêu cầu này yêu cầu máy chủ DNS tại `192.6.23.4` phân giải tên `mydmn.org`. Điều này đặc biệt hữu ích để kiểm tra xem máy chủ DNS có nhận dạng được tên miền hay không hoặc để xác minh rằng máy chủ đang hoạt động bình thường.


#### Lệnh `dig`


`dig` (*Domain Information Groper*) là một công cụ hiện đại, hoàn thiện và linh hoạt hơn `nslookup`. Công cụ này hỗ trợ các truy vấn phức tạp và cung cấp thông tin chi tiết về quy trình giải quyết, hệ thống phân cấp máy chủ liên quan, loại bản ghi được trả về (A, AAAA, MX, TXT, v.v.) và bất kỳ lỗi nào gặp phải.


Ví dụ truy vấn cơ bản:

```bash
dig mydmn.org
```


Truy vấn một máy chủ DNS cụ thể:

```bash
dig @192.6.23.4 mydmn.org
```


Lệnh này kiểm tra tính khả dụng của bản ghi DNS trên một máy chủ nhất định.

Một trong những lợi thế chính của `dig` là nó hiển thị chi tiết phản hồi DNS, rất hữu ích cho việc chẩn đoán lỗi cấu hình.


#### Cấu hình thủ công trình phân giải DNS


Đôi khi, cần phải ghi đè các máy chủ DNS được sử dụng cục bộ, ví dụ như trong môi trường thử nghiệm hoặc buộc sử dụng các máy chủ cụ thể. Việc này có thể được thực hiện bằng cách chỉnh sửa tệp `/etc/resolv.conf`, tệp này định nghĩa cài đặt phân giải DNS của hệ thống.


Cấu hình ví dụ:


```bash
vi /etc/resolv.conf

search mydmn.org
nameserver 192.168.1.10
nameserver 192.168.1.11
```



- Trường `tìm kiếm` chỉ định tên miền sẽ tự động thêm vào khi giải quyết tên viết tắt.
- Các mục `nameserver` xác định các máy chủ DNS sẽ sử dụng theo thứ tự ưu tiên.


Trên nhiều bản phân phối hiện đại (đặc biệt là những bản sử dụng `systemd-resolved`), các thay đổi đối với `/etc/resolv.conf` chỉ mang tính tạm thời và có thể bị ghi đè khi khởi động lại hoặc kết nối lại mạng. Các phương pháp lâu dài hơn bao gồm sử dụng `resolvconf`, `systemd-resolved` hoặc sửa đổi cấu hình *NetworkManager*.


#### Lệnh `host`


Một công cụ DNS đơn giản nhưng hiệu quả khác là `host`. Công cụ này phân giải tên miền thành địa chỉ IP (hoặc ngược lại) và có thể giúp chẩn đoán lỗi DNS hoặc cấu hình sai trên mạng Interface.


Ví dụ:

```bash
host mydmn.org
```


Tra cứu ngược:

```bash
host 192.6.23.4
```


`host` đặc biệt tiện dụng cho việc kiểm tra nhanh, nhất là khi sử dụng trong các tập lệnh dòng lệnh.


Việc truy vấn lặp lại hoặc truy vấn chuyên sâu đến máy chủ DNS của bên thứ ba mà không được phép có thể bị hiểu là nỗ lực xâm nhập hoặc hoạt động độc hại. Nếu sử dụng không đúng cách hoặc nhắm vào các mạng bạn không kiểm soát, các lệnh này có thể giống như quét do thám, thường là bước đầu tiên trong một cuộc tấn công. Luôn hạn chế sử dụng chúng trong các môi trường bạn quản lý hoặc nơi bạn có thẩm quyền rõ ràng.


### Công cụ quét mạng


Khi giám sát hoặc bảo mật mạng cục bộ hoặc mạng diện rộng, điều quan trọng là phải xác định các thiết bị đang hoạt động và các dịch vụ mà chúng cung cấp. Đây chính xác là những gì công cụ `nmap` (*Network Mapper*) thực hiện.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

#### Giới thiệu `nmap`


`nmap` cho phép quét mục tiêu một hoặc nhiều máy chủ để phát hiện các cổng mở, các dịch vụ khả dụng (HTTP, SSH, DNS, v.v.), và đôi khi thậm chí cả loại hệ điều hành đang sử dụng. Nhờ nhiều tùy chọn, `nmap` cung cấp tổng quan chính xác về bề mặt tiếp xúc của mạng, điều cần thiết trong các giai đoạn kiểm tra hoặc củng cố quản lý cơ sở hạ tầng.


Giống như lệnh `host`, `nmap` không bao giờ được sử dụng trên các mạng hoặc cơ sở hạ tầng không thuộc sở hữu của bạn hoặc khi chưa được ủy quyền rõ ràng. Quét cổng trái phép có thể bị gắn cờ là hoạt động do thám độc hại, thường bị phát hiện bởi các hệ thống bảo mật (tường lửa, IDS/IPS) và thậm chí có thể dẫn đến hậu quả pháp lý.


#### Sử dụng cơ bản


Để quét một máy chủ cụ thể và xem các cổng mở của máy chủ đó:

```bash
nmap 192.168.0.1
```


Lệnh này quét 1000 cổng phổ biến nhất trên máy chủ `192.168.0.1` và hiển thị các dịch vụ đã truy cập và giao thức đã sử dụng. Nếu cấu hình phân giải DNS, bạn cũng có thể sử dụng tên máy chủ thay vì IP Address.


#### Quét toàn bộ mạng


Một trong những ưu điểm của `nmap` là khả năng quét toàn bộ dải địa chỉ chỉ bằng một lệnh. Điều này giúp bạn dễ dàng, ví dụ, kiểm kê nhanh chóng tất cả các máy đang hoạt động trên mạng:


```bash
nmap 192.168.0.0/24
```


Trong trường hợp này, tất cả các máy chủ trong phạm vi `192.168.0.0` đến `192.168.0.255` sẽ được truy vấn. Đối với mỗi IP Address, kết quả sẽ liệt kê các cổng đang mở, trạng thái của chúng (đang mở, đã lọc, v.v.) và, nếu có thể, tên của dịch vụ tương ứng.



![Image](assets/fr/055.webp)



Người quản trị có thể dựa vào `nmap` cho một số tác vụ:


- Phát hiện máy chủ đang hoạt động**: xác định máy nào phản hồi trong một mạng con;
- Kiểm kê dịch vụ**: đảm bảo chỉ có thể truy cập được các cổng cần thiết (nguyên tắc đặc quyền tối thiểu);
- Kiểm tra sự tuân thủ**: so sánh các cổng mở với chính sách bảo mật của tổ chức;
- Phòng ngừa lỗ hổng**: phát hiện các dịch vụ không an toàn hoặc lỗi thời đang chạy trên các máy quan trọng.


https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

### Công cụ thẩm vấn quy trình


Để phân tích sâu hơn các tiến trình đang hoạt động và các tệp đang mở, đặc biệt là trong bối cảnh mạng, quản trị viên Linux thường sử dụng lệnh `lsof` (*Liệt kê các tệp đang mở*). Mặc dù có tên như vậy, `lsof` không chỉ giới hạn ở các tệp truyền thống: trên hệ thống UNIX, mọi thứ đều được coi là tệp, bao gồm cả socket mạng, thiết bị và kênh truyền thông.


Do đó, công cụ này cung cấp chế độ xem theo chiều ngang của hệ thống bằng cách liên hệ các quy trình đang hoạt động, cổng mạng mở, tệp được truy cập và người dùng liên quan.


#### Phân tích mạng với `lsof`


Tùy chọn `-i` giới hạn đầu ra ở các kết nối mạng (TCP, UDP, IPv4 hoặc IPv6). Điều này giúp bạn dễ dàng xem những tiến trình nào đang giao tiếp qua mạng:


```bash
lsof -i
```


Lệnh này liệt kê tất cả các tiến trình đang chạy bằng ổ cắm mạng, hiển thị cổng đang sử dụng, giao thức (TCP/UDP), trạng thái kết nối cũng như PID và người dùng liên quan.


#### Lọc theo IP Address hoặc cổng


Bạn có thể tinh chỉnh tìm kiếm bằng cách chỉ định IP Address và một cổng, cô lập một luồng mạng cụ thể. Ví dụ: để kiểm tra phiên SMTP (cổng 25) với một máy chủ cụ thể:


```bash
lsof -n -i @192.168.2.1:25
```


Điều này sẽ chỉ hiển thị các kết nối mạng đang hoạt động với máy chủ `192.168.2.1` trên cổng 25, hữu ích để chẩn đoán hoạt động đáng ngờ hoặc sự cố luồng SMTP.


#### Theo dõi truy cập thiết bị


Một điểm mạnh khác của `lsof` là theo dõi các tệp đặc biệt như phân vùng đĩa. Ví dụ: để kiểm tra những tiến trình nào đã mở tệp trên `/dev/sda1`:


```bash
lsof /dev/sda1
```


Tính năng này hữu ích khi nỗ lực ngắt kết nối không thành công vì thiết bị vẫn đang được sử dụng hoặc khi điều tra ứng dụng nào đang truy cập vào phân vùng.


#### Phân tích chéo: quy trình và mạng lưới


Có thể kết hợp các tùy chọn để có thông tin chi tiết chính xác. Ví dụ: để xem tất cả các cổng mạng được mở bởi một tiến trình có PID 1521:


```bash
lsof -i -a -p 1521
```


Tùy chọn `-a` giao với các tiêu chí (`-i` và `-p`), giới hạn đầu ra chỉ dành cho các kết nối mạng của quy trình đó.


#### Theo dõi nhiều người dùng


`lsof` cũng có thể được sử dụng để phân tích hoạt động của người dùng cụ thể, liệt kê tất cả các tệp họ đã mở, tùy chọn lọc theo PID:


```bash
lsof -p 1521 -u 500,phil
```


Phần này hiển thị các tệp hoặc kết nối mạng được người dùng `phil` hoặc UID 500 sử dụng, giới hạn ở tiến trình 1521.


### Tóm tắt phần


Trong phần cuối này, chúng ta đã khám phá một loạt các công cụ thiết yếu để chẩn đoán, phân tích và quản trị mạng máy tính. Được xây dựng xung quanh các lớp của mô hình TCP/IP, nghiên cứu này không chỉ làm rõ cách thức hoạt động của truyền thông mạng mà còn thiết lập một phương pháp luận chặt chẽ để xác định, cô lập và giải quyết các vấn đề tiềm ẩn.


Các công cụ này cung cấp cho quản trị viên một bộ đòn bẩy kỹ thuật thống nhất để theo dõi tình trạng mạng, phân tích lưu lượng, kiểm tra kết nối và nhanh chóng can thiệp vào thiết bị hoặc dịch vụ bị lỗi.


#### Truy cập mạng Layer


Các công cụ cung cấp khả năng hiển thị trực tiếp vào giao diện và khung:


- arp / ip neigh**: kiểm tra và sửa đổi bộ đệm ARP/NDP để kiểm tra hoặc sửa các liên kết IP-MAC;
- tcpdump**: bắt gói tin bằng dòng lệnh, có thể lọc và xuất;
- Wireshark**: phân tích gói tin đồ họa với giải mã giao thức sâu;
- ethtool**: truy vấn và điều chỉnh các thông số vật lý của card Ethernet (tốc độ, song công, WoL, v.v.).


#### Mạng Layer


Các công cụ để đánh giá kết nối IP, định tuyến và lưu lượng gói tin:


- ping**: kiểm tra khả năng tiếp cận và đo độ trễ bằng ICMP;
- ip route**: kiểm tra và sửa đổi bảng định tuyến để kiểm soát đường dẫn gói tin;
- traceroute**: xác định từng bước nhảy của các bộ định tuyến dọc theo tuyến đường đến đích;
- ss**: danh mục chi tiết các socket TCP/UDP và các tiến trình liên quan (kế nhiệm netstat).


#### Lớp vận chuyển và lớp ứng dụng


Công cụ chẩn đoán dịch vụ và quy trình:


- nslookup / dig / host**: Truy vấn DNS để xác thực việc giải quyết tên và phân tích bản ghi;
- nmap**: khám phá các cổng mở và các dịch vụ dễ bị tấn công để đánh giá bề mặt tấn công;
- lsof**: liệt kê các tệp và ổ cắm được mở bởi các tiến trình, liên kết hoạt động của hệ thống và mạng.


Việc thành thạo các công cụ này, mỗi công cụ được liên kết với một giai đoạn cụ thể của mô hình TCP/IP, cho phép áp dụng một phương pháp tiếp cận bài bản: bắt đầu từ Layer vật lý, chuyển sang định tuyến và lên đến các dịch vụ ứng dụng. Chuỗi kiến thức chuyên môn này trang bị cho quản trị viên khả năng chẩn đoán, bảo mật và tối ưu hóa cơ sở hạ tầng, đảm bảo cả hiệu suất và tính khả dụng của mạng.


# Phần cuối


<partId>09d5393c-63bc-42fc-bf79-c65e380211bd</partId>


## Đánh giá & Xếp hạng


<chapterId>114c33c0-9831-4d74-affd-f5d37adc53c3</chapterId>


<isCourseReview>true</isCourseReview>

## Kỳ thi cuối kỳ


<chapterId>b99e005e-8dd0-4fa4-b302-f940c27a30ac</chapterId>


<isCourseExam>true</isCourseExam>

## Phần kết luận


<chapterId>3b449814-78f3-41c0-8138-0a04f3682719</chapterId>


<isCourseConclusion>true</isCourseConclusion>