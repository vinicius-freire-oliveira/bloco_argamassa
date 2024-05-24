# Definição da classe Bloco que representa um bloco de construção com suas dimensões e juntas de argamassa
class Bloco:
    def __init__(self, comprimento, altura, espessura, junta_horizontal, junta_vertical):
        # Inicializa os atributos do bloco com as dimensões fornecidas
        self.comprimento = comprimento
        self.altura = altura
        self.espessura = espessura
        self.junta_horizontal = junta_horizontal
        self.junta_vertical = junta_vertical

    # Método para calcular o número de blocos necessários por metro quadrado (m²)
    def calcular_numero_blocos(self):
        # Fórmula para calcular o número de blocos considerando as juntas de argamassa
        n = 1 / ((self.comprimento + self.junta_vertical) * (self.altura + self.junta_horizontal))
        return n

    # Método para calcular o volume de argamassa necessário por metro quadrado (m²)
    def calcular_volume_argamassa(self):
        # Calcula o número de blocos por m²
        n = self.calcular_numero_blocos()
        # Fórmula para calcular o volume de argamassa
        V = (1 - n * (self.comprimento * self.altura)) * self.espessura
        return V

    # Método para calcular o consumo de blocos e argamassa por metro quadrado (m²)
    def calcular_consumo(self):
        # Obtém o número de blocos por m²
        numero_blocos = self.calcular_numero_blocos()
        # Obtém o volume de argamassa por m²
        volume_argamassa = self.calcular_volume_argamassa()
        # Retorna ambos os valores
        return numero_blocos, volume_argamassa

# Exemplo de uso da classe Bloco
# Cria uma instância da classe Bloco com as dimensões e juntas especificadas
bloco = Bloco(comprimento=0.39, altura=0.19, espessura=0.14, junta_horizontal=0.015, junta_vertical=0.015)

# Calcula o número de blocos e o volume de argamassa por metro quadrado (m²)
numero_blocos, volume_argamassa = bloco.calcular_consumo()

# Exibe apresentação
print("\nCálculo para número de blocos (0,39 x 0,19 x 0,14) e volume de argamassa por m²\n")
# Exibe o número de blocos por metro quadrado com duas casas decimais
print(f"Número de blocos por m²: {numero_blocos:.2f} un/m²")
# Exibe o volume de argamassa por metro quadrado com quatro casas decimais
print(f"Volume de argamassa por m²: {volume_argamassa:.4f} m³/m²")

