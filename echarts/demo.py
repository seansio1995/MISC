from flask  import Flask , render_template, url_for



app=Flask(__name__)

@app.route("/")

def echar():
    return render_template("mydemo.html")



if __name__=="__main__":
    app.run(debug=True)
