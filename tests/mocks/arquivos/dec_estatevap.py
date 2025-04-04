MockDecEstatEvap = [
    "***********************************************************************\n",
    "*                                                                     *\n",
    "*            CEPEL - CENTRO DE PESQUISAS DE ENERGIA ELETRICA          *\n",
    "*  CEPEL: DECOMP     - Versao 32.1 - Ago/2024(L)                      *\n",
    "*                                                                     *\n",
    "***********************************************************************\n",
    "\n",
    "\n",
    "   PROGRAMA LICENCIADO PARA OPERADOR NACIONAL DO SISTEMA ELETRICO ONS                                                                                                             \n",
    "\n",
    "\n",
    "____________________________________________________________________\n",
    "\n",
    " PMO - JANEIRO/25 - FEVEREIRO/25 - REV 0 - FCF COM CVAR - 12 REE - VALOR ESPE    \n",
    "____________________________________________________________________\n",
    "\n",
    "-----------------------------------------------------\n",
    "Estatísticas de evaporacao das usinas hidroeletricas                           \n",
    "-----------------------------------------------------\n",
    "----------------------------------------------------------------------------------------\n",
    "IPER;         Indice do periodo                                                                                                                                                                         \n",
    "Num Usinas;   Numero de usinas considerando evaporacao                                                                                                                                                  \n",
    "Num UsiTot;   Numero total de usinas do periodo                                                                                                                                                         \n",
    "Evap. Modelo; Evaporao total das usinas no periodo calculada pelo modelo (hm3).                                                                                                                       \n",
    "Evap. Calc.;  Evaporacao total no periodo caculada pelos polinomios (hm3).                                                                                                                              \n",
    "Desvio Pos.;  Valor absoluto dos desvios positivos: |Evap. Calc.| > |Evap.Modelo| (hm3)                                                                                                                 \n",
    "Desvio Neg.;  Valor absoluto dos desvios negativos: |Evap. Calc.| < |Evap.Modelo| (hm3)                                                                                                                 \n",
    "Desvio Abs.;  Desvio absoluto entre o valor exato e o obtido pelo modelo (hm3)                                                                                                                          \n",
    "Evap. Modelo; Evaporao total das usinas no periodo calculada pelo modelo (m3/s).                                                                                                                      \n",
    "Evap. Calc.;  Evaporacao total no periodo caculada pelos polinomios (m3/s).                                                                                                                             \n",
    "Desvio Pos.;  Valor absoluto dos desvios positivos: |Evap. Calc.| > |Evap.Modelo| (m3/s)                                                                                                                \n",
    "Desvio Neg.;  Valor absoluto dos desvios negativos: |Evap. Calc.| < |Evap.Modelo| (m3/s)                                                                                                                \n",
    "Desvio Abs.;  Desvio absoluto entre o valor exato e o obtido pelo modelo (m3/s)                                                                                                                         \n",
    "Desvio;       Desvio percentual entre o valor exato e o obtido pelo modelo (%)                                                                                                                          \n",
    "----------------------------------------------------------------------------------------\n",
    "\n",
    "@Tabela\n",
    "-----;----------;----------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;-----------;\n",
    "IPER ;Num Usinas;Num UsiTot;Evap. Modelo;Evap. Calc. ;Desvio Pos. ;Desvio Neg. ;Desvio Abs. ;Evap. Modelo;Evap. Calc. ;Desvio Pos. ;Desvio Neg. ;Desvio Abs. ;  Desvio   ;\n",
    "  -  ;    -     ;    -     ;   (hm3)    ;   (hm3)    ;   (hm3)    ;   (hm3)    ;   (hm3)    ;   (m3/s)   ;   (m3/s)   ;   (m3/s)   ;   (m3/s)   ;   (m3/s)   ;    (%)    ;\n",
    "-----;----------;----------;------------;------------;------------;------------;------------;------------;------------;------------;------------;------------;-----------;\n",
    "   1 ;    167   ;    167   ;    260.150 ;    260.145 ;      0.003 ;      0.008 ;      0.010 ;    430.143 ;    430.134 ;      0.004 ;      0.013 ;      0.017 ;       0.00;\n",
    "   2 ;    167   ;    167   ;    264.589 ;    263.072 ;      0.107 ;      1.624 ;      1.731 ;    437.482 ;    434.974 ;      0.177 ;      2.685 ;      2.862 ;       0.66;\n",
    "   3 ;    167   ;    167   ;    271.080 ;    267.127 ;      0.171 ;      4.124 ;      4.295 ;    448.214 ;    441.678 ;      0.283 ;      6.819 ;      7.102 ;       1.61;\n",
    "   4 ;    167   ;    167   ;    280.369 ;    271.911 ;      0.117 ;      8.575 ;      8.692 ;    463.573 ;    449.588 ;      0.194 ;     14.179 ;     14.372 ;       3.20;\n",
    "   5 ;    167   ;    167   ;    291.284 ;    277.381 ;      0.164 ;     14.067 ;     14.231 ;    481.620 ;    458.632 ;      0.271 ;     23.259 ;     23.531 ;       5.13;\n",
    "   6 ;    167   ;    167   ;    888.929 ;    881.827 ;      1.367 ;      8.469 ;      9.836 ;    367.448 ;    364.512 ;      0.565 ;      3.501 ;      4.066 ;       1.12;\n",
    "   0 ;    167   ;    167   ;    376.067 ;    370.244 ;      0.322 ;      6.144 ;      6.466 ;    438.080 ;    429.920 ;      0.249 ;      8.409 ;      8.658 ;       1.95;\n",
]
