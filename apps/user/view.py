from flask import Blueprint, render_template, request, redirect, url_for

from apps.user.model import User

user_bp = Blueprint("user", __name__)  # Blueprint("蓝图的名字", __name__)


@user_bp.route("/user")
def index():
    return "用户首页"


users = []


@user_bp.route("/user/reg", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        for u in users:
            if u.username == username:
                msg = "用户已经存在"
                return render_template("user/register.html", msg=msg)
        user = User(username, password)
        users.append(user)
        return redirect("/user/show")
    return render_template("user/register.html")


@user_bp.route("/user/show")
def show():
    return render_template("user/show.html", users=users)


@user_bp.route("/user/del")
def dele():
    name = request.args.get("username")
    for i in users:
        if name == i.username:
            users.remove(i)
            return redirect("/user/show")
    else:
        return "错误"
