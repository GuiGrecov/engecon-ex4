# CÓDIGO - PARA CÁLCULO DO TIR

## 1. Introdução

Esse código utiliza um loop capaz de modificar o valor que aparece no Pk o qual calcula o VPL por meio da fórmula abaixo: (responsável por generalizar a fórmula do VPL) 

![image](https://github.com/GuiGrecov/engecon-ex4/assets/94385953/fb05f4bd-93b0-4301-b915-a2d31c162c0e)

Depois de fazermos isso para cada i (juros) que temos vamos ter um VPL diferente. Quando o VPL for igual a 0 nós encontramos o juros por trás da Taxa interna de Retorno! 

--------


## 2. Sobre o código 

O código funciona de uma forma simples: 

![image](https://github.com/GuiGrecov/engecon-ex4/assets/94385953/c05238c5-8a72-453d-b307-272c2e341df5)

Temos um loop que incremento i e gera um VPL, para esse código funcionar temos 35000 i diferentes para aumentarmos a precisão do algoritmo. 

## 3. Arquivo de entrada

![image](https://github.com/GuiGrecov/engecon-ex4/assets/94385953/6ddcf01a-e520-46f6-aa0e-7f7a1e92e0f3)

Precisamos somente enviar o "df.csv" arquivo de texto com as informaçõe de Fluxo de Caixa (Pk) em cada instante de tempo - nesse caso o tempo doe exercício foi medido por meio de anos. 

## 4. Arquivo de saída

![image](https://github.com/GuiGrecov/engecon-ex4/assets/94385953/87966af0-e5df-400b-b8ca-2cfd1bb60683)

O python me gera um arquivo com o juros x o valor de VPL. O código de Python faz isso 35000 vezes.

## 5. Diagrama do código: 

![image](https://github.com/GuiGrecov/engecon-ex4/assets/94385953/7e757af7-9bf0-4df4-82ec-2922607c3341)

-------

**Links:** 

* Código Python: https://github.com/GuiGrecov/engecon-ex4/blob/main/engecon-code4.py
* Input (arquivo de entrada): https://github.com/GuiGrecov/engecon-ex4/blob/main/df.csv
* Arquivo final (output): https://github.com/GuiGrecov/engecon-ex4/blob/main/arquivofinal1.csv

