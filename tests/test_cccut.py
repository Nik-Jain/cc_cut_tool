import os
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

@pytest.mark.parametrize("field_option, field_range, delimiter_option, delimiter, file_name, expected_result", 
                         [("-f", "2", "-d", ",", "fourchords.csv", "Artist\nMatt Redman\xa0and\xa0Jonas Myrin\nThirsty Merc\nHarry Styles\nToto\nCheb Khaled\nMichel Teló\nMichelle Branch\nBowling for Soup\nAlan Walker\n"),])
def test_delimiter_option(field_option, field_range, delimiter_option, delimiter, file_name, expected_result):
    result = os.popen(' '.join(['cccut', field_option, field_range, delimiter_option, delimiter, file_name, '|', 'head'])).read()
    assert expected_result == result
