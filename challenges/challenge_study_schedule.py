def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    studing = 0
    for student in permanence_period:
        if type(student[0]) != int or type(student[1]) != int:
            return None

        interval = range(student[0], student[1] + 1)
        if target_time in interval:
            studing += 1
    return studing
