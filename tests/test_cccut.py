import subprocess
import pytest

def test_version():
    result = subprocess.run(['cccut', '--version'], capture_output=True, text=True)
    assert "cccut v0.1.0" in result.stdout
    result = subprocess.run(['cccut', '-v'], capture_output=True, text=True)
    assert "cccut v0.1.0" in result.stdout

@pytest.mark.parametrize("field_option, field_range, file_name, expected_result", 
                         [("-f", "2", "sample.tsv", "f1\n1\n6\n11\n16\n21\n"),])
def test_field_option(field_option, field_range, file_name, expected_result):
    result = subprocess.run(['cccut', field_option, field_range, file_name], capture_output=True, text=True)
    assert expected_result == result.stdout

