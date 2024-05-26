import svg
from maps import id_maps
from states.gradients import State

import textwrap


COUNTER_THRESHOLD = 7


def build_description(text: str):
    gradient_state_machine = State()
    wrapper = textwrap.TextWrapper(width=60)

    add_gradient = False

    text_list = [i.strip() for i in text.split("\n")]

    actual_text_list = []
    counter = 0
    for i in text_list:
        text = wrapper.wrap(i)

        if len(text) == 0:
            counter += 1

        for j in text:
            if counter > COUNTER_THRESHOLD:
                add_gradient = True
                actual_text_list[-1].text = (
                    actual_text_list[-1].text[0 : len(actual_text_list[-1].text) - 3]
                    + "..."
                )
                break

            actual_text_list.append(
                svg.TSpan(
                    x=75,
                    y=283.6 + (24 * counter),
                    text=j,
                )
            )
            counter += 1

    canvas = svg.G(
        elements=[
            svg.Text(
                fill="#FFF7F8",
                style="white-space:pre",
                font_family="Kokoro",
                font_size="20px",
                letter_spacing="0rem",
                elements=actual_text_list,
            )
        ]
    )
    if add_gradient:
        canvas.elements.extend(
            [
                svg.Text(
                    fill=f"url('#{id_maps['description']}')",
                    style="white-space:pre",
                    font_family="Kokoro",
                    font_size="20px",
                    letter_spacing="0rem",
                    elements=actual_text_list,
                )
            ]
        )

        gradient_state_machine.append(
            svg.LinearGradient(
                id=f"{id_maps['description']}",
                x1="384",
                y1="290",
                x2="384",
                y2="476",
                gradientUnits="userSpaceOnUse",
                elements=[
                    svg.Stop(
                        stop_opacity="0",
                        stop_color="#070519",
                    ),
                    svg.Stop(
                        offset="1",
                        stop_opacity="0.8",
                    ),
                ],
            ),
        )
    return canvas
