from django.urls import reverse, resolve


class TestUrls:

    def test_login_url(self):
        path = reverse('login_method')
        assert resolve(path).view_name == 'login_method'

    def test_register_url(self):
        path = reverse('register_method')
        assert resolve(path).view_name == 'register_method'
