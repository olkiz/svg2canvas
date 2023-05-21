from svgelements import *
from ConverterABC import ConverterABC

class PyTkConverter(ConverterABC):
    def convert(self, file) -> str:
        svg = SVG.parse(file)
        data = self.__prepareStartString(svg.width, svg.height)
        for element in list(svg.elements()):
            if type(element) is Rect:
                fill = element.fill if element.fill != None else ""
                stroke = element.stroke if element.stroke != None else ""
                x1 = element.x + element.width
                y1 = element.y + element.height
                data += f"canvas.create_rectangle({element.x}, {element.y}, {x1}, {y1}, width={element.stroke_width}, fill=\"{fill}\", outline=\"{stroke}\")\n"
            elif type(element) is Ellipse:
                fill = element.fill if element.fill != None else ""
                stroke = element.stroke if element.stroke != None else ""
                x0 = element.cx - element.rx
                y0 = element.cy - element.ry
                x1 = element.cx + element.rx
                y1 = element.cy + element.ry
                data += f"canvas.create_oval({x0}, {y0}, {x1}, {y1}, width={element.stroke_width}, fill=\"{fill}\", outline=\"{stroke}\")\n"
            elif type(element) is Path:
                fill = element.fill if element.fill != None else ""
                stroke = element.stroke if element.stroke != None else ""
                points = list(element.as_points())
                for segment in element.segments():
                    if type(segment) is Line:
                        data += f"canvas.create_line({segment.start.x}, {segment.start.y}, {segment.end.x}, {segment.end.y}, width={element.stroke_width}, fill=\"{stroke}\")\n"
                    elif type(segment) is Close:
                        data += f"canvas.create_line({segment.start.x}, {segment.start.y}, {segment.end.x}, {segment.end.y}, width={element.stroke_width}, fill=\"{stroke}\")\n"
                    elif type(segment) is CubicBezier:
                        pass
        data += self.__prepareEndString()
        return data

    def __prepareStartString(self, width, height) -> str:
        return f"""import tkinter
top = tkinter.Tk()
canvas = tkinter.Canvas(top, bg="white", height={height}, width={width})
"""
    
    def __prepareEndString(self) -> str:
        return f"""canvas.pack()
top.mainloop()
"""