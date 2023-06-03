import pynecone as pc

class State(pc.State):
    name = "Service Masters"


def index():
    return pc.vstack(
        pc.hstack(
        pc.text(State.name, font_size="2.5em",color="#39FF14",font_weight="bold",padding_bottom="0.5em"),
        pc.text("Tasks and Delivery", color="white", font_size="1.5em",margin_left="2em"),
        pc.text("Location", color="white", font_size="1.5em",margin_left="2em"),
        pc.text("Services", color="white", font_size="1.5em",margin_left="2em"),
        pc.text("Support", color="white", font_size="1.5em",margin_left="2em"),
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
        ),
        pc.hstack(
            pc.vstack(
            pc.heading("Home Services",font_size="5em",color="#FFFFFF",text_align="left"),
            pc.text("Discover Service Masters , your go-to platform for finding reliable professionals to handle all your home service needs. From plumbers to electricians, cleaners to carpenters, we connect you with skilled experts who ensure top-quality work. With user-friendly features and thorough screening processes, we make it easy for you to book appointments, read reviews, and enjoy peace of mind. Join our community today and experience the convenience of finding trusted professionals for your dream home.",color="#FFFFFF",text_align="left",margin_left="10em",margin_right="10em"),
            pc.hstack(
            pc.input(placeholder="Enter your service...",color="#FFFFFF"),
            pc.spacer(),
            pc.button("Discover",border_radius="1em",
                    box_shadow = "rgba(57, 255, 20, 0.8) 0 15px 30px -10px",
                    background_image = "linear-gradient(144deg, #3DFF00, #00FF8C 50%, #00FFC1)",
                    color="white",
                    _hover={
                        "opacity": 0.85,
                    }, )
            )
            ),
            pc.vstack(
            pc.image(src="/handyman.png", width="70em",margin_top="10em",margin_right="10em")    
            )
        )
    )


style = {
    "font_family": "Comic Sans MS",
    "background_color": "#000000",
    pc.Text: {
        "font_family": "Inter",
        "text_align": "center",
        "margin_right": "2em",
        "margin_top" : "1em",
    },
}

app = pc.App(state=State,style=style)
app.add_page(index)
app.compile()