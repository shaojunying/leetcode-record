#!/usr/bin/env python
# Created by Bruce yuan on 18-1-22.
from urllib.parse import urljoin

import requests
import os
import json
import time


class Config:
    """
    some config, such as your github page
    这里需要配置你自己的项目地址
    １．　本地仓库的的路径
    ２．　github中的仓库leetcode解法的路径
    """
    # 本地存放项目的路径
    local_path = r'C:\Users\shao\Documents\codingProject\leetcode-record'
    github_leetcode_url = 'https://github.com/shaojunying/leetcode-record/tree/master/src/leetcode_oj/'
    leetcode_url = 'https://leetcode.com/problems/'


class Question:
    """
    this class used to store the inform of every question
    """

    def __init__(self, id_,
                 name, url,
                 lock, difficulty):
        self.id_ = id_
        self.title = name
        # the problem description url　问题描述页
        self.url = url
        self.lock = lock  # boolean，锁住了表示需要购买
        self.difficulty = difficulty
        # the solution url
        self.python = ''
        self.java = ''
        self.javascript = ''
        self.c_plus_plus = ''

    def __repr__(self):
        """
        没啥用，我为了调试方便写的
        :return:
        """
        return str(self.id_) + ' ' + str(self.title) + ' ' + str(self.url)


class TableInform:
    def __init__(self):
        # 存储json解析出的所有问题
        self.questions = []
        # 存储所有问题的下标
        self.table = []
        # 存储每个问题id对应的问题详细信息
        self.table_item = {}
        # 记录付费问题总数
        self.locked = 0

    # 获取所有问题和问题的详细信息,存储数组中
    def get_leetcode_problems(self):
        """
        used to get leetcode inform
        :return:
        """
        # we should look the response data carefully to find law
        # return byte. content type is byte
        headers = {
            'Connection': 'close'}
        content = requests.get('https://leetcode.com/api/problems/algorithms/', headers=headers).content
        print(content)

        # get all problems
        self.questions = json.loads(content)['stat_status_pairs']
        # print(self.questions)
        difficultys = ['Easy', 'Medium', 'Hard']
        for i in range(len(self.questions) - 1, -1, -1):
            # 获取第i个问题
            question = self.questions[i]
            # 分别获取问题的名字,url,id
            name = question['stat']['question__title']
            url = question['stat']['question__title_slug']
            id_ = str(question['stat']['frontend_question_id'])
            # 对id进行格式化
            if int(id_) < 10:
                id_ = '00' + id_
            elif int(id_) < 100:
                id_ = '0' + id_
            # 如果问题需要付费,就将lock赋为true
            # 同时付费问题总数加1
            lock = question['paid_only']
            if lock:
                self.locked += 1
            # 获取问题的难度
            difficulty = difficultys[question['difficulty']['level'] - 1]
            url = Config.leetcode_url + url + '/description/'
            q = Question(id_, name, url, lock, difficulty)
            # 将问题的id存入表格table中
            self.table.append(q.id_)
            # 将id对应问题的详细信息存入table_item中中
            self.table_item[q.id_] = q
        return self.table, self.table_item

    # 创建问题文件夹
    def __create_folder(self, oj_name):
        oj_algorithms = Config.local_path + '/' + oj_name
        if os.path.exists(oj_algorithms):
            # 已经存在这个文件夹
            print(oj_name, ' algorithms is already exits')
        else:
            # 创建文件夹
            print('creating {} algorithms....'.format(oj_name))
            os.mkdir(oj_algorithms)
        for item in self.table_item.values():
            question_folder_name = oj_algorithms + '/' + item.id_ + '. ' + item.title
            if os.name != 'posix':
                # 如果不是linux，那么就要吧后面的问号去掉
                question_folder_name = question_folder_name[:-1]
            if not os.path.exists(question_folder_name):
                print(question_folder_name + 'is not exits, create it now....')
                os.mkdir(question_folder_name)

    def update_table(self, oj):
        # the complete inform should be update
        complete_info = CompleteInform()
        # 获取leetcode的问题
        self.get_leetcode_problems()
        # 总问题数
        complete_info.total = len(self.table)
        # 付费问题数
        complete_info.lock = self.locked
        # 创建文件夹
        self.__create_folder(oj)
        oj_algorithms = Config.local_path + '/' + oj
        #
        for _, folders, _ in os.walk(oj_algorithms):
            # _代表当前文件所在目录
            # folders 表示所有的子文件夹
            # 路径下的文件
            for folder in folders:
                for _, _, files in os.walk(os.path.join(oj_algorithms, folder)):
                    if len(files) != 0:
                        # 完成的题目数量+1
                        complete_info.complete_num += 1
                    for item in files:
                        # print(os.path.abspath(item))
                        # print(folder)
                        if item.endswith('.py'):
                            complete_info.solved['python'] += 1

                            # 将文件路径中空格给替换
                            folder_url = folder.replace(' ', "%20")
                            # 拼贴出正确的路径
                            folder_url = urljoin(folder_url, item)
                            # 加上github项目的目录,实现文件路径的生成
                            folder_url = urljoin(Config.github_leetcode_url, folder_url)
                            # folder[:3]为问题序号,问题id为1的时候,截出来的是001
                            # table_item[001]将会赋值为[编程语言]{文件路径},实现直接点击就可跳转
                            self.table_item[folder[:3]].python = '[Python]({})'.format(folder_url)
                        elif item.endswith('.java'):
                            complete_info.solved['java'] += 1
                            folder_url = folder.replace(' ', "%20")
                            folder_url = urljoin(folder_url, item)
                            folder_url = urljoin(Config.github_leetcode_url, folder_url)
                            self.table_item[folder[:3]].java = '[Java]({})'.format(folder_url)
                        elif item.endswith('.cpp'):
                            complete_info.solved['c++'] += 1
                            folder_url = folder.replace(' ', "%20")
                            folder_url = urljoin(folder_url, item)
                            folder_url = urljoin(Config.github_leetcode_url, folder_url)
                            self.table_item[folder[:3]].c_plus_plus = '[C++]({})'.format(folder_url)
                        elif item.endswith('.js'):
                            complete_info.solved['javascript'] += 1
                            folder_url = folder.replace(' ', "%20")
                            folder_url = urljoin(folder_url, item)
                            folder_url = urljoin(Config.github_leetcode_url, folder_url)
                            self.table_item[folder[:3]].javascript = '[JavaScript]({})'.format(folder_url)
        readme = Readme(complete_info.total,
                        complete_info.complete_num,
                        complete_info.lock,
                        complete_info.solved)
        readme.create_leetcode_readme([self.table, self.table_item])
        print('-------the complete inform-------')
        print(complete_info.solved)
        print('the total complete num is: {}'.format(
            complete_info.complete_num))


