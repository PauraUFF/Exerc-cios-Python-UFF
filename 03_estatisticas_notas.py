notas = [7.5, 8.0, 6.5, 9.0, 7.8, 4.2, 0.5, 3.0]
media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)
acima_media = [nota for nota in notas if nota > media]

print(f"Média: {media:.2f}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Notas acima da média: {len(acima_media)}")
