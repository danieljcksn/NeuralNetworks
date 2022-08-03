from manimlib import *

class MCPNeuron(Scene):
    def construct(self):
        inputsLabels = ["x_1", "x_2", "x_3",
                        "...", "x_n \in \{0, 1\}"]

        circle = Circle()
        circle.set_fill("#161925", opacity=1)
        circle.set_stroke(WHITE, width=3)

        texLabels = VGroup()
        for label in inputsLabels:
            texLabels.add(Tex(label).scale(.8),)

        texLabels.arrange(DOWN, buff=1)

        output = Tex("y \in \{0, 1\}")
        vg = VGroup(texLabels, circle, output).arrange(RIGHT, buff=1)

        edges = VGroup()
        for label in texLabels:
            edges.add(Line(label.get_center(), circle.get_center(), buff=.5))

        edges.add(Line(circle.get_center(), output))

        self.add(edges)
        self.add(vg)
