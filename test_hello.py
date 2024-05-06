from hello import add, world


def test_add():
    assert add(1, 3) == 4
    
def test_world():
    assert world() == 'hello world'
