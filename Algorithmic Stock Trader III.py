b = [153, 117, 125, 184, 146, 190, 91, 26, 45, 94, 13, 61, 171, 28, 106, 126, 98, 16, 156, 43, 176, 139, 54, 140, 198]

from Algorithmic_Stock_Trader_IV import loop, pot

pot_new, pick = pot(b)

print(loop(0, 2, pick, pot_new)[0])