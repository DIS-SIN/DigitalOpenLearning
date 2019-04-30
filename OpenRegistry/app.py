from flask import Flask, redirect, url_for, request, jsonify, render_template
app = Flask(__name__)

# @app.route('/success/<submission>')
# def success(submission):
#     # return "The content has been successfully submitted: %s" % url
#     data = { "url": submission }
#     # data = submission
#     response = jsonify(data)
#     return response

# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         # submission = {
#         #     "url": request.form['url']
#         # }
#         submission = request.form['url']

#     return redirect(url_for('success', submission = submission))






# @app.route('/success/<submission>')
# def success(submission):
#     data = { "url": submission }
#     response = jsonify(data)
#     return response

# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         submission = request.form['url']

#     return redirect(url_for('success', submission = submission))



# @app.route('/success/<submission>')
# def success(submission):
#     data = submission
#     response = jsonify(data)
#     return response

# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         submission = {
#             "url": request.form['url']
#         }

#     return redirect(url_for('success', submission = submission))




# @app.route('/success/<submission>')
# def success(submission):
#     data = {
#         'url': submission.get('url')
#     }
#     response = jsonify(data)
#     return response

# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         submission = {
#             "url": request.form['url']
#         }


#     return redirect(url_for('success', submission = submission))





# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         submission = request.form['url']

#     data = { 'url': submission }
#     response = jsonify(data)
#     return response
#     # return redirect(url_for('success', submission = submission))




# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         submission = {
#             "url": request.form['url'],
#             "name": request.form['name']
#         }
#     response = jsonify(submission)
#     return response





# @app.route('/submit', methods=['POST'])
# def submit():
#     data = request.get_json()
#     response = jsonify(data)
#     return response



# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         submission = request.form
#     response = jsonify(submission)
#     return response




# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         submission = {
#             'url': request.form['url'],
#             'categories': request.form.getlist('category')
#         }
#     response = jsonify(submission)
#     return response



@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    response = jsonify(data)
    print(data)
    print(response)
    return response


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        response = jsonify(data)
        return response
    else:
        return render_template('openRegistry.html')


if __name__ == '__main__':
   app.run(debug = True)