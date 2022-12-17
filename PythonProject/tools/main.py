import pandas
from public.Encryption import make_md5
from public.Data import read_excel_dict, read_excel, make_insert_sql
import public.tools
import os
import time
import datetime
import openpyxl
import redis


default_data_path = os.path.dirname(__file__) + '\\data'
default_data_file = default_data_path + '\\data.xlsx'



def show_main_menu():
    os.system('cls')
    print('1. ')
    print('0. 退出')


def handle_main_menu(all_tables):
    table = []
    while True:
        show_main_menu()
        choose_menu = int(input('输入选项：'))
        match choose_menu:
            case 0:
                exit(0)
            case _:
                print('无效数据！请重新输入')
                time.sleep(1)
    return table

def show_list(list_data):
    for num, each in enumerate(list_data):
        print('%i:%s' % (num+1, each))


if __name__ == '__main__':
    # print(time.strftime("%Y%m%d"))
    print('当前时间:', int(time.time()))
    print('当前时间:', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    # 新增角色
    sql_1 = 'INSERT INTO `dlcenter_log`.`statis_role_183` (`game_id`, `company_id`, `channel_id`, `uid`, `sid`, `servername`, `role_id`, `role_name`, `level`, `first_charge_level`, `first_charge_money`, `first_charge_time`, `first_charge_flag`, `second_charge_level`, `second_charge_money`, `second_charge_time`, `ctime`, `user_ctime`, `ip`, `is_first_role`, `valid_role`, `subtract`) ' \
            'VALUES ('+game_id+', '+company_id+', '+channel_id+', '+uid+', '+sid+', '+servername+', '+role_id+', '+role_name+', '+level+', '+first_charge_level+', '+first_charge_money+', '+first_charge_time+', '+first_charge_flag+', '+second_charge_level+', '+second_charge_money+', '+second_charge_time+', '+ctime+', '+user_ctime+', '+ip+', '+is_first_role+', '+valid_role+', '+subtract+');'


