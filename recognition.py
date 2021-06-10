import datetime

import PIL.Image
import face_recognition
from PIL import Image
import os
from pixellib.instance import instance_segmentation
from datetime import time






def func2(i, j):

    IC2015 = face_recognition.load_image_file(i)
    IC2015_encord = face_recognition.face_encodings(IC2015)[0]



    IC2019 = face_recognition.load_image_file(j)
    IC2019_coord = face_recognition.face_locations(IC2019)

    if len(IC2019_coord)>0:

        n = 0
        for i in range(0, len(IC2019_coord), 1):
            IC2019_encord = face_recognition.face_encodings(IC2019)[i]
            compare = face_recognition.compare_faces([IC2015_encord], IC2019_encord)
            if compare == [True]:
                # return 'Да, это один и тот же человек'
                n = n + 1

        if n > 0:
            os.rename(j, '/Users/aleksejzajcev/Downloads/проверка изображений/Здесь есть Иришка ' + str(datetime.datetime.now()) + '.jpeg')

            return "На этом фото есть Ирина Зайцева"
        else:
            os.rename(j, '/Users/aleksejzajcev/Downloads/проверка изображений/Здесь нет Иришки ' + str(datetime.datetime.now()) + '.jpeg')
            return "Нет Ирины Зайцевой на фото"
    else:
        func3(i, j)
        # os.rename(j, '/Users/aleksejzajcev/Downloads/проверка изображений/Обрезать фото ' + str(datetime.datetime.now()) + '.jpeg')
        # return "Возникли проблемы с распознаванием лица, попробуйте приблизить(обрезать) изображение"

def func3(i, j):
    print(j)
    obrez = PIL.Image.Image.load(j)
    p1 = round(int(j.size[0])*0.1)
    p2 = round(int(j.size[0])*0.9)
    p3 = round(int(j.size[1]) * 0.1)
    p4 = round(int(j.size[1]) * 0.9)

    obrez.crop(p1, p2, p3, p4)
    obrez.save(j)
    # func2(i, j)







def main():
    P = os.listdir('/Users/aleksejzajcev/Downloads/проверка изображений')
    i = '/Users/aleksejzajcev/PycharmProjects/pythonProject/database/иришка 2015.jpeg'
    print(len(P))
    print(P[0])
    for n in range(0, len(P), 1):

        prov = '/Users/aleksejzajcev/Downloads/проверка изображений/' + str(P[n])
        if prov == '/Users/aleksejzajcev/Downloads/проверка изображений/.DS_Store':
            pass
        # seg_img = instance_segmentation()
        # seg_img.load_model("/Users/aleksejzajcev/PycharmProjects/pythonProject/database/Библиотека распознавания объектов.h5")
        #
        # seg_img.segmentImage(
        #     image_path=j,
        #     show_bboxes=True,
        #     # segment_target_classes=target,
        #     extract_segmented_objects=True,
        #     save_extracted_objects=True,
        #     output_image_name="/Users/aleksejzajcev/Downloads/иришка 2019(_2_).jpeg"
        # )


        func3(i, prov)





if __name__ == '__main__':
    main()
