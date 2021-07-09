from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestModels:
    def test_note_exists(self):
        usr_inst = mixer.blend('notes.Notes', id=1)
        assert usr_inst.is_notes_instance == True

    def test_note_not_exists(self):
        usr_inst = mixer.blend('notes.Notes', id=0)
        assert usr_inst.is_notes_instance == False
