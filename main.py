from agents.creative_agent import generate_script

if __name__ == '__main__':
    theme = 'Por que o pão de acúcar tem esse nome?'
    script = generate_script(theme)
    print('\n=== ROTEIRO GERADO ===\n')
    print(script)