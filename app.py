from flask import Flask,request,render_template
app = Flask(__name__)


@app.route("/",methods=["GET","POST"])


def ATM_Transactions():

    if request.method=="POST":
        resp = request.form

        a = resp.get('num1')
        a=float(a)
        balance = 120756.45

        if resp.get('key')=='1':
            try:
                result = balance - float(a)
                if float(a)>balance:
                    raise ValueError("insufficient balance")
            except ValueError as ve:
                result=ve
                return render_template("result4.html", resp=result)


            return render_template("result1.html",resp=result,res1=a)
        elif resp.get('key')=='2':
            result=balance+int(a)

            return render_template("result2.html",resp=result)

    else:

        return render_template("calci.html")





if __name__ == '__main__':
    app.run(debug=True)