class CompleteInform:
    """
    静态表
    """

    def __init__(self):
        # 记录各种类型问题解决个数
        self.solved = {
            'python': 0,
            'c++': 0,
            'java': 0,
            'javascript': 0
        }
        # 解决数量
        self.complete_num = 0
        # 付费问题数量
        self.lock = 0
        # 总问题数量
        self.total = 0

    def __repr__(self):
        return str(self.solved)


class Readme:
    """
    generate folder and markdown file
    update README.md when you finish one problem by some language
    """

    def __init__(self, total, solved, locked, others=None):
        """
        :param total: total problems nums
        :param solved: solved problem nums
        :param others: 暂时还没用，我想做扩展
        """
        # 所有问题数
        self.total = total
        # 解决问题数
        self.solved = solved
        self.others = others
        # 付费
        self.locked = locked
        # 当前时间
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 消息
        self.msg = '# Keep thinking, keep alive\n' \
                   'Until {}, I have solved **{}** / **{}** problems ' \
                   'while **{}** are still locked.' \
                   '\n\nCompletion statistic: ' \
                   '\n1. JavaScript: {javascript} ' \
                   '\n2. Python: {python}' \
                   '\n3. C++: {c++}' \
                   '\n4. Java: {java}' \
                   '\n\nNote: :lock: means you need to buy a book from LeetCode\n'.format(
            self.time, self.solved, self.total, self.locked, **self.others)

    def create_leetcode_readme(self, table_instance):
        """
        create REAdME.md
        :return:
        """
        # 记录readme文件路径
        file_path = Config.local_path + '/README.md'
        # write some basic inform about leetcode
        with open(file_path, 'w') as f:
            f.write(self.msg)
            f.write('\n----------------\n')

        with open(file_path, 'a') as f:
            f.write('## LeetCode Solution Table\n')
            f.write('| ID | Title | Difficulty | JavaScript | Python | C++ | Java |\n')
            f.write('|:---:' * 7 + '|\n')
            table, table_item = table_instance

            for index in table:
                item = table_item[index]
                # 问题是付费的
                if item.lock:
                    _lock = ':lock:'
                else:
                    _lock = ''
                data = {
                    'id': item.id_,
                    'title': '[{}]({}) {}'.format(item.title, item.url, _lock),
                    'difficulty': item.difficulty,
                    'js': item.javascript if item.javascript else 'To Do',
                    'python': item.python if item.python else 'To Do',
                    'c++': item.c_plus_plus if item.c_plus_plus else 'To Do',
                    'java': item.java if item.java else 'To Do'
                }
                line = '|{id}|{title}|{difficulty}|{js}|{python}|{c++}|{java}|\n'.format(**data)
                f.write(line)
            # 创建readme成功
            print('README.md was created.....')


def main():
    table = TableInform()
    table.update_table('src\leetcode_oj')


if __name__ == '__main__':
    main()
