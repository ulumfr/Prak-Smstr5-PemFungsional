data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

def curried_converter(weeks):
    def inner_curried(days):
        def inner_inner_curried(hours):
            def final_curried(minutes):
                return weeks * 7 * 24 * 60 + days * 24 * 60 + hours * 60 + minutes
            return final_curried
        return inner_inner_curried
    return inner_curried

outputData = []
for item in data:
    parts = item.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])
    
    converted_value = curried_converter(weeks)(days)(hours)(minutes)
    outputData.append(converted_value)

print("OutputData = ", outputData)