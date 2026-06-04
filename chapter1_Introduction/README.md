# YOLOv8 Demo - Lesson 1

Dự án này dùng để demo YOLOv8 cho bài học đầu tiên. Script hiện tại là `traking_video.py`, chạy detection/tracking trên video với model `yolov8n.pt`.

## 1. Cài Python

Tải Python từ trang chính thức:

https://www.python.org/downloads/

Khuyến nghị dùng Python 3.10 trở lên. Khi cài trên Windows, nhớ tick `Add Python to PATH`.

Kiểm tra sau khi cài:

```bash
python --version
pip --version
```

## 2. Tạo môi trường ảo

Mở terminal tại thư mục dự án và chạy:

```bash
python -m venv .venv
```

Kích hoạt môi trường ảo:

```bash
.venv\Scripts\activate
```

Nếu dùng PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## 3. Cài thư viện

Sau khi đã activate `.venv`, cài thư viện cần thiết:

```bash
pip install ultralytics opencv-python
```

Nếu máy chưa có PyTorch phù hợp, `ultralytics` sẽ tự kéo các gói cần thiết trong đa số trường hợp. Nếu gặp lỗi CUDA/GPU, có thể cài bản PyTorch phù hợp theo hướng dẫn chính thức của PyTorch.

## 4. Chạy demo

Chạy file:

```bash
python traking_video.py
```

Script hiện tại sẽ:

- mở video `eg4.mp4`
- dùng model `yolov8n.pt`
- vẽ kết quả detection/tracking lên khung hình

Nhấn `q` để thoát.

## 5. Ghi chú cho buổi demo

- `yolov8n.pt` là model nhẹ, chạy nhanh, phù hợp demo realtime.
- Model COCO gốc nhận diện rất tốt người, xe, vật dụng phổ biến, nhưng không mạnh với trái cây nếu chưa fine-tune.
- Nếu muốn demo trái cây tốt hơn, nên dùng custom dataset và train lại model.

## 6. Cấu trúc hiện tại

- `traking_video.py`: script chạy YOLOv8 trên video
- `yolov8n.pt`: model nhẹ để demo
- `eg1.mp4`, `eg2.mp4`, `eg3.mp4`: video mẫu
- `bottle-detection.gif`: ảnh demo
