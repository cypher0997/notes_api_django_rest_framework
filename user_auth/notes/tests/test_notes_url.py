from django.urls import reverse, resolve


class TestUrls:

    def test_detail_url(self):
        path = reverse('notes')
        assert resolve(path).view_name == 'notes'
