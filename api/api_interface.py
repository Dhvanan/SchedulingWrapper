import sys
sys.path.append('/root/SchedulingWrapper')
from boot_instances import boot
import Scheduler
from flask import Flask, jsonify
from flask import make_response
from flask import abort
from flask import request

app = Flask(__name__)

@app.route('/todo/api/v1.0/tasks',methods=['GET'])
def test():
    print('in test')
    return jsonify({1:1})

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_instances():
    print 'in create tasks'
    print request.json
    if not request.json:
        abort(400)
    boot(request.json)
    print 'calling boot'
    return jsonify({'1':1})


if __name__ == '__main__':
    app.run(port=5001,debug=True)

