"""
Desafio do Jogo de Adivinhação

Crie um jogo onde o computador escolhe um número aleatório entre 1 e 100,
e o jogador precisa adivinhar qual é esse número.

Requisitos:
1. O jogo deve informar se o palpite está alto ou baixo
2. Contar quantas tentativas o jogador usou
3. Permitir jogar novamente
4. Mostrar a pontuação baseada no número de tentativas:
   - Até 5 tentativas: 100 pontos
   - De 6 a 10 tentativas: 50 pontos
   - Mais de 10 tentativas: 25 pontos

Dicas:
- Use random.randint(1, 100) para gerar o número aleatório
- Use while True para criar um loop infinito
- Use break para sair do loop
- Use input() para receber os palpites do jogador
- Use try/except para tratar erros quando o usuário digitar algo que não é número

Bônus (opcional):
- Adicione níveis de dificuldade (fácil: 1-50, médio: 1-100, difícil: 1-200)
- Salve o recorde de pontuação em um arquivo

Exemplo de como começar:
1. Primeiro importe o módulo random
2. Crie um loop principal do jogo
3. Gere um número aleatório
4. Peça palpites ao jogador
5. Compare o palpite com o número e dê dicas
6. Conte as tentativas
7. Calcule a pontuação no final

Boa sorte!
"""

# Seu código começa aqui:
import random
nmrs = random.randint(1, 20)
tentativas = 0  # Criando contador de tentativas

while True:
   try:
      t = int(input('Tente adivinhar o número: '))
      tentativas += 1  # Aumenta o contador a cada tentativa
   except ValueError:
      print('Digite apenas números')
      continue
   if t == nmrs:
      print(f'Parabéns, você acertou em {tentativas} tentativas!')
      # Calcula pontuação após acertar
      if tentativas <= 5:
         print('Você fez 100 pontos!')
      elif tentativas <= 10:
         print('Você fez 50 pontos!')
      else:
         print('Você fez 25 pontos!')
      break
   elif t > nmrs:
      print('O número é menor que o seu palpite.')
   else:
      print('O número é maior que o seu palpite.')