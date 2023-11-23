import sys
import os
# 随机
import random
# 处理字符串
import string
# 获取当前时间
from datetime import datetime
# 随机字符串
import secrets

def output_file_path(folderName,fileName):
    """ 输出文件路径

    :param folderName: 文件夹名
    :param fileName: 文件名
    :return: 文件路径
    """

    # 输出文件夹
    output_path =  sys.path[0] + '/GarbageCode/' + folderName + '/'
    # 如果文件夹不存在，则创建
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    full_path = output_path + fileName + '.swift'
    print(full_path)
    return full_path


def file_header_note_code(fileName, projectName):
    """ Swift文件顶部的注释说明代码
 
    :param fileName: 文件名
    :param projectName: 项目名
    :return: 顶部注释说明代码字符串
    """

    # 获取对应格式的当前时间字符串
    now_date = datetime.now().strftime("%Y/%m/%d")
    # 顶部注释说明代码
    header_note_code = '//\n//  '+fileName+'.swift\n//  '+ projectName +'\n\n//  Created by 蔡青旺 on '+ now_date + '.\n//  \n//\n\n'
    return header_note_code


def reference_header_file(array):
    """ Swift文件引用的头文件
 
    :param array: 头文件数组
    :return: 头部引用字符串
    """

    header_file_string = ''
    for header_file in array:
        header_file_string += ('import ' + header_file + '\n')
    return header_file_string


def generate_random_string(length):
    """ 生成随机字符串
 
    :param length: 字符串长度
    :return: 随机字符串
    """
    generate_random_letters = string.ascii_letters
    if length <= 0:
        raise ValueError("随机字符串错误")
    return ''.join(secrets.choice(generate_random_letters) for i in range(length))


def create_class_name(subffix):
    """ 随机生成类名字符串
 
    :param subffix: 类名后缀，如ViewController、Model等
    :return: 随机类名列表
    """
    
    first = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    second = "abcdefghijklmnopqrstuvwxyz"
    array = []

    # 设置生成多少个类名
    class_count = 50

    
    for i in range(1, class_count):
        # 前三个字母大写，当做前缀用
        class_name = random.choice(first)
        for i in range(1, 2):
            class_name += random.choice(first)

        # 中间字符串的长度，中间使用小写
        count = random.randint(5, 20)
        for i in range(1, count):
            class_name += random.choice(second)

        # 类名后缀
        class_name += subffix
        array.append(class_name)

    return array

def create_property_list(count, isUIKit):
    """ 创建属性列表
 
    :param count: 属性个数
    :param isUIKit: 是否引用UIKit框架
    :return: 返回属性列表字符串
    """

    propryNameArray = []
    for i in range(1, count):
        # 属性名长度
        length = random.randint(10, 25)
        propryNameArray.append(generate_random_string(length))
    # 去重
    propryNameArray = list(set(propryNameArray))

    #属性类型
    propryTypeArray = []
    if isUIKit:
        propryTypeArray = ['UILabel', 'UITableView', 'UIScrollView', 'UIImageView', 'UICollectionView','UIView', 'UIButton', 'UITextField',
                           'String', 'Int', 'CGFloat', 'Double', 'Bool']
    else:
        propryTypeArray = ['String', 'Int', 'CGFloat', 'Double', 'Bool']

    # 前半部分为私有属性，后半部分为公共属性
    propry_list_string = ''
    for index, item in enumerate(propryNameArray):
        if (index + 1) < (len(propryNameArray) / 2): 
            propry_list_string += '    private var ' + item + ':' + random.choice(propryTypeArray) + '!\n'
        else:
            propry_list_string += '    public var ' + item + ':' + random.choice(propryTypeArray) + '!\n'

    return propry_list_string



def create_model_swift(projectName,fileName,classType='struct'):
    """ 创建Model文件
 
    :param projectName: 项目名
    :param fileName: 文件名
    :param classType: 文件类型，class、struct
    """

    full_path = output_file_path('Model',fileName)

    # 打开文件，并写入
    file = open(full_path, 'w')
    # 获取对应格式的当前时间字符串
    now_date = datetime.now().strftime("%Y/%m/%d")
    # 写入文件头部注释
    file.write(file_header_note_code(fileName, projectName))
    # 写入头文件引用
    file.write(reference_header_file(['Foundation']))
    # 创建类
    file.write('\n' + classType + ' ' + fileName + ' {\n')

    # 创建属性
    # 随机生成属性的个数
    propry_count = random.randint(10, 30)
    propry_list_string = create_property_list(propry_count, False)
    file.write(propry_list_string)
    file.write('\n\n')
    file.write('}')
    
    file.close()


def create_vc_swift(projectName,fileName,superClass='UIViewController'):
    """ 创建VC文件
 
    :param projectName: 项目名
    :param fileName: 文件名
    :param superClass: 父类
    """

    full_path = output_file_path('ViewController',fileName)

    # 打开文件，并写入
    file = open(full_path, 'w')
    # 获取对应格式的当前时间字符串
    now_date = datetime.now().strftime("%Y/%m/%d")
    # 写入文件头部注释
    file.write(file_header_note_code(fileName, projectName))
    # 写入头文件引用
    file.write(reference_header_file(['Foundation', 'UIKit']))
    # 创建类
    file.write('\nclass ' + fileName + ': ' + superClass + ' {\n')
    
    # 创建属性
    # 随机生成属性的个数
    propry_count = random.randint(5, 20)
    propry_list_string = create_property_list(propry_count, True)
    file.write(propry_list_string)
    file.write('\n\n')
    
    # 写入 viewDidLoad 方法
    title_length = random.randint(8, 20)
    title = generate_random_string(title_length)
    file.write('    override func viewDidLoad() {\n        super.viewDidLoad()\n        title = "'+ title +'"\n    }\n\n')
   
    # 创建方法
    method_count = random.randint(5, 20)
    method_name_array = []
    for i in range(1, method_count):
        # 属性名长度
        method_name_length = random.randint(20, 40)
        method_name_array.append(generate_random_string(method_name_length))
    # 去重
    method_name_array = list(set(method_name_array))

    for method_name in method_name_array:
        array_name_length = random.randint(3, 10)
        array_name = generate_random_string(array_name_length) + 'Array'
        file.write('    func ' + method_name + 'AtVC() {\n\n       var ' + array_name + ': [String] = []\n')

        array_count = random.randint(5, 15)

        for i in range(1, array_count):
            array_string_length = random.randint(10, 50)
            array_string = generate_random_string(array_string_length)

            file.write('       ' + array_name + '.append("'+ array_string +'")\n')

        file.write('\n    }\n\n')

    file.write('}')

    file.close()


# 创建VC
class_name_vc_array = create_class_name('ViewController')
class_name_vc_array = list(set(class_name_vc_array))
for class_name in class_name_vc_array:
    create_vc_swift('ProjectName', class_name)

# 创建Model
class_name_model_array = create_class_name('Model')
class_name_model_array = list(set(class_name_model_array))
for class_name in class_name_model_array:
    create_model_swift('ProjectName', class_name)

