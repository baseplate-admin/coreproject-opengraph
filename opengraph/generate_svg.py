import svg
from helpers.image_to_base64 import image_to_base64
from builder.title import build_title
from builder.secondary_title import build_secondary_title
from builder.description import build_description
from maps import id_maps

from states.gradients import State as GradientState

gradient_state_machine = GradientState()


def generate_svg(background_image, title, secondary_title, description):
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
                    build_title(title),
                    build_secondary_title(secondary_title),
                    build_description(description),
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
    x = generate_svg(
        "./test.jpg",
        "Yoru no Kurage wa Oyogenai Me LOVES ACG 1",
        [
            "HELLLOWORLDDSSDFSDFSD",
            "Fdsafasdsdfsdfsdfasdfasdfsdf",
            "dfasfasdfujasdhufghuweihuiortwehuiorhouiwehrouiewuhrhuioweuhiorwe",
        ],
        """
        "I want to find what I enjoy."
        
Mahiru Kouzuki, a skilled artist, gives up on her passion after her elementary school classmates ridicule her colorful jellyfish mural. Several years later, upon encountering an unexpected admirer in Kano Yamanouchi—a former idol with a troubled past—Mahiru decides to pursue her childhood dreams once more.

Tasked with designing the mascot for Kano's new music project, JELEE, Mahiru enlists the help of her childhood friend and professional streamer Kiui Watase to make JELEE's first music video. Together with Kim Anouk Mei Takanashi, a pianist and fan of Kano's work as an idol, the girls aim to turn JELEE into a global hit. However, if they want to succeed in this ambitious endeavor, they will first have to free themselves from the shackles of their pasts.        """,
    )
    with open("test.svg", "w") as f:
        f.write(str(x))
    # print(x)
