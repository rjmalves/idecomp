MockREHorizPer = "RE-HORIZ-PER;    701;      1;      6\n"
MockREHorizData = "RE-HORIZ-DATA;    701;      2021/01/01;      2022/02/01\n"
MockRE = "RE;702;re(405) + contante_aditiva\n"
MockREPerPat = (
    "RE-PER-PAT;702;      1;     NA;      ; re(405) + contante_aditiva \n"
)
MockREDataPat = "RE-DATA-PAT;702;2021/01/01;;; re(405) + contante_aditiva \n"
MockRELimFormPerPat = "RE-LIM-FOR-PER-PAT;    701;      1;     6 ;     1;               ;        4100       \n"
MockRELimFormDataPat = (
    "RE-LIM-FOR-PER-PAT;    701;2021/01/01; ;     1; ;4100       \n"
)
MockAliasElet = "ALIAS-ELET ;  1 ; constante_aditiva\n"
MockAliasEletValPerPat = (
    "ALIAS-ELET-VAL-PER-PAT;       1 ;    1 ;      ; 1; 1000\n"
)
MockRERegraAtiva = (
    "RE-REGRA-ATIVA; 62; 53000 < demanda_sin & demanda_sin <= 63000\n"
)
MockREHabilita = "RE-HABILITA; 703; 61\n"
MockRETratViol = "RE-TRAT-VIOL;     701;hard        ;            1.0"
MockRETratViolPer = (
    "RE-TRAT-VIOL-PER;  701;      1;      6;        hard;        1000.0"
)

