from flask import render_template_string

from utils import TestCase


class TestTemplateUse(TestCase):

    def test_resized_img_src(self):

        @self.app.route('/resized_img_src')
        def use():
            return render_template_string('''
                <img src="{{ resized_img_src('cc.png') }}" />
            '''.strip())

        res = self.client.get('/resized_img_src')
        self.assert200(res)
        self.assertIn('src="/imgsizer/cc.png?', res.data.decode('utf-8'))

    def test_url_for(self):

        @self.app.route('/url_for')
        def use():
            return render_template_string('''
                <img src="{{ url_for('images', filename='cc.png') }}" />
            '''.strip())

        res = self.client.get('/url_for')
        self.assert200(res)
        self.assertIn('src="/imgsizer/cc.png?', res.data.decode('utf-8'))
