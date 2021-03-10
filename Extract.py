import cv2
import imutils
from pyzbar import pyzbar

print( cv2.__version__ )

def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect    
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 3, y - 3), font, 1, (0, 0, 255), 1)       
        with open("barcode_result.txt", mode ='w') as file:
            file.write("Recognized Barcode:" + barcode_info)    
    return frame

cap = cv2.VideoCapture(0)
ret, frame = cap.read()   
if not cap.isOpened():
    print("Error in opening camera")
while ret:
    ret, frame = cap.read()
    frame = read_barcodes(frame)
    cv2.imshow('Barcode/QR code reader', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   
cap.release()
cv2.destroyAllWindows()