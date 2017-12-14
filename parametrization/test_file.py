import uuid
import pytest


def is_uuid(s):
    try:
        uuid.UUID(s)
    except ValueError:
        return False
    return True


def test_is_uuid_32_chars():
    assert is_uuid('cde0fd2d72b14135a62e127dd0683218')


def test_is_uuid_v1():
    assert is_uuid(str(uuid.uuid1()))


def test_is_uuid_v4():
    assert is_uuid(str(uuid.uuid4()))


def test_is_uuid_invalid_32_non_hex():
    assert not is_uuid('z' * 32)


def test_is_uuid_invalid_non_32():
    assert not is_uuid('not a uuid')
