# تشخیص چهره به صورت زنده با استفاده از دوربین
# Real-time Face Recognition using webcam
# توسعه‌دهنده: [ابوالفضل کریمی] - تاریخ: [1403.08.05]

import face_recognition as fr
import cv2

#تنظیمات اولیه (پیکربندی تصاویر مرجع)
# مسیر تصاویر مرجع را وارد کنید
# Set the path and names for reference images
REFERENCE_IMAGES = [
    {"file": "person1.jpg", "name": "Person One"},
    {"file": "person2.jpg", "name": "Person Two"}
]

#تنظیمات نمایش
COLOR_RECT = (0, 0, 255)          # رنگ کادر دور چهره - قرمز / Red
COLOR_TEXT = (255, 0, 0)          # رنگ نوشته - آبی / Blue
FONT = cv2.FONT_HERSHEY_COMPLEX   # نوع فونت / Font style
FONT_SCALE = 1                    # اندازه فونت / Font size
THICKNESS = 2                     # ضخامت خطوط / Thickness

#بارگذاری و رمزگذاری چهره‌های مرجع
# Load and encode reference face images
known_encodings = []
known_names = []

for person in REFERENCE_IMAGES:
    try:
        image = fr.load_image_file(person["file"])
        encoding = fr.face_encodings(image)[0]
        known_encodings.append(encoding)
        known_names.append(person["name"])
    except IndexError:
        print(f"[Error] چهره‌ای در تصویر {person['file']} یافت نشد.")
        print(f"[Error] No face found in the image {person['file']}")
        exit()

#شروع به گرفتن تصویر از وبکم
# Start webcam capture
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        print("[Error] دریافت تصویر از دوربین ناموفق بود.")
        print("[Error] Failed to capture from webcam.")
        break

    # معکوس کردن تصویر برای دید آینه‌ای
    # Flip image horizontally (mirror effect)
    frame = cv2.flip(frame, 1)

    # تبدیل تصویر به RGB
    # Convert image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # پیدا کردن مکان و رمزگذاری چهره‌ها در فریم فعلی
    # Detect face locations and encodings in the current frame
    face_locations = fr.face_locations(rgb_frame)
    face_encodings = fr.face_encodings(rgb_frame)

    # مقایسه چهره‌های پیدا شده با چهره‌های مرجع
    # Compare each detected face with known faces
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = fr.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        # بررسی اینکه آیا چهره‌ای تطابق دارد یا خیر
        # Check if there's any match
        if True in matches:
            match_index = matches.index(True)
            name = known_names[match_index]

        # رسم کادر دور چهره
        # Draw rectangle around face
        cv2.rectangle(frame, (left, top), (right, bottom), COLOR_RECT, 3)

        # نوشتن نام فرد روی تصویر
        # Put name label above the rectangle
        cv2.putText(frame, name, (left, top - 10), FONT, FONT_SCALE, COLOR_TEXT, THICKNESS)

    # نمایش فریم نهایی
    # Show the resulting frame
    cv2.imshow('Face Recognition', frame)

    # برای خروج، کلید 'q' را فشار دهید
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# آزادسازی منابع
# Release resources
cap.release()
cv2.destroyAllWindows()
