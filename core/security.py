from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verificar_senha(senha: str, hash_senha: str) -> bool:
    """_summary_
    Verifica senha comparando como texto, informada pelo usuário.
    Args:
        senha (str): _description_
        hash_senha (str): _description_

    Returns:
        bool: _description_
        True or False
    """
    return CRIPTO.verify(senha, hash_senha)

def gra_hash_senha(senha: str) -> str:
    """_summary_
    Função que gera e retorna o hash da senha.
    Args:
        senha (str): _description_

    Returns:
        str: _description_
    """
    return CRIPTO.hash(senha)
