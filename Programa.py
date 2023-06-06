import random

# Lista de funcionários cadastrados
funcionario = []

# Dicionário contendo as "informações" para cada setor
setores = {
    "pre-campo": {
        "informacao_funcionario": [
            "O setor pré-campo compreende todas as atividades realizadas antes do início do cultivo, como o preparo do terreno, a análise do solo, a escolha das sementes e o planejamento das atividades agrícolas. É nessa etapa que os agricultores definem as estratégias e técnicas que serão adotadas para garantir o sucesso da safra.",
            "No setor pré-campo, os agricultores se dedicam a preparar adequadamente o terreno para o cultivo, realizando a aragem, a nivelagem e a adubação do solo. Além disso, é nessa fase que são feitas as análises do solo para verificar suas características e necessidades nutricionais, visando uma melhor escolha dos insumos agrícolas a serem utilizados.",
            "O setor pré-campo é fundamental para o sucesso da produção agrícola, pois é nele que são tomadas as decisões estratégicas que influenciarão diretamente os resultados obtidos no campo. Nessa etapa, os agricultores realizam estudos de viabilidade econômica, analisam as condições climáticas e escolhem as variedades de sementes mais adequadas, levando em consideração fatores como resistência a pragas, adaptação ao clima local e potencial de produtividade."
        ],
        "inovacoes_agricolas": [
            "Investir em tecnologias de sensoriamento remoto para monitorar as condições do solo, permitindo uma análise mais precisa e em tempo real das características e necessidades nutricionais. Isso auxiliará os agricultores a tomar decisões mais assertivas em relação à adubação e manejo do solo.",
            "Utilizar técnicas de agricultura de precisão, como o mapeamento detalhado da propriedade, para identificar áreas com diferentes características e necessidades, possibilitando a aplicação precisa de insumos agrícolas. Isso resultará em uma distribuição mais eficiente dos recursos e redução do desperdício.",
            "Explorar o uso de sistemas de informação geográfica (SIG) para analisar as condições climáticas e de solo, identificar áreas propícias para o cultivo de determinadas culturas e otimizar o planejamento agrícola. Essa abordagem auxiliará os agricultores a tomar decisões estratégicas com base em dados precisos e atualizados."
        ],
        "melhores_praticas": [
            "Realizar análises de solo regulares para avaliar suas características e necessidades nutricionais, permitindo a aplicação adequada de fertilizantes e corretivos. Isso garante um solo saudável e balanceado, favorecendo o desenvolvimento das culturas.",
            "Implementar o manejo integrado de pragas e doenças, priorizando o uso de métodos biológicos, como a introdução de organismos benéficos e o uso de armadilhas, em vez de depender exclusivamente de pesticidas químicos. Isso contribui para o equilíbrio do ecossistema e reduz os impactos negativos ao meio ambiente.",
            "Promover a diversificação de culturas, adotando rotação e consórcio de plantas, para melhorar a saúde do solo, reduzir a incidência de pragas e doenças, e aumentar a eficiência do uso de recursos naturais. Essa prática também contribui para a sustentabilidade econômica dos agricultores, oferecendo diversificação de produtos."
        ]
    },
    "campo": {
        "informacao_funcionario": [
            "O setor campo abrange todas as atividades relacionadas ao cultivo das plantas, desde o plantio até a colheita. Nessa fase, os agricultores aplicam técnicas de manejo adequadas para garantir o crescimento saudável das culturas, como irrigação, controle de pragas e doenças, adubação e monitoramento constante das condições da lavoura.",
            "No setor campo, os agricultores realizam o manejo diário da lavoura, aplicando práticas que visam otimizar o crescimento das plantas, prevenir a incidência de pragas e doenças, e garantir a produtividade esperada. Isso inclui atividades como irrigação na medida certa, controle de plantas invasoras, aplicação adequada de fertilizantes e defensivos agrícolas, monitoramento do estado das plantas e adoção de medidas corretivas quando necessário.",
            "O setor campo é a etapa em que os agricultores colocam em prática todo o conhecimento adquirido, utilizando técnicas e estratégias para cuidar das culturas, promover seu desenvolvimento e garantir uma colheita bem-sucedida. Envolve a realização de atividades como preparo do solo, plantio, tratos culturais (como irrigação, controle de pragas e doenças) e colheita. O manejo adequado da lavoura é essencial para garantir a qualidade dos produtos agrícolas e a sustentabilidade da produção."
        ],
        "inovacoes_agricolas": [
            "Implementar o uso de sensores de umidade do solo para monitorar as necessidades hídricas das plantas em tempo real. Isso permitirá uma irrigação mais eficiente e precisa, evitando tanto o excesso quanto a escassez de água nas culturas.",
            "Adotar o uso de técnicas de controle biológico de pragas, como a introdução de insetos predadores naturais ou o uso de armadilhas inteligentes. Essas estratégias reduzem a dependência de pesticidas químicos e promovem um manejo mais sustentável das pragas agrícolas.",
            "Utilizar drones equipados com câmeras e sensores para monitorar a saúde das plantas de forma mais eficiente. Essa tecnologia possibilita a detecção precoce de doenças, deficiências nutricionais ou estresses ambientais, permitindo a aplicação de medidas corretivas de maneira rápida e precisa."
        ],
        "melhores_praticas": [
            "Estabelecer um manejo adequado da água, utilizando técnicas de irrigação eficientes, como gotejamento ou aspersão localizada, para evitar o desperdício e garantir que as plantas recebam a quantidade necessária de água. Isso contribui para a conservação dos recursos hídricos e reduz os custos de produção.",
            "Realizar o monitoramento constante das plantas, observando seu desenvolvimento, detectando sinais de estresse, doenças ou pragas. Com base nessa observação, adotar medidas preventivas ou corretivas, como podas, adubações complementares ou controle biológico, para manter a saúde das culturas.",
            "Implementar práticas de conservação do solo, como o uso de cobertura vegetal, cultivo mínimo e terraceamento, para evitar a erosão, melhorar a estrutura do solo e aumentar sua capacidade de retenção de água e nutrientes. Isso promove a sustentabilidade do sistema produtivo e a preservação dos recursos naturais."
        ]
    },
    "pos-campo": {
        "informacao_funcionario": [
            "O setor pós-campo engloba as atividades que ocorrem após a colheita das culturas, envolvendo a logística de transporte dos produtos agrícolas até o local de processamento ou consumo, bem como o armazenamento adequado para preservar a qualidade e evitar perdas.",
            "No setor pós-campo, os agricultores lidam com a organização e o planejamento do transporte dos produtos agrícolas, selecionando os meios de transporte mais adequados, como caminhões, trens ou barcaças, e estabelecendo rotas eficientes para garantir que os produtos cheguem aos destinos finais de forma segura e dentro do prazo.",
            "O setor pós-campo também envolve a implementação de técnicas e estratégias de armazenamento adequado dos produtos agrícolas, como grãos, frutas e hortaliças, visando a conservação da qualidade e a prevenção de perdas. Isso inclui a seleção de estruturas de armazenamento adequadas, o controle da temperatura e umidade, a prevenção de infestações por pragas e o monitoramento constante da qualidade dos produtos. O objetivo é garantir que os alimentos cheguem aos consumidores finais em condições ideais, mantendo sua segurança e valor nutricional."
        ],
        "inovacoes_agricolas": [
            "Implementar o uso de tecnologias de rastreamento e monitoramento em tempo real durante o transporte dos produtos agrícolas. Isso possibilita um controle mais preciso das condições de transporte, como temperatura e umidade, garantindo a qualidade dos produtos até seu destino final.",
            "Adotar sistemas de armazenamento inteligentes, como silos com controle automatizado de temperatura e umidade. Essa tecnologia contribui para a conservação dos produtos agrícolas, evitando perdas por deterioração e mantendo sua qualidade ao longo do tempo.",
            "Implementar o uso de embalagens inteligentes e sustentáveis, equipadas com sensores de qualidade, que possam monitorar as condições internas dos produtos durante o transporte e armazenamento. Essas embalagens podem fornecer informações sobre temperatura, umidade, exposição à luz e até mesmo detectar a presença de gases indesejados. Isso permite o controle mais preciso das condições de conservação dos produtos, evitando perdas, garantindo a qualidade e prolongando sua vida útil. Além disso, o uso de embalagens sustentáveis, como materiais biodegradáveis ou recicláveis, contribui para a redução do impacto ambiental."
        ],
        "melhores_praticas": [
            "Adotar um planejamento eficiente da logística de transporte, considerando a otimização das rotas, a escolha dos veículos adequados e a programação adequada das entregas. Isso reduz os custos logísticos, minimiza os impactos ambientais e garante a entrega dos produtos agrícolas de forma rápida e segura.",
            "Utilizar métodos adequados de armazenamento, como a ventilação correta, o controle de temperatura e umidade, e a inspeção regular dos produtos, para preservar sua qualidade e evitar perdas. Isso contribui para a segurança alimentar, garantindo que os alimentos cheguem aos consumidores em condições ideais.",
            "Implementar boas práticas de higiene e segurança na manipulação dos produtos agrícolas durante a etapa de pós-campo, como o uso de equipamentos de proteção individual, a limpeza adequada dos recipientes de transporte e a adoção de procedimentos sanitários. Isso garante a qualidade e a segurança dos alimentos, protegendo a saúde dos consumidores."
        ]
    }
}

