from svgelements import *
from ConverterABC import ConverterABC

class SwiftConverter(ConverterABC):
    def convert(self, file) -> str:
        svg = SVG.parse(file)
        shouldAddBezierFunction = False
        data = self.__prepareStartString()
        i = 0
        for element in list(svg.elements()):
            if type(element) is Rect:
                data += f"        let path{i} = UIBezierPath(rect: CGRect(x:{element.x}, y:{element.y}, width: {element.width}, height: {element.height}))\n"
                data += f"        path{i}.lineWidth = {element.stroke_width}\n"
                data += f"        UIColor(hex: 0x{str(element.stroke)[1:]}).setStroke()\n" if element.stroke != None else ""
                data += f"        UIColor(hex: 0x{str(element.fill)[1:]}).setFill()\n" if element.fill != None else ""
                data += f"        path{i}.stroke()\n"
                data += f"        path{i}.fill()\n" if element.fill != None else ""
            elif type(element) is Ellipse:
                data += f"        let path{i} = UIBezierPath(ovalIn: CGRect(x:{element.cx - element.rx}, y:{element.cy - element.ry}, width: {element.rx * 2}, height: {element.ry * 2}))\n"
                data += f"        path{i}.lineWidth = {element.stroke_width}\n"
                data += f"        UIColor(hex: 0x{str(element.stroke)[1:]}).setStroke()\n" if element.stroke != None else ""
                data += f"        UIColor(hex: 0x{str(element.fill)[1:]}).setFill()\n" if element.fill != None else ""
                data += f"        path{i}.stroke()\n"
                data += f"        path{i}.fill()\n" if element.fill != None else ""
            elif type(element) is Path:
                data += f"        let path{i} = UIBezierPath()\n"
                for segment in element.segments():
                    if type(segment) is Move:
                        data += f"        path{i}.move(to: CGPoint(x: {segment.end.x}, y: {segment.end.y}))\n"
                    elif type(segment) is Line:
                        data += f"        path{i}.addLine(to: CGPoint(x: {segment.end.x}, y: {segment.end.y}))\n"
                    elif type(segment) is Close:
                        data += f"        path{i}.close()\n"
                    elif type(segment) is CubicBezier:
                        data += f"        path{i}.addCurve(to: CGPoint(x: {segment.end.x}, y: {segment.end.y}), controlPoint1: CGPoint(x: {segment.control1.x}, y: {segment.control1.y}), controlPoint2: CGPoint(x: {segment.control1.x}, y: {segment.control1.y}))\n"
                data += f"        path{i}.lineWidth = {element.stroke_width}\n"
                data += f"        UIColor(hex: 0x{str(element.stroke)[1:]}).setStroke()\n" if element.stroke != None else ""
                data += f"        UIColor(hex: 0x{str(element.fill)[1:]}).setFill()\n" if element.fill != None else ""
                data += f"        path{i}.fill()\n" if element.fill != None else ""
                data += f"        path{i}.stroke()\n"
            i += 1
        data += self.__prepareEndString(svg.width, svg.height)
        return data

    def __prepareStartString(self) -> str:
        return """import UIKit
extension UIColor {
    init(hex: UInt) {
        self.init(red: CGFloat((hex >> 16) & 0xFF), green: CGFloat((hex >> 8) & 0xFF), blue: CGFloat(hex & 0xFF), alpha: 1.0)
    }
}
class GeneratedCanvasView: UIView {

    override func layoutSubviews() {
        super.layoutSubviews()
        backgroundColor = .white

        setNeedsDisplay()
    }

    override func draw(_ rect: CGRect) {
"""

    def __prepareEndString(self, width, height) -> str:
            return f"""
    }}
}}
let generatedCanvasView = GeneratedCanvasView(frame: CGRect(x: 0, y: 0, width: {width}, height: {height}))

"""