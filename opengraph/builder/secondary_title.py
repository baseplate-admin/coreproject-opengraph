import svg
from maps import id_maps
from states.gradients import State

THRESHOLD = 100


def build_secondary_title(text: list[str]):
    gradient_state_machine = State()
    text_length = 0
    add_gradient = False

    final_text = []
    for i in text:
        is_last = i == text[-1]

        text_length += len(i)
        if not is_last:
            text_length += 3

        if text_length > THRESHOLD:
            base = text_length - len(i)
            target = THRESHOLD - base - 3
            if target < 0:
                actual_text = "..."
            else:
                actual_text = i[0:target] + "..."

            final_text.append(actual_text)
            add_gradient = True
            break
        else:
            final_text.append(i)

    canvas = svg.Text(
        fill="#AFAFAF",
        style="white-space:pre",
        font_family="Kokoro",
        font_size="16px",
        letter_spacing="0rem",
        elements=[
            svg.TSpan(
                x=75,
                y=234.98,
                # • == &#8226;
                text=" &#8226; ".join(final_text),
                style="color:white",
            ),
        ],
    )

    if add_gradient:
        canvas.elements.extend(
            [
                svg.TSpan(
                    x=75,
                    y=234.98,
                    text=final_text,
                    fill=f"url('#{id_maps['secondary_title']}')",
                    style="color:white",
                ),
            ]
        )

        gradient_state_machine.append(
            svg.LinearGradient(
                id=f"{id_maps['secondary_title']}",
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
