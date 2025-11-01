import pytest
from projeto.src.estoque import EstoqueProduto, EstoqueInsuficienteException

class TestEstoqueProduto:
    def test_criacao_produto_com_estoque_inicial_valido(self):
        produto = EstoqueProduto('caneta', 10)
        assert produto.get_quantidade_atual() == 10

    def test_criacao_produto_com_estoque_negativo_deve_falhar(self):
        with pytest.raises(ValueError):
            EstoqueProduto('lápis', -1)
    
    def test_criacao_produto_com_nome_vazio_deve_falhar(self):
        with pytest.raises(ValueError):
            EstoqueProduto("  ", 0)

    def test_criacao_produto_com_quantidade_none_deve_falhar(self):
        with pytest.raises(ValueError):
            EstoqueProduto('borracha', None)

    def test_adicionar_itens_com_sucesso(self):
        produto = EstoqueProduto('caderno', 5)
        produto.adicionar(3)
        assert produto.get_quantidade_atual() == 8
    
    def test_adicionar_quantidade_zero_ou_negativa_deve_lancar(self):
        produto = EstoqueProduto('livro', 2)
        with pytest.raises(ValueError):
            produto.adicionar(0)
        with pytest.raises(ValueError):
            produto.adicionar(-5)
    
    def test_adicionar_none_deve_lancar(self):
        produto = EstoqueProduto("Agenda", 1)
        with pytest.raises(ValueError):
            produto.adicionar(None)
    
    def test_remover_itens_com_sucesso(self):
        produto = EstoqueProduto('papel', 10)
        produto.remover(4)
        assert produto.get_quantidade_atual() == 6

    def test_remover_quantidade_zero_ou_negativa_deve_lancar(self):
        produto = EstoqueProduto('marcador', 3)
        with pytest.raises(ValueError):
            produto.remover(0)
        with pytest.raises(ValueError):
            produto.remover(-2)

    def test_remover_none_deve_lancar(self):
        produto = EstoqueProduto('marca-texto', 3)
        with pytest.raises(ValueError):
            produto.remover(None)
    
    def test_remover_mais_do_que_disponivel_deve_lancar_estoque_insuficiente(self):
        produto = EstoqueProduto('Grampeador', 2)
        with pytest.raises(EstoqueInsuficienteException):
            produto.remover(3)

    def test_remover_exatamente_o_estoque_fica_zero(self):
        produto = EstoqueProduto('Tesoura', 4)
        produto.remover(4)
        assert produto.get_quantidade_atual() == 0