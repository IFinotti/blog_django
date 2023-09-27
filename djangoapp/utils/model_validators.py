def validate_png(image):
    if not image.name.lower().endswith('.png'):
        print("It's not a png")