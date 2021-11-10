# Popen, PIPE이용하여 data보내기(실패?)
# from subprocess import Popen, PIPE
# import json
#
# # Initialise the data
# array = ["This is from python!!!"]
# data = {'array':array}
#
# # Stringify the data
# stringified_data = json.dumps(data)
#
# # Call the node process and pass the data as command line argument
# process = Popen(['node', 'arraysum.js', stringified_data], stdout=PIPE)
#
# # This line essentially wait for the
# # node process to complete and then read stdout data
# stdout = process.communicate()[0]
#
# # The stdout is a bytes string, you can convert it to another encoding
# # but json.load() supprots bytes string so we aren't converting
#
# # Parse the data into json
# result_data = json.loads(stdout)
# array_sum = result_data['sum']
# print('Sum of array from Node.js process = ', array_sum)


# Flask이용하여 data보내기(document보고 처음부터)python data send to nodejs

# from flask import Flask, render_template, make_response
#
# # __name__ : name of th application's module or package
# # 이게 있어야 flask가 어디서 resource를 찾아햐 하는지 알 수 있다.
# # name에 app(여기서는 req.data.py)파일명이 문자열로 들어간다.
# app = Flask(__name__)
# # Flask가 우리 function에 어떤 URL을 trigger해야 하는거 설정
# @app.route("/")
# def hello_world():
#     return "Hello, World!"
# # debug 모드 켜기
# if __name__ == '__main__':app.run(debug=True)
#
# @app.errorhandler(404)
# def not_found(error):
#     resp = make_response(render_template('error.html'), 404)
#     resp.headers['X-Something'] = 'A value'
#     return resp


# socket으로 data 보내기
# import socket
#
# host = socket.gethostname()
# port = 8080
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((host, port))
# s.sendall(b'Hello, World')
# s.close()
# data = s.recv(1042)



# requests, json으로 json과 연결하기
# client
import requests
import json

url = "http://localhost:8080"
data = {"msg": "This is msg from python"}
# header = {"content-type": "application/json", "Accept": "text/plain", "x-access-token": "iwantaconnect!"}
header = {"content-type": "application/json", "Accept": "text/plain"}
r = requests.post(url, data=json.dumps(data), headers=header)

# print(r.status_code) # nodejs에서 보내주는 satus code출력(200)
# print(r.text) # nodejs서 보내주는 상태 출력




