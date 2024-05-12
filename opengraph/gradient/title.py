import svg
from maps import id_maps

THRESHOLD = 40


def title_gradient(text: str):
    add_gradient = False

    if len(text.strip()) >= THRESHOLD:
        add_gradient = True
        text = text[0:37] + "..."

    canvas = svg.Text(
        fill="#ffffff",
        style="white-space:pre",
        font_family="Kokoro",
        font_size="32px",
        font_weight="bold",
        letter_spacing="0rem",
        elements=[
            svg.TSpan(
                x=75,
                y=197.96001,
                text=text,
                style="color:white",
            ),
        ],
    )

    if add_gradient:
        canvas.elements.extend(
            [
                svg.TSpan(
                    x=75,
                    y=197.96001,
                    text=text,
                    fill=f"url('#{id_maps['title_gradient']}')",
                    style="color:white",
                ),
            ]
        )
    return canvas
