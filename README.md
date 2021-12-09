# Xây dựng web khai thác ngữ liệu song ngữ Anh-Việt
Để thuận tiện cho việc nghiên cứu, thống kê, so sánh, đối chiếu giữa hai ngôn ngữ: tiếng Anh và tiếng Việt. Trang web này được xây dựng để giúp thực hiện điều đó

## Kho ngữ liệu song ngữ Anh-Việt
- Ngữ liệu song ngữ Anh-Việt được trích một phần từ kho ngữ liệu song ngữ EVC do các nhà nghiên cứu của Trường ĐH Khoa học Tự nhiên – Tp.HCM xây dựng.
- Các bản dịch tương ứng của mỗi ngôn ngữ được đặt song song với nhau (gióng hàng).

## Các chức năng trong trang web
#### 1. Hiển thị song ngữ Anh-Việt
- Hiển thị một số câu trong ngữ liệu và đã được gióng hàng ở cấp độ từ.
- Sự khác biệt về loại hình ngôn ngữ giữa tiếng Anh (biến hình) và tiếng Việt (đơn lập) làm nên sự khác biệt trong ranh giới từ giữa 2 ngôn ngữ.

    - VD: "học sinh" là 1 từ trong tiếng Việt, trong khi "student" là 1 từ trong tiếng Anh.\
    Không thể dùng cách tách từ của tiếng Anh (mỗi từ cách nhau một khoảng trắng) cho tiếng Việt. Vì vậy để phân đoạn từ cho tiếng Việt chúng ta cần một phương pháp khác để phù hợp với loại hình ngôn ngữ đơn lập.
- Ngữ liệu song ngữ sau khi được phân đoạn từ sẽ tiến đến gióng hàng từ.

#### 2. Tìm kiếm
Tìm kiếm một từ trong ngữ liệu, kết quả trả về là câu chứa chính xác từ đó. Song song với mỗi câu là câu đã được dịch ở ngôn ngữ kia.

  VD: Từ tìm kiếm: displays\
  "A special function key that **displays** the help menu ."\
  "Một phím chức_năng đặc_biệt __trình_bày__ trên màn_hình thực_đơn hỗ_trợ ."
  
#### 3. Thống kê
Thống kê dữ liệu, hiển thị những từ với tần số xuất hiện của chúng trong ngữ liệu.

**Hướng đi của đề tài**

| **STT** | **Miêu tả chức năng cơ bản** | **Miêu tả chức năng nâng cao (nếu có thể)** |
| --- | :-- | :-- |
| 1 | Dùng ngữ liệu có sẵn | Thu thập ngữ liệu thô từ các website song ngữ|
| 2 | Hiển thị song ngữ Anh-Việt đã được tách từ, gióng hàng | Hiển thị ngẫu nhiên song ngữ mỗi lần truy cập<br> Thêm nhãn từ loại|
| 3 | Tìm kiếm từ trong một câu | Tìm kiếm từ dựa vào từ loại<br>Tìm kiếm từ dựa vào hình thái từ|
| 4 | Thống kê tần xuất xuất hiện của một từ| |
