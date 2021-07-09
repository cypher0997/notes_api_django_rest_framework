from django.contrib.auth.models import User
import pytest


@pytest.mark.django_db
class TestModels:
    def test_user_exists(self):
        res = None
        data = User.objects.get(pk=8)
        if isinstance(data, User):
            res = True
        else:
            res = False
        assert res == True
