from flask_appbuilder import AppBuilder, BaseView, expose, has_access
from app import appbuilder
from flask import redirect


class MyView(BaseView):

    default_view = 'method1'

    @expose('/method1/')
    @has_access
    def method1(self):
        self.update_redirect()
        return  redirect('http://localhost:8088')

appbuilder.add_view(MyView, "Superset", category='My View')
