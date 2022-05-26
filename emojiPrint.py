from PIL import Image           


def return_image(sentiment):
    if (sentiment == "love"):
        img = Image.open('emoji/love.jpeg')
        img.show()
        

    elif (sentiment == "fear"):
        img = Image.open('emoji/fear.jpeg')
        img.show()

    elif (sentiment == "joy"):
        img = Image.open('emoji/joy.png')
        img.show()

    elif (sentiment == "anger"):
        img = Image.open('emoji/angry.png')
        img.show()

    elif (sentiment == "surprise"):
        img = Image.open('emoji/surprised.jpeg')
        img.show()

    else:
        img = Image.open('emoji/sad.jpeg')
        img.show()

