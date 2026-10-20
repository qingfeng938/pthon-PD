def parse_student(line):
    parts = line.strip().split(",")
    if len(parts) != 2:
        raise ValueError("字段数量不正确")
    name, score_str = parts
    if name == "":
        raise ValueError("姓名为空")
    score = int(score_str)
    if score < 0 or score > 100:
        raise ValueError("成绩超出 0~100 范围")
    return {"name": name, "score": score}