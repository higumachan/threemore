from flask import *
from logging.handlers import *
from settings import *
import pymongo

app = Flask(__name__);

formatter = logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
)
error_log = os.path.join(app.root_path, 'logs/error.log')
error_file_handler = RotatingFileHandler(
    error_log, maxBytes=100000, backupCount=10
)    
error_file_handler.setLevel(logging.ERROR)
error_file_handler.setFormatter(formatter)
app.logger.addHandler(error_file_handler)


@app.before_request
def before_request():
    g.conn = pymongo.Connection(host=DB_HOST);
    g.db = g.conn[DB_NAME];

@app.teardown_request
def teardown_request(exception):
    g.conn.close();

PAGE_PER_COUNT = 10;

@app.route("/index<int:id>.html")
def index(id):
    username = request.args["username"];

    recommends = list(g.db.recommends.find({"username": username}).skip(id * PAGE_PER_COUNT).limit(PAGE_PER_COUNT));
    return render_template("index.html", rs=recommends);

if __name__ == "__main__":
    app.debug = True;
    app.run(port=8000);

