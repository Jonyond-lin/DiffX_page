import os
from PIL import Image
from torchvision import transforms
from torchvision.transforms.functional import resize
from torchvision.utils import save_image

def image_list_1(path):
    image1 = os.path.join(path, '03_0079_000-5292c129_1_3DDFA.jpg')
    image2 = os.path.join(path, '03_0079_000-5292c129_1_VIS.jpg')
    image3 = os.path.join(path, '03_0079_000-5292c129_1_NIR.jpg')
    image4 = os.path.join(path, '03_0079_000-5292c129_1_SWIR.jpg')
    image5 = os.path.join(path, '03_0079_000-5292c129_1_THERMAL.jpg')
    image6 = os.path.join(path, '03_0201_000-2b607816_0_3DDFA.jpg')
    image7 = os.path.join(path, '03_0201_000-2b607816_0_VIS.jpg')
    image8 = os.path.join(path, '03_0201_000-2b607816_0_NIR.jpg')
    image9 = os.path.join(path, '03_0201_000-2b607816_0_SWIR.jpg')
    image10 = os.path.join(path, '03_0201_000-2b607816_0_THERMAL.jpg')
    # image11 = os.path.join(path, '1-11.jpg')
    # image12 = os.path.join(path, '1-12.jpg')

    transform = transforms.Compose([
        transforms.Resize((2048, 2048), interpolation=Image.BICUBIC),
        transforms.ToTensor()
    ])

    image1 = transform(Image.open(image1).convert('RGB'))
    image2 = transform(Image.open(image2).convert('RGB'))
    image3 = transform(Image.open(image3).convert('RGB'))
    image4 = transform(Image.open(image4).convert('RGB'))
    image5 = transform(Image.open(image5).convert('RGB'))
    image6 = transform(Image.open(image6).convert('RGB'))
    image7 = transform(Image.open(image7).convert('RGB'))
    image8 = transform(Image.open(image8).convert('RGB'))
    image9 = transform(Image.open(image9).convert('RGB'))
    image10 = transform(Image.open(image10).convert('RGB'))
    # image11 = transform(Image.open(image11).convert('RGB'))
    # image12 = transform(Image.open(image12).convert('RGB'))

    return [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10]


def image_list_2(path):
    image1 = os.path.join(path, '2-1.jpg')
    image2 = os.path.join(path, '2-2.jpg')
    image3 = os.path.join(path, '2-3.jpg')
    image4 = os.path.join(path, '2-4.jpg')
    image5 = os.path.join(path, '2-5.jpg')
    image6 = os.path.join(path, '2-6.jpg')
    image7 = os.path.join(path, '2-7.jpg')
    image8 = os.path.join(path, '2-8.jpg')
    image9 = os.path.join(path, '2-9.jpg')
    image10 = os.path.join(path, '2-10.jpg')
    image11 = os.path.join(path, '2-11.jpg')
    image12 = os.path.join(path, '2-12.jpg')

    transform = transforms.Compose([
        transforms.Resize((2048, 2048), interpolation=Image.BICUBIC),
        transforms.ToTensor()
    ])

    image1 = transform(Image.open(image1).convert('RGB'))
    image2 = transform(Image.open(image2).convert('RGB'))
    image3 = transform(Image.open(image3).convert('RGB'))
    image4 = transform(Image.open(image4).convert('RGB'))
    image5 = transform(Image.open(image5).convert('RGB'))
    image6 = transform(Image.open(image6).convert('RGB'))
    image7 = transform(Image.open(image7).convert('RGB'))
    image8 = transform(Image.open(image8).convert('RGB'))
    image9 = transform(Image.open(image9).convert('RGB'))
    image10 = transform(Image.open(image10).convert('RGB'))
    image11 = transform(Image.open(image11).convert('RGB'))
    image12 = transform(Image.open(image12).convert('RGB'))

    return [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12]


