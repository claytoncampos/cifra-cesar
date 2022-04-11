from cesar.cesar import encripta


def test_encripta_clayton_retorna():
    assert encripta('Clayton') == 'huscfa'
