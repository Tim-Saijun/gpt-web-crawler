from doctest import debug
from flask import Flask, request, jsonify, render_template,send_file
from file_info import get_tree, get_tree_as_file
import os

app = Flask(__name__)
@app.route('/')
def api_docs():
    return render_template('api_docs.html')

@app.route('/get_tree')
def get_tree_():
    target_folder = request.args.get('target_folder')
    return get_tree(target_folder)

@app.route('/get_tree_as_file')
def get_tree_as_file_():
    target_folder = request.args.get('target_folder')
    file_path = get_tree_as_file(target_folder)
    print(file_path)
    return send_file(file_path, as_attachment=True)

@app.route('/get_tree_url')
def get_tree_url():
    target_folder = request.args.get('target_folder')
    file_path = get_tree_as_file(target_folder)
    file_name = os.path.basename(file_path)
    return f"http://{request.host}/{file_name}"

@app.route('/<path:filename>.json')
def send_json_file(filename):
    print(filename)
    return send_file(filename + '.json', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
