from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout


class Start(App):
    def build(self):
        f = FloatLayout()
        label1 = Label(text="Running App")

        f.add_widget(label1)
        import frames_from_video_mp4
        frames_from_video_mp4.just_pass()

        return f


if __name__ == "__main__":
    Start().run()

