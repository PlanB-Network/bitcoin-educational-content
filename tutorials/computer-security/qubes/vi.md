---
name: Qubes
description: Một hệ điều hành khá an toàn.
---

![cover](assets/cover.webp)



Qubes OS là một hệ điều hành mã nguồn mở, miễn phí, được thiết kế dành cho những người dùng đặt bảo mật lên hàng đầu. Điểm đặc biệt của nó dựa trên một ý tưởng đơn giản nhưng cấp tiến: thay vì xem xét toàn bộ máy tính, nó chia việc sử dụng thành các phần độc lập gọi là **_qubes_**.



Mỗi qube hoạt động như một **môi trường ảo biệt lập**, với mức độ tin cậy và chức năng cụ thể. Vì vậy, ngay cả khi một ứng dụng bị xâm phạm, cuộc tấn công vẫn chỉ giới hạn trong qube của ứng dụng đó mà không ảnh hưởng đến phần còn lại của hệ thống.



> Nếu bạn nghiêm túc về vấn đề bảo mật, Qubes OS là hệ điều hành tốt nhất hiện nay. - **Edward Snowden**.

Tuy nhiên, việc cài đặt Qubes OS đòi hỏi nhiều sự chuẩn bị hơn so với cài đặt một hệ điều hành thông thường. Việc này bao gồm việc kiểm tra một số điều kiện tiên quyết về phần cứng, hiểu những kiến thức cơ bản về ảo hóa và chấp nhận một trải nghiệm khác biệt, nơi mọi tác vụ hàng ngày đều được xem xét dưới góc độ tách biệt. Nhưng một khi đã được triển khai, Qubes OS cung cấp một nền tảng mạnh mẽ, định nghĩa lại cách bạn tương tác với máy tính hàng ngày. Trong hướng dẫn này, chúng tôi sẽ giải thích cách Qubes OS hoạt động và cách cài đặt dễ dàng trên hệ thống của bạn.



## Hệ điều hành Qubes hoạt động như thế nào?



Hệ điều hành Qubes dựa trên nguyên tắc phân vùng. Thay vì sử dụng một hệ thống duy nhất, nó dựa vào trình quản lý siêu giám sát **Xen** để tạo ra các máy ảo biệt lập, gọi là qube. Mỗi qube được dành riêng cho một tác vụ hoặc mức độ tin cậy cụ thể (công việc, duyệt web cá nhân, giao dịch ngân hàng, v.v.). Sự phân tách này đảm bảo rằng bất kỳ sự xâm phạm nào trong một qube không thể lây lan sang các qube khác, hoạt động như nhiều máy tính độc lập trong một máy duy nhất.



Người dùng Interface được quản lý bởi một miền trung tâm, an toàn có tên là **dom0**. Miền này hoàn toàn tách biệt với Internet, trở thành trái tim của hệ thống. Mặc dù các cửa sổ và menu được hiển thị bởi dom0, việc thực thi thực tế của các ứng dụng diễn ra trong các qube tương ứng của chúng.



## Các loại qubes khác nhau



Xung quanh dom0 có nhiều loại qube khác nhau, mỗi loại có vai trò rất cụ thể.





- **AppVM** được sử dụng để chạy các ứng dụng hàng ngày: người dùng có thể tách biệt email chuyên nghiệp của mình khỏi hoạt động duyệt web hoặc giao dịch ngân hàng, trong khi mỗi môi trường vẫn hoàn toàn độc lập với nhau.





- Các AppVM này dựa trên **TemplateVM**, đóng vai trò là các mẫu tập trung để cài đặt và cập nhật phần mềm, loại bỏ nhu cầu quản lý từng qube riêng biệt.



Hệ điều hành Qubes cũng tích hợp các máy ảo chuyên dụng cho **dịch vụ hệ thống**.





- **NetVM** quản lý trực tiếp các **thiết bị mạng** và đảm bảo kết nối với Internet. Chúng thường được liên kết với **FirewallVM**, can thiệp để **lọc lưu lượng** và hạn chế việc tiếp xúc với các qube khác.





- ServiceVM đóng vai trò tương tự, ví dụ như trong quản lý thiết bị USB, luôn theo cùng một logic: cô lập các thành phần có nguy cơ cao nhất để giảm bề mặt tấn công.



Cuối cùng, đối với các tác vụ thỉnh thoảng hoặc rủi ro, Qubes OS cung cấp **DisposableVM**. Các qube tạm thời này được tạo ra ngay lập tức để **mở một tài liệu đáng ngờ** hoặc **truy cập một trang web đáng ngờ**, sau đó biến mất hoàn toàn khi đóng lại, xóa sạch mọi dấu vết và ngăn chặn mọi cuộc tấn công dai dẳng.



