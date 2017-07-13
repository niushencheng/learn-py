"""
操作mysql的使用
"""
import pymysql

if __name__ == '__main__':
    conn = pymysql.connect(user = 'ctp_paas', password = 'd0yTJasc9tpXp1qxs', database = 'ctp_paas', charset = 'utf-8')