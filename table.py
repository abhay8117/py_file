for i in range(2,21):
    with open(f'table of  {i}.txt', 'w') as f:
        for j in range(1,11):
            #f.write(f'{i} x {j} = {i*j}\n')  This gives you one extra line in output
            f.write(f'{i} x {j} = {i*j}')
            if j!=10:
                f.write('\n')