from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components
import os

# Tell streamlit that there is a component called st_picture_carousel,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
    "st_picture_carousel", path=str(frontend_dir)
)

# Create the python function that will be called
def st_picture_carousel(
        n_pics: Optional[int] = 7,
        cell: Optional[tuple[str, str]] = ('190px', '120px'),
        img_path: Optional[str] = "",
        img_list: Optional[list[str]]=[],
        img_size: Optional[tuple[str, str]] = ('100px', '50px'),
        key: Optional[str] = None,
):
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        n_pics=n_pics,
        cell=cell,
        img_path=img_path,
        img_list=img_list,
        img_size=img_size,
        key=key,
    )

    return component_value


def main():
    st.subheader("Example [st.header]")
    img_list=os.listdir("static/portraits")
    st_picture_carousel(n_pics=9,
                        cell=('300px', '150px'),
                        img_path=r"/static/portraits",
                        img_list=img_list,
                        img_size=('180px', '130px'))

if __name__ == "__main__":
    main()