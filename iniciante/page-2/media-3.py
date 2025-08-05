def main():
    n1, n2, n3, n4 = map(float, input().split())
    m = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / (2 + 3 + 4 + 1)
    
    try:
        e = float(input())
        print(f"Media: {m:.1f}")
        print("Aluno em exame.")
        print(f"Nota do exame: {e:.1f}")
        
        m = (m + e) / 2
        if m >= 5:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print(f"Media final: {m:.1f}")

    except:
        print(f"Media: {m:.1f}")
        if m >= 7:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        
    return 0

if __name__ == "__main__":
    main()