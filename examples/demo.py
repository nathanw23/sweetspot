from sweetspot import LargerIsBetter,TargetIsBest,MultiObjectiveDesirability
import numpy as np
wt=LargerIsBetter(0,12); mut=TargetIsBest(0)
MOD=MultiObjectiveDesirability({"WT":wt,"Mut":mut})
print(MOD(WT=[0,6,12],Mut=[0,1,-1]))
