def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [human_years,15,15]
    if human_years == 2:
        return [human_years,24,24]
    else:
        return [human_years,24+((human_years-2)*4),24+((human_years-2)*5)]


print(human_years_cat_years_dog_years(1), [1,15,15])
print(human_years_cat_years_dog_years(2), [2,24,24])
print(human_years_cat_years_dog_years(10), [10,56,64])