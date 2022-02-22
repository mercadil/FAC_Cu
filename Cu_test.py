from pfac import fac

fac.SetAtom('Cu')
fac.Closed('1s', '2s', '3s')
fac.Config('2p6 3p6 4s1 3d10', group='ik0_ii0')
fac.Config('2p6 3p6 4s1 3d9', group='ik0_ii1')
fac.Config('2p6 3p6 4s1 3d7', group='ik0_ii3')
fac.Config('2p6 3p6 4s1 3d8', group='ik0_ii2')
fac.Config('2p6 3p6 4s1 3d6', group='ik0_ii4')
fac.Config('2p6 3p6 4s1 3d5', group='ik0_ii5')
fac.Config('2p6 3p6 4s1 3d4', group='ik0_ii6')
fac.Config('2p6 3p6 4s1 3d3', group='ik0_ii7')
fac.Config('2p6 3p6 4s1 3d2', group='ik0_ii8')
fac.Config('2p6 3p6 4s1 3d1', group='ik0_ii9')
fac.Config('2p6 3p6 4s1', group='ik0_ii10')

fac.Config('2p5 3p6 4s1 3d10', group='ik1_ii1')
fac.Config('2p5 3p6 4s1 3d9', group='ik1_ii2')
fac.Config('2p5 3p6 4s1 3d8', group='ik1_ii3')
fac.Config('2p5 3p6 4s1 3d7', group='ik1_ii4')
fac.Config('2p5 3p6 4s1 3d6', group='ik1_ii5')
fac.Config('2p5 3p6 4s1 3d5', group='ik1_ii6')
fac.Config('2p5 3p6 4s1 3d4', group='ik1_ii7')
fac.Config('2p5 3p6 4s1 3d3', group='ik1_ii8')
fac.Config('2p5 3p6 4s1 3d2', group='ik1_ii9')
fac.Config('2p5 3p6 4s1 3d1', group='ik1_ii10')

fac.Config('2p5 3p5 4s1 3d10', group='ik2_ii2')
fac.Config('2p5 3p5 4s1 3d9', group='ik2_ii3')
fac.Config('2p5 3p5 4s1 3d8', group='ik2_ii4')
fac.Config('2p5 3p5 4s1 3d7', group='ik2_ii5')
fac.Config('2p5 3p5 4s1 3d6', group='ik2_ii6')
fac.Config('2p5 3p5 4s1 3d5', group='ik2_ii7')
fac.Config('2p5 3p5 4s1 3d4', group='ik2_ii8')
fac.Config('2p5 3p5 4s1 3d3', group='ik2_ii9')
fac.Config('2p5 3p5 4s1 3d2', group='ik2_ii10')

fac.Config('2p5 3p4 4s1 3d10', group='ik3_ii3')
fac.Config('2p5 3p4 4s1 3d9', group='ik3_ii4')
fac.Config('2p5 3p4 4s1 3d8', group='ik3_ii5')
fac.Config('2p5 3p4 4s1 3d7', group='ik3_ii6')
fac.Config('2p5 3p4 4s1 3d6', group='ik3_ii7')
fac.Config('2p5 3p4 4s1 3d5', group='ik3_ii8')
fac.Config('2p5 3p4 4s1 3d4', group='ik3_ii9')
fac.Config('2p5 3p4 4s1 3d3', group='ik3_ii10')

fac.Config('2p6 3p5 4s1 3d10', group='ik4_ii1')
fac.Config('2p6 3p5 4s1 3d9', group='ik4_ii2')
fac.Config('2p6 3p5 4s1 3d8', group='ik4_ii3')
fac.Config('2p6 3p5 4s1 3d7', group='ik4_ii4')
fac.Config('2p6 3p5 4s1 3d6', group='ik4_ii5')
fac.Config('2p6 3p5 4s1 3d5', group='ik4_ii6')
fac.Config('2p6 3p5 4s1 3d4', group='ik4_ii7')
fac.Config('2p6 3p5 4s1 3d3', group='ik4_ii8')
fac.Config('2p6 3p5 4s1 3d2', group='ik4_ii9')
fac.Config('2p6 3p5 4s1 3d1', group='ik4_ii10')

ladders = {0: 0, 1: 1, 2: 2, 3: 3, 4: 1}

all_groups = ["ik%d_ii%d"%(k, i) for k in ladders for
               i in range(ladders[k], 11)]
ii1_low = ['ik0_ii1']
ii1_up = ['ik1_ii1']

name = 'Cu_test'
fac.ConfigEnergy(0)
fac.OptimizeRadial(['ik0_ii0'])
fac.ConfigEnergy(1)
print('ConfigEnergy and optimizeRadial done.')
fac.Structure(name+'.lev.b', all_groups)
fac.MemENTable(name+'.lev.b')
fac.PrintTable(name+'.lev.b', name+'.lev', 1)
print('Level table saved.')
fac.TransitionTable(name+'.tr.b', [ii1_low], [ii1_up])
fac.PrintTable(name+'.tr.b', name+'.tr', 1)
print('Transition table saved.')
#fac.AITable(name+'.ai.b', ['2pm1'], ['3dm2', '3dm1_4sm1'])
#fac.PrintTable(name+'.ai.b', name+'.ai', 1)
#print('AI table saved.')

#print(fac.AIBranch(name+'.ai.b', 319, 7))
#print(fac.AIBranch(name+'.ai.b', 320, 7))
