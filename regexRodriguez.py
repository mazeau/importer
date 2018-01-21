import re
from rdkit import Chem

inputfile ="""
! Radicals from the base
R1H   !   .h
R2OH   !   .oh
R3OOH   !   .o/oh
R4CH3   !   .ch3
R5CHO   !   .ch//o
R6CH2OH   !   .ch2/oh
R7CH3O   !   .o/ch3
R8CH3OO   !   .o/o/ch3
R9C2HT   !   .c///ch
R10C2H3V   !   .ch//ch2
R11C2H5   !   .ch2/ch3
R12CHCOV   !   .ch//c//o
R13CH2CHO   !   .ch2/ch//o
R14CH3CO   !   .c(//o)/ch3
R15C2H5O   !   .o/ch2/ch3
R16C2H4OOH   !   .ch2/ch2/o/oh
R17C2H5OO   !   .o/o/ch2/ch3
R18CH3COOO   !   .o/o/c(//o)/ch3
R19C3H7   !   .ch2/ch2/ch3
R20C4H9   !   .ch2/ch2/ch2/ch3
R21CH3OCO   !   .c(//o)/o/ch3
R22CO2H   !   .c(//o)/oh
R23C2H3O2B   !   .ch2/c(//o)/oh
R24C2H4OH   !   .ch2/ch2/oh
R25C2H4OH   !   .ch(/oh)/ch3
! Free radicals :
R26C5H11   !   .ch(/ch2/ch3)2
R27C5H11   !   .ch2/ch2/ch2/ch2/ch3
R28C5H11   !   .ch(/ch3)/ch2/ch2/ch3
R29C6H11OK   !   .c(//o)/ch2/ch2/ch2/ch2/ch3
R30C6H11OA   !   .ch2/ch2/ch2/ch2/ch2/ch//o
R31C6H11OA   !   .ch(/ch3)/ch2/ch2/ch2/ch//o
R32C6H11OA   !   .ch(/ch2/ch3)/ch2/ch2/ch//o
R33C6H11OA   !   .ch(/ch2/ch//o)/ch2/ch2/ch3
R34C6H11OA   !   .ch(/ch//o)/ch2/ch2/ch2/ch3
R35C6H11O2K   !   .o/c(//o)/ch2/ch2/ch2/ch2/ch3
R36C6H11O2B   !   .ch2/ch2/ch2/ch2/ch2/c(//o)/oh
R37C6H11O2B   !   .ch(/ch3)/ch2/ch2/ch2/c(//o)/oh
R38C6H11O2B   !   .ch(/ch2/ch3)/ch2/ch2/c(//o)/oh
R39C6H11O2B   !   .ch(/ch2/c(//o)/oh)/ch2/ch2/ch3
R40C6H11O2B   !   .ch(/c(//o)/oh)/ch2/ch2/ch2/ch3
R41C3H7O2U   !   .o/o/ch2/ch2/ch3
R42C4H9O2U   !   .o/o/ch2/ch2/ch2/ch3
R43C5H11O2U   !   .o/o/ch(/ch2/ch3)2
R44C5H11O2U   !   .o/o/ch2/ch2/ch2/ch2/ch3
R45C5H11O2U   !   .o/o/ch(/ch3)/ch2/ch2/ch3
R46C6H11O3AU   !   .o/o/ch2/ch2/ch2/ch2/ch2/ch//o
R47C4H7OA   !   .ch2/ch2/ch2/ch//o
R48C6H11O3AU   !   .o/o/ch(/ch3)/ch2/ch2/ch2/ch//o
R49C3H5OA   !   .ch2/ch2/ch//o
R50C6H11O3AU   !   .o/o/ch(/ch2/ch3)/ch2/ch2/ch//o
R51C6H11O3AU   !   .o/o/ch(/ch2/ch//o)/ch2/ch2/ch3
R52C6H11O3AU   !   .o/o/ch(/ch//o)/ch2/ch2/ch2/ch3
R53C6H11O4UB   !   .o/o/ch2/ch2/ch2/ch2/ch2/c(//o)/oh
R54C4H7O2B   !   .ch2/ch2/ch2/c(//o)/oh
R55C6H11O4UB   !   .o/o/ch(/ch3)/ch2/ch2/ch2/c(//o)/oh
R56C3H5O2B   !   .ch2/ch2/c(//o)/oh
R57C6H11O4UB   !   .o/o/ch(/ch2/ch3)/ch2/ch2/c(//o)/oh
R58C6H11O4UB   !   .o/o/ch(/ch2/c(//o)/oh)/ch2/ch2/ch3
R59C6H11O4UB   !   .o/o/ch(/c(//o)/oh)/ch2/ch2/ch2/ch3
R60C3H7O2P   !   .ch(/ch3)/ch2/o/oh
R61C3H7O2P   !   .ch2/ch2/ch2/o/oh
R62C4H9O2P   !   .ch(/ch2/o/oh)/ch2/ch3
R63C4H9O2P   !   .ch(/ch3)/ch2/ch2/o/oh
R64C4H9O2P   !   .ch2/ch2/ch2/ch2/o/oh
R65C5H11O2P   !   .ch(/ch3)/ch(/o/oh)/ch2/ch3
R66C5H11O2P   !   .ch2/ch2/ch(/o/oh)/ch2/ch3
R67C5H11O2P   !   .ch(/ch2/o/oh)/ch2/ch2/ch3
R68C5H11O2P   !   .ch(/ch2/ch3)/ch2/ch2/o/oh
R69C5H11O2P   !   .ch(/ch3)/ch2/ch2/ch2/o/oh
R70C5H11O2P   !   .ch2/ch2/ch2/ch2/ch2/o/oh
R71C5H11O2P   !   .ch2/ch(/o/oh)/ch2/ch2/ch3
R72C5H11O2P   !   .ch(/ch2/ch3)/ch(/o/oh)/ch3
R73C5H11O2P   !   .ch(/ch3)/ch2/ch(/o/oh)/ch3
R74C5H11O2P   !   .ch2/ch2/ch2/ch(/o/oh)/ch3
R75C6H11O3AP   !   .ch(/ch2/o/oh)/ch2/ch2/ch2/ch//o
R76C6H11O3AP   !   .ch(/ch2/ch2/o/oh)/ch2/ch2/ch//o
R77C6H11O3AP   !   .ch(/ch2/ch//o)/ch2/ch2/ch2/o/oh
R78C6H11O3AP   !   .ch(/ch//o)/ch2/ch2/ch2/ch2/o/oh
R79C4H7O3AU   !   .o/o/ch2/ch2/ch2/ch//o
R80C4H7OK   !   .c(//o)/ch2/ch2/ch3
R81C6H11O3AP   !   .ch2/ch(/o/oh)/ch2/ch2/ch2/ch//o
R82C6H11O3AP   !   .ch(/ch(/o/oh)/ch3)/ch2/ch2/ch//o
R83C6H11O3AP   !   .ch(/ch2/ch//o)/ch2/ch(/o/oh)/ch3
R84C6H11O3AP   !   .ch(/ch//o)/ch2/ch2/ch(/o/oh)/ch3
R85C6H11O3KP   !   .c(//o)/ch2/ch2/ch2/ch(/o/oh)/ch3
R86C3H5O3AU   !   .o/o/ch2/ch2/ch//o
R87C6H11O3AP   !   .ch(/ch3)/ch(/o/oh)/ch2/ch2/ch//o
R88C6H11O3AP   !   .ch2/ch2/ch(/o/oh)/ch2/ch2/ch//o
R89C6H11O3AP   !   .ch(/ch2/ch//o)/ch(/o/oh)/ch2/ch3
R90C6H11O3AP   !   .ch(/ch//o)/ch2/ch(/o/oh)/ch2/ch3
R91C6H11O3KP   !   .c(//o)/ch2/ch2/ch(/o/oh)/ch2/ch3
R92C6H11O3AP   !   .ch(/ch//o)/ch(/o/oh)/ch2/ch2/ch3
R93C6H11O3KP   !   .c(//o)/ch2/ch(/o/oh)/ch2/ch2/ch3
R94C6H11O3AP   !   .ch(/ch2/ch3)/ch(/o/oh)/ch2/ch//o
R95C6H11O3AP   !   .ch(/ch3)/ch2/ch(/o/oh)/ch2/ch//o
R96C6H11O3AP   !   .ch2/ch2/ch2/ch(/o/oh)/ch2/ch//o
R97C6H11O3KP   !   .c(//o)/ch(/o/oh)/ch2/ch2/ch2/ch3
R98C6H11O3AP   !   .ch(/ch(/o/oh)/ch//o)/ch2/ch2/ch3
R99C6H11O3AP   !   .ch(/ch2/ch3)/ch2/ch(/o/oh)/ch//o
R100C6H11O3AP   !   .ch(/ch3)/ch2/ch2/ch(/o/oh)/ch//o
R101C6H11O3AP   !   .ch2/ch2/ch2/ch2/ch(/o/oh)/ch//o
R102C6H11O4PB   !   .ch(/ch2/o/oh)/ch2/ch2/ch2/c(//o)/oh
R103C6H11O4PB   !   .ch(/ch2/ch2/o/oh)/ch2/ch2/c(//o)/oh
R104C6H11O4PB   !   .ch(/ch2/c(//o)/oh)/ch2/ch2/ch2/o/oh
R105C6H11O4PB   !   .ch(/c(//o)/oh)/ch2/ch2/ch2/ch2/o/oh
R106C4H7O4UB   !   .o/o/ch2/ch2/ch2/c(//o)/oh
R107C6H11O4PB   !   .ch2/ch(/o/oh)/ch2/ch2/ch2/c(//o)/oh
R108C6H11O4PB   !   .ch(/ch(/o/oh)/ch3)/ch2/ch2/c(//o)/oh
R109C6H11O4PB   !   .ch(/ch2/c(//o)/oh)/ch2/ch(/o/oh)/ch3
R110C6H11O4PB   !   .ch(/c(//o)/oh)/ch2/ch2/ch(/o/oh)/ch3
R111C3H5O4UB   !   .o/o/ch2/ch2/c(//o)/oh
R112C6H11O4PB   !   .ch(/ch3)/ch(/o/oh)/ch2/ch2/c(//o)/oh
R113C6H11O4PB   !   .ch2/ch2/ch(/o/oh)/ch2/ch2/c(//o)/oh
R114C6H11O4PB   !   .ch(/ch2/c(//o)/oh)/ch(/o/oh)/ch2/ch3
R115C6H11O4PB   !   .ch(/c(//o)/oh)/ch2/ch(/o/oh)/ch2/ch3
R116C6H11O4PB   !   .ch(/c(//o)/oh)/ch(/o/oh)/ch2/ch2/ch3
R117C6H11O4PB   !   .ch(/ch2/ch3)/ch(/o/oh)/ch2/c(//o)/oh
R118C6H11O4PB   !   .ch(/ch3)/ch2/ch(/o/oh)/ch2/c(//o)/oh
R119C6H11O4PB   !   .ch2/ch2/ch2/ch(/o/oh)/ch2/c(//o)/oh
R120C6H11O4PB   !   .ch(/ch(/o/oh)/c(//o)/oh)/ch2/ch2/ch3
R121C6H11O4PB   !   .ch(/ch2/ch3)/ch2/ch(/o/oh)/c(//o)/oh
R122C6H11O4PB   !   .ch(/ch3)/ch2/ch2/ch(/o/oh)/c(//o)/oh
R123C6H11O4PB   !   .ch2/ch2/ch2/ch2/ch(/o/oh)/c(//o)/oh
R124C3H7O4UP   !   .o/o/ch(/ch3)/ch2/o/oh
R125C3H7O4UP   !   .o/o/ch2/ch2/ch2/o/oh
R126C4H9O4UP   !   .o/o/ch(/ch2/o/oh)/ch2/ch3
R127C4H9O4UP   !   .o/o/ch(/ch3)/ch2/ch2/o/oh
R128C4H9O4UP   !   .o/o/ch2/ch2/ch2/ch2/o/oh
R129C5H11O4UP   !   .o/o/ch(/ch3)/ch(/o/oh)/ch2/ch3
R130C5H11O4UP   !   .o/o/ch2/ch2/ch(/o/oh)/ch2/ch3
R131C3H7O2P   !   .ch(/o/oh)/ch2/ch3
R132C5H11O4UP   !   .o/o/ch(/ch2/o/oh)/ch2/ch2/ch3
R133C5H11O4UP   !   .o/o/ch(/ch2/ch3)/ch2/ch2/o/oh
R134C5H11O4UP   !   .o/o/ch(/ch3)/ch2/ch2/ch2/o/oh
R135C5H11O4UP   !   .o/o/ch2/ch2/ch2/ch2/ch2/o/oh
R136C5H11O4UP   !   .o/o/ch2/ch(/o/oh)/ch2/ch2/ch3
R137C5H11O4UP   !   .o/o/ch(/ch2/ch3)/ch(/o/oh)/ch3
R138C5H11O4UP   !   .o/o/ch(/ch3)/ch2/ch(/o/oh)/ch3
R139C5H11O4UP   !   .o/o/ch2/ch2/ch2/ch(/o/oh)/ch3
R140C3H7O2P   !   .ch2/ch(/o/oh)/ch3
R141C6H11O5AUP   !   .o/o/ch(/ch2/o/oh)/ch2/ch2/ch2/ch//o
R142C6H11O3KP   !   .c(//o)/ch2/ch2/ch2/ch2/ch2/o/oh
R143C6H11O5AUP   !   .o/o/ch(/ch2/ch2/o/oh)/ch2/ch2/ch//o
R144C6H11O5AUP   !   .o/o/ch(/ch2/ch//o)/ch2/ch2/ch2/o/oh
R145C6H11O5AUP   !   .o/o/ch(/ch//o)/ch2/ch2/ch2/ch2/o/oh
R146C4H7O3AP   !   .ch(/ch2/o/oh)/ch2/ch//o
R147C4H7O3AP   !   .ch(/ch//o)/ch2/ch2/o/oh
R148C4H7O3KP   !   .c(//o)/ch2/ch2/ch2/o/oh
R149C6H11O5AUP   !   .o/o/ch2/ch(/o/oh)/ch2/ch2/ch2/ch//o
R150C6H11O5AUP   !   .o/o/ch(/ch(/o/oh)/ch3)/ch2/ch2/ch//o
R151C6H11O5AUP   !   .o/o/ch(/ch2/ch//o)/ch2/ch(/o/oh)/ch3
R152C6H11O5AUP   !   .o/o/ch(/ch//o)/ch2/ch2/ch(/o/oh)/ch3
R153C3H5O3AP   !   .ch(/ch//o)/ch2/o/oh
R154C3H5O3KP   !   .c(//o)/ch2/ch2/o/oh
R155C6H11O5AUP   !   .o/o/ch(/ch3)/ch(/o/oh)/ch2/ch2/ch//o
R156C6H11O5AUP   !   .o/o/ch2/ch2/ch(/o/oh)/ch2/ch2/ch//o
R157C4H7O3AP   !   .ch(/o/oh)/ch2/ch2/ch//o
R158C6H11O5AUP   !   .o/o/ch(/ch2/ch//o)/ch(/o/oh)/ch2/ch3
R159C6H11O5AUP   !   .o/o/ch(/ch//o)/ch2/ch(/o/oh)/ch2/ch3
R160C6H11O5AUP   !   .o/o/ch(/ch//o)/ch(/o/oh)/ch2/ch2/ch3
R161C6H11O5AUP   !   .o/o/ch(/ch2/ch3)/ch(/o/oh)/ch2/ch//o
R162C6H11O5AUP   !   .o/o/ch(/ch3)/ch2/ch(/o/oh)/ch2/ch//o
R163C3H5O3AP   !   .ch(/o/oh)/ch2/ch//o
R164C6H11O5AUP   !   .o/o/ch2/ch2/ch2/ch(/o/oh)/ch2/ch//o
R165C4H7O3AP   !   .ch2/ch(/o/oh)/ch2/ch//o
R166C5H11O2P   !   .ch(/o/oh)/ch2/ch2/ch2/ch3
R167C6H11O5AUP   !   .o/o/ch(/ch(/o/oh)/ch//o)/ch2/ch2/ch3
R168C6H11O5AUP   !   .o/o/ch(/ch2/ch3)/ch2/ch(/o/oh)/ch//o
R169C6H11O5AUP   !   .o/o/ch(/ch3)/ch2/ch2/ch(/o/oh)/ch//o
R170C3H5O3AP   !   .ch2/ch(/o/oh)/ch//o
R171C6H11O5AUP   !   .o/o/ch2/ch2/ch2/ch2/ch(/o/oh)/ch//o
R172C4H7O3AP   !   .ch2/ch2/ch(/o/oh)/ch//o
R173C6H11O6UPB   !   .o/o/ch(/ch2/o/oh)/ch2/ch2/ch2/c(//o)/oh
R174C6H11O6UPB   !   .o/o/ch(/ch2/ch2/o/oh)/ch2/ch2/c(//o)/oh
R175C6H11O6UPB   !   .o/o/ch(/ch2/c(//o)/oh)/ch2/ch2/ch2/o/oh
R176C6H11O6UPB   !   .o/o/ch(/c(//o)/oh)/ch2/ch2/ch2/ch2/o/oh
R177C4H7O4PB   !   .ch(/ch2/o/oh)/ch2/c(//o)/oh
R178C4H7O4PB   !   .ch(/c(//o)/oh)/ch2/ch2/o/oh
R179C6H11O6UPB   !   .o/o/ch2/ch(/o/oh)/ch2/ch2/ch2/c(//o)/oh
R180C6H11O6UPB   !   .o/o/ch(/ch(/o/oh)/ch3)/ch2/ch2/c(//o)/oh
R181C6H11O6UPB   !   .o/o/ch(/ch2/c(//o)/oh)/ch2/ch(/o/oh)/ch3
R182C6H11O6UPB   !   .o/o/ch(/c(//o)/oh)/ch2/ch2/ch(/o/oh)/ch3
R183C3H5O4PB   !   .ch(/c(//o)/oh)/ch2/o/oh
R184C6H11O6UPB   !   .o/o/ch(/ch3)/ch(/o/oh)/ch2/ch2/c(//o)/oh
R185C6H11O6UPB   !   .o/o/ch2/ch2/ch(/o/oh)/ch2/ch2/c(//o)/oh
R186C4H7O4PB   !   .ch(/o/oh)/ch2/ch2/c(//o)/oh
R187C6H11O6UPB   !   .o/o/ch(/ch2/c(//o)/oh)/ch(/o/oh)/ch2/ch3
R188C6H11O6UPB   !   .o/o/ch(/c(//o)/oh)/ch2/ch(/o/oh)/ch2/ch3
R189C6H11O6UPB   !   .o/o/ch(/c(//o)/oh)/ch(/o/oh)/ch2/ch2/ch3
R190C6H11O6UPB   !   .o/o/ch(/ch2/ch3)/ch(/o/oh)/ch2/c(//o)/oh
R191C6H11O6UPB   !   .o/o/ch(/ch3)/ch2/ch(/o/oh)/ch2/c(//o)/oh
R192C3H5O4PB   !   .ch(/o/oh)/ch2/c(//o)/oh
R193C6H11O6UPB   !   .o/o/ch2/ch2/ch2/ch(/o/oh)/ch2/c(//o)/oh
R194C4H7O4PB   !   .ch2/ch(/o/oh)/ch2/c(//o)/oh
R195C6H11O6UPB   !   .o/o/ch(/ch(/o/oh)/c(//o)/oh)/ch2/ch2/ch3
R196C6H11O6UPB   !   .o/o/ch(/ch2/ch3)/ch2/ch(/o/oh)/c(//o)/oh
R197C6H11O6UPB   !   .o/o/ch(/ch3)/ch2/ch2/ch(/o/oh)/c(//o)/oh
R198C3H5O4PB   !   .ch2/ch(/o/oh)/c(//o)/oh
R199C6H11O6UPB   !   .o/o/ch2/ch2/ch2/ch2/ch(/o/oh)/c(//o)/oh
R200C4H7O4PB   !   .ch2/ch2/ch(/o/oh)/c(//o)/oh
R201C3H7O4UP   !   .o/o/ch(/o/oh)/ch2/ch3
R202C3H7O4UP   !   .o/o/ch2/ch(/o/oh)/ch3
R203C3H7O2U   !   .o/o/ch(/ch3)2
R204C4H7O5AUP   !   .o/o/ch(/ch2/o/oh)/ch2/ch//o
R205C4H7O5AUP   !   .o/o/ch(/ch//o)/ch2/ch2/o/oh
R206C3H5O5AUP   !   .o/o/ch(/ch//o)/ch2/o/oh
R207C4H7O5AUP   !   .o/o/ch(/o/oh)/ch2/ch2/ch//o
R208C3H5O5AUP   !   .o/o/ch(/o/oh)/ch2/ch//o
R209C4H7O5AUP   !   .o/o/ch2/ch(/o/oh)/ch2/ch//o
R210C4H7O3AU   !   .o/o/ch(/ch3)/ch2/ch//o
R211C4H7O3KP   !   .c(//o)/ch2/ch(/o/oh)/ch3
R212C5H11O4UP   !   .o/o/ch(/o/oh)/ch2/ch2/ch2/ch3
R213C3H5O5AUP   !   .o/o/ch2/ch(/o/oh)/ch//o
R214C3H5O3AU   !   .o/o/ch(/ch3)/ch//o
R215C4H7O5AUP   !   .o/o/ch2/ch2/ch(/o/oh)/ch//o
R216C4H7O3AU   !   .o/o/ch(/ch//o)/ch2/ch3
R217C4H7O3KP   !   .c(//o)/ch(/o/oh)/ch2/ch3
R218C4H7O6UPB   !   .o/o/ch(/ch2/o/oh)/ch2/c(//o)/oh
R219C4H7O6UPB   !   .o/o/ch(/c(//o)/oh)/ch2/ch2/o/oh
R220C3H5O6UPB   !   .o/o/ch(/c(//o)/oh)/ch2/o/oh
R221C4H7O6UPB   !   .o/o/ch(/o/oh)/ch2/ch2/c(//o)/oh
R222C3H5O6UPB   !   .o/o/ch(/o/oh)/ch2/c(//o)/oh
R223C4H7O6UPB   !   .o/o/ch2/ch(/o/oh)/ch2/c(//o)/oh
R224C4H7O4UB   !   .o/o/ch(/ch3)/ch2/c(//o)/oh
R225C3H5O6UPB   !   .o/o/ch2/ch(/o/oh)/c(//o)/oh
R226C3H5O4UB   !   .o/o/ch(/ch3)/c(//o)/oh
R227C4H7O6UPB   !   .o/o/ch2/ch2/ch(/o/oh)/c(//o)/oh
R228C4H7O4UB   !   .o/o/ch(/c(//o)/oh)/ch2/ch3
R229C3H7   !   .ch(/ch3)2
R230C4H7O3AP   !   .ch(/ch//o)/ch(/o/oh)/ch3
R231C4H7OA   !   .ch(/ch3)/ch2/ch//o
R232C3H5O3KP   !   .c(//o)/ch(/o/oh)/ch3
R233C3H5OA   !   .ch(/ch3)/ch//o
R234C4H7O3AP   !   .ch(/ch3)/ch(/o/oh)/ch//o
R235C4H7OA   !   .ch(/ch//o)/ch2/ch3
R236C4H7O4PB   !   .ch(/c(//o)/oh)/ch(/o/oh)/ch3
R237C4H7O2B   !   .ch(/ch3)/ch2/c(//o)/oh
R238C3H5O2B   !   .ch(/ch3)/c(//o)/oh
R239C4H7O4PB   !   .ch(/ch3)/ch(/o/oh)/c(//o)/oh
R240C4H7O2B   !   .ch(/c(//o)/oh)/ch2/ch3
R241C4H7O5AUP   !   .o/o/ch(/ch//o)/ch(/o/oh)/ch3
R242C4H7O5AUP   !   .o/o/ch(/ch3)/ch(/o/oh)/ch//o
R243C4H7O6UPB   !   .o/o/ch(/c(//o)/oh)/ch(/o/oh)/ch3
R244C4H7O6UPB   !   .o/o/ch(/ch3)/ch(/o/oh)/c(//o)/oh
R245C5H9OA   !   .ch2/ch2/ch2/ch2/ch//o
R246C5H9O2B   !   .ch2/ch2/ch2/ch2/c(//o)/oh


!Added species
R290C6H11O3AU !ch3/ch2/ch2/ch2/ch2/c(/o/o(.))//o
R291C6H11O3AP !ch3/ch2/ch2/ch(.)/ch2/c(/o/oh)//o
R292C6H11O3AP !ch3/ch2/ch(.)/ch2/ch2/c(/o/oh)//o
R293C6H11O3AP !ch3/ch(.)/ch2/ch2/ch2/c(/o/oh)//o
R300C6H11O5APU !ch3/ch2/ch2/ch(/o/o(.))/ch2/c(/o/oh)//o
R301C6H11O5APU !ch3/ch2/ch(/o/o(.))/ch2/ch2/c(/o/oh)//o
R302C6H11O5APU !ch3/ch(/o/o(.))/ch2/ch2/ch2/c(/o/oh)//o
R305C6H11O5APP !ch3/ch(.)/ch2/ch(/o/oh)/ch2/c(/o/oh)//o
R306C6H11O5APP
R307C6H11O5APP
R310C6H11O7APPU !ch3/ch(/o/o(.))/ch2/ch(/o/oh)/ch2/c(/o/oh)//o
R311C6H11O7APPU
R312C6H11O7APPU
C6H8OK(OOH)2O !ch3/ch(/o/oh)/ch2/c(//o)/ch2/c(/o/oh)//o
C6H11OKOOH !ch3/ch2/ch2/ch2/ch2/c(/o/oh)//o
gcaprolac ! ch2(#1)/ch(/ch2/ch3)/o/c(//o)/ch2/1
dcaprolac ! ch2(#1)/ch(/ch3)/o/c(//o)/ch2/ch2/1
C6H12OOOHP !ch3/ch2/ch2/ch2/ch2/ch(/o/oh)/o(.)
HCOOOH !ch(//o)/o/oh
C6H11OKOH !ch3/ch2/ch2/ch2/ch2/ch(/oh)/o(.)
C6H11OKO ! ch3/ch2/ch2/ch2/ch2/c(//o)/o(.)
        """