def image_list_3(path):
    image1 = os.path.join(path, '3-1.jpg')
    image2 = os.path.join(path, '3-2.jpg')
    image3 = os.path.join(path, '3-3.jpg')
    image4 = os.path.join(path, '3-4.jpg')
    image5 = os.path.join(path, '3-5.jpg')
    image6 = os.path.join(path, '3-6.jpg')
    image7 = os.path.join(path, '3-7.jpg')
    image8 = os.path.join(path, '3-8.jpg')
    image9 = os.path.join(path, '3-9.jpg')
    image10 = os.path.join(path, '3-10.jpg')
    image11 = os.path.join(path, '3-11.jpg')
    image12 = os.path.join(path, '3-12.jpg')

    transform = transforms.Compose([
        transforms.Resize((2048, 2048), interpolation=Image.BICUBIC),
        transforms.ToTensor()
    ])

    image1 = transform(Image.open(image1).convert('RGB'))
    image2 = transform(Image.open(image2).convert('RGB'))
    image3 = transform(Image.open(image3).convert('RGB'))
    image4 = transform(Image.open(image4).convert('RGB'))
    image5 = transform(Image.open(image5).convert('RGB'))
    image6 = transform(Image.open(image6).convert('RGB'))
    image7 = transform(Image.open(image7).convert('RGB'))
    image8 = transform(Image.open(image8).convert('RGB'))
    image9 = transform(Image.open(image9).convert('RGB'))
    image10 = transform(Image.open(image10).convert('RGB'))
    image11 = transform(Image.open(image11).convert('RGB'))
    image12 = transform(Image.open(image12).convert('RGB'))

    return [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12]


def image_list_4(path):
    image1 = os.path.join(path, '4-1.jpg')
    image2 = os.path.join(path, '4-2.jpg')
    image3 = os.path.join(path, '4-3.jpg')
    image4 = os.path.join(path, '4-4.jpg')
    image5 = os.path.join(path, '4-5.jpg')
    image6 = os.path.join(path, '4-6.jpg')
    image7 = os.path.join(path, '4-7.jpg')
    image8 = os.path.join(path, '4-8.jpg')
    image9 = os.path.join(path, '4-9.jpg')
    image10 = os.path.join(path, '4-10.jpg')
    image11 = os.path.join(path, '4-11.jpg')
    image12 = os.path.join(path, '4-12.jpg')

    transform = transforms.Compose([
        transforms.Resize((2048, 2048), interpolation=Image.BICUBIC),
        transforms.ToTensor()
    ])

    image1 = transform(Image.open(image1).convert('RGB'))
    image2 = transform(Image.open(image2).convert('RGB'))
    image3 = transform(Image.open(image3).convert('RGB'))
    image4 = transform(Image.open(image4).convert('RGB'))
    image5 = transform(Image.open(image5).convert('RGB'))
    image6 = transform(Image.open(image6).convert('RGB'))
    image7 = transform(Image.open(image7).convert('RGB'))
    image8 = transform(Image.open(image8).convert('RGB'))
    image9 = transform(Image.open(image9).convert('RGB'))
    image10 = transform(Image.open(image10).convert('RGB'))
    image11 = transform(Image.open(image11).convert('RGB'))
    image12 = transform(Image.open(image12).convert('RGB'))

    return [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12]

basic_path = "D:\WZY\My_paper\AAAI2025\图\qualitative\qualitative_forth"


img_1 = image_list_1(path=basic_path)
# img_2 = image_list_2(path=basic_path)
# img_3 = image_list_3(path=basic_path)
# img_4 = image_list_4(path=basic_path)

save_image(img_1, fp=os.path.join(basic_path, "qualitative_forth.jpg"), nrow=5, padding=0,pad_value=1)
# save_image(img_2, fp=os.path.join(basic_path, "qualitative_2.jpg"), nrow=3, padding=0,pad_value=1)
# save_image(img_3, fp=os.path.join(basic_path, "qualitative_3.jpg"), nrow=3, padding=0,pad_value=1)
# save_image(img_4, fp=os.path.join(basic_path, "qualitative_4.jpg"), nrow=3, padding=0,pad_value=1)
