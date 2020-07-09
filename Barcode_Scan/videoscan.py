import numpy as np
from pyzbar import pyzbar
import datetime
import time
import argparse
import cv2



# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="barcode.csv",
                help="path to output CSV file containing barcodes")
args = vars(ap.parse_args())


cap = cv2.VideoCapture('last.mp4')

# open the output CSV file for writing and initialize the set of
csv = open(args["output"], "w")
found = set()

while True:
    ret, frame = cap.read()

    barcodes = pyzbar.decode(frame)
    # loop barcode
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # if the barcode text is currently not in our CSV file, write
        # the timestamp + barcode to disk and update the set
        if barcodeData not in found:
            csv.write("{},{}\n".format(datetime.datetime.now(),
                                       barcodeData))
            csv.flush()
            found.add(barcodeData)

    # show the frame
    #cv2.resizeWindow('output', 625,450)
    cv2.imshow('output', frame)

    key = cv2.waitKey(8) & 0xFF
    if key == ord("q"):
        break

cap.release()
csv.close
cv2.destroyAllWindows()
