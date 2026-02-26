import streamlit as st

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