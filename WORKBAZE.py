import pymorphy2
import pymorphy2.analyzer

from pymorphy2 import opencorpora_dict
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
import glob
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import openpyxl
from openpyxl import Workbook
import datetime
import os
from selenium.webdriver.firefox.options import Options
from docxtpl import DocxTemplate
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from docx2pdf import convert

from openpyxl.styles import Color, PatternFill, Font, Border
import jinja2
from jinja2 import Template
from collections import OrderedDict

def wordskl(word, padezh):
    d = OrderedDict()
    split = word.split()
    lenspl = len(split)


    # print(split[1])
    for i in range(0, lenspl):
        morph = pymorphy2.MorphAnalyzer()
        parse_name = morph.parse(split[i])[0]

        if parse_name.tag.case == 'nomn':
            n = parse_name.inflect({padezh})[0]
        else:
            n = split[i]
        d[n]=n
    N = list(d.values())


    data = N[0]
    for f in range(1, lenspl):
        data = data + " " + N[f]
    return data
def fioskl(fio, padezh):

    split = str.split(fio)

    # name
    lingue_name = split[1]
    morph = pymorphy2.MorphAnalyzer()
    parse_name = morph.parse(lingue_name)[0]
    gender_name = parse_name.tag.gender
    I = str.title((parse_name.inflect({padezh})[0]))



    #family
    try:
        lingue_family = split[0]
        morph_family = pymorphy2.MorphAnalyzer()
        parse_family = morph_family.parse(lingue_family)
        print(parse_family)
        gender_family = parse_family.tag.gender
        F = str.title((parse_family.inflect({padezh}, gender_name)[0]))
        print(f'3 {parse_family}')
        print(gender_family)
    except:
        try:

            lingue_family = split[0]
            morph_family = pymorphy2.MorphAnalyzer()
            parse_family = morph_family.parse(lingue_family)[1]
            gender_family = parse_family.tag.gender
            F = str.title((parse_family.inflect({padezh})[0]))
            print(f'3 {parse_family}')
            print('exept')
        except:

            lingue_family = split[0]
            morph_family = pymorphy2.MorphAnalyzer()
            parse_family = morph_family.parse(lingue_family)[0]
            gender_family = parse_family.tag.gender
            F = str.title((parse_family.inflect({padezh})[0]))
            print(f'3 {parse_family}')
            print('exept2')


        # n=0
        # while True:
        #     lingue_family = split[0]
        #     morph_family = pymorphy2.MorphAnalyzer()
        #     parse_family = morph_family.parse(lingue_family)[n]
        #     gender_family = parse_family.tag.gender
        #     F = str.title((parse_family.inflect({padezh})[0]))
        #     n = n + 1


    #         if gender_name == gender_family:
    #             break
    # if F == '*чков':
    #     F=F+'а'




    if len(split) > 3:
        O = str.title(split[2])+' '+split[3]
    else:
        lingue = split[2]
        morph = pymorphy2.MorphAnalyzer()
        O = str.title((morph.parse(lingue)[0].inflect({padezh})[0]))

    return (f'{F} {I} {O}')

def CreateDoc(fio, dolzhn, organization, sut, statia, srok_protokola):
    # начало автоматического создания документа

    # сейчас
    now = datetime.datetime.now()
    monthfull = now.strftime('%B')
    month00 = now.strftime('%m')
    day = now.strftime('%d')
    year = now.strftime('%Y')

    fio_gent = fioskl(fio, 'gent')
    fio_ablt = fioskl(fio, 'ablt')

    dolzhn_ablt = wordskl(dolzhn, 'ablt')
    dolzhn_gent = wordskl(dolzhn, 'gent')

    # в срок через 14 дней
    srok = now + datetime.timedelta(days=srok_protokola)
    srok_monthfull = srok.strftime('%B')
    srok_month00 = srok.strftime('%m')
    srok_day = srok.strftime('%d')
    srok_year = srok.strftime('%Y')

    jinja_env = jinja2.Environment()

    doc = DocxTemplate("C:\\Users\\user\\Documents\\документы\\ВЫЗОВ ФОРМА.docx")
    doc.render({'день_составления_вызова': day, 'месяц_составления_вызова': monthfull, 'год_составления_вызова': year,
      'Должность_специалиста': "Специалист-эксперт", 'ФИО_специалиста_полностью': "Зайцев Алексей Дмитриевич",
      'Должность_правонарушителя_ТП': dolzhn_ablt,
      'организация_правонарушитель': organization, 'Суть_правонарушения_что_было_сделано': sut,
      'ФИО_правонарушителя_ТП': fio_ablt, 'Часть_статья': statia, 'Должность_правонарушителя_РП': dolzhn_gent, 'ФИО_правонарушителя_РП': fio_gent, 'День_составления_протокола': srok_day,
      'месяц_составления_протокола': srok_monthfull, 'год_составления_протокола': srok_year,
      'ИОФ_специалиста': "А.Д. Зайцев"}, jinja_env)

    doc.save("C:\\Users\\user\\Downloads\\Вызов на протокол " + fio + ".doc")


def main():
    fio = 'семенова зоя вадимовна'
    dolzhn = 'специалист-эксперт управления федеральной службы в сфере защиты прав потребителей'
    organization = 'ГБУЗ НО «Городская больница №33»'
    sut = 'в нарушение требований п. 5.6, 5.8 СП 3.1.5.2826-10 "Профилактика ВИЧ-инфекции" на момент проверки 21.04.2021 г. в медицинских картах стационарного больного  № 248/э, № 326/э, № 177/э, № 7865/э, № 587/э, № 507/э, № 7821/э, № 346/э, № 607/э пролеченных пациентов урологического отделения в январе 2021 года,    при  наличии результатов тестирования на ВИЧ-инфекцию не зафиксированы сведения о проведении обязательного до- и послетестового консультирования, отсутствует форма информируемого согласия' # Суть_правонарушения_что_было_сделано
    statia = 'ч.1 ст 6.3'
    srok_protokola = 10 # указывается через сколько дней назначен протокол
    # CreateDoc(fio, dolzhn, organization, sut, statia, srok_protokola)
    # print(wordskl(dolzhn, 'ablt'))
    print(fioskl(fio, 'gent'))
    # padezhi = ['nomn', 'gent', 'datv', 'accs', 'ablt', 'loct', 'voct', 'gen2', 'acc2', 'loc2']

if __name__ == '__main__':
    main()