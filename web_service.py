from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

result = {
    "results":[
            {"name":{"first":"Roger", "last":"L."}, "item":"cookset", "icon":"data:image/jpeg;base64,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"},
            {"name":{"first":"Rick", "last":"C."}, "item":"行山杖", "icon":"https://www.icmetl.org/wp-content/uploads/2020/11/user-icon-human-person-sign-vector-10206693.png"},
            {"name":{"first":"Raymond", "last":"K."}, "item":"二人帳篷", "icon":"https://www.icmetl.org/wp-content/uploads/2020/11/user-icon-human-person-sign-vector-10206693.png"},
            {"name":{"first":"Kelvin", "last":"L."}, "item":"防水袋", "icon":"https://www.icmetl.org/wp-content/uploads/2020/11/user-icon-human-person-sign-vector-10206693.png"},
            {"name":{"first":"Rose", "last":"Lam"}, "item":"跑山鞋", "icon":"https://www.icmetl.org/wp-content/uploads/2020/11/user-icon-human-person-sign-vector-10206693.png"},
            {"name":{"first":"Sandy", "last":"Chan"}, "item":"背心背囊", "icon":"https://www.icmetl.org/wp-content/uploads/2020/11/user-icon-human-person-sign-vector-10206693.png"},
            {"name":{"first":"Snow", "last":"White"}, "item":"紅蘋果", "icon":"https://www.icmetl.org/wp-content/uploads/2020/11/user-icon-human-person-sign-vector-10206693.png"},

        ]
}

@app.route("/status", methods=["GET"])
def status():   # for testing connection
    print("/status")
    result = {}
    result['status'] = 'OK connected'
    print("end of /status")
    return jsonify(result)
 

@app.route("/participant", methods=["GET"])
def get_participant():
    print(f"/participant")    
    # result ={"data": 1}
    return jsonify(result)


#return a file
@app.route("/resource/<filename>", methods=["GET"])
def resource(filename):   
    print(f"/resource/{filename}")
    return send_file(filename)



if __name__ == '__main__':
    port = 5001
    print(f"Start Service at port: {port}")
    app.run(host="0.0.0.0", port=port, debug=False)
