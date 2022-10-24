import os
import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient


app=Flask(__name__)
client=MongoClient("mongodb+srv://eunbiyoon:Emily135@microblog-application.vihgli5.mongodb.net/test")
app.db=client.voc

@app.route("/", methods=["POST"])
def home():
    if request.method=="POST":
        entry_content=request.form.get("content")
        formatted_date=datetime.datetime.today().strftime("%Y-%m-%d")
        app.db.entries.insert_one({"content":entry_content, "date":formatted_date})
        if request.form.get('action1') == 'Noise/Vibration':
            return render_template('tl/noise.html') # do something
            
        else:
            pass # unknown
    entries_with_date=[
        (
            entry["content"],
            entry["date"],
            datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
        )
        for entry in app.db.entries.find({})
    ]
    return render_template("index.html", entries=entries_with_date)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


