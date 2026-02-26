from engine.pipeline import run_pipeline

if __name__ == "__main__":

    theme = input("Digite o tema: ")

    result = run_pipeline(theme)

    print("\n=== SCRIPT FINAL ===\n")
    print(result["final_script"])

    print(f"\nDuração final: {result['final_duration']}s")