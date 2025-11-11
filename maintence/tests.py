from django.test import TestCase
from maintence.models.reparos import Reparos
from maintence.models.ativos import Ativos
from django.contrib.auth import get_user_model

User = get_user_model()

class ReparoROITest(TestCase):
    def setUp(self):
        # cria um ativo e um usuário de teste
        self.user = User.objects.create(username='teste_user')
        self.ativo = Ativos.objects.create(
            nome="Compressor",
            codigo_ativo="CMP001",
            valor_inicial=10000,
            vida_util_esperada=1000,
            unid_vida_util="horas"
        )

    def test_calculo_roi_funciona(self):
        """Verifica se o ROI é calculado corretamente ao salvar"""
        reparo = Reparos.objects.create(
            id_ativo=self.ativo,
            tipo="Corretiva",
            descricao="Troca de válvula",
            tempo_parada_hora=5,
            extensao_vida_util=100,
            unid_extensao_vida_util="horas",
            id_usuario=self.user,
            custo_total_peca=500,
            custo_mao_obra=200
        )

        # ROI esperado = ((ganho - custo) / custo)
        # ganho = (valor_inicial / vida_util_esperada) * extensao_vida_util
        ganho = (self.ativo.valor_inicial / self.ativo.vida_util_esperada) * reparo.extensao_vida_util
        custo = reparo.custo_total()
        roi_esperado = round((ganho - custo) / custo, 2)

        print(f"\n💡 Ganho estimado: {ganho}, Custo total: {custo}, ROI calculado: {reparo.roi_calculado}")
        self.assertAlmostEqual(float(reparo.roi_calculado), roi_esperado, places=2)

    def test_custo_total_soma_peca_e_mao_obra(self):
        """Verifica se o custo_total soma os dois campos"""
        reparo = Reparos.objects.create(
            id_ativo=self.ativo,
            tipo="Preventiva",
            descricao="Lubrificação",
            tempo_parada_hora=2,
            extensao_vida_util=50,
            unid_extensao_vida_util="horas",
            id_usuario=self.user,
            custo_total_peca=200,
            custo_mao_obra=300
        )
        self.assertEqual(float(reparo.custo_total()), 500.0)
