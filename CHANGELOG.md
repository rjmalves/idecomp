# v1.1.1

- Fix na leitura do arquivo `vazoes.rvX` quando gerado por versões antigas do GEVAZP, onde o número de postos não fazia parte dos dados do arquivo.


# v1.1.0

- Atualizada a modelagem dos registros do dadger sensíveis ao número de estágios para o máximo suportado pelo modelo (TI, VE).
- Atualizada a modelagem com propriedades para registros do dadger de manutenção e disponibilidade (MP, MT, FD).
- Atualizada na classe `Dadger` as propriedades para acesso aos registros atualizados (MP, MT, FD).


# v1.0.1

- Fix nas colunas o DataFrame de Volume Útil de Reservatórios do arquivo Relato


# v1.0.0

- Primeira major release
- Suporte à leitura e escrita todos os arquivos de entrada utilizados oficialmente no modelo DECOMP
- Suporte aos registros utilizados pelo polinômio de jusante em LIBS
- Adicionados registros VL, VA e VU ao dadger
- Registros do dadger com número de campos variáveis por patamar agora suportam o máximo do modelo DECOMP (5)
- Métodos le_arquivo e escreve_arquivo deprecados
