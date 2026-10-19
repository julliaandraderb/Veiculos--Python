# Sistema de Veículos — Herança e Polimorfismo

Projeto desenvolvido em **Python** para praticar conceitos de **Programação Orientada a Objetos (POO)**, utilizando classes, herança e sobrescrita de métodos.

## Objetivo

Criar um sistema simples que represente diferentes tipos de veículos, permitindo que carros e motos tenham características próprias e comportamentos específicos.

## Conceitos utilizados

- Classes e objetos
- Construtores (`__init__`)
- Atributos e métodos
- Herança
- `super()`
- Sobrescrita de métodos
- Polimorfismo

## Classes

- **Veiculo:** classe principal que contém os atributos `marca` e `modelo` e o método `ligar()`.
- **Carro:** herda de `Veiculo` e possui o atributo adicional `num_portas`.
- **Moto:** herda de `Veiculo` e possui o atributo adicional `cilindradas`.

## Funcionalidades

- Criar objetos de carros e motos.
- Armazenar marca e modelo dos veículos.
- Informar o número de portas de um carro.
- Informar as cilindradas de uma moto.
- Exibir mensagens diferentes ao ligar cada tipo de veículo.

## Tecnologias

- Python
- Visual Studio Code

---

Desenvolvido por **Júllia Andrade**, durante o curso de **Desenvolvimento de Sistemas**.
