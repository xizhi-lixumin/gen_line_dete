
from PIL import Image, ImageDraw
import 


def randomly_gen_junction():
    return 



def draw_line():
    width, height = 100, 100
    # 创建一个新的Image对象，指定大小，模式和背景色：
    img = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建一个ImageDraw对象，关联到Image对象：
    draw = ImageDraw.Draw(img)
    # 使用draw.line方法，在画布上绘制直线，指定起点和终点坐标，颜色和宽度：
    draw.line((25, 25, 75, 75), fill=(0, 0, 0), width=2)
    # 显示或保存修改后的图片：
    img.show()
    # 或img.save(filename)

draw_line()