# Programa-para-calcular-juros-e-atraso-nos-pagamentos-
# Calculadora de Multa por Atraso

## Descrição
Esta é uma aplicação de desktop simples desenvolvida em Python usando a biblioteca Tkinter. Ela calcula o valor total a ser pago em uma parcela atrasada, incluindo multas e taxas adicionais.

## Funcionalidades
- Calcula o valor total a ser pago com base no valor da parcela, data de vencimento e data de pagamento.
- Inclui cálculos de multa por atraso, multa por dias de atraso e taxa de reemissão de boleto.
- Interface gráfica amigável e fácil de usar.
- Formatação automática das datas durante a digitação.

## Requisitos
- Python 3.x
- Tkinter (geralmente vem pré-instalado com Python)

## Como usar
1. Execute o script Python `teste4.py`.
2. Insira o valor da parcela.
3. Digite a data de vencimento no formato dd/mm/aaaa.
4. Digite a data de pagamento no formato dd/mm/aaaa.
5. Clique no botão "Calcular".
6. O resultado será exibido na tela, mostrando um resumo detalhado do pagamento.

## Detalhes do cálculo
- Multa por atraso: 2% do valor da parcela
- Multa por dias de atraso: (Multa por atraso / 30) * número de dias de atraso
- Taxa de reemissão de boleto: R$ 2,88 (valor fixo)

## Autor
Desenvolvido por Vitão

