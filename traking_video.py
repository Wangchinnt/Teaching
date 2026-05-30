import cv2

from ultralytics import YOLO

# Load the YOLO8 model
model = YOLO("yolov8n.pt")

# Object detection with image
# results_of_image = model("cat and dog.jpg", show=True, save=True)

# Open the video file
video_path = "bottle-detection.gif"
cap = cv2.VideoCapture(video_path)
window_name = "YOLO8 Tracking"

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 640, 640)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLO8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True, imgsz=480, conf=0.25, verbose=False)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow(window_name, annotated_frame)
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()