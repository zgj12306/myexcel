python版本3.7.4

扩展库在require.txt文件里面

通过 pip install -r require.txt 命令安装扩展

需要配置nginx

server{

    listen 80;
    server_name hello.zgj.com;
    charset utf-8;
    client_max_body_size 75M;  #上传文件大小限制

    # 网站静态文件所在目录
    location /static{
        alias /usr/src/app/HelloWorld/static;
    }

    # 上传文件所在目录
    location /media{
        alias /usr/src/app/HelloWorld/media;
    }

    # 动态文件交给uwsgi处理
    location / {
        uwsgi_pass python:8001;
        include /etc/nginx/uwsgi_params;
    }
}

运行uwsgi --ini HelloWorld.ini

访问http://hello.zgj.com/index