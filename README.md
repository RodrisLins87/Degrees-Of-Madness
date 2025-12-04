# Degree of Madness

**Degree of Madness** é um jogo 2D desenvolvido em **Python** usando a biblioteca **Pygame**, onde o jogador controla um personagem, coleta pontos, evita inimigos e pode recuperar vida através de itens.

---

## Tecnologias

- **Linguagem:** Python 3.11+  
- **Biblioteca principal:** [Pygame](https://www.pygame.org/)  
- **Dependências adicionais:** Nenhuma além do Pygame  

---

## Estrutura do Código

O projeto utiliza **Programação Orientada a Objetos (POO)**:

### Classe `Entidade`
Classe base para objetos que se movem verticalmente:

- **Atributos:**  
  - `image`: sprite do objeto  
  - `rect`: retângulo para colisões  
  - `vel`: velocidade do movimento vertical  

- **Métodos:**  
  - `update()`: move o objeto para baixo  
  - `draw(tela)`: desenha o objeto na tela  
  - `reset_if_needed(altura, largura)`: reposiciona o objeto no topo da tela caso ultrapasse a borda inferior  

---

### Classe `Player`
Representa o jogador:

- **Atributos:**  
  - `image`, `rect`  
  - `vel`: velocidade de movimento  
  - `vida`: vida do jogador (0-100)  

- **Métodos:**  
  - `mover(largura, altura)`: movimentação via **W, A, S, D** com limites de tela  
  - `draw(tela)`: renderiza o player  

---

### Classes Especializadas
- `Enemy(Entidade)`: inimigos que reduzem a vida do jogador  
- `Item(Entidade)`: itens que aumentam a vida do jogador  

---

### Classe `Game`
Classe principal que controla todo o fluxo do jogo:

- **Inicialização (`__init__`)**  
  - Configura a janela, fundo, sons, músicas, clock e fontes  
  - Carrega imagem de **Game Over**  
  - Inicializa variáveis de jogo com `reset_game()`  

- **`reset_game()`**  
  - Cria jogador, inimigos, obstáculos e itens  
  - Reinicia pontuação e controle de aumento de velocidade  

- **`aumentar_velocidade()`**  
  - Aumenta a velocidade dos inimigos a cada 5 segundos (aprox. 300 frames)  

- **`verificar_colisoes()`**  
  - Obstáculos: adicionam pontos  
  - Inimigos: reduzem vida do jogador  
  - Itens de vida: aumentam a vida do jogador  

- **`run()`**  
  - Loop principal do jogo (60 FPS)  
  - Processa eventos, movimentos, colisões, desenho e controle de Game Over  
  - Atualiza a tela com `pygame.display.update()`  
  - Permite reiniciar o jogo clicando após Game Over  

---

# Resultado

![Imagem do Resultado final do jogo Degree of Madness](https://github.com/RodrisLins87/Degrees-Of-Madness/blob/main/Degree%20of%20Madness_print.png)

## Como Jogar
1. Execute o script principal:

```bash
python main.py


---

Durante o jogo, o personagem se movimenta pelas teclas: A,W,S,D.