MockRestricaoEletrica = [
    "&**************************************************\n",
    "& Descrição colunas:\n",
    "&**************************************************\n",
    "& CodRe: Código da restrição elétrica\n",
    "& Formula: Fórmula que define a restrição elétrica\n",
    "&************************************************** \n",
    "&              ;Cod ; Nome do alias\n",
    "ALIAS-ELET ;  1 ; constante_aditiva\n",
    "ALIAS-ELET ;  2 ; constante_multiplicativa\n",
    "ALIAS-ELET ;  3 ; constante_limite\n",
    "&                                   ; CodAlias;perIni;perFin;Pat;Valor(MW)\n",
    "ALIAS-ELET-VAL-PER-PAT;       1 ;    1 ;      ; NA; 1000\n",
    "ALIAS-ELET-VAL-PER-PAT;       2 ;    2 ;    NA;   ;   10\n",
    "ALIAS-ELET-VAL-PER-PAT;       3 ;    1 ;      ; 1 ; 1061\n",
    "ALIAS-ELET-VAL-PER-PAT;       3 ;    1 ;      ; 2 ; 1065\n",
    "ALIAS-ELET-VAL-PER-PAT;       3 ;    1 ;      ; 3 ; 1048\n",
    "ALIAS-ELET-VAL-PER-PAT;       3 ;    6 ;      ; 1 ;  914\n",
    "ALIAS-ELET-VAL-PER-PAT;       3 ;    6 ;      ; 2 ;  905  \n",
    "ALIAS-ELET-VAL-PER-PAT;       3 ;    6 ;      ; 3 ;  882\n",
    "&\n",
    "&\n",
    "&******************************************;*******;*******;*******;******;************************************************************************************************************************\n",
    "&                                          ;CodRe  ;PerIni ;PerFin ;Pat   ;Formula\n",
    "&-                                         ;       ;       ;       ;      ;\n",
    "&SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS;IIIIIII;IIIIIII;IIIIIII;IIIIII;SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS\n",
    "RE-PER-PAT;     701;      1;       ;    NA; re(405) \n",
    "RE-PER-PAT;     702;      1;     NA;      ; re(405) + contante_aditiva \n",
    "RE-PER-PAT;     703;      1;       ;    NA; re(405) * constante_multiplicativa\n",
    "RE-PER-PAT;     704;      1;       ;      ; re(405) + 0.31*ger_conjh(66,1)\n",
    "RE-PER-PAT;     705;      1;       ;      ; re(405) + 0.46*ger_conjh(66,1)\n",
    "RE-PER-PAT;     706;      1;     NA;      ; re(405) + 0.59*ger_conjh(66,1)\n",
    "RE-PER-PAT;     707;      1;     NA;    NA; re(405) + 0.30*ger_conjh(66,1)                                                                                         \n",
    "&\n",
    "&**************************************************\n",
    "& Descrição colunas:\n",
    "&**************************************************\n",
    "& CodRe: Código da restrição elétrica\n",
    "& PerIni: Período inicial de validade do dado\n",
    "& PerFin: Período final de validade do dado\n",
    "&***********************************;*******;*******;*******;\n",
    "&                                   ;CodRe  ;PerIni ;PerFin ;\n",
    "&                                   ;       ;       ;       ;\n",
    "&***********************************;IIIIIII;IIIIIII;IIIIIII;\n",
    "RE-HORIZ-PER;    701;      1;      6\n",
    "RE-HORIZ-PER;    702;      1;      6\n",
    "RE-HORIZ-PER;    703;      1;      6\n",
    "RE-HORIZ-PER;    704;      1;      6\n",
    "RE-HORIZ-PER;    705;      1;      6\n",
    "RE-HORIZ-PER;    706;      1;      6\n",
    "RE-HORIZ-PER;    707;      1;      6\n",
    "&\n",
    "&**************************************************\n",
    "& Descrição colunas:\n",
    "&**************************************************\n",
    "& CodRe: Código da restrição elétrica\n",
    "& PerIni: Período inicial de validade do dado\n",
    "& PerFin: Período final de validade do dado\n",
    "& Pat: Índice do patamar de carga no período\n",
    "& LimInf: Limite inferior da restrição elétrica \n",
    "& LimSup: Limite superior da restrição elétrica\n",
    "&*************************************************;*******;*******;*******;******;***************;************;\n",
    "&                                                 ;CodRe  ;PerIni ;PerFin ;Pat   ;LimInf         ;LimSup      ;\n",
    "&                                                 ;       ;       ;       ;-     ;               ;            ;\n",
    "&*************************************************;IIIIIII;IIIIIII;IIIIIII;IIIIII;SSSSSSSSSSSSSSS;SSSSSSSSSSSS;\n",
    "RE-LIM-FORM-PER-PAT;    701;      1;     6 ;     1;               ;        4100       \n",
    "RE-LIM-FORM-PER-PAT;    702;      1;     6 ;     1;               ;        5365        \n",
    "RE-LIM-FORM-PER-PAT;    703;      1;     6 ;     1;               ;        6387        \n",
    "RE-LIM-FORM-PER-PAT;    704;      1;     6 ;     1;               ;        4887        \n",
    "RE-LIM-FORM-PER-PAT;    705;      1;     6 ;     1;               ;        6204        \n",
    "RE-LIM-FORM-PER-PAT;    706;      1;     6 ;     1;               ;        6971        \n",
    "RE-LIM-FORM-PER-PAT;    707;      1;     6 ;     1;               ;        5838   \n",
    "RE-LIM-FORM-PER-PAT;    701;      1;     6 ;     2;               ;        4100        \n",
    "RE-LIM-FORM-PER-PAT;    702;      1;     6 ;     2;               ;        5365        \n",
    "RE-LIM-FORM-PER-PAT;    703;      1;     6 ;     2;               ;        6387        \n",
    "RE-LIM-FORM-PER-PAT;    704;      1;     6 ;     2;               ;        4887        \n",
    "RE-LIM-FORM-PER-PAT;    705;      1;     6 ;     2;               ;        6204        \n",
    "RE-LIM-FORM-PER-PAT;    706;      1;     6 ;     2;               ;        6971        \n",
    "RE-LIM-FORM-PER-PAT;    707;      1;     6 ;     2;               ;        5838  \n",
    "RE-LIM-FORM-PER-PAT;    701;      1;     6 ;     3;               ;        4100        \n",
    "RE-LIM-FORM-PER-PAT;    702;      1;     6 ;     3;               ;        5365        \n",
    "RE-LIM-FORM-PER-PAT;    703;      1;     6 ;     3;               ;        6387        \n",
    "RE-LIM-FORM-PER-PAT;    704;      1;     6 ;     3;               ;        4887        \n",
    "RE-LIM-FORM-PER-PAT;    705;      1;     6 ;     3;               ;        6204        \n",
    "RE-LIM-FORM-PER-PAT;    706;      1;     6 ;     3;               ;        6971        \n",
    "RE-LIM-FORM-PER-PAT;    707;      1;     6 ;     3;               ;        5838     \n",
    "&\n",
    "&**************************************************\n",
    "& Descrição colunas:\n",
    "&************************************************** \n",
    "RE-REGRA-ATIVA; 61; 59000 > demanda_sin | demanda_sin > 76000\n",
    "RE-REGRA-ATIVA; 62; 53000 < demanda_sin & demanda_sin <= 63000\n",
    "RE-REGRA-ATIVA; 63; constante_teste < demanda_sin\n",
    "RE-REGRA-ATIVA; 64; 78000 < demanda_sin\n",
    "RE-REGRA-ATIVA; 65; peq_SUL_PCH_S <= constante_teste\n",
    "&**************************************************\n",
    "& Descrição colunas:\n",
    "&************************************************** \n",
    "RE-HABILITA; 701; 65\n",
    "RE-HABILITA; 702; 61\n",
    "RE-HABILITA; 703; 61\n",
    "RE-HABILITA; 704; 62\n",
    "RE-HABILITA; 705; 63\n",
    "RE-HABILITA; 706; 63\n",
    "RE-HABILITA; 707; 64\n",
    "&\n",
    "\n",
    "\n",
]

MockRestricoes = MockRestricaoEletrica
