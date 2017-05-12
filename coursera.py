import xml.etree.ElementTree as etree
import requests
import json
import re

def get_courses_list():
    tree = etree.parse('./coursera.xml')
    root = tree.getroot()
    my_dict = []
    for i, k in enumerate(root):
        for j in range(0, len(k)):
            result = re.sub('\n', '', k[j].text)
            my_dict.append(result) # красивый список всех ссылок
    list_20 = [my_dict[i] for i in range(15,35)]
    return list_20


def get_course_info(course_slug):
    pass


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    get_courses_list()
