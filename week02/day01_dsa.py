items = [1, 2, 2, 3, 4, 4, 5, 5]
list_a = ["alex", "samira", "mike", "noor"]
list_b = ["mike", "noor", "omar", "alex"]
reports = [1, 2, 2, 3, 3, 3, 4]


def remove_duplicates(items):
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

def find_common_users(list_a, list_b):
    common_users = []
    for user in list_a:
        if user in list_b:
            common_users.append(user)
    return common_users

def count_reports(reports):
    report_count = {}
    for report in reports:
        if report in report_count:
            report_count[report] += 1
        else:
            report_count[report] = 1
    return report_count

unique_items = remove_duplicates(items)
common_users = find_common_users(list_a, list_b)
counted_reports = count_reports(reports)

print(f"Unique Items: {unique_items}")
print(f"Common Users: {common_users}")
print(f"Report Counts: {counted_reports}")