### Cơ chế sao chép an toàn (qrexec)



Việc trao đổi giữa các qube dựa trên **qrexec**, một hệ thống giao tiếp giữa các máy ảo (VM) được thiết kế để bảo mật. Thay vì để các qube giao tiếp tự do, qrexec áp đặt **các chính sách cụ thể**: một tệp được sao chép từ AppVM này sang AppVM khác, hoặc văn bản được truyền qua bảng nhớ tạm, luôn đi qua một kênh được hệ thống giám sát và xác thực. Bằng cách này, ngay cả hành động sao chép và dán đơn giản cũng được kiểm soát để ngăn chặn sự lây lan của phần mềm độc hại.



### Quản lý đĩa



Hệ điều hành Qubes sử dụng một hệ thống quản lý lưu trữ thông minh. TemplateVM chứa cơ sở phần mềm chung, trong khi AppVM chỉ thêm dữ liệu cá nhân và các tệp cụ thể. Điều này giúp giảm dung lượng ổ đĩa sử dụng và tạo điều kiện cho việc cập nhật toàn cầu. Mặt khác, DisposableVM sử dụng các ổ đĩa tạm thời, biến mất hoàn toàn khi đóng. Mô hình này không chỉ đảm bảo tính bảo mật cao hơn mà còn quản lý tài nguyên hiệu quả.



## Tại sao nên chọn hệ điều hành Qubes?



Ưu điểm của Qubes OS nằm ở mô hình bảo mật độc đáo. Cốt lõi của phương pháp này là phân vùng, bảo vệ người dùng bằng cách cô lập từng tác vụ trên các máy ảo riêng biệt. Trên thực tế, một email hoặc trang web độc hại chỉ có thể xâm phạm một qube duy nhất, đảm bảo toàn bộ phần còn lại của hệ thống và dữ liệu cá nhân của bạn được bảo vệ hoàn toàn. Kiến trúc này hạn chế đáng kể các cuộc tấn công phức tạp vốn có thể lan truyền tự do trên một hệ thống thông thường.



Hệ điều hành Qubes cũng mang đến tính minh bạch và khả năng kiểm soát hoàn toàn môi trường kỹ thuật số của bạn. Bạn biết chính xác phần mềm nào có quyền truy cập vào tài nguyên nào, dù là mạng, thiết bị USB hay các thành phần nhạy cảm khác. Hệ thống tích hợp các tính năng bảo mật nâng cao theo mặc định, chẳng hạn như mã hóa toàn bộ ổ đĩa, và hỗ trợ sử dụng các dịch vụ ẩn danh như hệ điều hành Whonix.



https://planb.network/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

Thay vì tìm cách tạo ra một hệ thống bất khả xâm phạm, Qubes OS tập trung vào khả năng phục hồi: nó bao bọc các thiệt hại trong trường hợp bị xâm phạm, giảm thiểu rủi ro cho phần còn lại của hệ thống. Cách tiếp cận thực dụng này khiến Qubes OS trở thành lựa chọn ưu tiên cho người dùng có nhu cầu bảo mật cao hoặc muốn duy trì quyền kiểm soát tối đa đối với cuộc sống số của mình.



## Cài đặt hệ điều hành Qubes



Trước khi cài đặt hệ điều hành Qubes, điều quan trọng là phải đảm bảo phần cứng của bạn đáp ứng các yêu cầu tối thiểu, vì hệ thống dựa vào công nghệ ảo hóa để cô lập Qubes. Các thành phần chính cần kiểm tra là:




- **Bộ xử lý**: Bộ xử lý 64 bit tương thích với công nghệ ảo hóa phần cứng (Intel VT-x hoặc AMD-V).
- RAM: yêu cầu tối thiểu 8 GB, nhưng chúng tôi khuyên dùng RAM 16 GB trở lên để chạy nhiều qube cùng lúc.
- **Không gian lưu trữ**: tối thiểu 36 GB, lý tưởng nhất là 128 GB trên ổ SSD để có hiệu suất tối ưu.



Để cài đặt Qubes OS, hãy tải xuống ảnh ISO chính thức từ [trang web chính thức] của Qubes OS (https://www.qubes-os.org/downloads/). Điều quan trọng là phải kiểm tra tính toàn vẹn của ISO bằng chữ ký GPG được cung cấp để đảm bảo tệp không bị giả mạo và quá trình tải xuống được bảo mật.



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)



Sau khi ISO đã được xác minh, bạn cần tạo một phương tiện cài đặt có thể khởi động, thường là ổ USB. Để thực hiện việc này, hãy tải xuống và cài đặt phần mềm như **Rufus** trên Windows hoặc **Etcher** trên Windows, Linux hoặc macOS. Các công cụ này cho phép bạn sao chép ISO vào ổ USB để có thể khởi động.



