from tkinter.ttk import LabeledScale
from manimlib import *


def labeled_circle(text, font_size, circle_height, circle_color):
    labeled_circle = VGroup()

    circle = Circle(color=circle_color)
    circle.set_height(circle_height)

    label = Tex(text, font_size=font_size).move_to(
        circle.get_center())

    labeled_circle.add(label)
    labeled_circle.add(circle)

    return labeled_circle


class MCPNeuron(Scene):
    def construct(self):
        neuron = VGroup()

        input_lbls = ["x_1", "x_2", "x_3", "...", "x_n"]
        weight_lbls = ["w_1", "w_2", "w_3", "...", "w_n"]

        input_signals = VGroup()

        for i in range(0, len(input_lbls)):
            # Render ellipsis without wrapper circle
            if i == 3:
                ellipsis = labeled_circle(
                    "...", 30, .7, "#161925").rotate(PI/2)
                ellipsis1 = labeled_circle(
                    "...", 30, .7, "#161925").rotate(PI/2)

                input_signals.add(
                    VGroup(ellipsis, ellipsis1).arrange(RIGHT, buff=1))
                continue

            line = VGroup()

            weight = labeled_circle(weight_lbls[i], 30, .7, WHITE)
            input = labeled_circle(input_lbls[i], 30, .7, "#161925")

            line.add(input, weight).arrange(RIGHT, buff=1)
            line.add(Line(input, weight))

            input_signals.add(line)

        input_signals.arrange(direction=BOTTOM, buff=0.1)

        summing_junction = labeled_circle(
            "\Sigma", 50, .9, WHITE).next_to(input_signals, buff=1)
        bias = labeled_circle(
            "b", 30, .7, "#161925").next_to(summing_junction, direction=UP, buff=1.7)

        neuron.add(input_signals)
        neuron.add(summing_junction, bias, Line(summing_junction, bias))

        for i in range(0, len(input_signals)):
            if(i != 3):
                neuron.add(Line(input_signals[i][1], summing_junction))

        rec = Rectangle(width=.85, height=.9)
        rec.set_color(WHITE)
        rec_label = Tex("\phi (.)", font_size=40).move_to(rec.get_center())

        activation_function = VGroup(
            rec, rec_label).next_to(summing_junction, buff=1)

        summing_output = Line(summing_junction, activation_function)
        neuron.add(activation_function, summing_output)

        output = labeled_circle("y", 30, .7, "#161925").next_to(
            activation_function, buff=.5)
        neuron.add(output, Line(activation_function, output))
        self.add(neuron)
