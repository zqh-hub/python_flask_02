Python_Blueprint

###### 框架目录

```
|--- apps
		|--- __init__
		|--- user
			|--- view.py
			|--- model.py
		
		|--- goods
|--- static
	 |--- css
	 |--- js
	 |--- images
|--- templates
|--- app.py
|--- settings
```

创建app

```python
# apps/__init__
from flask import Flask
import settings
from apps.user.view import user_bp

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(settings)
    app.register_blueprint(user_bp)  # -- -- -- -- -- -- 蓝图注册
    print(app.url_map)
    return app
    
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
# app.py
from apps import create_app

app = create_app()    # -- -- -- -- -- -- 创建app

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090)
    
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
# apps/user/view.py
from flask import Blueprint

user_bp = Blueprint("user", __name__)  # Blueprint("蓝图的名字", __name__)

@user_bp.route("/user")
def index():
    return "用户首页"
```

