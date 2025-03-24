import streamlit as st
import os
import time
from manim import *

def create_birthday_animation():
    class BirthdayScene(Scene):
        def construct(self):
            text = Text("Happy Birthday!").scale(2).set_color_by_gradient(RED, ORANGE, YELLOW)
            self.play(Write(text))
            self.wait(2)
            self.play(FadeOut(text))

    output_path = "birthday.mp4"
    if not os.path.exists(output_path):
        BirthdayScene().render()
        os.rename("media/videos/scene/480p15.mp4", output_path)

def main():
    st.title("🎉 Birthday Celebration App")
    st.write("Enjoy a birthday animation for your loved ones!")
    
    if st.button("Play Animation 🎥"):
        create_birthday_animation()
        time.sleep(2)  # Give time for the animation to be created
        st.video("birthday.mp4")
    
    st.image("https://cdn.pixabay.com/photo/2017/02/01/10/31/happy-birthday-2029626_960_720.png", caption="Happy Birthday!")

if __name__ == "__main__":
    main()


