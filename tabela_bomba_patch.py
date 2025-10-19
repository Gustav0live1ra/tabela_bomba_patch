import pandas as pd
from tabulate import tabulate

def l():
    print('-='*70)
try:
    db = pd.read_csv('tabela_final.csv')
except:
    db = pd.DataFrame({
        'jogador' : ['jogador1','jogador2','jogador3','jogador4'],
        'jogos' : [0,0,0,0],
        'pontos' : [0,0,0,0],
        'vitorias' : [0,0,0,0],
        'empates' : [0,0,0,0],
        'derrotas' : [0,0,0,0],
        'gols pro' : [0,0,0,0],
        'gols contra' : [0,0,0,0],
        'saldo de gols' : [0,0,0,0]
    })
    db.to_csv('tabela_final.csv', index=False)


jogadores = db['jogador'].tolist()
total_partidas = int(input('Quantas partidas foram jogadas? '))

for c in range(1,total_partidas+1):

    db = pd.read_csv('tabela_final.csv')

    l()
    print(f'{c:>60}º partida')
    time_1 = str(input('jogador da casa: ')).lower()
    time_2 = str(input('jogador de fora: ')).lower()
    gols_1 = int(input('gols jogador casa: '))
    gols_2 = int(input('gols jogador fora: '))
    print()

    #Sempre use "or" para validar ambos os jogadores.
    #Assim, o código só continua quando ambos estiverem registrados.
    if time_1 not in jogadores or time_2 not in jogadores:
        while time_1 not in jogadores or time_2 not in jogadores:
            print('JOGADOR NÃO REGISTRADO, POR FAVOR INSIRA OS DADOS CORRETAMENTE!\n')
            time_1 = str(input('jogador da casa: ')).lower()
            time_2 = str(input('jogador de fora: ')).lower()
            gols_1 = int(input('gols jogador casa: '))
            gols_2 = int(input('gols jogador fora: '))
            print()
    if gols_1 > gols_2:
        db.loc[db['jogador'] == time_1, 'jogos'] += 1
        db.loc[db['jogador'] == time_2, 'jogos'] += 1
        db.loc[db['jogador'] == time_1, 'pontos'] += 3
        db.loc[db['jogador'] == time_1, 'vitorias'] += 1
        db.loc[db['jogador'] == time_2, 'derrotas'] += 1
        db.loc[db['jogador'] == time_1, 'gols pro'] += gols_1
        db.loc[db['jogador'] == time_1, 'gols contra'] += gols_2
        db.loc[db['jogador'] == time_1, 'saldo de gols'] += gols_1 - gols_2
        db.loc[db['jogador'] == time_2, 'gols pro'] += gols_2
        db.loc[db['jogador'] == time_2, 'gols contra'] += gols_1
        db.loc[db['jogador'] == time_2, 'saldo de gols'] += gols_2 - gols_1
    elif gols_1 < gols_2:
        db.loc[db['jogador'] == time_1, 'jogos'] += 1
        db.loc[db['jogador'] == time_2, 'jogos'] += 1
        db.loc[db['jogador'] == time_2, 'pontos'] += 3
        db.loc[db['jogador'] == time_2, 'vitorias'] += 1
        db.loc[db['jogador'] == time_1, 'derrotas'] += 1
        db.loc[db['jogador'] == time_2, 'gols pro'] += gols_2
        db.loc[db['jogador'] == time_2, 'gols contra'] += gols_1
        db.loc[db['jogador'] == time_2, 'saldo de gols'] += gols_2 - gols_1
        db.loc[db['jogador'] == time_1, 'gols pro'] += gols_1
        db.loc[db['jogador'] == time_1, 'gols contra'] += gols_2
        db.loc[db['jogador'] == time_1, 'saldo de gols'] += gols_1 - gols_2
    else: # gols_1 == gols_2
        db.loc[db['jogador'] == time_1, 'jogos'] += 1
        db.loc[db['jogador'] == time_2, 'jogos'] += 1
        db.loc[db['jogador'] == time_1, 'pontos'] += 1
        db.loc[db['jogador'] == time_2, 'pontos'] += 1
        db.loc[db['jogador'] == time_1, 'empates'] += 1
        db.loc[db['jogador'] == time_2, 'empates'] += 1
        db.loc[db['jogador'] == time_1, 'gols pro'] += gols_1
        db.loc[db['jogador'] == time_1, 'gols contra'] += gols_2
        db.loc[db['jogador'] == time_2, 'gols pro'] += gols_2
        db.loc[db['jogador'] == time_2, 'gols contra'] += gols_1

    db = db.sort_values(by=['pontos', 'vitorias', 'saldo de gols', 'gols pro'], ascending=[False, False, False, False]).reset_index(drop=True)
    db.index += 1
    db.index.name = 'posição'
    db.index = db.index.astype(str) + 'º'
    print(tabulate(db, headers='keys', tablefmt='fancy_grid', showindex=True))
    db.to_csv('tabela_final.csv', index=False)