Trước khi bắt đầu cài đặt, cần cấu hình **BIOS hoặc UEFI** của máy tính để **bật ảo hóa** và cho phép khởi động từ USB. Tùy thuộc vào kiểu máy, có thể cần phải **tắt Khởi động An toàn**, vì hệ điều hành Qubes có thể không khởi động được khi tùy chọn này được bật.



![0_02](assets/fr/02.webp)



Sau khi đáp ứng các điều kiện này, hãy khởi động lại máy tính và truy cập BIOS/UEFI bằng cách nhấn ngay **Esc**, **Del**, **F9**, **F10**, **F11** hoặc **F12** (tùy theo nhà sản xuất). Trong menu khởi động, hãy chọn ổ USB làm thiết bị khởi động để khởi chạy cài đặt hệ điều hành Qubes.



**Màn hình khởi động**


Khi khởi động từ ổ USB, bạn sẽ được đưa trực tiếp đến menu **GRUB**, nơi bạn có thể chọn hành động cần thực hiện. Sử dụng các phím mũi tên trên bàn phím, chọn "Cài đặt hệ điều hành Qubes" và nhấn "Enter".



![0_03](assets/fr/03.webp)



**Lựa chọn ngôn ngữ** :



Khi quá trình cài đặt bắt đầu, bước đầu tiên là **chọn ngôn ngữ** và **biến thể khu vực** phù hợp với cấu hình của bạn. Điều này đảm bảo các tùy chọn hệ thống và cài đặt được hiển thị chính xác bằng ngôn ngữ bạn muốn.



![0_04](assets/fr/04.webp)



**Cấu hình tham số**:



Ở giai đoạn này, bạn sẽ cần cấu hình một số Elements trước khi khởi chạy cài đặt trên máy của mình.



![0_05](assets/fr/05.webp)



**Bố trí bàn phím**:



Nhấp vào tùy chọn **Bàn phím**, sau đó chọn **bố cục** phù hợp với máy tính của bạn. Sau khi chọn xong, hãy nhấp vào **Kết thúc** để chuyển sang bước tiếp theo.



**Lựa chọn điểm đến** :



Chọn tùy chọn "Đích cài đặt" để chọn ổ đĩa bạn muốn cài đặt hệ điều hành Qubes. Theo mặc định, quá trình phân vùng sẽ diễn ra tự động, cho phép bạn xóa toàn bộ dữ liệu khỏi ổ đĩa và cài đặt hệ thống trên đó. Tuy nhiên, bạn có thể chọn **Tùy chỉnh** hoặc **Tùy chỉnh Nâng cao** để thực hiện phân vùng tùy chỉnh. Sau đó, nhấp vào "Hoàn tất". Hệ thống sẽ yêu cầu bạn đặt **mật khẩu**, hoạt động như một Layer bảo mật để mã hóa dữ liệu của bạn. Hãy đảm bảo chọn một mật khẩu phức tạp và duy nhất.



![0_06](assets/fr/06.webp)



![0_07](assets/fr/07.webp)



**Chọn định dạng ngày và giờ** :


Nhấp vào tùy chọn Giờ và ngày, sau đó chọn khu vực địa lý của bạn. Bạn cũng có thể chọn định dạng giờ mong muốn: 24 giờ hoặc 12 giờ.



![0_08](assets/fr/08.webp)



**Tạo tài khoản người dùng**:


Nhấp vào **Tạo người dùng** để tạo **tài khoản đầu tiên** của bạn, cho phép bạn đăng nhập vào hệ điều hành Qubes.



![0_09](assets/fr/09.webp)



**Kích hoạt tài khoản root** :


Bạn cũng có thể **kích hoạt tài khoản root** bằng cách đặt mật khẩu riêng cho quản trị.



![0_10](assets/fr/10.webp)



Sau khi thực hiện xong các thiết lập này, hãy nhấp vào **Bắt đầu cài đặt** để bắt đầu quá trình.



![0_11](assets/fr/11.webp)



Đợi **kết thúc quá trình cài đặt**, sau đó nhấp vào **khởi động lại hệ thống** để hoàn tất cài đặt và khởi động hệ điều hành Qubes.



![0_12](assets/fr/12.webp)



**Cấu hình bổ sung**:


Sau khi khởi động lại, Qubes OS sẽ nhắc bạn hoàn tất **các mẫu mặc định và cấu hình Qubes**. Nhập mật khẩu đã thiết lập để mã hóa ổ đĩa.



![0_13](assets/fr/13.webp)



