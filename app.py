from flask import Flask, request, render_template



app = Flask(__name__)



@app.route('/')
def index():
    return render_template('/audio_player.html')





#######################################
#                                     #
#  (Main) Starting Point of Program   #
#                                     #
#######################################
if __name__ == '__main__':
    app.run(debug=True)