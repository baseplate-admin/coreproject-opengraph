import svg
from helpers.image_to_base64 import image_to_base64


def generate_svg(background_image):
    canvas = svg.SVG(
        viewBox=[0, 0, 1200, 630],
        width=1200,
        height=630,
        elements=[
            svg.Image(
                width=1200,
                height=630,
                href=image_to_base64(background_image),
            )
        ],
    )

    return canvas


if __name__ == "__main__":
    x = generate_svg("./test.jpg")
    with open("test.svg", "w") as f:
        f.write(str(x))
    print(x)
