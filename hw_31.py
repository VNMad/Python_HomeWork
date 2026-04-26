#____________________________________________________________________
#1. Извлечение дат
#____________________________________________________________________
import re

text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline 28/02/2022."
dates = re.findall(r"\b\d{2}[./-]\d{2}[./-]\d{4}\b", text)

for date in dates:
    print(date)

#____________________________________________________________________
#2. Разделение списка тегов
#____________________________________________________________________
import re

tag_input = "python, data-science / machine-learning; AI neural-networks"
print(sorted(set(t.lower() for t in re.split(r"[,\s;/]+", tag_input) if t)))
