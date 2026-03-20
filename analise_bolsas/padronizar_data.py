def padronizar_periodo(periodo):
    import pandas as pd
    import re

    if pd.isna(periodo):
        return None

    periodo = str(periodo).strip()

    if ' a ' not in periodo:
        print(f"Formato inesperado: {periodo}")
        return None

    # Caso 1: datas completas
    if re.match(r'\d{2}/\d{2}/\d{4}', periodo):
        inicio, fim = periodo.split(' a ')
        inicio = pd.to_datetime(inicio, dayfirst=True)
        fim = pd.to_datetime(fim, dayfirst=True)

    else:
        meses = {
            'Janeiro': 1, 'Fevereiro': 2, 'Março': 3, 'Abril': 4,
            'Maio': 5, 'Junho': 6, 'Julho': 7, 'Agosto': 8,
            'Setembro': 9, 'Outubro': 10, 'Novembro': 11, 'Dezembro': 12
        }

        # 🔹 Caso 2: Novembro/2024 a Fevereiro/2025
        if '/' in periodo:
            inicio_str, fim_str = periodo.split(' a ')
            
            mes_inicio, ano_inicio = inicio_str.split('/')
            mes_fim, ano_fim = fim_str.split('/')
            
            mes_inicio = mes_inicio.strip().capitalize()
            mes_fim = mes_fim.strip().capitalize()
            
            inicio = pd.to_datetime(f'{ano_inicio}-{meses[mes_inicio]}-01')
            fim = pd.to_datetime(f'{ano_fim}-{meses[mes_fim]}-01') + pd.offsets.MonthEnd(0)

        # 🔹 Caso 3: 2025-Maio a Dezembro
        else:
            ano, resto = periodo.split('-')
            mes_inicio, mes_fim = resto.split(' a ')
            
            mes_inicio = mes_inicio.strip().capitalize()
            mes_fim = mes_fim.strip().capitalize()
            
            inicio = pd.to_datetime(f'{ano}-{meses[mes_inicio]}-01')
            fim = pd.to_datetime(f'{ano}-{meses[mes_fim]}-01') + pd.offsets.MonthEnd(0)

    return f"{inicio.date()} a {fim.date()}"