from pfac import fac

fac.SetAtom('Cu')
fac.Closed('1s', '2s', '3s')
fac.Config('3p6 2p6 3d9 4s1', group='upper')
fac.Config('3p6 2p5 3d10 4s1', group='lower')

name = 'Cu_test'
fac.ConfigEnergy(0)
fac.OptimizeRadial('lower')
fac.ConfigEnergy(1)
print('ConfigEnergy and optimizeRadial done.')
fac.Structure(name+'.lev.b', ['upper', 'lower'])
fac.MemENTable(name+'.lev.b')
fac.PrintTable(name+'.lev.b', name+'.lev', 1)
print('Level table saved.')
fac.TransitionTable(name+'.tr.b', ['lower'], ['upper'])
fac.PrintTable(name+'.tr.b', name+'.tr', 1)
print('Transition table saved.')
