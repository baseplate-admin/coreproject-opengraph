import svg
from maps import id_maps
from states.gradients import State

THRESHOLD = 40


def secondary_title_gradient(text: list[str]):
    gradient_state_machine = State()
    text_length = len("".join(text))
    add_gradient = False

    if text_length > THRESHOLD:
        add_gradient = True

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
                y=234.98,
                # • == &#8226;
                text=" &#8226; ".join(text),
                style="color:white",
            ),
        ],
    )

    return canvas
