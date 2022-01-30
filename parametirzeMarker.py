import pytest
import sys

@pytest.mark.parametrize("username,password",
                         [
                             ("elad","yes"),
                             ("WD","tobe"),
                             ("kelev","dog"),
                             
                
                         ]
                         
                         )
def test_login(username,password):
    print(username)
    print(password)