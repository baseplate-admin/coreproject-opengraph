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
                        style="fill:url(#paint0_linear_4350_5517)",
                    ),
                    svg.Rect(
                        x=25,
                        y=25,
                        width=1150,
                        height=580,
                        rx=24,
                        style="fill:url(#paint1_linear_4350_5517)",
                    ),
                ]
            ),
            # Our linear Gradient things
            svg.Defs(
                id="defs57",
                elements=[
                    svg.LinearGradient(
                        id="paint0_linear_4350_5517",
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
                        id="paint1_linear_4350_5517",
                        x1=25,
                        y1=315,
                        x2=1175,
                        y2=315,
                        gradientUnits="userSpaceOnUse",
                        elements=[
                            svg.Stop(
                                id="stop-52",
                                stop_color="#070519",
                            ),
                            svg.Stop(
                                id="stop-53",
                                offset="1",
                                stop_color="#070519",
                                stop_opacity="0",
                            ),
                        ],
                    ),
                    svg.LinearGradient(
                        id="paint2_linear_4350_5517",
                        x1=75,
                        y1=189,
                        x2=518,
                        y2=189,
                        gradientUnits="userSpaceOnUse",
                        elements=[
                            svg.Stop(
                                id="stop-54",
                                stop_color="#070519",
                                stop_opacity="0",
                            ),
                            svg.Stop(
                                id="stop-55",
                                offset="1",
                                stop_opacity="0.5",
                            ),
                        ],
                    ),
                    svg.LinearGradient(
                        id="paint3_linear_4350_5517",
                        x1=384,
                        y1=290,
                        x2=384,
                        y2=476,
                        gradientUnits="userSpaceOnUse",
                        elements=[
                            svg.Stop(
                                id="stop-56",
                                stop_color="#070519",
                                stop_opacity="0",
                            ),
                            svg.Stop(
                                id="stop-57",
                                offset="1",
                                stop_opacity="0.8",
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )

    return canvas


if __name__ == "__main__":
    x = generate_svg("./test.jpg")
    with open("test.svg", "w") as f:
        f.write(str(x))
    print(x)
