import svg
from maps import id_maps
from states.gradients import State

THRESHOLD = 40


def title_gradient(text: str):
    gradient_state_machine = State()
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

        gradient_state_machine.append(
            svg.LinearGradient(
                id=f"{id_maps['title_gradient']}",
                x1="0",
                y1="15",
                x2="498.196",
                y2="15",
                gradientUnits="userSpaceOnUse",
                elements=[
                    svg.Stop(
                        offset="0%",
                        stop_color="rgba(7, 5, 25, 0)",
                    ),
                    svg.Stop(
                        stop_color="rgba(0, 0, 0, 0.3)",
                        offset="71.68%",
                    ),
                ],
            ),
        )
    return canvas
