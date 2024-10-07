import cv2

source = "PXL_20241003_175730862~2.jpg"
destination = "newImage.png"
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

if src is None:
    print(f"Error: Could not load image from {source}")
else:
    scale_percent = 50

    new_width = int(src.shape[1] * scale_percent / 100)
    new_height = int(src.shape[0] * scale_percent / 100)

    dsize = (new_width, new_height)

    output = cv2.resize(src, dsize)

    if cv2.imwrite(destination, output):
        print(f"Resized image saved as {destination}")
    else:
        print(f"Error: Could not save image to {destination}")

    cv2.imshow('Resized Image', output)

    cv2.waitKey(0)

    cv2.destroyAllWindows()