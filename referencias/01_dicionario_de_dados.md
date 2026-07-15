# Dicionário de dados

Base retirada do site do [governo
canadense](https://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64).

Detalhes sobre as terminologias estão disponíveis
[aqui](https://natural-resources.canada.ca/energy-efficiency/transportation-alternative-fuels/personal-vehicles/choosing-right-vehicle/buying-electric-vehicle/understanding-the-tables/21383)
e resumidos a seguir.

Os conjuntos de dados fornecem classificações de consumo de combustível específicas do
modelo e emissões estimadas de dióxido de carbono para novos veículos leves para venda
no varejo no Canadá.

| Nome da coluna         | Descrição                                                                                  | Tipo de dado |
|------------------------|--------------------------------------------------------------------------------------------|--------------|
| `Model year`           | Ano do modelo                                                                              | Numérico     |
| `Make`                 | Fabricante                                                                                 | Categórico   |
| `Model`                | Modelo (ver abaixo)                                                                        | Categórico   |
| `Vehicle class`        | Classe do veículo (ver abaixo)                                                             | Categórico   |
| `Engine size (L)`      | Tamanho do motor em litros                                                                 | Numérico     |
| `Cylinders`            | Número de cilindros                                                                        | Numérico     |
| `Transmission`         | Tipo de transmissão (ver abaixo)                                                           | Categórico   |
| `Fuel type`            | Tipo de combustível (ver abaixo)                                                           | Categórico   |
| `City (L/100km)`       | Consumo de combustível em L/100 km em perímetro urbano                                     | Numérico     |
| `Highway (L/100km)`    | Consumo de combustível em L/100 km em estradas                                             | Numérico     |
| `Combined (L/100km)`   | Consumo de combustível em L/100 km considerando 55% em perímetro urbano e 45 % em estradas | Numérico     |
| `Combined (mpg)`       | Consumo combinado em milhas por galão                                                      | Numérico     |
| `CO2 emissions (g/km)` | Emissão de CO2 em g/km de percurso combinado                                               | Numérico     |
| `CO2 rating`           | Escala de emissão de CO2                                                                   | Categórico   |
| `Smog rating`          | Escala de emissão de poluentes smog                                                        | Categórico   |

## Detalhes para a coluna `Model`

- AWD = Tração nas quatro rodas - veículo projetado para operar com todas as rodas acionadas
- 4WD / 4X4 = Tração nas quatro rodas - veículo projetado para operar com duas ou quatro rodas acionadas
- FFV = Veículo flexível a combustível - veículo projetado para operar com gasolina e misturas de etanol de até 85% de etanol (E85)
- CNG = Gás natural comprimido; NGV = Veículo a gás natural
- SWB = Distância entre eixos curta; LWB = Distância entre eixos longa; EWB = Distância entre eixos estendida; # = Motor de alta potência

## Detalhes para a coluna `Vehicle class`

Considerando carros:


| Classe do veículo                   | Volume interno |
|-------------------------------------|-----------------|
| Dois lugares (T)                    | n/a             |
| Minicompacto (I)                    | Menos de 2.405 L (85 cu. ft.) |
| Subcompacto (S)                     | 2.405–2.830 L (85–99 cu. ft.) |
| Compacto (C)                        | 2.830–3.115 L (100–109 cu. ft.) |
| Médio (M)                           | 3.115–3.400 L (110–119 cu. ft.) |
| Grande (L)                          | 3.400 L (120 cu. ft.) ou mais |
| Perua (station wagon): Pequena (WS) | Menos de 3.680 L (130 cu. ft.) |
| Perua (station wagon): Média (WM)   | 3.680–4.530 L (130–159 cu. ft.) |

Onde L = litros e cu. ft. = pés cúbicos.

Considerando caminhonetes, caminhões e vans:

| Classe do veículo                    | Peso bruto do veículo |
|--------------------------------------|-----------------|
| Caminhonetes - Pequena (PS)          | Menos de 2.722 kg (6.000 lb) |
| Caminhonetes - Padrão (PL)           | 2.722–3.856 kg (6.000–8.500 lb) |
| Utilitário esportivo - Pequeno (US)  | Menos de 2.722 kg (6.000 lb) |
| Utilitário esportivo - Padrão (UL)   | 2.722–4.536 kg (6.000–9.999 lb) |
| Minivan (V)                          | Menos de 3.856 kg (8.500 lb) |
| Van - Carga (VC)                     | Menos de 3.856 kg (8.500 lb) |
| Van - Passageiros (VP)               | Menos de 4.536 kg (10.000 lb) |
| Veículo de uso especial (SP)         | Menos de 3.856 kg (8.500 lb) |

Onde kg = quilogramas e lb = libras.

## Detalhes para a coluna `Transmission`

- A = Automático
- AM = Manual automatizado
- AS = Automático com troca seletiva
- AV = Variável contínua
- M = Manual
- Número de marchas/velocidades (1–10)

## Detalhes para a coluna `Fuel type`

- X = Gasolina comum
- Z = Gasolina premium
- D = Diesel
- E = E85 (mistura de etanol e gasolina com até 85% de etanol)
- B = Eletricidade
- N = Gás natural
