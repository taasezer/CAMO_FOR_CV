import cv2
import pytesseract
from datetime import datetime
import logging
import os
import ctypes

# Logging yapılandırma
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# C++ DLL'sini yükle
cpp_dll = ctypes.CDLL('./CAMO_CM_CPP.dll')

def initialize_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        logger.error("Kamera açılamadı!")
        raise IOError("Kamera açılamadı!")
    return cap

def read_label_info(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

def save_video_and_info(name, surname, address, frame):
    data_dir = 'DATASERVICE'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    video_path = os.path.join(data_dir, f'{name}_{surname}_{timestamp}.avi')
    info_path = os.path.join(data_dir, f'{name}_{surname}.txt')

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_path, fourcc, 20.0, (640, 480))
    out.write(frame)
    out.release()

    with open(info_path, 'w') as file:
        file.write(f'Ad: {name}\nSoyad: {surname}\nAdres: {address}\nZaman: {timestamp}')

def main():
    try:
        cap = initialize_camera()
        while True:
            ret, frame = cap.read()
            if not ret:
                logger.error("Kamera görüntüsü alınamadı!")
                break

            cv2.imshow('Kamera Görüntüsü', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                label_info = read_label_info(frame)
                name, surname, address = "Ad", "Soyad", "Adres"
                save_video_and_info(name, surname, address, frame)
                break
    except Exception as e:
        logger.error(f"Ana işlem hatası: {e}")
    finally:
        if 'cap' in locals():
            cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
