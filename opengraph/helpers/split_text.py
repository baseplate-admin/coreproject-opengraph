import textwrap


def split(text: str, width=50) -> list[str]:
    wrapper = textwrap.TextWrapper(width=width)
    return wrapper.wrap(text=text)
