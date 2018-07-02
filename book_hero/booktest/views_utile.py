from io import BytesIO

from django.http import HttpResponse


def verifycode(request):
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    import random

    # 定义变量，用于画面的背景色，宽，高
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 25

    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)  # 画布

    # 创建画笔对象
    draw = ImageDraw.Draw(im)  # 此画笔用于画面对象书写

    # 调用画笔的point()函数给画布对象绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))  # 变量，只不过就被叫做xy，叫做a, b, 任何东西都可以
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))  # (R, G, B) 随机生成三原色
        draw.point(xy, fill=fill)  # 把点画上去

    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 生成4位验证码

    # 构造字体对象
    font = ImageFont.truetype(font='file/hktt.ttf', size=23)

    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))

    # 绘制四个字体
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)

    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str

    buffer = BytesIO()  # 缓存
    im.save(buffer, 'png')  # 指定图片的格式为png

    # 释放画笔
    del draw
    del im
    return HttpResponse(buffer.getvalue(), 'image/png')

























