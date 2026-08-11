MockRenovaveis = [
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n",
    "& Cadastro dos parques eolicos equivalentes\n",
    "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n",
    " PEE-CAD;        1;Eolica SECO\n",
    " PEE-CAD;        2;Eolica S\n",
    " PEE-CAD;        3;Eolica NE\n",
    " PEE-CAD;        4;Eolica N\n",
    " PEE-CAD;        11;Fotovoltaica SECO\n",
    " PEE-CAD;        12;Fotovoltaica S\n",
    " PEE-CAD;        13;Fotovoltaica NE\n",
    " PEE-CAD;        14;Fotovoltaica N\n",
    " PEE-SUBM;        1;       1\n",
    " PEE-SUBM;        2;       2\n",
    " PEE-SUBM;        3;       3\n",
    " PEE-SUBM;        4;       4\n",
    " PEE-SUBM;       11;       1\n",
    " PEE-SUBM;       12;       2\n",
    " PEE-SUBM;       13;       3\n",
    " PEE-SUBM;       14;       4\n",
    " PEE-CONFIG-PER;        1;      1;      3;centralizado\n",
    " PEE-CONFIG-PER;        2;      1;      3;centralizado\n",
    " PEE-CONFIG-PER;        3;      1;      3;centralizado\n",
    " PEE-CONFIG-PER;        4;      1;      3;centralizado\n",
    " PEE-CONFIG-PER;       11;      1;      3;centralizado\n",
    " PEE-CONFIG-PER;       12;      1;      3;centralizado\n",
    " PEE-CONFIG-PER;       13;      1;      3;centralizado\n",
    " PEE-CONFIG-PER;       14;      1;      3;centralizado\n",
    " PEE-POT-INST-PER;        1;      1;      3;          99999\n",
    " PEE-POT-INST-PER;        2;      1;      3;          99999\n",
    " PEE-POT-INST-PER;        3;      1;      3;          99999\n",
    " PEE-POT-INST-PER;        4;      1;      3;          99999\n",
    " PEE-POT-INST-PER;       11;      1;      3;          99999\n",
    " PEE-POT-INST-PER;       12;      1;      3;          99999\n",
    " PEE-POT-INST-PER;       13;      1;      3;          99999\n",
    " PEE-POT-INST-PER;       14;      1;      3;          99999\n",
    "PEE-GER-PER-PAT-CEN;1;1;1;1;81.0966\n",
    "PEE-GER-PER-PAT-CEN;1;1;2;1;87.6335\n",
    "PEE-GER-PER-PAT-CEN;1;1;3;1;134.5896\n",
    "PEE-GER-PER-PAT-CEN;1;2;1;1;102.0333\n",
    "PEE-GER-PER-PAT-CEN;14;3;2;353;1.627114\n",
    "PEE-GER-PER-PAT-CEN;14;3;3;353;1.611293\n",
]

MockPEECadastro = " PEE-CAD;        1;Eolica SECO"

MockPEESubmercado = " PEE-SUBM;        1;       1"

MockPEEConfiguracaoPeriodo = (
    " PEE-CONFIG-PER;        1;      1;      3;centralizado"
)

MockPEEPotenciaInstaladaPeriodo = (
    " PEE-POT-INST-PER;        1;      1;      3;          99999"
)

MockPEEGeracaoPeriodoPatamarCenario = "PEE-GER-PER-PAT-CEN;1;1;1;1;81.0966"

MockPEEGeracaoPeriodoPatamarCenarioComPeriodoFinal = (
    "PEE-GER-PER-PAT-CEN;1;1;1;1;1;7.7428"
)

# Variante do arquivo com o layout de 6 campos do card
# PEE-GER-PER-PAT-CEN (intervalo de períodos, com PerFin).
MockRenovaveisPeriodoFinal = [
    "&                   ;CodPEE   ;PerIni ;PerFin ;Pat   ;Cen;GerEolica\n",
    "PEE-GER-PER-PAT-CEN;1;1;1;1;1;7.7428\n",
    "PEE-GER-PER-PAT-CEN;1;1;1;2;1;5.7284\n",
    "PEE-GER-PER-PAT-CEN;1;1;1;3;1;4.387\n",
    "PEE-GER-PER-PAT-CEN;1;2;2;1;1;7.7428\n",
    "PEE-GER-PER-PAT-CEN;14;3;3;2;353;1.627114\n",
    "PEE-GER-PER-PAT-CEN;14;3;3;3;353;1.611293\n",
]
