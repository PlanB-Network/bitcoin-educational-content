---
term: CHỮ KÝ ADAPTOR
---

Phương pháp mật mã cho phép kết hợp một chữ ký thực sự với một chữ ký bổ sung (gọi là "chữ ký adaptor") để tiết lộ một phần dữ liệu bí mật. Phương pháp này hoạt động theo cách mà biết hai trong ba yếu tố: chữ ký hợp lệ, chữ ký adaptor, và bí mật cho phép suy ra yếu tố thứ ba còn thiếu. Một trong những đặc tính thú vị của phương pháp này là nếu chúng ta biết chữ ký adaptor của đối tác và điểm cụ thể trên đường cong elliptic liên kết với bí mật được sử dụng để tính toán chữ ký adaptor này, chúng ta có thể suy ra chữ ký adaptor của riêng mình phù hợp với cùng một bí mật, mà không bao giờ cần truy cập trực tiếp vào bí mật đó. Trong một giao dịch giữa hai bên không tin tưởng lẫn nhau, kỹ thuật này cho phép việc tiết lộ đồng thời hai thông tin nhạy cảm giữa các bên tham gia. Quy trình này loại bỏ nhu cầu về sự tin tưởng trong các giao dịch tức thì như Coin Swap hoặc Atomic Swap. Hãy lấy một ví dụ để hiểu rõ hơn. Alice và Bob muốn gửi cho nhau 1 BTC, nhưng họ không tin tưởng lẫn nhau. Do đó, họ sẽ sử dụng chữ ký adaptor để loại bỏ nhu cầu về sự tin tưởng vào bên kia trong giao dịch này (do đó làm cho nó trở thành một giao dịch "nguyên tử"). Họ tiến hành như sau:
* Alice khởi xướng giao dịch nguyên tử này. Cô ấy tạo một giao dịch $m_A$ gửi 1 BTC cho Bob. Cô ấy tạo một chữ ký $s_A$ xác thực giao dịch này bằng khóa riêng $p_A$ ($P_A = p_A \cdot G$), và sử dụng một nonce $n_A$ và một bí mật $t$ ($N_A = n_A \cdot G$ và $T = t \cdot G$): 
$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$
&nbsp;
* Alice tính toán chữ ký adaptor $s_A'$ từ bí mật $t$ và chữ ký thực sự $s_A$:  
$$s_A' = s_A - t$$
&nbsp;
* Alice gửi cho Bob chữ ký adaptor $s_A'$ của mình, giao dịch chưa ký $m_A$, điểm tương ứng với bí mật $T$, và điểm tương ứng với nonce $N_A$. Chúng ta gọi những thông tin này là "adaptor". Lưu ý rằng chỉ với thông tin này, Bob không thể khôi phục được BTC của Alice.
* Tuy nhiên, Bob có thể xác minh rằng Alice không lừa dối anh ta. Để làm điều này, anh ta kiểm tra xem chữ ký adaptor $s_A'$ của Alice có khớp với giao dịch hứa hẹn $m_A$ hay không. Nếu phương trình sau đúng, thì anh ta được thuyết phục rằng chữ ký adaptor của Alice là hợp lệ: 
$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$
&nbsp;
* Việc xác minh này cung cấp cho Bob sự đảm bảo từ Alice, để anh ta có thể tiếp tục quá trình giao dịch nguyên tử với tâm trạng thoải mái. Anh ta sau đó sẽ tạo giao dịch của mình $m_B$ gửi 1 BTC cho Alice và chữ ký adaptor $s_B'$ của mình, sẽ được liên kết với cùng một bí mật $t$ mà chỉ Alice biết cho đến nay (Bob không biết giá trị $t$ này, chỉ biết điểm tương ứng $T$ mà Alice đã cung cấp cho anh ta): $$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$
&nbsp;
* Bob gửi cho Alice chữ ký điều chỉnh của mình $s_B'$, giao dịch chưa ký $m_B$, điểm tương ứng với bí mật $T$, và điểm tương ứng với nonce $N_B$. Alice giờ đây có thể kết hợp chữ ký điều chỉnh của Bob $s_B'$ với bí mật $t$, mà chỉ cô ấy biết, để tính toán một chữ ký hợp lệ $s_B$ cho giao dịch $m_B$ mà gửi BTC của Bob cho cô ấy: $$s_B = s_B' + t$$
&nbsp;
$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$
&nbsp;
* Alice phát sóng giao dịch đã ký này $m_B$ trên blockchain Bitcoin để thu hồi BTC mà Bob đã hứa với cô. Bob biết về giao dịch này trên blockchain. Do đó, anh ta có thể trích xuất chữ ký $s_B = s_B' + t$. Từ thông tin này, Bob có thể tách riêng bí mật nổi tiếng $t$ mà anh ta cần:
$$t = (s_B' + t) - s_B' = s_B - s_B'$$
&nbsp;
* Tuy nhiên, bí mật $t$ này là thông tin duy nhất còn thiếu để Bob tạo ra chữ ký hợp lệ $s_A$, từ chữ ký điều chỉnh của Alice $s_A'$, điều này sẽ cho phép anh ta xác nhận giao dịch $m_A$ gửi một BTC từ Alice cho Bob. Sau đó, anh ta tính toán $s_A$ và lần lượt phát sóng giao dịch $m_A$: $$s_A = s_A' + t$$
&nbsp;
$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$