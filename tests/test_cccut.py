import os
import subprocess
import pytest

def test_version():
    result = subprocess.run(['cccut', '--version'], capture_output=True, text=True)
    assert "cccut v0.1.0" in result.stdout
    result = subprocess.run(['cccut', '-v'], capture_output=True, text=True)
    assert "cccut v0.1.0" in result.stdout

@pytest.mark.parametrize("field_option, field_range, file_name, expected_result", 
                         [("-f", "2", "sample.tsv", "f1\n1\n6\n11\n16\n21\n"),
                          ("-f", "1,2", "sample.tsv", 'f0\tf1\n0\t1\n5\t6\n10\t11\n15\t16\n20\t21\n'),])
def test_field_option(field_option, field_range, file_name, expected_result):
    result = subprocess.run(['cccut', field_option, field_range, file_name], capture_output=True, text=True)
    assert expected_result == result.stdout

@pytest.mark.parametrize("field_option, field_range, delimiter_option, delimiter, file_name, expected_result", 
                         [("-f", "2", "-d", ",", "fourchords.csv", "Artist\nMatt Redman\xa0and\xa0Jonas Myrin\nThirsty Merc\nHarry Styles\nToto\nCheb Khaled\nMichel Teló\nMichelle Branch\nBowling for Soup\nAlan Walker\n"),
                          ("-f", '"1 2"', "-d", ",", "fourchords.csv", '\ufeffSong title\tArtist\n"10000 Reasons (Bless the Lord)"\tMatt Redman\xa0and\xa0Jonas Myrin\n"20 Good Reasons"\tThirsty Merc\n"Adore You"\tHarry Styles\n"Africa"\tToto\n"Aicha"\tCheb Khaled\n"Ai Se Eu Te Pego"\tMichel Teló\n"All You Wanted"\tMichelle Branch\n"Almost"\tBowling for Soup\n"Alone"\tAlan Walker\n')])
def test_delimiter_option(field_option, field_range, delimiter_option, delimiter, file_name, expected_result):
    result = os.popen(' '.join(['cccut', field_option, field_range, delimiter_option, delimiter, file_name, '|', 'head'])).read()
    assert expected_result == result

def test_std_input_read():
    result = os.popen(' '.join(['tail', '-n5', 'fourchords.csv', '|', 'cccut', '-d,', '-f"1 2"'])).read()
    assert result == '"Young Volcanoes"\tFall Out Boy\n"You Found Me"\tThe Fray\n"You\'ll Think Of Me"\tKeith Urban\n"You\'re Not Sorry"\tTaylor Swift\n"Zombie"\tThe Cranberries\n'
