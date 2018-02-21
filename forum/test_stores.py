import pytest
import models, store

def test_stores_should_be_similar():
    member_store1 = store.MemberStore()
    member_store2 = store.MemberStore()

    assert member_store1.get_all() is member_store2.get_all()

def test_get_by_id_should_retrieve_same_object():
    member_store = store.MemberStore()
    member = models.Member('TEST', 28)
    member_store.add(member)

    member_retrieved = member_store.get_by_id(member.id)

    assert member is member_retrieved

def test_delete_should_raise_error():
    member_store = store.MemberStore()

    with pytest.raises(ValueError):
        member_store.delete(5)

def test_update_member():
    member_store = store.MemberStore()
    member = models.Member('TEST', 28)
    member_store.add(member)

    member_replacement = models.Member('TEST2', 58)
    member_replacement.id = member.id

    member_store.update(member_replacement)
    member_retrieved = member_store.get_by_id(member.id)

    assert member_retrieved is member_replacement

pytest.main()
