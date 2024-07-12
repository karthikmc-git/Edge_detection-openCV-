import cv2

def live_edge_detection(image):
    t1 = 30
    t2 = 100
    gi = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gi, t1, t2)
    return canny

video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    ret, frame = video.read()
    if not ret:
        print("Error: Failed to read frame.")
        break

    edges = live_edge_detection(frame)
    
    cv2.imshow('Live Edge Detection', edges)
    cv2.imshow('Normal Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
