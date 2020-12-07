def count_any(groups: list[str]) -> int:
    return sum(
        len(set(''.join(group.split())))
        for group in groups
    )

def count_all(groups: list[str]) -> int:
    return sum(
        len(set.intersection(*map(set, group.splitlines())))
        for group in groups
    )


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        forms = f.read().split('\n\n')

    print('Q1:', 'For each group, count the number of questions to which',
          'anyone answered "yes". What is the sum of those counts?')
    print('A1:', count_any(forms))

    print('Q2:', 'For each group, count the number of questions to which',
          'everyone answered "yes". What is the sum of those counts?')
    print('A2:', count_all(forms))
