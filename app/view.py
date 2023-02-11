from flask import Flask, render_template, request, send_file
import os, datetime
import subprocess
import shutil
from requests_html import HTMLSession
import bs4
import pandas as pd


app = Flask(__name__)  # 模块名


@app.route('/usage')
def usage():
    return render_template("usage.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/baidu_verify_codeva-Qi5Gr9bBib.html')
def baidu_verify():
    return render_template("baidu_verify_codeva-Qi5Gr9bBib.html")

@app.route("/")  # 网页默认第一个页面为‘/’
def index():
    return render_template("index.html")  # 打开第一个网页


@app.route("/submit", methods=['GET', "POST"])  # 第二级网页
def log():
    basicdata = str(request.form.get("basicdata"))
    remote_ip = request.remote_addr
    subprocess.run(["python3", "app/getuid.py", basicdata, remote_ip])
    df = pd.read_csv('./cache/IP_log.csv', engine='python', usecols=[0, 1])
    frame = pd.DataFrame(df)
    df1 = frame.drop_duplicates(subset='IP', keep='last', inplace=False)
    result = df[df["IP"] == f'{str(remote_ip)}']
    print(result.iloc[-1, 1],"检测到，准备注入")
    uid = result.iloc[-1, 1]
    print(f'id获取成功{uid}')
    if not os.path.exists(f'./cache/{uid}/'):
        os.makedirs(f'./cache/{uid}/')
    #main.execute(uid)
    subprocess.run(["python3", "app/main.py", uid])
    return send_file(f'/www/wwwroot/default/cache/{uid}/结果-{uid}.zip', as_attachment=True)


@app.errorhandler(500)
def not_found(error):
    return render_template('error500.html'), 500

@app.route('/error500')
def error500(error):
    return render_template('error500.html'), 500

#if __name__ == "__main__":
    #app.run(host='0.0.0.0', debug=False, use_reloader=False)  # 启动程序
