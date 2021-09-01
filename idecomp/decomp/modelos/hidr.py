from io import BufferedReader
from typing import List

from idecomp._utils.registrosbinario import RegistroAnBinario
from idecomp._utils.registrosbinario import RegistroFnBinario
from idecomp._utils.registrosbinario import RegistroInBinario
from idecomp._utils.leiturabinario import LeituraBinario
from idecomp._utils.blocobinario import BlocoBinario


class BlocoBinarioHidr(BlocoBinario):
    def __init__(self):
        super().__init__()
        self._dados = []

    # Override
    def le(self, arq: BufferedReader):
        """
        """
        reg_nome = RegistroAnBinario(12)
        reg_posto = RegistroInBinario(32)
        reg_posto_bdh = RegistroInBinario(8)
        reg_subsistema = RegistroInBinario(32)
        reg_empresa = RegistroInBinario(32)
        reg_jusante = RegistroInBinario(32)
        reg_desvio = RegistroInBinario(32)
        reg_volume = RegistroFnBinario(32)
        reg_cota = RegistroFnBinario(32)
        reg_polinomio = RegistroFnBinario(32)
        reg_evaporacao = RegistroInBinario(32)
        reg_num_conjunto_maquinas = RegistroInBinario(32)
        reg_potencia = RegistroFnBinario(32)
        reg_ignorar = RegistroFnBinario(32)
        reg_h_nominal = RegistroFnBinario(32)
        reg_q_nominal = RegistroInBinario(32)
        reg_produt = RegistroFnBinario(32)
        reg_perdas = RegistroFnBinario(32)
        reg_numero_polinomios = RegistroInBinario(32)
        reg_canal_fuga = RegistroFnBinario(32)
        reg_influencia_vert = RegistroInBinario(32)
        reg_fator_carga = RegistroFnBinario(32)
        reg_vazao = RegistroFnBinario(32)
        reg_numero_unidades = RegistroInBinario(32)
        reg_tipo_turbina = RegistroInBinario(32)
        reg_repr_conjunto = RegistroInBinario(32)
        reg_taxa_indisp_f = RegistroFnBinario(32)
        reg_taxa_indisp_p = RegistroFnBinario(32)
        reg_tipo_perda = RegistroInBinario(32)
        reg_data = RegistroAnBinario(8)
        reg_obs = RegistroAnBinario(43)
        reg_vol_ref = RegistroFnBinario(32)
        reg_tipo_regul = RegistroAnBinario(1)

        # Realiza a leitura
        self._dados = [
                       reg_nome.le_registro(arq),
                       reg_posto.le_registro(arq),
                       *reg_posto_bdh.le_linha_tabela(arq, 8),
                       reg_subsistema.le_registro(arq),
                       reg_empresa.le_registro(arq),
                       reg_jusante.le_registro(arq),
                       reg_desvio.le_registro(arq),
                       reg_volume.le_registro(arq),
                       reg_volume.le_registro(arq),
                       reg_volume.le_registro(arq),
                       reg_volume.le_registro(arq),
                       reg_cota.le_registro(arq),
                       reg_cota.le_registro(arq),
                       *reg_polinomio.le_linha_tabela(arq, 5),
                       *reg_polinomio.le_linha_tabela(arq, 5),
                       *reg_evaporacao.le_linha_tabela(arq, 12),
                       reg_num_conjunto_maquinas.le_registro(arq),
                       *reg_num_conjunto_maquinas.le_linha_tabela(arq, 5),
                       *reg_potencia.le_linha_tabela(arq, 5),
                       *reg_ignorar.le_linha_tabela(arq, 75),
                       *reg_h_nominal.le_linha_tabela(arq, 5),
                       *reg_q_nominal.le_linha_tabela(arq, 5),
                       reg_produt.le_registro(arq),
                       reg_perdas.le_registro(arq),
                       reg_numero_polinomios.le_registro(arq),
                       *reg_polinomio.le_linha_tabela(arq, 30),
                       *reg_polinomio.le_linha_tabela(arq, 6),
                       reg_canal_fuga.le_registro(arq),
                       reg_influencia_vert.le_registro(arq),
                       reg_fator_carga.le_registro(arq),
                       reg_fator_carga.le_registro(arq),
                       reg_vazao.le_registro(arq),
                       reg_numero_unidades.le_registro(arq),
                       reg_tipo_turbina.le_registro(arq),
                       reg_repr_conjunto.le_registro(arq),
                       reg_taxa_indisp_f.le_registro(arq),
                       reg_taxa_indisp_p.le_registro(arq),
                       reg_tipo_perda.le_registro(arq),
                       reg_data.le_registro(arq),
                       reg_obs.le_registro(arq),
                       reg_vol_ref.le_registro(arq),
                       reg_tipo_regul.le_registro(arq)
                      ]

    # Override
    def escreve(self, arq: BufferedReader):
        """
        """
        pass


class LeituraHidr(LeituraBinario):
    """
    Classe com utilidades gerais para leitura de arquivos
    do DECOMP com comentários.
    """
    def __init__(self,
                 diretorio: str):
        super().__init__(diretorio)

    def _cria_blocos_leitura(self) -> List[BlocoBinario]:
        """
        Método que cria a lista de blocos a serem lidos no arquivo.
        Implementa o Factory Pattern.
        """
        MAX_BLOCOS = 600

        b: List[BlocoBinario] = [BlocoBinarioHidr()
                                 for _ in range(MAX_BLOCOS)]

        return b
