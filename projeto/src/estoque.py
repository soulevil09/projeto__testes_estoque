from typing import Optional

class EstoqueInsuficienteException(Exception):
    """Exceção lançada quando uma remoção deixaria o estoque negativo"""
    pass

class EstoqueProduto:
    def __init__(self, nome_produto: str, quantidade_inicial: int) -> None:
        if quantidade_inicial is None:
            raise ValueError("quantidade_inicial não pode ser None")
        if quantidade_inicial <0:
            raise ValueError("quantidade_inicial não pode ser negativa")
        if not nome_produto or not str(nome_produto).strip():
            raise ValueError("nome_produto não pode ser vazio")
        self._nome = nome_produto.strip()
        self._quantidade = int(quantidade_inicial)

    def adicionar(self, quantidade: int) -> None:
        if quantidade is None or quantidade <= 0:
            raise ValueError("quantidade a adicionar deve ser > 0")
        self._quantidade += int(quantidade)
    
    def remover(self, quantidade: int) -> None:
        if quantidade is None or quantidade <= 0:
            raise ValueError("quantidade a remover deve ser > 0")
        quantidade = int(quantidade)
        if self._quantidade - quantidade < 0:
            raise EstoqueInsuficienteException(
                f"Remoção de {quantidade} excede o estoque atual de {self._quantidade}"
            )
        self._quantidade -= quantidade

    def get_quantidade_atual(self) -> int:
        return self._quantidade       