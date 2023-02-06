MockDecAvlEvap = [
    "***********************************************************************\n",
    "*                                                                     *\n",
    "*            CEPEL - CENTRO DE PESQUISAS DE ENERGIA ELETRICA          *\n",
    "*  CEPEL: DECOMP     - Versao 31.14 - Dez/2022(L)                     *\n",
    "*                                                                     *\n",
    "***********************************************************************\n",
    "\n",
    "\n",
    "   PROGRAMA LICENCIADO PARA OPERADOR NACIONAL DO SISTEMA ELETRICO ONS                                                                                                             \n",
    "\n",
    "\n",
    "____________________________________________________________________\n",
    "\n",
    " Backtest Preliminar CPAMP 2022-2023 - Hibrido DECOMP 01/2020 rv4                \n",
    "____________________________________________________________________\n",
    "\n",
    "------------------------------------------------------------\n",
    "Avaliacao dos desvios da Representacao linear da evaporacao.                    \n",
    "------------------------------------------------------------\n",
    "------------------------------------------------------------------------------\n",
    "IPER;         Indice do periodo                                                                                                                                                                         \n",
    "USIH;         Numero de cadastro da usina hidroeletrica                                                                                                                                                 \n",
    "NomeUsih;     Nome de cadastro da usina hidroeletrica                                                                                                                                                   \n",
    "Sist;         Numero do subsistema                                                                                                                                                                      \n",
    "REE;          Numero de cadastro do reservatorio equivalente                                                                                                                                            \n",
    "Varm;         Volume Armazenado Total                                                                                                                                                                   \n",
    "Evap. Calc.;  Evaporacao caculada pelos polinomios AreaXCota e CotaXVolume                                                                                                                              \n",
    "Evap. Modelo; Evaporacao calculada pelo modelo linear construido pelo Decomp                                                                                                                            \n",
    "Desvio Abs.;  Desvio absoluto entre o valor exato e o obtido pelo modelo (hm3)                                                                                                                          \n",
    "Desvio;       Desvio percentual entre o valor exato e o obtido pelo modelo (%)                                                                                                                          \n",
    "------------------------------------------------------------------------------\n",
    "\n",
    "@Tabela\n",
    "-----;-----;--------------;----;-----;----------;----------;----------;------------;-----------;\n",
    "IPER ;USIH ;   NomeUsih   ;Sist; REE ;   Varm   ;Evap. Calc;Evap. Mode;Desvio Abs. ;  Desvio   ;\n",
    "  -  ;  -  ;      -       ; -  ;  -  ;  (hm3)   ;  (hm3)   ;  (hm3)   ;   (hm3)    ;    (%)    ;\n",
    "-----;-----;--------------;----;-----;----------;----------;----------;------------;-----------;\n",
    "   1 ; 001 ; CAMARGOS     ;  1 ; 010 ;   120.00 ;     0.00 ;     0.00 ;      0.000 ;       0.00;\n",
    "   1 ; 001 ; CAMARGOS     ;  1 ; 010 ;   254.40 ;     0.00 ;     0.00 ;      0.000 ;       0.00;\n",
    "   1 ; 001 ; CAMARGOS     ;  1 ; 010 ;   388.80 ;     0.00 ;     0.00 ;      0.000 ;       0.00;\n",
    "   1 ; 001 ; CAMARGOS     ;  1 ; 010 ;   523.20 ;     0.00 ;     0.00 ;      0.000 ;       0.00;\n",
    "   1 ; 001 ; CAMARGOS     ;  1 ; 010 ;   657.60 ;     0.00 ;     0.00 ;      0.000 ;       0.00;\n",
    "   1 ; 002 ; ITUTINGA     ;  1 ; 010 ;    10.66 ;     0.00 ;     0.00 ;      0.000 ;       0.00;\n",
    "   1 ; 004 ; FUNIL-GRANDE ;  1 ; 010 ;   265.86 ;     0.05 ;     0.05 ;      0.000 ;       0.00;\n",
    "   1 ; 006 ; FURNAS       ;  1 ; 010 ;  5733.00 ;     1.58 ;     1.64 ;      0.052 ;       3.29;\n",
    "   1 ; 006 ; FURNAS       ;  1 ; 010 ;  9176.40 ;     2.28 ;     2.29 ;      0.001 ;       0.05;\n",
    "   1 ; 006 ; FURNAS       ;  1 ; 010 ; 12619.80 ;     2.87 ;     2.93 ;      0.067 ;       2.33;\n",
    "   1 ; 006 ; FURNAS       ;  1 ; 010 ; 16063.20 ;     3.39 ;     3.58 ;      0.198 ;       5.84;\n",
    "   1 ; 006 ; FURNAS       ;  1 ; 010 ; 19506.60 ;     3.87 ;     4.23 ;      0.361 ;       9.32;\n",
    "   1 ; 007 ; M. DE MORAES ;  1 ; 010 ;  1540.00 ;     0.40 ;     0.39 ;     -0.005 ;      -1.20;\n",
    "   1 ; 007 ; M. DE MORAES ;  1 ; 010 ;  2040.00 ;     0.46 ;     0.46 ;     -0.001 ;      -0.12;\n",
    "   1 ; 007 ; M. DE MORAES ;  1 ; 010 ;  2540.00 ;     0.53 ;     0.53 ;      0.000 ;       0.01;\n",
    "   1 ; 007 ; M. DE MORAES ;  1 ; 010 ;  3040.00 ;     0.60 ;     0.60 ;      0.000 ;       0.02;\n",
    "   1 ; 007 ; M. DE MORAES ;  1 ; 010 ;  3540.00 ;     0.66 ;     0.67 ;      0.002 ;       0.25;\n",
    "   1 ; 008 ; ESTREITO     ;  1 ; 010 ;  1329.60 ;     0.11 ;     0.11 ;      0.000 ;       0.00;\n",
    "   1 ; 009 ; JAGUARA      ;  1 ; 010 ;   415.80 ;     0.06 ;     0.06 ;      0.000 ;       0.00;\n",
    "   1 ; 010 ; IGARAPAVA    ;  1 ; 010 ;   235.19 ;     0.10 ;     0.10 ;      0.000 ;       0.00;\n",
    "   1 ; 011 ; VOLTA GRANDE ;  1 ; 010 ;  2137.00 ;     0.42 ;     0.42 ;      0.000 ;       0.00;\n",
    "   1 ; 012 ; P. COLOMBIA  ;  1 ; 010 ;  1418.06 ;     0.30 ;     0.30 ;      0.000 ;       0.00;\n",
    "   1 ; 014 ; CACONDE      ;  1 ; 010 ;    51.00 ;     0.03 ;     0.03 ;      0.009 ;      32.71;\n",
    "   1 ; 014 ; CACONDE      ;  1 ; 010 ;   151.80 ;     0.05 ;     0.06 ;      0.004 ;       7.99;\n",
    "   1 ; 014 ; CACONDE      ;  1 ; 010 ;   252.60 ;     0.08 ;     0.08 ;      0.000 ;       0.21;\n",
    "   1 ; 014 ; CACONDE      ;  1 ; 010 ;   353.40 ;     0.10 ;     0.10 ;      0.001 ;       0.62;\n",
    "   1 ; 014 ; CACONDE      ;  1 ; 010 ;   454.20 ;     0.11 ;     0.12 ;      0.003 ;       2.48;\n",
    "   1 ; 015 ; E. DA CUNHA  ;  1 ; 010 ;    12.82 ;     0.01 ;     0.01 ;      0.000 ;       0.00;\n",
    "   1 ; 016 ; A.S.OLIVEIRA ;  1 ; 010 ;    22.69 ;     0.01 ;     0.01 ;      0.000 ;       0.00;\n",
    "   1 ; 017 ; MARIMBONDO   ;  1 ; 010 ;   890.00 ;     0.33 ;     0.36 ;      0.032 ;       9.71;\n",
    "   1 ; 017 ; MARIMBONDO   ;  1 ; 010 ;  1942.00 ;     0.56 ;     0.56 ;      0.005 ;       0.93;\n",
    "   1 ; 017 ; MARIMBONDO   ;  1 ; 010 ;  2994.00 ;     0.76 ;     0.76 ;      0.004 ;       0.53;\n",
    "   1 ; 017 ; MARIMBONDO   ;  1 ; 010 ;  4046.00 ;     0.92 ;     0.96 ;      0.034 ;       3.64;\n",
    "   1 ; 017 ; MARIMBONDO   ;  1 ; 010 ;  5098.00 ;     1.08 ;     1.16 ;      0.080 ;       7.48;\n",
    "   1 ; 018 ; A. VERMELHA  ;  1 ; 010 ;  5856.00 ;     1.10 ;     1.11 ;      0.008 ;       0.76;\n",
    "   1 ; 018 ; A. VERMELHA  ;  1 ; 010 ;  6889.80 ;     1.25 ;     1.25 ;      0.003 ;       0.20;\n",
    "   1 ; 018 ; A. VERMELHA  ;  1 ; 010 ;  7923.60 ;     1.38 ;     1.38 ;      0.000 ;       0.00;\n",
    "   1 ; 018 ; A. VERMELHA  ;  1 ; 010 ;  8957.40 ;     1.52 ;     1.52 ;      0.002 ;       0.13;\n",
    "   1 ; 018 ; A. VERMELHA  ;  1 ; 010 ;  9991.20 ;     1.65 ;     1.66 ;      0.008 ;       0.48;\n",
    "   1 ; 020 ; BATALHA      ;  1 ; 010 ;   430.05 ;     0.00 ;     0.00 ;      0.000 ;       0.00;\n",
    "   1 ; 020 ; BATALHA      ;  1 ; 010 ;   700.36 ;     0.00 ;     0.00 ;      0.000 ;       0.00;\n",
    "   1 ; 020 ; BATALHA      ;  1 ; 010 ;   970.67 ;     0.00 ;     0.00 ;      0.000 ;       0.00;\n",
    "   1 ; 020 ; BATALHA      ;  1 ; 010 ;  1240.99 ;     0.00 ;     0.00 ;      0.000 ;       0.00;\n",
    "   1 ; 020 ; BATALHA      ;  1 ; 010 ;  1511.30 ;     0.00 ;     0.00 ;      0.000 ;       0.00;\n",
    "   1 ; 021 ; SERRA FACAO  ;  1 ; 010 ;  1752.00 ;     0.12 ;     0.13 ;      0.009 ;       7.39;\n",
    "   1 ; 021 ; SERRA FACAO  ;  1 ; 010 ;  2441.40 ;     0.17 ;     0.17 ;      0.000 ;       0.01;\n",
    "   1 ; 021 ; SERRA FACAO  ;  1 ; 010 ;  3130.80 ;     0.20 ;     0.21 ;      0.004 ;       1.78;\n",
    "   1 ; 021 ; SERRA FACAO  ;  1 ; 010 ;  3820.20 ;     0.23 ;     0.24 ;      0.010 ;       4.31;\n",
    "   1 ; 021 ; SERRA FACAO  ;  1 ; 010 ;  4509.60 ;     0.26 ;     0.28 ;      0.015 ;       5.78;\n",
    "   1 ; 024 ; EMBORCACAO   ;  1 ; 010 ;  4669.00 ;     0.00 ;     0.00 ;      0.000 ;       0.00;\n",
    "   1 ; 024 ; EMBORCACAO   ;  1 ; 010 ;  7280.20 ;     0.00 ;     0.00 ;      0.000 ;       0.00;\n",
    "   1 ; 024 ; EMBORCACAO   ;  1 ; 010 ;  9891.40 ;     0.00 ;     0.00 ;      0.000 ;       0.00;\n",
    "   1 ; 024 ; EMBORCACAO   ;  1 ; 010 ; 12502.60 ;     0.00 ;     0.00 ;      0.000 ;       0.00;\n",
    "   1 ; 024 ; EMBORCACAO   ;  1 ; 010 ; 15113.80 ;     0.00 ;     0.00 ;      0.000 ;       0.00;\n",
    "   1 ; 025 ; NOVA PONTE   ;  1 ; 010 ;  2412.00 ;     0.46 ;     0.49 ;      0.031 ;       6.66;\n",
    "   1 ; 025 ; NOVA PONTE   ;  1 ; 010 ;  4488.00 ;     0.75 ;     0.75 ;      0.000 ;       0.01;\n",
    "   1 ; 025 ; NOVA PONTE   ;  1 ; 010 ;  6564.00 ;     0.98 ;     1.00 ;      0.022 ;       2.21;\n",
    "   1 ; 025 ; NOVA PONTE   ;  1 ; 010 ;  8640.00 ;     1.20 ;     1.26 ;      0.062 ;       5.14;\n",
    "   1 ; 025 ; NOVA PONTE   ;  1 ; 010 ; 10716.00 ;     1.42 ;     1.52 ;      0.102 ;       7.17;\n",
    "   1 ; 026 ; MIRANDA      ;  1 ; 010 ;   974.00 ;     0.07 ;     0.07 ;     -0.002 ;      -2.22;\n",
    "   1 ; 026 ; MIRANDA      ;  1 ; 010 ;  1003.20 ;     0.08 ;     0.07 ;     -0.001 ;      -0.97;\n",
    "   1 ; 026 ; MIRANDA      ;  1 ; 010 ;  1032.40 ;     0.08 ;     0.08 ;      0.000 ;      -0.24;\n",
    "   1 ; 026 ; MIRANDA      ;  1 ; 010 ;  1061.60 ;     0.08 ;     0.08 ;      0.000 ;       0.00;\n",
    "   1 ; 026 ; MIRANDA      ;  1 ; 010 ;  1090.80 ;     0.08 ;     0.08 ;      0.000 ;      -0.18;\n",
    "\n",
]