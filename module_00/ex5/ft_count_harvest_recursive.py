def ft_count_harvest_recursive() -> None:
    days_until = int(input("Days until harvest: "))

    def countdown(i: int) -> None:
        if i > days_until:
            print("Harvest time!")
            return
        print("Day", i)
        countdown(i + 1)
    countdown(1)
