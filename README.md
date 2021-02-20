# DjangoDemo
Django  练习

loginDemo文件夹：参考博客：https://www.cnblogs.com/feifei-cyj/p/14402366.html

loginDemo2文件夹：参考博客：https://www.cnblogs.com/feifei-cyj/p/14396376.html

loginDemo3文件夹：参考博客：https://www.cnblogs.com/feifei-cyj/p/14404110.html

loginDemo4文件夹：参考博客：https://www.cnblogs.com/feifei-cyj/p/14404399.html

loginDemo5文件夹：参考博客：https://www.cnblogs.com/feifei-cyj/p/14412418.html

loginDemo6文件夹：参考博客：https://www.cnblogs.com/feifei-cyj/p/14417701.html

loginDemo7文件夹：参考博客：https://www.cnblogs.com/feifei-cyj/p/14421858.html

说明：

1、下载代码后，用pycharm打开到loginDemoX目录；

2、本地安装虚拟环境：pip3 install virtualenv -i https://pypi.python.org/simple/

3、virtualenv envior  #  envior为环境名称，记住在哪个文件夹下建立的虚拟环境

4、source envior/bin/activate # 激活环境

5、pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

6、迁移数据库： python3 manage.py migrate

7、创建超级用户：python3 manage.py createsuperuser

8、启动项目：python3 manage.py runserver

9、访问http://127.0.0.1:8000/login/   用户名密码为上面创建的超级用户信息

10、访问http://127.0.0.1:8000/admin/  用户名密码为上面创建的超级用户信息，进入新增event、guest记录