# Função para verificar a existência de um funcionário com base no ID
def verificar_existencia_funcionario(funcionario, id_funcionario):
    return next((c for c in funcionario if c["id"] == id_funcionario), None)

# Função para obter informações de um funcionário
def obter_informacao_funcionario(funcionario):
    id_funcionario = int(input("Digite o ID do funcionário para obter a devida informação: "))
    funcionario = verificar_existencia_funcionario(funcionario, id_funcionario)

    if not funcionario:
        print("O funcionário não existe!")
    else:
        setor = funcionario["setor"]
        informacoes_setor = setores.get(setor)

        if informacoes_setor:
            informacoes = informacoes_setor.get("informacao_funcionario")
            resposta = random.choice(informacoes)
            print(resposta)
        else:
            print("Setor inválido.")

# Função para obter informações sobre inovações agrícolas
def obter_inovacoes_agricolas(funcionario):
    id_funcionario = int(input("Digite o ID do funcionário para obter a devida informação: "))
    funcionario = verificar_existencia_funcionario(funcionario, id_funcionario)

    if not funcionario:
        print("O funcionário não existe!")
    else:
        setor = funcionario["setor"]
        informacoes_setor = setores.get(setor)

        if informacoes_setor:
            informacoes = informacoes_setor.get("inovacoes_agricolas")
            resposta = random.choice(informacoes)
            print(resposta)
        else:
            print("Setor inválido.")

