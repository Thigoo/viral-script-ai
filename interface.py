import streamlit as st

from engine.pipeline import run_pipeline

st.set_page_config(
    page_title="Viral Script AI",
    page_icon="🚀",
    layout="wide",

)

tab1, tab2 = st.tabs(["📘 Sobre o Produto", "⚙️ Gerador de Roteiros"])

# ABA 1 — SOBRE O PRODUTO
with tab1:

    st.markdown("# 🚀 Viral Script AI")
    st.markdown("### Crie roteiros virais otimizados por IA em menos de 1 minuto.")
    
    st.markdown("""
    Uma IA com sistema interno de criação, crítica e refinamento automático 
    para gerar roteiros mais envolventes e dentro da duração ideal para 
    **Shorts, Reels e TikTok**.
    """)

    st.divider()

    st.markdown("## 🧠 O Que é o Viral Script AI?")

    st.markdown("""
    O Viral Script AI é uma ferramenta de geração de roteiros baseada em 
    um sistema **multi-agente de Inteligência Artificial**.

    Em vez de simplesmente gerar um texto, ele utiliza três etapas internas:
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🎨 Criativo")
        st.markdown("Gera o roteiro inicial com foco em impacto e engajamento.")

    with col2:
        st.markdown("### 🧠 Crítico")
        st.markdown("Avalia qualidade, retenção, profundidade e alinhamento com o tema.")

    with col3:
        st.markdown("### 🔁 Refinador")
        st.markdown("Ajusta automaticamente o roteiro para melhorar desempenho e duração.")

    st.divider()

    st.markdown("## 🎯 Para Quem é")

    st.markdown("""
    - Criadores de conteúdo  
    - YouTubers  
    - Influenciadores  
    - Profissionais de marketing  
    - Quem quer crescer com vídeos curtos  

    Ideal para quem produz conteúdo para:
    - YouTube Shorts  
    - Instagram Reels  
    - TikTok  
    """)

    st.divider()

    st.markdown("## 🚀 Como Funciona")

    st.markdown("""
    1. Você informa um tema.  
    2. A IA cria um roteiro inicial.  
    3. O sistema avalia qualidade e duração.  
    4. Se necessário, ele ajusta automaticamente.  
    5. Você recebe um roteiro final otimizado.  

    Tudo isso em segundos.
    """)

    st.divider()

    st.markdown("## 📊 O Diferencial")

    st.markdown("""
    ✔️ Avaliação automática de qualidade  
    ✔️ Verificação de duração estimada  
    ✔️ Refinamento iterativo até atingir padrão mínimo  
    ✔️ Estrutura multi-agente inteligente  

    Isso significa menos tentativa e erro para você.
    """)

    st.divider()

    st.markdown("## 💡 Missão")

    st.markdown("""
    Facilitar a criação de conteúdo estratégico usando Inteligência Artificial estruturada,
    tornando a produção de vídeos mais eficiente e profissional.
    """)

# ABA 2 — GERADOR REAL
with tab2:

    st.markdown("# ⚙️ Gerador de Roteiros")

    st.markdown("Digite um tema e gere um roteiro otimizado automaticamente.")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        theme = st.text_input("🎯 Tema do vídeo")

    # with col2:
    #     platform = st.selectbox(
    #         "📱 Plataforma",
    #         ["YouTube Shorts", "Instagram Reels", "TikTok"]
    #     )

    generate_button = st.button("🚀 Gerar roteiro")

    st.divider()

    if generate_button and theme:

        status_container = st.empty()

        with st.spinner("Executando pipeline multi-agente..."):
            result = run_pipeline(theme)

        status_container.empty()

        st.markdown("## 📜 Roteiro Final")
        st.markdown(result["final_script"])

        st.divider()

        st.markdown("## 📊 Métricas de Qualidade")

        if result["iterations"]:
            last_iteration = result["iterations"][-1]
            critic = last_iteration["critic"]

            metrics = {
                "Hook": critic["hook_score"],
                "Retenção": critic["retention_score"],
                "Profundidade": critic["depth_score"],
                "Clareza": critic["clarity_score"],
                "Alinhamento com Tema": critic["theme_alignment_score"],
            }

            for name, value in metrics.items():
                st.markdown(f"**{name} — {value}/10**")
                st.progress(value / 10)

        st.markdown(f"### ⏱️ Duração estimada: {result['final_duration']}s")

        st.metric("Duração estimada", f'{result["final_duration"]}s')

        st.divider()

        with st.expander("🔍 Ver processo de melhoria"):

            if result["initial_script"]:
                st.markdown("### 📝 Roteiro Inicial")
                st.markdown(result["initial_script"])
                st.divider()

            for iteration in result["iterations"]:

                st.markdown(f"### 🔁 Iteração {iteration['iteration']}")
                st.markdown(f"Duração estimada: {iteration['duration']}s")

                critic_data = iteration["critic"]

                st.markdown("**Feedback do crítico:**")
                st.write(critic_data["feedback"])

                st.divider()

        st.success("Roteiro pronto para publicação 🚀")

    elif generate_button and not theme:
        st.warning("Digite um tema para gerar o roteiro.")