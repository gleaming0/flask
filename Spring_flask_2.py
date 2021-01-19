from flask import Flask, render_template, request

app = Flask(__name__)

class Problem:
    def __init__(self, Pnum, Pname, Solved, Pcond, Pdetail, Pinout):
        self.Pnum = Pnum
        self.Pname = Pname
        self.Solved = Solved
        self.Pcond = Pcond
        self.Pdetail = Pdetail
        self.Pinout = Pinout
    
    def dict(self):
        return {"Pnum" : self.Pnum, "Pname":self.Pname, "Solved":self.Solved, "Pcond":self.Pcond, "Pdetail":self.Pdetail, "Pinout":self.Pinout}

p_1001 = Problem("1001", "a+b", "Null", ["0.5초", "128MB"],["두 개의 숫자 a,b를 입력받아 합을 출력하시오", "0 < a,b <100", "첫째 줄에 a+b를 출력한다."], [["20 4"], "24"])
p_1002 = Problem("1002", "a-b", "Null", ["0.5초", "128MB"],["2개의 숫자 a,b를 입력받아 차을 출력하시오.", "0 < a,b <100", "첫째 줄에 a-b를 출력한다."], [["20 4"], "16"])
p_1003 = Problem("1003", "a*b", "Null", ["0.5초", "128MB"],["2개의 숫자 a,b를 입력받아 곱을 출력하시오.", "0 < a,b <100", "첫째 줄에 a*b를 출력한다."], [["20 4"], "80"])
p_1004 = Problem("1004", "a/b", "Null", ["0.5초", "128MB"],["2개의 숫자 a,b 를 입력받아 몫을 출력하시오.", "0 < a,b <100", "첫째 줄에 a/b를 출력한다."], [["20 4"], "5"])
p_1005 = Problem("1005", "a%/b", "Null", ["0.5초", "128MB"],["2개의 숫자 a,b를 입력받아 나머지을 출력하시오.", "0 < a,b <100", "첫째 줄에 a%b를 출력한다."], [["20 4"], "0"])

Problems = {1001 : p_1001, 1002 : p_1002, 1003 : p_1003, 1004 : p_1004, 1005 : p_1005}

@app.route('/return_Pinfo', methods=['POST'])
def return_Pinfo():
    input_data = request.get_json()
    Pnum = input_data["Pnum"][0] #1001
    Pinfo = getattr(Problems[Pnum], "dict")() #1001의 문제정보
    
    makeinfo = {}
    dictt = Problems[Pnum].dict()
    for key, value in dictt.items():
        makeinfo[key] = value
        print(key, value)
    
    return makeinfo #결과적으론 이게 출력됨

@app.route('/change_Pinfo', methods=['POST'])
def change_Pinfo():
    input_data = request.get_json()
    SubNum = input_data["SubNum"][0] #1001
    Result = input_data["Result"] #T
    
    setattr(Problems[SubNum], "Solved", Result)
    
    return Problems[SubNum].Solved #return 값 없어야 함

if __name__ == '__main__':
    app.run(debug = True)

    #host='127.0.0.1' : 1234일 경우 그 웹에 접속하면 됨
    #'0.0.0.0:1234' -> localhost:1234 해도 ok
    #'내IP:1234' -> 내IP:1234
    
    #app.run(host='192.168.35.5', port=1234)