import uuid
import pytest


def is_uuid(s):
    try:
        uuid.UUID(s)
    except ValueError:
        return False
    return True


@pytest.mark.parametrize('uuid_', ['cde0fd2d72b14135a62e127dd0683218',
                                   str(uuid.uuid1()),
                                   str(uuid.uuid4())])
def test_is_uuid(uuid_):
    assert is_uuid(uuid_)


@pytest.mark.parametrize('uuid_', ['z' * 32,
                                   'not a uuid'])
def test_is_uuid_invalid(uuid_):
    assert not is_uuid(uuid_)
