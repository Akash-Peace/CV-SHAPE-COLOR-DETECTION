import numpy as np, cv2
def start():
    cap = cv2.VideoCapture(0)
    canvas = None
    rgb = (255, 255, 255)
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)

        # For Color detection
        color_rec = cv2.rectangle(frame, (10, 10), (50, 50), (0, 0, 0), 2)
        cv2.putText(frame, "To change color, show the color inside the box.", (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0, 1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        red_lower = np.array([170, 70, 50], np.uint8)
        red_upper = np.array([180, 255, 255], np.uint8)
        red_mask = cv2.inRange(hsv, red_lower, red_upper)
        green_lower = np.array([25, 52, 72], np.uint8)
        green_upper = np.array([102, 255, 255], np.uint8)
        green_mask = cv2.inRange(hsv, green_lower, green_upper)
        blue_lower = np.array([94, 80, 2], np.uint8)
        blue_upper = np.array([120, 255, 255], np.uint8)
        blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
        kernal = np.ones((5, 5), "uint8")
        red_mask = cv2.dilate(red_mask, kernal)
        #res_red = cv2.bitwise_and(frame, frame, mask=red_mask)
        green_mask = cv2.dilate(green_mask, kernal)
        #res_green = cv2.bitwise_and(frame, frame, mask=green_mask)
        blue_mask = cv2.dilate(blue_mask, kernal)
        #res_blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
        if cv2.mean(red_mask[20:40, 20:40])[0] == 255:
            cv2.putText(frame, "RED color detected", (375, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            rgb = (0, 0, 255)
        elif cv2.mean(green_mask[20:40, 20:40])[0] == 255:
            cv2.putText(frame, "GREEN color detected", (375, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            rgb = (0, 255, 0)
        elif cv2.mean(blue_mask[20:40, 20:40])[0] == 255:
            cv2.putText(frame, "BLUE color detected", (375, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            rgb = (255, 0, 0)

        # For Shape detection and sketching
        if canvas is None:
            canvas = np.zeros_like(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            real_contours = cv2.contourArea(contour)
            if real_contours > 500 and real_contours < 1000:
                approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
                if len(approx) > 3 and len(approx) < 10:
                    cv2.drawContours(frame, [approx], 0, (0, 0, 0), 3)
                    x2, y2, w, h = cv2.boundingRect(approx)
                    canvas = cv2.line(canvas, (x2, y2), (x2, y2), rgb, 5)

        frame = cv2.add(frame, canvas)
        #stacked = np.hstack((canvas, frame))
        cv2.imshow("Virtual Sketch", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()