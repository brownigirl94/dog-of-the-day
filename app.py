from flask import Flask, render_template
import random

app = Flask(__name__)

# list fun gifs
images = [
    "https://media.giphy.com/media/3otPoL5Ee6HzGbC2yY/giphy.gif",
    "https://media.giphy.com/media/mCRJDo24UvJMA/giphy.gif",
    "https://media.giphy.com/media/4Zo41lhzKt6iZ8xff9/giphy.gif",
    "https://media.giphy.com/media/xThtadSLoInlcD1UmA/giphy.gif",
    "https://media.giphy.com/media/1kkxWqT5nvLXupUTwK/giphy.gif",
    "https://media.giphy.com/media/1kkxWqT5nvLXupUTwK/giphy.gif",
    "https://media.giphy.com/media/1kkxWqT5nvLXupUTwK/giphy.gif",
    "https://media.giphy.com/media/14rtlR7b01cjQI/giphy.gif",
    "https://media.giphy.com/media/pcwaLYOQb3xN6/giphy.gif",
    "https://media.giphy.com/media/aSZSj0mT8f6tW/giphy.gif",
    "https://media.giphy.com/media/U7969wTwwtn6KBvEdA/giphy.gif",
    "https://media.giphy.com/media/U7969wTwwtn6KBvEdA/giphy.gif",
    "https://media.giphy.com/media/3oEduXZs5RBUe4b8Gc/giphy.gif",
    "https://media.giphy.com/media/mRB9PmJFOjAw8/giphy.gif",
    "https://media.giphy.com/media/10AVDflAKRV86A/giphy.gif",
    "https://media.giphy.com/media/10AVDflAKRV86A/giphy.gif",
    "https://media.giphy.com/media/10AVDflAKRV86A/giphy.gif"
]

@app.route('/')
def index():
    url = random.choices(images)
    return render_template('index.html', url=url[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0")
