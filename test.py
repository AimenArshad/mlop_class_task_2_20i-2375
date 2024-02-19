import pytest
from main import StudentsInMLOps

@pytest.fixture
def ml_ops_class():
    return StudentsInMLOps()

def test_enrollStudents(ml_ops_class):
    ml_ops_class.enrollStudents(5)
    assert ml_ops_class.getTotalStrength() == 5

def test_dropStudents(ml_ops_class):
    ml_ops_class.enrollStudents(10)
    ml_ops_class.dropStudents(3)
    assert ml_ops_class.getTotalStrength() == 7

def test_getClassName(ml_ops_class):
    assert ml_ops_class.getClassName() == "MLOps"