# Função para obter informações sobre melhores práticas agrícolas
def obter_melhores_praticas_agricolas(funcionario):
    id_funcionario = int(input("Digite o ID do funcionário para obter a devida informação: "))
    funcionario = verificar_existencia_funcionario(funcionario, id_funcionario)

    if not funcionario:
        print("O funcionário não existe!")
    else:
        setor = funcionario["setor"]
        informacoes_setor = setores.get(setor)

        if informacoes_setor:
            informacoes = informacoes_setor.get("melhores_praticas")
            resposta = random.choice(informacoes)
            print(resposta)
        else:
            print("Setor inválido.")

# Função para cadastrar um funcionário
def cadastrar_funcionario(funcionario):
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    setor = input("Digite o setor do funcionário (pre-campo, campo, pos-campo): ")
    while setor not in ["pre-campo", "campo", "pos-campo"]:
        print("----------Valor inválido! Por favor, digite novamente.----------")
        setor = input("Digite o setor do funcionário (pre-campo, campo, pos-campo): ")
    novo_funcionario = {"id": len(funcionario) + 1, "nome": nome, "cargo": cargo, "setor": setor}

    funcionario.append(novo_funcionario)

    print(f"\nID do Funcionário cadastrado: {novo_funcionario['id']}")

# Função para listar os dados dos funcionários cadastrados
def listar_dados(funcionario):
    print("=== Lista de Funcionarios Cadastrados ===")
    if not funcionario:
        print("Nenhum funcionario cadastrado.")
    else:
        for funcionario in funcionario:
            print(f"ID: {funcionario['id']}")
            print(f"Nome: {funcionario['nome']}")
            print(f"Cargo: {funcionario['cargo']}")
            print(f"Setor: {funcionario['setor']}")
            print("------------------------")

# Loop principal do programa
while True:
    
    # Menu do Programa
    print("\nDigite o número da operação desejada:")
    print("[1] Cadastrar funcionário da fazenda")
    print("[2] Acesso à Informação")
    print("[3] Recomendações de Inovações Agrícolas")
    print("[4] Melhores Práticas Agrícolas")
    print("[5] Listar os Funcionarios Cadastrados")
    print("[6] Encerrar programa")
    opcao = int(input())

    if opcao == 1:
        cadastrar_funcionario(funcionario)
    elif opcao == 2:
        obter_informacao_funcionario(funcionario)
    elif opcao == 3:
        obter_inovacoes_agricolas(funcionario)
    elif opcao == 4:
        obter_melhores_praticas_agricolas(funcionario)
    elif opcao == 5:
        listar_dados(funcionario)
    elif opcao == 6:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Escolha uma opção válida.")
