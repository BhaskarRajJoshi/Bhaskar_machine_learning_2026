# def solve_hanoi(disks, source, target, aux):
#     step = 0
#     # if disks == 1:
#     #     print(f'Moving disk {disks} from {source} to {target}')
#     if disks > 0:
#         step += solve_hanoi(disks-1,source,aux,target)
#         print(f'moving disk {disks} from {source} to {target}')
#         step +=1
#         step +=solve_hanoi(disks-1, aux,target,source)
#
#     return step
#
# print(solve_hanoi(4, 'A', 'C', 'B'))
#

# def solve_hanoi(disks,source='A',target='C', auxi='B'):
#     if disks == 1:
#         print(f'Moving disk {disks} from {source} to {target}')
#     elif disks == 2:
#         print(f'Moving disk 1 from {source} to {auxi}')
#         print(f'Moving disk 2 from {source} to {target}')
#         print(f'Moving disk 1 from {auxi} to {target}')
#     elif disks >2:
#         solve_hanoi(disks - 1, source, auxi, target)
#         print(f'Moving disk {disks} from {source} to {target}')
#         solve_hanoi(disks - 1, source, target, auxi)
#     return 1

def solve_hanoi(disks,source='A',target='C', auxi='B'):
    step =0
    if disks == 1:
        step +=1
        print(f'Moving disk {disks} from {source} to {target}')
    elif disks>1:
        step +=solve_hanoi(disks-1,source,auxi,target)
        print(f'Moving disks {disks} from {source} to {target}')
        step +=1
        step +=solve_hanoi(disks-1, auxi,target,source)
    return step





print(solve_hanoi(4))

