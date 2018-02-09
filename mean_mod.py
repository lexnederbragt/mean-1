def makeavg(num_list):
    try:
        mean = sum(num_list)/len(num_list)
        if isinstance(mean, complex):
            return NotImplemented
        return mean
    except ZeroDivisionError as detail:
        msg = "\n Cannot compute the mean value of an empty list"
        raise ZeroDivisionError(detail.__str__() + msg)
    except TypeError as detail:
        msg = "\n Please pass a list of numbers, not strings"
        raise TypeError(detail.__str__() + msg)
