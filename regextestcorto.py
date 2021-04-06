import re
print(sum([int(x) for x in re.findall("[0-9]+",open("regex_sum_642069.txt").read())]))
#uso list comprehension per specificare come vadano generati gli elemeni della lista
#di int sfruttando il fatto che se f è un file handle posso usare f.read() per
#ottenere il contenuto del file e che f è il risultato di una assegnazione con open,
#quindi nemmeno mi serve salvare il file handle! Uso chiaramente inoltre le regex
