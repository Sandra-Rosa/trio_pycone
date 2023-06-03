import pynecone as pc

class State(pc.State):
    name = "Trio Pynecone"


def index():
    return pc.hstack(
        pc.heading(State.name, font_size="2em",color="#39FF14"),
        pc.text("Tasks and Delivery", color="white", font_size="1.5em"),
        pc.text("Location", color="white", font_size="1.5em"),
        pc.text("Services", color="white", font_size="1.5em"),
        pc.text("Support", color="white", font_size="1.5em"),
        pc.button(
                    "Become a Tasker",
                    border_radius="1em",
                    margin_top = "1em",
                    position = "fixed",
                    right="2",
                    box_shadow = "rgba(57, 255, 20, 0.8) 0 15px 30px -10px",
                    background_image = "linear-gradient(144deg, #3DFF00, #00FF8C 50%, #00FFC1)",
                    box_sizing="border-box",
                    color="white",
                    _hover={
                        "opacity": 0.85,
                    },  
        )
    )


style = {
    "font_family": "Comic Sans MS",
    "background_color": "#000000",
    pc.Text: {
        "font_family": "Inter",
        "text_align": "center",
        "margin_right": "2em",
        "margin_left": "2em",
        "margin_top" : "1em",
    },
}

app = pc.App(state=State,style=style)
app.add_page(index)
app.compile()