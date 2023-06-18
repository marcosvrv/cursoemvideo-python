d = float(input('Uma distância em metros: '))
print('A medida de {}m corresponde a:'.format(d))
km = d / 10 / 10 / 10
hm = d / 10 / 10
dam = d / 10
dm = d * 10
cm = d * 10 * 10
mm = d * 10 * 10 * 10
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))
