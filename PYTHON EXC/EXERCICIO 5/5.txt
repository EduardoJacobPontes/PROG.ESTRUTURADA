
import random

def main():
  vida_do_aventureiro = 100
  ataque_aventureiro = print(random.randint(10, 20))   
  defesa_aventureiro = print(random.randint(1, 5))  
  print("vida do aventureiro", vida_do_aventureiro, "- ataque aventureiro",ataque_aventureiro,"- defesa aventureiro",defesa_aventureiro)
  
  
  vida_monstro = print(random.randint(60, 80))
  ataque_monstro = print(random.randint(20, 30))   
  print("vida do monstro", vida_monstro,"- ataque do monstro",ataque_monstro,"- defesa do monstro")

  rodada = 1 

  while vida_do_aventureiro >=0 and vida_monstro >=0:
    print("rodada", rodada)
    vida_monstro = (vida_monstro - random.randint(1, ataque_aventureiro))
    if vida_monstro <=0:
      print("o mostro foi derrotado")
      break
     
    dano_monstro = (random.randint(1, ataque_monstro)- defesa_aventureiro) 
    if dano_monstro >=0:
      vida_do_aventureiro = (vida_do_aventureiro - dano_monstro)
    if vida_do_aventureiro <=0:
        print("o aventureiro fracassou")
        break

    rodada += 1

    print("vida do aventureiro", vida_do_aventureiro, "- ataque aventureiro",ataque_aventureiro,"- defesa aventureiro",defesa_aventureiro)
    print("vida do monstro", vida_monstro,"- ataque do monstro",ataque_monstro,"- defesa do monstro")

main()