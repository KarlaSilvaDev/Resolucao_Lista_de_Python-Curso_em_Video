dist = float(input('Insira uma distância em metros: '))
print('A medida de {} metros corresponde a:\n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(dist, (dist/1000), (dist/100), (dist/10), (dist*10), (dist*100), (dist*1000) ))