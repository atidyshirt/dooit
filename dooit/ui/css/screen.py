from dooit.utils.default_config import *  # noqa


screen_CSS = f"""
Screen {{
    background: {BACKGROUND};
    layout: grid;
    grid-size: 2 2;
    grid-columns: 2fr 8fr;
    grid-rows: 1fr 1;
}}

StatusBar {{
    column-span: 2
}}
"""