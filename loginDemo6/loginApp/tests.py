import pymysql
from django.test import TestCase

# Create your tests here.
'''
connect（）建立数据库连接
execute（）执行sql语句
close（）  关闭数据库连接
'''
def test_db():
    connection = pymysql.connect(
        host = '',
        user = '',
        password = '',
        db = '',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            sql = ''
            cursor.execute(sql)
            connection.commit()

        with connection.cursor() as cursor:
            sql = ''
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()

if __name__ == '__main__':
    test_db()