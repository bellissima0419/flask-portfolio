from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/<username>/<int:post_id>')
# def my_home(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)

# @app.route('/')
# def my_home():
#     return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# # @app.route('/components.html')
# # def components():
# #     return render_template('components.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')
