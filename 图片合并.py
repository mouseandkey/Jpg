from PIL import Image
import os

def image_list_read():
    image_path_list = []
    path = ' '
    # 每张图片自己依次输入
    # i = 1
    # while path != '+':
    #     path = input(f'输入第{i}张图片地址: ')
    #     image_path_list.append(path.replace('-', '_'))
    #     i += 1
    # del image_path_list[-1]

    # 输入首尾，批量输入
    path = input('输入图片首尾地址：')
    number, start, end = path.split('-')
    print(number, start, end)
    for i in range(int(start), int(end)+1):
        image_path_list.append(f'{number}_{i}')
    return image_path_list

def image_open(image_path_list):
    im_list = []
    for path in image_path_list:
        image_path = '.\\继母\\' + path + '.jpg'
        img = Image.open(image_path)
        if img.mode == "RGBA":
            img = img.convert('RGB')
            im_list.append(img)
        else:
            im_list.append(img)
    return im_list

def image_connect(im_list, image_path):
    # 计算图片尺寸
    image_width = im_list[0].size[0]
    image_high = 0
    for image in im_list:
        if image.size[0] != image_width:
            with open('error.txt', 'w') as fp:
                fp.write('出现图片宽度不同的情况')
            exit(0)
        else:
            image_high += image.size[1]

    #新建图片
    image_new = Image.new('RGB', (image_width, image_high))
    #开始复制粘贴
    im_high = 0
    for im in im_list:
        image_new.paste(im.copy(), (0, im_high))
        im_high += im.size[1]

    #保存图片
    filename = '.\\temp\\'+image_path+'-'+str(len(im_list))+'.jpg'
    image_new.save(filename)


if __name__ == '__main__':
    image_path_list = image_list_read()
    im_list = image_open(image_path_list)
    image_connect(im_list, image_path_list[0])
    print('成功')
