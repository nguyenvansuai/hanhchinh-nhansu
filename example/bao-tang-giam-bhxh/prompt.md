# Prompt – Báo tăng, giảm BHXH tháng 11

## Chuẩn bị (trước giờ dạy)

1. Cài plugin Hành chính – Nhân sự (trọn bộ, hoặc tối thiểu skill `bhxh-che-do`).
2. Bật **Code execution** (claude.ai: Settings → Capabilities; ChatGPT: Code Interpreter).
3. Mở cuộc trò chuyện mới, **đính kèm 3 file trong `dau-vao/`**: `thong-tin-cong-ty.md`, `danh-sach-dong-bhxh-thang-10.xlsx`, `bien-dong-nhan-su-thang-11.xlsx`.

## Prompt demo (chép nguyên văn)

```
Tôi là HCNS Công ty TNHH Công nghệ Bình Minh (thông tin đính kèm).
Đính kèm danh sách đang đóng BHXH tháng 10/2026 và ghi chú biến động nhân sự tháng 11/2026. Hãy:
1. Lập danh sách báo tăng, giảm, điều chỉnh BHXH tháng 11: họ tên, mã số, phương án, từ tháng, mức lương đóng, lý do.
2. Chỉ ra trường hợp dễ làm sai và giải thích vì sao.
3. Tính tổng tiền BHXH, BHYT, BHTN phải nộp tháng 11 (phần người lao động và phần công ty), so với tháng 10.
4. Liệt kê giấy tờ cần thu và việc phải làm với từng người.
Xuất danh sách ra Excel.
```

Kết quả đúng: xem `ket-qua-mau/ket-qua.md` – **7 người kê khai** (2 tăng, 3 giảm, 2 điều chỉnh), anh Cường **vẫn đóng tháng 11** và báo giảm từ tháng 12, chị Bình và chị Giang không kê khai; **tổng nộp tháng 11: 55.260.000đ** (người lao động 18.164.500đ, công ty 37.095.500đ).

## Prompt hỏi tiếp (nếu còn thời gian)

```
Soạn tin nhắn hướng dẫn chị Dung nộp giấy tờ hưởng chế độ thai sản và cho biết chị được nghỉ, được hưởng thế nào.
```

```
Anh Cường nghỉ việc thì được hưởng trợ cấp thất nghiệp không? Soạn hướng dẫn gửi anh ấy.
```

## Prompt đầy đủ khi đã kết nối Drive, Gmail, Calendar (chỉ giảng trên slide, không demo)

```
Đọc file "Danh sách lao động" và các quyết định nhân sự tháng 11 trong thư mục "Nhân sự/2026" trên Drive,
lập danh sách báo tăng – giảm BHXH tháng 11 và lưu vào thư mục "BHXH/2026/T11",
tạo nháp email hướng dẫn giấy tờ gửi riêng từng người,
và tạo nhắc hạn trên lịch: nộp hồ sơ tháng 11, chốt sổ cho anh Cường, báo tăng lại anh Em ngày 01/12.
```

Lý do không demo phần connector: dữ liệu nhân sự thật nằm rải rác nhiều file, quyền truy cập Drive mỗi lớp mỗi khác. Đặt sẵn file trong `dau-vao/` cho kết quả ổn định.
