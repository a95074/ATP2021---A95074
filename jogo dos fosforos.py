# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

def fosforos():
    n=21
    ordem=input("Pretendende jogar primeiro? Sim(s) ou Não(n):")
    if ordem=="Sim" or ordem=="s" or ordem=="sim" or ordem=="S":
            while n >1:
                jogada=int(input("Quantos fósforos quer tirar? 1, 2, 3, 4?"))
                if jogada>=1 and jogada<=4:
                    n=n-jogada
                    print("Restam", n, "fósforos!")
                    if jogada==1:
                        n=n-4
                        print("A jogada do computador é retirar 4 fósforos.")
                        print("Restam", n, "fósforos!")
                    if jogada==2:
                        n=n-3
                        print("A jogada do computador é retirar 3 fósforos.")
                        print("Restam", n, "fósforos!")
                    if jogada==3:
                        n=n-2
                        print("A jogada do computador é retirar 2 fósforos.")
                        print("Restam", n, "fósforos!")    
                    if jogada==4:
                        n=n-1
                        print("A jogada do computador é retirar 1 fósforos.")
                        print("Restam", n, "fósforos!")
                if jogada<1 or jogada>4:
                    print("Erro!")
                
            print("Jogador perdeu!")  
    if ordem=="Não" or ordem=="não" or ordem=="n" or ordem=="N":
            jogada2=random.randint(1,4)
            n=n-jogada2
            print("A jogada do computador é retirar", jogada2, "fósforos.")
            print("Restam", n, "fósforos!")
            while n>1:
                jogada=int(input("Quantos fósforos quer tirar? 1, 2, 3, 4?"))
                if jogada>=1 and jogada<=4:    
                    n=n-jogada
                    print("Restam", n, "fósforos!")   
                    if n==1:
                        print("Jogador ganha!Parabéns!")
                    if n==2:
                        jogada2=1
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                        print("O Jogador perdeu!")
                    if n==3:
                        jogada2=2
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                        print("O Jogador perdeu!")
                    if n==4:
                        jogada2=3
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                        print("O Jogador perdeu!")
                    if n==5:
                        jogada2=4
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                        print("O Jogador perdeu!")
                    if n==6:
                        jogada2=random.randint(1,4)
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==7:
                        jogada2=1
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==8:
                        jogada2=2
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==9:
                        jogada2=3
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==10:
                        jogada2=4
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==11:
                        jogada2=random.randint(1,4)
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==12:
                        jogada2=1
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==13:
                        jogada2=2
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==14:
                        jogada2=3
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==15:
                        jogada2=4
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==16:
                        jogada2=random.randint(1,4)
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==17:
                        jogada2=1
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==18:
                        jogada2=2
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==19:
                        jogada2=3
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                    if n==20:
                        jogada2=4
                        n=n-jogada2
                        print("A jogada do computador é retirar", jogada2, "fósforos.")
                        print("Restam", n, "fósforos!")
                if jogada<1 or jogada>4:
                    print("Erro!")

                    
fosforos()