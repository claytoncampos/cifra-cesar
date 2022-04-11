from cesar.cesar import encripta


def test_encripta_clayton_retorna_pynlgba():
    assert encripta('clayton') == 'pynlgba'


def test_encripta_pynlgba_retorna_clayton():
    assert encripta('pynlgba') == 'clayton'


def test_encripta_deve_retornar_minusculas():
    assert encripta('A').islower()


def test_encripta_deve_preservar_os_espacos():
    resultado = encripta('e a')
    assert resultado[1] == ' '
