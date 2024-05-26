import svg
from helpers.image_to_base64 import image_to_base64
from gradient.title import title_gradient
from gradient.secondary_title import secondary_title_gradient
from maps import id_maps

from states.gradients import State as GradientState

gradient_state_machine = GradientState()


def generate_svg(background_image, title):
    canvas = svg.SVG(
        viewBox=[0, 0, 1200, 630],
        width=1200,
        height=630,
        elements=[
            svg.Image(
                width=1200,
                height=630,
                href=image_to_base64(background_image),
            ),
            # Our linear Gradient things
            svg.G(
                elements=[
                    svg.Rect(
                        x=25,
                        y=25,
                        width=1150,
                        height=580,
                        rx=24,
                        fill="#070519",
                        fill_opacity=0.4,
                    ),
                    svg.Rect(
                        x=25,
                        y=25,
                        width=1150,
                        height=580,
                        rx=24,
                        style=f"fill:url(#{id_maps['gradient_1']})",
                    ),
                    svg.Rect(
                        x=25,
                        y=25,
                        width=1150,
                        height=580,
                        rx=24,
                        style=f"fill:url(#{id_maps['gradient_2']})",
                    ),
                ]
            ),
            svg.G(
                elements=[
                    svg.Text(
                        fill="#dcd9f7",
                        style="white-space:pre",
                        font_family="Kokoro",
                        font_size="16px",
                        font_weight="bold",
                        letter_spacing="0rem",
                        elements=[
                            svg.TSpan(
                                x=887.90,
                                y=108.98,
                                text="coreproject.moe",
                            )
                        ],
                    ),
                    svg.Text(
                        fill="#afafaf",
                        style="white-space:pre",
                        font_family="Kokoro",
                        font_size="16px",
                        font_weight="600",
                        letter_spacing="0rem",
                        elements=[
                            svg.TSpan(
                                x=1011.72,
                                y=108.98,
                                text="/anime/163078",
                            )
                        ],
                    ),
                ],
            ),
            svg.G(
                elements=[
                    title_gradient(title),
                    secondary_title_gradient(['HELLLOWORLDDSSDFSDFSD','Fdsafasdsdfsdfsdfasdfasdfsdf']),
                ]
            ),
            
            # Our linear Gradient things
            svg.Defs(
                elements=[
                    svg.LinearGradient(
                        id=f"{id_maps['gradient_1']}",
                        x1=600,
                        y1=25,
                        x2=600,
                        y2=605,
                        gradientUnits="userSpaceOnUse",
                        elements=[
                            svg.Stop(
                                id="stop-50",
                                stop_color="#070519",
                            ),
                            svg.Stop(
                                id="stop-51",
                                offset="1",
                                stop_color="#070519",
                                stop_opacity="0",
                            ),
                        ],
                    ),
                    svg.LinearGradient(
                        id=f"{id_maps['gradient_2']}",
                        x1=25,
                        y1=315,
                        x2=1175,
                        y2=315,
                        gradientUnits="userSpaceOnUse",
                        elements=[
                            svg.Stop(
                                stop_color="#070519",
                            ),
                            svg.Stop(
                                offset="1",
                                stop_color="#070519",
                                stop_opacity="0",
                            ),
                        ],
                    ),
                    # svg.LinearGradient(
                    #     id="paint2_linear_4350_5517",
                    #     x1=75,
                    #     y1=189,
                    #     x2=518,
                    #     y2=189,
                    #     gradientUnits="userSpaceOnUse",
                    #     elements=[
                    #         svg.Stop(
                    #             id="stop-54",
                    #             stop_color="#070519",
                    #             stop_opacity="0",
                    #         ),
                    #         svg.Stop(
                    #             id="stop-55",
                    #             offset="1",
                    #             stop_opacity="0.5",
                    #         ),
                    #     ],
                    # ),
                    # svg.LinearGradient(
                    #     id="paint3_linear_4350_5517",
                    #     x1=384,
                    #     y1=290,
                    #     x2=384,
                    #     y2=476,
                    #     gradientUnits="userSpaceOnUse",
                    #     elements=[
                    #         svg.Stop(
                    #             id="stop-56",
                    #             stop_color="#070519",
                    #             stop_opacity="0",
                    #         ),
                    #         svg.Stop(
                    #             id="stop-57",
                    #             offset="1",
                    #             stop_opacity="0.8",
                    #         ),
                    #     ],
                    # ),
                ]
                + gradient_state_machine.get(),
            ),
        ],
    )

    return canvas


if __name__ == "__main__":
    x = generate_svg("./test.jpg", "Yoru no Kurage wa Oyogenai Me LOVES ACG 1")
    with open("test.svg", "w") as f:
        f.write(str(x))
    print(x)
