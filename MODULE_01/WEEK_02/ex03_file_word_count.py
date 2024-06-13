def count_on_line(line):
    output_dict = {}
    list_words = line.split()
    for word in list_words:
        if word not in output_dict:
            output_dict[word] = 1
        else:
            output_dict[word] += 1

    return output_dict


def update_dict(old_dict, new_dict):
    cur_dict = old_dict
    for key in new_dict:
        if key not in cur_dict:
            cur_dict[key] = new_dict[key]
        else:
            cur_dict[key] += new_dict[key]

    return cur_dict


def word_count(file_path):
    output = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            new_dict = count_on_line(line=line.lower())
            old_dict = output
            output = update_dict(old_dict=old_dict, new_dict=new_dict)

    return output
