# ستون CSV
def parse_csv(path: str):
    with open(path,'r') as file:
        for row in file:
           row = row.strip().split(",")
           yield row

def calculate_sums(path_file: str) -> None:
        result = ''
        rows = list(parse_csv(path_file))
        for row in rows:
            row = list(map(int,row))
            row.append(sum(row))
            result += f"{', '.join(map(str,row))}\n"
        with open('result.csv','w') as newFile:
            newFile.write(result)
path = './2/1.csv'
calculate_sums(path)