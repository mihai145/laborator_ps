import numpy as np

print(f'Intervalul de timp intre doua esatioane: {1/2000}s')

cnt_samples = 2000 * 60 * 60
print(f'Esantioane memorate intr-o ora: {cnt_samples}')

cnt_bytes = (cnt_samples * 4) // 8
print(f'Bytes consumati intr-o ora: {cnt_bytes}')
print(f'MB consumati intr-o ora: {np.round(cnt_bytes/(1024**2), 4)}')

# Rezultat:

# Intervalul de timp intre doua esatioane: 0.0005s
# Esantioane memorate intr-o ora: 7200000
# Bytes consumati intr-o ora: 3600000
# MB consumati intr-o ora: 3.4332