Tiếp theo, hãy bắt đầu bằng cách chọn **TemplateVM** bạn muốn cài đặt. Các tùy chọn phổ biến bao gồm **Debian 12 Xfce**, **Fedora 41 Xfce** và **Whonix 17**, tùy chọn thứ hai được khuyến nghị cho các mục đích sử dụng yêu cầu **ẩn danh và bảo mật mạng**. Bạn cũng có thể định nghĩa **mẫu mặc định**, sẽ làm cơ sở cho việc tạo **AppVM** mới.



![0_14](assets/fr/14.webp)



Trong phần **Cấu hình chính**, bạn có thể chọn tự động tạo các qube hệ thống thiết yếu như **sys-net**, **sys-firewall** và **Máy ảo dùng một lần mặc định**. Nên bật tùy chọn cho phép **sys-firewall và sys-usb dùng một lần** để hạn chế việc lộ thông tin thiết bị và mạng trong trường hợp bị xâm phạm. Bạn cũng có thể tạo các **AppVM** mặc định, chẳng hạn như **cá nhân**, **công việc**, **không đáng tin cậy** và **kho lưu trữ**, để sắp xếp các hoạt động của bạn theo mức độ tin cậy của chúng.



![0_15](assets/fr/15.webp)



Hệ điều hành Qubes cũng cho phép bạn tạo **qube dành riêng cho thiết bị USB** (sys-usb) và cấu hình **qube Whonix Gateway và Workstation** để bảo mật thông tin liên lạc của bạn qua mạng Tor. Đối với người dùng nâng cao, phần **Cấu hình nâng cao** cho phép bạn tạo **LVM thin pool** để quản lý hiệu quả không gian đĩa giữa các qube.



Sau khi tất cả các tùy chọn này được cấu hình, hãy nhấp vào **Hoàn tất**, sau đó nhấp vào **Kết thúc cấu hình**. Chờ hệ thống áp dụng các thiết lập này. Sau đó, bạn sẽ được nhắc **đăng nhập vào tài khoản người dùng**, và môi trường Qubes OS của bạn sẽ sẵn sàng sử dụng, bảo mật và được cô lập phù hợp cho các hoạt động khác nhau.



![0_17](assets/fr/17.webp)



Hệ điều hành của bạn hiện đã được cài đặt và sẵn sàng sử dụng.



![0_18](assets/fr/18.webp)



## Tạo một qube trên hệ thống của bạn



Để tạo một qube, quy trình được quản lý bởi công cụ **Qube Manager**, có thể truy cập từ menu Start. Trong cửa sổ công cụ, chỉ cần nhấp vào biểu tượng **Create qube** để mở một cửa sổ cấu hình mới. Trước tiên, hãy nhập tên cho qube của bạn, chẳng hạn như "perso-web" hoặc "work", để xác định mục đích sử dụng.



Tiếp theo, bạn sẽ chọn **Loại** của nó, thường là **AppVM** cho các tác vụ thường xuyên, hoặc **DisposableVM** cho mục đích sử dụng tạm thời. Điều quan trọng là phải chọn **Template** mà qube của bạn sẽ dựa trên, chẳng hạn như "fedora-39" hoặc "debian-12", vì đây sẽ là nền tảng cung cấp hệ điều hành và phần mềm. Bạn cũng sẽ chỉ định **NetVM**, qube chịu trách nhiệm truy cập Internet, theo mặc định là **sys-firewall**.



Cuối cùng, sau khi điều chỉnh dung lượng lưu trữ và RAM (nếu cần), chỉ cần nhấp vào **OK** là quá trình tạo sẽ bắt đầu. Khi quá trình hoàn tất, qube mới của bạn sẽ hiển thị trong danh sách và sẵn sàng để sử dụng.



Tóm lại, Qubes OS không phải là một hệ điều hành thông thường, mà là một giải pháp bảo mật tiên tiến, tái định nghĩa kiến trúc của máy tính cá nhân. Phương pháp tiếp cận của nó, dựa trên việc phân vùng và cô lập thông qua ảo hóa, mang đến khả năng bảo vệ vượt trội trước các mối đe dọa tinh vi nhất. Bằng cách phân chia môi trường làm việc thành các qube chuyên biệt cho từng tác vụ, Qubes OS đảm bảo phần mềm độc hại không thể lây lan và gây nguy hiểm cho toàn bộ hệ thống.



Cho dù bạn cần lướt web an toàn, bảo vệ thông tin nhạy cảm hay làm việc với nhiều mức độ tin cậy khác nhau, Qubes OS đều cung cấp một khuôn khổ minh bạch, linh hoạt. Bằng cách áp dụng các phương pháp hay và tận dụng tối đa các tính năng của hệ điều hành, bạn sẽ có một **pháo đài kỹ thuật số** thích ứng với các mối đe dọa hiện đại. Tìm hiểu thêm về bảo vệ dữ liệu và quyền riêng tư của bạn.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1