structures = {}
for line in inputfile.splitlines():
    if '!' not in line: continue
    if not line.split('!')[0].strip():
        continue
    name, structure = (s.strip() for s in line.split('!'))
    structures[name]=structure
#  structure is a string... the last right column entry in my dictionary
#  structures is a dictionary
#  name is a string... the last name entry in my dictionary

raw_smiles = {}
for name, structure in structures.iteritems():
    s = structure
    s = re.sub('/?ch3', '[CH3]', s)
    s = re.sub('/?ch2', '[CH2]', s)
    s = re.sub('/?ch', '[CH]', s)
    s = re.sub('/?c', '[C]', s)
    s = s.replace('//o', '=O')
    s = re.sub('/?oh', '[OH]', s)
    s = re.sub('/?o', '[O]', s)
    s = re.sub('\(?\.\)?', '', s)
    s = re.sub('^h$', '[H]', s)
    s = s.replace('//', '#')  # if you still have a // by now it started as a ///
    if '(#1)' in s:
        assert '/1' in s
        s = s.replace('(#1)', '1').replace('/1', '1')


    def expander(match):
        """
        For use in regular expressions substitution.
        Accepts a Match object with two groups, first is the bracket to repeat,
        second is the number of times to repeat it.
        """
        number = int(match.group(2))  # how many times to repeat
        result = match.group(1) * number
        print "Expanding {} to {} in string {}".format(match.string[match.start():match.end()], result, match.string)
        return result


    s = re.sub('(\([^)]+\))(\d+)', expander, s)

    raw_smiles[name] = s
#  raw_smiles is a dictionary
#  s is a string... my converted smiles

smiless = {}
for name, smiles in raw_smiles.iteritems():
    try:
        molecule = Chem.MolFromSmiles(smiles) # turn it into an rdkit molecule
        smiles = Chem.MolToSmiles(molecule,True) # turn it back into a (canonical) smiles
    except:
        print "couldn't convert ", name, structures[name], smiles
    smiless[name] = smiles
    #print name, smiles

for name in sorted(smiless.keys()):
    smiles = smiless[name]
    print "{}\t{}\t! Confirmed by translating name automatically".format(name,smiles)