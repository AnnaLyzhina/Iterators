def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for item in sublist:
            yield item
