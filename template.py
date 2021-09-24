import datetime
import pickle
import PIL.Image
import face_recognition
from PIL import Image
import os
from pixellib.instance import instance_segmentation
from datetime import time

def func1(dir):
    P = os.listdir(dir)
    print(f'элементов в папке: {len(P)}')
    prov = {}
    for i in range(0, len(P)):
        if P[i] == '.DS_Store':
            continue
        else:
            prov[len(prov)] = P[i]
    print(f'Занесено в журнал {len(prov)}')
    print(prov)
    file_encord_dict = {}
    E = os.listdir('/Users/aleksejzajcev/Downloads/реестр кодировок лица')
    E2 = {}
    for t in range(0, len(E)):
        if E[t] == '.DS_Store':
            continue
        else:
            E2[len(E2)] = E[t]
    for iter in range(0, len(E2)):
        dir_true = f'/Users/aleksejzajcev/Downloads/реестр кодировок лица/{E2[iter]}'
        file_true = face_recognition.load_image_file(dir_true)
        file_encord_true = face_recognition.face_encodings(file_true)[0]
        file_encord_dict[len(file_encord_dict)+1] = file_encord_true

    for foto in range(0, len(prov), 1):
        file = face_recognition.load_image_file(f'{dir}/{prov[foto]}')
        hmp = face_recognition.face_locations(file)
        people = len(hmp)
        print(people)
        if people == 0:
            print(f'на фото {prov[foto]} не удалось обнаружить лица')
            os.replace(f'{dir}/{prov[foto]}', f'/Users/aleksejzajcev/Downloads/не удалось обнаружить лица/{prov[foto]}')
        if people != 0:
            n = 0
            for true in range(1, len(file_encord_dict)+1):
                for list in range(0, people, 1):

                    file_encord = face_recognition.face_encodings(file)[list]
                    check = face_recognition.compare_faces([file_encord_dict[true]], file_encord)
                    print(f'на фото {prov[foto]} {check}')
                    if check == [True]:
                        n =+ 1
                        #
                        # break
                    # if check == [False] and list == people-1:
                print(f'найдено совпадений на фото по лицам - {n}')
            if n != 0:
                os.replace(f'{dir}/{prov[foto]}', f'/Users/aleksejzajcev/Downloads/есть искомое лицо/{prov[foto]}')
            if n == 0:
                os.replace(f'{dir}/{prov[foto]}', f'/Users/aleksejzajcev/Downloads/не обнаружено искомого лица/{prov[foto]}')


def func2(dir):
    P = os.listdir(dir)
    print(f'элементов в папке: {len(P)}')
    prov = {}
    for i in range(0, len(P)):
        if P[i] == '.DS_Store':
            continue
        else:
            prov[len(prov)] = P[i]
    print(f'Занесено в журнал {len(prov)}')
    print(prov)
    dir_true = '/Users/aleksejzajcev/Downloads/1.JPG'
    file_true = face_recognition.load_image_file(dir_true)
    file_encord_true = face_recognition.face_encodings(file_true)[0]

    for foto in range(0, len(prov), 1):
        file = face_recognition.load_image_file(f'{dir}/{prov[foto]}')
        hmp = face_recognition.face_locations(file)
        people = len(hmp)
        print(people)
        if people == 0:
            print(f'на фото {prov[foto]} не удалось обнаружить лица')
            os.replace(f'{dir}/{prov[foto]}', f'/Users/aleksejzajcev/Downloads/не удалось обнаружить лица/{prov[foto]}')
        else:
            for list in range(0, people, 1):
                n=0
                file_encord = face_recognition.face_encodings(file)[list]
                check = face_recognition.compare_faces([file_encord_true], file_encord)
                print(f'на фото {prov[foto]} {check}')
                if check == [True]:
                    os.replace(f'{dir}/{prov[foto]}', f'/Users/aleksejzajcev/Downloads/есть искомое лицо/{prov[foto]}')
                    break
                if check == [False] and list == people-1:
                    os.replace(f'{dir}/{prov[foto]}', f'/Users/aleksejzajcev/Downloads/не обнаружено искомого лица/{prov[foto]}')


# надо доработать строчку 42-43, ибо она не проверяет фотки, где нет искомого лица, либо не проверяет фотки где одно из лиц не искомое.



def func3():
    dir_true = '/Users/aleksejzajcev/Downloads/Тэ Хён.jpeg'
    dir = '/Users/aleksejzajcev/Downloads/Чонгук.jpeg'
    file_true = face_recognition.load_image_file(dir_true)
    file_encord_true = face_recognition.face_encodings(file_true)[0]
    file = face_recognition.load_image_file(dir)
    file_encord = face_recognition.face_encodings(file)[0]
    print(file_encord_true)
    print(file_encord)
    compare = face_recognition.compare_faces([file_encord_true], file_encord)

    print(compare)




def main():
    one = os.path.exists('/Users/aleksejzajcev/Downloads/есть искомое лицо')
    if one is False:
        os.mkdir('/Users/aleksejzajcev/Downloads/есть искомое лицо')
    two = os.path.exists('/Users/aleksejzajcev/Downloads/не обнаружено искомого лица')
    if two is False:
        os.mkdir('/Users/aleksejzajcev/Downloads/не обнаружено искомого лица')

    tree = os.path.exists('/Users/aleksejzajcev/Downloads/не удалось обнаружить лица')
    if tree is False:
        os.mkdir('/Users/aleksejzajcev/Downloads/не удалось обнаружить лица')


    dir = '/Users/aleksejzajcev/Downloads/проверка'
    func1(dir)
    # func3()

if __name__ == '__main__':
    main()