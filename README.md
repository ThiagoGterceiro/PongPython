# PongPython

Explicação do código do jogo Pong com pontuação em arquivo de texto
O código que criamos é uma implementação simples do jogo Pong usando a biblioteca pygame em Python. Além disso, implementamos a funcionalidade para registrar e armazenar a pontuação do jogo em um arquivo de texto, chamado placar.txt. Abaixo está a explicação de como o código funciona, dividido em suas principais seções:

1. Inicialização e configuração
No início do código, a biblioteca pygame é inicializada com o comando pygame.init(), o que é necessário para usar todos os recursos do pygame, como gráficos e eventos.

Definimos também algumas variáveis importantes:

Tamanho da tela: A tela do jogo tem 800 pixels de largura e 600 pixels de altura.

Cores: Usamos as cores PRETO (para o fundo da tela) e BRANCO (para a bola e as raquetes).

Raquetes e bola: A raquete tem 15 pixels de largura e 100 pixels de altura, e a bola tem 10 pixels de raio. A velocidade da bola e das raquetes também é definida, além de sua posição inicial.

2. Função salvar_placar
A função salvar_placar é responsável por gravar a pontuação no arquivo de texto placar.txt. Toda vez que um ponto é marcado, essa função é chamada para atualizar o placar. Ela escreve no arquivo a pontuação de ambos os jogadores:

python
Copiar
def salvar_placar():
    with open("placar.txt", "w") as arquivo:
        arquivo.write(f"Jogador Esquerdo: {placar_esquerda}\n")
        arquivo.write(f"Jogador Direito: {placar_direita}\n")
Esse arquivo é sobrescrito cada vez que o placar é atualizado.

3. Função desenha_jogo
Esta função é responsável por desenhar todos os elementos gráficos do jogo na tela:

O fundo da tela é pintado de preto.

As raquetes são desenhadas como retângulos brancos, com as coordenadas baseadas na posição de cada raquete.

A bola é desenhada como um círculo branco.

Uma linha central divide a tela em duas partes.

Além disso, a função também exibe a pontuação de cada jogador no topo da tela, utilizando uma fonte para desenhar o texto de cada jogador:

python
Copiar
texto_esquerda = fonte.render(str(placar_esquerda), True, BRANCO)
texto_direita = fonte.render(str(placar_direita), True, BRANCO)
Esses textos são então posicionados na tela para mostrar a pontuação.

4. Função move_bola
A função move_bola controla o movimento da bola, a detecção de colisões e a pontuação. Ela move a bola para a direita ou para a esquerda (bola_velocidade_x), e para cima ou para baixo (bola_velocidade_y). A cada movimento, a bola pode colidir com as paredes superior ou inferior, invertendo sua direção vertical.

Quando a bola atinge a borda esquerda ou direita da tela (indicando que um dos jogadores marcou um ponto), o placar é atualizado e a função salvar_placar é chamada para armazenar a pontuação no arquivo:

python
Copiar
if bola_x - bola_raio <= 0:
    placar_direita += 1
    salvar_placar()
    bola_x = LARGURA // 2
    bola_y = ALTURA // 2
    return True
Esse código detecta quando a bola passa pela raquete da esquerda ou da direita, aumenta a pontuação do jogador correspondente e reinicia a posição da bola no centro da tela.

5. Função move_raquetes
A função move_raquetes trata o movimento das raquetes dos jogadores. As raquetes podem ser movidas para cima e para baixo pelas teclas do teclado:

Jogador esquerdo: Usando as teclas W (para cima) e S (para baixo).

Jogador direito: Usando as teclas de seta para cima e para baixo.

A função também garante que as raquetes não saiam da tela, verificando se a posição das raquetes não ultrapassa o topo ou o fundo da tela.

6. Loop principal do jogo
O loop principal é o coração do jogo. Dentro desse loop:

A função move_raquetes é chamada para atualizar as posições das raquetes.

A função move_bola é chamada para mover a bola e verificar se houve algum ponto marcado.

A função desenha_jogo é chamada para desenhar todos os elementos (bola, raquetes e pontuação) na tela.

O loop roda a 60 quadros por segundo (FPS) para garantir que o jogo seja executado de maneira suave.

7. Arquivo de pontuação
Cada vez que um ponto é marcado, o arquivo placar.txt é atualizado com a pontuação mais recente. O conteúdo do arquivo se parecerá com isto:

yaml
Copiar
Jogador Esquerdo: 1
Jogador Direito: 0
Isso permite que a pontuação seja salva e que os jogadores possam consultar o placar a qualquer momento.

