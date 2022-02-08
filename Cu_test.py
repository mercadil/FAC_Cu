from pfac import fac

fac.SetAtom('Cu')
fac.Closed('1s', '2s', '3s', '3p')
fac.Config('2p6 3d10 4s1', group='ground')
fac.Config('2p6 3d9 4s1', group='lower')
fac.Config('2p5 3d10 4s1', group='upper')
fac.Config('2p6 3d8 4s1', group='lower_AI')

name = 'Cu_test'
fac.ConfigEnergy(0)
fac.OptimizeRadial('ground')
fac.ConfigEnergy(1)
print('ConfigEnergy and optimizeRadial done.')
fac.Structure(name+'.lev.b', ['ground', 'upper',
                              'lower', 'lower_AI',])
fac.MemENTable(name+'.lev.b')
fac.PrintTable(name+'.lev.b', name+'.lev', 1)
print('Level table saved.')
fac.TransitionTable(name+'.tr.b', ['lower'], ['upper'])
fac.PrintTable(name+'.tr.b', name+'.tr', 1)
print('Transition table saved.')
fac.AITable(name+'.ai.b', ['upper'], ['lower_AI'])
fac.PrintTable(name+'.ai.b', name+'.ai', 1)
print('AI table saved.')

print(fac.AIBranch(name+'.ai.b', 21, 5))
print(fac.AIBranch(name+'.ai.b', 21, 12))
