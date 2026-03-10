# Viral Script AI

**Viral Script** é um gerador de roteiros para vídeos curtos alimentado por IA, projetado para criar e otimizar roteiros com alto potencial de retenção para plataformas como **YouTube Shorts, Instagram Reels e TikTok**.

O sistema utiliza uma **arquitetura multi-agente baseada em LLMs**, onde diferentes agentes especializados colaboram em um pipeline de geração e melhoria de conteúdo.

O fluxo segue o modelo:

`Criar → Criticar → Refinar`

Esse processo permite que o roteiro seja **gerado, analisado criticamente e otimizado automaticamente**, resultando em textos mais naturais, envolventes e estruturados para maximizar retenção de audiência.

---

# Objetivos do Projeto

Este projeto foi desenvolvido com três propósitos principais:

### 1️⃣ Laboratório técnico

Explorar na prática conceitos modernos de:

- Engenharia de prompts
- Orquestração de LLMs
- Sistemas multi-agente
- Pipelines iterativos de geração de conteúdo

### 2️⃣ MVP de produto

Testar a viabilidade de uma ferramenta que ajude criadores de conteúdo a gerar roteiros de forma rápida e otimizada.

### 3️⃣ Estudo de arquitetura de IA aplicada

Demonstrar como múltiplos agentes especializados podem colaborar para melhorar resultados gerados por modelos de linguagem.

---

# Arquitetura do Sistema

O sistema utiliza uma arquitetura de **multi-agentes especializados**, onde cada agente possui uma função específica dentro do pipeline.

## Creative Agent

Responsável por gerar o **primeiro rascunho do roteiro**.

Ele utiliza técnicas de:

- storytelling
- curiosidade narrativa
- psicologia de retenção
- linguagem natural para vídeos curtos

Entrada:

- tema ou título do vídeo

Saída:

- roteiro inicial

---

## Critic Agent

Analisa o roteiro gerado avaliando sua qualidade com base em critérios específicos.

Critérios avaliados:

- força do gancho inicial
- potencial de retenção
- profundidade do conteúdo
- clareza narrativa
- alinhamento com o tema

O agente retorna:

- pontuações de qualidade
- feedback detalhado
- indicação se o roteiro precisa de refinamento

---

## Refinement Agent

Responsável por **melhorar o roteiro inicial** com base na análise do agente crítico.

Esse agente:

- corrige pontos fracos
- melhora a narrativa
- mantém a estrutura original quando já funciona
- evita clichês comuns de IA
- preserva ritmo adequado para vídeos curtos

---

# Pipeline de Geração

O fluxo completo do sistema funciona da seguinte forma:

```
Usuário fornece tema do vídeo
↓
Creative Agent gera roteiro inicial
↓
Critic Agent avalia o roteiro
↓
Refinement Agent otimiza o conteúdo
↓
Roteiro final é apresentado ao usuário
```

Além disso, o sistema também calcula:

- **duração estimada de narração**
- **legendas automáticas (.srt)**

---

# Interface

A aplicação possui uma interface web simples construída com **Streamlit**, permitindo:

- inserir o tema do vídeo
- gerar roteiros automaticamente
- visualizar versão inicial e versão otimizada
- baixar legendas prontas
- acompanhar o processo de melhoria do roteiro

---

# Tecnologias Utilizadas

- Python
- Streamlit
- LangChain
- LangGraph
- LLMs (via API)
- Prompt Engineering

---

# Funcionalidades

- geração automática de roteiros para vídeos curtos
- arquitetura multi-agente
- análise crítica automatizada
- refinamento automático de conteúdo
- cálculo de duração estimada
- geração de arquivo de legenda `.srt`
- interface interativa para criação de conteúdo

---

---

# Como Executar o Projeto

### 1. Clonar o repositório

`git clone https://github.com/seu-usuario/viral-script.git`

### 2. Entrar no projeto

`cd viral-script-ai`

### 3. Criar ambiente virtual

`python -m venv venv`

### 4. Ativar ambiente virtual

- Windows
  `venv\Scripts\activate`

- Linux/Mac
  `source venv/bin/activate`

### 5. Instalar dependências

`pip install -r requirements.txt`

### 6. Configurar variáveis de ambiente

Crie um arquivo `.env` com sua chave da API

Exemplo:

`OPENAI_API_KEY=sua_chave_aqui`

### 7. Rodar a aplicação

`streamlit run interface.py`

### Exemplos de uso

Entrada do usuário:

`Dicas para ser mais saudável`

Saída:

Um roteiro estruturado com:

- gancho inicial
- desenvolvimento narrativo
- conclusão memorável
- duração ideal para Shorts

### Aprendizados

Este projeto explora conceitos importantes de IA aplicada:

- design de agentes especializados
- pipelines de geração iterativa
- avaliação automática de conteúdo
- mitigação de padrões de escrita de IA
- otimização para retenção de audiência
