def solution(id_list, report, k):
    report_to_set = set(report)
    set_to_list = list(report_to_set)
    reported = []
    report_list = []
    for i in set_to_list:
        tokens = i.split()
        report_list.append(tokens)
        reported.append(tokens[1])

    stop_check = [0 for i in range(len(id_list))]
    for i in reported:
        stop_check[id_list.index(i)] += 1

    answer = [0 for i in range(len(id_list))]
    for i in report_list:
        if stop_check[id_list.index(i[1])] >= k:
            email_receiver = i[0]
            answer[id_list.index(email_receiver)] += 1

    return answer
