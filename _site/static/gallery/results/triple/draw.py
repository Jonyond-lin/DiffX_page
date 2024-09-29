import os
from PIL import Image
from torchvision import transforms
from torchvision.transforms.functional import resize
from torchvision.utils import save_image

def image_list(path):
    transform = transforms.Compose([
        transforms.Resize((2048, 2048), interpolation=Image.BICUBIC),
        transforms.ToTensor()
    ])
    image1_1 = os.path.join(path, '1-1.jpg')
    image1_2 = os.path.join(path, '1-2.jpg')
    image1_3 = os.path.join(path, '1-3.jpg')
    image1_4 = os.path.join(path, '1-4.jpg')
    image1_5 = os.path.join(path, '1-5.jpg')

    image2_1 = os.path.join(path, '2-1.jpg')
    image2_2 = os.path.join(path, '2-2.jpg')
    image2_3 = os.path.join(path, '2-3.jpg')
    image2_4 = os.path.join(path, '2-4.jpg')
    image2_5 = os.path.join(path, '2-5.jpg')

    image3_1 = os.path.join(path, '3-1.jpg')
    image3_2 = os.path.join(path, '3-2.jpg')
    image3_3 = os.path.join(path, '3-3.jpg')
    image3_4 = os.path.join(path, '3-4.jpg')
    image3_5 = os.path.join(path, '3-5.jpg')

    image4_1 = os.path.join(path, '4-1.jpg')
    image4_2 = os.path.join(path, '4-2.jpg')
    image4_3 = os.path.join(path, '4-3.jpg')
    image4_4 = os.path.join(path, '4-4.jpg')
    image4_5 = os.path.join(path, '4-5.jpg')

    image1_1 = transform(Image.open(image1_1).convert('RGB'))
    image1_2 = transform(Image.open(image1_2).convert('RGB'))
    image1_3 = transform(Image.open(image1_3).convert('RGB'))
    image1_4 = transform(Image.open(image1_4).convert('RGB'))
    image1_5 = transform(Image.open(image1_5).convert('RGB'))

    image2_1 = transform(Image.open(image2_1).convert('RGB'))
    image2_2 = transform(Image.open(image2_2).convert('RGB'))
    image2_3 = transform(Image.open(image2_3).convert('RGB'))
    image2_4 = transform(Image.open(image2_4).convert('RGB'))
    image2_5 = transform(Image.open(image2_5).convert('RGB'))

    image3_1 = transform(Image.open(image3_1).convert('RGB'))
    image3_2 = transform(Image.open(image3_2).convert('RGB'))
    image3_3 = transform(Image.open(image3_3).convert('RGB'))
    image3_4 = transform(Image.open(image3_4).convert('RGB'))
    image3_5 = transform(Image.open(image3_5).convert('RGB'))

    image4_1 = transform(Image.open(image4_1).convert('RGB'))
    image4_2 = transform(Image.open(image4_2).convert('RGB'))
    image4_3 = transform(Image.open(image4_3).convert('RGB'))
    image4_4 = transform(Image.open(image4_4).convert('RGB'))
    image4_5 = transform(Image.open(image4_5).convert('RGB'))


    return [image1_1, image1_2, image1_3, image1_4, image1_5, image2_1, image2_2, image2_3, image2_4, image2_5, 
            image3_1, image3_2, image3_3, image3_4, image3_5, image4_1, image4_2, image4_3, image4_4, image4_5]



basic_path = "D:\WZY\My_paper\AAAI2025\图\qualitative\qualitative_diverse"


img_ = image_list(path=basic_path)

save_image(img_, fp=os.path.join(basic_path, "qualitative_diverse.jpg"), nrow=5, padding=0,pad_value=1)
# save_image(img_2, fp=os.path.join(basic_path, "qualitative_2.jpg"), nrow=3, padding=0,pad_value=1)
# save_image(img_3, fp=os.path.join(basic_path, "qualitative_3.jpg"), nrow=3, padding=0,pad_value=1)
# save_image(img_4, fp=os.path.join(basic_path, "qualitative_4.jpg"), nrow=3, padding=0,pad_value=1)
