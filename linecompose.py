from lxml import etree
from io import StringIO, BytesIO
from random import randint
import fire
import math


def create_svg_root(canvas_height, canvas_width):
    xml = f'<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 {canvas_height} {canvas_width}" enable-background="new 0 0 {canvas_height} {canvas_width}" xml:space="preserve"></svg>'
    tree = etree.parse(StringIO(xml))
    svg = tree.getroot()
    return svg


def random_color(x):
    color_list = ["black", "white"]
    random_number = randint(0, len(color_list)-1)
    random_color = color_list[random_number]
    return random_color

def rand_seperated(min=10000 ,max=1000000):
    return seperated(randint(min, max))


def seperated(number):
    """Split number in groups of thousends"""
    s = '%d' % number
    groups = []
    while s and s[-1].isdigit():
        groups.append(s[-3:])
        s = s[:-3]
    return s + '.'.join(reversed(groups))


def compose():
    svg = create_svg_root(1000, 1000)

    for x in range(3000):
        line = etree.Element("line", stroke="#1D1D1B", x1=str(rand_seperated()), y1=str(rand_seperated()), x2=str(rand_seperated()), y2=str(rand_seperated()))
        svg.append(line)

    svg_file = open("Output.svg", "w")
    svg_file.write(etree.tostring(svg).decode("utf-8"))
    svg_file.close()

if __name__ == '__main__':
  fire.Fire()