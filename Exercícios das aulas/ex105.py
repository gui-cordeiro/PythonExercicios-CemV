# Exercício 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#                - Quantidades de notas;
#                - A maior nota;
#                - A menor nota;
#                - A média da turma;
#                - A situação (opcional).
#                Adicione também as docstrings da função.

def notas(*notas, sit=False):
   """
   -> Função para analisar notas e situações de vários alunos.   
   :param notas: Uma ou mais notas dos alunos (aceita várias).
   :param sit: [OPCIONAL] Indica se deve ou não exibir a situação geral dos alunos.
   :return: Dicionário contendo informações acerca da situação da turma. 
   """
   dados = dict()
   dados['total'] = len(notas)
   dados['maior'] = max(notas)
   dados['menor'] = min(notas)
   dados['média'] = (sum(notas) / len(notas))
   if sit:
      if dados['média'] > 7:
         dados['situação'] = 'BOM'
      elif dados['média'] > 5:
         dados['situação'] = 'RAZOÁVEL'
      else:
         dados['situação'] = 'RUIM'
   return dados

# help(notas)
situacao = notas(8.1, 9, 10, 5, 5.3, 10, 10, 5, sit=True)
print(situacao)