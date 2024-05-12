import textwrap


def split_text(text: str, width=50) -> list[str]:
    wrapper = textwrap.TextWrapper(width=width)
    return wrapper.wrap(text=text)
