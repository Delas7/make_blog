from flask import Flask, Blueprint, request, render_template, jsonify, make_response, redirect, url_for
from blog_control.user_mgmt import User
from flask_login import login_user, current_user, logout_user
import datetime

blog_abtest = Blueprint('blog', __name__)

@blog_abtest.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'GET':
        print(request.args.get('user_email'))
        return redirect(url_for('blog.test_blog'))
    else:
        # print(request.headers)
        # content type 이 application/json 인 경우에만 body 영역의 파라미터를 가져올 수 있음
        # print(request.get_json())
        
        print(request.form['user_email'])
        user = User.create(request.form['user_email'], 'A')
        # 
        login_user(user, remember=True, duration=datetime.timedelta(days=365))
        
        
        return redirect(url_for('blog.test_blog'))
    # return redirect('/blog/test_blog')
    # return make_response(jsonify(success=True), 200)
    
@blog_abtest.route('/test_blog', methods=['GET'])
def test_blog():
    if current_user.is_authenticated:
        print('login')
        return render_template('blog_A.html', user_email=current_user.user_email)
    else:
        print('unlogin')
        return render_template('blog_A.html')
    
    
@blog_abtest.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('blog.test_blog'))